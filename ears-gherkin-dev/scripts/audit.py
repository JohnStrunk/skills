#!/usr/bin/env python3
"""Audit Gherkin feature files and step definitions.

Combines spec-level EARS compliance checks with step definition coverage
and organization audits into a single script.

Spec checks (from .feature files):
- Every Rule title contains exactly one "shall" (no more, no fewer).
- Rule titles do not use wrong obligation keywords (should, may, will, must).
- Rule titles do not contain vague or unmeasurable language.
- EARS structural keywords (If/While/When/Where) are used correctly.
- Rule titles use explicit system names (no pronouns like "it").
- The freeform description below a Rule title does not contain additional
  EARS requirements.
- Every Rule has at least one Scenario.
- No Scenarios exist outside of a Rule block.

Step checks (via framework dry-run):
- Unused step files: step definition files not matched by any .feature file.
- Missing step definitions: steps in .feature files with no matching def.
- Near-duplicate files: step files with similar names (consolidation candidates).
- Multi-step files: files containing more than one step definition.
- Step file naming: step files not named after their step pattern.
- Statistics: total files, matched vs. unused, coverage.

Usage:
  audit.py <path-to-.feature-file>
  audit.py <directory>
  audit.py file1.feature dir/ file2.feature
  audit.py features/ --steps-only --framework behave

Exit code 0 on pass, 1 on any audit error or finding.
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
from typing import Any

# ---------------------------------------------------------------------------
# Spec audit constants
# ---------------------------------------------------------------------------

VAGUE_TERMS: dict[str, list[str]] = {
    "vague adverb": [
        "quickly",
        "slowly",
        "efficiently",
        "properly",
        "reasonably",
        "approximately",
        "usually",
        "typically",
        "generally",
        "soon",
        "eventually",
        "immediately",
    ],
    "unmeasurable adjective": [
        "user-friendly",
        "flexible",
        "intuitive",
        "robust",
        "scalable",
        "efficient",
        "seamless",
        "responsive",
        "reliable",
        "powerful",
        "smart",
        "easy-to-use",
    ],
    "vague quantifier": [
        "various",
        "some",
        "any",
        "many",
        "few",
        "several",
        "most",
        "a lot",
    ],
    "escape clause": [
        "as appropriate",
        "if possible",
        "as needed",
        "where practical",
        "to the extent feasible",
        "if necessary",
        "when applicable",
    ],
    "continuation term": [
        "etc.",
        "and so on",
        "and/or",
        "such as",
        "for example",
    ],
    "indefinite temporal term": [
        "timely",
        "in a timely manner",
        "in real time",
        "promptly",
        "without delay",
        "as soon as possible",
        "periodic",
    ],
}

WRONG_OBLIGATION_KEYWORDS: list[str] = ["should", "may", "will", "must"]

PRONOUNS_BEFORE_SHALL: list[str] = ["it", "they", "he", "she", "we", "you"]

# ---------------------------------------------------------------------------
# Step audit constants
# ---------------------------------------------------------------------------

SIMILARITY_THRESHOLD = 0.90

NAMING_SIMILARITY_THRESHOLD = 0.50

# Word-level antonym / qualifier pairs that legitimately distinguish
# two otherwise-identical step filenames.
_ANTONYM_PAIRS: list[tuple[str, str]] = [
    ("not", ""),
    ("no", ""),
    ("should", "should_not"),
    ("is", "is_not"),
    ("exists", "not_exist"),
    ("valid", "invalid"),
    ("expired", "valid"),
    ("accepts", "rejects"),
    ("include", "exclude"),
    ("includes", "excludes"),
    ("contain", "not_contain"),
    ("contains", "not_contain"),
    ("with", "without"),
    ("a", "an"),
    ("singular", "plural"),
    ("again", ""),
    ("llm", "mcp"),
    ("get", "post"),
    ("get", "delete"),
    ("post", "put"),
    ("post", "delete"),
    ("delete", "put"),
    ("create", "delete"),
    ("eslint", "markdownlint"),
    ("eslint", "yamllint"),
    ("markdownlint", "yamllint"),
    ("dependency", "dev_dependency"),
    ("fields", "methods"),
    ("field", "method"),
    ("select", "delete"),
    ("sleep", "wake"),
    ("key", "url"),
    ("be", "equal"),
    ("row", "rows"),
    ("n", "zero"),
    ("n", ""),
    ("has", "should"),
    ("has", "stored"),
    ("has", "is"),
    ("has", "with"),
    ("stored", "should"),
    ("been", "be"),
    ("been", ""),
    ("dev", ""),
    ("valid", ""),
    ("idea", ""),
    ("lint", "eslint"),
    ("on", ""),
    ("k8s", ""),
    ("config", ""),
    ("staged", ""),
    ("arbitrary", ""),
    ("problem", ""),
    ("statement", ""),
    ("artifact", ""),
    ("workspace", ""),
]

STEP_FILE_EXTENSIONS: dict[str, list[str]] = {
    "behave": [".py"],
    "cucumber-js": [".js", ".ts", ".mjs", ".cjs"],
}

STEP_DIR_NAMES = {"given", "when", "then"}

HOOK_KEYWORDS = frozenset(
    {
        "Before",
        "After",
        "BeforeAll",
        "AfterAll",
        "BeforeStep",
        "AfterStep",
    }
)


_CI = os.environ.get("GITHUB_ACTIONS") == "true"


def _gh_annotation(
    level: str, message: str, file: str | None = None, line: int | None = None
) -> None:
    """Emit a GitHub Actions workflow command annotation."""
    if not _CI:
        return
    params: list[str] = []
    if file:
        params.append(f"file={file}")
    if line:
        params.append(f"line={line}")
    param_str = " " + ",".join(params) if params else ""
    print(f"::{level}{param_str}::{message}")


# ---------------------------------------------------------------------------
# Spec audit functions
# ---------------------------------------------------------------------------


def _find_wrong_obligation_keywords(title: str) -> list[str]:
    """Find non-standard obligation keywords in a Rule title."""
    pattern = r"\b(" + "|".join(WRONG_OBLIGATION_KEYWORDS) + r")\b"
    return [m.lower() for m in re.findall(pattern, title, re.IGNORECASE)]


def _find_vague_terms(title: str) -> list[tuple[str, str]]:
    """Find vague or unmeasurable language in a Rule title.

    Returns (term, category) pairs.
    """
    found: list[tuple[str, str]] = []
    for category, terms in VAGUE_TERMS.items():
        for term in terms:
            escaped = re.escape(term)
            if term.endswith("."):
                pattern = r"\b" + escaped
            else:
                pattern = r"\b" + escaped + r"\b"
            if re.search(pattern, title, re.IGNORECASE):
                found.append((term, category))
    return found


def _check_ears_pattern_structure(title: str) -> list[str]:
    """Check EARS structural keyword usage in a Rule title."""
    errors: list[str] = []
    lower = title.lower()

    if re.match(r"\s*if\b", lower):
        shall_pos = lower.find("shall")
        then_match = re.search(r"\bthen\b", lower)
        then_pos = then_match.start() if then_match else -1
        if shall_pos != -1 and (then_pos == -1 or then_pos > shall_pos):
            errors.append(
                "EARS 'If' pattern requires 'then' before 'shall' "
                "(template: If <condition>, then the <system> shall <response>)."
            )

    for keyword in ["while", "when", "where"]:
        if re.match(r"\s*" + keyword + r"\b", lower):
            keyword_end = lower.index(keyword) + len(keyword)
            before_shall = lower[: lower.find("shall")] if "shall" in lower else lower
            if "," not in before_shall[keyword_end:]:
                errors.append(
                    f"EARS '{keyword.capitalize()}' clause should be followed by a comma "
                    f"before the system name (template: {keyword.capitalize()} <clause>, "
                    f"the <system> shall <response>)."
                )
            break

    return errors


def _check_missing_system_name(title: str) -> list[str]:
    """Check for pronouns used instead of an explicit system name."""
    errors: list[str] = []
    pattern = r"\b(" + "|".join(PRONOUNS_BEFORE_SHALL) + r")\s+shall\b"
    match = re.search(pattern, title, re.IGNORECASE)
    if match:
        pronoun = match.group(1).lower()
        errors.append(
            f"Pronoun '{pronoun}' found before 'shall' — use an explicit system name."
        )
    return errors


def audit_feature_file(file_path: str) -> int:
    """Audit a Gherkin feature file for EARS requirement mapping."""
    with open(file_path) as f:
        lines = f.readlines()

    rules: list[dict[str, Any]] = []
    current_rule: dict[str, Any] | None = None
    scenarios_outside_rules: list[str] = []

    # Simple state machine to parse Gherkin structure
    # This is a lightweight parser that focuses on Rules and Scenarios

    in_rule_description = False

    # EARS detection regex
    # Matches strings containing 'shall' and common EARS structures
    ears_pattern = re.compile(r"\bshall\b", re.IGNORECASE)

    # Line types
    rule_re = re.compile(r"^\s*Rule:\s*(.*)", re.IGNORECASE)
    scenario_re = re.compile(
        r"^\s*(Scenario Outline|Scenario Template|Scenario|Example):\s*(.*)",
        re.IGNORECASE,
    )

    for line_num, line in enumerate(lines, start=1):
        rule_match = rule_re.match(line)
        scenario_match = scenario_re.match(line)

        if rule_match:
            title = rule_match.group(1).strip()
            current_rule = {
                "title": title,
                "line": line_num,
                "shall_count": len(ears_pattern.findall(title)),
                "description": [],
                "scenarios": [],
                "description_ears_count": 0,
            }
            rules.append(current_rule)
            in_rule_description = True
            continue

        if scenario_match:
            scenario_title = scenario_match.group(2).strip()
            if current_rule:
                current_rule["scenarios"].append(scenario_title)
            else:
                scenarios_outside_rules.append(scenario_title)
            in_rule_description = False
            continue

        # Capture description lines
        if in_rule_description and current_rule:
            # Avoid capturing empty lines or lines that start with Gherkin keywords
            clean_line = line.strip()
            if clean_line and not any(
                clean_line.startswith(kw)
                for kw in [
                    "Given",
                    "When",
                    "Then",
                    "And",
                    "But",
                    "*",
                    "@",
                    "#",
                    "Background:",
                    "Examples:",
                    "Scenarios:",
                    "|",
                ]
            ):
                current_rule["description"].append(clean_line)
                if ears_pattern.search(clean_line):
                    current_rule["description_ears_count"] += 1

    # Reporting — (message, line_number_or_None) tuples
    errors: list[tuple[str, int | None]] = []
    successes: list[str] = []

    if scenarios_outside_rules:
        errors.append(
            (
                f"Found {len(scenarios_outside_rules)} scenarios outside of any Rule block: "
                f"{', '.join(scenarios_outside_rules)}",
                None,
            )
        )

    for rule in rules:
        rule_prefix = f"Rule '{rule['title']}':"
        rule_line: int = rule["line"]

        if rule["shall_count"] == 0:
            errors.append(
                (
                    f"{rule_prefix} Rule title must be an EARS requirement "
                    "(must contain 'shall').",
                    rule_line,
                )
            )
        elif rule["shall_count"] > 1:
            errors.append(
                (
                    f"{rule_prefix} Rule title contains {rule['shall_count']} "
                    "occurrences of 'shall'. EARS requirements must be atomic "
                    "— use exactly one 'shall' per Rule.",
                    rule_line,
                )
            )
        else:
            successes.append(f"{rule_prefix} Valid EARS requirement in title.")

        wrong_kws = _find_wrong_obligation_keywords(rule["title"])
        if wrong_kws:
            kw_list = ", ".join(sorted(set(wrong_kws)))
            errors.append(
                (
                    f"{rule_prefix} Rule title uses non-standard obligation "
                    f"keyword(s): {kw_list}. Use 'shall' for mandatory requirements.",
                    rule_line,
                )
            )

        vague_found = _find_vague_terms(rule["title"])
        for term, category in vague_found:
            errors.append(
                (
                    f"{rule_prefix} Rule title contains vague language: "
                    f"'{term}' ({category}). Replace with a specific, "
                    "measurable value.",
                    rule_line,
                )
            )

        for err in _check_ears_pattern_structure(rule["title"]):
            errors.append((f"{rule_prefix} {err}", rule_line))

        for err in _check_missing_system_name(rule["title"]):
            errors.append((f"{rule_prefix} {err}", rule_line))

        if rule["description_ears_count"] > 0:
            errors.append(
                (
                    f"{rule_prefix} Description contains "
                    f"{rule['description_ears_count']} EARS requirement(s). "
                    "Additional requirements must not appear in the "
                    "description — move each to its own Rule title.",
                    rule_line,
                )
            )

        if not rule["scenarios"]:
            errors.append(
                (
                    f"{rule_prefix} No scenarios found under this rule.",
                    rule_line,
                )
            )
        else:
            successes.append(
                f"{rule_prefix} {len(rule['scenarios'])} scenario(s) found."
            )

    # Final Output
    print(f"--- Audit Report for {file_path} ---")
    if not errors:
        print(
            "PASS: Specification follows EARS-Gherkin 1-to-1 mapping and has coverage."
        )
    else:
        print("FAIL: Specification has audit errors.")
        for msg, line_no in errors:
            print(f"  [ERROR] {msg}")
            _gh_annotation("error", msg, file_path, line_no)

    print("\nSummary of findings:")
    for succ in successes:
        print(f"  [OK] {succ}")

    return 0 if not errors else 1


def _resolve_feature_files(paths: list[str]) -> list[str]:
    """Expand paths into a sorted list of .feature file paths."""
    files: list[str] = []
    for p in paths:
        path = Path(p)
        if path.is_file():
            files.append(str(path))
        elif path.is_dir():
            files.extend(sorted(str(f) for f in path.rglob("*.feature")))
        else:
            print(f"Warning: '{p}' does not exist, skipping.")
    return files


# ---------------------------------------------------------------------------
# Step audit: Framework detection
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
# Step audit: Framework dry-run
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

    # Root steps __init__.py -- auto-imports subdirectories
    root_init = steps_dir / "__init__.py"
    if not root_init.exists():
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
    """Run cucumber-js --dry-run and return parsed JSON output.

    Uses the project-local cucumber-js so the project's config, step
    definitions, and support modules are available.  If the local binary
    is missing (e.g. node_modules not installed), returns a skippable
    error with remediation advice.
    """
    # Prefer the project-local binary so the project's cucumber config
    # (requireModule, require globs, etc.) is honoured.
    try:
        check = subprocess.run(
            ["npx", "cucumber-js", "--version"],
            capture_output=True,
            text=True,
            timeout=30,
        )
    except subprocess.TimeoutExpired:
        return {
            "features": [],
            "error": "cucumber-js version check timed out after 30s.",
        }
    if check.returncode != 0:
        return {
            "features": [],
            "error": (
                "cucumber-js is not installed locally. "
                "Step definition audit requires the project's own "
                "cucumber-js so that its configuration and step "
                "definitions are available.\n"
                "  Fix: run `npm install` (or `npm ci`) in the "
                "project root, then re-run the audit."
            ),
        }

    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as tmp:
        tmp_path = tmp.name

    try:
        # Don't pass features_dir as a positional arg — let the project's
        # cucumber config (cucumber.js / cucumber.cjs) control the feature
        # paths.  Passing an extra path merges with the config and can
        # pick up stray .feature files in node_modules or other directories.
        result = subprocess.run(
            [
                "npx",
                "cucumber-js",
                "--dry-run",
                "--format",
                f"json:{tmp_path}",
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
# Step audit: JSON parsing
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
                keyword = step.get("keyword", "").strip()
                if keyword in HOOK_KEYWORDS:
                    continue
                match = step.get("match")
                if match and "location" in match:
                    loc = match["location"]
                    # location format: "path/to/file.py:line"
                    file_path = loc.rsplit(":", 1)[0]
                    matched_files.add(file_path)
                elif not match:
                    step_loc = step.get("location", "unknown")
                    name = step.get("name", "")
                    undefined_steps.append(f"{keyword} {name}  ({step_loc})")

    return matched_files, undefined_steps


# ---------------------------------------------------------------------------
# Step audit: Step file discovery
# ---------------------------------------------------------------------------


def _find_step_files(features_dir: str, framework: str) -> list[str]:
    """Find all step definition files on disk."""
    valid_exts = set(STEP_FILE_EXTENSIONS.get(framework, [".py"]))
    features_path = Path(features_dir)

    # Look for steps in the standard locations.  When the caller passes
    # the project root (.) rather than the features/ directory itself,
    # we also need to check features/steps and features/step_definitions.
    step_dirs = []
    for candidate in [
        features_path / "steps",
        features_path / "step_definitions",
        features_path / "features" / "steps",
        features_path / "features" / "step_definitions",
        features_path.parent / "steps",
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
                if f.stem.lower() in ("hooks", "before_hooks", "after_hooks"):
                    continue
                # Skip files in support directories
                if "support" in f.parts:
                    continue
                step_files.append(str(f))

    return sorted(step_files)


# ---------------------------------------------------------------------------
# Step audit: Near-duplicate detection
# ---------------------------------------------------------------------------


def _normalize_filename(name: str) -> str:
    """Normalize a step filename for similarity comparison."""
    # Remove extension, convert to lowercase
    stem = Path(name).stem.lower()
    # Remove common prefixes/suffixes
    stem = re.sub(r"^(step_|the_|a_|an_)", "", stem)
    return stem


def _differs_by_antonym(name_a: str, name_b: str) -> bool:
    """Check if two normalized names differ only by known antonym pairs."""
    words_a = set(name_a.split("_"))
    words_b = set(name_b.split("_"))
    remaining = (words_a - words_b) | (words_b - words_a)
    if not remaining:
        return True
    for w1, w2 in _ANTONYM_PAIRS:
        pair = {w1, w2} - {""}
        if pair and pair <= remaining:
            remaining -= pair
            if not remaining:
                return True
    return False


def _find_near_duplicate_files(
    step_files: list[str],
) -> list[tuple[str, str, float]]:
    """Find pairs of step files with similar names."""
    duplicates: list[tuple[str, str, float]] = []
    names = [_normalize_filename(f) for f in step_files]

    for i in range(len(step_files)):
        for j in range(i + 1, len(step_files)):
            if names[i] == names[j]:
                if not _differs_by_antonym(names[i], names[j]):
                    duplicates.append((step_files[i], step_files[j], 1.0))
            else:
                ratio = SequenceMatcher(None, names[i], names[j]).ratio()
                if ratio >= SIMILARITY_THRESHOLD:
                    if not _differs_by_antonym(names[i], names[j]):
                        duplicates.append((step_files[i], step_files[j], ratio))

    return duplicates


# ---------------------------------------------------------------------------
# Step audit: Multi-step file detection
# ---------------------------------------------------------------------------


def _check_multi_step_files(
    features_json: list[dict],
) -> list[tuple[str, list[str]]]:
    """Detect files containing more than one step definition.

    Uses dry-run JSON match locations to group steps by source line.
    A parameterized step definition matched by multiple step texts still
    maps to a single source line, so it is correctly counted as one step.
    Returns list of (file_path, [step_texts]) for offending files.
    """
    file_lines: dict[str, dict[str, str]] = {}
    for feature in features_json:
        for element in feature.get("elements", []):
            for step in element.get("steps", []):
                match = step.get("match")
                if match and "location" in match:
                    loc = match["location"]
                    parts = loc.rsplit(":", 1)
                    file_path = parts[0]
                    line = parts[1] if len(parts) > 1 else "0"
                    if file_path not in file_lines:
                        file_lines[file_path] = {}
                    if line not in file_lines[file_path]:
                        keyword = step.get("keyword", "").strip()
                        name = step.get("name", "")
                        file_lines[file_path][line] = f"{keyword} {name}"

    return [
        (fp, list(lines.values())) for fp, lines in file_lines.items() if len(lines) > 1
    ]


# ---------------------------------------------------------------------------
# Step audit: Step file naming check
# ---------------------------------------------------------------------------


def _split_camel_case(text: str) -> str:
    """Insert spaces before uppercase letters in camelCase words."""
    return re.sub(r"([a-z])([A-Z])", r"\1 \2", text)


def _stem_word(word: str) -> str:
    """Naive English stemming — strip common suffixes."""
    for suffix in (
        "tion",
        "sion",
        "ing",
        "ment",
        "ness",
        "ally",
        "ous",
        "ive",
        "ful",
        "less",
        "able",
        "ible",
    ):
        if word.endswith(suffix) and len(word) > len(suffix) + 2:
            return word[: -len(suffix)]
    if word.endswith("ly") and len(word) > 4:
        return word[:-2]
    if word.endswith("ed") and len(word) > 4:
        return word[:-2]
    if word.endswith("es") and len(word) > 4:
        return word[:-2]
    if word.endswith("s") and len(word) > 3 and not word.endswith("ss"):
        return word[:-1]
    return word


def _step_text_to_words(step_text: str) -> set[str]:
    """Extract lowercase stemmed words from step text."""
    expanded = _split_camel_case(step_text)
    cleaned = re.sub(r"[^a-zA-Z0-9\s]", " ", expanded)
    return {_stem_word(w.lower()) for w in cleaned.split() if len(w) > 1}


_NAMING_STOP_WORDS = frozenset(
    {
        "a",
        "an",
        "the",
        "is",
        "be",
        "to",
        "of",
        "in",
        "on",
        "at",
        "by",
        "for",
        "it",
        "its",
        "has",
        "have",
        "had",
        "are",
        "was",
        "that",
        "this",
        "with",
    }
)


def _check_step_file_naming(
    features_json: list[dict],
) -> list[tuple[str, str, str]]:
    """Check that step files are named after their step pattern.

    Uses word-overlap: the filename's words should be a reasonable
    subset of the step text's words plus feature-level context words.
    Returns list of (actual_file, actual_stem, step_text) for mismatches.
    """
    findings: list[tuple[str, str, str]] = []
    seen_files: set[str] = set()

    for feature in features_json:
        feature_uri = feature.get("uri", "")
        feature_context = {
            _stem_word(w)
            for w in re.sub(r"[^a-zA-Z]", " ", Path(feature_uri).stem).lower().split()
            if len(w) > 1
        } - _NAMING_STOP_WORDS

        for element in feature.get("elements", []):
            for step in element.get("steps", []):
                match = step.get("match")
                if match and "location" in match:
                    loc = match["location"]
                    file_path = loc.rsplit(":", 1)[0]
                    if file_path in seen_files:
                        continue
                    seen_files.add(file_path)

                    name = step.get("name", "")
                    step_words = (
                        _step_text_to_words(name) | feature_context
                    ) - _NAMING_STOP_WORDS
                    file_words = {
                        _stem_word(w)
                        for w in Path(file_path).stem.lower().split("_")
                        if len(w) > 1
                    } - _NAMING_STOP_WORDS
                    if not file_words or not step_words:
                        continue

                    overlap = len(file_words & step_words) / len(file_words)
                    if overlap < NAMING_SIMILARITY_THRESHOLD:
                        findings.append((file_path, Path(file_path).stem, name))

    return findings


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


# ---------------------------------------------------------------------------
# Combined audit
# ---------------------------------------------------------------------------


def audit(
    paths: list[str],
    *,
    specs_only: bool = False,
    steps_only: bool = False,
    framework: str | None = None,
) -> int:
    """Run the full audit and print a report. Returns 0 on pass, 1 on findings."""
    exit_code = 0

    # --- Spec audit ---
    if not steps_only:
        feature_files = _resolve_feature_files(paths)

        if not feature_files:
            print("No .feature files found.")
            exit_code = 1
        else:
            total_errors = 0
            for fpath in feature_files:
                try:
                    total_errors += audit_feature_file(fpath)
                except (OSError, UnicodeDecodeError) as e:
                    print(f"Error auditing {fpath}: {e}")
                    total_errors += 1

            if len(feature_files) > 1:
                print(f"\n--- Summary: {len(feature_files)} file(s) audited ---")
                if total_errors == 0:
                    print("All files passed.")
                else:
                    print(f"{total_errors} file(s) had errors.")

            if total_errors > 0:
                exit_code = 1

    # --- Step audit ---
    if not specs_only:
        # Use the first path as the features directory for step audit
        features_dir = paths[0] if paths else "."

        # Auto-detect framework if needed
        fw = framework
        if not fw:
            fw = _detect_framework(features_dir)
            if not fw:
                print(
                    "Could not auto-detect BDD framework. "
                    "Use --framework to specify one."
                )
                return 1
            print(f"Auto-detected framework: {fw}")

        # Run framework dry-run
        print(f"Running {fw} dry-run...")
        if fw == "behave":
            result = _run_behave_dry_run(features_dir)
        elif fw == "cucumber-js":
            result = _run_cucumber_dry_run(features_dir)
        else:
            print(f"Unsupported framework: {fw}")
            return 1

        if result["error"]:
            print(f"Warning: {result['error']}")

        features_json = result["features"]

        # Extract matches from JSON
        matched_files, undefined_steps = _extract_matches(features_json)

        # Find all step files on disk
        all_step_files = _find_step_files(features_dir, fw)

        # Normalize all paths to absolute for comparison
        matched_normalized = {
            os.path.normpath(os.path.abspath(f)) for f in matched_files
        }
        all_normalized = {os.path.normpath(os.path.abspath(f)) for f in all_step_files}

        # Unused step files (on disk but not matched)
        unused_files = sorted(all_normalized - matched_normalized)

        # Near-duplicate detection
        near_dupes = _find_near_duplicate_files(all_step_files)

        # Multi-step file detection
        multi_step = _check_multi_step_files(features_json)

        # Step file naming check
        naming_issues = _check_step_file_naming(features_json)

        # Report
        print("\n--- Step Definition Audit Report ---")
        print(f"Framework: {fw}")
        print(f"Step files on disk: {len(all_step_files)}")
        print(f"Step files matched: {len(matched_normalized & all_normalized)}")

        errors: list[str] = []
        warnings: list[str] = []

        # Missing step definitions
        _print_section("Missing step definitions", undefined_steps)
        for s in undefined_steps:
            errors.append(f"MISSING: {s}")
            loc_match = re.search(r"\((.+):(\d+)\)$", s)
            if loc_match:
                _gh_annotation(
                    "error",
                    f"Missing step definition: {s}",
                    loc_match.group(1),
                    int(loc_match.group(2)),
                )
            else:
                _gh_annotation("error", f"Missing step definition: {s}")

        # Unused step files
        unused_msgs = [str(f) for f in unused_files]
        _print_section("Unused step files", unused_msgs)
        for u in unused_msgs:
            errors.append(f"UNUSED: {u}")
            _gh_annotation("error", "Unused step file", u)

        # Near-duplicate files (warning only — similar names are expected
        # for related-but-distinct steps)
        dup_messages: list[str] = []
        for f1, f2, ratio in near_dupes:
            pct = int(ratio * 100)
            dup_messages.append(
                f"{pct}% similar:\n      {Path(f1).name}\n      {Path(f2).name}"
            )
            _gh_annotation(
                "warning", f"Near-duplicate ({pct}% similar to {Path(f2).name})", f1
            )
        _print_section("Near-duplicate step files (warning)", dup_messages)
        if dup_messages:
            warnings.extend(f"DUPLICATE: {d}" for d in dup_messages)

        # Multi-step files
        multi_messages: list[str] = []
        for fp, steps in multi_step:
            step_list = ", ".join(steps)
            multi_messages.append(f"{fp}: {step_list}")
            _gh_annotation("error", f"Multi-step file (contains: {step_list})", fp)
        _print_section("Multi-step files", multi_messages)
        if multi_messages:
            errors.extend(f"MULTI-STEP: {m}" for m in multi_messages)

        # Step file naming (warning only — filename words should overlap
        # with the step text words)
        naming_messages: list[str] = []
        for actual_file, actual_stem, step_text in naming_issues:
            naming_messages.append(
                f'{actual_file}: filename={actual_stem}, step="{step_text}"'
            )
            _gh_annotation(
                "warning",
                f'Step file naming: "{actual_stem}" doesn\'t match step "{step_text}"',
                actual_file,
            )
        _print_section("Step file naming (warning)", naming_messages)
        if naming_messages:
            warnings.extend(f"NAMING: {n}" for n in naming_messages)

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
                msg = (
                    f"ORGANIZATION: {f} is not in a keyword directory "
                    f"(given/, when/, or then/)"
                )
                errors.append(msg)
                _gh_annotation(
                    "error", "Not in a keyword directory (given/, when/, or then/)", f
                )

        if keyword_dirs_found:
            print("    Steps by keyword directory:")
            for kw in ("given", "when", "then"):
                count = keyword_dirs_found.get(kw, 0)
                print(f"      {kw}/: {count} file(s)")

        # Count feature steps (excluding hooks)
        total_feature_steps = 0
        for feature in features_json:
            for element in feature.get("elements", []):
                for step in element.get("steps", []):
                    if step.get("keyword", "").strip() not in HOOK_KEYWORDS:
                        total_feature_steps += 1

        if total_feature_steps:
            matched_count = total_feature_steps - len(undefined_steps)
            coverage = matched_count / total_feature_steps * 100
            print(
                f"    Feature step coverage: {coverage:.0f}% "
                f"({matched_count}/{total_feature_steps} steps matched)"
            )

        # Summary
        print("\n--- Summary ---")
        if not errors and not warnings:
            print("PASS: No issues found.")
        else:
            if errors:
                print(f"ERRORS: {len(errors)} issue(s) detected.")
                if undefined_steps:
                    print(f"  - {len(undefined_steps)} missing step definition(s)")
                if unused_msgs:
                    print(f"  - {len(unused_msgs)} unused step file(s)")
                if multi_messages:
                    print(f"  - {len(multi_messages)} multi-step file(s)")
                org_issues = [e for e in errors if e.startswith("ORGANIZATION:")]
                if org_issues:
                    print(f"  - {len(org_issues)} file(s) not in keyword directories")
            if warnings:
                print(f"WARNINGS: {len(warnings)} informational issue(s).")
                if dup_messages:
                    print(f"  - {len(dup_messages)} near-duplicate pair(s)")
                if naming_messages:
                    print(f"  - {len(naming_messages)} step file naming issue(s)")
            if not errors:
                print("PASS: No blocking issues found.")

        if errors:
            exit_code = 1

    return exit_code


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Audit Gherkin feature files and step definitions."
    )
    parser.add_argument(
        "paths",
        nargs="+",
        help="Path(s) to .feature file(s) or director(ies) to audit. "
        "Directories are searched recursively for .feature files.",
    )
    parser.add_argument(
        "--specs-only",
        action="store_true",
        default=False,
        help="Only run spec (EARS compliance) audit.",
    )
    parser.add_argument(
        "--steps-only",
        action="store_true",
        default=False,
        help="Only run step definition audit.",
    )
    parser.add_argument(
        "--framework",
        choices=list(STEP_FILE_EXTENSIONS.keys()),
        default=None,
        help="BDD framework (auto-detected if not specified).",
    )
    args = parser.parse_args()

    try:
        result_code = audit(
            args.paths,
            specs_only=args.specs_only,
            steps_only=args.steps_only,
            framework=args.framework,
        )
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    sys.exit(result_code)
