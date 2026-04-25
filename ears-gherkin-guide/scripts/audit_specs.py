#!/usr/bin/env python3
import argparse
import re
import sys
from typing import Any


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
            current_rule = {
                "title": rule_match.group(1).strip(),
                "description": [],
                "scenarios": [],
                "ears_count": 0,
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
                    current_rule["ears_count"] += 1

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

        # Check 1-to-1 requirement constraint
        if rule["ears_count"] == 0:
            errors.append(
                f"{rule_prefix} Missing EARS requirement in description (must contain 'shall')."
            )
        elif rule["ears_count"] > 1:
            errors.append(
                f"{rule_prefix} Multiple EARS requirements found ({rule['ears_count']}). "
                "Each Rule must contain exactly one."
            )
        else:
            successes.append(f"{rule_prefix} Valid EARS requirement found.")

        # Check scenario coverage
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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Audit Gherkin feature files for EARS requirement mapping."
    )
    parser.add_argument("file", help="Path to the .feature file to audit")
    args = parser.parse_args()

    try:
        sys.exit(audit_feature_file(args.file))
    except Exception as e:
        print(f"Error auditing file: {e}")
        sys.exit(1)
