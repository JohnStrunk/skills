# Restricted Natural Language Specification Templates Beyond EARS

A survey of structured/restricted natural language approaches for writing
requirements specifications. EARS is the most widely known, but a rich
ecosystem of alternatives exists, each with different trade-offs.

## Landscape Summary

| Template System | Origin | Year | Domain Focus | Key Idea |
| --- | --- | --- | --- | --- |
| **EARS** | Rolls-Royce / Mavin et al. | 2009 | General (safety-critical) | 5 keyword-driven patterns |
| **Rupp / MASTeR** | SOPHIST GmbH / Chris Rupp | 2007/2014 | General (IREB-aligned) | Typed templates with condition sub-templates |
| **Adv-EARS** | Majumdar et al. | 2011 | Use case derivation | Formal grammar; auto-derives use case diagrams |
| **Boilerplates** | Hull et al. | 2010 | General | Fill-in-the-blank patterns; semantic graphs |
| **Planguage** | Tom Gilb | 1988/2005 | Non-functional / quality | Keyword-driven quantification |
| **SPIDER** | Cheng et al. | 2005 | Formal verification | Structured English to temporal logics |
| **RELAX** | Whittle et al. | 2009/2010 | Self-adaptive systems | Uncertainty operators; fuzzy temporal logic |
| **ACE** | University of Zurich | 1990s+ | Knowledge representation | Controlled natural language to first-order logic |
| **RESPECT** | Model-driven (MDE) | 2025 | General | Template models linked to domain models |
| **Gherkin / BDD** | Cucumber project | 2008+ | Behavior/acceptance testing | Given/When/Then executable specifications |

---

## 1. Rupp's Template / MASTeR (SOPHIST)

**Full name:** Mustergültige Anforderungen -- die SOPHIST Templates für
Requirements ("Exemplary Requirements -- the SOPHIST Templates for
Requirements")

**Origin:** Chris Rupp and die SOPHISTen, SOPHIST GmbH (Nuremberg).
Rupp's original template dates to ~2007; the expanded MASTeR system was
published in 2014. It is the template recommended by **IREB**
(International Requirements Engineering Board) in the CPRE Foundation
Level curriculum.

### Template Types

MASTeR provides **separate templates** for different requirement
categories:

**FunctionalMASTeR** (functional requirements):

```text
[<condition>] <system> <liability> [<activity type>] <process verb> <object>
```

- **Liability** uses modal verbs: SHALL (mandatory), SHOULD (desired),
  WILL (recommendation)
- Example: *"The document editor shall provide the user with the
  ability to create new documents."*

**PropertyMASTeR** (non-functional / quality requirements):

```text
[<condition>] <characteristic> of <subject matter> <liability> [<qualifying expression>] <value>
```

- Example: *"The design of the website should be responsive."*

**EnvironmentMASTeR** (technological environment requirements):

```text
[<condition>] <system> <liability> be designed in a way <environment constraint>
```

- Example: *"The charger shall be designed so the system operates in
  a 100-240V/50-60Hz range."*

**ProcessMASTeR** (process requirements):

```text
[<condition>] <actor> <liability> <process verb> <object>
```

- Example: *"Software developers should work according to the
  Personal Software Process."*

**Condition sub-templates:**

- **ConditionMASTeR** -- general conditional
- **LogicMASTeR** -- logical conditions (IF ... THEN)
- **EventMASTeR** -- event triggers (WHEN)
- **TimeMASTeR** -- temporal conditions (AS SOON AS, AS LONG AS, AFTER)

**Pros:** Comprehensive (covers functional, non-functional, environment,
and process requirements). IREB-aligned and widely taught. Benchmarking
studies rank MASTeR highest overall across quality metrics.

**Cons:** More complex to learn than EARS (multiple template types).
Condition syntax is less prescriptive than EARS keywords. Some research
notes potential for ambiguity due to structural rigidity.

**References:**

- Chris Rupp and die SOPHISTen, *Requirements Templates -- The
  Blueprint of your Requirement*, SOPHIST GmbH, 2014
- [IREB Foundation Level Handbook][ireb-handbook]
- [Fran Caballero's Requirements Generator][fran-gen] (interactive
  tool supporting both MASTeR and EARS)

---

## 2. Adv-EARS (Advanced EARS)

**Origin:** Dipankar Majumdar, Sabnam Sengupta, Ananya Kanjilal, Swapan
Bhattacharya. Published at ACITY 2011 (Springer CCIS vol. 198).

### Concept

Extends EARS with a **formal context-free grammar (CFG)** so that
requirements documents can be parsed and **use case models automatically
derived** from the parse tree.

### Extensions Over EARS

- **Hybrid requirements:** combines event-driven and conditional
  requirements in a single construct, addressing gaps in EARS
- **Formal parse tree:** reveals actors, use cases, and their
  relationships for automated UML diagram generation
- Minor designer intervention needed only to finalize relationships

### Application Example

A case study on an Insurance System demonstrated that Adv-EARS
formatted requirements could be parsed to auto-generate use case
diagrams.

**Pros:** Automated use case derivation from structured requirements.

**Cons:** More formal than EARS (harder for non-specialists). Focused
specifically on deriving use case models, not general specification
quality.

**References:**

- [Springer chapter][adv-ears-springer]
- [ResearchGate PDF][adv-ears-rg]

---

## 3. Boilerplates (Hull et al.)

**Origin:** Hull, Jackson, and Dick, *Requirements Engineering* (2010).
The term "boilerplate" is used broadly in RE to describe any
fixed-format template, but Hull et al. formalized a specific
pattern-based approach.

### How They Work

Boilerplates consist of **fixed syntax elements** with
**fill-in-the-blank attributes** (in angle brackets):

```text
WHEN <trigger> the <system> shall <action> if <assumption>
WHILE <state> the <system> shall <action> if <assumption>
```

Parts of boilerplates can be connected through **relationships**,
forming a "semantic graph" that links related requirements.

### Relationship to EARS

EARS can itself be seen as a specific boilerplate system. Hull's
boilerplates are more general -- they define a library of patterns from
which teams select, rather than prescribing a fixed set of five
patterns.

### Boilerplate Tooling

- **DODT** (Domain Ontology-based requirements Development Tool):
  semi-automatically transforms free-text NL requirements into
  boilerplate format using domain ontologies. Achieved 60% fully
  automatic transformation, with 79.4% best-fitting matches ranked
  correctly.
- Ontology-enhanced boilerplates restrict vocabulary to semantically
  meaningful domain terms, reducing errors.

**Pros:** Flexible (teams define custom libraries for their domain).
Good for inexperienced engineers. Can be combined with ontologies for
vocabulary control.

**Cons:** Less prescriptive than EARS -- quality depends on the library
chosen. No standardized set: teams must curate their own.

**References:**

- Hull, Jackson, Dick, *Requirements Engineering*, Springer, 2010
- [Arora et al., "Requirement Boilerplates" (PDF)][boilerplates-pdf]
- [Ontology + boilerplates tool (Springer 2023)][onto-boilerplates]

---

## 4. Planguage (Tom Gilb)

**Origin:** Tom Gilb, first described ~1988, fully elaborated in
*Competitive Engineering* (Butterworth-Heinemann, 2005).

### Quantification-Driven Design

A **keyword-driven language for quantifying quality requirements**.
Unlike EARS/MASTeR (which template the sentence structure), Planguage
templates the **measurement structure** around a requirement.

### Core Keywords

| Keyword | Purpose | Example |
| --- | --- | --- |
| **Tag** | Unique identifier | `LuggageHandlingSpeed` |
| **Scale** | Unit of measure | Time between bag drop-off and carousel |
| **Goal** | Minimum acceptable level | 95% of bags within 5 minutes |
| **Stretch** | Desirable target beyond Goal | 99% of bags within 3 minutes |
| **Wish** | Ideal outcome | 100% of bags within 2 minutes |
| **Fail** | Unacceptable level | More than 10% exceed 10 minutes |
| **Past** | Current baseline | 85% within 7 minutes (2024 data) |

Additional keywords: **Ambition, Sponsor, Version, Note, Issue, Risk,
Source, Qualifier**

### Qualifier Syntax

Qualifiers add conditions:

```text
WISH [First release, enterprise version]: 1 Dec 2025
PLAN [US market, first 6 months]: Defects Per Million < 1,000
```

### Planguage Industry Adoption

- Over 15,000 engineers at Intel voluntarily adopted Planguage (~2012)
- Can be taught in a few hours
- The **Needs & Means** tool supports Planguage with a reusable
  library of meter specifications and integrates with Gherkin
  Given/When/Then for test parameters

**Pros:** Excellent for non-functional / quality requirements (where
EARS is weakest). Forces quantification. Extensible and customizable.

**Cons:** Not designed for functional requirements (no sentence-level
template). More complex than EARS for simple shall-statements. Less
widely adopted than EARS in safety-critical domains.

**References:**

- Tom Gilb, *Competitive Engineering*, Butterworth-Heinemann, 2005
- [How to Quantify Quality (methodsandtools.com)][gilb-quantify]
- [Planguage guide (malotaux.eu)][planguage-guide]

---

## 5. SPIDER

**Origin:** Betty H.C. Cheng et al., 13th IEEE International Conference
on Requirements Engineering, 2005.

### Natural Language to Formal Logic

Bridges the gap between **informal natural language requirements** and
**formal specifications** (temporal logics). Users write in structured
English; SPIDER automatically maps to specification patterns and
translates to LTL, CTL, or GIL for model checking.

### Structured English Grammar

```text
scope ::= "Globally"
        | "Before " R
        | "After " Q
        | "Between " Q " and " R
        | "After " Q " until " R
```

The grammar supports scoped temporal properties -- the user only works
at the natural language level while the tool handles formal
translation.

**Pros:** Enables formal verification without requiring engineers to
learn temporal logic. Pattern-based (leverages Dwyer et al.'s
specification pattern system).

**Cons:** Benchmarking studies found SPIDER negatively impacts metrics
for unambiguity, completeness, and verifiability. More niche than
EARS. Prototype tool, not widely adopted in industry.

**References:**

- [Cheng et al., "Facilitating the construction of specification
  pattern-based properties" (ResearchGate)][spider-rg]

---

## 6. RELAX

**Origin:** Jon Whittle, Pete Sawyer, Nelly Bencomo, Betty H.C. Cheng,
Jean-Michel Bruel. Published in *Requirements Engineering* journal,
2010.

### Uncertainty-Aware Requirements

A requirements language for **self-adaptive systems** that explicitly
addresses **uncertainty**. Standard SHALL statements assume
deterministic behavior; RELAX allows requirements to be *relaxed*
under adverse conditions.

### Uncertainty Operators

| Operator | Meaning |
| --- | --- |
| `SHALL` | Invariant -- must always hold |
| `EVENTUALLY` | Will hold at some future point |
| `AS EARLY AS POSSIBLE` | Soft temporal bound |
| `AS CLOSE AS POSSIBLE TO <value>` | Soft value bound |
| `AS MANY AS POSSIBLE` | Soft quantity bound |
| `UNTIL <condition>` | Holds until condition changes |
| `BEFORE <event>` | Must hold before event |
| `AFTER <event>` | Must hold after event |

### RELAX Specification Structure

Each RELAX-ed requirement includes structured annotations:

- **ENV** -- environment assumptions
- **MON** -- what the system monitors
- **REL** -- relationships between requirements
- **DEP** -- dependencies

Engineers must explicitly distinguish **invariant** requirements
(always SHALL) from **non-invariant** requirements (can be RELAXed).
The invariants provide a reference point for adaptive behavior.

### RELAX Formal Semantics

RELAX maps to **fuzzy branching temporal logic (FBTL)**, which goes
beyond probabilistic logics by expressing uncertainty about thresholds
themselves.

**Pros:** Only template system designed for self-adaptive systems.
Makes uncertainty explicit. Formally grounded in temporal logic.

**Cons:** Niche (only relevant for adaptive/autonomous systems). More
complex than EARS. Limited industry adoption.

**References:**

- [Whittle et al., *RE* 2010 (Springer)][relax-springer]
- [Original RE'09 paper (PDF)][relax-pdf]

---

## 7. Attempto Controlled English (ACE)

**Origin:** University of Zurich, Attempto project (1990s--present).

### Full Controlled Natural Language

A **full controlled natural language** (not just a template). ACE
defines a precise subset of English with restricted grammar and
unambiguous semantics. Any ACE text can be automatically parsed into
first-order logic (discourse representation structures).

### ACE Syntax Rules

- Every noun requires a determiner: *"A customer inserts a card"*
  (not *"Customers insert cards"*)
- Attachment is verb-first: *"A customer inserts a card with a code"*
  means the code is used for insertion, not that the card has a code
- Coordination: *and* has higher precedence than *or*
- Quantifier scope fixed by word order
- Supports declarative sentences, queries (yes/no and wh-), and
  commands

### ACE Example

```text
A trusted customer inserts two valid cards.
If a card that is expired is inserted then the system rejects the card.
```

### ACE Tooling

- **APE** (Attempto Parsing Engine) -- translates ACE to DRS, OWL,
  SWRL
- **ACE-in-GF** -- implementation in Grammatical Framework

**Pros:** Full language, not just a template. Formally unambiguous
(every sentence has exactly one interpretation). Executable (can be
used for simulation, prototyping, and validation).

**Cons:** Steep learning curve (effectively a new language disguised
as English). Restrictive (many natural English constructions are
invalid). Not widely adopted for industrial requirements engineering.

**References:**

- [ACE Wikipedia][ace-wiki]
- [ACE formal grammar (PDF)][ace-grammar]
- [APE on GitHub][ape-github]

---

## 8. RESPECT (REquirements SPECification using Templates)

**Origin:** Recent work (2025), model-driven engineering approach.

### Model-Driven Templates

Uses **MDE (model-driven engineering)** to model requirements
templates, linking template models to existing **domain models**. This
allows templates to be created, evolved, and verified against the
domain.

**Pros:** Templates are not fixed -- they can evolve with the domain.
Built-in verification against domain models. Addresses the "fixed
format" limitation of other template systems.

**Cons:** Requires MDE infrastructure. Very recent, limited adoption
data.

**References:**

- [Springer 2025][respect-springer]

---

## Comparative Benchmarking

A 2024 study ([Springer][benchmarking]) benchmarked five template
systems head-to-head: **EARS, Adv-EARS, Boilerplates, MASTeR, and
SPIDER**.

### Benchmarking Findings

1. **Templates generally improve quality** compared to free-text
   requirements across multiple metrics
2. **MASTeR leads overall** -- it had solely positive effects across
   the most quality categories, and was the only template with
   positive effects in five specific metrics
3. **No conclusive favorite** -- most effect sizes were relatively
   similar between the top systems
4. **SPIDER showed trade-offs** -- distinctive positive features but
   also negatively impacted unambiguity, completeness, and
   verifiability
5. **EARS** remained strong for ease of learning and practical
   adoption

### Industry Adoption Context

- **79%** of companies use unstructured natural language
- **16%** use structured/restricted natural language (templates)
- **5%** use formal approaches (MBSE)

---

## Template Selection Guide

| If you need... | Consider... |
| --- | --- |
| Easy adoption, general purpose | **EARS** |
| IREB certification alignment, comprehensive typing | **Rupp / MASTeR** |
| Quantified quality requirements | **Planguage** |
| Executable behavior specifications | **Gherkin / BDD** |
| Auto-derivation of use case models | **Adv-EARS** |
| Domain-specific vocabulary control | **Boilerplates + ontologies** |
| Formal verification bridge | **SPIDER** |
| Self-adaptive system uncertainty | **RELAX** |
| Full controlled natural language with logic translation | **ACE** |
| Evolving template systems linked to domain models | **RESPECT** |

<!-- Link references -->

[ireb-handbook]: https://www.gasq.org/files/content/gasq/downloads/certification/IREB/IREB%20FL/cpre_foundationlevel_handbook_en_v1.0.pdf
[fran-gen]: https://francaballero.net/requirements_generator/
[adv-ears-springer]: https://link.springer.com/chapter/10.1007/978-3-642-22555-0_5
[adv-ears-rg]: https://www.researchgate.net/publication/242495580_Adv-EARS_A_Formal_Requirements_Syntax_for_Derivation_of_Use_Case_Models
[boilerplates-pdf]: https://people.svv.lu/sabetzadeh/pub/REPA14.pdf
[onto-boilerplates]: https://link.springer.com/article/10.1007/s10515-023-00403-y
[gilb-quantify]: https://www.methodsandtools.com/archive/archive.php?id=91
[planguage-guide]: https://www.malotaux.eu/?id=planguage
[spider-rg]: https://www.researchgate.net/publication/4186992_Facilitating_the_construction_of_specification_pattern-based_properties
[relax-springer]: https://link.springer.com/article/10.1007/s00766-010-0101-0
[relax-pdf]: https://www.cse.msu.edu/~mckinley/Pubs/files/Whittle.RELAX.2009.pdf
[ace-wiki]: https://en.wikipedia.org/wiki/Attempto_Controlled_English
[ace-grammar]: https://attempto.ifi.uzh.ch/site/pubs/papers/hoefler2004theSyntax.pdf
[ape-github]: https://github.com/Attempto/APE
[respect-springer]: https://link.springer.com/article/10.1007/s10270-025-01265-6
[benchmarking]: https://link.springer.com/article/10.1007/s00766-024-00427-0
