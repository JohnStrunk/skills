# ears-gherkin-dev Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use
> superpowers:subagent-driven-development (recommended) or
> superpowers:executing-plans to implement this plan task-by-task.
> Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Merge `ears-gherkin-guide` and `gherkin-step-guide` into a
single `ears-gherkin-dev` skill with strict Red/Green TDD workflow,
consolidated reference files, and a merged audit script.

**Architecture:** One skill directory with a lean SKILL.md (~150 lines)
defining the strict TDD workflow, 4 consolidated reference files, and
one merged audit script. The two old skill directories are deleted.

**Tech Stack:** Markdown (skill + references), Python (audit script),
Gherkin/BDD (the subject matter — framework-agnostic)

**Markdown linting:** All `.md` files must pass `markdownlint` with
the config at `.github/markdownlint-config.yaml`. Key rules: 80-char
line limit (except code blocks and tables), ATX headings, fenced code
blocks must have a language tag. After writing any `.md` file, run
`pre-commit run --files <file>` to verify.

---

## File Map

### Created

<!-- markdownlint-disable MD013 -->

| File | Responsibility |
| :--- | :--- |
| `ears-gherkin-dev/SKILL.md` | Skill frontmatter + strict TDD workflow |
| `ears-gherkin-dev/reference/ears-requirements.md` | Merged EARS patterns, anti-patterns, quality |
| `ears-gherkin-dev/reference/gherkin-scenarios.md` | Scenario writing (existing + property-based testing) |
| `ears-gherkin-dev/reference/step-definitions.md` | Merged step best practices, anti-patterns, organization |
| `ears-gherkin-dev/reference/auditing.md` | Audit script documentation |
| `ears-gherkin-dev/scripts/audit.py` | Merged spec + step audit script |

<!-- markdownlint-enable MD013 -->

### Deleted

| Path | Reason |
| :--- | :--- |
| `ears-gherkin-guide/` | Replaced by `ears-gherkin-dev/` |
| `gherkin-step-guide/` | Replaced by `ears-gherkin-dev/` |

### Modified

| File | Change |
| :--- | :--- |
| `skills-todo.md` | Mark "Spec-driven development" as done |

---

## Task 1: Create directory structure and SKILL.md

**Files:**

- Create: `ears-gherkin-dev/SKILL.md`
- Create: `ears-gherkin-dev/reference/` (directory)
- Create: `ears-gherkin-dev/scripts/` (directory)

- [ ] **Step 1: Create directories**

```bash
mkdir -p ears-gherkin-dev/reference ears-gherkin-dev/scripts
```

- [ ] **Step 2: Write SKILL.md**

Write `ears-gherkin-dev/SKILL.md` with the following content:

````markdown
---
name: ears-gherkin-dev
description: >
  Drives development through EARS requirements and Gherkin scenarios
  using strict Red/Green TDD. Use this skill for ANY code change that
  affects system behavior — new features, bug fixes, handling unwanted
  behavior, and responding to review feedback. Every behavior change
  must be covered by an EARS requirement and verified by Gherkin
  scenarios before implementation begins.
---

# EARS-Gherkin Development

You are an expert Requirements Engineer and BDD Practitioner. Your
goal is to help the user build and maintain a comprehensive,
verifiable, and executable specification of their software system
using **EARS (Easy Approach to Requirements Syntax)** and **Gherkin**.

Every change to system behavior — new features, bug fixes, handling
unwanted behavior, and responding to review feedback — follows the
same strict Red/Green TDD workflow below.

## Reference Material

The `reference/` directory contains detailed guidance you MUST consult
during each phase of the workflow:

- `reference/ears-requirements.md` — EARS pattern definitions,
  anti-patterns, elicitation techniques, validation criteria, and
  quality checklist.
- `reference/gherkin-scenarios.md` — Scenario writing best practices,
  declarative style, Scenario Outlines, EARS-to-scenario mapping,
  property-based testing, and common anti-patterns.
- `reference/step-definitions.md` — Step definition writing,
  parameterization, one-step-per-file organization, support layer
  patterns, and framework-specific conventions.
- `reference/auditing.md` — What the audit script checks, how to
  read its output, and how to fix common findings.

## Workflow

This workflow is mandatory for every behavior change. Follow the steps
in order. Do not skip steps.

### 1. Understand the Change

Read the request, bug report, or review feedback. Identify what
behavior is changing and why. If the request is vague, ask clarifying
questions — consult `reference/ears-requirements.md` for elicitation
techniques.

### 2. Write or Update the EARS Requirement

Formulate or revise the EARS requirement that governs this behavior.
Consult `reference/ears-requirements.md` for pattern selection,
anti-patterns, and quality criteria.

- Place the requirement as a `Rule:` title in the appropriate
  `.feature` file (see "Locating Feature Files" below).
- One `Rule:` block per EARS requirement — the title IS the
  requirement.
- Each requirement must contain exactly one "shall."

### 3. Write Failing Scenario(s)

Write Gherkin scenarios under that Rule that demonstrate the desired
behavior. Consult `reference/gherkin-scenarios.md`.

- For **bug fixes**, write a scenario that reproduces the bug.
- For **new features**, write scenarios covering the happy path and
  key boundary conditions.
- For **unwanted behavior**, write scenarios that trigger the
  unwanted condition and verify the response.
- Prefer **property-based testing** over example-only testing where
  practical for broader coverage.
- Scenarios must be **declarative**, not imperative.

### 4. Run and Confirm RED

Execute the scenarios and confirm they fail. This proves the test is
actually testing something new. If the scenarios pass before any code
change, either the test is wrong or the behavior already exists.

### 5. Write or Update Step Definitions

Implement step definition files for any new or changed steps. Consult
`reference/step-definitions.md`.

- **One step definition per file.**
- **File named after its one step** in snake_case (e.g., a step
  `the shopping cart is empty` lives in
  `the_shopping_cart_is_empty.py`).
- Organize files in keyword directories: `given/`, `when/`, `then/`.
- Step bodies delegate to a support layer — no raw selectors, SQL,
  or HTTP calls in step definitions.

### 6. Implement the Code

Write the minimum code to make the scenarios pass.

### 7. Run and Confirm GREEN

Execute the scenarios and confirm they all pass.

### 8. Audit

Run the audit script against the features directory:

```bash
python scripts/audit.py features/
```

Consult `reference/auditing.md` for interpreting results. Fix all
findings before considering the work complete.

## Locating Feature Files

Before writing any Gherkin, determine whether the requirement belongs
in an existing feature file or requires a new one.

1. **Scan existing files**: List all `.feature` files in `features/`.
   Read each file's `Feature:` title, description, and `Rule:` titles
   to understand its scope.
2. **Match by scope**: A requirement belongs in an existing file when
   it falls within that file's stated feature scope.
3. **Decide**:
   - **Modify existing file** — Add a new `Rule:` block when a
     matching feature file exists.
   - **Create new file** — Only when no existing file's scope covers
     the requirement. Use the naming pattern
     `NNNN-short-name.feature` with the next sequential number.

When in doubt, prefer modifying an existing file.

## Key Rules

- One EARS requirement per `Rule:` block — the Rule title IS the
  requirement.
- One step definition per file — file named in snake_case after the
  step pattern.
- Scenarios are declarative, not imperative.
- Property-based testing preferred over example-only testing where
  practical.
- Proactively audit after every change — do not wait to be asked.
````

- [ ] **Step 3: Lint the SKILL.md**

```bash
pre-commit run --files ears-gherkin-dev/SKILL.md
```

Fix any lint errors before proceeding.

- [ ] **Step 4: Commit**

```bash
git add ears-gherkin-dev/SKILL.md
git commit -m "Add ears-gherkin-dev SKILL.md with strict TDD workflow"
```

---

## Task 2: Create consolidated ears-requirements.md

**Files:**

- Create: `ears-gherkin-dev/reference/ears-requirements.md`
- Source: `ears-gherkin-guide/reference/ears-patterns.md`
- Source: `ears-gherkin-guide/reference/ears-anti-patterns.md`
- Source: `ears-gherkin-guide/reference/requirements-quality.md`

This file merges three source files into one. The structure below
shows the exact heading hierarchy and where each section's content
comes from.

- [ ] **Step 1: Write ears-requirements.md**

Write `ears-gherkin-dev/reference/ears-requirements.md` with this
structure:

```markdown
# EARS Requirements — Comprehensive Reference
```

Then the following sections, in order. For each section, copy the
content from the source file indicated. Do not change the content
unless noted. Ensure all lines comply with the 80-character limit.

**Section structure:**

<!-- markdownlint-disable MD013 -->

| Heading | Source |
| :--- | :--- |
| `## The General EARS Syntax` | `ears-patterns.md` "The General EARS Syntax" |
| `## Pattern 1: Ubiquitous` | `ears-patterns.md` "Pattern 1: Ubiquitous" |
| `## Pattern 2: Event-Driven` | `ears-patterns.md` "Pattern 2: Event-Driven" |
| `## Pattern 3: State-Driven` | `ears-patterns.md` "Pattern 3: State-Driven" |
| `## Pattern 4: Unwanted Behavior` | `ears-patterns.md` "Pattern 4: Unwanted Behavior" |
| `## Pattern 5: Optional Feature` | `ears-patterns.md` "Pattern 5: Optional Feature" |
| `## Pattern 6: Complex (Combined Patterns)` | `ears-patterns.md` "Pattern 6: Complex" (all subsections) |
| `## Pattern Selection Decision Tree` | `ears-patterns.md` "Pattern Selection Decision Tree" |
| `## EARS Keywords and Obligation Levels` | `ears-patterns.md` "EARS Keywords and Obligation Levels" |
| `## Decomposing Complex Requirements` | `ears-patterns.md` "Decomposing Complex Requirements" |
| `## EARS-to-Gherkin Structural Mapping` | `ears-patterns.md` "EARS-to-Gherkin Structural Mapping" |
| `## NFR Patterns` | `ears-patterns.md` "NFR Patterns" |
| `## Domain-Specific Examples` | `ears-patterns.md` "Domain-Specific Examples" |
| `## Anti-Patterns` | New heading |
| `### The Eight Defects EARS Prevents` | `ears-anti-patterns.md` "The Eight Defects EARS Prevents" |
| `### Anti-Pattern 1–10` | `ears-anti-patterns.md` anti-patterns 1–10 (all, as `###` subheadings under `## Anti-Patterns`) |
| `### Before-and-After Transformations` | `ears-anti-patterns.md` "Before-and-After Transformations" |
| `### Words and Phrases to Eliminate` | `ears-anti-patterns.md` content from anti-pattern 5 "Words and Phrases to Eliminate" subsection (extract to stand alone here, remove from anti-pattern 5 to avoid duplication) |
| `## Elicitation and Validation` | New heading |
| `### Active Elicitation` | `requirements-quality.md` "Active Elicitation" |
| `### Characteristics of a Well-Formed Requirement` | `requirements-quality.md` "Characteristics of a Well-Formed Requirement" |
| `### The Testability Principle` | `requirements-quality.md` "The Testability Principle" (includes Verification Methods and SMART subsections) |
| `### Elicitation Questions by Requirement Type` | `requirements-quality.md` "Elicitation Questions by Requirement Type" |
| `### Decomposition Strategy` | `requirements-quality.md` "Decomposition Strategy" |
| `### Common User Phrases and Their EARS Translations` | `requirements-quality.md` "Common User Phrases and Their EARS Translations" |
| `### Validating Against the User's Intent` | `requirements-quality.md` "Validating Against the User's Intent" |
| `## Quality Checklist` | `ears-anti-patterns.md` "Quality Checklist" (single consolidated checklist — this is the authoritative copy) |

<!-- markdownlint-enable MD013 -->

- [ ] **Step 2: Lint**

```bash
pre-commit run --files ears-gherkin-dev/reference/ears-requirements.md
```

Fix any lint errors.

- [ ] **Step 3: Commit**

```bash
git add ears-gherkin-dev/reference/ears-requirements.md
git commit -m "Add consolidated ears-requirements.md reference"
```

---

## Task 3: Create updated gherkin-scenarios.md

**Files:**

- Create: `ears-gherkin-dev/reference/gherkin-scenarios.md`
- Source: `ears-gherkin-guide/reference/gherkin-scenarios.md`

Copy the existing file and add a new "Property-Based Testing" section
after the "Scenario Outlines" section.

- [ ] **Step 1: Copy existing file**

```bash
cp ears-gherkin-guide/reference/gherkin-scenarios.md \
   ears-gherkin-dev/reference/gherkin-scenarios.md
```

- [ ] **Step 2: Add Property-Based Testing section**

Insert the following section after the "Scenario Outlines" section
(after the "Bad Example — Different Behaviors Forced Into an Outline"
subsection, before "Background Blocks"):

````markdown
---

## Property-Based Testing

Where practical, use property-based testing to provide broader
coverage than example-only scenarios. Instead of checking specific
input-output pairs, property-based tests verify that a property or
invariant holds across many inputs.

### When to Use

- The requirement states a general rule that should hold for any
  valid input (e.g., "all passwords must be at least 8 characters")
- Boundary conditions are numerous or non-obvious
- The behavior is mathematical or algorithmic (sorting, filtering,
  calculations)
- Example-based testing would require many rows to cover the input
  space adequately

### When NOT to Use

- The behavior is inherently example-driven (specific error messages
  for specific inputs)
- The number of valid inputs is small and enumerable
- The property is harder to express than the examples

### Expressing Properties in Gherkin

Use Scenario Outlines with generated or representative data, and
write Then steps that assert properties rather than exact values:

```gherkin
Rule: When the user submits a search query, the search service shall return only results matching the query.

  Scenario Outline: Search results match the query term
    Given the product catalog contains diverse products
    When the user searches for "<query>"
    Then every result should contain "<query>" in its name
      or description
    And no result should be unrelated to "<query>"

    Examples: Representative queries across categories
      | query       |
      | headphones  |
      | running     |
      | organic     |
      | bluetooth   |
      | waterproof  |
```

### Property Assertions in Step Definitions

The Then step asserts a **property** (every result matches) rather
than a **specific value** (result #1 is "Sony Headphones"). The step
definition should:

1. Retrieve the full result set
2. Assert the property holds for every item
3. Provide a clear failure message identifying which item violated
   the property

```text
# Pseudocode — framework-agnostic
def step_every_result_matches(context, query):
    for result in context.search_results:
        assert query.lower() in result.name.lower()
            or query.lower() in result.description.lower(),
            f"Result '{result.name}' does not match '{query}'"
```

### Combining with Scenario Outlines

Scenario Outlines are the natural Gherkin vehicle for property-based
testing. Use named Examples blocks to organize inputs by category:

```gherkin
Rule: The pricing engine shall apply the correct discount tier based on order total.

  Scenario Outline: Discount tier is correct for order total
    Given a customer with no special promotions
    When the customer places an order totaling $<total>
    Then the discount should be <discount>%
    And the final price should equal $<total> minus <discount>%

    Examples: No discount (under $50)
      | total | discount |
      | 10.00 | 0        |
      | 49.99 | 0        |

    Examples: Silver tier ($50-$99.99)
      | total | discount |
      | 50.00 | 5        |
      | 75.00 | 5        |

    Examples: Gold tier ($100+)
      | total  | discount |
      | 100.00 | 10       |
      | 500.00 | 10       |
```

The property being tested: the discount percentage is determined
solely by which tier the order total falls into. The Then step
verifies both the tier assignment and the arithmetic.
````

- [ ] **Step 3: Lint**

```bash
pre-commit run --files ears-gherkin-dev/reference/gherkin-scenarios.md
```

Fix any lint errors.

- [ ] **Step 4: Commit**

```bash
git add ears-gherkin-dev/reference/gherkin-scenarios.md
git commit -m "Add gherkin-scenarios.md with property-based testing"
```

---

## Task 4: Create consolidated step-definitions.md

**Files:**

- Create: `ears-gherkin-dev/reference/step-definitions.md`
- Source: `gherkin-step-guide/reference/step-best-practices.md`
- Source: `gherkin-step-guide/reference/step-anti-patterns.md`
- Source: `gherkin-step-guide/reference/step-organization.md`

This file merges three source files. Organization content comes first
(establishes the structural rules), then best practices, then
anti-patterns.

- [ ] **Step 1: Write step-definitions.md**

Write `ears-gherkin-dev/reference/step-definitions.md` with this
structure:

```markdown
# Step Definitions — Comprehensive Reference
```

Then the following sections, in order:

<!-- markdownlint-disable MD013 -->

| Heading | Source |
| :--- | :--- |
| `## Core Principle: One Step Per File` | `step-organization.md` "Core Principle: One Step Per File". **Strengthen** the text to emphasize this is the single most important structural rule: "This is non-negotiable. Every step definition lives in its own file. A file with two or more steps is an audit failure." |
| `## Directory Structure` | `step-organization.md` "Directory Structure" (all subsections: Typical Layout, File Naming Convention, What Goes in Each File, Framework-Specific Conventions, Godog) |
| `## The Three-Layer Model` | `step-best-practices.md` "Keep Step Definitions Declarative" (rename heading; include the three-layer diagram and before/after examples) |
| `## Parameterize Similar Steps` | `step-best-practices.md` "Parameterize Similar Steps" (all content including When NOT to Parameterize) |
| `## Step Reuse Across Features` | `step-best-practices.md` "Step Reuse Across Features" |
| `## Parameter Types` | `step-best-practices.md` "Parameter Types" (all subsections) |
| `## Hooks` | `step-best-practices.md` "Hooks vs. Step Logic" (rename) |
| `## Naming Conventions` | `step-best-practices.md` "Step Definition Naming Conventions" |
| `## Stub Steps (Pending Implementation)` | `step-best-practices.md` "Stub Steps (Pending Implementation)" |
| `## Support Layer Patterns` | `step-organization.md` "Support Layer Patterns" (Page Object, API Client, Factory) |
| `## Shared State Management` | `step-organization.md` "Shared State Management" (all subsections) |
| `## Scaling Patterns` | `step-organization.md` "Scaling Patterns" |
| `## Anti-Patterns` | New heading |
| `### Near-Duplicate Steps` | `step-anti-patterns.md` "Near-Duplicate Steps" |
| `### Multiple Steps Per File` | `step-anti-patterns.md` "Multiple Steps Per File" |
| `### Implementation Leakage` | `step-anti-patterns.md` "Implementation Leakage" |
| `### Overloaded Steps` | `step-anti-patterns.md` "Overloaded Steps" |
| `### Tight Coupling Between Steps` | `step-anti-patterns.md` "Tight Coupling Between Steps" |
| `### Regex Overengineering` | `step-anti-patterns.md` "Regex Overengineering" |
| `### Assertion-Free Then Steps` | `step-anti-patterns.md` "Assertion-Free Then Steps" |
| `### Silent Stub Steps` | `step-anti-patterns.md` "Silent Stub Steps" |
| `### Hard-Coded Test Data` | `step-anti-patterns.md` "Hard-Coded Test Data in Step Patterns" |
| `## Quality Checklist` | Consolidate from `step-best-practices.md` and `step-anti-patterns.md` checklists (they are nearly identical — use the union of both, deduplicated) |

<!-- markdownlint-enable MD013 -->

- [ ] **Step 2: Lint**

```bash
pre-commit run --files ears-gherkin-dev/reference/step-definitions.md
```

Fix any lint errors.

- [ ] **Step 3: Commit**

```bash
git add ears-gherkin-dev/reference/step-definitions.md
git commit -m "Add consolidated step-definitions.md reference"
```

---

## Task 5: Create auditing.md reference

**Files:**

- Create: `ears-gherkin-dev/reference/auditing.md`

This is a new file documenting the merged audit script.

- [ ] **Step 1: Write auditing.md**

Write `ears-gherkin-dev/reference/auditing.md` with the following
content:

````markdown
# Auditing — Reference

This document describes the audit script (`scripts/audit.py`) and
how to use it to verify the quality and consistency of your EARS
requirements, Gherkin scenarios, and step definitions.

---

## When to Audit

**After every change.** Run the audit script proactively as the
final step of the development workflow — do not wait to be asked.
Specifically:

- After creating or modifying a `.feature` file
- After creating or modifying a step definition file
- After deleting or renaming step files
- Before considering any work complete

---

## Usage

```bash
# Audit everything (specs + steps)
python scripts/audit.py features/

# Audit only .feature file structure
python scripts/audit.py features/ --specs-only

# Audit only step definition files
python scripts/audit.py features/ --steps-only

# Specify BDD framework (auto-detected if not given)
python scripts/audit.py features/ --framework behave
python scripts/audit.py features/ --framework cucumber-js
```

The script exits with code 0 if all checks pass, 1 if any findings
are reported.

---

## Spec Checks

The spec audit validates `.feature` file structure against the
EARS-Gherkin mapping rules:

| Check | What it catches |
| :--- | :--- |
| Rule has exactly one "shall" | Missing or compound EARS requirements |
| No wrong obligation keywords | "should", "may", "will", "must" in Rule titles |
| No vague language | Unmeasurable adverbs, adjectives, quantifiers |
| Correct EARS structure | Mismatched keywords (When for states, etc.) |
| Explicit system name | Pronouns ("it") before "shall" |
| Clean Rule descriptions | Additional EARS requirements in freeform text |
| Scenario coverage | Rules with no scenarios |
| Scenarios inside Rules | Scenarios outside any Rule block |

### Common Spec Findings and Fixes

**"Rule title contains 2 occurrences of 'shall'"** — The requirement
is compound. Split it into two `Rule:` blocks, each with one "shall."

**"Rule title uses non-standard obligation keyword: should"** —
Replace "should" with "shall."

**"Rule title contains vague language: 'quickly'"** — Replace with a
measurable value (e.g., "within 200 milliseconds").

**"No scenarios found under this rule"** — Write at least one
scenario demonstrating the requirement.

---

## Step Checks

The step audit validates step definition file organization using the
BDD framework's dry-run output. It delegates step matching to the
actual framework, so it uses the same matching logic your tests use.

| Check | What it catches |
| :--- | :--- |
| Missing step definitions | Steps in `.feature` files with no match |
| Unused step files | Step files not matched by any scenario |
| Multiple steps per file | Files containing more than one step def |
| Step file naming | Filenames that don't match step patterns |
| Near-duplicate files | Similar filenames (consolidation candidates) |
| Keyword directory structure | Files not in `given/`, `when/`, `then/` |

### Common Step Findings and Fixes

**"MISSING: Given the user is logged in"** — Create a new step file
in `features/steps/given/the_user_is_logged_in.py` (or equivalent
for your framework).

**"UNUSED: features/steps/when/old_step.py"** — The step is not
used by any scenario. Delete the file or update scenarios to use it.

**"MULTI-STEP: features/steps/given/setup.py contains 3 steps"** —
Split into three files, one per step, each named after its step.

**"NAMING: features/steps/given/step1.py should be
the_shopping_cart_is_empty.py"** — Rename the file to match the step
pattern it contains.

**"75% similar: add_to_cart.py / add_item_to_cart.py"** — These may
be candidates for consolidation into one parameterized step.

---

## Supported Frameworks

| Framework | Detection | Dry-run command |
| :--- | :--- | :--- |
| Behave (Python) | `environment.py` or `.py` step files | `uvx behave --dry-run` |
| Cucumber-JS | `cucumber.*` config or `.js/.ts` step files | `npx @cucumber/cucumber --dry-run` |

The framework is auto-detected from project structure. Use
`--framework` to override if detection fails.

---

## Reading the Report

The audit report has sections for each check category. Each finding
is prefixed with a category tag:

- `MISSING:` — Step definition needed
- `UNUSED:` — Step file can be deleted
- `MULTI-STEP:` — File needs splitting
- `NAMING:` — File needs renaming
- `DUPLICATE:` — Consolidation candidate
- `ORGANIZATION:` — File not in keyword directory

The summary at the end shows total findings and a pass/fail verdict.
````

- [ ] **Step 2: Lint**

```bash
pre-commit run --files ears-gherkin-dev/reference/auditing.md
```

Fix any lint errors.

- [ ] **Step 3: Commit**

```bash
git add ears-gherkin-dev/reference/auditing.md
git commit -m "Add auditing.md reference for merged audit script"
```

---

## Task 6: Create merged audit.py script

**Files:**

- Create: `ears-gherkin-dev/scripts/audit.py`
- Source: `ears-gherkin-guide/scripts/audit_specs.py`
- Source: `gherkin-step-guide/scripts/audit_steps.py`

This merges both audit scripts into one, fixes the support directory
false positives, and adds two new checks: multiple-steps-per-file
and step file naming.

- [ ] **Step 1: Write the merged audit.py**

Write `ears-gherkin-dev/scripts/audit.py`. The script structure is:

1. **Spec audit functions** — copied from `audit_specs.py`:
   `VAGUE_TERMS`, `WRONG_OBLIGATION_KEYWORDS`,
   `PRONOUNS_BEFORE_SHALL`, `_find_wrong_obligation_keywords`,
   `_find_vague_terms`, `_check_ears_pattern_structure`,
   `_check_missing_system_name`, `audit_feature_file`,
   `_resolve_feature_files`. No changes to these functions.

2. **Step audit functions** — copied from `audit_steps.py`:
   `_detect_framework`, `_STEPS_INIT_CONTENT`,
   `_ensure_steps_init`, `_run_behave_dry_run`,
   `_run_cucumber_dry_run`, `_extract_matches`,
   `_find_step_files`, `_normalize_filename`,
   `_find_near_duplicate_files`, `_print_section`.
   Changes noted below.

3. **New step check functions** — new code for multi-step and
   naming checks.

4. **Combined `audit` function** — replaces the old separate
   entry points.

5. **CLI** — new `argparse` with `--specs-only`, `--steps-only`,
   `--framework`.

**Change 1: Fix `_find_step_files` to exclude support directory.**

In the `_find_step_files` function, after the line that skips
`__init__.py`, `environment.py`, `conftest.py`, and hooks files,
add a check to skip files under a `support` directory:

```python
# In _find_step_files, inside the loop over files:
for f in step_dir.rglob("*"):
    if f.is_file() and f.suffix in valid_exts:
        if f.name in (
            "__init__.py", "environment.py", "conftest.py"
        ):
            continue
        if "hooks" in f.name.lower():
            continue
        # NEW: skip files in support directories
        if "support" in f.parts:
            continue
        step_files.append(str(f))
```

**Change 2: Add `_check_multi_step_files` function.**

This function groups matched steps by file using the dry-run JSON
output. If more than one step maps to the same file, it reports a
finding.

```python
def _check_multi_step_files(
    features_json: list[dict],
) -> list[tuple[str, list[str]]]:
    """Detect files containing more than one step definition.

    Uses dry-run JSON match locations to group steps by file.
    Returns list of (file_path, [step_texts]) for offending files.
    """
    file_steps: dict[str, list[str]] = {}
    for feature in features_json:
        for element in feature.get("elements", []):
            for step in element.get("steps", []):
                match = step.get("match")
                if match and "location" in match:
                    loc = match["location"]
                    file_path = loc.rsplit(":", 1)[0]
                    keyword = step.get("keyword", "").strip()
                    name = step.get("name", "")
                    step_text = f"{keyword} {name}"
                    if step_text not in file_steps.get(
                        file_path, []
                    ):
                        file_steps.setdefault(
                            file_path, []
                        ).append(step_text)

    return [
        (fp, steps)
        for fp, steps in file_steps.items()
        if len(steps) > 1
    ]
```

**Change 3: Add `_check_step_file_naming` function.**

This function extracts each step's pattern text and its matched file
from the dry-run JSON, converts the pattern to an expected
snake_case filename, and flags mismatches.

```python
def _step_text_to_filename(step_text: str) -> str:
    """Convert step text to expected snake_case filename stem.

    Removes quotes, parameter placeholders, and converts to
    snake_case.
    """
    # Remove quoted strings and angle-bracket placeholders
    cleaned = re.sub(r'"[^"]*"', "", step_text)
    cleaned = re.sub(r"<[^>]*>", "", cleaned)
    cleaned = re.sub(r"\{[^}]*\}", "", cleaned)
    # Remove extra whitespace and convert to snake_case
    cleaned = cleaned.strip()
    cleaned = re.sub(r"[^a-zA-Z0-9\s]", "", cleaned)
    cleaned = re.sub(r"\s+", "_", cleaned).lower()
    # Remove trailing underscores
    cleaned = cleaned.strip("_")
    return cleaned


def _check_step_file_naming(
    features_json: list[dict],
) -> list[tuple[str, str, str]]:
    """Check that step files are named after their step pattern.

    Returns list of (actual_file, actual_stem, expected_stem)
    for mismatches.
    """
    findings: list[tuple[str, str, str]] = []
    seen_files: set[str] = set()

    for feature in features_json:
        for element in feature.get("elements", []):
            for step in element.get("steps", []):
                match = step.get("match")
                if match and "location" in match:
                    loc = match["location"]
                    file_path = loc.rsplit(":", 1)[0]
                    if file_path in seen_files:
                        continue
                    seen_files.add(file_path)

                    keyword = step.get("keyword", "").strip()
                    name = step.get("name", "")
                    step_text = f"{keyword} {name}"
                    expected = _step_text_to_filename(name)
                    actual = Path(file_path).stem

                    if expected and actual != expected:
                        findings.append(
                            (file_path, actual, expected)
                        )

    return findings
```

**Change 4: Combined `audit` function.**

The new `audit` function runs both spec and step audits based on
flags:

```python
def audit(
    paths: list[str],
    framework: str | None = None,
    specs_only: bool = False,
    steps_only: bool = False,
) -> int:
    """Run spec and/or step audits. Returns 0 on pass, 1 on
    findings."""
    total_errors = 0

    if not steps_only:
        # Spec audit
        feature_files = _resolve_feature_files(paths)
        if not feature_files:
            print("No .feature files found.")
            return 1
        for fpath in feature_files:
            try:
                total_errors += audit_feature_file(fpath)
            except Exception as e:
                print(f"Error auditing {fpath}: {e}")
                total_errors += 1
        if len(feature_files) > 1:
            print(
                f"\n--- Spec Summary: "
                f"{len(feature_files)} file(s) audited ---"
            )

    if not specs_only:
        # Step audit
        features_dir = paths[0]
        # (step audit logic from audit_steps.py audit()
        # function, with the new checks integrated)
        # ... framework detection, dry-run, extract matches,
        # find step files, near-duplicates ...
        # Plus:
        # - _check_multi_step_files(features_json)
        # - _check_step_file_naming(features_json)
        # Report multi-step findings as MULTI-STEP
        # Report naming findings as NAMING

    return 0 if total_errors == 0 else 1
```

**Change 5: New CLI.**

```python
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Audit EARS-Gherkin specs and step "
        "definitions."
    )
    parser.add_argument(
        "paths",
        nargs="+",
        help="Path(s) to .feature file(s) or director(ies).",
    )
    parser.add_argument(
        "--specs-only",
        action="store_true",
        help="Only audit .feature file structure.",
    )
    parser.add_argument(
        "--steps-only",
        action="store_true",
        help="Only audit step definition files.",
    )
    parser.add_argument(
        "--framework",
        choices=["behave", "cucumber-js"],
        default=None,
        help="BDD framework (auto-detected if not given).",
    )
    args = parser.parse_args()

    try:
        exit_code = audit(
            args.paths,
            framework=args.framework,
            specs_only=args.specs_only,
            steps_only=args.steps_only,
        )
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    sys.exit(exit_code)
```

When assembling the full file, combine all the functions from both
source scripts plus the new functions above. Keep the same imports
from both files (merge and deduplicate). Add `from pathlib import
Path` if not already present.

The complete `audit` function for the step audit portion should
follow the same structure as the existing `audit()` in
`audit_steps.py`, but integrate the two new checks
(`_check_multi_step_files` and `_check_step_file_naming`) into the
reporting. Print multi-step findings in a `[Multi-step files]`
section and naming findings in a `[Step file naming]` section. Add
their counts to the summary.

- [ ] **Step 2: Lint and verify syntax**

```bash
pre-commit run --files ears-gherkin-dev/scripts/audit.py
python -c "import ast; ast.parse(open('ears-gherkin-dev/scripts/audit.py').read()); print('OK')"
```

Fix any lint or syntax errors.

- [ ] **Step 3: Commit**

```bash
git add ears-gherkin-dev/scripts/audit.py
git commit -m "Add merged audit.py with support dir fix and new checks"
```

---

## Task 7: Delete old skill directories and update skills-todo.md

**Files:**

- Delete: `ears-gherkin-guide/` (entire directory)
- Delete: `gherkin-step-guide/` (entire directory)
- Modify: `skills-todo.md`

- [ ] **Step 1: Delete old directories**

```bash
rm -rf ears-gherkin-guide/ gherkin-step-guide/
```

- [ ] **Step 2: Update skills-todo.md**

In `skills-todo.md`, update the "Spec-driven development" entry to
indicate it has been addressed. Change:

```markdown
- Spec-driven development
  - A skill that colaborates with the user to produce EARS and
    Gherkin specifications for a project, and then uses those
    specifications to drive the development of the project.
```

To:

```markdown
- ~~Spec-driven development~~ — Done: `ears-gherkin-dev` skill
```

- [ ] **Step 3: Lint**

```bash
pre-commit run --files skills-todo.md
```

Fix any lint errors.

- [ ] **Step 4: Commit**

```bash
git add -A ears-gherkin-guide/ gherkin-step-guide/ skills-todo.md
git commit -m "Remove old Gherkin skills, update skills-todo.md"
```

---

## Task 8: Final verification

- [ ] **Step 1: Verify directory structure**

```bash
find ears-gherkin-dev/ -type f | sort
```

Expected output:

```text
ears-gherkin-dev/SKILL.md
ears-gherkin-dev/reference/auditing.md
ears-gherkin-dev/reference/ears-requirements.md
ears-gherkin-dev/reference/gherkin-scenarios.md
ears-gherkin-dev/reference/step-definitions.md
ears-gherkin-dev/scripts/audit.py
```

- [ ] **Step 2: Verify old directories are gone**

```bash
ls ears-gherkin-guide/ 2>&1 || true
ls gherkin-step-guide/ 2>&1 || true
```

Both should report "No such file or directory."

- [ ] **Step 3: Run markdownlint on all new files**

```bash
pre-commit run --files \
  ears-gherkin-dev/SKILL.md \
  ears-gherkin-dev/reference/ears-requirements.md \
  ears-gherkin-dev/reference/gherkin-scenarios.md \
  ears-gherkin-dev/reference/step-definitions.md \
  ears-gherkin-dev/reference/auditing.md
```

All must pass.

- [ ] **Step 4: Verify audit script syntax**

```bash
python -c "import ast; ast.parse(open('ears-gherkin-dev/scripts/audit.py').read()); print('Syntax OK')"
```

- [ ] **Step 5: Verify no old references remain**

```bash
grep -r "ears-gherkin-guide\|gherkin-step-guide" \
  ears-gherkin-dev/ skills-todo.md || echo "Clean"
```

Should print "Clean" — no references to the old skill names in the
new files.
