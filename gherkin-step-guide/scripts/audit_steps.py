#!/usr/bin/env python3
"""Audit Gherkin step definition files for coverage and organization.

Delegates step matching to the actual BDD framework via dry-run, so it uses
the same matching logic your tests use. Supports Behave (via uvx) and
Cucumber-js (via npx).

Checks:
- Unused step files: step definition files not matched by any .feature file.
- Missing step definitions: steps in .feature files with no matching def.
- Near-duplicate files: step files with similar names (consolidation candidates).
- Statistics: total files, matched vs. unused, coverage.

Usage:
  audit_steps.py features/
  audit_steps.py features/ --framework behave
  audit_steps.py features/ --framework cucumber-js

Exit code 0 on pass, 1 on any finding.
"""

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from difflib import SequenceMatcher
from pathlib import Path

SIMILARITY_THRESHOLD = 0.75

STEP_FILE_EXTENSIONS: dict[str, list[str]] = {
    "behave": [".py"],
    "cucumber-js": [".js", ".ts", ".mjs", ".cjs"],
}

STEP_DIR_NAMES = {"given", "when", "then"}


# ---------------------------------------------------------------------------
# Framework detection
# ---------------------------------------------------------------------------


def _detect_framework(project_dir: str) -> str | None:
    """Auto-detect framework from project structure and files."""
    project = Path(project_dir)

    # Check for Behave markers
    env_file = project / "environment.py"
    if env_file.exists():
        return "behave"

    steps_dir = project / "steps"
    if steps_dir.is_dir():
        for f in steps_dir.rglob("*"):
            if f.suffix == ".py":
                return "behave"
            if f.suffix in (".js", ".ts", ".mjs", ".cjs"):
                return "cucumber-js"

    # Check for config files
    for name in ("cucumber.js", "cucumber.cjs", "cucumber.mjs", "cucumber.yml"):
        if (project.parent / name).exists() or (project / name).exists():
            return "cucumber-js"

    # Check for package.json with cucumber dependency
    pkg = project.parent / "package.json"
    if pkg.exists():
        try:
            content = pkg.read_text()
            if "cucumber" in content.lower():
                return "cucumber-js"
        except OSError:
            pass

    return None


# ---------------------------------------------------------------------------
# Framework dry-run
# ---------------------------------------------------------------------------

_STEPS_INIT_CONTENT = """\
import glob
import importlib.util
import os

_steps_dir = os.path.dirname(__file__)
for _subdir in ("given", "when", "then"):
    _subdir_path = os.path.join(_steps_dir, _subdir)
    if not os.path.isdir(_subdir_path):
        continue
    for _filepath in sorted(glob.glob(os.path.join(_subdir_path, "*.py"))):
        _basename = os.path.basename(_filepath)
        if _basename.startswith("_"):
            continue
        _spec = importlib.util.spec_from_file_location(_basename[:-3], _filepath)
        _mod = importlib.util.module_from_spec(_spec)
        _spec.loader.exec_module(_mod)
"""


def _ensure_steps_init(features_dir: str) -> list[str]:
    """Ensure __init__.py files exist for subdirectory step discovery.

    Creates __init__.py in features/steps/ and each keyword subdirectory
    so Behave can discover step modules. Returns list of created paths
    (for cleanup).
    """
    steps_dir = Path(features_dir) / "steps"
    if not steps_dir.is_dir():
        return []

    created: list[str] = []

    # Root steps __init__.py — auto-imports subdirectories
    root_init = steps_dir / "__init__.py"
    if not root_init.exists() or root_init.stat().st_size == 0:
        root_init.write_text(_STEPS_INIT_CONTENT)
        created.append(str(root_init))

    # Keyword subdirectory __init__.py files
    for subdir in steps_dir.iterdir():
        if subdir.is_dir() and subdir.name in STEP_DIR_NAMES:
            sub_init = subdir / "__init__.py"
            if not sub_init.exists():
                sub_init.write_text("")
                created.append(str(sub_init))

    return created


def _run_behave_dry_run(features_dir: str) -> dict:
    """Run behave --dry-run and return parsed JSON output."""
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as tmp:
        tmp_path = tmp.name

    # Ensure steps subdirectories are discoverable
    created_inits = _ensure_steps_init(features_dir)

    try:
        result = subprocess.run(
            [
                "uvx",
                "behave",
                "--dry-run",
                "--format",
                "json",
                "--outfile",
                tmp_path,
                "--no-summary",
                features_dir,
            ],
            capture_output=True,
            text=True,
            timeout=120,
        )

        if not Path(tmp_path).exists() or Path(tmp_path).stat().st_size == 0:
            stderr = result.stderr.strip()
            if "No steps directory" in stderr or "ConfigError" in stderr:
                print(f"Behave configuration error: {stderr}")
                return {"features": [], "error": stderr}
            print(f"Behave produced no output. stderr: {stderr}")
            return {"features": [], "error": stderr}

        with open(tmp_path) as f:
            data = json.load(f)

        return {"features": data, "error": None}
    except FileNotFoundError:
        return {
            "features": [],
            "error": "uvx not found. Install uv: https://docs.astral.sh/uv/",
        }
    except subprocess.TimeoutExpired:
        return {"features": [], "error": "Behave dry-run timed out after 120s."}
    except json.JSONDecodeError as e:
        return {"features": [], "error": f"Failed to parse Behave JSON output: {e}"}
    finally:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        for init_path in created_inits:
            try:
                os.unlink(init_path)
            except OSError:
                pass


def _run_cucumber_dry_run(features_dir: str) -> dict:
    """Run cucumber-js --dry-run and return parsed JSON output."""
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as tmp:
        tmp_path = tmp.name

    try:
        result = subprocess.run(
            [
                "npx",
                "--yes",
                "@cucumber/cucumber",
                "--dry-run",
                "--format",
                f"json:{tmp_path}",
                features_dir,
            ],
            capture_output=True,
            text=True,
            timeout=120,
        )

        if not Path(tmp_path).exists() or Path(tmp_path).stat().st_size == 0:
            stderr = result.stderr.strip()
            print(f"Cucumber produced no output. stderr: {stderr}")
            return {"features": [], "error": stderr}

        with open(tmp_path) as f:
            data = json.load(f)

        return {"features": data, "error": None}
    except FileNotFoundError:
        return {
            "features": [],
            "error": "npx not found. Install Node.js: https://nodejs.org/",
        }
    except subprocess.TimeoutExpired:
        return {"features": [], "error": "Cucumber dry-run timed out after 120s."}
    except json.JSONDecodeError as e:
        return {"features": [], "error": f"Failed to parse Cucumber JSON output: {e}"}
    finally:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass


# ---------------------------------------------------------------------------
# JSON parsing
# ---------------------------------------------------------------------------


def _extract_matches(features_json: list[dict]) -> tuple[set[str], list[str]]:
    """Extract matched step files and undefined steps from dry-run JSON.

    Returns (matched_files, undefined_steps).
    """
    matched_files: set[str] = set()
    undefined_steps: list[str] = []

    for feature in features_json:
        for element in feature.get("elements", []):
            for step in element.get("steps", []):
                match = step.get("match")
                if match and "location" in match:
                    loc = match["location"]
                    # location format: "path/to/file.py:line"
                    file_path = loc.rsplit(":", 1)[0]
                    matched_files.add(file_path)
                elif not match:
                    step_loc = step.get("location", "unknown")
                    keyword = step.get("keyword", "").strip()
                    name = step.get("name", "")
                    undefined_steps.append(f"{keyword} {name}  ({step_loc})")

    return matched_files, undefined_steps


# ---------------------------------------------------------------------------
# Step file discovery
# ---------------------------------------------------------------------------


def _find_step_files(features_dir: str, framework: str) -> list[str]:
    """Find all step definition files on disk."""
    valid_exts = set(STEP_FILE_EXTENSIONS.get(framework, [".py"]))
    features_path = Path(features_dir)

    # Look for steps in the standard locations
    step_dirs = []
    for candidate in [
        features_path / "steps",
        features_path.parent / "steps",
        features_path / "step_definitions",
        features_path.parent / "step_definitions",
    ]:
        if candidate.is_dir():
            step_dirs.append(candidate)

    if not step_dirs:
        return []

    step_files: list[str] = []
    for step_dir in step_dirs:
        for f in step_dir.rglob("*"):
            if f.is_file() and f.suffix in valid_exts:
                # Skip __init__.py, environment.py, conftest.py, hooks files
                if f.name in ("__init__.py", "environment.py", "conftest.py"):
                    continue
                if "hooks" in f.name.lower():
                    continue
                step_files.append(str(f))

    return sorted(step_files)


# ---------------------------------------------------------------------------
# Near-duplicate detection
# ---------------------------------------------------------------------------


def _normalize_filename(name: str) -> str:
    """Normalize a step filename for similarity comparison."""
    # Remove extension, convert to lowercase
    stem = Path(name).stem.lower()
    # Remove common prefixes/suffixes
    stem = re.sub(r"^(step_|the_|a_|an_)", "", stem)
    return stem


def _find_near_duplicate_files(
    step_files: list[str],
) -> list[tuple[str, str, float]]:
    """Find pairs of step files with similar names."""
    duplicates: list[tuple[str, str, float]] = []
    names = [_normalize_filename(f) for f in step_files]

    for i in range(len(step_files)):
        for j in range(i + 1, len(step_files)):
            if names[i] == names[j]:
                duplicates.append((step_files[i], step_files[j], 1.0))
            else:
                ratio = SequenceMatcher(None, names[i], names[j]).ratio()
                if ratio >= SIMILARITY_THRESHOLD:
                    duplicates.append((step_files[i], step_files[j], ratio))

    return duplicates


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------


def _print_section(title: str, items: list[str]) -> None:
    """Print a titled section of the report."""
    print(f"\n  [{title}]")
    if not items:
        print("    (none)")
    else:
        for item in items:
            print(f"    {item}")


def audit(features_dir: str, framework: str | None = None) -> int:
    """Run the full audit and print a report. Returns 0 on pass, 1 on findings."""

    # Auto-detect framework if needed
    if not framework:
        framework = _detect_framework(features_dir)
        if not framework:
            print(
                "Could not auto-detect BDD framework. Use --framework to specify one."
            )
            return 1
        print(f"Auto-detected framework: {framework}")

    # Run framework dry-run
    print(f"Running {framework} dry-run...")
    if framework == "behave":
        result = _run_behave_dry_run(features_dir)
    elif framework == "cucumber-js":
        result = _run_cucumber_dry_run(features_dir)
    else:
        print(f"Unsupported framework: {framework}")
        return 1

    if result["error"]:
        print(f"Warning: {result['error']}")

    features_json = result["features"]

    # Extract matches from JSON
    matched_files, undefined_steps = _extract_matches(features_json)

    # Find all step files on disk
    all_step_files = _find_step_files(features_dir, framework)

    # Normalize all paths to absolute for comparison
    matched_normalized = {os.path.normpath(os.path.abspath(f)) for f in matched_files}
    all_normalized = {os.path.normpath(os.path.abspath(f)) for f in all_step_files}

    # Unused step files (on disk but not matched)
    unused_files = sorted(all_normalized - matched_normalized)

    # Near-duplicate detection
    near_dupes = _find_near_duplicate_files(all_step_files)

    # Report
    print("\n--- Step Definition Audit Report ---")
    print(f"Framework: {framework}")
    print(f"Step files on disk: {len(all_step_files)}")
    print(f"Step files matched: {len(matched_normalized & all_normalized)}")

    findings: list[str] = []

    # Missing step definitions
    _print_section("Missing step definitions", undefined_steps)
    if undefined_steps:
        findings.extend(f"MISSING: {s}" for s in undefined_steps)

    # Unused step files
    unused_msgs = [str(f) for f in unused_files]
    _print_section("Unused step files", unused_msgs)
    if unused_msgs:
        findings.extend(f"UNUSED: {u}" for u in unused_msgs)

    # Near-duplicate files
    dup_messages: list[str] = []
    for f1, f2, ratio in near_dupes:
        pct = int(ratio * 100)
        dup_messages.append(
            f"{pct}% similar:\n      {Path(f1).name}\n      {Path(f2).name}"
        )
    _print_section("Near-duplicate step files", dup_messages)
    if dup_messages:
        findings.extend(f"DUPLICATE: {d}" for d in dup_messages)

    # Statistics
    print("\n  [Statistics]")
    if all_step_files:
        utilization = (
            len(matched_normalized & all_normalized) / len(all_step_files) * 100
        )
        print(f"    Step file utilization: {utilization:.0f}%")

    # Check keyword directory structure
    keyword_dirs_found: dict[str, int] = {}
    for f in all_step_files:
        parent = Path(f).parent.name.lower()
        if parent in STEP_DIR_NAMES:
            keyword_dirs_found[parent] = keyword_dirs_found.get(parent, 0) + 1
        else:
            findings.append(
                f"ORGANIZATION: {f} is not in a keyword directory "
                f"(given/, when/, or then/)"
            )

    if keyword_dirs_found:
        print("    Steps by keyword directory:")
        for kw in ("given", "when", "then"):
            count = keyword_dirs_found.get(kw, 0)
            print(f"      {kw}/: {count} file(s)")

    # Count feature steps
    total_feature_steps = 0
    for feature in features_json:
        for element in feature.get("elements", []):
            total_feature_steps += len(element.get("steps", []))

    if total_feature_steps:
        matched_count = total_feature_steps - len(undefined_steps)
        coverage = matched_count / total_feature_steps * 100
        print(
            f"    Feature step coverage: {coverage:.0f}% "
            f"({matched_count}/{total_feature_steps} steps matched)"
        )

    # Summary
    print("\n--- Summary ---")
    if not findings:
        print("PASS: No issues found.")
    else:
        print(f"FINDINGS: {len(findings)} issue(s) detected.")
        if undefined_steps:
            print(f"  - {len(undefined_steps)} missing step definition(s)")
        if unused_msgs:
            print(f"  - {len(unused_msgs)} unused step file(s)")
        if dup_messages:
            print(f"  - {len(dup_messages)} near-duplicate pair(s)")
        org_issues = [f for f in findings if f.startswith("ORGANIZATION:")]
        if org_issues:
            print(f"  - {len(org_issues)} file(s) not in keyword directories")

    return 0 if not findings else 1


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Audit Gherkin step definition files for coverage and organization."
    )
    parser.add_argument(
        "features_dir",
        help="Path to the features directory.",
    )
    parser.add_argument(
        "--framework",
        choices=list(STEP_FILE_EXTENSIONS.keys()),
        default=None,
        help="BDD framework (auto-detected if not specified).",
    )
    args = parser.parse_args()

    try:
        exit_code = audit(args.features_dir, args.framework)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    sys.exit(exit_code)
