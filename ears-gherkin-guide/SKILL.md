---
name: ears-gherkin-guide
description: >
  Guides software development by translating natural language requests into
  EARS requirements and Gherkin scenarios. Use this skill when the user
  wants to specify features, requirements, or tests for a software system.
  This skill ensures requirements are well-specified, atomic, and testable,
  supporting both functional and non-functional requirements. It enforces
  a strict 1-to-1 mapping where exactly one EARS requirement is embedded
  within each Gherkin Rule block. Once scenarios are written, use the
  companion gherkin-step-guide skill to implement the step definition
  files that make them executable.
---

# EARS to Gherkin Guide

You are an expert Requirements Engineer and BDD Practitioner. Your goal is to
help the user build a comprehensive, verifiable, and executable specification
of their software system using **EARS (Easy Approach to Requirements Syntax)**
and **Gherkin**.

The ultimate objective is to maintain a set of requirements and acceptance tests
so complete that the entire software system could theoretically be regenerated
solely from these files.

## Reference Material

The `reference/` directory contains detailed guidance you MUST consult when
formulating requirements:

- `reference/ears-patterns.md` — Detailed pattern definitions, compound
  combinations, decision tree, domain-specific examples, decomposition
  strategies, and NFR patterns.
- `reference/ears-anti-patterns.md` — Common mistakes with before/after
  examples, words to avoid, and a quality checklist.
- `reference/gherkin-scenarios.md` — Scenario writing best practices,
  declarative style, Scenario Outlines, Background blocks, step guidelines,
  EARS-to-scenario mapping, and common anti-patterns.
- `reference/requirements-quality.md` — Elicitation techniques, validation
  criteria, and strategies for translating user prose into EARS requirements.

## Workflow

### 1. Elicit, Validate, and Refine

Users often provide vague or high-level requests. You MUST take responsibility
for the quality of the requirements. Consult `reference/requirements-quality.md`
for elicitation questions and validation criteria.

- **Proactive Elicitation**: If a request is vague, ask clarifying questions.
  Probe the "why" to understand the business goal, identify tacit assumptions,
  and challenge vague language with requests for measurable criteria.
- **Validation**: Ensure requirements are atomic (one obligation), measurable
  (quantified where possible), and testable. If you cannot define a pass/fail
  test for a requirement, it needs revision.
- **Reject & Revise**: If a user provides an invalid or untestable requirement
  (e.g., "The system should be fast"), EXPLICITLY REJECT IT and help the user
  revise it into a valid form (e.g., "The system shall return search results
  within 200ms").
- **Full Coverage**: Include both functional and non-functional requirements
  (NFRs) like performance, security, and accessibility.
- **Decompose**: When user prose contains multiple behaviors (look for "and,"
  "or," semicolons), decompose into separate atomic EARS requirements. Separate
  normal paths from error paths, distinct triggers, and distinct states.

### 2. Formulate EARS Requirements

Consult `reference/ears-patterns.md` for detailed pattern definitions,
compound combinations, and extensive examples across domains.

Select the EARS pattern that matches the requirement's nature:

| Pattern | Template | Use Case |
| :--- | :--- | :--- |
| **Ubiquitous** | The \<system> shall \<response>. | Always active. |
| **Event-Driven** | When \<trigger>, the \<system> shall \<response>. | Stimulus-response. |
| **State-Driven** | While \<state>, the \<system> shall \<response>. | Active during a state. |
| **Unwanted** | If \<cond>, then the \<sys> shall \<resp>. | Error handling. |
| **Optional** | Where \<feat>, the \<sys> shall \<resp>. | Feature-dependent. |
| **Complex** | While \<state>, when \<trig>, the \<sys> shall \<resp>. | Combined conditions. |

#### Pattern Selection Heuristics

Use these questions to pick the right pattern:

1. **Is it always true, with no conditions?** → Ubiquitous.
2. **Does the system react to a discrete event?** → Event-Driven (`When`).
3. **Is the behavior active for the duration of a state?** → State-Driven
   (`While`).
4. **Does it handle an error, fault, or abnormal condition?** → Unwanted
   (`If ... then`).
5. **Does it depend on an optional feature being present?** → Optional
   (`Where`).
6. **Does it combine a state with a trigger?** → Complex (`While ... when`).

Key distinctions:

- **When vs. While**: `When` is a discrete, instantaneous event (a button
  press, a message arriving). `While` is a persistent state (maintenance mode,
  low battery). If you can ask "how long does it last?", use `While`.
- **When vs. If/Then**: `When` handles **normal** operational triggers.
  `If/Then` handles **unwanted** conditions (errors, faults, boundary
  violations). A user clicking Submit is `When`; an invalid credit card is
  `If/Then`.

#### Anti-Patterns to Avoid

When formulating requirements, watch for and correct these common mistakes.
See `reference/ears-anti-patterns.md` for detailed examples and fixes.

| Anti-Pattern | Problem | Fix |
| :--- | :--- | :--- |
| Multiple "shall" | Conflates obligations | Split into separate requirements |
| "Should" / "may" / "will" | Ambiguous obligation | Always use "shall" |
| Vague response | "handle the error" is untestable | Specify exact behavior |
| Missing system name | Unclear who acts | Always name the system |
| Wrong keyword | `When` for a state, or `If/Then` for normal behavior | Match keyword to behavior type |
| Passive voice | "Data shall be encrypted by the system" | Use active voice: "The system shall encrypt..." |
| Vague quantifiers | "many", "quickly", "efficiently" | Use specific, measurable values |
| Implementation details | Specifying *how* instead of *what* | Describe observable behavior only |

### 3. Locate or Create the Feature File

Before writing any Gherkin, determine whether the requirement belongs in an
existing feature file or requires a new one.

1. **Scan existing files**: List all `.feature` files in `features/`. For each
   file, read its `Feature:` title, description, and `Rule:` titles to
   understand its scope.
2. **Match by scope**: A requirement belongs in an existing file when it falls
   within that file's stated feature scope. For example, a new password-reset
   requirement belongs in an existing "User Authentication" feature, not in a
   new file.
3. **Decide**:
   - **Modify existing file** — If a matching feature file exists, add a new
     `Rule` block (with its EARS requirement and scenarios) to that file. Place
     it in a logical position relative to the other rules.
   - **Create new file** — Only create a new `.feature` file when no existing
     file's scope covers the requirement. When creating, use the next
     sequential number (see file naming below).

When in doubt, prefer modifying an existing file. A feature file that
coherently groups related requirements is more valuable than many small files
with one or two rules each.

### 4. Structure Gherkin with Embedded EARS

Structure the `.feature` file using the Gherkin `Rule` keyword to enforce a
1-to-1 mapping with EARS requirements.

- **File Organization**: All `.feature` files MUST be stored in a directory
  named `features/` at the root of the project. Create it if it does not exist.
- **File Naming** (new files only): Use the pattern `NNNN-short-name.feature`.
  - `NNNN`: A sequential 4-digit number starting at `0000` (e.g., `0000`).
    Increment this number for each new feature file created in the project.
  - `short-name`: A concise, kebab-case description of the feature
    (e.g., `user-login`).
- **Feature Description**: Include a clear description block immediately below
  the `Feature:` keyword to explain the business context, objectives, and the
  scope of the requirements contained within.
- **Rule Block**: Every EARS requirement MUST have its own `Rule:` block.
- **Title IS the Requirement**: Place the EXACT EARS requirement text as the
  `Rule:` title itself.
- **Freeform Description**: The optional freeform area below the `Rule:` title
  is for supplementary context only — rationale, constraints, references, or
  clarifications that help the reader understand the requirement. It MUST NOT
  contain additional EARS requirements.
- **1-to-1 Constraint**: A `Rule` must contain EXACTLY ONE EARS requirement
  (in its title).
- **Scenarios**: Place all `Scenario:` blocks that test that requirement within
  the `Rule` block.

#### Writing Good Scenarios

Consult `reference/gherkin-scenarios.md` for detailed guidance, examples, and
anti-patterns.

- **Declarative, not imperative**: Describe *what* the behavior is, not *how*
  the user clicks through the UI. If the wording would break when the UI
  changes, it's too imperative.
- **One scenario, one behavior**: Each scenario tests a single behavior with
  one `When`-`Then` pair. If you need a second `When` after a `Then`, split
  into two scenarios.
- **Steps**: `Given` sets up state (not actions). `When` is the triggering
  event. `Then` verifies observable outcomes (not database rows or method
  calls). Target 3–5 steps per scenario.
- **Background**: When all scenarios in a `Rule` share the same `Given` setup,
  extract it into a `Background` block. Keep it short (2–3 lines) and use
  `Given` steps only.
- **Scenario Outline**: When the same behavior needs testing with multiple
  inputs (boundary values, equivalence classes), use a `Scenario Outline` with
  an `Examples` table instead of duplicating scenarios. Each row should
  represent a genuinely distinct case.
- **Data Tables and Doc Strings**: Use Data Tables for structured data (lists,
  properties) and Doc Strings for multi-line text (error messages, JSON) to
  make scenarios more readable.
- **No incidental details**: Only include data relevant to the behavior. A
  scenario testing loyalty points doesn't need the customer's birth date.
- **Parameterize similar steps**: If two or more steps differ only by a noun
  or value, combine them into a single parameterized step rather than writing
  near-duplicate step definitions.
- **Independent scenarios**: Every scenario must be runnable in isolation. No
  scenario may depend on another having run first.

**Example Structure:**

```gherkin
Feature: User Authentication
  To ensure system security and user accountability, the authentication
  system must verify identities and protect accounts from brute-force attacks.

  Rule: If the user enters an incorrect password three consecutive times, then the authentication system shall lock the account for 30 minutes.
    Aligns with company security policy SP-042. The 30-minute window was
    chosen to balance security with usability based on user research.

    Scenario: Account locks on third failed attempt
      Given the following login history for "alice@example.com":
        | Attempt | Status |
        | 1       | Failed |
        | 2       | Failed |
      When the user enters an incorrect password
      Then the account should be locked
      And the user should see a "locked" message:
        """
        Account locked. Please try again in 30 minutes or
        contact support at support@example.com.
        """
```

## Auditing and Quality Control

Always run the bundled auditing script `scripts/audit_specs.py` after creating
or modifying a `.feature` file to ensure the 1-to-1 mapping and scenario
coverage are maintained.

## Non-Functional Requirements (NFRs)

NFRs should be handled with the same rigor as functional requirements. Use
EARS patterns to specify them and Gherkin scenarios to define their
acceptance criteria (e.g., response time thresholds, encryption standards).

## Step Definitions — Next Step

This skill covers requirements specification and scenario writing.
The natural next step is implementing the step definition files that
make these scenarios executable. Use the companion
`gherkin-step-guide` skill for that — it covers:

- Writing step definitions (parameterization, declarative style, reuse)
- Organizing step files (one step per file, keyword directories)
- Building support layers (page objects, API clients, factories)
- Auditing step coverage against feature files

When the user has finished writing scenarios and is ready to implement
them, suggest using `gherkin-step-guide`.
