# EARS Tooling Ecosystem: Comprehensive Reference

> **Last updated:** 2026-04-15
>
> EARS (Easy Approach to Requirements Syntax) was created by Alistair Mavin at
> Rolls-Royce and first published in 2009. It provides six sentence templates
> (Ubiquitous, Event-driven, State-driven, Unwanted behavior, Optional feature,
> Complex) for writing structured natural language requirements. EARS is used by
> organizations including Airbus, Bosch, Dyson, Honeywell, Intel, NASA,
> Rolls-Royce, and Siemens. Notably, Mavin has stated that EARS "does not
> require a specialist tool or notation" and is intentionally lightweight. This
> document catalogs every known tool that supports, implements, or relates to
> EARS.

---

## Table of Contents

1. [Commercial Requirements Management Tools with EARS Support](#1-commercial-requirements-management-tools-with-ears-support)
2. [EARS Checking and Validation Tools](#2-ears-checking-and-validation-tools)
3. [EARS Templates and Authoring Aids](#3-ears-templates-and-authoring-aids)
4. [Requirements Linting and Quality Tools (EARS-Adjacent)](#4-requirements-linting-and-quality-tools-ears-adjacent)
5. [Research and Academic Tools](#5-research-and-academic-tools)
6. [Integration Between EARS and BDD/Gherkin](#6-integration-between-ears-and-bddgherkin)
7. [NLP Libraries Commonly Used for Requirements Analysis](#7-nlp-libraries-commonly-used-for-requirements-analysis)
8. [Standards and Guidelines Referenced by EARS Tools](#8-standards-and-guidelines-referenced-by-ears-tools)
9. [Key Findings and Ecosystem Summary](#9-key-findings-and-ecosystem-summary)
10. [References](#10-references)

---

## 1. Commercial Requirements Management Tools with EARS Support

### 1.1 QRA Corp — QVscribe

| Attribute | Detail |
| ----------- | -------- |
| **Vendor** | QRA Corp (Canada) |
| **Product** | QVscribe |
| **Website** | [qracorp.com](https://qracorp.com/) |
| **Type** | Commercial requirements quality analysis tool |
| **Current version** | v1.0.963 (Feb 2026) |
| **Status** | Actively maintained |

**What it does:** QVscribe is the industry-leading dedicated EARS requirements
quality tool. It analyzes natural language requirements against EARS sentence
templates and INCOSE quality rules, providing real-time feedback, scoring, and
improvement suggestions. It operates as a plugin for major requirements
management platforms.

**Key features:**

- Automated EARS template detection and validation (all six patterns:
  ubiquitous, event-driven, state-driven, unwanted behavior, optional feature,
  complex)
- INCOSE requirements quality rule checking
- Requirements quality scoring and dashboard
- Ambiguity, vagueness, and passive voice detection
- Glossary management and terminology consistency
- Readability analysis

**Platform integrations:**

- IBM DOORS Next
- Siemens Polarion ALM
- Jama Connect
- Microsoft Word
- Microsoft Excel
- Standalone (QRAcloud)

**Pricing model:** Custom enterprise pricing. No free tier. Contact vendor for
quotes.

**Links:**

- Product page: `https://qracorp.com/qvscribe/`
- Features: `https://qracorp.com/qvscribe-features/`
- EARS resources: `https://qracorp.com/ears-resources/`
- DOORS Next integration: `https://qracorp.com/qvscribe-for-doors-next/`
- Polarion integration: `https://qracorp.com/qvscribe-polarion/`
- Jama integration: `https://qracorp.com/qvscribe-for-jama/`

---

### 1.2 QRA Corp — ReqWriter

| Attribute | Detail |
| ----------- | -------- |
| **Vendor** | QRA Corp |
| **Product** | ReqWriter |
| **Website** | [qracorp.com/reqwriter](https://qracorp.com/reqwriter/) |
| **Type** | AI-assisted requirements rewriting agent |
| **Status** | Active (Jan 2026) |

**What it does:** ReqWriter is an AI-powered requirements authoring assistant
within the QVscribe/QRAcloud ecosystem. It applies EARS and INCOSE standards to
generate rewrite suggestions that preserve the original requirement's intent
while improving structure and compliance.

**Key features:**

- AI-driven requirement rewriting using EARS templates
- Intent-preserving reformulation
- EARS and INCOSE standard application
- Integrated with QVscribe workflow

**Pricing model:** Part of QRA Corp's commercial offering. Custom pricing.

---

### 1.3 Jama Software — Jama Connect Advisor

| Attribute | Detail |
| ----------- | -------- |
| **Vendor** | Jama Software |
| **Product** | Jama Connect Advisor |
| **Website** | [jamasoftware.com](https://www.jamasoftware.com/platform/jama-connect-advisor) |
| **Type** | AI-powered requirements quality add-on for Jama Connect |
| **Current version** | v9.31+ (2025-2026) |
| **Status** | Actively maintained |

**What it does:** Jama Connect Advisor is a native NLP-powered add-on for the
Jama Connect requirements management platform. It evaluates requirements
against EARS notation patterns and INCOSE best practices, providing quality
scores and improvement recommendations.

**Key features:**

- NLP-based requirements quality analysis
- EARS notation pattern validation
- INCOSE rules alignment
- Real-time quality scoring during authoring
- Batch analysis of requirement sets
- Requirements maturity monitoring over time
- Ambiguity and contradiction detection

**EARS-specific capabilities:**

- Scores requirements against EARS template compliance
- Suggests EARS-compliant reformulations
- Monitors quality scores through the development lifecycle

**Pricing model:** Enterprise subscription. Quote required. Jama Connect
licensing includes Creator, Stakeholder, Reviewer, and Test Runner tiers. No
charge for hosting, reviewers, API usage, or file storage. Advisor is an
add-on.

**Links:**

- Advisor page: `https://www.jamasoftware.com/platform/jama-connect-advisor`
- Requirements management:
  `https://www.jamasoftware.com/requirements-management`

---

### 1.4 IBM — DOORS Next and Engineering AI Hub

| Attribute | Detail |
| ----------- | -------- |
| **Vendor** | IBM |
| **Product** | IBM Engineering Requirements Management DOORS Next |
| **Website** | [ibm.com](https://www.ibm.com/products/requirements-management) |
| **Type** | Enterprise requirements management platform |
| **Current version** | 9.7.x |
| **Status** | Actively maintained |

**What it does:** IBM DOORS Next is one of the most widely used enterprise
requirements management tools, especially in aerospace, defense, and automotive
industries. EARS support is available through third-party integrations rather
than natively.

**EARS support:**

- **Via QVscribe for DOORS Next:** QRA Corp's plugin provides full EARS
  template checking within the DOORS Next environment
- **Via IBM Engineering AI Hub (v1.2, Feb 2026):** IBM's successor to the
  Requirements Quality Assistant (RQA). Uses generative AI for requirements
  quality analysis. Focuses on INCOSE-based rules rather than explicitly
  branding as EARS, but covers similar quality criteria
- **Via DXL scripting:** DOORS classic supports custom DXL scripts that can
  implement EARS pattern matching

**IBM Engineering Requirements Quality Assistant (RQA):** Legacy Watson
NLP-based tool (v3.1.x, discontinued Mar 2023). Detected 10 quality issue
types per INCOSE guidelines. Being replaced by Engineering AI Hub.

**Pricing model:** Enterprise licensing. Quote required. On-premises or SaaS
deployment.

**Links:**

- DOORS Next: `https://www.ibm.com/products/requirements-management`
- Engineering AI Hub: `https://www.ibm.com/docs/en/engineering-ai-hub/1.2.0`
- Legacy RQA: `https://www.ibm.com/docs/en/erqa`

---

### 1.5 Siemens — Polarion REQUIREMENTS

| Attribute | Detail |
| ----------- | -------- |
| **Vendor** | Siemens Digital Industries Software |
| **Product** | Polarion REQUIREMENTS (part of Polarion ALM) |
| **Website** | [polarion.plm.automation.siemens.com](https://polarion.plm.automation.siemens.com/products/polarion-requirements) |
| **Type** | Enterprise requirements management platform |
| **Status** | Actively maintained (2026) |

**What it does:** Polarion is a web-based ALM platform with comprehensive
requirements management including LiveDocs technology, traceability, workflow
automation, and ReqIF support. EARS support is available through a rich
ecosystem of third-party extensions.

**Key features (native):**

- 100% browser-based requirements management
- LiveDocs with paragraph-level traceability
- ReqIF import/export (DOORS interoperability)
- Workflow automation with electronic signatures
- Baseline management and configuration control
- Microsoft Word/Excel import/export

**EARS support (via extensions):**

- **QVscribe for Polarion** — Full EARS + INCOSE checking (QRA Corp)
- **reQlab** — AI-powered EARS + INCOSE + Sophist sentence template validation
  (see section 1.6 below)
- **ALMate** — Generative AI with INCOSE checking
- **Semios** — INCOSE/ISO requirements validation
- **Native Polarion AI** — INCOSE Content Validation built into newer versions

**Pricing model:** Enterprise. Quote required. Named/concurrent user licensing.
30-day free trial available.

---

### 1.6 reQlab — AI-Powered Requirements Validation for Polarion

| Attribute | Detail |
| ----------- | -------- |
| **Vendor** | reQlab (Polarion extension partner) |
| **Product** | reQlab |
| **Website** | [Polarion Extensions](https://extensions.polarion.com/extensions/333-reqlab-ai-powered-requirements-validation-tool-on-premise-gdpr-compliant) |
| **Type** | Commercial Polarion extension |
| **Version** | 2.0 (May 2025) |
| **Status** | Active |

**What it does:** AI-powered requirements validation tool integrated directly
into Polarion ALM. Analyzes requirements using NLP against multiple standards
including EARS.

**Key features:**

- EARS, INCOSE, and Sophist sentence template support
- Missing modal verb detection
- Passive construction identification
- Weak language flagging
- Complex sentence detection
- Redundancy and contradiction analysis
- Improvement suggestions with rephrased requirements
- Customizable error classifications and scoring
- Processes approximately 5,000 requirements per minute
- On-premise deployment option (GDPR compliant)
- German and English language support

**Requirements:** Polarion 2304 (3.23.4) or later.

**Pricing model:** Commercial. Partner-supported. Contact vendor for pricing.

---

### 1.7 Other Commercial Platforms (Limited or No Native EARS Support)

The following commercial requirements management platforms do not have explicit
native EARS support but are worth noting for their requirements quality
features:

#### Visure Requirements ALM

- **Vendor:** Visure Solutions
- **Website:** [visuresolutions.com](https://www.visuresolutions.com/)
- **Quality features:** Quality Analyzer tool, Vivia AI Assistant
- **EARS support:** None documented
- **Pricing:** Commercial. Cloud or on-premise. 14-day free trial.
- **Integrations:** IBM DOORS, Jira, Azure DevOps, GitLab, Sparx EA, ReqIF

#### SPEC Innovations — Innoslate

- **Vendor:** SPEC Innovations
- **Website:** [specinnovations.com](https://specinnovations.com/)
- **Features:** Cloud-native MBSE, requirements management, modeling,
  simulation, AI Quality Analytics
- **EARS support:** None documented
- **Pricing:** Commercial. Cloud and on-premise options.

#### Modern Requirements4DevOps

- **Vendor:** Modern Requirements
- **Website:** [modernrequirements.com](https://www.modernrequirements.com/)
- **Features:** Requirements management natively within Azure DevOps.
  Copilot4DevOps for AI-assisted authoring. INVEST/SWOT/MoSCoW analysis.
- **EARS support:** None documented
- **Pricing:** Commercial. Flexible pricing by team size.

#### ReqView

- **Vendor:** ReqView (Czech Republic)
- **Website:** [reqview.com](https://www.reqview.com/)
- **Features:** Git-based requirements management. ISO/IEC/IEEE 29148
  templates. Jira and Sparx EA integration. Traceability analysis.
- **EARS support:** None documented natively, but supports custom templates
- **Pricing:** Commercial. Free trial available.

#### reqSuite RM

- **Vendor:** OSSENO / PeakAvenue
- **Website:** [osseno.com](https://www.osseno.com/en)
- **Features:** AI-based quality control for requirements. General quality
  checking.
- **EARS support:** No explicit EARS support documented
- **Pricing:** Enterprise. Acquired by PeakAvenue (Oct 2025).

---

## 2. EARS Checking and Validation Tools

### 2.1 Open-Source EARS Validators

#### ears-lint-go

| Attribute | Detail |
| ----------- | -------- |
| **Author** | labeth |
| **Repository** | [github.com/labeth/ears-lint-go](https://github.com/labeth/ears-lint-go) |
| **Language** | Go (100%) |
| **License** | MIT |
| **Status** | Active (Apr 2026, very new) |
| **Stars** | 0 |

**What it does:** A deterministic standalone Go library for linting EARS
requirement sentences. Performs shell parsing, pattern classification, boolean
clause parsing, catalog matching, and generates machine-readable diagnostics.

**Supported EARS patterns:**

- Ubiquitous: `The <system> shall <response>`
- State-driven: `While <expr>, the <system> shall <response>`
- Event-driven: `When <expr>, the <system> shall <response>`
- Optional-feature: `Where <expr>, the <system> shall <response>`
- Unwanted-behaviour: `If <expr>, then the <system> shall <response>`
- Complex (combinations of the above)

**Validation modes:**

- **Strict:** Structural failures are errors
- **Guided:** Structural failures downgrade to warnings

**Installation:** `go get github.com/labeth/ears-lint-go`

---

#### EARS_Checker

| Attribute | Detail |
| ----------- | -------- |
| **Author** | bmd6 |
| **Repository** | [github.com/bmd6/EARS_Checker](https://github.com/bmd6/EARS_Checker) |
| **Language** | Python (100%) |
| **License** | Not specified |
| **Status** | Stale (Oct 2024, 4 commits) |
| **Stars** | 1 |

**What it does:** A Python script that checks requirements for EARS syntax
compliance. Outputs reports in Markdown, plain text, and Org-mode formats.

---

#### earsqa (Browser Extension)

| Attribute | Detail |
| ----------- | -------- |
| **Author** | ammonit-software |
| **Repository** | [github.com/ammonit-software/earsqa](https://github.com/ammonit-software/earsqa) |
| **Language** | TypeScript (67.7%), HTML (24.1%) |
| **License** | MIT |
| **Status** | Active (Mar 2026) |
| **Stars** | 0 |

**What it does:** A Chrome/Edge browser extension providing real-time EARS
validation in contenteditable fields. Useful for checking requirements directly
within web-based tools.

**Validation checks:**

- ERROR: Missing "shall" keyword
- ERROR: Weak words (should, may, might, could)
- WARNING: Vague terms (fast, quickly, user-friendly)
- WARNING: Ambiguous pronouns (it, they, this, that)

**Supported EARS patterns:**

- Ubiquitous: `The [system] shall [action]`
- Event-Driven: `WHEN [trigger] the [system] shall [action]`
- Unwanted: `IF [condition] THEN the [system] shall [action]`
- State-Driven: `WHILE [state] the [system] shall [action]`
- Optional: `WHERE [feature] the [system] shall [action]`

**Installation:** Build from source via npm, then sideload into Chrome/Edge
developer mode. Includes a demo HTML page for testing.

---

#### EARS-Rule-Detection

| Attribute | Detail |
| ----------- | -------- |
| **Author** | chubozeko |
| **Repository** | [github.com/chubozeko/EARS-Rule-Detection](https://github.com/chubozeko/EARS-Rule-Detection) |
| **Language** | Python (100%) |
| **License** | MIT |
| **Status** | Stale (academic project, 3 commits) |
| **Stars** | 8 |

**What it does:** An NLP project from the University of Oulu that classifies
requirements into EARS pattern types. Developed for a Natural Language
Processing and Text Mining course.

**NLP libraries:** NLTK, NumPy, Textstat

**EARS patterns detected:**

- Ubiquitous, Event-driven, State-driven, Unwanted behavior, Optional feature,
  Complex

**Implementation:** Three separate Python scripts (`ears_ubiquitous.py`,
`ears_event_driven.py`, `ears_state_driven.py`), each processing text files and
evaluating sentence compliance with EARS structures.

---

#### template-conformance

| Attribute | Detail |
| ----------- | -------- |
| **Author** | armsp |
| **Repository** | [github.com/armsp/template-conformance](https://github.com/armsp/template-conformance) |
| **Language** | Python |
| **License** | Attribution required |
| **Status** | Abandoned (no activity since ~2019, 2 commits) |
| **Stars** | 3 |

**What it does:** A Flask REST API that checks whether requirements conform to
EARS, RUPP, or Agile user story templates using spaCy NLP.

**Based on:** Arora, Sabetzadeh, Briand, and Zimmer, "Automated Checking of
Conformance to Requirements Templates Using Natural Language Processing," IEEE
Transactions on Software Engineering, 2015.

**Key files:**

- `ears_template_conformance.py` — EARS validation logic
- `rupp_template_conformance.py` — RUPP validation logic
- `agile_user_story_conformance.py` — User story validation
- `template_conformance_core.py` — Core NLP processing
- `api_engine.py` — REST API interface

---

#### requirementchecker.com

| Attribute | Detail |
| ----------- | -------- |
| **Product** | Requirements Checker |
| **URL** | [requirementchecker.com](https://requirementchecker.com/) |
| **Type** | Free web application |
| **Status** | Available |

**What it does:** A free browser-based EARS requirements analyzer with pattern
validation and Excel export. Creator and implementation details are unknown.

---

#### RequirementsSyntax.github.io

| Attribute | Detail |
| ----------- | -------- |
| **Author** | jjappleg |
| **Repository** | [github.com/jjappleg/RequirementsSyntax.github.io](https://github.com/jjappleg/RequirementsSyntax.github.io) |
| **Language** | HTML (65.6%), JavaScript (28.1%), TypeScript (6.3%) |
| **Status** | Stale (Jul 2025, 2 commits) |
| **Stars** | 1 |

**What it does:** A web-based EARS Requirements Syntax Analyzer. Built with
Vite, Tailwind CSS, and ESLint. Minimal documentation available.

---

### 2.2 AI/LLM-Based EARS Evaluation

#### incose-reqts-eval

| Attribute | Detail |
| ----------- | -------- |
| **Author** | jethomp3 |
| **Repository** | [github.com/jethomp3/incose-reqts-eval](https://github.com/jethomp3/incose-reqts-eval) |
| **Language** | Python (100%) |
| **License** | Not specified |
| **Status** | Stale (Nov 2025) |
| **Stars** | 0 |

**What it does:** Automates evaluation of system requirements against INCOSE
guidelines and EARS classification criteria. Designed to help reviewers
identify requirements needing refinement in large requirement sets.

**Two implementations:**

- `incose_evaluator_API.py` — Uses OpenAI API for cloud-based analysis
- `incose_evaluator_Ollama.py` — Uses local Ollama models (e.g., Llama3) for
  privacy-preserving offline processing

**Evaluation approach:**

- INCOSE metrics (weighted total score 0-100 with sub-scores)
- EARS classification (categorizes as Ubiquitous, Event-driven, etc.)
- Context-specific recommendations based on requirement type
- Strict JSON enforcement and automatic malformed data cleanup
- Resume capability for large Excel file processing

**Input/Output:** Excel files (.xlsx)

---

#### LERE (LLM + Enhanced EARS)

| Attribute | Detail |
| ----------- | -------- |
| **Author** | hanhan13579 |
| **Repository** | [github.com/hanhan13579/LERE](https://github.com/hanhan13579/LERE) |
| **Language** | Not specified (prompts + data) |
| **License** | Not specified |
| **Status** | Stale (Dec 2025) |
| **Stars** | 1 |

**What it does:** Uses Large Language Models (Qwen2.5 and ChatGPT-4.0) with an
enhanced EARS paradigm to normalize Chinese requirement texts. Addresses eight
standardization issues: uniqueness, conciseness, verifiability, feasibility,
passive voice avoidance, paradigm adherence, symbol prohibition, and pronoun
elimination.

**Approach:** Two-stage sequential prompt processing with carefully crafted
prompts that guide LLMs to apply EARS patterns to Chinese requirements.

**Dataset:** 138 Chinese requirement texts with eight issue type categories.

---

## 3. EARS Templates and Authoring Aids

### 3.1 IDE Extensions

#### ears-syntax-vscode (VS Code Extension)

| Attribute | Detail |
| ----------- | -------- |
| **Author** | BlueDotBrigade |
| **Repository** | [github.com/BlueDotBrigade/ears-syntax-vscode](https://github.com/BlueDotBrigade/ears-syntax-vscode) |
| **Marketplace** | [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=BlueDotBrigade.ears-syntax-vscode) |
| **Language** | TypeScript |
| **License** | MIT |
| **Version** | 2.2.0 (Dec 2023) |
| **Status** | Stale (no recent activity) |
| **Stars** | 6 |
| **Installs** | 225 |

**What it does:** A VS Code extension that enables writing software
requirements using EARS syntax with syntax highlighting, code completion, and
Markdown compatibility.

**Key features:**

- **Syntax highlighting:** Automatically highlights EARS patterns and keywords
  in `.ears` and `.txt` files
- **Code completion:** Intelligent snippets for EARS templates (e.g.,
  `When [trigger], the system shall [response]`)
- **Markdown support:** Combine EARS syntax with Markdown in the same document

**Installation:** Search "EARS Syntax" in VS Code Extensions or install from
the marketplace. No additional configuration required.

---

#### adv-ears (Advanced EARS with Language Server)

| Attribute | Detail |
| ----------- | -------- |
| **Author** | Amir Arad |
| **Repository** | [github.com/amir-arad/adv-ears](https://github.com/amir-arad/adv-ears) |
| **Language** | TypeScript (97.4%) |
| **License** | MIT |
| **Status** | Active (Apr 2026) |
| **Stars** | 2 |
| **Requires** | Node.js >= 22.0.0 |

**What it does:** A formal requirements language tool that parses Advanced EARS
requirements into an AST, generates PlantUML diagrams, extracts actors and use
cases, and provides a Language Server Protocol (LSP) implementation for IDE
integration.

**Supported requirement patterns:**

- UB (Ubiquitous): `The system shall...`
- EV (Event-driven): `When X the system shall...`
- UW (Unwanted): `The system shall not...`
- ST (State-driven): `While X the system shall...`
- OP (Optional/Conditional): `If X then...` or `Where X...`
- HY (Hybrid): Complex conditional statements

**CLI commands:**

- `validate` — Check requirements syntax
- `parse` — Parse into AST
- `generate` — Generate PlantUML diagrams from requirements
- `analyze` — Extract actors, use cases, and statistics
- `lsp` — Launch the Language Server

**Architecture:** SimpleParser (regex-based) -> ASTGenerator ->
UMLGenerator/Analysis

**VS Code integration:** Includes language server capabilities for real-time
error detection, auto-completion, and hover information.

---

### 3.2 Specification-Driven Development Tools

#### spec-engine (Claude Code Plugin)

| Attribute | Detail |
| ----------- | -------- |
| **Author** | farshidghyasi (inspired by Kiro) |
| **Repository** | [github.com/farshidghyasi/spec-engine](https://github.com/farshidghyasi/spec-engine) |
| **Language** | Shell |
| **License** | MIT |
| **Version** | v2.3.0 (Apr 2026) |
| **Status** | Active |
| **Stars** | 5 |

**What it does:** A Claude Code plugin implementing spec-driven development
that uses EARS notation for all acceptance criteria. Guides features through a
structured pipeline: Requirements (EARS) -> Design -> Tasks (DAG) -> Execution
-> Quality Gates -> Security Review -> Release.

**EARS patterns used:**

- Event-Driven: `WHEN [trigger] THE SYSTEM SHALL [behavior]`
- State-Driven: `WHILE [state] THE SYSTEM SHALL [behavior]`
- Conditional: `IF [condition] WHEN [trigger] THE SYSTEM SHALL`
- Negative: `THE SYSTEM SHALL NOT [behavior]`
- Ubiquitous: `THE SYSTEM SHALL [behavior]`
- Feature-Specific: `WHERE [feature] WHEN [trigger] THE SYSTEM SHALL`

**Key features:**

- Interactive spec creation with `/spec <name>`
- Automatic security EARS criteria generation
- Wave-based DAG execution with parallel task batching
- Four-agent team (Implementer, Tester, Reviewer, Debugger)
- STRIDE threat modeling
- 15-phase security audit
- Wiring enforcement (ensures code is connected, not just written)

---

### 3.3 Conversion and Template Tools

#### EARS-Rupp-s-template-conversion

| Attribute | Detail |
| ----------- | -------- |
| **Author** | parv97 |
| **Repository** | [github.com/parv97/EARS-Rupp-s-template-conversion-](https://github.com/parv97/EARS-Rupp-s-template-conversion-) |
| **Language** | Jupyter Notebook |
| **License** | Not specified |
| **Status** | Stale (Apr 2025) |
| **Stars** | 4 |

**What it does:** Automates conversion of natural language specifications into
EARS and Rupp's requirement templates. Uses a vagueness dictionary and basic
English vocabulary for analysis. Requires Python >= 3.9 and Java 8.

---

## 4. Requirements Linting and Quality Tools (EARS-Adjacent)

These tools do not specifically implement EARS but check for the same kinds of
quality issues that EARS is designed to prevent (ambiguity, vagueness, passive
voice, missing structure).

### 4.1 Commercial Quality Tools

#### Qualicen Scout

| Attribute | Detail |
| ----------- | -------- |
| **Vendor** | Qualicen (Germany) |
| **Website** | [qualicen.de](https://www.qualicen.de/) |
| **Type** | Commercial requirements quality assurance |
| **Status** | Active |

**What it does:** Automatic analysis for reviewing requirement documents using
text analysis technology. Includes over 400 quality assurance rules.

**Key features:**

- Automatic requirements quality analysis
- 400+ built-in quality rules
- Monitors ~54,000 test cases across 63 projects (reported scale)
- Requirements engineering and test design support
- Training courses (200+ available)
- Audit and process consulting services

**EARS support:** Not explicitly documented, but quality rules cover similar
concerns (ambiguity, vagueness, structure).

**Pricing:** Commercial. Contact vendor.

---

#### ScopeMaster

| Attribute | Detail |
| ----------- | -------- |
| **Vendor** | ScopeMaster |
| **Website** | [scopemaster.com](https://scopemaster.com/) |
| **Type** | Commercial requirements quality analysis |
| **Status** | Active |

**What it does:** AI/NLP-powered requirements quality analysis tool. Analyzes
user stories and requirements for ambiguity, completeness, and testability.

**EARS support:** Not explicitly documented, but performs similar
quality checks.

**Pricing:** Commercial. Website inaccessible for detailed pricing at time of
research.

---

### 4.2 Open-Source Quality and Linting Tools

#### TRLC (Treat Requirements Like Code)

| Attribute | Detail |
| ----------- | -------- |
| **Author** | BMW Software Engineering |
| **Repository** | [github.com/bmw-software-engineering/trlc](https://github.com/bmw-software-engineering/trlc) |
| **Language** | Python (94.7%) |
| **License** | GPL-3.0 |
| **Version** | 2.0.3 (Nov 2025) |
| **Status** | Active |
| **Stars** | 89 |

**What it does:** A domain-specific language for writing and linking
requirements with metadata, designed to manage requirements like source code in
version control. Includes a static analysis tool for type checking and
user-defined rule validation.

**Key features:**

- DSL for requirements with metadata
- Static analysis with custom check rules
- CI/CD pipeline integration
- API for building custom tools (HTML rendering, diff, impact analysis)
- Python 3.8-3.14 support

**EARS support:** Not explicitly EARS-aware, but user-defined rules could
enforce EARS patterns.

---

#### Doorstop

| Attribute | Detail |
| ----------- | -------- |
| **Author** | doorstop-dev |
| **Repository** | [github.com/doorstop-dev/doorstop](https://github.com/doorstop-dev/doorstop) |
| **Language** | Python (95.6%) |
| **License** | LGPLv3 |
| **Version** | v3.1 (Jan 2026) |
| **Status** | Active |
| **Stars** | 616 |

**What it does:** Requirements management system that stores textual
requirements alongside source code in version control. Uses YAML-based storage
with hierarchical document trees and item traceability.

**Key features:**

- YAML-based linkable items
- Hierarchical document tree
- Traceability validation
- HTML publishing
- Command-line interface
- Integrity checks

**EARS support:** None native, but YAML structure could be extended with custom
EARS-related attributes.

---

#### sphinx-needs

| Attribute | Detail |
| ----------- | -------- |
| **Author** | useblocks |
| **Repository** | [github.com/useblocks/sphinx-needs](https://github.com/useblocks/sphinx-needs) |
| **Language** | Python (94.3%) |
| **License** | MIT |
| **Version** | 8.0.0 (Mar 2026) |
| **Status** | Active |
| **Stars** | 274 |

**What it does:** A Sphinx extension for defining, linking, and filtering
requirement-class objects in documentation. Supports requirements,
specifications, implementations, and test cases with visualization tools.

**Key features:**

- Needtable, Needflow, and Needpie visualizations
- DO-178B/C, IEC-61508, ISO 26262, ED-12C compliance support
- Custom need types (bugs, user stories, etc.)
- Customizable layouts and styling

**EARS support:** None native, but need types and custom directives could model
EARS patterns.

---

#### VisualNarrator

| Attribute | Detail |
| ----------- | -------- |
| **Author** | Marcel Robeer (Utrecht University) |
| **Repository** | [github.com/MarcelRobeer/VisualNarrator](https://github.com/MarcelRobeer/VisualNarrator) |
| **Language** | Python |
| **License** | Not specified |
| **Status** | Stale (2015-2019) |
| **Stars** | 29 |

**What it does:** Transforms user stories into conceptual models containing
entities and relationships using spaCy NLP. Extracts structured data from
natural language requirements.

**EARS support:** None, focused on user stories rather than EARS templates.

---

#### reqT

| Attribute | Detail |
| ----------- | -------- |
| **Author** | reqT |
| **Repository** | [github.com/reqT/reqT](https://github.com/reqT/reqT) |
| **Language** | Scala (98.4%) |
| **License** | Apache v2 (core) / AGPLv3 (desktop, due to JaCoP dependency) |
| **Version** | v4.6.3 (Dec 2025) |
| **Status** | Active |
| **Stars** | 22 |

**What it does:** Open source requirements engineering tool combining natural
language with formal structure. Supports modeling, analysis, visualization, and
constraint-based release allocation via Scala scripting.

**EARS support:** None documented.

---

#### specfact-cli

| Attribute | Detail |
| ----------- | -------- |
| **Author** | nold-ai |
| **Repository** | [github.com/nold-ai/specfact-cli](https://github.com/nold-ai/specfact-cli) |
| **Language** | Python |
| **License** | Apache-2.0 |
| **Version** | v0.46.2 (Apr 2026, beta) |
| **Status** | Active |
| **Stars** | 15 |

**What it does:** CLI tool for validation and alignment in software delivery.
AI-assisted code review against custom contracts, drift detection across
backlog/specs/tests/code, local-first validation.

**EARS support:** None. Uses contract-first methodology rather than EARS.

---

### 4.3 Requirements Quality Standards Tools

#### OpenReq

| Attribute | Detail |
| ----------- | -------- |
| **Organization** | OpenReq EU Research Consortium |
| **Website** | [openreq.eu](https://www.openreq.eu/) |
| **Type** | Research platform |
| **Status** | Available (self-hosted APIs and OpenReq Live) |

**What it does:** Research-driven requirements engineering platform with
requirements intelligence, personal recommendations, group decision support,
and dependency management.

**EARS support:** None explicitly documented.

---

## 5. Research and Academic Tools

### 5.1 EARS-CTRL (Requirements to Controllers)

| Attribute | Detail |
| ----------- | -------- |
| **Authors** | Levi Lúcio, Salman Rahman, Chih-Hong Cheng, Alistair Mavin |
| **Repository** | [github.com/levilucio/EARS-CTRL](https://github.com/levilucio/EARS-CTRL) |
| **Language** | Java (99.8%) |
| **License** | Apache-2.0 |
| **Status** | Stale (Jul 2025) |
| **Stars** | 5 |
| **Paper** | "Just Formal Enough? Automated Analysis of EARS Requirements" (NASA Formal Methods Conference, 2017, 56 citations) |

**What it does:** Converts EARS requirements into executable software
controllers that can be simulated. Built on JetBrains MPS with mbeddr, it
provides an integrated environment where requirements are directly transformed
into simulatable controller implementations.

**Key features:**

- EARS requirements editing within MPS IDE
- Transformation to executable controllers
- MATLAB/Simulink model generation (R2017a)
- Interactive simulation of requirements
- Video demo: [youtube.com/watch?v=IOyFRd6mbd0](https://youtu.be/IOyFRd6mbd0)

**Requirements:** mbeddr for MPS 3.4.3, MATLAB/Simulink R2017a, Gradle build

---

### 5.2 EARS-CTRL-light

| Attribute | Detail |
| ----------- | -------- |
| **Author** | levilucio |
| **Repository** | [github.com/levilucio/EARS-CTRL-light](https://github.com/levilucio/EARS-CTRL-light) |
| **Language** | Java (99.4%) |
| **License** | Apache-2.0 |
| **Status** | Stale |
| **Stars** | 2 |

**What it does:** A lightweight version of EARS-CTRL that supports EARS-based
requirement specification and controller construction but does not generate
Simulink models. Useful for EARS authoring without the full simulation
pipeline.

---

### 5.3 Academic Requirements Quality Tools (Not Publicly Available)

These tools are described in academic papers but have no public download
available:

| Tool | Origin | Description | Reference |
| ------ | -------- | ------------- | ----------- |
| **QuARS** (Quality Analyzer for Requirements Specifications) | ISTI-CNR, Italy / CMU SEI | NLP-based lexical and syntactic analysis for ambiguity, clarity, understandability | SEI report, 2005 |
| **QuARS Express** | ISTI-CNR, Italy | Enhanced version handling structured requirement documents | NLP4RE 2019 |
| **RETA** (Requirements Template Analyzer) | Academic | Detects vague terms, quantifiers, pronouns, complex requirements, adverbs | Literature references |
| **ARM** (Automated Requirements Measurement) | Academic | Ambiguity detection tool | Comparative studies |
| **AmbiDetect** | Academic | ML-based ambiguous requirement classifier using scikit-learn | Paper prototype |
| **NAI** (Nocuous Ambiguity Identification) | Academic | ML-based coordination ambiguity detection | Paper prototype |

---

### 5.4 Key Academic Papers on EARS Tools

| Year | Paper | Authors | Venue | Citations | Tool/Contribution |
| ------ | ------- | --------- | ------- | ----------- | ------------------- |
| 2009 | "Easy Approach to Requirements Syntax (EARS)" | A. Mavin, P. Wilkinson, A. Harwood | IEEE RE | 492 | Original EARS methodology |
| 2010 | "Big EARS (The Return of 'Easy Approach to Requirements Engineering')" | A. Mavin, P. Wilkinson | IEEE RE | 98 | EARS extensions and lessons |
| 2011 | "Adv-EARS: A Formal Requirements Syntax for Derivation of Use Case Models" | D. Majumdar, S. Sengupta, A. Kanjilal | Springer | 16 | Advanced EARS with formal grammar |
| 2011 | "Automated Requirements Modelling with Adv-EARS" | D. Majumdar, S. Sengupta, A. Kanjilal | J. Info. Tech. | 18 | Automated modeling from Adv-EARS |
| 2015 | "Automated Checking of Conformance to Requirements Templates Using NLP" | Arora, Sabetzadeh, Briand, Zimmer | IEEE TSE | N/A | template-conformance tool basis |
| 2016 | "Listens Learned (8 Lessons Learned Applying EARS)" | A. Mavin, P. Wilkinson, S. Gregory | IEEE RE | 43 | Practical EARS application lessons |
| 2017 | "Just Formal Enough? Automated Analysis of EARS Requirements" | L. Lúcio, S. Rahman, C. Cheng, A. Mavin | NASA FM | 56 | EARS-CTRL tool |
| 2018 | "A CLEAR Adoption of EARS" | B. Hall | IEEE | 6 | SysML integration discussion |
| 2019 | "Ten Years of EARS" | A. Mavin, P. Wilkinson | IEEE Software | 24 | EARS retrospective |
| 2024 | "Benchmarking Requirement Template Systems" | K. Grosser, A.S. Ahmadian, et al. | RE Journal | 4 | EARS vs. MASTeR comparison |
| 2024 | "Towards Pattern-based Domain-Specific Requirements Engineering" | T. Chuprina, D. Mendez, et al. | arXiv | N/A | Domain-specific EARS for UAV flight controllers |

---

## 6. Integration Between EARS and BDD/Gherkin

### 6.1 Direct EARS-to-Gherkin Bridge Tools

There is a notable gap in tooling that directly bridges EARS requirements to
Gherkin scenarios. The few tools that exist are experimental or emerging:

#### RequireKit (require-kit)

| Attribute | Detail |
| ----------- | -------- |
| **Author** | requirekit |
| **Repository** | [github.com/requirekit/require-kit](https://github.com/requirekit/require-kit) |
| **Language** | Python |
| **License** | MIT |
| **Version** | v1.0.0 |
| **Status** | Active (2025-2026) |
| **Stars** | 1, 151 commits |

**What it does:** RequireKit is currently the only known tool that explicitly
bridges EARS requirements to Gherkin scenarios. It provides an end-to-end
workflow:

1. **Gather requirements** interactively
2. **Formalize to EARS** via `/formalize-ears` command
3. **Generate BDD scenarios** via `/generate-bdd` command
4. **Maintain traceability** from Gherkin features back to EARS requirements

**Supported EARS patterns:**

- Ubiquitous: `The [system] shall [behavior]`
- Event-Driven: `When [trigger], the [system] shall [response]`
- State-Driven: `While [state], the [system] shall [behavior]`
- Unwanted Behavior: `If [error], then the [system] shall [recovery]`
- Optional Feature: `Where [feature], the [system] shall [behavior]`

**Epic/Feature hierarchy:** Organizes requirements into Epic -> Feature ->
Requirement structure suitable for agile workflows. Technology-agnostic
output.

---

#### Carrot PRD (Gherkin Extension for Requirements)

| Attribute | Detail |
| ----------- | -------- |
| **Author** | talvinder |
| **Repository** | [github.com/talvinder/carrot-product-requirements-document-prd](https://github.com/talvinder/carrot-product-requirements-document-prd) |
| **Language** | Gherkin |
| **License** | MIT |
| **Status** | Stale (Jun 2023) |
| **Stars** | 40 |

**What it does:** Extends Gherkin syntax for creating Product Requirements
Documents. While not EARS-specific, it bridges the gap between structured
requirements and BDD by adding Feature blocks with user stories, scenarios,
tags for metadata, and object-action tracking across documents.

**Relevance to EARS-Gherkin integration:** Demonstrates how Gherkin syntax can
be extended for requirements management, a pattern that could be adapted for
EARS templates.

---

### 6.2 Traceability Tools (Requirements to Tests)

The major commercial platforms (Jama Connect, IBM DOORS Next, Polarion) all
provide traceability from requirements to test cases, which can include Gherkin
scenarios when test management is integrated:

| Platform | Traceability Features |
| ---------- | ---------------------- |
| **Jama Connect** | Live Traceability between requirements, tests, risks. Can link to external Gherkin tests via integrations. |
| **IBM DOORS Next** | Full lifecycle traceability across ELM suite. Links to test management via Rational Quality Manager. |
| **Polarion ALM** | Paragraph-level traceability in LiveDocs. Links requirements to test cases. ReqIF exchange. |
| **ReqView** | Git-based traceability. Jira integration for linking to BDD test scenarios. |
| **Doorstop** | Item linking and traceability validation in version control. |
| **sphinx-needs** | Needflow/Needtable for requirements-to-test traceability in Sphinx documentation. |

### 6.3 Conceptual Mapping: EARS to Gherkin

No standardized mapping from EARS templates to Gherkin scenarios exists as a
formal specification. However, natural correspondences include:

| EARS Pattern | Gherkin Mapping |
| ------------- | ----------------- |
| **Ubiquitous**: `The [system] shall [behavior]` | `Then [system] [behavior]` (invariant assertion) |
| **Event-driven**: `When [trigger], the [system] shall [response]` | `When [trigger]` / `Then [system] [response]` |
| **State-driven**: `While [state], the [system] shall [behavior]` | `Given [state]` / `Then [system] [behavior]` |
| **Unwanted behavior**: `If [condition], then the [system] shall [recovery]` | `Given [error condition]` / `Then [system] [recovery]` |
| **Optional feature**: `Where [feature], the [system] shall [behavior]` | `Given [feature] is enabled` / `Then [system] [behavior]` (tagged with `@feature`) |
| **Complex**: Combination of above | Scenario Outline with multiple Given/When/Then steps |

---

## 7. NLP Libraries Commonly Used for Requirements Analysis

These general-purpose NLP libraries serve as the foundation for most custom
EARS analysis tools:

| Library | URL | Language | Use in EARS Tools |
| --------- | ----- | ---------- | ------------------- |
| **spaCy** | [spacy.io](https://spacy.io/) | Python | Most commonly used. Foundation for template-conformance, EARS-Rule-Detection. POS tagging, dependency parsing, NER. |
| **NLTK** | [nltk.org](https://www.nltk.org/) | Python | Used in EARS-Rule-Detection. Tokenization, POS tagging, parsing. Good for rule-based analysis. |
| **Hugging Face Transformers** | [huggingface.co](https://huggingface.co/) | Python | BERT, SpanBERT models used in recent requirements ambiguity research. |
| **TextBlob** | [PyPI](https://pypi.org/project/textblob/) | Python | Lightweight NLP. Sentiment analysis, POS tagging. |
| **Textstat** | [PyPI](https://pypi.org/project/textstat/) | Python | Used in EARS-Rule-Detection. Text readability metrics. |

---

## 8. Standards and Guidelines Referenced by EARS Tools

| Standard | Organization | Relevance to EARS |
| ---------- | ------------- | ------------------- |
| **INCOSE Guide to Writing Requirements (GtWR)** | INCOSE | Primary quality standard. EARS patterns align with INCOSE structure rules. Both Jama Advisor and QVscribe check against INCOSE rules. |
| **ISO/IEC/IEEE 29148:2018** | ISO/IEC/IEEE | Systems and software engineering requirements processes. ReqView provides templates based on this standard. |
| **IEEE 830** | IEEE | Software Requirements Specifications standard. Predecessor to 29148. |
| **DO-178C** | RTCA | Airborne software. EARS widely used in aerospace requirements per this standard. sphinx-needs supports DO-178C compliance. |
| **ISO 26262** | ISO | Automotive functional safety. EARS used in automotive requirements. sphinx-needs supports ISO 26262. |
| **IEC 61508** | IEC | Functional safety of electrical/electronic systems. sphinx-needs supports IEC 61508. |
| **IREB CPRE** | IREB | Certified Professional for Requirements Engineering. EARS taught as part of IREB curriculum. |

---

## 9. Key Findings and Ecosystem Summary

### 9.1 The EARS Tool Landscape Is Sparse but Growing

EARS was intentionally designed to be tool-agnostic ("no specialist tool is
necessary"). This philosophy has resulted in a smaller tooling ecosystem
compared to methodologies like BDD/Gherkin, which were designed around
automation from the start.

### 9.2 Two Dominant Commercial Tools

1. **QRA QVscribe** is the industry-leading dedicated EARS tool. It integrates
   with all major requirements management platforms and provides the deepest
   EARS-specific analysis.
2. **Jama Connect Advisor** is the second major option, offering native EARS +
   INCOSE checking within the Jama ecosystem.

### 9.3 Platform EARS Support Is Indirect

IBM DOORS Next and Siemens Polarion do not have native EARS support but offer
it through extensions (QVscribe, reQlab, Engineering AI Hub). The trend is
toward AI-powered requirements quality that encompasses EARS-like checks
without necessarily branding them as EARS.

### 9.4 Open-Source EARS Tools Are Nascent

The most promising open-source projects are:

- **adv-ears** — TypeScript LSP server with PlantUML generation (most
  architecturally sophisticated)
- **ears-lint-go** — Go linter for CI/CD integration (newest, most focused)
- **earsqa** — Browser extension for real-time validation (practical for web
  tools)
- **RequireKit** — Only tool bridging EARS to BDD/Gherkin (most relevant for
  end-to-end workflows)
- **spec-engine** — Claude Code plugin using EARS for spec-driven development
  (most integrated with modern AI workflows)

### 9.5 No EARS Packages on PyPI or npm

Despite EARS being a well-known methodology in requirements engineering, no
dedicated EARS package exists on PyPI or npm. All implementations are
standalone repositories.

### 9.6 The EARS-Gherkin Bridge Is Nearly Empty

RequireKit is the only known tool that explicitly converts EARS requirements to
Gherkin scenarios. This represents a significant opportunity for tooling
development, especially given the natural correspondences between EARS patterns
and Gherkin Given/When/Then structure.

### 9.7 AI/LLM Integration Is the Emerging Frontier

Several 2025-2026 projects combine EARS with LLMs:

- **spec-engine** uses EARS in Claude Code workflows
- **LERE** applies LLMs to EARS for Chinese requirements normalization
- **incose-reqts-eval** uses OpenAI/Ollama for EARS classification
- **IBM Engineering AI Hub** replaces rule-based NLP with generative AI
- **QRA ReqWriter** uses AI for EARS-compliant rewrites

This signals that EARS may become more prominent as AI-assisted requirements
engineering grows.

### 9.8 Academic Tools Are Largely Unavailable

Research tools like QuARS, RETA, ARM, AmbiDetect, and NAI are described in
papers but have no public downloads. This gap means that practitioners cannot
easily benefit from academic advances in requirements quality analysis.

---

## 10. References

### Official EARS Resources

- Alistair Mavin (EARS creator):
  [alistairmavin.com/ears](https://alistairmavin.com/ears/)
- EARS training:
  [alistairmavin.com/training](https://alistairmavin.com/training/)

### Commercial Tool Vendors

- QRA Corp:
  [qracorp.com](https://qracorp.com/)
- QRA QVscribe features:
  [qracorp.com/qvscribe-features](https://qracorp.com/qvscribe-features/)
- QRA ReqWriter:
  [qracorp.com/reqwriter](https://qracorp.com/reqwriter/)
- QRA EARS resources:
  [qracorp.com/ears-resources](https://qracorp.com/ears-resources/)
- Jama Software:
  [jamasoftware.com](https://www.jamasoftware.com/)
- Jama Connect Advisor:
  [jamasoftware.com/platform/jama-connect-advisor](https://www.jamasoftware.com/platform/jama-connect-advisor)
- IBM Engineering:
  [ibm.com/products/requirements-management](https://www.ibm.com/products/requirements-management)
- IBM Engineering AI Hub:
  [ibm.com/docs/en/engineering-ai-hub/1.2.0](https://www.ibm.com/docs/en/engineering-ai-hub/1.2.0)
- Siemens Polarion:
  [polarion.plm.automation.siemens.com](https://polarion.plm.automation.siemens.com/)
- reQlab for Polarion:
  [extensions.polarion.com](https://extensions.polarion.com/extensions/333-reqlab-ai-powered-requirements-validation-tool-on-premise-gdpr-compliant)
- Qualicen:
  [qualicen.de](https://www.qualicen.de/)
- Visure Solutions:
  [visuresolutions.com](https://www.visuresolutions.com/)
- Modern Requirements:
  [modernrequirements.com](https://www.modernrequirements.com/)
- ReqView:
  [reqview.com](https://www.reqview.com/)

### Open-Source Repositories

- adv-ears:
  [github.com/amir-arad/adv-ears](https://github.com/amir-arad/adv-ears)
- ears-syntax-vscode:
  [github.com/BlueDotBrigade/ears-syntax-vscode](https://github.com/BlueDotBrigade/ears-syntax-vscode)
- ears-lint-go:
  [github.com/labeth/ears-lint-go](https://github.com/labeth/ears-lint-go)
- earsqa:
  [github.com/ammonit-software/earsqa](https://github.com/ammonit-software/earsqa)
- EARS_Checker:
  [github.com/bmd6/EARS_Checker](https://github.com/bmd6/EARS_Checker)
- EARS-Rule-Detection:
  [github.com/chubozeko/EARS-Rule-Detection](https://github.com/chubozeko/EARS-Rule-Detection)
- template-conformance:
  [github.com/armsp/template-conformance](https://github.com/armsp/template-conformance)
- EARS-CTRL:
  [github.com/levilucio/EARS-CTRL](https://github.com/levilucio/EARS-CTRL)
- EARS-CTRL-light:
  [github.com/levilucio/EARS-CTRL-light](https://github.com/levilucio/EARS-CTRL-light)
- EARS-Rupp-s-template-conversion:
  [github.com/parv97/EARS-Rupp-s-template-conversion-](https://github.com/parv97/EARS-Rupp-s-template-conversion-)
- RequirementsSyntax.github.io:
  [github.com/jjappleg/RequirementsSyntax.github.io](https://github.com/jjappleg/RequirementsSyntax.github.io)
- spec-engine:
  [github.com/farshidghyasi/spec-engine](https://github.com/farshidghyasi/spec-engine)
- LERE:
  [github.com/hanhan13579/LERE](https://github.com/hanhan13579/LERE)
- incose-reqts-eval:
  [github.com/jethomp3/incose-reqts-eval](https://github.com/jethomp3/incose-reqts-eval)
- RequireKit:
  [github.com/requirekit/require-kit](https://github.com/requirekit/require-kit)
- requirementchecker.com:
  [requirementchecker.com](https://requirementchecker.com/)
- TRLC:
  [github.com/bmw-software-engineering/trlc](https://github.com/bmw-software-engineering/trlc)
- Doorstop:
  [github.com/doorstop-dev/doorstop](https://github.com/doorstop-dev/doorstop)
- sphinx-needs:
  [github.com/useblocks/sphinx-needs](https://github.com/useblocks/sphinx-needs)
- VisualNarrator:
  [github.com/MarcelRobeer/VisualNarrator](https://github.com/MarcelRobeer/VisualNarrator)
- reqT:
  [github.com/reqT/reqT](https://github.com/reqT/reqT)
- specfact-cli:
  [github.com/nold-ai/specfact-cli](https://github.com/nold-ai/specfact-cli)
- Carrot PRD:
  [github.com/talvinder/carrot-product-requirements-document-prd](https://github.com/talvinder/carrot-product-requirements-document-prd)
- OpenReq:
  [openreq.eu](https://www.openreq.eu/)

### Academic Papers

- Mavin, Wilkinson, Harwood.
  "Easy Approach to Requirements Syntax (EARS)."
  IEEE RE, 2009.
- Mavin, Wilkinson. "Big EARS." IEEE RE, 2010.
- Majumdar, Sengupta, Kanjilal.
  "Adv-EARS: A Formal Requirements Syntax for
  Derivation of Use Case Models." Springer, 2011.
- Arora, Sabetzadeh, Briand, Zimmer.
  "Automated Checking of Conformance to
  Requirements Templates Using NLP."
  IEEE TSE, 2015.
- Mavin, Wilkinson, Gregory.
  "Listens Learned (8 Lessons Learned Applying
  EARS)." IEEE RE, 2016.
- Lucio, Rahman, Cheng, Mavin.
  "Just Formal Enough? Automated Analysis of
  EARS Requirements." NASA FM, 2017.
- Hall. "A CLEAR Adoption of EARS." IEEE, 2018.
- Mavin, Wilkinson.
  "Ten Years of EARS." IEEE Software, 2019.
- Grosser, Ahmadian, et al.
  "Benchmarking Requirement Template Systems."
  RE Journal, 2024.
- Chuprina, Mendez, et al.
  "Towards Pattern-based Domain-Specific
  Requirements Engineering."
  arXiv:2404.17338, 2024.

### VS Code Marketplace

- EARS Syntax:
  [marketplace.visualstudio.com](https://marketplace.visualstudio.com/items?itemName=BlueDotBrigade.ears-syntax-vscode)
