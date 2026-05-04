---
name: gherkin-step-guide
description: >
  Guides creation, review, and auditing of Gherkin step definition files —
  the code that implements .feature file test steps. Use this skill when the
  user wants to write, refactor, organize, or audit BDD step definitions in
  any framework (Cucumber, Behave, Godog, SpecFlow, pytest-bdd, etc.). This skill
  complements the ears-gherkin-guide skill, which covers requirements and
  scenario specification; this one picks up at the implementation layer.
  Use it whenever step files, step definitions, step organization, or step
  reuse comes up.
---

# Gherkin Step Definition Guide

You are an expert BDD practitioner. Your goal is to help the user create,
organize, and maintain high-quality step definition files that implement
Gherkin scenarios.

Step definitions are the bridge between human-readable scenarios and
executable test code. Good step definitions are reusable, maintainable, and
keep implementation details out of the scenario layer. Bad ones become a
maintenance burden that undermines the value of BDD.

This guide is framework-agnostic — the principles apply to Cucumber (Ruby,
Java, JS/TS), Behave (Python), pytest-bdd, SpecFlow (.NET), Godog (Go),
and others. Framework-specific syntax is noted where it matters.

## Reference Material

The `reference/` directory contains detailed guidance you MUST consult when
working with step definitions:

- `reference/step-best-practices.md` — Parameterization, declarative style,
  reuse patterns, parameter types, and hooks.
- `reference/step-anti-patterns.md` — Common mistakes with before/after
  examples and a quality checklist.
- `reference/step-organization.md` — File organization strategies,
  support/helper layer patterns, and state management.

## Workflow

### 1. Understand the Scenario Layer

Before writing step definitions, read the `.feature` files that the steps
will implement. Understand the domain language, the patterns used in
Given/When/Then steps, and any Scenario Outlines or Data Tables that need
parameter handling.

If the project uses the EARS-Gherkin approach (see `ears-gherkin-guide`),
the `Rule:` blocks define the requirements — use them to understand what
each scenario is verifying.

### 2. Survey Existing Steps

Before writing any new step definition, check for existing steps that
already cover the behavior or could be generalized to cover it.

1. **Search existing step files** for steps with similar wording or
   parameters. A step like `the user enters their "email"` might already
   exist as `the user enters their {field}`.
2. **Check for near-duplicates** — steps that differ only by a noun, value,
   or phrasing. These are candidates for consolidation into a single
   parameterized step.
3. **Run the audit script** (`scripts/audit_steps.py`) to get a full
   inventory of existing step definitions and detect gaps.

### 3. Write Step Definitions

Consult `reference/step-best-practices.md` for detailed guidance.

Follow these core principles:

- **Parameterize, don't duplicate.** If two steps differ only by a noun or
  value, write one parameterized step definition instead of two
  near-identical ones.
- **Stay declarative.** Step definitions translate *what* a scenario says
  into code, but the code itself should delegate to a support layer (page
  objects, API clients, database helpers). The step definition wires intent
  to implementation — it should not *be* the implementation.
- **One responsibility per step.** A `Given` sets up state. A `When`
  performs an action. A `Then` asserts an outcome. Do not mix these
  responsibilities within a single step.
- **Reuse across features.** Step definitions are global (in most
  frameworks). Write them to be reusable across feature files, not coupled
  to a single scenario.
- **Mark stubs as pending.** When creating step files before the
  implementation is ready, use the framework's pending marker (e.g.,
  `raise NotImplementedError` in Behave, `return 'pending'` in
  Cucumber-JS, `godog.ErrPending` in Go). Never write empty bodies or
  `assert True` — silent stubs hide missing implementation.

#### Parameterization Quick Reference

Step definitions accept parameters that capture variable parts of the step
text. Use them to generalize steps.

| Parameter Style | Example Step Text | Captures |
| :--- | :--- | :--- |
| Quoted string | `the user enters "alice@test.com"` | String value |
| Numeric | `the cart contains 3 items` | Integer/float |
| Data Table | `Given the following users:` | Tabular data |
| Doc String | `Then the error message should be:` | Multi-line text |
| Custom type | `the user has a "premium" account` | Domain enum/object |

#### Framework Syntax At a Glance

| Framework | Step Definition Syntax |
| :--- | :--- |
| **Behave** (Python) | `@given('pattern with "{param}"')` |
| **pytest-bdd** (Python) | `@given(parsers.parse('pattern with "{param}"'))` |
| **Cucumber** (Java) | `@Given("pattern with {string}")` |
| **Cucumber** (JS/TS) | `Given('pattern with {string}', ...)` |
| **Cucumber** (Ruby) | `Given(/^pattern with "([^"]*)"$/) do \|param\|` |
| **SpecFlow** (C#) | `[Given(@"pattern with ""(.*)""")]` |
| **Godog** (Go) | `ctx.Given("^pattern with \"([^\"]*)\"$", stepFunc)` |

### 4. Organize Step Files

Consult `reference/step-organization.md` for detailed patterns.

- **One step per file.** Each step definition lives in its own file. This
  makes every step independently discoverable and auditable — an unused
  step is an unused file.
- **Name files after the step.** Derive the filename from the step pattern
  in snake_case (e.g., a step `the shopping cart is empty` lives in
  `the_shopping_cart_is_empty.py`). Strip quotes and parameter placeholders.
- **Organize by keyword type.** Place files in directories by their
  Gherkin keyword: `features/steps/given/`, `features/steps/when/`,
  `features/steps/then/`.
- **Separate support code.** Implementation logic (page objects, API
  clients, database helpers) belongs in a support or helper module, not
  inline in step definitions.
- **Manage shared state** through the framework's context or world object,
  not through module-level globals or inter-step coupling.

### 5. Audit and Maintain

Always run the bundled auditing script `scripts/audit_steps.py` after
creating or modifying step files to catch problems early.

The script delegates step matching to the actual BDD framework (via
`uvx behave --dry-run` or `npx @cucumber/cucumber --dry-run`), so it
uses the same matching logic your tests use — no reimplemented regex
parsing.

The script detects:

- **Unused step files** — step definition files that are not matched by
  any step in any `.feature` file. In the one-step-per-file model, an
  unused file means an unused step.
- **Missing step definitions** — steps in `.feature` files with no
  matching definition. These will fail at runtime.
- **Near-duplicate files** — step files with similar names that may be
  candidates for consolidation into a single parameterized step.
- **Statistics** — total step files, matched vs. unused, and coverage.

Usage:

```bash
# Audit a Behave project (auto-detected)
python scripts/audit_steps.py features/

# Specify framework explicitly
python scripts/audit_steps.py features/ --framework behave
python scripts/audit_steps.py features/ --framework cucumber-js
```

## Hooks

Hooks (`Before`, `After`, `Around`, `BeforeStep`, `AfterStep`) run setup and
teardown code outside of step definitions. Use them for cross-cutting
concerns that apply to many scenarios — not as a substitute for `Given`
steps.

| Use hooks for | Use Given steps for |
| :--- | :--- |
| Browser/driver lifecycle | Scenario-specific preconditions |
| Database transaction wrapping | Inserting specific test data |
| Logging and screenshots on failure | Setting up a particular user state |
| Cleaning up external resources | Describing context the reader needs |

The key distinction: if a reader needs to see the setup to understand the
scenario, it belongs in a `Given`. If it is invisible infrastructure, use a
hook.

## Writing Scenarios — Previous Step

This skill covers step definition implementation. If the user needs to
write or revise the `.feature` files and requirements that step
definitions implement, use the companion `ears-gherkin-guide` skill —
it covers EARS requirements, Gherkin scenario writing, and
specification quality. When the user is working on requirements or
scenarios and then shifts to implementation, suggest switching to this
skill.
