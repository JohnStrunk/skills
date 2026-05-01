#!/usr/bin/env python3
"""Audit Gherkin .feature files for EARS requirement compliance.

Checks:
- Every Rule title contains exactly one "shall" (no more, no fewer).
- Rule titles do not use wrong obligation keywords (should, may, will, must).
- Rule titles do not contain vague or unmeasurable language.
- EARS structural keywords (If/While/When/Where) are used correctly.
- Rule titles use explicit system names (no pronouns like "it").
- The freeform description below a Rule title does not contain additional
  EARS requirements.
- Every Rule has at least one Scenario.
- No Scenarios exist outside of a Rule block.

Usage:
  audit_specs.py <path-to-.feature-file>
  audit_specs.py <directory>                # audit all .feature files recursively
  audit_specs.py file1.feature dir/ file2.feature

Exit code 0 on pass, 1 on any audit error.
"""

import argparse
import re
import sys
from pathlib import Path
from typing import Any

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
        then_pos = lower.find("then")
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
    with open(file_path, "r") as f:
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
        r"^\s*(Scenario|Example|Scenario Outline):\s*(.*)", re.IGNORECASE
    )

    for line in lines:
        rule_match = rule_re.match(line)
        scenario_match = scenario_re.match(line)

        if rule_match:
            title = rule_match.group(1).strip()
            current_rule = {
                "title": title,
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
                ]
            ):
                current_rule["description"].append(clean_line)
                if ears_pattern.search(clean_line):
                    current_rule["description_ears_count"] += 1

    # Reporting
    errors: list[str] = []
    successes: list[str] = []

    if scenarios_outside_rules:
        errors.append(
            f"Found {len(scenarios_outside_rules)} scenarios outside of any Rule block: "
            f"{', '.join(scenarios_outside_rules)}"
        )

    for rule in rules:
        rule_prefix = f"Rule '{rule['title']}':"

        if rule["shall_count"] == 0:
            errors.append(
                f"{rule_prefix} Rule title must be an EARS requirement "
                "(must contain 'shall')."
            )
        elif rule["shall_count"] > 1:
            errors.append(
                f"{rule_prefix} Rule title contains {rule['shall_count']} "
                "occurrences of 'shall'. EARS requirements must be atomic "
                "— use exactly one 'shall' per Rule."
            )
        else:
            successes.append(f"{rule_prefix} Valid EARS requirement in title.")

        wrong_kws = _find_wrong_obligation_keywords(rule["title"])
        if wrong_kws:
            kw_list = ", ".join(sorted(set(wrong_kws)))
            errors.append(
                f"{rule_prefix} Rule title uses non-standard obligation "
                f"keyword(s): {kw_list}. Use 'shall' for mandatory requirements."
            )

        vague_found = _find_vague_terms(rule["title"])
        for term, category in vague_found:
            errors.append(
                f"{rule_prefix} Rule title contains vague language: "
                f"'{term}' ({category}). Replace with a specific, "
                "measurable value."
            )

        for err in _check_ears_pattern_structure(rule["title"]):
            errors.append(f"{rule_prefix} {err}")

        for err in _check_missing_system_name(rule["title"]):
            errors.append(f"{rule_prefix} {err}")

        if rule["description_ears_count"] > 0:
            errors.append(
                f"{rule_prefix} Description contains "
                f"{rule['description_ears_count']} EARS requirement(s). "
                "Additional requirements must not appear in the "
                "description — move each to its own Rule title."
            )

        if not rule["scenarios"]:
            errors.append(f"{rule_prefix} No scenarios found under this rule.")
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
        for err in errors:
            print(f"  [ERROR] {err}")

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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Audit Gherkin feature files for EARS requirement mapping."
    )
    parser.add_argument(
        "paths",
        nargs="+",
        help="Path(s) to .feature file(s) or director(ies) to audit. "
        "Directories are searched recursively for .feature files.",
    )
    args = parser.parse_args()

    feature_files = _resolve_feature_files(args.paths)

    if not feature_files:
        print("No .feature files found.")
        sys.exit(1)

    total_errors = 0
    for fpath in feature_files:
        try:
            total_errors += audit_feature_file(fpath)
        except Exception as e:
            print(f"Error auditing {fpath}: {e}")
            total_errors += 1

    if len(feature_files) > 1:
        print(f"\n--- Summary: {len(feature_files)} file(s) audited ---")
        if total_errors == 0:
            print("All files passed.")
        else:
            print(f"{total_errors} file(s) had errors.")

    sys.exit(0 if total_errors == 0 else 1)
