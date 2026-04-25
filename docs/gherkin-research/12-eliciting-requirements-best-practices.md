# Best Practices for Eliciting and Specifying Requirements

This document synthesizes industry-standard best practices for requirement
elicitation and specification, grounded in frameworks such as
**ISO/IEC/IEEE 29148**, the **BABOK® Guide v3**, **IREB CPRE**, and the
**Volere Requirements Process**.

---

## 1. From "Gathering" to "Active Elicitation"

Modern requirements engineering distinguishes between passive **gathering** and
active **elicitation**.

- **Passive Gathering:** Treating requirements as pre-existing objects to be
  collected (the analyst as an "order-taker"). This often results in incomplete
  "wish lists" and missed assumptions.
- **Active Elicitation (Recommended):** A proactive discovery process where
  requirements are **drawn out** through dialogue, provocation, and analysis.
  The analyst acts as a facilitator and investigator, probing the "why" to
  uncover hidden needs.

### Collaborative Techniques (BABOK v3)

| Technique | Purpose |
| :--- | :--- |
| **Interviews & Workshops** | Direct dialogue to probe depth and reach consensus. |
| **Observation (Shadowing)** | Identifying "tacit knowledge"—tasks stakeholders do but forget to mention. |
| **Collaborative Games** | Revealing hidden assumptions and encouraging creative thinking. |
| **Prototyping** | Using low-fidelity mockups to trigger immediate stakeholder feedback. |

---

## 2. Characteristics of a "Well-Formed" Requirement (ISO 29148)

For a requirement to be actionable and verifiable, it must possess these nine
characteristics:

1. **Necessary:** Essential to meet the stakeholder's needs; removal causes a
   deficiency.
2. **Appropriate:** At the correct level of abstraction (no design details in
   high-level specs).
3. **Unambiguous:** Can be interpreted in only one way by all readers.
4. **Complete:** Contains all info needed to understand the requirement without
   external explanation.
5. **Singular:** Expresses a single, discrete thought (Atomic).
6. **Feasible:** Can be realized within technical, cost, and schedule
   constraints.
7. **Verifiable:** Can be proven to be met through a finite, cost-effective
   process.
8. **Correct:** Accurately represents the stakeholder's intent.
9. **Conforming:** Follows the project's prescribed style and templates.

---

## 3. Ensuring Testability: The "Fit Criterion"

A requirement is only as good as its verifiability. The **Volere Process**
introduces the **Fit Criterion**—a measurement that determines if a solution
meets the requirement.

- **The Principle:** If you cannot define a measurement (Fit Criterion), the
  requirement is likely ambiguous.
- **IEEE Verification Methods:** Every requirement should be assigned one of
  these methods:
  - **Inspection:** Visual examination of documentation or code.
  - **Analysis:** Using mathematical models or simulations.
  - **Demonstration:** Showing the system performs a task (qualitative).
  - **Test:** Using instrumentation to measure precise performance
    (quantitative).

### The SMART Test for NFRs

Non-Functional Requirements (NFRs) are notoriously vague. Apply the **SMART**
criteria:

- **Specific:** Names a specific behavior or component.
- **Measurable:** Uses metrics (e.g., "99.9% uptime" vs. "high availability").
- **Attainable:** Verification is technically possible.
- **Relevant:** Maps to a business or safety goal.
- **Time-bound:** Specifies *when* or *for how long* the behavior occurs.

---

## 4. Prioritization and Stakeholder Satisfaction (Kano Model)

Not all requirements are equal. The **Kano Model** helps prioritize based on
stakeholder delight:

1. **Must-Be (Basic):** Taken for granted; their absence causes extreme
   dissatisfaction, but their presence doesn't increase satisfaction (e.g., a
   phone making calls).
2. **Performance:** Satisfaction is directly proportional to how well the
   requirement is met (e.g., battery life).
3. **Attractive (Excitement):** Unexpected "delighters" that differentiate the
   product (e.g., advanced AI features).
4. **Indifferent:** Stakeholders don't care; these should be removed to save
   cost.
5. **Reverse:** Features that actually cause dissatisfaction for some users.

---

## 5. Syntactic Standardization

Using a structured template reduces errors by forcing the inclusion of triggers
and constraints.

### The ISO 29148 Template

`[Condition] [Subject] [Action] [Object] [Constraint]`

- *Example:* "When the emergency stop is pressed [Condition], the motor
  [Subject] shall cease [Action] rotation [Object] within 0.5 seconds
  [Constraint]."

### The EARS Patterns

- **Event-Driven:** `WHEN <trigger> THE <system> SHALL <response>`
- **State-Driven:** `WHILE <state> THE <system> SHALL <response>`
- **Unwanted Behavior:** `IF <unwanted condition> THEN THE <system> SHALL
  <response>`

---

## 6. Documentation and Traceability

Requirements must be documented in a way that maintains a "living" connection
to their source.

- **The Rationale (Volere):** Always document the "Why." If the business reason
  disappears, the requirement should be removed.
- **Traceability:** Every requirement must link **backward** to a
  stakeholder/source and **forward** to a test case and implementation
  artifact.
- **Active Validation (IREB):** Requirements are not complete until they have
  been validated against the original stakeholder intent through reviews,
  walkthroughs, or prototypes.

---

## Summary Checklist for well-formed requirements

- [ ] Is it atomic (one requirement per statement)?
- [ ] Does it use a mandatory verb ("shall")?
- [ ] Is there a measurable **Fit Criterion**?
- [ ] Does it avoid subjective adverbs ("fast," "easy," "efficient")?
- [ ] Is the **Rationale** documented?
- [ ] Is it traceable back to a stakeholder or business goal?
