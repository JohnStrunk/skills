# Requirements Quality — Elicitation and Validation Reference

This document provides guidance for translating user prose into well-formed,
testable EARS requirements. Consult this when eliciting requirements from
users and validating the quality of formulated requirements.

---

## Active Elicitation

Requirements do not pre-exist as fully formed statements — they must be
drawn out through dialogue. When the user describes a feature or behavior:

1. **Probe the "why."** Understanding the business goal helps formulate the
   right requirement, not just the stated one.
2. **Identify tacit assumptions.** Users often omit things they consider
   obvious. Ask about error cases, edge conditions, and non-functional
   expectations.
3. **Challenge vagueness.** If the user says "fast," "easy," or "secure,"
   ask for measurable criteria. What response time? What does "easy" mean
   concretely? What security standard?

---

## Characteristics of a Well-Formed Requirement

Every EARS requirement should satisfy these nine properties (derived from
ISO/IEC/IEEE 29148):

| Property | Description | Test |
| :--- | :--- | :--- |
| **Necessary** | Essential to the stakeholder's needs | Would removing it cause a deficiency? |
| **Appropriate** | At the right abstraction level | No design details in a high-level spec |
| **Unambiguous** | Only one interpretation possible | Could two readers disagree on meaning? |
| **Complete** | Contains all info needed to understand it | Needs no external explanation |
| **Singular** | Expresses one discrete obligation | Contains exactly one "shall" |
| **Feasible** | Can be realized within constraints | Is it technically achievable? |
| **Verifiable** | Can be proven through testing | Can you write a pass/fail test? |
| **Correct** | Accurately represents stakeholder intent | Does the user agree this is what they meant? |
| **Conforming** | Follows EARS templates | Uses the correct pattern and keywords |

---

## The Testability Principle

A requirement is only as good as its verifiability. For every requirement,
you should be able to define a **fit criterion** — a measurement that
determines whether the solution meets the requirement.

**If you cannot define how to test it, the requirement is ambiguous.**

### Verification Methods

| Method | Description | When to Use |
| :--- | :--- | :--- |
| **Test** | Instrumented measurement against a threshold | Performance, timing, capacity |
| **Demonstration** | Show the system performs the behavior | Functional behavior, UI |
| **Inspection** | Visual examination of artifacts | Compliance, documentation |
| **Analysis** | Mathematical models or simulations | Safety, reliability |

### SMART Criteria for NFRs

Non-functional requirements are prone to vagueness. Apply:

- **S**pecific: Names a specific behavior or component
- **M**easurable: Uses metrics (e.g., "99.9% uptime" not "high availability")
- **A**ttainable: Verification is technically possible
- **R**elevant: Maps to a business or safety goal
- **T**ime-bound: Specifies when or for how long

---

## Elicitation Questions by Requirement Type

When the user describes a feature, ask targeted questions to determine the
EARS pattern and fill in the template:

### For Ubiquitous Requirements

- "Is this always true, regardless of system state?"
- "Are there any conditions where this would NOT apply?"
- "What is the measurable threshold?"

### For Event-Driven Requirements

- "What specific action or event triggers this behavior?"
- "What exactly should the system do in response?"
- "Is there a time constraint on the response?"
- "What happens if the trigger occurs multiple times rapidly?"

### For State-Driven Requirements

- "How long does this condition persist?"
- "What causes the system to enter this state?"
- "What causes the system to leave this state?"
- "What should happen when the state ends?"

### For Unwanted Behavior Requirements

- "What could go wrong?"
- "What should the system do when this error occurs?"
- "How does the system recover to normal operation?"
- "Should the error be logged, and should anyone be notified?"

### For Optional Feature Requirements

- "Is this always present, or only in certain configurations?"
- "What happens in systems where this feature is NOT included?"
- "How is the feature enabled or disabled?"

### For Complex Requirements

- "Is this behavior conditional on both a state AND an event?"
- "Are there multiple conditions that must all be true?"
- "Can this be simplified into separate requirements?"

---

## Decomposition Strategy

When user prose contains multiple behaviors, decompose into atomic
requirements:

1. **Identify the distinct behaviors.** Look for "and," "or," and semicolons
   separating different obligations.
2. **Separate normal from error paths.** The happy path uses Event-Driven
   (`When`); error handling uses Unwanted Behavior (`If/Then`).
3. **Separate distinct triggers.** Different events producing different
   responses become separate requirements.
4. **Separate distinct states.** Behavior that varies by state gets one
   requirement per state.
5. **Extract optional features.** Feature-dependent behavior goes into
   `Where`-based requirements.
6. **Verify independence.** Each decomposed requirement should be
   independently testable.

---

## Common User Phrases and Their EARS Translations

| User says | Likely pattern | Clarify |
| :--- | :--- | :--- |
| "It should always..." | Ubiquitous | Confirm no conditions apply |
| "When the user clicks..." | Event-Driven | Ask about error cases |
| "During maintenance..." | State-Driven | Ask what defines entry/exit |
| "If something goes wrong..." | Unwanted Behavior | Ask for specific failure modes |
| "For premium users..." | Optional Feature | Ask how feature is enabled |
| "It needs to be fast" | Ubiquitous or Event-Driven | Ask for a number |
| "Handle errors properly" | Unwanted Behavior | Ask for each error case |
| "Make it secure" | Multiple patterns | Ask which threats to address |
| "Only admins can..." | Event-Driven + Unwanted | Decompose into allowed + denied |
| "The system should support..." | Ambiguous | Ask what "support" means concretely |

---

## Validating Against the User's Intent

After formulating EARS requirements, always present them to the user for
confirmation:

1. **Read back the requirements** in plain language to verify they capture
   the user's intent.
2. **Highlight any assumptions** you made during formulation.
3. **Ask about gaps:** "Are there error conditions I haven't covered?" "Are
   there other states or modes where this behaves differently?"
4. **Confirm measurable values** are acceptable: "Is 200ms an appropriate
   response time target?"

The goal is not just syntactic correctness — it's ensuring the requirement
accurately represents what the user actually needs.
