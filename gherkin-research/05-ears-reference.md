# EARS: Easy Approach to Requirements Syntax -- Comprehensive Reference

> **Source:** The authoritative reference for EARS is
> Alistair Mavin's official guide at
> <https://alistairmavin.com/ears/>. The definitions,
> templates, examples, and history in this document are
> drawn from that source and from the original academic
> publications.

**Definition (from
[alistairmavin.com/ears/](https://alistairmavin.com/ears/)):**
*"The Easy Approach to Requirements Syntax (EARS) is a
mechanism to gently constrain textual requirements."*

## Table of Contents

1. [Origins and Background](#1-origins-and-background)
2. [The Problem EARS Solves](#2-the-problem-ears-solves)
3. [Core EARS Templates and Patterns](#3-core-ears-templates-and-patterns)
4. [The General Syntax Rule](#4-the-general-syntax-rule)
5. [Complex Requirements -- Pattern 6](#5-complex-requirements----pattern-6)
6. [Keywords and Their Meanings](#6-keywords-and-their-meanings)
7. [Before and After Examples](#7-before-and-after-examples)
8. [Benefits and Rationale](#8-benefits-and-rationale)
9. [Comparison with Other Approaches](#9-comparison-with-other-approaches)
10. [Industry Adoption](#10-industry-adoption)
11. [Tools and Support](#11-tools-and-support)
12. [Key Publications](#12-key-publications)
13. [Practical Guidance for Applying EARS](#13-practical-guidance-for-applying-ears)

---

## 1. Origins and Background

### Who Created EARS

EARS was created by **Alistair Mavin**,
**Philip Wilkinson**, **Adrian Harwood**, and
**Mark Novak** at **Rolls-Royce PLC** (Aero Engines
division). The methodology emerged from practical work
analyzing jet engine control system certification
requirements -- specifically the airworthiness regulatory
documents governing aero engine control systems.

### When It Was Published

- **2009**: The original paper, *"Easy Approach to
  Requirements Syntax (EARS)"*, was presented at the
  **17th IEEE International Requirements Engineering
  Conference (RE'09)**.
- **2010**: A follow-up paper, *"Big EARS (The Return of
  Easy Approach to Requirements Syntax)"*, was presented
  at the **18th IEEE International Requirements
  Engineering Conference (RE'10)**, extending the
  original work.
- **2019**: A retrospective paper, *"Ten Years of EARS"*,
  was published in **IEEE Software** (vol. 36, no. 5,
  pp. 10-14), reflecting on a decade of adoption and
  evolution.

### How EARS Was Discovered

The creators did not invent EARS from abstract theory.
Developed by Alistair Mavin ("Mav") and colleagues at
Rolls-Royce PLC, EARS emerged while they were analyzing
airworthiness regulations for jet engine control systems.
While analyzing hundreds of requirements in aero engine
certification documents, Mavin observed that
*"requirements all followed a similar structure"* and
that *"requirements were easiest to read when the clauses
always appeared in the same order"*
([alistairmavin.com/ears/](https://alistairmavin.com/ears/)).
EARS codified these observations into a small set of
reusable templates.

---

## 2. The Problem EARS Solves

### Natural Language Requirements Are Inherently Problematic

Stakeholder requirements are typically written in
unconstrained natural language, which introduces
systematic defects. The original EARS paper identified
these recurring problems:

| Problem | Description | Example |
| --- | --- | --- |
| **Ambiguity** | Requirement can be interpreted in multiple ways | "The system should handle errors appropriately" |
| **Vagueness** | Imprecise language that cannot be verified | "The system shall respond quickly" |
| **Incompleteness** | Missing triggers, conditions, or responses | "The system shall disconnect the network" (when?) |
| **Wordiness** | Excessive verbosity obscuring intent | Multi-paragraph requirements burying the actual obligation |
| **Duplication** | Same requirement stated multiple times in different words | Redundant specifications across documents |
| **Inconsistency** | Contradictory requirements or varying styles across authors | Different authors using different conventions |
| **Subjectivity** | Requirements based on opinion rather than measurable criteria | "The interface shall be user-friendly" |
| **Untestability** | Requirements that cannot be verified through testing | "The system shall be reliable" |

### The Cost of These Defects

Requirements defects that escape into design,
implementation, and testing phases are progressively
more expensive to fix. Ambiguous requirements lead to:

- Incorrect implementations
- Rework during integration and testing
- Disputes between stakeholders and development teams
- Missed acceptance criteria
- Schedule and budget overruns

### The Gap EARS Fills

EARS occupies a deliberate middle ground:

- **Unconstrained natural language** is too ambiguous
  and error-prone
- **Formal specification languages** (Z, VDM, Alloy)
  have prohibitively steep learning curves and are
  impractical for most organizations
- **EARS provides structured natural language** -- gentle
  constraints that improve quality while remaining
  accessible to all stakeholders

---

## 3. Core EARS Templates and Patterns

EARS defines **six requirement patterns**, each
identified by a specific keyword (or lack thereof).
Every pattern follows a consistent clause structure.
The first five are the basic patterns; the sixth
(Complex) combines preconditions and triggers. All six
are described on the
[authoritative EARS page](https://alistairmavin.com/ears/).

### Pattern 1: Ubiquitous Requirements

**Definition**: Requirements that state fundamental,
always-active system properties. These have no
preconditions, triggers, or conditions -- they are
unconditionally true at all times.

**Template**:

```text
The <system name> shall <system response>.
```

**Characteristics**:

- No EARS keywords (no While, When, Where, If/Then)
- Always active -- the requirement holds continuously
- Describes inherent properties or constraints

**Ubiquitous Examples**:

- "The mobile phone shall have a mass of less than
  XX grams." *(from
  [alistairmavin.com/ears/](https://alistairmavin.com/ears/))*
- "The mobile phone shall have a mass of less than
  200 grams."
- "The system shall display the current time in
  24-hour format."
- "The software shall be written in Python."
- "The system shall hash all passwords using bcrypt."
- "The control system shall comply with DO-178C
  Level A."

### Pattern 2: Event-Driven Requirements

**Definition**: Requirements that specify system
responses to discrete triggering events. The system
performs an action when something specific happens.

**Template**:

```text
When <trigger>, the <system name> shall <system response>.
```

**Keyword**: **When**

**Characteristics**:

- The trigger is a discrete event (something that
  happens at a point in time)
- The response occurs as a consequence of the trigger
- Distinguishing from state-driven: events are
  instantaneous; states persist over time

**Event-Driven Examples**:

- "When 'mute' is selected, the laptop shall suppress
  all audio output." *(from
  [alistairmavin.com/ears/](https://alistairmavin.com/ears/))*
- "When the user presses the START button, the system
  shall begin recording."
- "When a user submits valid credentials, the system
  shall authenticate and redirect to the dashboard
  within 1 second."
- "When the ignition command is issued, the control
  system shall initiate the ignition sequence."
- "When payment is received, the application shall
  send a confirmation notification."

### Pattern 3: State-Driven Requirements

**Definition**: Requirements that are active only while
the system is in a particular state or condition. The
requirement applies continuously as long as the state
holds.

**Template**:

```text
While <precondition(s)>, the <system name> shall <system response>.
```

**Keyword**: **While**

**Characteristics**:

- The precondition describes a persistent state (not a
  momentary event)
- The requirement is active for the entire duration of
  the state
- Distinguishing from event-driven: states have
  duration; events are instantaneous

**State-Driven Examples**:

- "While there is no card in the ATM, the ATM shall
  display 'insert card to begin'." *(from
  [alistairmavin.com/ears/](https://alistairmavin.com/ears/))*
- "While no card is inserted, the ATM shall display
  'Please insert your card'."
- "While the aircraft is in flight, the control system
  shall maintain fuel flow within specified parameters."
- "While a user session is active, the system shall
  validate the session token on each request."
- "While the system is in standby mode, the display
  shall show the current temperature."
- "While the engine is running, the monitoring system
  shall record vibration levels every
  100 milliseconds."

### Pattern 4: Unwanted Behavior Requirements

**Definition**: Requirements that specify system
responses to undesirable situations -- errors, failures,
faults, or exceptional conditions. These are defensive
requirements.

**Template**:

```text
If <unwanted condition>, then the <system name> shall <system response>.
```

**Keywords**: **If ... then**

**Characteristics**:

- The condition describes something undesirable (error,
  fault, failure, anomaly)
- The response is typically a recovery, mitigation, or
  graceful degradation action
- The "then" distinguishes this from event-driven
  patterns and signals error-handling intent
- This pattern is specifically for **unwanted**
  situations -- not for normal operational conditions

**Unwanted Behavior Examples**:

- "If an invalid credit card number is entered, then
  the website shall display 'please re-enter credit
  card details'." *(from
  [alistairmavin.com/ears/](https://alistairmavin.com/ears/))*
- "If an invalid credit card number is entered, then
  the system shall display an error message."
- "If power fails, then the system shall preserve all
  unwritten data to persistent storage."
- "If the password is entered incorrectly three times,
  then the application shall lock the account for
  30 minutes."
- "If authentication fails, then the system shall
  display 'Invalid email or password'."
- "If airspeed data is unavailable, then the control
  system shall use model-derived airspeed."

### Pattern 5: Optional Feature Requirements

**Definition**: Requirements that apply only when a
particular feature or configuration option is included
in the product. Used for product lines, optional
modules, or configurable systems.

**Template**:

```text
Where <feature is included>, the <system name> shall <system response>.
```

**Keyword**: **Where**

**Characteristics**:

- The feature clause identifies an optional or variant
  capability
- The requirement only applies to configurations that
  include the specified feature
- Useful for product families, configurable platforms,
  and optional modules

**Optional Feature Examples**:

- "Where the car has a sunroof, the car shall have a
  sunroof control panel on the driver door." *(from
  [alistairmavin.com/ears/](https://alistairmavin.com/ears/))*
- "Where a sunroof is fitted, the control panel shall
  include a sunroof open/close switch."
- "Where two-factor authentication is enabled, the
  system shall send a verification code via SMS."
- "Where DisplayPort output is present, the software
  shall allow the user to select a display refresh
  rate."
- "Where overspeed protection is included, the control
  system shall test the validity of the overspeed
  signal."
- "Where the premium package is installed, the system
  shall enable voice-activated controls."

---

## 4. The General Syntax Rule

### The Universal EARS Formula

All EARS requirements follow a single generalized
structure. From
[alistairmavin.com/ears/](https://alistairmavin.com/ears/),
the **generic EARS syntax template** is:

> While \<optional pre-condition\>, when
> \<optional trigger\>, the \<system name\> shall
> \<system response\>

Or equivalently:

```text
While <precondition(s)>, when <trigger>,
the <system name> shall <system response>.
```

Each component has specific cardinality rules
(the **EARS ruleset**):

| Component | Cardinality | Description |
| --- | --- | --- |
| **Precondition(s)** | Zero or many | States that must be true (While clause) |
| **Trigger** | Zero or one | Event that initiates the response (When clause) |
| **System name** | One | The system, subsystem, or component being specified |
| **System response** | One or many | What the system shall do |

The six patterns are specializations of this general
formula with different components present or absent:

| Pattern | Preconditions | Trigger | System | Response |
| --- | :---: | :---: | :---: | :---: |
| Ubiquitous | -- | -- | 1 | 1+ |
| Event-driven | -- | 1 | 1 | 1+ |
| State-driven | 1+ | -- | 1 | 1+ |
| Unwanted behavior | -- | -- | 1 | 1+ |
| Optional feature | -- | -- | 1 | 1+ |
| Complex | 1+ | 1 | 1 | 1+ |

Note: The Unwanted Behavior and Optional Feature
patterns use different keywords (If/Then and Where) but
structurally serve as specializations of the
precondition concept for specific semantic purposes.

### Clause Ordering

EARS enforces a consistent clause order based on
temporal logic:

1. **While** (state/precondition) -- first, because the
   state must exist before anything else
2. **When** (trigger/event) -- second, because the event
   occurs within the state
3. **the \<system name\> shall** -- the obligation
4. **\<system response\>** -- what the system does

This ordering is not arbitrary. It reflects logical
temporal precedence: a state must hold, then an event
occurs within that state, then the system responds.

---

## 5. Complex Requirements -- Pattern 6

### Pattern 6: Complex (While ... When)

**Definition**: The sixth EARS pattern combines
state-driven preconditions with event-driven triggers.
It is formally listed as one of the six EARS patterns
on the
[authoritative EARS page](https://alistairmavin.com/ears/).

**Template**:

```text
While <precondition(s)>, when <trigger>,
the <system name> shall <system response>.
```

**Complex Pattern Examples**:

- "While the aircraft is on ground, when reverse thrust
  is commanded, the engine control system shall enable
  reverse thrust." *(from
  [alistairmavin.com/ears/](https://alistairmavin.com/ears/))*
- "While the aircraft is on the ground and reverse
  thrust is commanded, when wheel speed exceeds
  50 knots, the engine control system shall enable
  reverse thrust deployment."
- "While the system is in maintenance mode, when a
  diagnostic command is received, the controller shall
  execute the self-test sequence."
- "While the user is logged in, when the session has
  been idle for 15 minutes, the application shall
  display a timeout warning."

### Further Complex Combinations

### Optional Feature + Event

**Template**:

```text
Where <feature is included>, when <trigger>,
the <system name> shall <system response>.
```

**Example**:

- "Where cruise control is fitted, when the vehicle
  speed drops below the set speed by more than 5 mph,
  the system shall increase throttle to restore set
  speed."

### Optional Feature + State

**Template**:

```text
Where <feature is included>,
while <precondition(s)>,
the <system name> shall <system response>.
```

**Example**:

- "Where the heated seats option is installed, while
  the cabin temperature is below 10 degrees Celsius,
  the seat heater shall activate automatically."

### Optional Feature + State + Event

**Template**:

```text
Where <feature is included>,
while <precondition(s)>, when <trigger>,
the <system name> shall <system response>.
```

**Example**:

- "Where the advanced driver assistance package is
  included, while the vehicle is traveling above
  30 mph, when a forward collision is detected, the
  braking system shall apply emergency braking."

### Event + Unwanted Behavior

**Template**:

```text
When <trigger>, if <unwanted condition>,
then the <system name> shall <system response>.
```

**Example**:

- "When the user submits an order, if payment
  validation fails, then the system shall notify the
  customer and discard the incomplete order."
- "When reverse gear is selected, if the gear does not
  engage within 2 seconds, then the transmission
  controller shall display a gear fault notification."

### Guidelines for Complex Requirements

- Combine patterns only when the requirement genuinely
  involves multiple conditions
- If a complex requirement becomes difficult to read,
  consider decomposing it into simpler requirements
- Maintain the canonical clause order: Where, While,
  When, If/Then, shall
- Each complex requirement should still describe a
  single, coherent system behavior

---

## 6. Keywords and Their Meanings

### EARS Structural Keywords

| Keyword | Pattern | Meaning |
| --- | --- | --- |
| **While** | State-driven | Introduces a persistent precondition/state |
| **When** | Event-driven | Introduces a discrete triggering event |
| **Where** | Optional feature | Introduces a feature/configuration condition |
| **If ... then** | Unwanted behavior | Introduces an undesirable condition and its recovery |
| **shall** | All patterns | Denotes a mandatory obligation |

### Obligation Keywords (Requirement Strength)

EARS uses **"shall"** as its primary obligation keyword,
consistent with established standards (IEEE 830,
ISO/IEC/IEEE 29148, RFC 2119). The distinction between
obligation levels is critical:

| Keyword | Obligation Level | Meaning |
| --- | --- | --- |
| **shall** | Mandatory | An absolute requirement -- the system MUST comply. This is the standard EARS keyword. |
| **should** | Advisory / Recommended | Strongly recommended but not mandatory. There may be valid reasons to deviate, but the implications must be understood. |
| **may** | Optional / Permissive | Truly optional. The system is permitted but not required to do this. |
| **will** | Statement of intent / Future | Often used for declarations of purpose or design intent rather than verifiable requirements. Not recommended in EARS. |

### EARS Best Practice for Keywords

- **Always use "shall"** for requirements -- it signals
  a testable, mandatory obligation
- **Avoid "should" and "may"** in requirements -- they
  create ambiguity about whether the system must
  actually comply
- **Avoid "will"** -- it is often confused with "shall"
  but typically indicates a statement of fact or intent,
  not a verifiable requirement
- **Avoid negative requirements** where possible (e.g.,
  "shall not") -- they are harder to test. Reframe as
  positive obligations when feasible
- **One "shall" per requirement** -- if a requirement
  contains multiple "shall" clauses, it likely needs
  to be decomposed into separate requirements

### Words to Avoid in EARS Requirements

| Word/Phrase | Problem | Alternative |
| --- | --- | --- |
| "quickly", "fast" | Vague, unmeasurable | Specify a time (e.g., "within 2 seconds") |
| "efficiently" | Subjective | Define measurable efficiency criteria |
| "user-friendly" | Subjective, untestable | Specify concrete usability criteria |
| "appropriate", "suitable" | Ambiguous | State the specific criteria |
| "etc.", "and so on" | Incomplete | List all items explicitly |
| "preferably" | Unclear obligation | Use "shall" or remove |
| "convenient" | Subjective | Define specific conditions |
| "easy to use" | Subjective | Specify measurable usability requirements |
| "handle" | Vague action | Specify the exact behavior |
| "support" | Vague action | Specify what the system does |
| "minimize", "maximize" | Unbounded | Specify quantified limits |

---

## 7. Before and After Examples

### Example 1: Network Disconnection

**Before (vague)**:
> "The system shall break network connection."

**Problems**: No trigger specified. When should this
happen? Under what conditions? What type of connection?

**After (EARS -- Event-driven)**:
> "When the disconnect button is pressed, the software
> shall terminate the active network connection."

---

### Example 2: Order Processing

**Before (vague)**:
> "The system should process orders efficiently and
> handle failures properly."

**Problems**: "Efficiently" is unmeasurable. "Handle
failures properly" is vague. Two behaviors conflated.
Uses "should" instead of "shall".

**After (EARS -- decomposed into Event-driven +
Unwanted behavior)**:
> "When a customer submits an order, the system shall
> validate the payment information and store the order
> record within 3 seconds."
>
> "If payment validation fails, then the system shall
> notify the customer with the reason for failure and
> discard the incomplete order."

---

### Example 3: Phone Weight

**Before (vague)**:
> "The phone should be lightweight."

**Problems**: "Lightweight" is subjective and
unmeasurable. Uses "should" instead of "shall".

**After (EARS -- Ubiquitous)**:
> "The mobile phone shall have a mass of less than
> 200 grams."

---

### Example 4: ATM Display

**Before (vague)**:
> "The ATM should show a welcome screen when it's not
> being used."

**Problems**: "Not being used" is imprecise. "Should"
instead of "shall". "Welcome screen" is vague.

**After (EARS -- State-driven)**:
> "While no card is inserted, the ATM shall display
> the message 'Please insert your card'."

---

### Example 5: Audio Muting

**Before (vague)**:
> "The laptop must be able to mute sounds."

**Problems**: No trigger specified. "Must be able to"
is weaker than "shall". What sounds? All audio?

**After (EARS -- Event-driven)**:
> "When the mute button is selected, the laptop shall
> suppress all audio output."

---

### Example 6: Error Handling

**Before (vague)**:
> "The system should handle invalid credit card
> numbers appropriately."

**Problems**: "Appropriately" is undefined. "Should"
instead of "shall". No specific response.

**After (EARS -- Unwanted behavior)**:
> "If an invalid credit card number is entered, then
> the payment system shall display the message 'Invalid
> card number. Please re-enter your card details.'"

---

### Example 7: Auto-Save Feature

**Before (vague)**:
> "The application should auto-save user work."

**Problems**: No trigger or timing. "Should" instead of
"shall". What constitutes "user work"?

**After (EARS -- Event-driven)**:
> "When the user has not typed for 5 seconds, the
> editor shall automatically save the current document
> content to drafts."

---

### Example 8: Optional Feature

**Before (vague)**:
> "If the car has a sunroof, there should be a button
> for it."

**Problems**: Informal language. "Should" instead of
"shall". Imprecise about location and function.

**After (EARS -- Optional feature)**:
> "Where a sunroof is fitted, the vehicle control panel
> shall include a sunroof open/close switch on the
> overhead console."

---

### Example 9: Complex Multi-Condition

**Before (vague)**:
> "The engine should use reverse thrust when landing."

**Problems**: Oversimplified. Missing safety conditions.
"Should" instead of "shall". "When landing" is
imprecise.

**After (EARS -- Complex: State + Event)**:
> "While the aircraft is on the ground and ground speed
> exceeds 60 knots, when the thrust reverser deploy
> command is issued, the engine control system shall
> enable reverse thrust within 0.5 seconds."

---

### Example 10: Permission Management

**Before (vague)**:
> "Only admins should be able to delete things."

**Problems**: Informal. "Things" is vague. No specified
behavior for non-admins.

**After (EARS -- Event-driven + Unwanted behavior)**:
> "When a user with the administrator role initiates a
> deletion request, the system shall delete the
> specified resource and log the action."
>
> "If a user without the administrator role attempts a
> deletion, then the system shall reject the request
> and display 'Insufficient permissions: administrator
> role required'."

---

## 8. Benefits and Rationale

### Key Advantages

From
[alistairmavin.com/ears/](https://alistairmavin.com/ears/),
the authoritative EARS source highlights these key
advantages:

- **Reduces common problems** in natural language
  requirements
- **Effective for non-native English speakers**
- **Lightweight** with little training overhead
- **No specialist tool needed**
- **Easy to read**

### Why EARS Improves Requirements Quality

EARS delivers measurable improvements across multiple
dimensions:

#### 1. Eliminates Common Defects

By providing structured templates, EARS prevents the
most frequent natural language requirement defects --
ambiguity, vagueness, incompleteness, and
untestability -- at the point of authoring rather than
during review.

#### 2. Enforces Consistency

Regardless of who writes the requirement, EARS produces
a uniform style. This eliminates presentation bias
(where reviewers unconsciously judge requirements
quality by writing style rather than content) and makes
documents coherent across multiple authors.

#### 3. Minimal Training Overhead

EARS can be learned and applied within a half-day
training session. Authors report immediate improvement
in their first draft quality. The notation is described
as "lightweight" -- it requires no specialized tools,
formal methods training, or mathematical notation.

#### 4. Improves First Drafts

Requirements written with EARS approach finished quality
faster. The templates guide authors to include necessary
information (triggers, conditions, states) on the first
attempt, reducing review-rework cycles.

#### 5. Exposes Missing Information

If an author cannot write a requirement in EARS format,
it typically means they do not yet understand the
requirement well enough. As Mavin states: *"If you can't
write it in EARS, then you don't understand it."* This
makes gaps in understanding immediately visible.

#### 6. Cognitive Offloading

EARS separates syntax concerns from semantic concerns.
By providing a fixed syntactic structure, authors can
focus their cognitive effort on the **meaning** of the
requirement (what the system should do) rather than on
**how to express it** (sentence structure and word
choice).

#### 7. Complements Visual Models

EARS requirements map naturally to activity diagrams and
state charts. State-driven requirements correspond to
states in a state machine; event-driven requirements
correspond to transitions. This creates a natural bridge
between textual specifications and model-based
approaches.

#### 8. Works for Non-Native English Speakers

The constrained, template-based approach is particularly
valuable for international teams where requirements
authors may not be native English speakers. The
templates reduce the linguistic skill required to
produce clear, precise requirements.

#### 9. Improves Team Communication

Consistent requirement format improves communication
between teams (requirements authors, designers,
developers, testers). Everyone knows where to find the
trigger, the condition, and the expected behavior.

#### 10. Enhances Testability

Each EARS requirement has clear, verifiable conditions
and expected outcomes, making it straightforward to
derive test cases. The structured format directly
supports verification and validation activities.

### Quantitative Evidence

The original case study at Rolls-Royce demonstrated
both qualitative and quantitative improvements when EARS
was applied to aero engine control system certification
requirements. The authors found that:

- The templates addressed approximately **95% of
  typical requirement types** in industrial practice
- **Defect reduction correlated directly** with
  template adherence
- Requirements engineers reported **improved
  confidence** in specification completeness
- Development teams found **clearer acceptance
  criteria**
- **Reduced requirement-related rework** during testing
  phases

---

## 9. Comparison with Other Approaches

### EARS vs. Unconstrained Natural Language

| Dimension | Natural Language | EARS |
| --- | --- | --- |
| Accessibility | Very high | High |
| Ambiguity | High risk | Low risk |
| Consistency | Author-dependent | Template-enforced |
| Training needed | None | Half day |
| Tool requirements | None | None |
| Testability | Variable | Consistently high |

### EARS vs. Formal Methods (Z, VDM, Alloy)

| Dimension | Formal Methods | EARS |
| --- | --- | --- |
| Mathematical rigor | Very high | Low |
| Ambiguity | Eliminated | Greatly reduced |
| Learning curve | Very steep | Gentle |
| Stakeholder readability | Low (requires expertise) | High (natural language) |
| Tool requirements | Specialized tools | None |
| Industry adoption | Limited | Widespread |
| Completeness checking | Automated | Manual (aided by structure) |

### EARS vs. User Stories (As a... I want... So that...)

| Dimension | User Stories | EARS |
| --- | --- | --- |
| Focus | User goals and value | System behavior and obligations |
| Abstraction level | High (intent) | Specific (implementation-guiding) |
| Error handling | Rarely specified | Explicit (If/Then pattern) |
| Testability | Requires acceptance criteria | Built into structure |
| Typical domain | Agile software | Systems engineering, safety-critical |
| Specification completeness | Intentionally incomplete | Comprehensive |

### EARS vs. Use Cases

| Dimension | Use Cases | EARS |
| --- | --- | --- |
| Granularity | Scenario-level (multi-step) | Individual requirement-level |
| Format | Narrative/tabular flows | Single sentence |
| Scope | Actor-system interactions | System obligations |
| Error handling | Alternative/exception flows | Separate If/Then requirements |
| Traceability | Coarse-grained | Fine-grained |

### EARS vs. Rupp Template (Boilerplate)

The Rupp template (developed by Chris Rupp /
SOPHIST Group) is another structured natural language
approach for requirements. It uses a similar sentence
template:

```text
[Condition] The <system> shall/should/will
<action> [object] [constraint].
```

| Dimension | Rupp Template | EARS |
| --- | --- | --- |
| Keyword usage | Optional condition clause | Specific keywords (While/When/Where/If-Then) |
| Pattern differentiation | Single template with variants | Five distinct patterns |
| Semantic clarity | Condition type not explicit | Keywords explicitly convey condition type |
| Error handling | Not distinguished | Dedicated If/Then pattern |
| Optional features | Not distinguished | Dedicated Where pattern |

EARS provides finer semantic differentiation through its
keyword system -- a "While" clause means something
fundamentally different from a "When" clause, and the
reader knows this immediately.

### EARS vs. Planguage (Tom Gilb)

Planguage is a structured specification language
emphasizing quantification and metrics.

| Dimension | Planguage | EARS |
| --- | --- | --- |
| Focus | Quantified quality requirements | Behavioral requirements |
| Format | Keyword-tagged blocks | Single sentences |
| Quantification | Central (Scale, Meter, Goal, Stretch) | Author's responsibility |
| Learning curve | Moderate | Gentle |
| Best for | Non-functional/quality requirements | Functional/behavioral requirements |
| Complementary? | Yes -- they address different needs | Yes |

EARS and Planguage are more complementary than
competing. EARS excels at behavioral/functional
requirements while Planguage excels at quantified
quality/non-functional requirements.

### EARS vs. MASTER Template

The MASTER template is another semi-formal requirements
syntax. Comparative studies (e.g., RE'23 workshop
papers) have evaluated EARS, MASTER, and
ISO/IEC/IEEE 29148 templates:

- All semi-formal approaches significantly outperform
  unconstrained natural language
- EARS has the widest industrial adoption
- EARS requires the least training overhead
- MASTER provides more detailed structural decomposition
  but at higher complexity cost

### Summary Position

EARS is classified as a **semi-formal specification
method** -- it sits between unconstrained natural
language (informal) and mathematical specification
languages (fully formal). Multiple academic studies have
described it as *"the most used semi-formal
specification method"* for functional requirements.

---

## 10. Industry Adoption

### Organizations Using EARS

EARS has been adopted across a wide range of industries
and organizations:

| Organization | Industry | Notes |
| --- | --- | --- |
| **Rolls-Royce** | Aerospace / Defense | Created EARS; used for aero engine control systems |
| **Airbus** | Aerospace | Aircraft systems requirements |
| **NASA** | Space / Aerospace | Space systems requirements |
| **Intel** | Semiconductor / Computing | Hardware/software requirements |
| **Bosch** | Automotive / Industrial | Automotive systems |
| **Daimler** | Automotive | Vehicle systems |
| **Dyson** | Consumer Electronics | Product requirements |
| **Honeywell** | Aerospace / Industrial | Avionics and control systems |
| **Siemens** | Industrial / Healthcare | Multi-domain systems engineering |

### Academic Adoption

EARS is taught at universities in **China, France,
Germany, Sweden, the UK, and the USA** as part of
requirements engineering and systems engineering
curricula
([alistairmavin.com/ears/](https://alistairmavin.com/ears/)).
It is referenced in standards-related discussions and
INCOSE (International Council on Systems Engineering)
communities.

### Domain Coverage

EARS has proven effective across:

- **Aerospace and defense** (its origin domain)
- **Automotive** (ADAS, powertrain, vehicle systems)
- **Consumer electronics**
- **Industrial control systems**
- **Medical devices**
- **Software systems**
- **Semiconductor design**

The methodology's domain independence is a key
strength -- the templates apply regardless of whether
the system is a jet engine, a mobile phone, or a web
application.

---

## 11. Tools and Support

### Dedicated Tools

| Tool | Description |
| --- | --- |
| **QRA Corp EARS tools** | Requirements quality checking with EARS compliance validation; includes automated EARS usage assessment and integrated advisor functionality |
| **Jama Connect** | Requirements management platform with EARS notation support and compliance checking |
| **EARS Requirements Checker** (requirementchecker.com) | Dedicated web tool for analyzing and validating requirements against EARS patterns; supports Excel export |
| **RequireKit** | Requirements tool with built-in EARS notation pattern support |

### No Tool Required

A critical advantage of EARS is that it **requires no
specialized tool**. The templates can be applied using:

- Any text editor
- Spreadsheets (Excel, Google Sheets)
- Word processors
- Existing requirements management tools (DOORS,
  Polarion, Jama, etc.)
- Wiki systems

The tool-independence of EARS is a deliberate design
choice that lowers the adoption barrier.

### NLP and Automation Research

Academic research has explored automated EARS pattern
detection and classification:

- **EARS Rule Detection** (University of Oulu):
  NLP-based project for automatically classifying
  requirements into EARS categories
- **Automated EARS-Based Requirements Generation**:
  Research into generating EARS-format requirements
  from natural language descriptions
- **Cross-Project Multiclass Classification**: Machine
  learning approaches for classifying functional
  requirements into the five EARS classes

---

## 12. Key Publications

### Primary References

1. **Mavin, A., Wilkinson, P., Harwood, A., &
   Novak, M.** (2009). "Easy Approach to Requirements
   Syntax (EARS)." *Proceedings of the 17th IEEE
   International Requirements Engineering Conference
   (RE'09)*. IEEE.
   - The foundational paper introducing EARS with the
     five templates
   - Includes the Rolls-Royce aero engine case study
   - Cited by 490+ scholarly works

2. **Mavin, A. & Wilkinson, P.** (2010). "Big EARS
   (The Return of Easy Approach to Requirements
   Syntax)." *Proceedings of the 18th IEEE
   International Requirements Engineering Conference
   (RE'10)*. IEEE.
   - Extended the original work with additional
     patterns and guidance
   - Addressed complex requirement combinations

3. **Mavin, A. & Wilkinson, P.** (2019). "Ten Years
   of EARS." *IEEE Software*, 36(5), 10-14.
   - Retrospective on a decade of EARS adoption
   - Discusses evolution, lessons learned, and
     industry adoption

### Related Academic Work

1. **Cross-Project Multiclass Classification of
   EARS-Based Functional Requirements.** *Systems*
   journal, 13(7), 567. MDPI.
   - Treats EARS as "the most used semi-formal
     specification method"
   - Machine learning classification of requirements
     into five EARS classes

2. **Learning Software Requirements Syntax: An
   Unsupervised Approach.** *Knowledge-Based Systems*.
   Elsevier.
   - Compares requirements templates including EARS,
     Rupp, and User Stories

3. **A Comparative Evaluation of Requirement Template
   Systems.** *RE'23 Workshop*. University of Koblenz.
   - Compares EARS, MASTER, and ISO/IEC/IEEE 29148
     templates

### Tutorial and Practitioner Resources

1. **Terzakis, J.** (2013). "EARS: Easy Approach to
   Requirements Syntax." Tutorial at *ICCGI 2013*
   (IARIA Conference).
   - Comprehensive tutorial presentation covering all
     EARS patterns

2. **Alistair Mavin's EARS Guide**:
   [alistairmavin.com/ears/](https://alistairmavin.com/ears/)
   - The official practitioner guide maintained by
     EARS' creator

3. **QRA Corp**: "The Easy Approach to Requirements
   Syntax: The Definitive Guide" (PDF)
   - Comprehensive practitioner guide with
     fill-in-the-blank templates

---

## 13. Practical Guidance for Applying EARS

### Step-by-Step Process for Writing EARS Requirements

**Step 1: Identify the requirement type.** Ask yourself:

- Is this always true? -> **Ubiquitous**
- Does the system respond to an event? ->
  **Event-driven**
- Is the requirement active during a particular state?
  -> **State-driven**
- Does this handle an error, fault, or failure? ->
  **Unwanted behavior**
- Does this apply only when a feature is included? ->
  **Optional feature**
- Does it combine conditions? -> **Complex**

**Step 2: Apply the appropriate template.** Fill in the
placeholders with specific, measurable content.

**Step 3: Validate the requirement.** Check:

- Does it contain exactly one "shall"?
- Is the system name explicit?
- Is the response measurable and testable?
- Are all conditions and triggers specific (not vague)?
- Can a tester write a test case from this requirement
  alone?

### Decision Tree for Selecting Patterns

```text
Is the requirement always active (no conditions)?
  YES -> Ubiquitous:
         "The <system> shall <response>"
  NO  -> Does it respond to a specific event?
           YES -> Is there also a state precondition?
                    YES -> Complex:
                           "While <state>,
                            when <event>,
                            the <system>
                            shall <response>"
                    NO  -> Event-driven:
                           "When <event>,
                            the <system>
                            shall <response>"
           NO  -> Is it active during a state?
                    YES -> State-driven:
                           "While <state>,
                            the <system>
                            shall <response>"
                    NO  -> Does it handle an error?
                             YES -> Unwanted behavior:
                                    "If <condition>,
                                     then the <system>
                                     shall <response>"
                             NO  -> Is a feature present?
                                      YES -> Optional:
                                             "Where <feature>,
                                              the <system>
                                              shall <response>"
                                      NO  -> Reconsider:
                                             likely Ubiquitous
                                             or needs
                                             decomposition
```

### Common Mistakes and How to Avoid Them

| Mistake | Problem | Fix |
| --- | --- | --- |
| Multiple "shall" in one requirement | Requirement conflates multiple obligations | Split into separate requirements |
| Using "When" for a state | Confusing events with states | Use "While" for persistent conditions |
| Using "While" for an event | Confusing states with events | Use "When" for discrete triggers |
| Vague response | "Handle the error" is not testable | Specify the exact system behavior |
| Missing system name | Unclear who/what performs the action | Always name the system explicitly |
| Using "should" instead of "shall" | Ambiguous obligation level | Use "shall" for mandatory requirements |
| Using If/Then for normal behavior | If/Then is reserved for unwanted situations | Use When for normal event triggers |
| Implementation details in the response | Specifying how instead of what | Focus on observable behavior, not internal design |

### Tips for EARS Adoption

1. **Start small**: Apply EARS to a subset of
   requirements first. Demonstrate improvement before
   rolling out broadly.
2. **Train by example**: Show before/after
   transformations to illustrate the value.
3. **Use EARS for reviews**: Even if existing
   requirements were not written in EARS format, use
   EARS patterns as a review checklist to identify
   defects.
4. **Combine with other practices**: EARS addresses
   syntax; you still need good requirements
   elicitation, stakeholder management, and
   traceability practices.
5. **Don't force complex patterns**: If a requirement
   naturally fits a simple pattern, keep it simple.
   Complexity should reflect genuine requirement
   complexity, not artificial sophistication.
6. **Iterate**: First drafts may not be perfect. Use
   EARS as a tool for progressive refinement.
7. **Accept that EARS is a "gentle constraint"**: It is
   deliberately not as rigid as formal methods. Some
   judgment is still required.

### Quick Reference Card

```text
UBIQUITOUS:    The <system> shall <response>.
EVENT-DRIVEN:  When <trigger>,
               the <system> shall <response>.
STATE-DRIVEN:  While <state>,
               the <system> shall <response>.
UNWANTED:      If <condition>,
               then the <system> shall <response>.
OPTIONAL:      Where <feature>,
               the <system> shall <response>.
COMPLEX:       While <state>, when <trigger>,
               the <system> shall <response>.
```

---

## Summary

EARS -- *"a mechanism to gently constrain textual
requirements"*
([alistairmavin.com/ears/](https://alistairmavin.com/ears/))
-- is a lightweight, practical, and widely adopted
methodology for writing high-quality natural language
requirements. Developed by Alistair Mavin ("Mav") and
colleagues at Rolls-Royce PLC while analyzing
airworthiness regulations for jet engine control
systems, and first published in 2009, it provides six
templates that address the most common defects in
unconstrained natural language requirements. Its key
strengths are: minimal training overhead, no tool
dependency, applicability across domains, effectiveness
for non-native English speakers, and a proven track
record in safety-critical industries including
aerospace, automotive, and defense. EARS is used by
organizations including Airbus, Bosch, Dyson, Honeywell,
Intel, NASA, Rolls-Royce, and Siemens, and is taught at
universities in China, France, Germany, Sweden, the UK,
and the USA.

The core insight of EARS is that a small number of
keywords (While, When, Where, If/Then) combined with a
consistent clause ordering can dramatically improve
requirements quality while keeping requirements readable
by all stakeholders. It does not replace requirements
engineering expertise -- it amplifies it by providing a
reliable syntactic framework that lets authors focus on
getting the content right.
