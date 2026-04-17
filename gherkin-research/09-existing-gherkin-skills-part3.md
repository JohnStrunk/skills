# Existing Gherkin/BDD Skills - Part 3: Extended Survey

This document covers additional Claude Code skills (and one GitHub
Copilot agent) related to BDD, Cucumber, and Gherkin specifications
that complement the initial survey. Skills are grouped by source
repository and assessed for relevance to our goal of building a
Gherkin specification skill.

---

## Table of Contents

1. [BDD Feature Generator (bdd-feature-generator)](#1-bdd-feature-generator)
2. [BDD Patterns (thebushidocollective/han)](#2-bdd-patterns)
3. [BDD Scenarios (thebushidocollective/han)](#3-bdd-scenarios)
4. [BDD Principles (thebushidocollective/han)](#4-bdd-principles)
5. [BDD Collaboration (thebushidocollective/han)](#5-bdd-collaboration)
6. [Cucumber Best Practices (thebushidocollective/han)](#6-cucumber-best-practices)
7. [Cucumber Step Definitions (thebushidocollective/han)](#7-cucumber-step-definitions)
8. [Cucumber Fundamentals (thebushidocollective/han)](#8-cucumber-fundamentals)
9. [Add Cucumber Tests (decathlon/tzatziki)](#9-add-cucumber-tests)
10. [Playwright Cucumber Expert (jmr85/e2e-agent-skills)](#10-playwright-cucumber-expert)
11. [Feature Spec (steveclarke/dotfiles)](#11-feature-spec)
12. [Feature Requirements (steveclarke/dotfiles)](#12-feature-requirements)
13. [Feature Plan (steveclarke/dotfiles)](#13-feature-plan)
14. [Create Specification (github/awesome-copilot)](#14-create-specification)
15. [Bonus: Playwright BDD Skills
    (thebushidocollective/han)](#15-bonus-playwright-bdd-skills-thebushidocollectivehan)
16. [Summary and Key Takeaways](#16-summary-and-key-takeaways)

---

## 1. BDD Feature Generator

- **Source**: Originally listed as `moxa/sw` (repo is private/removed); SKILL.md
  found in `majiayu000/claude-skill-registry` at
  `skills/data/bdd-feature-generator/SKILL.md`
- **Installs**: ~1.2K
- **Category**: Test generation

### Purpose

Generates `.feature` files for **Golang Clean Architecture**
projects using Gherkin syntax. Specifically designed for projects
with existing Godog/Cucumber step
definitions for integration testing of REST APIs.

### Workflow

1. **Gather Requirements** -- Ask user for feature name, API
   endpoints, request/response structures, validation rules,
   database tables, external dependencies,
   event publishing, and error codes.
2. **Analyze Similar Features** -- Examine existing feature files in
   `/test/integration/features/` for reusable patterns.
3. **Generate Feature File** -- Produce a complete `.feature` file with
   Background, validation scenarios (Scenario Outline), success scenarios, and
   error scenarios.
4. **Apply Patterns** -- Use established error response structures, error code
   formats, tag conventions, and special assertion values.

### Automation

- **Generates files**: Yes, creates `.feature` files in
  `/test/integration/features/`
- **Runs commands**: No
- **Provides guidance**: Yes, includes reference documents for step definitions,
  patterns, and a feature template

### Key Instructions

- **ONLY use existing step definitions** -- never create new ones.
- All feature files must go in `/test/integration/features/`.
- Mandatory file headers: `#language: en` and `#utf-8`.
- Tags convention: always include `@all` plus feature-specific and category tags
  (`@success`, `@error`, `@contract_fields_validation`, etc.).
- Error code format: `PREFIX-ERRNUM` (e.g., `USR-01400`).
- Special assertion values: `"not nil"`, `"nil"`, `null`, `""`.
- Feature files are created BEFORE implementation code.

### Relevance

**Medium**. This skill is narrowly scoped to Golang API testing with specific
step definition patterns. However, its structured workflow (gather requirements,
analyze existing patterns, generate, apply conventions) is a useful model. The
concept of requiring existing step definitions and never inventing new ones is
a strong guardrail pattern. The tag convention system is worth considering.

---

## 2. BDD Patterns

- **Source**: `thebushidocollective/han` at
  `plugins/patterns/bdd/skills/bdd-patterns/SKILL.md`
- **Installs**: ~105
- **Category**: Pattern (reference knowledge)

### Purpose (bdd-patterns)

Teaches the Given-When-Then structure, feature file organization, Scenario
Outlines, and step definition patterns. Acts as a knowledge reference rather
than a generative tool.

### Workflow (bdd-patterns)

Not a workflow-driven skill. Activated contextually when users need help
applying BDD patterns including:

- Writing acceptance tests stakeholders can understand
- Defining behavior before implementation
- Creating living documentation from tests
- Bridging communication between developers and business

### Automation (bdd-patterns)

- **Generates files**: No
- **Runs commands**: No
- **Provides guidance**: Yes, pure reference material

### Key Instructions (bdd-patterns)

- Write scenarios from the user's perspective.
- Keep scenarios focused on single behaviors.
- Use declarative language, not implementation details.
- Reuse step definitions across scenarios.
- Use Background for common setup steps.
- Keep feature files organized by domain area.

### Relevance (bdd-patterns)

**Medium-Low**. Pure reference material with standard BDD best practices.
The content is well-organized but does not break new ground. The emphasis on
declarative vs. imperative style is universally applicable.

---

## 3. BDD Scenarios

- **Source**: `thebushidocollective/han` at
  `plugins/patterns/bdd/skills/bdd-scenarios/SKILL.md`
- **Installs**: ~74
- **Category**: Pattern (reference knowledge)

### Purpose (bdd-scenarios)

Teaches how to write effective BDD scenarios including acceptance criteria,
edge cases, and scenario organization with tags.

### Workflow (bdd-scenarios)

Not a structured workflow. Provides guidance for:

- Defining acceptance criteria for user stories
- Documenting expected system behavior
- Creating comprehensive test coverage
- Identifying edge cases early

### Automation (bdd-scenarios)

- **Generates files**: No
- **Runs commands**: No
- **Provides guidance**: Yes, reference material

### Key Instructions (bdd-scenarios)

- A good scenario should be: **Specific** (test one behavior), **Declarative**
  (describe what, not how), **Business-focused** (use domain language), and
  **Independent** (no dependencies on other scenarios).
- Start with the happy path scenario, then add edge cases systematically.
- Keep scenarios at 3-7 steps.
- Write scenarios before implementation.
- Uses the `Rule` keyword to group scenarios by acceptance criteria.
- Contrasts good vs. bad scenarios with clear examples.

### Relevance (bdd-scenarios)

**Medium**. The guidance on writing effective scenarios and the emphasis on
the `Rule` keyword for acceptance criteria grouping are directly applicable.
The 3-7 step guideline and the specific/declarative/business-focused/
independent framework are useful quality criteria.

---

## 4. BDD Principles

- **Source**: `thebushidocollective/han` at
  `plugins/patterns/bdd/skills/bdd-principles/SKILL.md`
- **Installs**: ~59
- **Category**: Pattern (reference knowledge)

### Purpose (bdd-principles)

Comprehensive reference covering BDD philosophy, the Three Amigos practice,
Discovery-Development-Delivery cycle, Example Mapping, Specification by Example,
ubiquitous language, outside-in development, and common misconceptions.

### Workflow (bdd-principles)

Not a workflow-driven skill. This is a deep knowledge reference that covers:

- Core BDD philosophy and the Discovery > Development > Delivery cycle
- Three Amigos collaboration sessions
- Example Mapping workshops (Yellow/Blue/Green/Red cards)
- Specification by Example
- Ubiquitous language development
- Outside-in development approach
- BDD vs. TDD comparison

### Automation (bdd-principles)

- **Generates files**: No
- **Runs commands**: No
- **Provides guidance**: Yes, extensive philosophical and practical reference

### Key Instructions (bdd-principles)

- BDD is fundamentally about **communication and collaboration**, not testing.
- Example Mapping uses four card colors: Yellow (stories), Blue (rules),
  Green (examples), Red (questions).
- Ubiquitous language: use business terms consistently (e.g., "Member" not
  "User", "Place order" not "Submit order").
- Living documentation: scenarios serve as executable specifications,
  documentation, common language, and regression suite.
- Key misconception corrections: BDD is not "just testing with Cucumber";
  it is not only about writing tests before code; not only testers write
  scenarios.
- Outside-in development: start from user-facing behavior, work inward.

### Relevance (bdd-principles)

**Medium**. While our Gherkin specification skill is focused on requirements
capture rather than test automation, several BDD principles are highly relevant:

- **Example Mapping** (rules + examples + questions) maps well to requirements
  discovery.
- **Ubiquitous language** is essential for specification clarity.
- **Specification by Example** turns vague requirements into concrete scenarios.
- The emphasis on collaboration and shared understanding aligns with our goal
  of using Gherkin as a communication tool.

---

## 5. BDD Collaboration

- **Source**: `thebushidocollective/han` at
  `plugins/patterns/bdd/skills/bdd-collaboration/SKILL.md`
- **Installs**: (part of the BDD plugin, not separately listed)
- **Category**: Pattern (reference knowledge)

### Purpose (bdd-collaboration)

Facilitates BDD collaboration between developers, testers, and business
stakeholders. Covers Three Amigos sessions, Example Mapping, Discovery
Workshops, ubiquitous language, and living documentation practices.

### Workflow (bdd-collaboration)

Provides a structured Discovery Workshop format:

1. **INTRODUCE** (5 min) -- Present the feature or story, share context.
2. **EXPLORE** (20 min) -- Ask "What are the rules?", "Can you give me an
   example?", "What could go wrong?"
3. **DOCUMENT** (15 min) -- Write scenarios together, capture questions.
4. **REVIEW** (10 min) -- Read scenarios aloud, confirm shared understanding.

### Automation (bdd-collaboration)

- **Generates files**: No
- **Runs commands**: No
- **Provides guidance**: Yes, workshop facilitation reference

### Key Instructions (bdd-collaboration)

- Schedule regular Three Amigos sessions.
- Use Example Mapping for complex stories.
- Create and maintain a domain glossary.
- Keep scenarios as living documentation.
- Define domain terms in feature descriptions.
- Link to business documentation with tags (`@jira:PAY-123`, `@since:v2.1`).
- Time-box discovery sessions.

### Relevance (bdd-collaboration)

**Medium-High** for our specification skill's design. The Discovery Workshop
format (introduce, explore, document, review) could inform an interactive
requirements-gathering workflow. The Example Mapping structure
(story > rules > examples > questions) is a natural fit for structured
specification capture. The domain glossary concept aligns well with
specification clarity goals.

---

## 6. Cucumber Best Practices

- **Source**: `thebushidocollective/han` at
  `plugins/tools/cucumber/skills/cucumber-best-practices/SKILL.md`
- **Installs**: ~74
- **Category**: Tool (reference knowledge)

### Purpose (cucumber-best-practices)

Comprehensive reference for Cucumber testing patterns and anti-patterns.
Covers scenario design principles, feature organization, Gherkin writing
guidelines, Scenario Outlines, step definition patterns, data management,
error handling, and the testing pyramid.

### Workflow (cucumber-best-practices)

Not a structured workflow. Reference material organized by topic area.

### Automation (cucumber-best-practices)

- **Generates files**: No
- **Runs commands**: No
- **Provides guidance**: Yes, extensive reference material

### Key Instructions (cucumber-best-practices)

**Scenario Design Principles:**

1. Write declarative scenarios (business-focused, not implementation-focused).
2. One scenario, one behavior.
3. Keep scenarios independent (each sets up its own preconditions).
4. Use Background wisely (common setup only, not too much).

**Gherkin Writing Guidelines:**

- Use domain language, not technical terms.
- Keep steps at the same abstraction level.
- Avoid conjunctive steps (don't combine multiple actions in one step).

**Anti-Patterns to Avoid:**

- Testing implementation details (`Then the database should have 1 record`).
- UI-specific assertions in business scenarios.
- Using Given for actions.
- Technical jargon in scenarios.

**Testing Pyramid:**

- E2E Cucumber Tests: 20% (critical user journeys only)
- Integration Tests: 30%
- Unit Tests: 50%

### Relevance (cucumber-best-practices)

**Medium**. The anti-pattern catalog is valuable for any Gherkin skill.
The principle of keeping steps at the same abstraction level is important
for specification quality. The testing pyramid guidance is less relevant
for a specification-focused skill.

---

## 7. Cucumber Step Definitions

- **Source**: `thebushidocollective/han` at
  `plugins/tools/cucumber/skills/cucumber-step-definitions/SKILL.md`
- **Installs**: ~40
- **Category**: Tool (reference knowledge)

### Purpose (cucumber-step-definitions)

Reference for writing step definitions in JavaScript/TypeScript, Java, and
Ruby. Covers parameterized steps, regular expressions, data tables, doc strings,
World context, hooks, and the Page Object pattern.

### Automation (cucumber-step-definitions)

- **Generates files**: No
- **Runs commands**: No
- **Provides guidance**: Yes, implementation-focused reference

### Key Instructions (cucumber-step-definitions)

- Keep steps simple and focused -- one action or assertion per step.
- Reuse steps -- write generic steps that work for multiple scenarios.
- Use the World -- share state through World, not global variables.
- Organize by domain -- group related steps together.
- Make steps readable -- step definitions should read like documentation.
- Don't create overly specific steps; create composable ones instead.
- Don't put assertions in Given/When.
- Don't call steps from within steps; extract to helper functions instead.

### Relevance (cucumber-step-definitions)

**Low**. This is purely about test implementation code, not about writing
Gherkin specifications. Only the guidance about composable vs. specific steps
has tangential relevance to writing good scenario text.

---

## 8. Cucumber Fundamentals

- **Source**: `thebushidocollective/han` at
  `plugins/tools/cucumber/skills/cucumber-fundamentals/SKILL.md`
- **Installs**: ~38
- **Category**: Tool (reference knowledge)

### Purpose (cucumber-fundamentals)

Core Cucumber concepts and Gherkin syntax reference. Covers keywords,
feature file structure, Scenario Outlines, tags, data tables, doc strings,
and the good-vs-bad scenario distinction.

### Automation (cucumber-fundamentals)

- **Generates files**: No
- **Runs commands**: No
- **Provides guidance**: Yes, syntax reference

### Key Instructions (cucumber-fundamentals)

- Feature files serve as **executable specifications** (living documentation).
- Written by developers, testers, AND business stakeholders.
- Use **ubiquitous language** (domain terminology consistently).
- Prefer **examples over rules** -- concrete examples clarify requirements.
- Good scenarios are declarative and business-focused; bad scenarios are
  imperative and implementation-focused.
- Includes complete keyword reference: Feature, Scenario, Given, When, Then,
  And, But, Background, Scenario Outline, Examples.

### Relevance (cucumber-fundamentals)

**Low-Medium**. Standard Gherkin syntax reference. The emphasis on scenarios
as "specifications first, tests second" aligns with our goal. The keyword
reference is useful but basic.

---

## 9. Add Cucumber Tests

- **Source**: `decathlon/tzatziki` at `skills/add-cucumber-tests/SKILL.md`
- **Installs**: ~70
- **Category**: Test generation (Java/Spring)

### Purpose (add-cucumber-tests)

Generates Tzatziki-based Cucumber BDD tests (`.feature` files) from a
functional specification. Specifically for Java/Spring projects using the
Tzatziki step definition library for HTTP, JPA, Kafka, MongoDB, OpenSearch,
logging, and MCP testing.

### Workflow (add-cucumber-tests)

This is the most structured and rigorous workflow of all skills surveyed:

1. **Understand the Specification** -- Analyze user input, break into a
   checklist of functional behaviors. Extract external dependencies,
   performance hints, and implicit error paths.
2. **Discover the Project** -- Detect build tool, read step definition
   reference files (`references/steps-core.md`, `steps-http.md`, etc.)
   based on detected dependencies. Catalog error-handling patterns from
   existing feature files.
3. **Check the Bootstrap** -- Search for test runner infrastructure
   (`@Suite`, `@CucumberContextConfiguration`, etc.).
4. **Verify the Environment** -- Run existing tests to confirm the
   infrastructure works. `Tests run: 0` means the runner is broken.
5. **Propose the Plan** -- **Mandatory checkpoint**: present the full plan
   to the user (files to create, behavior-to-scenario mapping, bootstrap
   work, suggested edge cases) and wait for explicit approval.
6. **Implement and Validate** -- Write `.feature` files using exact step
   patterns, run tests, fix any undefined step errors. Repeat until zero
   undefined-step errors remain.

### Automation (add-cucumber-tests)

- **Generates files**: Yes, creates `.feature` files and optionally
  bootstrap/runner classes
- **Runs commands**: Yes, runs Maven/Gradle test commands to validate
- **Provides guidance**: Yes, extensive reference documents for each
  Tzatziki module

### Key Instructions (add-cucumber-tests)

- **Steps come from code, not imagination** -- every step must match a real
  step definition. Inventing step text produces `UndefinedStepException`.
- **Verify the environment before writing tests** -- run at least one
  existing test first.
- **YAML by default** for structured data in doc strings.
- **Cover what was asked, then suggest what was missed** -- generate
  scenarios for requested behaviors, then proactively identify edge cases
  (external service failures, empty data, boundary conditions) and present
  them as optional additions.
- **Mandatory user checkpoint** before writing any file.
- **Reuse what exists** -- don't create duplicate runners or configs.
- **Run tests and inspect output** -- test output is ground truth for
  step validity. Zero undefined-step errors is a hard success criterion.
- **Edge case identification framework**: (a) every external service call
  -- what if it errors or times out? (b) every data collection -- what if
  empty or unexpected? (c) existing test patterns for similar features.

### Relevance (add-cucumber-tests)

**High**. This is the most sophisticated skill in the survey and offers
several patterns directly applicable to our specification skill:

1. **Mandatory user checkpoint** before generating output -- prevents
   wasted effort and ensures alignment.
2. **Structured edge case identification** -- systematically surfaces what
   the user might have missed.
3. **Environment verification** before generation -- ensures the output
   will actually work.
4. **Reference-based step validation** -- steps must come from an
   authoritative source, not imagination.
5. **Success criteria** are concrete and measurable (zero undefined-step
   errors, 100% behavior coverage, user approval obtained).

---

## 10. Playwright Cucumber Expert

- **Source**: `jmr85/e2e-agent-skills` at
  `skills/playwright-cucumber-expert/SKILL.md`
- **Installs**: ~25
- **Category**: Test infrastructure (Playwright + Cucumber)

### Purpose (playwright-cucumber-expert)

Senior BDD automation specialist for `@cucumber/cucumber` + Playwright.
Designs feature files, implements TypeScript step definitions, manages
browser lifecycle, and configures multi-profile test execution for CI/CD.

### Workflow (playwright-cucumber-expert)

1. **Determine complexity level** -- Basic / Intermediate / Advanced /
   Enterprise.
2. **Scaffold** -- Generate directory structure and config.
3. **Write features** -- Gherkin feature files with tags and structure.
4. **Implement steps** -- TypeScript step definitions.
5. **Build Page Objects** -- POM classes via World context.
6. **Configure profiles** -- `cucumber.js` profiles + HTML reporter.
7. **Set up hooks** -- Browser lifecycle in `tests/hooks.ts`.
8. **Integrate CI** -- GitHub Actions with profile-based execution.

### Automation (playwright-cucumber-expert)

- **Generates files**: Yes, scaffolds entire project structure with
  templates from `assets/` directory
- **Runs commands**: Yes, scaffolding scripts
  (`node scripts/scaffold-bdd.mjs --level <1-4>`)
- **Provides guidance**: Yes, extensive reference documents organized
  by topic (setup, structure, features, steps, hooks, tags, reporting,
  anti-patterns)

### Key Instructions (playwright-cucumber-expert)

**MUST DO:**

- Always use `async function (this: PlaywrightWorld)` -- never arrow
  functions.
- Keep Playwright `page` interactions inside Page Objects -- never in
  step definitions.
- Assertions (`expect()`) only in `Then` steps.
- Tag every scenario with domain tag + run-level tag.
- Mirror `features/` folder structure in `step_definitions/`.

**MUST NOT DO:**

- Arrow functions in step definitions (loses `this` binding).
- Playwright interactions directly in step definitions.
- Assertions inside `Given` or `When` steps.
- Share mutable state between scenarios via module-level variables.
- Mix `@playwright/test`'s `test()` runner with Cucumber.
- Write step descriptions referencing UI implementation details.

### Relevance (playwright-cucumber-expert)

**Low-Medium**. Primarily a test infrastructure skill. The tiered
complexity model (Basic > Intermediate > Advanced > Enterprise) with
progressive feature addition is an interesting UX pattern. The reference
document organization (by topic, loaded on demand) is a good information
architecture model. The MUST DO / MUST NOT DO constraint format is clear
and enforceable.

---

## 11. Feature Spec

- **Source**: `steveclarke/dotfiles` at `ai/skills/feature-spec/SKILL.md`
- **Installs**: ~31
- **Category**: Specification document creation

### Purpose (feature-spec)

Creates concise technical specification documents (5-10 pages) through guided
architectural decisions, system contracts, and technical design. Produces a
`spec.md` covering API design, data models, frontend architecture, and
integration points. Part of a larger feature development process (vision >
requirements > spec > plan).

### Workflow (feature-spec)

The skill works through 3 mandatory phases (with an optional 4th):

1. **Phase 1: Context Analysis and Scope Confirmation** -- Review vision and
   requirements documents, examine existing codebase patterns, identify
   similar features. Ask clarifying questions about scope (full-stack vs.
   backend-only, constraints, phase scope). **One question at a time.**
2. **Phase 2: Implementation Design Using Existing Patterns** -- Design
   following established codebase conventions. For backend: data models,
   service contracts, API endpoints, authorization. For frontend: type
   organization, component architecture. Ask only about unique aspects.
3. **Phase 3: Specification Document Creation** -- Create spec with
   recommended section flow: Overview > Architecture > Data > API >
   Authorization > Integration > Frontend > Design/UX > Configuration >
   File Organization > Quality Attributes.
4. **Phase 4 (Optional): Design Brief Creation** -- Extract design-relevant
   information into a standalone `design-brief.md` for designers.

### Automation (feature-spec)

- **Generates files**: Yes, creates `spec.md` and optionally
  `design-brief.md` and updates `discussion-summary.md`
- **Runs commands**: No
- **Provides guidance**: Yes, extensive structure templates and guidelines

### Key Instructions (feature-spec)

- **Specs define architecture and contracts, NOT implementation code.**
- Focus on WHAT and WHY, not HOW to code.
- Include table of contents with systematic section numbering.
- Use requirement cross-references (e.g., "implements REQ-2.1.1").
- Backend/frontend separation: keep API contracts separate from frontend
  types.
- Multi-context architecture: always create separate structures for
  different contexts (internal/external/public) for security isolation.
- Start by creating a TODO list to track phases.
- **Context first**: analyze existing patterns before asking questions.
- **Minimal interaction**: leverage comprehensive context to reduce
  back-and-forth.

### Relevance (feature-spec)

**High**. Although this skill produces traditional specification documents
rather than Gherkin, its structured multi-phase approach (context analysis >
design > document creation) is directly applicable. Key transferable patterns:

1. **Phased workflow with TODO tracking** -- progressive refinement.
2. **Context-first analysis** -- examine existing code before asking
   questions.
3. **One question at a time** -- prevents information overload.
4. **Cross-referencing** -- tracing spec items to requirements.
5. **Section flow optimization** -- sections ordered so each discipline
   reads contiguously.
6. **Concise output** -- 5-10 pages, explain each concept once.
7. **Clear anti-patterns** -- explicit list of pitfalls to avoid.

---

## 12. Feature Requirements

- **Source**: `steveclarke/dotfiles` at
  `ai/skills/feature-requirements/SKILL.md`
- **Installs**: ~30
- **Category**: Requirements document creation

### Purpose (feature-requirements)

Creates structured requirements documents through guided discovery,
practical scoping, and consolidated output. Produces `requirements.md`
with entities, workflows, constraints, and acceptance criteria.

### Workflow (feature-requirements)

3 phases:

1. **Phase 1: Requirements Discovery** -- Ask focused questions one at a
   time: capabilities needed, business entities, data constraints, business
   rules, audiences, interactions, empty states, presentation format,
   security, performance, integrations, compliance.
2. **Phase 2: Practical Focus and Future Planning** -- For each requirement:
   is it immediately practical? Should it go in `requirements.md` or
   `future.md`? Can it be stated in clear language? Is it testable?
3. **Phase 3: Document Generation** -- Apply ID prefixes (US-X.X.X,
   REQ-X.X.X, SC-X), create consolidated document with 10 sections.

### Automation (feature-requirements)

- **Generates files**: Yes, creates `requirements.md`, `future.md`, and
  updates `discussion-summary.md`
- **Runs commands**: No
- **Provides guidance**: Yes, structured discovery process

### Key Instructions (feature-requirements)

- **Requirement ID Format**: `US-X.X.X` (User Stories), `REQ-X.X.X`
  (Requirements), `SC-X` (Success Criteria).
- **Stay at requirements level**: Focus on WHAT and WHY, not HOW. Good:
  "System must track whether event is draft or published." Bad: "Use
  boolean flag for is_draft field."
- **ONE QUESTION AT A TIME** -- wait for answers before proceeding.
- Check if existing system patterns apply (search, file attachments,
  audit trail, multi-tenancy, permissions, tagging, custom fields).
- **Expect iteration** -- requirements get refined. Update ALL related
  sections consistently when they change.
- Keep language clear and conversational, not corporate-speak.

### Relevance (feature-requirements)

**High**. This skill's approach to requirements discovery is highly relevant
to a specification skill that captures requirements in Gherkin format:

1. **Systematic discovery questions** -- the question framework covers
   entities, rules, audiences, interactions, edge cases (empty states),
   and quality attributes.
2. **Practical scoping** -- separating current from future requirements.
3. **Requirement IDs** -- traceable identifiers for cross-referencing.
4. **One question at a time** -- interactive discovery pattern.
5. **Level discipline** -- staying at the right abstraction level
   (requirements, not implementation).

---

## 13. Feature Plan

- **Source**: `steveclarke/dotfiles` at `ai/skills/feature-plan/SKILL.md`
- **Installs**: ~27
- **Category**: Implementation plan creation

### Purpose (feature-plan)

Creates implementation plan documents with development phases, sequencing,
and actionable tasks. Works through 3 phases following established patterns.
Designed to follow after vision > requirements > spec in the feature
development pipeline.

### Workflow (feature-plan)

1. **Phase 1: Determine Plan Structure** -- Analyze spec, assess
   complexity, recommend structure (single plan vs. split by domain).
2. **Phase 2: Design Implementation Approach** -- Identify unique vs.
   established patterns, determine phase dependencies, validate
   sequencing with user.
3. **Phase 3: Generate Plan Documents** -- Create plan with TOC,
   checkbox tasks, cross-references, selective code detail.

### Automation (feature-plan)

- **Generates files**: Yes, creates `plan.md` or `plan-backend.md` /
  `plan-frontend.md`
- **Runs commands**: No
- **Provides guidance**: Yes, implementation sequencing

### Key Instructions (feature-plan)

- **Selective detail strategy**: Unique/novel code gets FULL detail with
  documentation; established patterns get only a reference and what is
  different.
- **Prerequisites as Phase 1** -- external setup, manual configs,
  environment requirements.
- Every implementation phase must be traceable to spec sections.
- No effort sizing estimates or time estimates.
- Checklist tasks ARE the completion criteria.

### Relevance (feature-plan)

**Medium-Low**. As an implementation planning tool, it is downstream from
where our specification skill operates. However, the selective detail
strategy (full detail for novel aspects, reference-only for established
patterns) is applicable to specification output -- write detailed Gherkin
scenarios for complex behavior, reference patterns for standard behavior.
The traceability requirement (every phase traces to spec sections) reinforces
the importance of requirement IDs.

---

## 14. Create Specification

- **Source**: `github/awesome-copilot` at `agents/specification.agent.md`
  (GitHub Copilot agent, not Claude Code skill)
- **Installs**: ~9.4K
- **Category**: Specification document creation

### Purpose (create-specification)

Generates or updates specification documents for new or existing
functionality, structured for use by Generative AIs. This is a GitHub
Copilot agent definition, not a Claude Code skill.

### Workflow (create-specification)

No multi-phase workflow. Operates in "specification mode" where it:

1. Works with the codebase to understand existing functionality.
2. Generates specification files in `/spec/` directory.
3. Follows a detailed template with numbered sections.

### Automation (create-specification)

- **Generates files**: Yes, creates `spec-*.md` files in `/spec/`
- **Runs commands**: No (but has access to VS Code tools)
- **Provides guidance**: Yes, via template structure

### Key Instructions (create-specification)

- Specifications must be **clear, unambiguous, and structured for
  effective use by Generative AIs**.
- Follow established documentation standards; ensure content is
  machine-readable and self-contained.
- **Best Practices for AI-Ready Specifications:**
  - Use precise, explicit, and unambiguous language.
  - Clearly distinguish between requirements, constraints, and
    recommendations.
  - Use structured formatting (headings, lists, tables) for easy parsing.
  - Avoid idioms, metaphors, or context-dependent references.
  - Define all acronyms and domain-specific terms.
  - Include examples and edge cases where applicable.

- **Specification Template Sections:**
  1. Introduction
  2. Purpose and Scope
  3. Definitions
  4. Requirements, Constraints, and Guidelines (with ID prefixes:
     REQ-001, SEC-001, CON-001, GUD-001, PAT-001)
  5. Interfaces and Data Contracts
  6. **Acceptance Criteria** (Given-When-Then format recommended)
  7. **Test Automation Strategy**
  8. Dependencies and External Integrations
  9. Examples and Edge Cases
  10. Validation Criteria
  11. Related Specifications

- File naming: `spec-[a-z0-9-]+.md` with descriptive names starting with
  purpose prefix (schema, tool, data, infrastructure, process,
  architecture, design).

### Relevance (create-specification)

**High**. This is the most relevant non-Gherkin specification skill in the
survey for several reasons:

1. **AI-Ready Specifications** -- the explicit goal of making specifications
   machine-readable and self-contained aligns perfectly with using Gherkin
   as a structured specification format.
2. **Given-When-Then in acceptance criteria** -- this agent already
   recommends Gherkin format for acceptance criteria within traditional
   spec documents, validating our approach of using Gherkin as the primary
   format.
3. **Requirement ID system** -- REQ-001, SEC-001, CON-001, etc. with clear
   prefixes for different requirement types.
4. **9.4K installs** -- high adoption validates demand for specification
   tools.
5. **Definitions section** -- explicitly requires defining all terms, which
   maps to Gherkin's ubiquitous language concept.
6. **Examples and edge cases** -- dedicated section, which is what Gherkin
   scenarios naturally provide.

---

## 15. Bonus: Playwright BDD Skills (thebushidocollective/han)

The han repository also includes three Playwright BDD skills that were not
in the original list but are worth noting:

### 15a. playwright-bdd-configuration

- **Path**:
  `plugins/tools/playwright-bdd/skills/playwright-bdd-configuration/SKILL.md`
- **Purpose**: Expert knowledge for configuring Playwright BDD
  projects using `defineBddConfig()`. Covers installation,
  feature/step paths, custom fixtures, multiple feature sets, i18n,
  and CI integration.
- **Relevance**: **Low**. Infrastructure configuration, not
  specification.

### 15b. playwright-bdd-gherkin-syntax

- **Path**:
  `plugins/tools/playwright-bdd/skills/playwright-bdd-gherkin-syntax/SKILL.md`
- **Purpose**: Comprehensive Gherkin syntax reference for Playwright
  BDD. Covers feature structure, keywords (Given/When/Then/And/But),
  scenario types (basic, outline, background, rule), tags (including
  Playwright-specific: `@skip`, `@only`, `@fail`, `@fixme`), data
  tables, doc strings, i18n, comments, and best practices.
- **Key insight**: Uses the **Rule** keyword to group scenarios under
  business rules -- directly relevant to specification-oriented
  Gherkin.
- **Relevance**: **Medium**. Good Gherkin syntax reference with the
  Rule keyword usage that aligns with specification-focused writing.

### 15c. playwright-bdd-step-definitions

- **Path**:
  `plugins/tools/playwright-bdd/skills/playwright-bdd-step-definitions/SKILL.md`
- **Purpose**: Creating step definitions with `createBdd()`, custom
  parameter types, fixtures, Page Object Model integration, data
  tables, doc strings, and decorator-based steps.
- **Relevance**: **Low**. Test implementation, not specification.

### Han BDD Enforcement Hook

The han repo also includes a BDD enforcement hook
(`plugins/patterns/bdd/hooks/enforce-bdd.md`) that activates automatically
when implementing features. It enforces the Discovery > Development >
Delivery cycle and includes a verification checklist:

- Wrote scenarios based on concrete examples
- Validated scenarios with stakeholders
- Implemented using outside-in TDD
- All scenarios pass
- Scenarios serve as living documentation

**Relevance**: **Medium**. The enforcement hook pattern (automatically
activating BDD practices when feature work is detected) is an interesting
model for ensuring specifications are created before implementation.

---

## 16. Summary and Key Takeaways

### Skills by Category

| Category | Skills | Count |
| -------- | ------ | ----- |
| Reference/Knowledge | bdd-patterns, bdd-scenarios, bdd-principles, bdd-collaboration, cucumber-best-practices, cucumber-step-definitions, cucumber-fundamentals, playwright-bdd-gherkin-syntax | 8 |
| Test Generation | bdd-feature-generator, add-cucumber-tests, playwright-cucumber-expert | 3 |
| Specification/Requirements | feature-spec, feature-requirements, feature-plan, create-specification | 4 |
| Configuration | playwright-bdd-configuration, playwright-bdd-step-definitions | 2 |

### Most Relevant Skills for Our Goal

Ranked by relevance to building a Gherkin specification skill:

1. **create-specification** (github/awesome-copilot) -- Already recommends
   Given-When-Then for acceptance criteria; AI-ready specification design;
   9.4K installs proving demand.

2. **add-cucumber-tests** (decathlon/tzatziki) -- Most sophisticated
   workflow with mandatory user checkpoint, structured edge case
   identification, environment verification, and concrete success criteria.

3. **feature-spec** (steveclarke/dotfiles) -- Multi-phase specification
   workflow with context-first analysis, cross-referencing, and section
   flow optimization.

4. **feature-requirements** (steveclarke/dotfiles) -- Systematic
   requirements discovery with one-question-at-a-time pattern, practical
   scoping, and requirement ID system.

5. **bdd-collaboration** (han) -- Discovery Workshop format and Example
   Mapping technique directly applicable to requirements gathering.

### Key Patterns to Adopt

**From add-cucumber-tests (tzatziki):**

- Mandatory user checkpoint before generating output.
- Structured edge case identification framework (external dependencies,
  empty/boundary data, state/ordering, patterns from existing code).
- Steps/scenarios must come from authoritative sources, not invention.
- Run and validate output; success criteria are concrete and measurable.
- "Cover what was asked, then suggest what was missed."

**From feature-spec and feature-requirements (steveclarke):**

- Multi-phase workflow with TODO tracking.
- Context-first analysis before asking questions.
- One question at a time during discovery.
- Cross-referencing between documents with requirement IDs.
- Concise output with anti-pattern lists.
- Separation of current vs. future scope.

**From create-specification (awesome-copilot):**

- AI-ready specification principles (precise language, no idioms, define
  all terms, include examples and edge cases).
- Given-When-Then format for acceptance criteria.
- Structured requirement ID system with type prefixes.
- Self-contained documents that don't rely on external context.

**From BDD principles and collaboration (han):**

- Example Mapping (rules > examples > questions) as a discovery technique.
- Ubiquitous language development and glossary.
- The Rule keyword for grouping scenarios by business rules.
- Discovery > Development > Delivery cycle.
- Living documentation concept.

**From bdd-feature-generator:**

- Tag conventions for organizing specifications.
- Feature files created BEFORE implementation.
- Analyze existing patterns before generating new content.

### What None of These Skills Do

No existing skill specifically:

- Uses Gherkin as a **requirements/specification format** (rather than
  a test format).
- Combines Gherkin with EARS-style requirement patterns.
- Generates Gherkin specifications from natural language requirements
  without targeting a specific test framework.
- Provides a specification-focused Gherkin skill independent of any
  testing framework (Cucumber, Playwright, Godog, etc.).

This gap confirms the opportunity for our Gherkin specification skill.
