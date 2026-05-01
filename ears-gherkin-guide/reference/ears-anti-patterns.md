# EARS Anti-Patterns — Detailed Reference

This document catalogs common mistakes when writing EARS requirements, with
examples showing the problem and the corrected form. Consult this when
reviewing or revising EARS requirements.

---

## The Eight Defects EARS Prevents

EARS was designed to address these recurring problems in natural language
requirements:

| Defect | Description | Example |
| :--- | :--- | :--- |
| **Ambiguity** | Multiple interpretations possible | "The system shall process the record" |
| **Vagueness** | Imprecise, unmeasurable language | "The system shall respond quickly" |
| **Complexity** | Multiple behaviors in one statement | "The system shall validate, store, and notify..." |
| **Omission** | Missing triggers, conditions, or responses | "The system shall disconnect the network" |
| **Duplication** | Same requirement stated differently in multiple places | Redundant specs across documents |
| **Wordiness** | Excessive verbosity obscuring intent | Multi-paragraph requirement burying the obligation |
| **Inappropriate implementation** | Specifying *how* instead of *what* | "The system shall use a MySQL database" |
| **Untestability** | Cannot be verified through testing | "The system shall be reliable" |

---

## Anti-Pattern 1: Using the Wrong Pattern

Misclassifying the requirement type causes confusion about system behavior.

### When vs. While

`When` is for discrete, instantaneous events. `While` is for persistent
states with duration.

```text
BAD (When for a state):
  When the system is in maintenance mode, the system shall reject logins.

GOOD (While for a state):
  While the system is in maintenance mode, the system shall reject logins.
```

**Why it matters:** "When" implies a one-time response to entering
maintenance mode. "While" correctly communicates that login rejection
persists for the entire duration of the state.

### When vs. If/Then

`When` handles normal operational triggers. `If/Then` handles unwanted
conditions.

```text
BAD (If/Then for normal behavior):
  If the user clicks submit, then the system shall save the form.

GOOD (When for normal behavior):
  When the user clicks submit, the system shall save the form.
```

```text
BAD (When for an error condition):
  When an invalid credit card is entered, the system shall display an error.

GOOD (If/Then for an error condition):
  If an invalid credit card number is entered, then the payment system
  shall display "Invalid card number. Please re-enter your card details."
```

**Why it matters:** The `If/Then` pattern signals to readers and testers
that this is a defensive requirement handling an abnormal case. Using `When`
for errors loses this semantic signal.

---

## Anti-Pattern 2: Compound Requirements (Multiple "shall")

Packing multiple obligations into a single requirement makes testing,
tracing, and maintaining them difficult.

```text
BAD:
  The system shall validate input and log errors and send notifications.

GOOD (decomposed into three requirements):
  When the user submits input, the system shall validate all fields against
  the defined schema.

  If input validation fails, then the system shall log the validation
  errors with a timestamp and user ID.

  If a critical validation error occurs, then the system shall send a
  notification to the system administrator.
```

**Rule of thumb:** If a requirement contains "and" between two actions,
consider whether it should be two requirements. Each EARS statement should
describe a single, atomic system response.

---

## Anti-Pattern 3: Using "Should" Instead of "Shall"

"Should" implies the requirement is optional or advisory, creating ambiguity
about whether the system must actually comply.

```text
BAD:
  The system should encrypt data at rest.

GOOD:
  The system shall encrypt all data at rest using AES-256.
```

**EARS obligation keywords:**

| Word | Meaning | Use in EARS |
| :--- | :--- | :--- |
| shall | Mandatory | Always use this |
| should | Advisory | Never use — ambiguous |
| may | Permissive | Never use in requirements |
| will | Intent | Never use — confused with "shall" |
| must | Mandatory (informal) | Use "shall" for consistency |

---

## Anti-Pattern 4: Passive Voice

Passive voice obscures which entity is responsible for the action.

```text
BAD:
  Data shall be encrypted by the system.

GOOD:
  The system shall encrypt all data at rest.
```

```text
BAD:
  An error message shall be displayed.

GOOD:
  The authentication system shall display "Invalid email or password."
```

**Rule:** Always write in active voice with the system name as the subject.

---

## Anti-Pattern 5: Vague Quantifiers and Adjectives

Unmeasurable language makes requirements untestable.

```text
BAD:  The system shall handle many concurrent users.
GOOD: The system shall support a minimum of 10,000 concurrent user sessions.

BAD:  The system shall respond quickly.
GOOD: The system shall return search results within 200 milliseconds.

BAD:  The system shall be user-friendly.
GOOD: The system shall enable a first-time user to complete the core
      workflow without external assistance in under 5 minutes.

BAD:  The system shall be highly available.
GOOD: The system shall maintain a minimum uptime of 99.99 percent
      measured monthly.
```

### Words and Phrases to Eliminate

**Vague adverbs:** quickly, slowly, efficiently, properly, reasonably,
approximately, usually, typically, generally, soon, eventually, immediately

**Unmeasurable adjectives:** user-friendly, flexible, intuitive, robust,
scalable, efficient, seamless, responsive, reliable, powerful, smart,
easy-to-use

**Vague quantifiers:** various, some, any, many, few, several, most,
a lot, up to (without a number)

**Escape clauses:** as appropriate, if possible, as needed, where practical,
to the extent feasible, if necessary, when applicable (without specifying
when)

**Continuation terms:** etc., and so on, and/or, such as (without exhaustive
list), for example (when used as the complete specification)

**Indefinite temporal terms:** timely, in a timely manner, in real time
(without defining latency), promptly, without delay, as soon as possible,
periodic (without period)

**Replace each with a specific, measurable value.** If you cannot define a
measurement, the requirement is likely ambiguous and needs further
elicitation.

---

## Anti-Pattern 6: Missing System Name

Omitting the system name makes it unclear who or what performs the action.

```text
BAD:
  When the button is clicked, it shall save the data.

GOOD:
  When the user clicks the "Save" button, the document editor shall
  persist the current document to the data store.
```

**Rule:** Always name the system explicitly. Never use pronouns like "it."
Use consistent terminology — if the system is called "the navigation system"
in one requirement, do not call it "the nav module" elsewhere.

---

## Anti-Pattern 7: Specifying Implementation

EARS requirements describe *what* the system must achieve, not *how* it
achieves it internally.

```text
BAD:
  When the user logs in, the system shall query the MySQL users table and
  compare the bcrypt hash.

GOOD:
  When the user submits credentials, the authentication system shall verify
  the credentials and return the result within 500 milliseconds.
```

```text
BAD:
  The system shall use WebSockets for real-time updates.

GOOD:
  The system shall deliver data updates to all connected clients within
  500 milliseconds of the data change occurring.
```

**Exception:** Some requirements legitimately constrain technology choices
(e.g., compliance or interoperability requirements like "The system shall
use TLS 1.3 or later"). This is acceptable when the technology choice is
itself the requirement, not an implementation preference.

---

## Anti-Pattern 8: Negative Requirements

Negative phrasing ("shall not") is harder to test and often unclear.

```text
BAD:
  The system shall not prevent authorized users from accessing resources.

GOOD:
  The system shall allow authenticated users with the required role to
  access protected resources.
```

**Guidelines:**

- Substitute "shall enable" for "shall not prohibit"
- Substitute "shall prohibit" for "shall not allow"
- Never use double negatives ("shall not prevent" = "shall allow")
- Some negative requirements are valid and clearer in negative form (e.g.,
  safety constraints: "the system shall not exceed 100 degrees Celsius").
  Use judgment.

---

## Anti-Pattern 9: Too Many Preconditions

When a requirement accumulates more than three preconditions, it becomes
unwieldy and hard to test.

```text
BAD:
  While the system is online, while the user is authenticated, while the
  database is available, while the cache is warm, when the user requests
  data, the system shall return results.

BETTER (decomposed):
  While the user is authenticated, when the user requests data, the system
  shall return results within 200 milliseconds.

  If the database is unavailable, then the system shall return cached
  results and display a staleness indicator.
```

**Rule:** Limit preconditions to three or fewer. Beyond that, decompose
into multiple requirements or use a table/decision matrix.

---

## Anti-Pattern 10: Missing Trigger or Condition

A requirement that omits the triggering event or precondition is incomplete.

```text
BAD:
  The system shall disconnect the network.

GOOD:
  When the disconnect button is pressed, the software shall terminate the
  active network connection.
```

```text
BAD:
  The engine control system shall enable reverse thrust.

GOOD:
  While the aircraft is on ground, when reverse thrust is commanded, the
  engine control system shall enable reverse thrust.
```

**Why it matters:** Without the trigger or condition, the requirement is
ambiguous — should the system always disconnect the network? On startup?
On shutdown? EARS forces you to make this explicit.

---

## Before-and-After Transformations

These examples show how to transform vague prose into valid EARS
requirements:

### "The system should be fast"

```text
BAD:  The system should be fast.
GOOD: The system shall return search results within 200 milliseconds.
      (Ubiquitous or Event-Driven, depending on context)
```

### "The phone should be lightweight"

```text
BAD:  The phone should be lightweight.
GOOD: The mobile phone shall have a mass of less than 200 grams.
      (Ubiquitous)
```

### "The system should process orders efficiently and handle failures properly"

```text
BAD:  The system should process orders efficiently and handle failures
      properly.

GOOD (decomposed):
  When a customer submits an order, the order processing system shall
  validate the payment information and store the order record within
  3 seconds.
  (Event-Driven)

  If payment validation fails, then the order processing system shall
  notify the customer with the reason for failure and discard the
  incomplete order.
  (Unwanted Behavior)
```

### "Only admins should be able to delete things"

```text
BAD:  Only admins should be able to delete things.

GOOD (decomposed):
  When a user with the administrator role initiates a deletion request,
  the system shall delete the specified resource and log the action.
  (Event-Driven)

  If a user without the administrator role attempts a deletion, then the
  system shall reject the request and display "Insufficient permissions:
  administrator role required."
  (Unwanted Behavior)
```

### "All data shall be encrypted"

```text
BAD:  All data shall be encrypted.

GOOD (decomposed — "all" is ambiguous):
  The system shall encrypt all data at rest using AES-256.
  (Ubiquitous)

  The system shall encrypt all data in transit using TLS 1.3 or later.
  (Ubiquitous)
```

---

## Quality Checklist

Before finalizing any EARS requirement, verify:

- [ ] Contains exactly one "shall"
- [ ] System name is explicit (no pronouns)
- [ ] Uses active voice
- [ ] Response is specific and measurable
- [ ] Correct EARS keyword is used (When/While/If-then/Where)
- [ ] No vague adverbs, adjectives, or quantifiers
- [ ] Describes *what*, not *how* (unless technology is the requirement)
- [ ] Can a tester write a test case from this requirement alone?
- [ ] Single behavior — would splitting improve clarity?
- [ ] Positive phrasing where possible
