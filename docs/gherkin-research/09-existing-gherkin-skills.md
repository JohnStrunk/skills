# Existing Gherkin / BDD Skills: Consolidated Survey

Research date: 2026-04-15

## Overview

A comprehensive survey of existing Claude Code skills related to Gherkin, BDD,
Cucumber, and software specification. Skills were found via `npx skills search`
on skills.sh, GitHub repository searches, and mcpmarket.com.

**Total skills analyzed: 22+** across four detailed research files:

- [Part 1](09-existing-gherkin-skills-part1.md) — 4 Gherkin-specific skills
  from skills.sh (cucumber-gherkin, playwright-bdd-gherkin-syntax,
  bdd-gherkin-specification, gherkin)
- [Part 2](09-existing-gherkin-skills-part2.md) — 4 additional Gherkin skills
  from skills.sh (gherkin-authoring, gherkin-expert, gherkin-generator-skill,
  bdd-gherkin-style)
- [Part 3](09-existing-gherkin-skills-part3.md) — 13 broader
  BDD/Cucumber/spec skills (bdd-feature-generator, han BDD plugin
  suite, add-cucumber-tests, playwright-cucumber-expert, steveclarke
  feature pipeline, create-specification)
- [GitHub & Other Sources](#github-and-other-sources) — Skills from
  mcpmarket.com, standalone GitHub repos, and project-embedded skills
  (below)

---

## Skills Found on skills.sh

Via `npx skills search gherkin`, `npx skills search bdd`, and
`npx skills search cucumber`:

### Gherkin-Specific

| Skill | Publisher | Installs | Type | Detailed Analysis |
| ------- | --------- | -------- | ---- | ----------------- |
| cucumber-gherkin | el-feo/ai-context | 112 | Reference (Ruby/Rails) | [Part 1 §1](09-existing-gherkin-skills-part1.md) |
| playwright-bdd-gherkin-syntax | thebushidocollective/han | 59 | Reference (Playwright) | [Part 1 §2](09-existing-gherkin-skills-part1.md) |
| bdd-gherkin-specification | jzallen/fred_simulations | 55 | Reference (framework-agnostic) | [Part 1 §3](09-existing-gherkin-skills-part1.md) |
| bdd-gherkin-style | moxa/sw | 11 | Unknown (repo inaccessible) | [Part 2 §8](09-existing-gherkin-skills-part2.md) |
| gherkin | tsipotu/gherkin-skill | 10 | **Interactive workflow** | [Part 1 §4](09-existing-gherkin-skills-part1.md) |
| gherkin-authoring | melodic-software/claude-code-plugins | 9 | Reference (.NET/Reqnroll) | [Part 2 §5](09-existing-gherkin-skills-part2.md) |
| gherkin-expert | rysweet/amplihack | 7 | Advisory (multi-agent) | [Part 2 §6](09-existing-gherkin-skills-part2.md) |
| gherkin-generator-skill | ehdez73/agent-skills | 7 | **Automated generation** | [Part 2 §7](09-existing-gherkin-skills-part2.md) |

### BDD & Cucumber

| Skill | Publisher | Installs | Type | Detailed Analysis |
| ------- | --------- | -------- | ---- | ----------------- |
| bdd-feature-generator | moxa/sw | 1,200 | Generation (Golang-specific) | [Part 3 §1](09-existing-gherkin-skills-part3.md) |
| bdd-patterns | thebushidocollective/han | 105 | Reference | [Part 3 §2](09-existing-gherkin-skills-part3.md) |
| bdd-scenarios | thebushidocollective/han | 74 | Reference | [Part 3 §3](09-existing-gherkin-skills-part3.md) |
| cucumber-best-practices | thebushidocollective/han | 74 | Reference | [Part 3 §8](09-existing-gherkin-skills-part3.md) |
| add-cucumber-tests | decathlon/tzatziki | 70 | **Interactive workflow** | [Part 3 §9](09-existing-gherkin-skills-part3.md) |
| bdd-principles | thebushidocollective/han | 59 | Reference | [Part 3 §4](09-existing-gherkin-skills-part3.md) |
| cucumber-step-definitions | thebushidocollective/han | 40 | Reference | [Part 3 §7](09-existing-gherkin-skills-part3.md) |
| cucumber-fundamentals | thebushidocollective/han | 38 | Reference | [Part 3 §6](09-existing-gherkin-skills-part3.md) |
| playwright-cucumber-expert | jmr85/e2e-agent-skills | 25 | Reference/Generation | [Part 3 §10](09-existing-gherkin-skills-part3.md) |

### Specification & Requirements

| Skill | Publisher | Installs | Type | Detailed Analysis |
| ------- | --------- | -------- | ---- | ----------------- |
| create-specification | github/awesome-copilot | 9,400 | **Interactive workflow** | [Part 3 §14](09-existing-gherkin-skills-part3.md) |
| feature-spec | steveclarke/dotfiles | 31 | **Interactive workflow** | [Part 3 §11](09-existing-gherkin-skills-part3.md) |
| feature-requirements | steveclarke/dotfiles | 30 | **Interactive workflow** | [Part 3 §12](09-existing-gherkin-skills-part3.md) |
| feature-plan | steveclarke/dotfiles | 27 | Implementation planning | [Part 3 §13](09-existing-gherkin-skills-part3.md) |

---

## GitHub and Other Sources

Additional skills found via GitHub search and mcpmarket.com that are not
listed on skills.sh:

| Skill | Source | Type | Notable |
| ----- | ------ | ---- | ------- |
| doc-bdd | vladm3105/aidoc-flow-framework | Document lifecycle (EARS Layer 3 → BDD Layer 4) | Most sophisticated; 90% quality gate, 8 scenario categories, formal traceability |
| behavior-driven-development | FradSer/dotclaude | Three-phase BDD (Discovery → Formulation → Automation) | Iron Law: no production code without a failing test |
| tdd-bdd-gherkin | jcorpac/ai-skills-library | Reference | Plain language emphasis, early stakeholder involvement |
| bdd-scenario-writing | vamsigudipati | 10-step generation framework | Outputs gap lists and scenario-to-spec mapping tables |
| BDD Gherkin Testing Patterns | majiayu000/claude-skill-registry | Reference (multi-framework) | Supports 10+ AI coding agents, not just Claude |
| E2E Cucumber + Playwright | langgenius/dify | Project-embedded | Dify-specific, not reusable |

### mcpmarket.com Skills

8 additional skills found on mcpmarket.com (Cucumber Fundamentals, Cucumber
Best Practices, Cucumber Step Definitions, BDD Skill, BDD Scenario Builder,
Gherkin Acceptance Criteria, BDD Principles, Rails Requirements Gherkin Writer).
These appear to be community contributions with limited documentation. Many
overlap with the thebushidocollective/han suite on skills.sh.

---

## Skill Categorization

| Category | Count | Skills |
| -------- | ----- | ------ |
| **Reference/Knowledge** | 14 | Most skills — provide Gherkin syntax, best practices, patterns as contextual knowledge for the agent |
| **Interactive Workflow** | 4 | gherkin (tsipotu), add-cucumber-tests (tzatziki), feature-spec (steveclarke), create-specification (awesome-copilot) |
| **Automated Generation** | 3 | gherkin-generator-skill (ehdez73), bdd-feature-generator (moxa), doc-bdd (vladm3105) |
| **Inaccessible** | 1 | bdd-gherkin-style (moxa/sw — repo returns 404) |

---

## Key Findings

### 1. Most skills are passive references, not active workflows

14 of 22 skills are knowledge dumps — they load Gherkin syntax and best
practices into the agent's context but define no step-by-step workflow.
Only 4 skills define an interactive process (ask questions → discover
requirements → generate scenarios → review).

### 2. No skill uses Gherkin as a specification format

Every Gherkin skill targets **test automation** (Cucumber, Playwright, Godog).
None use Gherkin as a **requirements/specification format** independent of
test frameworks. This is the primary gap our skill will fill.

### 3. No skill integrates EARS with Gherkin

The doc-bdd skill from vladm3105/aidoc-flow-framework references EARS as
"Layer 3" in its document lifecycle, but doesn't actually implement EARS
pattern detection or EARS-to-Gherkin conversion. No other skill mentions EARS.

### 4. The most sophisticated skills are the least installed

| Skill | Sophistication | Installs |
| ----- | ------------- | -------- |
| gherkin-generator-skill (two-agent loop, 100-point scoring) | High | 7 |
| gherkin (interactive workflow, conflict detection, glossary) | High | 10 |
| cucumber-gherkin (reference card, Ruby-specific) | Low | 112 |

Install count correlates with publisher visibility and ecosystem size,
not skill quality.

### 5. Best patterns to adopt from existing skills

**From tsipotu/gherkin-skill:**

- Ask clarifying questions before writing scenarios
- Scan for existing .feature files to detect conflicts
- Check project glossary for ubiquitous language
- Match existing style conventions

**From ehdez73/gherkin-generator-skill:**

- Two-agent loop (generator + reviewer) with iterative refinement
- 100-point scoring rubric (coverage, syntax, clarity, independence, realism)
- Structured approval criteria with minimum score threshold

**From decathlon/tzatziki add-cucumber-tests:**

- Mandatory user checkpoint before generating output
- Structured edge case identification (external deps, boundaries,
  state, patterns)
- Steps/scenarios must come from authoritative sources, not invention

**From steveclarke/dotfiles feature-spec:**

- Multi-phase workflow (context analysis → requirements → specification → plan)
- Context-first: analyze existing code before asking questions
- One question at a time to prevent information overload
- Cross-referencing via requirement IDs

**From github/awesome-copilot create-specification:**

- Already recommends Given-When-Then for acceptance criteria
- "AI-ready specifications" design philosophy
- 9.4K installs proves demand for specification skills

### 6. Anti-patterns observed in existing skills

- **Knowledge dumps without workflow** — loading 10KB of reference material
  into context without telling the agent what to *do* with it
- **Framework coupling** — skills that only work with one test runner
  (Ruby/Cucumber, Playwright-bdd, Golang/Godog)
- **No validation** — most skills generate .feature files but never check
  if they parse correctly or follow best practices
- **No iteration** — most skills generate once and stop; only
  gherkin-generator-skill implements a review loop
- **Missing "when not to use"** — only 2 skills (bdd-gherkin-specification,
  gherkin-expert) help users decide if Gherkin is appropriate

---

## Opportunity Summary

Our planned skill has a clear differentiation:

1. **Gherkin for specification, not just testing** — use Gherkin as a
   requirements capture format, independent of test automation
2. **EARS integration** — structured requirements (EARS) mapped to behavioral
   specifications (Gherkin), a combination no existing skill offers
3. **Interactive discovery workflow** — not a reference dump, but a guided
   process that asks questions, discovers requirements, and generates scenarios
4. **Quality gates** — scoring rubric, review loop, validation
5. **Framework-agnostic** — specifications that work regardless of which
   BDD test runner (if any) will eventually execute them
