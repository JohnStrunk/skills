# Design: Combine Gherkin Skills into `ears-gherkin-dev`

## Problem

Two separate skills (`ears-gherkin-guide` and `gherkin-step-guide`) cover what
is really a single development methodology. This split causes several problems:

1. **Trigger scope too narrow** — The skills only trigger when the user
   explicitly talks about features or requirements, but any behavior-changing
   code modification should go through the EARS/Gherkin process.
2. **No TDD enforcement** — Neither skill prescribes Red/Green TDD. Changes
   must be verified by first reproducing the problem (red) then confirming the
   fix (green).
3. **Audit script false positives** — The step audit script flags files in the
   `support/` directory as unused step definitions.
4. **Multiple steps per file** — Step files are ending up with more than one
   step definition, making them hard to locate and causing duplication.
5. **Example-only testing** — Scenarios only verify examples. Property-based
   testing should be used where practical for broader coverage.
6. **Audit not proactive** — The skills don't emphasize running audits after
   every change.

## Solution

Merge both skills into a single `ears-gherkin-dev` skill with a strict TDD
workflow, consolidated reference files, and a merged audit script.

## Directory Structure

```text
ears-gherkin-dev/
├── SKILL.md
├── reference/
│   ├── ears-requirements.md
│   ├── gherkin-scenarios.md
│   ├── step-definitions.md
│   └── auditing.md
└── scripts/
    └── audit.py
```

The old directories `ears-gherkin-guide/` and `gherkin-step-guide/` are deleted.

## Skill Description (Trigger)

```text
Drives development through EARS requirements and Gherkin scenarios using
strict Red/Green TDD. Use this skill for ANY code change that affects
system behavior — new features, bug fixes, handling unwanted behavior,
and responding to review feedback. Every behavior change must be covered
by an EARS requirement and verified by Gherkin scenarios before
implementation begins.
```

Excludes pure refactors that don't change behavior (e.g., renaming a variable).

## SKILL.md: Strict TDD Workflow

The SKILL.md is a concise (~150 line) workflow document. The numbered steps
are mandatory for every behavior change:

1. **Understand the change** — Read the request/bug/feedback. Identify what
   behavior is changing.
2. **Write/update EARS requirement** — Formulate or revise the EARS requirement
   that governs this behavior. Place it as a `Rule:` title in the appropriate
   `.feature` file. Consult `reference/ears-requirements.md`.
3. **Write failing scenario(s)** — Write Gherkin scenarios under that Rule that
   demonstrate the desired behavior. For bug fixes, write a scenario that
   reproduces the bug. Prefer property-based testing where practical for broader
   coverage. Consult `reference/gherkin-scenarios.md`.
4. **Run and confirm RED** — Execute the scenarios and confirm they fail. This
   proves the test is actually testing something new.
5. **Write/update step definitions** — Implement step definition files. One step
   per file. File named after its one step. Consult
   `reference/step-definitions.md`.
6. **Implement the code** — Write the minimum code to make the scenarios pass.
7. **Run and confirm GREEN** — Execute the scenarios and confirm they pass.
8. **Audit** — Run `scripts/audit.py` against the features directory. Fix any
   findings before considering the work complete.

Key rules stated in SKILL.md (one line each, details in references):

- One EARS requirement per `Rule:` block — the Rule title IS the requirement.
- One step definition per file — file named in snake_case after the step
  pattern.
- Scenarios are declarative, not imperative.
- Property-based testing preferred over example-only testing where
  practical.
- Proactively audit after every change — don't wait to be asked.

## Reference File Consolidation

### `reference/ears-requirements.md`

Merges three existing files:

- From `ears-patterns.md`: All 6 EARS pattern definitions, templates, selection
  heuristics, decision tree, compound patterns, NFR patterns, domain examples.
- From `ears-anti-patterns.md`: The 10 anti-patterns with before/after examples,
  words to avoid.
- From `requirements-quality.md`: Elicitation techniques, validation criteria
  (9 characteristics), SMART criteria, decomposition strategy, common user
  phrases to EARS translations.
- Single consolidated quality checklist (currently duplicated across sources).

### `reference/gherkin-scenarios.md`

Kept largely as-is from the existing file, plus:

- New section on property-based testing: when to use it, how to express it in
  Gherkin (Scenario Outlines with generated data, property assertions in Then
  steps), examples.
- EARS-to-scenario mapping stays here.

### `reference/step-definitions.md`

Merges three existing files:

- From `step-best-practices.md`: Parameterization, declarative style,
  three-layer model, reuse, custom types, hooks.
- From `step-anti-patterns.md`: The anti-patterns with before/after examples.
- From `step-organization.md`: One-step-per-file rule, keyword directory
  structure, file naming, framework conventions, support layer patterns, state
  management.
- Single consolidated quality checklist.
- Stronger emphasis on the one-step-per-file constraint and file naming
  convention.

### `reference/auditing.md`

New file covering:

- What the audit script checks (both spec-level and step-level).
- How to read audit output.
- Common findings and how to fix them.
- When to run the audit (after every change, proactively).

## Audit Script: Merged `scripts/audit.py`

### CLI

```bash
# Audit everything
python scripts/audit.py features/

# Audit only specs or steps
python scripts/audit.py features/ --specs-only
python scripts/audit.py features/ --steps-only

# Specify framework
python scripts/audit.py features/ --framework behave
```

Default runs both spec and step audits in sequence, single exit code.

### Bug Fix: Support Directory False Positives

In `_find_step_files()`, skip any file whose path contains a `/support/`
segment. Currently the function only skips specific filenames (`__init__.py`,
`environment.py`, `conftest.py`, files with "hooks" in the name).

### New Check: Multiple Steps Per File

Framework-agnostic approach using dry-run JSON output:

- The dry-run output already reports which file each matched step lives in
  (the `match.location` field gives `file:line`).
- Group matched steps by file — if more than one step maps to the same file,
  flag it.
- Works with any framework that produces the JSON dry-run format.

### New Check: Step File Naming

Framework-agnostic approach using dry-run JSON output:

- Extract each step's pattern text and its matched file from the dry-run output.
- Convert the pattern to an expected snake_case filename.
- Flag mismatches between actual filename and expected filename.

### Framework Agnosticism

- The SKILL.md workflow mentions no framework-specific syntax.
- Reference files keep the existing multi-framework tables (Behave, pytest-bdd,
  Cucumber Java/JS/Ruby, SpecFlow, Godog).
- The audit script is the only place with framework-specific logic, behind the
  `--framework` flag and auto-detection.

## What Gets Deleted

- `ears-gherkin-guide/` — entire directory.
- `gherkin-step-guide/` — entire directory.

## What Stays Untouched

- `docs/gherkin-research/` — background research, not part of the skill.
- `.agents/skills/` and `.claude/skills/` — marketplace skills, unrelated.

## `skills-todo.md` Update

The "Spec-driven development" entry is addressed by this skill and should be
updated to reflect that.
