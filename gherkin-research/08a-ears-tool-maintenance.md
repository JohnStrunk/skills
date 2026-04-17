# EARS & Requirements Engineering Tool Maintenance Status

> **Last reviewed:** 2026-04-15
>
> **Summary:** The EARS tooling ecosystem is significantly sparser than
> Gherkin's. There are only **2 actively maintained commercial tools** with
> native EARS support (QRA QVscribe and Jama Connect Advisor), and a small
> but growing set of open-source projects. Most open-source EARS tools are
> early-stage or academic prototypes. The major requirements management
> platforms (DOORS Next, Polarion, Jama) all now offer AI-assisted
> requirements quality features, with EARS/INCOSE checking available via
> built-in or third-party extensions. No dedicated EARS package exists on
> PyPI or npm.

---

## EARS-Specific Tools

| Tool | Type | URL | Last Update | Status | Notes |
| ------ | ------ | ----- | ------------- | -------- | ------- |
| **QRA QVscribe** | Commercial | [qracorp.com](https://qracorp.com/) | Feb 2026 (v1.0.963) | **Active** | Industry-leading EARS checker. Integrates with Polarion, DOORS Next, Jama, Word, Excel. Automated EARS templating (ubiquitous, state-driven, event-driven, unwanted behavior). Custom pricing, no free tier. |
| **QRA ReqWriter** | Commercial | [qracorp.com/reqwriter](https://qracorp.com/reqwriter/) | Jan 2026 | **Active** | AI-assisted requirements rewriting agent within QVscribe/QRAcloud. Applies EARS and INCOSE standards. Generates rewrite suggestions preserving intent. |
| **Jama Connect Advisor** | Commercial | [jamasoftware.com](https://www.jamasoftware.com/solutions/artificial-intelligence/) | v9.31 (2025-2026) | **Active** | Native NLP add-on for Jama Connect. Applies INCOSE rules and EARS notation patterns. Real-time quality scoring, batch analysis, requirement refinement. Enterprise pricing (quote required). |
| **BlueDotBrigade ears-syntax-vscode** | Open-source | [GitHub](https://github.com/BlueDotBrigade/ears-syntax-vscode) | Dec 2023 (v2.2.0) | **Stale** | VS Code extension for `.ears` and `.txt` files. Syntax highlighting and code completion for EARS patterns. Available on VS Code Marketplace. 6 stars. No recent activity. |
| **adv-ears** | Open-source | [GitHub](https://github.com/amir-arad/adv-ears) | Apr 2026 | **Active** | TypeScript LSP server + VS Code extension for "Advanced EARS" format. Parses requirements into AST, generates PlantUML diagrams, extracts actors/use cases. 2 stars, actively developed. |
| **EARS-Rule-Detection** | Open-source | [GitHub](https://github.com/chubozeko/EARS-Rule-Detection) | Apr 2026 (last starred) | **Stale** | Python NLP project (University of Oulu). Classifies requirements into EARS patterns using spaCy. Academic prototype; no recent code changes. 8 stars. |
| **EARS_Checker** | Open-source | [GitHub](https://github.com/bmd6/EARS_Checker) | Oct 2024 | **Stale** | Python script checking requirements for EARS syntax compliance. Minimal (4 commits). Outputs reports in Markdown/text/Org. 1 star. |
| **ears-lint-go** | Open-source | [GitHub](https://github.com/labeth/ears-lint-go) | Apr 2026 | **Active** | Go library for linting EARS requirements. Parses 6 EARS patterns, validates against catalogs, strict/guided modes. 0 stars, very new (created Apr 2026). |
| **earsqa** | Open-source | [GitHub](https://github.com/ammonit-software/earsqa) | Mar 2026 | **Active** | Browser extension (Chrome/Edge) for real-time EARS validation in contenteditable fields. Detects missing "shall," weak language, vague terms. TypeScript. 0 stars, new. |
| **spec-engine** | Open-source | [GitHub](https://github.com/farshidghyasi/spec-engine) | Apr 2026 (v2.3.0) | **Active** | Claude Code plugin for spec-driven development. Uses EARS notation for structured requirements, wave-based execution, quality gates. Shell-based. 5 stars. |
| **incose-reqts-eval** | Open-source | [GitHub](https://github.com/jethomp3/incose-reqts-eval) | Nov 2025 | **Stale** | Python AI tool evaluating requirements against INCOSE/EARS. Uses OpenAI or Ollama. Processes Excel files, outputs JSON scores. Early prototype. 0 stars. |
| **template-conformance** | Open-source | [GitHub](https://github.com/armsp/template-conformance) | 2019 (core) | **Abandoned** | Python/Flask app checking conformance to EARS, RUPP, and Agile user story templates via spaCy. 3 stars, 2 commits, no activity since ~2019. |
| **EARS-CTRL** | Open-source | [GitHub](https://github.com/levilucio/EARS-CTRL) | Jul 2025 | **Stale** | Java tool for expressing/analyzing controllers as EARS requirements. Academic (research). 5 stars, 17 open issues. Minimal recent activity. |
| **LERE** | Open-source | [GitHub](https://github.com/hanhan13579/LERE) | Dec 2025 | **Stale** | LLM + enhanced EARS method for normalizing Chinese requirements texts. Uses Qwen2.5/ChatGPT-4.0. Academic research paper companion. 1 star. |
| **requirementchecker.com** | Free web tool | [requirementchecker.com](https://requirementchecker.com/) | Unknown | **Available** | Free browser-based EARS requirements analyzer with pattern validation and Excel export. Creator unknown. Limited information available. |
| **RequirementsSyntax.github.io** | Open-source | [GitHub](https://github.com/jjappleg/RequirementsSyntax.github.io) | Jul 2025 | **Stale** | HTML website for EARS requirements syntax analysis. 1 star. Minimal project. |
| **EARS-Rupp-s-template-conversion** | Open-source | [GitHub](https://github.com/parv97/EARS-Rupp-s-template-conversion-) | Apr 2025 | **Stale** | Jupyter Notebook for automated NL-to-EARS/Rupp template conversion. Academic project. 4 stars. |
| **RequireKit (require-kit)** | Open-source | [GitHub](https://github.com/requirekit/require-kit) | 2025-2026 | **Active** | AI-powered requirements toolkit with EARS formalization, BDD/Gherkin generation, and epic/feature hierarchy. v1.0.0. 1 star, 151 commits. |

---

## Major Requirements Management Platforms

| Platform | Vendor | URL | Status | EARS Support | Pricing |
| ---------- | -------- | ----- | -------- | ------------- | --------- |
| **Jama Connect** | Jama Software | [jamasoftware.com](https://www.jamasoftware.com/) | **Active** (v9.32, Feb 2026) | **Native via Jama Connect Advisor** — NLP-based EARS + INCOSE checking, real-time scoring, batch analysis, requirement refinement | Enterprise, quote required. Annual subscription. |
| **IBM DOORS Next** | IBM | [ibm.com](https://www.ibm.com/products/requirements-management) | **Active** (9.7.x) | **Via IBM Engineering AI Hub** (replaced RQA). AI-powered requirements quality. INCOSE-based, not explicitly EARS-branded. Also integrates with QVscribe. | Enterprise, quote required. On-prem or SaaS. |
| **IBM Engineering AI Hub** | IBM | [ibm.com](https://www.ibm.com/products/requirements-quality-assistant) | **Active** (v1.2, Feb 2026) | Successor to IBM RQA. Uses generative AI. Requirements quality analysis, engineering assistant, MBSE use case discovery. | Enterprise add-on to ELM. |
| **IBM Engineering RQA** | IBM | [ibm.com](https://www.ibm.com/docs/en/erqa) | **Replaced** (v3.1.x, Mar 2023) | Watson NLP-based. Detected 10 quality issues per INCOSE. **Being replaced by Engineering AI Hub.** Third-party SaaS still available via REQUISIS. | Legacy; transition to AI Hub recommended. |
| **Polarion REQUIREMENTS** | Siemens | [polarion.plm.automation.siemens.com](https://polarion.plm.automation.siemens.com/) | **Active** (2026) | **Via extensions**: QVscribe for Polarion (EARS+INCOSE), reQlab (EARS+INCOSE+Sophist), ALMate (GenAI, INCOSE), Semios (INCOSE/ISO). Native Polarion AI has INCOSE Content Validation. | Enterprise, quote required. Named/concurrent user licensing. |
| **reqSuite RM** | OSSENO/PeakAvenue | [osseno.com](https://www.osseno.com/en) | **Active** (v4.6, Jul 2025) | General requirements quality. AI-based quality control. No explicit EARS support documented. | Enterprise, quote required. Acquired by PeakAvenue Oct 2025. |
| **reQlab** | (Polarion extension) | [Polarion Extensions](https://extensions.polarion.com/extensions/333-reqlab-ai-powered-requirements-validation-tool-on-premise-gdpr-compliant) | **Active** | EARS, INCOSE, and Sophist sentence template support. On-premise, GDPR compliant. Customizable error classifications. | Commercial Polarion extension. |

---

## Academic / Research Requirements Quality Tools

| Tool | Type | Origin | Status | Notes |
| ------ | ------ | -------- | -------- | ------- |
| **QuARS** (Quality Analyzer for Requirements Specifications) | Research | ISTI-CNR, Italy / CMU SEI | **Unavailable** | NLP-based lexical and syntactic analysis for ambiguity, clarity, understandability. Documented in 2005 SEI report. **No public download** available; contact researchers directly. |
| **QuARS Express** | Research | ISTI-CNR, Italy | **Unavailable** | Enhanced version handling structured requirement documents. Published at NLP4RE 2019. Not publicly downloadable. |
| **RETA** (Requirements Template Analyzer) | Research | Academic | **Unavailable** | Detects vague terms, quantifiers, pronouns, complex requirements, adverbs. Referenced in literature but no public download. |
| **ARM** (Automated Requirements Measurement) | Research | Academic | **Unavailable** | Ambiguity detection tool. Referenced in comparative studies. Not publicly available. |
| **AmbiDetect** | Research | Academic | **Unavailable** | ML-based ambiguous requirement classifier using scikit-learn. Prototype described in papers. |
| **NAI** (Nocuous Ambiguity Identification) | Research | Academic | **Unavailable** | ML-based coordination ambiguity detection. Prototype described in papers. |

---

## General NLP Libraries Used for Requirements Quality

| Library | URL | Language | Notes |
| --------- | ----- | ---------- | ------- |
| **spaCy** | [spacy.io](https://spacy.io/) | Python | Industrial-strength NLP. Most commonly used foundation for custom requirements quality checkers. Actively maintained. |
| **NLTK** | [nltk.org](https://www.nltk.org/) | Python | Classic NLP toolkit. Tokenization, POS tagging, parsing. Good for rule-based requirements analysis. |
| **Hugging Face Transformers** | [huggingface.co](https://huggingface.co/) | Python | Modern transformer models (BERT, SpanBERT) used in recent requirements ambiguity research. |
| **TextBlob** | [PyPI](https://pypi.org/project/textblob/) | Python | Simple NLP API. Sentiment analysis, POS tagging. Lightweight option for basic requirements checks. |

---

## Package Registry Search Results

| Registry | Search Term | Result |
| ---------- | ------------- | -------- |
| **PyPI** | "EARS requirements syntax" | **No dedicated EARS package found.** Only pip requirements.txt parsers returned. |
| **npm** | "EARS requirements syntax" | **No dedicated EARS package found.** General `requirements` package (v2.0.2) exists but is unrelated to EARS. |
| **VS Code Marketplace** | "EARS" | **ears-syntax-vscode** by BlueDotBrigade (v2.2.0, Dec 2023). |

---

## Key Observations

1. **QRA QVscribe is the dominant EARS tool.** It is the only mature,
   actively maintained tool with deep EARS support, integrating with all
   major requirements management platforms (Polarion, DOORS Next, Jama,
   Word, Excel). It is commercial with custom pricing.

2. **Jama Connect Advisor is the second major option**, offering native
   EARS + INCOSE checking within the Jama platform. Also commercial.

3. **No EARS packages exist on PyPI or npm.** The methodology is primarily
   supported through commercial tools or custom implementations built on
   general NLP libraries (spaCy, NLTK).

4. **Open-source EARS tools are nascent.** The most promising are:
   - `adv-ears` (TypeScript, LSP server, actively developed)
   - `ears-lint-go` (Go linter, very new)
   - `earsqa` (browser extension, new)
   - `RequireKit` (EARS + BDD toolkit)
   - `spec-engine` (Claude Code plugin with EARS)

5. **Academic requirements quality tools are largely unavailable.** QuARS,
   RETA, ARM, AmbiDetect, and NAI are described in papers but have no
   public downloads. This is a significant gap in the ecosystem.

6. **IBM is transitioning from RQA to Engineering AI Hub**, moving from
   traditional NLP to generative AI for requirements quality. This signals
   an industry shift toward LLM-based requirements analysis.

7. **The Polarion ecosystem has the richest third-party support** for
   requirements quality, with multiple extensions (QVscribe, reQlab,
   ALMate, Semios) offering EARS and/or INCOSE validation.

8. **EARS is gaining traction in the AI/LLM space.** Several 2025-2026
   projects (spec-engine, LERE, incose-reqts-eval) combine EARS with
   LLMs for requirements engineering, suggesting EARS may become more
   prominent as AI-assisted development grows.

---

## Sources

- [QRA Corp](https://qracorp.com/)
- [QRA QVscribe Features](https://qracorp.com/qvscribe-features/)
- [QRA Product Releases](https://qracorp.com/product-releases/)
- [QRA ReqWriter](https://qracorp.com/reqwriter/)
- [QRA EARS Resources](https://qracorp.com/ears-resources/)
- [Jama Software](https://www.jamasoftware.com/)
- [Jama Connect Advisor EARS FAQ](https://www.jamasoftware.com/requirements-management-guide/writing-requirements/frequently-asked-questions-about-the-ears-notation-and-jama-connect-requirements-advisor/)
- [IBM Engineering Requirements Management](https://www.ibm.com/products/requirements-management)
- [IBM Engineering AI Hub](https://www.ibm.com/docs/en/engineering-ai-hub/1.2.0)
- [IBM RQA Overview](https://www.ibm.com/docs/en/erqa?topic=assistant-overview)
- [Polarion REQUIREMENTS](https://polarion.plm.automation.siemens.com/products/polarion-requirements)
- [QVscribe for Polarion](https://qracorp.com/qvscribe-polarion/)
- [reQlab for Polarion](https://extensions.polarion.com/extensions/333-reqlab-ai-powered-requirements-validation-tool-on-premise-gdpr-compliant)
- [OSSENO reqSuite RM](https://www.osseno.com/en)
- [PeakAvenue + OSSENO acquisition](https://www.peakavenue.com/news-events/news/detail/peakavenue-osseno-strengthening-requirements-management)
- [Alistair Mavin EARS Official Guide](https://alistairmavin.com/ears/)
- [RequireKit](https://github.com/requirekit/require-kit)
- [adv-ears](https://github.com/amir-arad/adv-ears)
- [ears-syntax-vscode](https://github.com/BlueDotBrigade/ears-syntax-vscode)
- [EARS-Rule-Detection](https://github.com/chubozeko/EARS-Rule-Detection)
- [EARS_Checker](https://github.com/bmd6/EARS_Checker)
- [ears-lint-go](https://github.com/labeth/ears-lint-go)
- [earsqa](https://github.com/ammonit-software/earsqa)
- [spec-engine](https://github.com/farshidghyasi/spec-engine)
- [incose-reqts-eval](https://github.com/jethomp3/incose-reqts-eval)
- [LERE](https://github.com/hanhan13579/LERE)
- [template-conformance](https://github.com/armsp/template-conformance)
- [EARS-CTRL](https://github.com/levilucio/EARS-CTRL)
- [requirementchecker.com](https://requirementchecker.com/)
- [QuARS (SEI)](https://www.sei.cmu.edu/library/quars-a-tool-for-analyzing-requirement/)
- [QuARS NLP4RE Paper](https://ceur-ws.org/Vol-2376/NLP4RE19_paper07.pdf)
- [NLP4RE Workshop](https://nlp4re.github.io/2024/)
- [MDPI: Cross-Project EARS Classification](https://www.mdpi.com/2079-8954/13/7/567)
- [Nature: Multi-label Requirement Smells](https://www.nature.com/articles/s41598-025-86673-w)
