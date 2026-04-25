# Existing Gherkin Claude Code Skills -- Part 2

Analysis of four additional Gherkin-related Claude Code skills
found on the marketplace.

---

## 5. gherkin-authoring (melodic-software/claude-code-plugins)

### Overview

| Field | Value |
| ----- | ----- |
| **Name** | gherkin-authoring |
| **Source** | [melodic-software/claude-code-plugins](https://github.com/melodic-software/claude-code-plugins) |
| **Path in repo** | `plugins/spec-driven-development/skills/gherkin-authoring/` |
| **Install count** | 9 |
| **Part of** | A larger "spec-driven-development" plugin with multiple related skills |

### Purpose

A reference-oriented skill for authoring Gherkin acceptance criteria and BDD
feature files. It acts as a syntax guide, best-practices reference, and
integration helper -- particularly targeting .NET projects using Reqnroll
(successor to SpecFlow). It is part of a broader "spec-driven-development"
plugin ecosystem that also includes canonical-spec-format, spec-management,
and EARS-authoring skills.

### Workflow

1. User invokes the skill when writing Given/When/Then scenarios, feature files,
   or BDD-style specifications.
2. The skill provides structured reference material covering:
   - Full Gherkin syntax (Feature, Scenario, Scenario Outline, Background, etc.)
   - The Three A's pattern (Arrange/Act/Assert mapped to Given/When/Then)
   - Single behavior per scenario principle
   - Declarative vs. imperative style guidance
   - Scenario Outline usage with Examples tables
   - Tags and their categories
3. It offers integration guidance for mapping Gherkin to a "canonical spec" YAML
   format used by the broader plugin ecosystem.
4. It provides Reqnroll/.NET-specific code samples for step definitions and
   project setup.
5. The agent uses Read, Glob, Grep, Write, and Edit tools to work with the
   user's codebase.

### Automation

This skill is primarily a **guidance and reference skill**. It does not
implement an automated generation pipeline or multi-agent loop. The agent
receives the reference material and uses it to assist the user in writing
or reviewing Gherkin. It can write/edit files directly using the allowed tools.

### Key Gherkin Guidelines Enforced

- Single behavior per scenario (no multi-behavior scenarios)
- Declarative style preferred over imperative
- Use domain language, not technical jargon
- Background section should be short (1-3 steps), only for truly common setup
- Scenario Outline for parameterized tests with 3+ examples
- Tags organized by category: priority, type, feature, state, non-functional
- Given establishes context only; When contains single action; Then asserts
  observable outcomes
- No UI coupling or implementation details in steps
- Step reusability through parameterized patterns

### Anti-Patterns Explicitly Called Out

- Feature-length scenarios
- Imperative steps
- Technical jargon in steps
- UI-coupled steps
- Missing Background (duplicated Given steps)
- Too many Examples rows

### Strengths

- **Comprehensive reference material**: Includes a full syntax reference,
  best-practices guide, and validation checklist -- all well-organized.
- **Part of a larger ecosystem**: Integrates with canonical-spec-format,
  EARS-authoring, and spec-management skills, enabling end-to-end
  specification workflows.
- **Reqnroll/.NET integration**: Provides specific code samples for .NET BDD
  setup, making it useful for .NET teams.
- **Canonical spec mapping**: Shows how Gherkin acceptance criteria map to a
  structured YAML specification format, bridging the gap between specs and
  tests.
- **Good/bad examples**: Every guideline includes both positive and negative
  examples with clear explanations.
- **Validation checklist**: Provides a concrete checklist for scenario quality
  review before finalizing.

### Weaknesses

- **No automated generation**: Unlike the gherkin-generator-skill, there is no
  multi-agent loop or automated iteration. It relies entirely on the agent
  following the reference material.
- **No scoring or review mechanism**: No structured way to evaluate the quality
  of generated Gherkin. Quality depends on the agent's adherence to guidelines.
- **Tied to a proprietary specification ecosystem**: The canonical spec mapping
  and EARS integration are specific to this plugin's ecosystem and may not
  apply to other BDD workflows.
- **No language localization guidance**: Doesn't address writing Gherkin in
  non-English languages (despite Gherkin's multi-language support).
- **Limited to .NET/Reqnroll**: The framework integration is only for .NET. No
  guidance for Cucumber (Java/JS/Ruby), pytest-bdd, Behave, or other
  frameworks.

### Supporting Files (gherkin-authoring)

| File | Description |
| ---- | ----------- |
| `references/syntax-reference.md` | Complete Gherkin syntax covering keywords, step patterns, data tables, doc strings, Scenario Outline, tags, Background, Rule keyword, comments, language declaration. Very thorough. |
| `references/best-practices.md` | Detailed BDD best practices covering: behavior over implementation, single behavior per scenario, declarative over imperative, step writing patterns, Background usage, Scenario Outline organization, tagging strategy, data tables, doc strings, anti-patterns, language and readability, Reqnroll-specific practices, and maintenance guidelines. |

### Full SKILL.md Content (gherkin-authoring)

> ```markdown
> ---
> name: gherkin-authoring
> description: Gherkin acceptance criteria authoring. Use when writing Given/When/Then
>   scenarios, feature files, or BDD-style specifications. Provides syntax reference,
>   best practices, and Reqnroll integration guidance.
> allowed-tools: Read, Glob, Grep, Write, Edit
> ---
>
> # Gherkin Authoring
>
> Gherkin/BDD acceptance criteria authoring for executable specifications.
>
> ## When to Use This Skill
>
> **Keywords:** Gherkin, Given/When/Then, BDD, behavior-driven development, feature
> files, scenarios, acceptance criteria, Reqnroll, Cucumber, SpecFlow, executable
> specifications
>
> **Use this skill when:**
> - Writing acceptance criteria in Given/When/Then format
> - Creating .feature files for BDD testing
> - Converting requirements to executable specifications
> - Setting up Reqnroll tests in .NET projects
> - Understanding Gherkin syntax and best practices
>
> [... extensive content covering Quick Syntax Reference, Step Keywords, The Three A's
> Pattern, Single Behavior Per Scenario, Declarative vs Imperative Style, Background
> Section, Scenario Outline, Tags, Integration with Canonical Spec, Best Practices,
> Reqnroll Integration (.NET), Anti-Patterns, and Validation Checklist ...]
> ```

---

## 6. gherkin-expert (rysweet/amplihack)

### Overview (gherkin-expert)

| Field | Value |
| ----- | ----- |
| **Name** | gherkin-expert |
| **Source** | [rysweet/amplihack](https://github.com/rysweet/amplihack) |
| **Path in repo** | `.claude/skills/gherkin-expert/` |
| **Install count** | 7 |
| **Part of** | The "amplihack" framework -- a large multi-agent agentic coding framework |

### Purpose (gherkin-expert)

An expert-level advisory skill for Gherkin/BDD specification writing. Rather
than automating Gherkin generation, it provides expert consultation on when and
how to use Gherkin, scenario design, and BDD methodology. A distinguishing
feature is its emphasis on using Gherkin as a prompt engineering technique to
improve AI code generation quality (citing +26% improvement over English-only
prompts based on their experiments).

### Workflow (gherkin-expert)

1. The skill activates when the user mentions Gherkin, BDD, Given/When/Then,
   feature files, acceptance criteria, Cucumber, SpecFlow, or behavioral
   specifications.
2. It delegates to a `gherkin-expert` agent (referenced as
   `amplihack:specialized:gherkin-expert`) with knowledge of:
   - Gherkin syntax and idioms
   - BDD methodology (discovery workshops, living documentation, specification
     by example)
   - Scenario design principles
   - Domain modeling through scenarios
   - Using Gherkin specs as AI prompt context
3. The skill includes a "judgment call" section that explicitly states when
   Gherkin is and isn't the right tool -- a unique feature among Gherkin skills.
4. Users interact through slash-command-style invocations (e.g.,
   `/gherkin-expert Write Gherkin scenarios for our user authentication flow`).

### Automation (gherkin-expert)

This skill provides **expert guidance** rather than automated generation. It
delegates to a specialized agent but does not implement a generation/review
loop. The skill file is relatively compact (about 80 lines), suggesting the
bulk of the intelligence resides in the referenced agent definition, which is
part of the amplihack framework's agent system.

### Key Gherkin Guidelines

- Single-behavior focus per scenario
- Declarative style, avoiding implementation details
- Ubiquitous language from domain modeling
- Use Gherkin strategically -- not for everything (explicit guidance on when
  English requirements are sufficient)

### "When Gherkin Adds Value" Decision Framework (Unique)

**Good fit:**

- Complex multi-step behavioral requirements with many edge cases
- Multi-actor scenarios
- Business rules with combinatorial conditions (scenario outlines)
- Acceptance criteria that stakeholders need to validate
- Features where "what done looks like" is ambiguous in English

**English is fine:**

- Simple CRUD operations with obvious behavior
- Internal tooling with a single developer as audience
- Config changes, styling, documentation
- Requirements where the hard part is algorithm design, not behavior spec

### Strengths (gherkin-expert)

- **Pragmatic "when to use" guidance**: Unlike other skills that assume Gherkin
  is always appropriate, this skill explicitly guides users on when Gherkin adds
  value and when plain English is sufficient. This is valuable for avoiding
  over-specification.
- **AI prompt engineering angle**: Cites experimental evidence (+26%
  improvement) for using Gherkin as structured context in AI code generation
  prompts. This connects BDD to the modern AI-assisted development workflow.
- **BDD methodology coverage**: Goes beyond syntax to cover discovery workshops,
  living documentation, and specification by example -- the broader BDD
  ecosystem.
- **Part of a larger framework**: Sits within the amplihack multi-agent system,
  so it can potentially coordinate with other specialized agents.
- **Lightweight and focused**: The SKILL.md is concise and doesn't try to be
  a complete Gherkin reference; it focuses on expert advisory use cases.

### Weaknesses (gherkin-expert)

- **Minimal concrete guidance**: The SKILL.md itself is thin compared to other
  skills. It lacks inline syntax references, example scenarios, or best
  practices. The actual intelligence is presumably in the agent definition,
  which we can't fully evaluate.
- **Agent dependency**: Relies on an `amplihack:specialized:gherkin-expert`
  agent that is defined elsewhere in the framework. The skill is not
  self-contained.
- **No file generation workflow**: Does not describe how to actually create
  .feature files or integrate with test frameworks. It is advisory only.
- **Tied to amplihack framework**: The skill is designed to work within the
  amplihack multi-agent ecosystem and may not work well as a standalone skill.
- **No review or validation mechanism**: No structured way to evaluate the
  quality of the Gherkin the agent produces.
- **No supporting reference files**: The skill directory contains only the
  SKILL.md file; no reference documents, templates, or examples.

### Full SKILL.md Content (gherkin-expert)

> ```markdown
> ---
> name: gherkin-expert
> version: 1.0.0
> description: Gherkin/BDD specification expert for writing behavioral scenarios,
>   acceptance criteria, and applying structured specifications to improve code
>   generation quality
> activation_keywords:
>   - "Gherkin"
>   - "BDD"
>   - "behavior-driven"
>   - "Given When Then"
>   - "Given/When/Then"
>   - "Feature:"
>   - "Scenario:"
>   - "Scenario Outline:"
>   - "acceptance criteria"
>   - "behavioral specification"
>   - "feature file"
>   - "cucumber"
>   - "SpecFlow"
> agent: amplihack:specialized:gherkin-expert
> ---
>
> # Gherkin Expert Skill
>
> ## Purpose
> Provides expert-level Gherkin/BDD specification assistance for writing behavioral
> scenarios that clarify acceptance criteria and improve downstream code generation
> quality.
>
> ## When This Skill Activates
> - User asks to write or review Gherkin feature files or scenarios
> - User needs help structuring complex acceptance criteria
> - User wants to translate business requirements into Given/When/Then format
> - User asks about BDD methodology or scenario design
> - User wants behavioral specifications for multi-actor or multi-step workflows
> - User mentions Cucumber, SpecFlow, or BDD frameworks
> - User is working on features with complex acceptance criteria that would benefit
>   from structured scenarios
>
> ## How It Works
> This skill delegates to the `gherkin-expert` agent which has knowledge of:
> 1. Gherkin syntax and idioms
> 2. BDD methodology
> 3. Scenario design
> 4. Domain modeling
> 5. AI prompt improvement (using Gherkin specs as prompt context, +26% improvement)
>
> ## When Gherkin Adds Value (Judgment Call)
> [... guidance on good fit vs. "English is fine" ...]
>
> ## Usage Examples
> [... slash-command examples ...]
>
> ## Key Resources
> - Gherkin experiment results: experiments/hive_mind/gherkin_v2_recipe_executor/
> - Issue #3939: Formal specification integration roadmap
> - Gherkin reference: https://cucumber.io/docs/gherkin/reference/
> ```

---

## 7. gherkin-generator-skill (ehdez73/agent-skills)

### Overview (gherkin-generator-skill)

| Field | Value |
| ----- | ----- |
| **Name** | gherkin-generator-skill |
| **Source** | [ehdez73/agent-skills](https://github.com/ehdez73/agent-skills) |
| **Path in repo** | `skills/gherkin-generator-skill/` |
| **Install count** | 7 |
| **Part of** | A small skills repo with 2 skills (3-amigos-skill and gherkin-generator-skill) |

### Purpose (gherkin-generator-skill)

An automated Gherkin generation skill that transforms functional requirements
into production-ready `.feature` files through a two-agent iterative loop. A
"generator agent" creates the Gherkin, and a "reviewer agent" validates
coverage, structure, and clarity. The loop runs up to 5 iterations, fixing
issues automatically until the reviewer approves (score >= 85).

This is the most sophisticated and automated of all the Gherkin skills analyzed.

### Workflow (gherkin-generator-skill)

1. **Input validation**: User provides functional requirements,
   business context, and feature/module name. If anything is
   missing, the skill asks explicitly.
2. **Iteration loop** (max 5 rounds):
   a. Invoke `gherkin-generator-agent` with requirements, context, and any
      previous feedback.
   b. Generator returns a valid Gherkin `.feature` code block (no explanations).
   c. Invoke `gherkin-reviewer-agent` with the generated Gherkin and original
      requirements.
   d. Reviewer returns structured JSON: `{approved, score, issues, suggestions,
      annotated_gherkin}` with severity levels (BLOCKING, MAJOR, MINOR, INFO).
   e. If approved or score >= 85: stop and deliver.
   f. If not: pass feedback to generator for next iteration.
3. **Delivery**: Present final `.feature` file with score, summary, iteration
   count, and offer to save or refine further.

### Automation (gherkin-generator-skill)

This is the **most automated** of all Gherkin skills:

- **Two-agent architecture**: Separate generator and reviewer agents with
  independent concerns.
- **Automated iteration loop**: Up to 5 rounds of generate-review-fix without
  user intervention.
- **Structured scoring**: 100-point rubric across 5 dimensions with clear
  approval thresholds.
- **File generation**: Produces a complete `.feature` file ready for use.
- **Safety limits**: 5-iteration maximum prevents infinite loops.

### Key Gherkin Guidelines Enforced (gherkin-generator-skill)

The skill enforces a comprehensive set of rules through its reviewer agent:

**Structure:**

- Single Feature per file
- Feature header with user story context (As a / I want / So that)
- Background only if 3+ scenarios share identical Given steps
- Descriptive scenario names (describe behavior, not action sequence)

**Step semantics:**

- Given = system state/precondition (not actions)
- When = one action per step (no UI details, no multi-actions)
- Then = observable results (no implementation/technical details)
- And/But = continuation of previous step type (no mixing)

**Data and examples:**

- Realistic values (not "test123", "foo", "abc")
- Inline values in double quotes
- Scenario Outline + Examples for data variants
- Column names matching step placeholders

**Tags:**

- @smoke for critical path
- @happy-path for standard successful flow
- @edge-case for boundary values
- @error-handling for errors and validation failures
- @regression for non-regression scenarios

**Coverage:**

- 100% of requirements must have at least one scenario
- Both happy path AND error/validation flows required
- Scenario Outline for requirements with variants

### Scoring Rubric (100 points)

| Dimension | Points | Details |
| --------- | ------ | ------- |
| Requirements Coverage | 30 | Happy path (15) + Error flows (15) |
| Syntactic Quality & Structure | 20 | Valid syntax (8) + Background (4) + Outline (4) + Tags (4) |
| Step Clarity & Maintainability | 25 | Given clarity (8) + When actions (9) + Then results (8) |
| Scenario Independence | 15 | Isolation (10) + No cross-dependencies (5) |
| Realism & Usability | 10 | Realistic data (5) + Descriptive names (5) |

### Approval Criteria

- **Approved**: Zero BLOCKING issues AND score >= 85 AND <= 2 MAJOR issues
- **Also approved**: Zero BLOCKING + Zero MAJOR AND score >= 80
- **Not approved**: Any BLOCKING issues OR >= 3 MAJOR issues OR score < 80

### Strengths (gherkin-generator-skill)

- **Most complete automation**: The two-agent generate-review loop is unique
  among Gherkin skills. It provides genuine automated quality assurance.
- **Structured scoring rubric**: The 100-point rubric across 5 dimensions
  provides objective, repeatable quality assessment.
- **Severity-based issue classification**: BLOCKING/MAJOR/MINOR/INFO levels
  give clear prioritization for fixes.
- **Rich supporting documentation**: 5 additional files (generator-agent.md,
  reviewer-agent.md, gherkin-rules.md, gherkin-best-practices.md,
  workflow-implementation.md) provide deep reference material.
- **Annotated Gherkin output**: The reviewer annotates the Gherkin with inline
  comments showing exactly what needs fixing and why.
- **Safety limits**: The 5-iteration cap prevents runaway loops.
- **100% coverage requirement**: Every functional requirement must map to at
  least one scenario.
- **Clear input checklist**: Explicitly requires functional requirements,
  business context, and feature name before proceeding.
- **Multi-language support**: Instructions note to detect requirements language
  and use it consistently throughout.

### Weaknesses (gherkin-generator-skill)

- **Complexity**: The two-agent loop adds significant complexity. Each
  iteration requires invoking two sub-agents, parsing JSON, and managing
  state across iterations. This could be slow and expensive in token usage.
- **No framework integration**: Unlike gherkin-authoring, there is no guidance
  on connecting generated .feature files to specific test frameworks (Cucumber,
  Reqnroll, pytest-bdd, etc.).
- **Agent-internal quality**: The quality ultimately depends on the LLM playing
  both generator and reviewer roles convincingly. In practice, the reviewer
  may be biased toward approving (or over-criticizing) since it's the same
  underlying model.
- **No existing codebase integration**: The skill generates feature files from
  requirements in isolation. It doesn't scan the existing codebase for step
  definitions, existing features, or domain patterns.
- **Rigid iteration limit**: 5 iterations may not be enough
  for complex features, and there's no guidance on what to do
  when max iterations are reached with a low score.
- **Language inconsistency in examples**: Despite the rule about consistent
  language, some examples in the generator-agent.md show English used even
  when discussing multi-language support.

### Supporting Files (gherkin-generator-skill)

| File | Description |
| ---- | ----------- |
| `agents/generator-agent.md` | Detailed instructions for the generator agent: input/output format, generation rules, how to handle iteration feedback, comprehensive anti-patterns, example inputs and outputs for both first iteration and subsequent iterations, and a pre-return checklist. ~13KB. |
| `agents/reviewer-agent.md` | Detailed instructions for the reviewer agent: 100-point scoring rubric across 5 dimensions, severity levels with examples, approval decision logic, 10-step review process, annotated Gherkin format with inline comments, common issues to look for by category, and a complete example review output. ~11KB. |
| `references/gherkin-rules.md` | Combined rules for both agents covering: mandatory structure, Given/When/Then semantics, data and examples, tags, language consistency, approval criteria checklist, common anti-patterns with good/bad examples, and separate instruction sections for generator and reviewer. ~8KB. |
| `references/gherkin-best-practices.md` | Best practices reference covering: anatomy of a .feature file, step rules for Given/When/Then, Scenario Outline and Examples usage, recommended tags, common anti-patterns (with 5 detailed examples), and a quality checklist. ~7KB. |
| `references/workflow-implementation.md` | Architecture diagram and step-by-step process for the two-agent iterative cycle, including: system architecture, 5 detailed steps (validate, generate, review, loop, deliver), and configuration settings (max iterations, language detection, approval threshold). ~3KB. |

### Full SKILL.md Content (gherkin-generator-skill)

> ```markdown
> ---
> name: gherkin-generator-skill
> description: >
>   **Transforms functional requirements into production-ready Gherkin (BDD)
>   scenarios** through automated two-agent iteration. The generator creates
>   `.feature` files; the reviewer validates coverage, structure, and
>   clarity--fixed automatically until approved (score >= 85).
>
>   **MUST HAVE**: Explicit functional requirements + business context.
>   Missing these? Ask explicitly.
>
>   **USE THIS SKILL** when:
>   - User provides functional requirements + asks to "generate Gherkin",
>     "write BDD scenarios", "create feature tests"
>   - User has a requirements document and wants executable acceptance
>     criteria / test cases
>   - User mentions transforming specs into Given/When/Then format
>   - User needs test scenarios covering happy paths AND error handling
>
>   **DELIVERS**: A syntax-valid, requirement-complete `.feature` file with
>   100% functional coverage, clear Given/When/Then steps (no UI coupling),
>   independent scenarios, and appropriate tags.
> ---
>
> # Skill: Gherkin Generator (BDD)
>
> Transforms functional requirements -> automated iteration -> production-ready
> `.feature` files.
>
> [... extensive content covering Quick Input Checklist, Execution Flow diagram,
> Agent Roles (generator + reviewer), Approval Criteria table, Detailed Reference
> Guides, Typical Execution walkthrough, Key Design Principles, Common Refinement
> Requests, Example Input, Example Output ...]
> ```

---

## 8. bdd-gherkin-style (moxa/sw)

### Overview (bdd-gherkin-style)

| Field | Value |
| ----- | ----- |
| **Name** | bdd-gherkin-style |
| **Source** | [moxa/sw](https://github.com/moxa/sw) |
| **Install count** | 11 |
| **Status** | **INACCESSIBLE -- Repository not found** |

### Investigation Results

The repository `moxa/sw` is not accessible:

- GitHub API returns HTTP 404 (Not Found) for the repository.
- The GitHub user/organization `moxa` has no public repositories.
- Web fetch of the repository URL returns a 404 error.
- Searching GitHub for "bdd-gherkin-style" in code and repositories returns
  zero results.
- No cached or mirrored copies of the repository could be found.

The repository was either:

1. Made private after the skill was published to the marketplace
2. Deleted entirely
3. The owner/repo name may have been changed

### What We Know

Based on the name "bdd-gherkin-style" and the install count of 11 (the highest
among the four skills in this analysis), this skill likely provided guidance
for writing BDD-style Gherkin scenarios. However, without access to the source
code, no detailed analysis can be performed.

### Assessment

**Unable to evaluate.** The repository is not publicly accessible. This is a
significant concern for users who may have installed this skill -- they cannot
review its source code, report issues, or contribute improvements. It also
means the skill cannot be updated or maintained.

---

## Comparative Analysis

### Summary Table

| Feature | gherkin-authoring | gherkin-expert | gherkin-generator | bdd-gherkin-style |
| ------- | ----------------- | -------------- | ----------------- | ----------------- |
| **Installs** | 9 | 7 | 7 | 11 |
| **Approach** | Reference/guidance | Expert advisory | Automated generation | N/A (inaccessible) |
| **Automation** | None (manual) | None (advisory) | Two-agent loop | Unknown |
| **File generation** | Via agent tools | None described | Yes (.feature) | Unknown |
| **Review mechanism** | Checklist | None | Automated scoring (100-pt rubric) | Unknown |
| **Framework integration** | .NET/Reqnroll | Framework-agnostic | None | Unknown |
| **Multi-language** | No | No | Yes (detect + use) | Unknown |
| **Supporting files** | 2 reference docs | 0 | 5 docs (agents + refs) | Unknown |
| **Self-contained** | Yes | No (needs amplihack) | Yes | Unknown |
| **When-to-use guidance** | No | Yes (unique) | No | Unknown |

### Key Differentiators

1. **gherkin-authoring** excels as a comprehensive reference with .NET/Reqnroll
   integration and connection to a broader specification ecosystem. Best for
   teams already using the melodic-software plugin suite.

2. **gherkin-expert** is unique in providing pragmatic "when to use Gherkin"
   guidance and connecting BDD to AI prompt engineering. Best as an advisory
   tool for teams deciding whether Gherkin is appropriate for a given feature.

3. **gherkin-generator-skill** is the most automated and sophisticated,
   implementing a genuine generate-review-fix loop with structured scoring.
   Best for teams that want to convert requirements documents into .feature
   files with minimal manual intervention.

4. **bdd-gherkin-style** cannot be evaluated due to repository inaccessibility.

### Common Patterns Across Skills

All accessible skills share these Gherkin best practices:

- **Single behavior per scenario**: Universally enforced
- **Declarative over imperative**: All emphasize intent over UI mechanics
- **No UI coupling**: Steps should describe actions, not click targets
- **No implementation details in Then**: Observable outcomes only
- **Scenario independence**: No cross-scenario state dependencies
- **Realistic test data**: Avoid "test123" and "foo" placeholder data
- **Standard tag taxonomy**: @smoke, @happy-path, @edge-case, @error-handling

### Gaps Across All Skills

None of the analyzed skills address:

1. **Step definition code generation**: Generating the glue code that connects
   .feature files to test frameworks
2. **Living documentation**: Generating documentation from feature files
3. **Existing feature file analysis**: Reviewing and improving existing .feature
   files already in the codebase
4. **CI/CD integration**: Connecting generated features to test pipelines
5. **Coverage analysis**: Comparing feature files against existing code to
   identify untested areas
6. **Collaboration workflows**: Facilitating BDD discovery workshops between
   stakeholders, developers, and testers (though ehdez73's companion
   3-amigos-skill partially addresses this)
