# Deep Dive: doc-bdd Skill from aidoc-flow-framework

**Repository**:
[vladm3105/aidoc-flow-framework](https://github.com/vladm3105/aidoc-flow-framework)
**Date**: 2026-04-15
**Scope**: Complete analysis of the doc-bdd skill and its
surrounding framework

---

## Framework Overview

### Philosophy: AI-First Specification-Driven Development (SDD)

The aidoc-flow-framework implements an **AI-First
Specification-Driven Development** methodology where AI agents
(Claude Code, Gemini CLI, GitHub Copilot) are the primary
operators. Humans work *through* AI assistants. The framework's
core principle is **"formalize before implementing"** -- every
line of code must trace back to business requirements through a
chain of progressively more detailed specification artifacts.

### The 15-Layer Architecture

The framework defines a 15-layer pipeline from business
requirements to production code. Each layer produces a specific
artifact type with formal templates, validation schemas, quality
scores, and cumulative traceability tags.

| Layer | Artifact | Purpose | C4 Level |
| ----- | -------- | ------- | -------- |
| 0 | Strategy | Business owner documents | External |
| 1 | **BRD** | Business Requirements Document | Context (L1) |
| 2 | **PRD** | Product Requirements Document | Container (L2) |
| 3 | **EARS** | Formal requirements (WHEN-THE-SHALL-WITHIN) | Transition |
| 4 | **BDD** | Gherkin test scenarios | Transition |
| 5 | **ADR** | Architecture Decision Records | Bridge |
| 6 | **SYS** | System Requirements | Component (L3) |
| 7 | **REQ** | Atomic Requirements | Decomposition |
| 8 | CTR | API Contracts (optional) | Decomposition |
| 9 | SPEC | Technical Specifications | Code (L4) |
| 10 | TSPEC | Test Specifications | Validation |
| 11 | TASKS | Task Breakdown | Execution |
| 12-14 | Code/Tests/Validation | Implementation | -- |

### SDD Depth Variants

The framework supports three depth levels:

- **SDD-Lite**: REF -> BRD -> PRD -> TASKS (MVPs, prototypes, 1-3 months)
- **SDD-Standard**: + EARS, ADR, SYS, REQ (production apps, 3-6 months)
- **SDD-Full**: All 15 layers + 4-Gate CHG (enterprise/regulated, 6+ months)

### Core Lifecycle

Each iteration follows: **MVP (1-2 weeks) -> PROD (30-90 days) -> NEW MVP**.
Each BRD represents one iteration cycle. New features get new
BRDs (BRD-01, BRD-02, BRD-03). Cross-cycle traceability is
maintained via `@depends: BRD-01` tags.

### Cumulative Tagging -- The Traceability Backbone

The most distinctive architectural pattern is **cumulative
tagging**: each layer must include traceability tags from ALL
upstream layers. This creates a complete audit trail:

```text
BRD (0 tags) -> PRD (@brd) -> EARS (@brd,@prd) -> BDD (+@ears) -> ADR (+@bdd) ->
SYS (+@adr) -> REQ (+@sys) -> CTR (+@req) -> SPEC (+@ctr) -> TSPEC (+@spec) -> TASKS (+@tspec)
```

By the time you reach Layer 11 (TASKS), each artifact carries
8-10 traceability tags linking it back through every upstream
decision.

### Skill Ecosystem Per Layer

Each layer has up to **6 specialized skills**:

| Skill Suffix | Role |
| ------------ | ---- |
| `doc-{type}` | Core creation skill (rules, structure, syntax) |
| `doc-{type}-autopilot` | Automated generation pipeline |
| `doc-{type}-validator` | Structural/schema validation |
| `doc-{type}-reviewer` | Content quality and semantic review |
| `doc-{type}-fixer` | Automated issue remediation |
| `doc-{type}-audit` | Unified wrapper (validator + reviewer -> combined report) |

This means the BDD layer alone has **6 skills**: doc-bdd, doc-bdd-autopilot,
doc-bdd-validator, doc-bdd-reviewer, doc-bdd-fixer, and doc-bdd-audit.

---

## Layer 3: EARS Skill (doc-ears) -- Upstream to BDD

### Purpose

EARS (Easy Approach to Requirements Syntax) is Layer 3 -- it formalizes product
requirements from BRD/PRD into precise behavioral statements using the
**WHEN-THE-SHALL-WITHIN** syntax pattern.

### EARS Syntax Patterns (4 Categories)

1. **Event-Driven** (IDs 001-099):
   `WHEN [trigger] THE [system] SHALL [response] WITHIN [constraint]`

2. **State-Driven** (IDs 101-199):
   `WHILE [state] THE [system] SHALL [behavior] WITHIN [constraint]`

3. **Unwanted Behavior** (IDs 201-299):
   `IF [error/problem] THE [system] SHALL [prevention] WITHIN [constraint]`

4. **Ubiquitous** (IDs 401-499):
   `THE [system] SHALL [system-wide requirement] WITHIN [boundary]`

### BDD-Ready Scoring System

EARS has a **BDD-Ready Score** that measures readiness for BDD generation:

| Dimension | Weight |
| --------- | ------ |
| Requirements Clarity (EARS syntax, atomicity, quantifiable constraints) | 40% |
| Testability (BDD translation possible, observable verification, edge cases) | 35% |
| Quality Attribute Completeness (performance targets, security, reliability) | 15% |
| Strategic Alignment (business objectives, implementation paths) | 10% |

**Quality Gate**: Score < 90% blocks BDD artifact creation.

### Key Rules

- Element ID format: `EARS.{DOC_NUM}.{HASH}` (3 segments, dot-separated)
- Source Document: single `@prd: PRD.NN.EE.SS` value (no ranges, no multiples)
- Cumulative tags required: @brd, @prd (2 tags from Layers 1-2)
- All quantitative values must use `@threshold:` tags
  referencing PRD threshold registry
- File size limit: 1200 lines max, target 800
- Mandatory nested folder structure:
  `docs/03_EARS/EARS-NN_{slug}/`
- Formal language keywords: SHALL (mandatory), SHALL NOT
  (prohibited), SHOULD (recommended), MAY (optional)
- Ambiguous terms forbidden: "fast", "efficient", "user-friendly"

### Downstream Handoff to BDD

EARS produces formal requirements that BDD consumes as follows:

| EARS Category | BDD Mapping |
| ------------- | ----------- |
| Event-Driven (WHEN...SHALL) | Success path scenarios (@primary) |
| State-Driven (WHILE...SHALL) | State validation scenarios |
| Unwanted Behavior (IF...SHALL) | Error handling scenarios (@negative) |
| Ubiquitous (THE...SHALL) | Quality attribute scenarios (@quality_attribute) |
| Quality Attributes section | Performance/security/reliability tests |
| Threshold references | `@threshold:` tags in BDD steps |

---

## Layer 4: doc-bdd Skill -- Complete Detailed Analysis

### Purpose (doc-bdd)

Create **BDD (Behavior-Driven Development)** test scenarios --
Layer 4 artifact that defines executable test scenarios using
Gherkin syntax. BDD translates EARS formal requirements into
executable Given-When-Then scenarios.

**Upstream**: BRD (Layer 1), PRD (Layer 2), EARS (Layer 3)
**Downstream**: ADR (Layer 5), SYS (Layer 6), REQ (Layer 7)

### C4 Model Position

BDD is NOT a C4 level itself. It is a **refinement step**
that formalizes the transition from Context (BRD) to Container
(PRD), alongside EARS. BDD operates at the scenario/test level,
using sequence diagrams (not C4 diagrams) for visualization.

### Execution Environment

**Critical note**: BDD tests run in **QA STAGING ONLY** -- not
in CI pipeline. CI uses UTEST/ITEST. BDD validates user
acceptance criteria after staging deployment.

### Full Workflow (13 Steps)

1. **Read Upstream Artifacts** -- Read BRD, PRD, and EARS
   to understand requirements
2. **Reserve Suite ID** -- Check `docs/04_BDD/` for next
   available ID (BDD-01, BDD-02)
3. **Create Suite Folder** --
   `mkdir -p docs/04_BDD/BDD-02_knowledge_engine/`
4. **Create Index File** -- Copy from
   `BDD-SECTION-0-TEMPLATE.md`
5. **Design Section Split** -- Identify logical domains,
   estimate scenarios per section (target 6-10)
6. **Create Section Files** -- Copy from
   `BDD-MVP-TEMPLATE.feature`
7. **Add Section Metadata Tags** -- `@section`,
   `@parent_doc`, `@index`, upstream tags
8. **Write Scenarios** -- For each EARS requirement:
   success path + 2-3 error conditions + 1-2 edge cases +
   parameterized tests
9. **Replace Magic Numbers with Thresholds** -- Use
   `@threshold:PRD.NN.category.key` format
10. **Create Redirect Stub** -- At `docs/04_BDD/` root
    with `@redirect` tag and 0 scenarios
11. **Update Index File** -- List all section files with
    scenario counts and traceability matrix
12. **Validate BDD Suite** -- Run validation scripts
13. **Commit Changes** -- Commit suite folder and redirect
    stub together

### Prerequisites (CRITICAL)

Before creating BDD, the skill mandates reading:

1. **Shared Standards**: `.claude/skills/doc-flow/SHARED_CONTENT.md`
2. **Upstream BRD, PRD, EARS**: The artifacts that drive the test scenarios
3. **Template**: `ai_dev_ssd_flow/04_BDD/BDD-MVP-TEMPLATE.feature`
4. **Validation Rules**: `ai_dev_ssd_flow/04_BDD/BDD_MVP_SCHEMA.yaml`

Upstream artifact verification is marked CRITICAL:

- List existing upstream artifacts with
  `ls docs/01_BRD/ docs/02_PRD/ docs/03_EARS/ docs/04_BDD/`
- Reference only existing documents in traceability tags
- Use `null` only when upstream artifact type genuinely does not exist
- NEVER use placeholders like `BRD-XXX` or `TBD`
- Do NOT create missing upstream artifacts -- skip functionality instead

### Section-Based Structure (MANDATORY)

All BDD suites MUST use section-based structure with nested folders. No backward
compatibility with legacy formats is maintained.

#### Directory Structure

```text
docs/04_BDD/
+-- BDD-02_knowledge_engine/           # Suite folder (REQUIRED)
|   +-- BDD-02.md                      # Index file (MANDATORY)
|   +-- BDD-02.1_ingest.feature        # Section 1
|   +-- BDD-02.2_query.feature         # Section 2
|   +-- BDD-02.3.00_learning.feature   # Aggregator (if 5+ subsections)
|   +-- BDD-02.3.01_learning_path.feature    # Subsection 1
|   +-- BDD-02.3.02_bias_detection.feature   # Subsection 2
|   +-- BDD-02_README.md               # Optional companion
|   +-- BDD-02_TRACEABILITY.md         # Optional companion
+-- BDD-02_knowledge_engine.feature    # Redirect stub (0 scenarios)
```

#### Three Valid File Patterns (ONLY)

| Pattern | Example | Use When |
| ------- | ------- | -------- |
| Section-Only | `BDD-02.14_query_result_filtering.feature` | Standard section (<=800 lines, <=12 scenarios) |
| Subsection | `BDD-02.24.01_quality_performance.feature` | Section requires splitting |
| Aggregator | `BDD-02.12.00_query_graph_traversal.feature` | Organizing 5+ subsections (@redirect, 0 scenarios) |

#### Prohibited Patterns (ERROR)

- `_partN` suffix
  (e.g., `BDD-02_query_part1.feature`)
- Single-file with scenarios
  (e.g., `BDD-02_knowledge_engine.feature` with scenarios)
- `features/` subdirectory inside suite folder

#### Size Limits

- **Max 800 lines** per `.feature` file (soft limit: 600)
- **Max 12 scenarios** per Feature block
- When limits are exceeded, split into subsections

### Gherkin Syntax Requirements

#### Feature File Structure

```gherkin
# Traceability Tags (Gherkin-native, NOT in comments)
@section: 2.14
@parent_doc: BDD-02
@index: BDD-02.md
@brd:BRD.02.0103
@prd:PRD.02.0702
@ears:EARS.02.1401

Feature: BDD-02.14: Query Result Filtering
  As a data analyst
  I want filtered query results
  So that I can focus on relevant data

  Background:
    Given the system timezone is "America/New_York"
    And the current time is "09:30:00" in "America/New_York"

  @primary @functional
  Scenario: Successful filter application
    Given valid filter criteria
    When user applies filter
    Then filtered results are returned
    And response time is less than @threshold:PRD.02.perf.api.p95_latency
```

#### Tags Placement (CRITICAL - E041)

Tags MUST be **Gherkin-native** (placed before the Feature
keyword as Gherkin tags), NOT embedded in comments. Comment-based
tags cannot be parsed by test frameworks.

```gherkin
# INVALID:
# @brd: BRD.01.0101
Feature: My Feature

# VALID:
@brd:BRD.01.0101
@prd:PRD.01.0101
@ears:EARS.01.2401
Feature: My Feature
```

#### Times and Timezones (MANDATORY)

- All times include seconds: `HH:MM:SS`
- Use IANA timezone format: `America/New_York`, `America/Los_Angeles`
- Avoid ambiguous abbreviations (EST/EDT/PST/PDT)

### Unified Element ID Format (MANDATORY)

**Pattern**: `BDD.{DOC_NUM}.{HASH}` (3 segments, dot-separated)

| Element Type | Code | Example |
| ------------ | ---- | ------- |
| Test Scenario | 14 | BDD.02.1401 |
| Step | 15 | BDD.02.1501 |

Removed/forbidden patterns: `SCENARIO-XXX`, `TS-XXX`, `STEP-XXX`, `TC-XXX`

The newer YAML template uses a **hash-based** ID system:

- Format: `BDD.{doc_id}.{section_id}.{hash}`
- Hash: SHA256 of
  `"{doc_id}:{section_id}:{title}:{description}"`,
  truncated to 4 hex chars
- Collision handling: extend hash from 4 to 8 chars if
  duplicate detected
- Example: `BDD.01.03.d7a2`

### ADR-Ready Scoring System

The ADR-Ready Score measures BDD maturity and readiness for ADR progression.

#### Scoring Criteria (4 Dimensions)

| Dimension | Weight | Sub-criteria |
| --------- | ------ | ------------ |
| **Scenario Completeness** | **35%** | All EARS translated to BDD (15%), Comprehensive coverage success/error/edge (15%), Observable verification methods (5%) |
| **Testability** | **30%** | Scenarios are automatable (15%), Data-driven Examples tables used (10%), Performance benchmarks quantifiable (5%) |
| **Architecture Requirements Clarity** | **25%** | Quality attributes specified (15%), Integration points defined (10%) |
| **Business Validation** | **10%** | Business acceptance criteria traceable (5%), Measurable success outcomes (5%) |

The newer YAML template version uses a slightly different weighting:

| Dimension | Weight |
| --------- | ------ |
| Scenario coverage (all EARS requirements have scenarios) | 40% |
| Gherkin quality (valid syntax, atomic scenarios, executable) | 25% |
| Traceability (cumulative tags complete) | 20% |
| Edge case coverage (error, recovery, parameterized) | 15% |

#### Score-to-Status Mapping

| ADR-Ready Score | Required Status |
| --------------- | --------------- |
| >= 90% | Approved |
| 70-89% | In Review |
| < 70% | Draft |

**Quality Gate**: Score < 90% **blocks** ADR artifact creation.
This is a hard gate.

#### Display Format

```markdown
| **ADR-Ready Score** | [checkmark] 95% (Target: >=90%) |
```

### Threshold Registry Integration (MANDATORY)

All quantitative values MUST use `@threshold:` keys. No hardcoded magic numbers.

#### Inline Step Format

```gherkin
# INVALID (hardcoded):
Then response time is less than 200ms

# VALID (threshold reference):
Then response time is less than @threshold:PRD.035.perf.api.p95_latency
```

#### Common Threshold Categories

| Category | BDD Usage | Example Key |
| -------- | --------- | ----------- |
| `perf.*` | Performance validation | `perf.api.p95_latency` |
| `sla.*` | SLA validation | `sla.uptime.target` |
| `limit.*` | Rate limit testing | `limit.api.requests_per_second` |
| `timeout.*` | Timeout validation | `timeout.request.sync` |

### Cumulative Tagging Requirements

Layer 4 (BDD) must include tags from Layers 1-3:
**@brd, @prd, @ears** (3+ tags).

Format (Gherkin-native tags before Feature):

```gherkin
@brd:BRD.01.0103
@prd:PRD.01.0702
@ears:EARS.01.2401
Feature: Feature Name
```

### All 8 Scenario Categories

| # | Category | Tag | Description | Source |
| - | -------- | --- | ----------- | ------ |
| 1 | Success Path | `@primary` | Happy path scenarios | EARS Event-Driven |
| 2 | Alternative Path | `@alternative` | Optional parameters, different workflows | EARS variations |
| 3 | Error Conditions | `@negative` | Invalid inputs, error handling | EARS Unwanted Behavior |
| 4 | Edge Cases | `@edge_case`, `@boundary` | Boundary conditions, limits | EARS constraints |
| 5 | Data-Driven | `@data_driven` | Parameterized with Examples tables | EARS parameterized values |
| 6 | Integration | `@integration` | External system interactions | EARS external dependencies |
| 7 | Quality Attributes | `@quality_attribute` | Performance, security, reliability | EARS Quality Attributes |
| 8 | Failure Recovery | `@failure_recovery` | Error recovery, circuit breakers | EARS recovery statements |

All 8 categories should be represented in every BDD suite.

### Enhanced Scenario Tagging (v2.0 from Autopilot)

The autopilot adds additional mandatory tags beyond the core 8 categories:

#### Scenario Type Classification (5 categories)

| Tag | Purpose | Priority Default |
| --- | ------- | ---------------- |
| `@scenario-type:success` | Primary happy path | @p0-critical |
| `@scenario-type:optional` | Alternative workflows | @p2-medium |
| `@scenario-type:recovery` | Failure recovery | @p1-high |
| `@scenario-type:parameterized` | Data-driven | @p2-medium |
| `@scenario-type:error` | Negative cases | @p1-high |

#### Priority Classification

| Tag | Definition | Impact |
| --- | ---------- | ------ |
| `@p0-critical` | MVP blocking -- must pass for release | Blocks deployment |
| `@p1-high` | Sprint required -- must pass within sprint | Sprint scope |
| `@p2-medium` | Next iteration -- important but deferrable | Next planning cycle |
| `@p3-low` | Backlog -- nice to have | Future consideration |

#### SHALL+WITHIN Language Pattern

For timed operations, the framework uses formal EARS-derived language:

```gherkin
@scenario-type:success @p0-critical
Scenario: Authentication completes within performance threshold
  Given user has valid credentials
  When user submits authentication request
  Then the system SHALL authenticate the user
  And the response SHALL be returned WITHIN @threshold:PRD.01.perf.auth.p95_latency
```

### Section Metadata Requirements

All `.feature` files MUST include section metadata tags:

```gherkin
@section: NN.SS              # Section number
@parent_doc: BDD-NN          # Parent BDD suite
@index: BDD-NN.0_index.md    # Index file reference
@brd:BRD.NN.EE.SS            # Upstream BRD element
@prd:PRD.NN.EE.SS            # Upstream PRD element
@ears:EARS.NN.SS.RR          # Upstream EARS requirement
```

For subsections, add: `@parent_section: NN.SS`

Feature title format: `Feature: BDD-NN.SS: Domain Description`

### Aggregator Files

Used when a section has 5+ subsections:

- `@redirect` tag MUST be present
- 0 scenarios (redirect stub only)
- Lists subsections in Feature description

### Index File Template

Mandatory `BDD-NN.0_index.md` for each suite containing:

- Suite Overview (purpose, scope)
- Section File Map (section, file, scenarios, lines, status, description)
- Traceability Matrix (BDD section -> upstream source -> description)

### Validation Error Codes

| Code | Description | Severity |
| ---- | ----------- | -------- |
| E001 | Document Control fields missing | ERROR |
| E002 | Gherkin syntax invalid | ERROR |
| E003 | ADR-Ready Score format invalid | ERROR |
| E004 | Upstream traceability tags missing | ERROR |
| E041 | Tags in comments (not Gherkin-native) | ERROR |
| E008 | Element ID format invalid | ERROR |
| CHECK 9.1 | File naming pattern invalid | ERROR |
| CHECK 9.2 | Prohibited pattern detected | ERROR |
| CHECK 9.3 | Aggregator requirements not met | ERROR |
| CHECK 9.4 | File size exceeds limits | ERROR |
| CHECK 9.5 | Section metadata tags missing | ERROR |
| CHECK 9.6 | Index file missing | ERROR |
| CHECK 9.7 | Non-Gherkin content in .feature file | ERROR |

### Post-Creation Validation (MANDATORY)

A validation loop must execute IMMEDIATELY after document creation:

```text
LOOP:
  1. Run validation script
  2. IF errors fixed: GOTO LOOP (re-validate)
  3. IF warnings fixed: GOTO LOOP (re-validate)
  4. IF unfixable issues: Log for manual review
  5. IF clean: Mark VALIDATED, proceed
```

**Quality Gate**: Blocking -- cannot proceed to ADR creation
until validation passes with 0 errors.

### Reserved ID Exemption

Documents with ID `BDD-00_*` (index, traceability matrix,
glossaries) are fully exempt from validation.

### Tag Format Convention

| Notation | Format | Artifacts | Purpose |
| -------- | ------ | --------- | ------- |
| Dash | TYPE-NN | ADR, SPEC, CTR | Technical artifacts -- document references |
| Dot | TYPE.NN.xxxx | BRD, PRD, EARS, BDD, SYS, REQ | Hierarchical artifacts -- element references |

---

## The doc-bdd Satellite Skills

### doc-bdd-autopilot (v2.3) -- Automated Generation Pipeline

The most complex of the satellite skills. It orchestrates a
5-phase pipeline:

**Phase 1: EARS Analysis** -- Read EARS documents, extract
statements, categorize by type, identify quality attributes,
extract threshold references.

**Phase 2: BDD Readiness Check** -- Validate EARS BDD-Ready
score >= 90%. Auto-fix EARS issues if below threshold. Uses
`doc-ears-validator` for delegation.

**Phase 3: BDD Generation** -- Plan section structure, generate
feature files, create all 8 scenario categories (success, error,
edge, data-driven, quality attribute, integration, failure
recovery, alternative), add cumulative tags, write files. Uses
`quality-advisor` for real-time feedback during generation.

**Phase 4: BDD Validation** -- Run `doc-bdd-validator`, check
ADR-Ready score >= 90%, auto-fix issues in a loop (max 3
iterations).

**Phase 5: Review & Fix Cycle** -- Run `doc-bdd-reviewer`, if
score < 90% invoke `doc-bdd-fixer`, re-review, iterate up to 3
times.

Key features:

- **Smart Document Detection**: Auto-determines action based
  on input type (BDD-NN triggers review, EARS-NN triggers
  generate-or-review)
- **Chunked Parallel Execution**: Maximum 3 documents per
  chunk to prevent context overflow
- **Input Contract (IPLAN-004)**: Supports `--ref`, `--prompt`,
  `--iplan` modes with precedence ordering
- **Context Management**: Pause between chunks for user acknowledgment

### doc-bdd-reviewer (v1.5) -- Content Quality Gate

Performs 9 review checks:

| # | Check | Weight | Description |
| - | ----- | ------ | ----------- |
| 0 | Structure Compliance | 12/12 | BLOCKING -- nested folder validation |
| 1 | Gherkin Syntax Compliance | 19% | Feature structure, Given-When-Then order |
| 2 | Scenario Completeness | 23% | Happy path, error, edge cases covered |
| 3 | EARS Alignment | 19% | Every scenario maps to EARS requirement |
| 4 | Step Definition Reusability | 10% | Duplicate/similar step detection |
| 5 | Data Table Validation | 9% | Examples tables complete and valid |
| 6 | Placeholder Detection | 5% | No [TODO] or [TBD] remaining |
| 7 | Naming Compliance | 10% | Element IDs follow standards |
| 8 | Upstream Drift Detection | 5% | Detects stale BDD content |

**Upstream Drift Detection** is particularly notable -- it maintains a mandatory
`.drift_cache.json` with SHA-256 content hashes and modification timestamps. It
uses a three-phase algorithm (Load Cache -> Detect Drift -> Update Cache) and
flags content changes > 20% as critical errors.

### doc-bdd-validator (v1.2) -- Structural Validation

Validates 12 checks including:

- Folder structure (BLOCKING)
- Metadata validation (tags, custom_fields)
- Structure validation (9 required sections)
- Content validation (Gherkin syntax)
- Traceability validation (cumulative tags)
- ADR-Ready Score calculation

### doc-bdd-fixer (v2.2) -- Automated Remediation

7-phase fix pipeline:

1. Phase 0: Fix structure violations
2. Phase 1: Create missing files
3. Phase 2: Fix broken links
4. Phase 3: Fix element IDs
5. Phase 4: Fix content issues
6. Phase 5: Update references
7. Phase 6: Handle upstream drift

Accepts both audit reports (`BDD-NN.A_audit_report_vNNN.md` preferred) and
legacy review reports (`BDD-NN.R_review_report_vNNN.md`).

### doc-bdd-audit (v1.0) -- Unified Wrapper

Orchestrates validator then reviewer, merges findings into a combined report
with normalized fix queue for the fixer. The combined report includes:

- Summary (validator status + reviewer score)
- Score Calculation (deduction-based: `100 - total_deductions`)
- Validator Findings + Reviewer Findings + Coverage Findings
- Fix Queue (auto_fixable, manual_required, blocked)
- Recommended Next Step

---

## Layer 5: ADR Skill (doc-adr) -- Downstream from BDD

### Purpose (doc-adr)

Create Architecture Decision Records -- Layer 5 artifact
documenting architectural decisions with
Context-Decision-Consequences format and rationale.

### How ADR Consumes BDD Output

ADR references BDD as one of 4 upstream sources:

- @brd (Layer 1), @prd (Layer 2), @ears (Layer 3),
  @bdd (Layer 4)

The ADR specifically:

- Documents architectural decisions for topics identified
  in BRD/PRD
- References BDD scenarios that validate the architecture
  (in Section 8: Verification)
- Defines success criteria based on BDD test coverage
- Lists BDD scenario IDs that prove the decision works

### ADR Structure (11 Sections)

1. Document Control (with SYS-Ready Score)
2. Context (Problem Statement, Technical Context)
3. Decision (Chosen Solution, Key Components)
4. Alternatives Considered (Options with pros/cons)
5. Consequences (Positive/Negative Outcomes, Costs)
6. Architecture Flow (Mermaid diagrams, Integration Points)
7. Implementation Assessment (Phases, Rollback, Monitoring)
8. Verification (Success Criteria, **BDD Scenarios**)
9. Traceability (Upstream/Downstream, Tags, Cross-Links)
10. Related Decisions (Dependencies, Supersessions)
11. MVP Lifecycle (Iteration guidance)

### SYS-Ready Scoring System

| Dimension | Weight |
| --------- | ------ |
| Decision Completeness (Context/Decision/Consequences/Alt.) | 30% |
| Architecture Clarity (Mermaid diagrams REQUIRED, components) | 35% |
| Implementation Readiness (Complexity, deps, rollback) | 20% |
| Verification Approach (Testing strategy, success metrics) | 15% |

Quality Gate: Score < 90% blocks SYS artifact creation.

### ADR Lifecycle States

Proposed -> Accepted -> Deprecated/Superseded by ADR-XXX

### Threshold Dual Role

ADR documents both **reference** platform-wide thresholds from
PRD and **define** architecture-specific thresholds unique to
the decision (e.g., circuit breaker failure thresholds, retry
max attempts, cache TTL).

### Cross-Linking Tags

ADR introduces AI-friendly cross-linking:

- `@depends: ADR-NN` -- Hard prerequisite
- `@discoverability: ADR-NN (short rationale)` -- Related
  document for AI search

These are info-level (non-blocking) but enable AI/LLM tools
to infer relationships.

---

## Cross-Cutting Patterns

### 1. Naming Conventions

**Document IDs**: `TYPE-NN` (2 digits minimum, expand as needed)

- Valid: BDD-01, BDD-99, BDD-102
- Invalid: BDD-001 (unnecessary leading zero)

**Element IDs**: `TYPE.{DOC_NUM}.{HASH}` (3+ segments,
dot-separated)

- New hash-based: `BDD.01.03.d7a2` (SHA256-derived,
  4-hex-char hash)
- Legacy integer: `BDD.02.1401` (type code + sequential
  number)

**File Names**: `TYPE-NN.SS_{slug}.feature` for sections,
`TYPE-NN_{slug}/` for folders

**Tag Notation**:

- Dot format (`TYPE.NN.xxxx`) for hierarchical artifacts
  (BRD, PRD, EARS, BDD, SYS, REQ)
- Dash format (`TYPE-NN`) for technical artifacts
  (ADR, SPEC, CTR)

### 2. Quality Scoring Approach

Every layer has a **downstream-ready score** measuring
readiness for the next layer:

| Layer | Score Name | Target | Blocks |
| ----- | --------- | ------ | ------ |
| EARS (Layer 3) | BDD-Ready Score | >= 90% | BDD creation |
| BDD (Layer 4) | ADR-Ready Score | >= 90% | ADR creation |
| ADR (Layer 5) | SYS-Ready Score | >= 90% | SYS creation |

Common scoring pattern:

- 4 weighted dimensions totaling 100%
- Largest weight goes to the core purpose (clarity,
  completeness, or architecture)
- Status automatically maps: >= 90% = Approved/Accepted,
  70-89% = In Review/Proposed, < 70% = Draft
- Deduction-based calculation in review reports: `100 - total_deductions`
- Visual indicators: checkmark >= 90%, yellow circle 85-89%, X < 85%

### 3. Traceability Enforcement

- **Upstream Required**: Every artifact except BRD must
  reference its upstream sources
- **Downstream Optional**: Only add links to existing
  documents
- **No-TBD Rule**: NEVER use placeholder IDs (TBD, XXX, NNN)
- **Existing Only**: Both upstream and downstream links must
  reference existing documents
- **Cumulative Tags**: Each layer carries ALL upstream tags
  (not just immediate parent)

### 4. Version Control and Report Artifacts

Reports use versioned naming: `TYPE-NN.{SUFFIX}_report_vNNN.md`

- `.A_` = Audit report (preferred)
- `.R_` = Review report (legacy-compatible)
- `.F_` = Fix report

Version detection scans folder for existing reports and auto-increments.
Same-day reviews each get unique version numbers.
Delta reporting compares scores between review versions.

### 5. Threshold Registry Pattern

All quantitative values are externalized to a PRD-managed threshold registry:

- Format: `@threshold:PRD.NN.category.subcategory.key`
- Categories: `perf.*`, `sla.*`, `limit.*`, `timeout.*`,
  `retry.*`, `circuit.*`, `cache.*`
- No hardcoded "magic numbers" allowed in any artifact
- ADR layer can define architecture-specific thresholds
  with `@threshold:ADR.NN.*`

### 6. Mandatory Validation Loops

Every creation skill includes a mandatory post-creation validation loop:

```text
LOOP:
  1. Run validation
  2. IF errors: fix and re-validate
  3. IF warnings: fix and re-validate
  4. IF unfixable: log for manual review
  5. IF clean: mark VALIDATED, proceed
```

This is blocking -- you cannot proceed to the next layer
until validation passes with 0 errors.

### 7. Document Size Policy

All SDD documents are **monolithic** (single self-contained
file) up to **50,000 tokens**. If a document exceeds 50,000
tokens, create a new document of the same type with its own
scope. For BDD specifically, the per-file limit is 800 lines
with a soft limit of 600.

---

## What We Can Learn -- Specific Techniques Worth Adopting

### 1. Downstream-Ready Scoring

The concept of a **scored quality gate** between layers is
powerful. Each BDD document has a numeric score (0-100)
computed from weighted dimensions. This score directly
controls workflow progression -- a document below 90%
physically cannot proceed to the next phase. This is more
rigorous than a simple pass/fail checklist.

**Adoption idea**: Our Gherkin skill could include a quality
score for generated scenarios based on coverage completeness,
Gherkin syntax compliance, and traceability to source
requirements.

### 2. Scenario Category Taxonomy

The 8 mandatory scenario categories ensure comprehensive
coverage:

1. Success Path, 2. Alternative Path, 3. Error Conditions,
   4\. Edge Cases, 5. Data-Driven, 6. Integration,
   7\. Quality Attributes, 8. Failure Recovery

The v2.0 autopilot simplifies this to 5 `@scenario-type`
categories with priority tags (@p0-@p3). This dual taxonomy
(8 coverage categories + 5 type tags + 4 priority levels) is
extremely systematic.

**Adoption idea**: Define a minimum scenario category
checklist that our skill enforces, ensuring users do not
produce Gherkin with only happy-path scenarios.

### 3. Threshold Externalization

The `@threshold:PRD.NN.category.key` pattern eliminates
magic numbers from test scenarios. Instead of
`Then response time is less than 200ms`, you write
`Then response time is less than @threshold:PRD.01.perf.api.p95_latency`.

**Adoption idea**: While we may not need a full registry,
encouraging users to define named constants for quantitative
values in scenarios would improve maintainability.

### 4. Cumulative Tagging for Traceability

Each layer carries ALL upstream traceability tags. By the
time you reach BDD (Layer 4), every feature file carries
@brd, @prd, and @ears tags. This creates an auditable chain
from business requirements to test scenarios.

**Adoption idea**: Our skill should encourage (or require)
upstream references in generated Gherkin, even if simplified
to a single `@requirement:` tag linking back to the source.

### 5. Satellite Skill Pattern (Create/Validate/Review/Fix/Audit)

The decomposition of a single skill into 6 specialized
sub-skills is architecturally elegant:

- **Creator** defines rules and structure
- **Autopilot** automates creation pipeline
- **Validator** checks structural compliance
- **Reviewer** checks content quality and semantic
  correctness
- **Fixer** applies automated remediation
- **Audit** wraps validator + reviewer into unified workflow

**Adoption idea**: Even if we do not build 6 separate
skills, separating validation concerns (structural vs.
content quality) and having an automated fix capability
would strengthen our skill.

### 6. Upstream Drift Detection

The reviewer's drift detection (Check #8) maintains a
SHA-256 hash cache of upstream documents. When the EARS
requirements change after BDD scenarios were written, the
reviewer flags the drift. This prevents stale test scenarios.

**Adoption idea**: For scenarios generated from requirements
documents, include metadata about the source document version
so staleness can be detected.

### 7. Section-Based File Organization

The mandatory nested folder structure with index files,
section files, aggregators, and redirect stubs provides a
highly organized approach to managing large test suites. The
800-line file limit and 12-scenario-per-Feature limit force
modular decomposition.

**Adoption idea**: Define clear guidance on when and how to
split large feature files.

### 8. SHALL+WITHIN Language Pattern

For timed operations, the framework uses formal language:
`Then the system SHALL authenticate the user`
`And the response SHALL be returned WITHIN`
`@threshold:PRD.01.perf.auth.p95_latency`

This bridges EARS formal requirements language directly into
Gherkin, making the translation more systematic and the
connection between requirements and tests explicit.

### 9. Aggregator Pattern for Large Suites

When a section exceeds 5 subsections, an aggregator file acts
as a table of contents with 0 scenarios and `@redirect` tag.
This provides navigability in large test suites without
sacrificing the flat file structure that test runners expect.

### 10. Execution Environment Boundaries

The clear statement that "BDD tests run in QA STAGING ONLY --
not in CI pipeline" is an important architectural boundary.
The framework distinguishes between unit/integration tests
(CI) and acceptance tests (staging), each with appropriate
tooling.

---

## Full SKILL.md Content -- doc-bdd (Verbatim)

````markdown
---
name: doc-bdd
description: Layer 4 artifact for Behavior-Driven Development test scenarios using Gherkin Given-When-Then format
metadata:
  tags:
    - sdd-workflow
    - layer-4-artifact
    - shared-architecture
  custom_fields:
    layer: 4
    artifact_type: BDD
    architecture_approaches: [ai-agent-based, traditional-8layer]
    priority: shared
    development_status: active
    skill_category: core-workflow
    upstream_artifacts: [BRD, PRD, EARS]
    downstream_artifacts: [ADR, SYS, REQ]
    version: "1.1"
    last_updated: "2026-02-27"
  versioning_policy: "tracks BDD-MVP-TEMPLATE schema_version"
---

# doc-bdd

## Purpose

Create **BDD (Behavior-Driven Development)** test scenarios - Layer 4 artifact in the SDD workflow that defines executable test scenarios using Gherkin syntax.

**Layer**: 4

**Upstream**: BRD (Layer 1), PRD (Layer 2), EARS (Layer 3)

**Downstream**: ADR (Layer 5), SYS (Layer 6), REQ (Layer 7)

## Prerequisites

### Upstream Artifact Verification (CRITICAL)

**Before creating this document, you MUST:**

1. **List existing upstream artifacts**:
   ```bash
   ls docs/01_BRD/ docs/02_PRD/ docs/03_EARS/ docs/04_BDD/ 2>/dev/null
   ```

1. **Reference only existing documents** in traceability tags
2. **Use `null`** only when upstream artifact type genuinely doesn't exist
3. **NEVER use placeholders** like `BRD-XXX` or `TBD`
4. **Do NOT create missing upstream artifacts** - skip functionality instead

Before creating BDD, read:

1. **Shared Standards**: `.claude/skills/doc-flow/SHARED_CONTENT.md`
2. **Upstream BRD, PRD, EARS**: Read artifacts that drive these test scenarios
3. **Template**: `ai_dev_ssd_flow/04_BDD/BDD-MVP-TEMPLATE.feature`
4. **Creation Rules**: `ai_dev_ssd_flow/04_BDD/BDD-MVP-TEMPLATE.feature`
5. **Validation Rules**: `ai_dev_ssd_flow/04_BDD/BDD_MVP_SCHEMA.yaml`

## When to Use This Skill

Use `doc-bdd` when:

- Have completed BRD (Layer 1), PRD (Layer 2), EARS (Layer 3)
- Need to define executable test scenarios
- Validating EARS formal requirements with Given-When-Then format
- Creating acceptance criteria for features
- You are at Layer 4 of the SDD workflow

## Section-Based Structure (MANDATORY)

**All BDD suites MUST use section-based structure.** No backward compatibility with legacy formats.

### Directory Structure

**Nested Folder Rule (MANDATORY)**: ALL BDD suites MUST use nested folders regardless of size.

```
docs/04_BDD/
├── BDD-02_knowledge_engine/           # Suite folder (REQUIRED)
│   ├── BDD-02.md              # Index file (MANDATORY)
│   ├── BDD-02.1_ingest.feature        # Section 1
│   ├── BDD-02.2_query.feature         # Section 2
│   ├── BDD-02.3.00_learning.feature   # Aggregator (if 5+ subsections)
│   ├── BDD-02.3.01_learning_path.feature    # Subsection 1
│   ├── BDD-02.3.02_bias_detection.feature   # Subsection 2
│   ├── BDD-02_README.md               # Optional companion
│   └── BDD-02_TRACEABILITY.md         # Optional companion
└── BDD-02_knowledge_engine.feature    # Redirect stub (0 scenarios)
```

**CRITICAL**: Never create BDD files directly in `docs/04_BDD/` without a nested folder structure.

### Three Valid File Patterns (ONLY)

| Pattern | Example | Use When |
| ------- | ------- | -------- |
| Section-Only | `BDD-02.14_query_result_filtering.feature` | Standard section (≤800 lines, ≤12 scenarios) |
| Subsection | `BDD-02.24.01_quality_performance.feature` | Section requires splitting |
| Aggregator | `BDD-02.12.00_query_graph_traversal.feature` | Organizing multiple subsections (@redirect, 0 scenarios) |

### Prohibited Patterns (ERROR)

| Pattern | Example | Fix |
|---------|---------|-----|
| _partN suffix | `BDD-02_query_part1.feature` | Use `BDD-02.2.01_query.feature` |
| Single-file | `BDD-02_knowledge_engine.feature` (with scenarios) | Use section-based format |
| features/ subdirectory | `BDD-02_slug/features/` | Put `.feature` files at suite folder root |

### Critical Rules

1. **All `.feature` files in suite folder** - No `features/` subdirectory
2. **Index file mandatory**: `BDD-NN.0_index.md` for all suites
3. **Max 800 lines** per `.feature` file (soft limit: 600)
4. **Max 12 scenarios** per Feature block
5. **Section metadata tags required**: `@section`, `@parent_doc`, `@index`

## Gherkin Syntax

### Feature File Structure

```gherkin
# Traceability Tags (Gherkin-native, NOT in comments)
@section: 2.14
@parent_doc: BDD-02
@index: BDD-02.md
@brd:BRD.02.0103
@prd:PRD.02.0702
@ears:EARS.02.1401

Feature: BDD-02.14: Query Result Filtering
  As a data analyst
  I want filtered query results
  So that I can focus on relevant data

  Background:
    Given the system timezone is "America/New_York"
    And the current time is "09:30:00" in "America/New_York"

  @primary @functional
  Scenario: Successful filter application
    Given valid filter criteria
    When user applies filter
    Then filtered results are returned
    And response time is less than @threshold:PRD.02.perf.api.p95_latency
```

### Tags Placement (CRITICAL - E041)

**Tags MUST be Gherkin-native, NOT in comments.**

```gherkin
# INVALID (frameworks cannot parse comment-based tags):
# @brd: BRD.01.0101
# @prd: PRD.01.0101
Feature: My Feature

# VALID (Gherkin-native tags before Feature):
@brd:BRD.01.0101
@prd:PRD.01.0101
@ears:EARS.01.2401
Feature: My Feature
```

### Times and Timezones (MANDATORY)

- All times include seconds: `HH:MM:SS`
- Use IANA timezone format: `America/New_York`, `America/Los_Angeles`
- Avoid ambiguous abbreviations (EST/EDT/PST/PDT)

```gherkin
Given the current time is "14:30:00" in "America/New_York"
And the system timezone is "America/New_York"
```

## Unified Element ID Format (MANDATORY)

**Pattern**: `BDD.{DOC_NUM}.{HASH}` (3 segments, dot-separated)

| Element Type | Code | Example |
| ------------ | ---- | ------- |
| Test Scenario | 14 | BDD.02.1401 |
| Step | 15 | BDD.02.1501 |

> **REMOVED PATTERNS** - Do NOT use:
>
> - `SCENARIO-XXX`, `TS-XXX` → Use `BDD.NN.14.SS`
> - `STEP-XXX` → Use `BDD.NN.15.SS`
> - `TC-XXX` → Use `BDD.NN.14.SS`

## ADR-Ready Scoring System

**Purpose**: Measures BDD maturity and readiness for ADR progression.

**Format in Document Control**:

```markdown
| **ADR-Ready Score** | ✅ 95% (Target: ≥90%) |
```

### Status and ADR-Ready Score Mapping

| ADR-Ready Score | Required Status |
| --------------- | --------------- |
| ≥90% | Approved |
| 70-89% | In Review |
| <70% | Draft |

### Scoring Criteria

**Scenario Completeness (35%)**:

- All EARS statements translated to BDD scenarios: 15%
- Comprehensive coverage (success/error/edge): 15%
- Observable verification methods specified: 5%

**Testability (30%)**:

- Scenarios are automatable: 15%
- Data-driven Examples tables used: 10%
- Performance benchmarks quantifiable: 5%

**Architecture Requirements Clarity (25%)**:

- Performance, security, scalability quality attributes specified: 15%
- Integration points and external dependencies defined: 10%

**Business Validation (10%)**:

- Business acceptance criteria traceable: 5%
- Measurable success outcomes defined: 5%

**Quality Gate**: Score <90% blocks ADR artifact creation.

## Threshold Registry Integration (MANDATORY)

**All quantitative values MUST use `@threshold:` keys.** No hardcoded magic numbers.

### Inline Step Format

```gherkin
# INVALID (hardcoded):
Then response time is less than 200ms

# VALID (threshold reference):
Then response time is less than @threshold:PRD.035.perf.api.p95_latency
```

### Scenario Tag Format

```gherkin
@threshold:PRD.NN.perf.api.p95_latency
Scenario: API responds within performance threshold
```

### Common Threshold Categories

| Category | BDD Usage | Example Key |
| -------- | --------- | ----------- |
| `perf.*` | Performance validation | `perf.api.p95_latency` |
| `sla.*` | SLA validation | `sla.uptime.target` |
| `limit.*` | Rate limit testing | `limit.api.requests_per_second` |
| `timeout.*` | Timeout validation | `timeout.request.sync` |

## Cumulative Tagging Requirements

**Layer 4 (BDD)**: Must include tags from Layers 1-3 (BRD, PRD, EARS)

**Tag Count**: 3+ tags (@brd, @prd, @ears)

**Format** (Gherkin-native tags before Feature):

```gherkin
@brd:BRD.01.0103
@prd:PRD.01.0702
@ears:EARS.01.2401
Feature: Feature Name
```

## Tag Format Convention

| Notation | Format | Artifacts | Purpose |
| -------- | ------ | --------- | ------- |
| Dash | TYPE-NN | ADR, SPEC, CTR | Technical artifacts - document references |
| Dot | TYPE.NN.xxxx | BRD, PRD, EARS, BDD, SYS, REQ | Hierarchical artifacts - element references |

## Scenario Types

**All 8 categories should be represented:**

| Category | Tag | Description |
|----------|-----|-------------|
| Success Path | `@primary` | Happy path scenarios |
| Alternative Path | `@alternative` | Optional parameters, different workflows |
| Error Conditions | `@negative` | Invalid inputs, error handling |
| Edge Cases | `@edge_case`, `@boundary` | Boundary conditions, limits |
| Data-Driven | `@data_driven` | Parameterized with Examples tables |
| Integration | `@integration` | External system interactions |
| Quality Attributes | `@quality_attribute` | Performance, security, reliability |
| Failure Recovery | `@failure_recovery` | Error recovery, circuit breakers |

### Success Path Example

```gherkin
@primary @functional
Scenario: User logs in successfully
  Given valid credentials
  When user submits login
  Then user is authenticated
```

### Error Conditions Example

```gherkin
@negative @error_handling
Scenario: Trade rejected due to insufficient funds
  Given account balance is $1000
  When trade requires $5000
  Then trade is rejected
  And error code "INSUFFICIENT_FUNDS" is returned
```

### Edge Cases Example

```gherkin
@edge_case @boundary
Scenario: Trade at exact position limit
  Given current delta is 0.499
  And position limit is 0.50
  When trade increases delta to 0.50
  Then trade is accepted
```

### Data-Driven Example

```gherkin
@data_driven
Scenario Outline: Validate price precision
  Given instrument <symbol>
  When price is <price>
  Then precision should be <decimals> decimal places
  Examples:
    | symbol | price  | decimals |
    | SPY    | 450.25 | 2        |
    | AMZN   | 3250.5 | 1        |
```

## Section Metadata Requirements

All `.feature` files MUST include section metadata tags:

```gherkin
@section: NN.SS              # Section number (e.g., 2.1, 2.14)
@parent_doc: BDD-NN          # Parent BDD suite (e.g., BDD-02)
@index: BDD-NN.0_index.md    # Index file reference
@brd:BRD.NN.EE.SS            # Upstream BRD element
@prd:PRD.NN.EE.SS            # Upstream PRD element
@ears:EARS.NN.SS.RR          # Upstream EARS requirement
```

**For subsections, add**:

```gherkin
@parent_section: NN.SS       # Parent section number
```

**Feature Title Format**:

```gherkin
Feature: BDD-NN.SS: Domain Description
```

## Aggregator Files

**Use when**: Section has 5+ subsections

**Requirements**:

- `@redirect` tag MUST be present
- 0 scenarios (redirect stub only)
- List subsections in Feature description

```gherkin
@redirect
@section: 2.12.00
@parent_doc: BDD-02
@index: BDD-02.md

Feature: BDD-02.12: Query Graph Traversal (Aggregator)

  This is a redirect stub. Test scenarios are in subsections:
  - BDD-02.12.01_depth_first.feature - Depth-first traversal tests
  - BDD-02.12.02_breadth_first.feature - Breadth-first traversal tests

Background:
  Given the system timezone is "America/New_York"
  # No scenarios in aggregator - redirect only
```

## Index File Template

**Mandatory**: `BDD-NN.0_index.md` for each suite

```markdown
# BDD-02.0: Knowledge Engine Test Suite Index

## Suite Overview
**Purpose**: Test scenarios for Knowledge Engine functionality
**Scope**: Ingest, Query, Learning, Performance Monitoring

## Section File Map
| Section | File | Scenarios | Lines | Status | Description |
|---------|------|-----------|-------|--------|-------------|
| 02.1 | BDD-02.1_ingest.feature | 8 | 350 | Active | Ingest tests |
| 02.2 | BDD-02.2_query.feature | 10 | 420 | Active | Query tests |

## Traceability Matrix
| BDD Section | Upstream Source | Description |
|-------------|----------------|-------------|
| BDD-02.1 | EARS.02.01-05 | Ingest requirements |
| BDD-02.2 | EARS.02.06-12 | Query requirements |
```

## Creation Process

### Step 1: Read Upstream Artifacts

Read BRD, PRD, and EARS to understand requirements to test.

### Step 2: Reserve Suite ID

Check `docs/04_BDD/` for next available ID (e.g., BDD-01, BDD-02).

**ID Numbering Convention**: Start with 2 digits and expand only as needed.

- ✅ Correct: BDD-01, BDD-99, BDD-102
- ❌ Incorrect: BDD-001, BDD-009 (extra leading zero not required)

### Step 3: Create Suite Folder

```bash
mkdir -p docs/04_BDD/BDD-02_knowledge_engine/
```

### Step 4: Create Index File

```bash
cp ai_dev_ssd_flow/04_BDD/BDD-SECTION-0-TEMPLATE.md docs/04_BDD/BDD-02_knowledge_engine/BDD-02.md
```

### Step 5: Design Section Split

- Identify logical domains or EARS groupings
- Estimate scenarios per section (target: 6-10)
- Plan for subsections if needed (>800 lines)

### Step 6: Create Section Files

```bash
cp ai_dev_ssd_flow/04_BDD/BDD-MVP-TEMPLATE.feature docs/04_BDD/BDD-02_knowledge_engine/BDD-02.1_ingest.feature
```

### Step 7: Add Section Metadata Tags

- `@section`, `@parent_doc`, `@index`
- Upstream traceability: `@brd`, `@prd`, `@ears`

### Step 8: Write Scenarios

For each requirement from EARS/PRD:

1. Success path scenario
2. Error condition scenarios (2-3)
3. Edge case scenarios (1-2)
4. Scenario outlines for parameterized tests

### Step 9: Replace Magic Numbers with Thresholds

- Add to PRD threshold registry first if key missing
- Use `@threshold:PRD.NN.category.key` format

### Step 10: Create Redirect Stub

```bash
# Create redirect stub at docs/04_BDD/ root
touch docs/04_BDD/BDD-02_knowledge_engine.feature
```

Add minimal content with `@redirect` tag and 0 scenarios.

### Step 11: Update Index File

- List all section files with scenario counts
- Add traceability matrix

### Step 12: Validate BDD Suite

```bash
python3 scripts/validate_bdd_suite.py --root BDD
```

### Step 13: Commit Changes

Commit suite folder and redirect stub together.

## Validation

### Validation Error Codes Reference

| Code | Description | Severity |
| ---- | ----------- | -------- |
| E001 | Document Control fields missing | ERROR |
| E002 | Gherkin syntax invalid | ERROR |
| E003 | ADR-Ready Score format invalid | ERROR |
| E004 | Upstream traceability tags missing | ERROR |
| E041 | Tags in comments (not Gherkin-native) | ERROR |
| E008 | Element ID format invalid | ERROR |
| CHECK 9.1 | File naming pattern invalid | ERROR |
| CHECK 9.2 | Prohibited pattern detected | ERROR |
| CHECK 9.3 | Aggregator requirements not met | ERROR |
| CHECK 9.4 | File size exceeds limits | ERROR |
| CHECK 9.5 | Section metadata tags missing | ERROR |
| CHECK 9.6 | Index file missing | ERROR |
| CHECK 9.7 | Non-Gherkin content in .feature file | ERROR |

### Manual Checklist

**File Structure**:

- [ ] All `.feature` files in suite folder (no `features/` subdirectory)
- [ ] Index file exists: `BDD-NN.0_index.md`
- [ ] Redirect stub at `docs/BDD/BDD-NN_slug.feature` (0 scenarios)
- [ ] No file exceeds 800 lines
- [ ] No Feature block exceeds 12 scenarios

**File Naming**:

- [ ] All files match one of 3 valid patterns
- [ ] No prohibited patterns (_partN, single-file)

**Tags and Metadata**:

- [ ] Tags are Gherkin-native (NOT in comments)
- [ ] Section metadata: `@section`, `@parent_doc`, `@index`
- [ ] Cumulative tags: `@brd`, `@prd`, `@ears`
- [ ] All quantitative values use `@threshold:` keys
- [ ] Times include seconds (HH:MM:SS) with IANA timezone

**Scenarios**:

- [ ] All 8 scenario categories represented
- [ ] Given-When-Then structure
- [ ] No subjective language ("fast", "reliable")
- [ ] Observable outcomes in Then steps

**Aggregators** (if applicable):

- [ ] Has `@redirect` tag
- [ ] Has 0 scenarios
- [ ] Lists subsections in Feature description

## Common Pitfalls

| Mistake | Correction |
|---------|------------|
| Tags in comments `# @brd:` | Use Gherkin-native `@brd:` before Feature |
| `ADR-Ready Score: 95%` | Use `✅ 95% (Target: ≥90%)` |
| `response time < 200ms` (hardcoded) | Use `@threshold:PRD.NN.perf.api.p95_latency` |
| `.feature` in `features/` subdir | Put at suite folder root |
| `BDD-02_query_part1.feature` | Use `BDD-02.2.01_query.feature` |
| Missing @ears tag | All 3 upstream tags are MANDATORY |
| Only success scenarios | Include all 8 scenario categories |
| `Status: Approved` (with <90% score) | Use `Status: In Review` or `Draft` |
| File >800 lines | Split into subsections |
| `09:30` (no seconds) | Use `09:30:00` |
| `EST` timezone | Use `America/New_York` |

## Post-Creation Validation (MANDATORY)

**CRITICAL**: Execute validation loop IMMEDIATELY after document creation.

### Automatic Validation Loop

```
LOOP:
  1. Run: python scripts/validate_bdd_suite.py --root BDD
  2. IF errors fixed: GOTO LOOP (re-validate)
  3. IF warnings fixed: GOTO LOOP (re-validate)
  4. IF unfixable issues: Log for manual review
  5. IF clean: Mark VALIDATED, proceed
```

### Quality Gate

**Blocking**: YES - Cannot proceed to ADR creation until validation passes with 0 errors.

---

## Reserved ID Exemption

**Pattern**: `BDD-00_*.md` or `BDD-00_*.feature`

**Scope**: Documents with reserved ID `000` are FULLY EXEMPT from validation.

**Document Types**:

- Index documents (`BDD-00_index.md`)
- Traceability matrix templates
- Glossaries, registries, checklists

---

## Next Skill

After creating BDD, use:

**`doc-adr`** - Create Architecture Decision Records (Layer 5)

The ADR will:

- Document architectural decisions for topics identified in BRD/PRD
- Include `@brd`, `@prd`, `@ears`, `@bdd` tags (cumulative)
- Use Context-Decision-Consequences format
- Reference BDD scenarios that validate the architecture

## Related Resources

- **Template**: `ai_dev_ssd_flow/04_BDD/BDD-MVP-TEMPLATE.feature`
- **Index Template**: `ai_dev_ssd_flow/04_BDD/BDD-SECTION-0-TEMPLATE.md`
- **Aggregator Template**: `ai_dev_ssd_flow/04_BDD/BDD-AGGREGATOR-TEMPLATE.feature`
- **Schema**: `ai_dev_ssd_flow/04_BDD/BDD_MVP_SCHEMA.yaml`
- **Creation Rules**: `ai_dev_ssd_flow/04_BDD/BDD-MVP-TEMPLATE.feature`
- **Validation Rules**: `ai_dev_ssd_flow/04_BDD/BDD_MVP_SCHEMA.yaml`
- **Shared Standards**: `.claude/skills/doc-flow/SHARED_CONTENT.md`
- **ID Standards**: `ai_dev_ssd_flow/ID_NAMING_STANDARDS.md`

## Quick Reference

| Item | Value |
|------|-------|
| **Purpose** | Define executable test scenarios |
| **Layer** | 4 |
| **Tags Required** | @brd, @prd, @ears (3 tags) |
| **ADR-Ready Score** | ≥90% required for "Approved" status |
| **Element ID Format** | `BDD.NN.14.SS` (scenarios), `BDD.NN.15.SS` (steps) |
| **File Structure** | Nested suite folder: `docs/04_BDD/BDD-NN_{slug}/` |
| **Max File Size** | 800 lines (soft: 600) |
| **Max Scenarios** | 12 per Feature block |
| **Time Format** | HH:MM:SS with IANA timezone |
| **Quantitative Values** | Use `@threshold:PRD.NN.category.key` |
| **Next Skill** | doc-adr |

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.1 | 2026-02-27 | Migrated frontmatter to `metadata`; corrected framework reference path to `ai_dev_ssd_flow` | System |
| 1.0 | 2026-02-08 | Initial skill definition with YAML frontmatter standardization | System |

````
