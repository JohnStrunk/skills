# EARS Patterns — Detailed Reference

This document provides comprehensive guidance on each EARS pattern, compound
combinations, the general syntax rule, and domain-specific examples. Consult
this when formulating EARS requirements from user prose.

## The General EARS Syntax

Every EARS requirement follows a single generalized structure:

```text
While <optional precondition(s)>, when <optional trigger>,
the <system name> shall <system response>.
```

Cardinality rules:

| Component | Cardinality | Description |
| :--- | :--- | :--- |
| Precondition(s) | Zero or many | States that must be true (`While` clause) |
| Trigger | Zero or one | Event that initiates the response (`When` clause) |
| System name | Exactly one | The system, subsystem, or component |
| System response | One or many | What the system shall do |

Clauses always appear in temporal order: preconditions → trigger → system →
response. This ordering reflects logical precedence: a state must hold, then
an event occurs within that state, then the system responds.

---

## Pattern 1: Ubiquitous

**Template:** `The <system name> shall <system response>.`

Requirements that state fundamental, always-active system properties. No
preconditions, triggers, or conditions — unconditionally true at all times.
No EARS keywords are used.

**When to use:** For properties, constraints, or behaviors that hold
continuously regardless of system state.

**Examples:**

```text
The mobile phone shall have a mass of less than 200 grams.
The system shall encrypt all data at rest using AES-256.
The API shall return responses in JSON format.
The system shall comply with WCAG 2.1 Level AA accessibility guidelines.
The system shall use TLS 1.3 or later for all network communications.
The password storage module shall hash all passwords using bcrypt with a
minimum cost factor of 12.
The database shall maintain referential integrity across all foreign key
relationships.
```

---

## Pattern 2: Event-Driven

**Template:** `When <trigger>, the <system name> shall <system response>.`

**Keyword:** `When`

The system performs an action when a discrete event occurs. The trigger is
instantaneous — it happens at a point in time.

**When to use:** For behaviors triggered by a user action, a signal, a
threshold crossing, a message arriving, or a timer expiring.

**Examples:**

```text
When 'mute' is selected, the laptop shall suppress all audio output.
When the user clicks the "Submit Order" button, the e-commerce system shall
create an order record and redirect to the order confirmation page within
2 seconds.
When a new user account is created, the system shall send a verification
email to the registered address within 30 seconds.
When the temperature sensor detects a reading above 80 degrees Celsius,
the cooling fan shall activate.
When the user selects "Export to PDF," the reporting system shall generate
a PDF document containing all visible data within 10 seconds.
```

---

## Pattern 3: State-Driven

**Template:**
`While <precondition(s)>, the <system name> shall <system response>.`

**Keyword:** `While`

Requirements active for the entire duration of a state. The precondition
describes a persistent condition, not a momentary event.

**When to use:** For behaviors that must be continuously active during a
particular system state, operational mode, or environmental condition.

**Distinguishing from Event-Driven:** If you can ask "how long does it
last?", it's a state — use `While`. If it's instantaneous, use `When`.

**Examples:**

```text
While there is no card in the ATM, the ATM shall display 'insert card to
begin'.
While the system is in maintenance mode, the system shall reject new user
logins.
While battery level is below 15 percent, the mobile device shall disable
background application refresh.
While the user session is active, the web application shall refresh the
authentication token every 15 minutes.
While the patient monitor is connected to a patient, the monitor shall
sample vital signs at least once per second.
```

---

## Pattern 4: Unwanted Behavior

**Template:**
`If <unwanted condition>, then the <system name> shall <system response>.`

**Keywords:** `If ... then`

System responses to undesirable situations — errors, failures, faults, or
boundary violations. The `If ... then` keywords signal that the condition is
*undesirable*, distinguishing this from normal Event-Driven triggers.

**When to use:** For error handling, fault tolerance, safety responses,
boundary conditions, and recovery from undesirable states.

**Distinguishing from Event-Driven:** `If/Then` is exclusively for
**unwanted** conditions. Normal operational triggers use `When`. A user
clicking "Submit" is `When`; an invalid credit card is `If/Then`.

**Examples:**

```text
If an invalid credit card number is entered, then the website shall display
'please re-enter credit card details'.
If the password is entered incorrectly three times, then the application
shall lock the user account for 30 minutes.
If the database is unavailable, then the system shall queue incoming
requests and retry every 30 seconds.
If the API rate limit is exceeded, then the system shall return a 429
status code with a Retry-After header.
If the primary server fails to respond within 5 seconds, then the load
balancer shall route traffic to the secondary server.
```

---

## Pattern 5: Optional Feature

**Template:**
`Where <feature is included>, the <system name> shall <system response>.`

**Keyword:** `Where`

Requirements that apply only when a particular feature or configuration
option is present. Used for product lines, optional modules, or configurable
systems.

**When to use:** For requirements conditional on a feature, module, or
configuration option being present in a particular product variant.

**Examples:**

```text
Where the car has a sunroof, the car shall have a sunroof control panel on
the driver door.
Where two-factor authentication is enabled, the system shall prompt for a
verification code after password entry.
Where the enterprise license tier is active, the system shall enable
SAML-based single sign-on integration.
Where the application includes an offline mode, the system shall cache the
most recent 7 days of data for offline access.
Where the printer has a duplex unit, the printer shall default to
double-sided printing.
```

---

## Pattern 6: Complex (Combined Patterns)

Complex requirements combine multiple EARS keywords. The canonical clause
order is: `Where` → `While` → `When` → `If/Then` → `shall`.

### While + When (State + Event)

```text
While <precondition(s)>, when <trigger>,
the <system name> shall <system response>.
```

**Examples:**

```text
While the aircraft is on ground, when reverse thrust is commanded, the
engine control system shall enable reverse thrust.
While the user is logged in, when the session has been idle for 15 minutes,
the application shall display a timeout warning.
While the system is in debug mode, when an unhandled exception occurs, the
logging service shall capture the full stack trace.
```

### Where + When (Feature + Event)

```text
Where <feature is included>, when <trigger>,
the <system name> shall <system response>.
```

**Examples:**

```text
Where voice control is enabled, when the user says "navigate home," the
navigation system shall calculate a route to the saved home address.
Where biometric authentication is available, when the user taps the login
button, the system shall prompt for fingerprint verification.
```

### Where + While (Feature + State)

```text
Where <feature is included>, while <precondition(s)>,
the <system name> shall <system response>.
```

**Examples:**

```text
Where the heated seats option is installed, while the cabin temperature is
below 10 degrees Celsius, the seat heater shall activate automatically.
Where the premium analytics module is licensed, while a report is being
generated, the system shall display a progress indicator.
```

### While + If/Then (State + Unwanted Behavior)

```text
While <precondition(s)>, if <unwanted condition>,
then the <system name> shall <system response>.
```

**Examples:**

```text
While the aircraft is in flight, if engine oil pressure drops below 40 PSI,
then the engine monitoring system shall illuminate the warning light.
While the system is processing a batch job, if memory usage exceeds
85 percent, then the batch processor shall pause execution and release
cached resources.
```

### When + If/Then (Event + Unwanted Behavior)

```text
When <trigger>, if <unwanted condition>,
then the <system name> shall <system response>.
```

**Examples:**

```text
When the user submits an order, if payment validation fails, then the
system shall notify the customer and discard the incomplete order.
When reverse gear is selected, if the gear does not engage within 2 seconds,
then the transmission controller shall display a gear fault notification.
```

### Where + While + When (Feature + State + Event)

```text
Where <feature is included>, while <precondition(s)>,
when <trigger>, the <system name> shall <system response>.
```

**Examples:**

```text
Where adaptive cruise control is installed, while the vehicle is traveling
above 30 km/h, when the lead vehicle decelerates, the ACC system shall
reduce speed to maintain a 2-second following gap.
Where the premium analytics module is licensed, while a report is being
generated, when the dataset exceeds 1 million rows, the system shall
switch to the distributed processing engine.
```

### Guidelines for Complex Requirements

- Combine patterns only when the requirement genuinely involves multiple
  conditions.
- If a complex requirement becomes difficult to read, decompose it into
  simpler requirements.
- Maintain the canonical clause order: Where → While → When → If/Then → shall.
- Each complex requirement should still describe a single, coherent behavior.
- Limit preconditions to three or fewer. Beyond three, use a table, decision
  matrix, or decompose into multiple requirements.

---

## Pattern Selection Decision Tree

```text
Is the requirement always active (no conditions)?
  YES → Ubiquitous: "The <system> shall <response>"
  NO  → Does it respond to a specific event?
          YES → Is there also a state precondition?
                  YES → Complex: "While <state>, when <event>,
                         the <system> shall <response>"
                  NO  → Event-Driven: "When <event>,
                         the <system> shall <response>"
          NO  → Is it active during a persistent state?
                  YES → State-Driven: "While <state>,
                         the <system> shall <response>"
                  NO  → Does it handle an error or fault?
                          YES → Unwanted: "If <condition>,
                                 then the <system> shall <response>"
                          NO  → Is it feature-dependent?
                                  YES → Optional: "Where <feature>,
                                         the <system> shall <response>"
                                  NO  → Reconsider: likely Ubiquitous
                                         or needs decomposition
```

---

## EARS Keywords and Obligation Levels

### Structural Keywords

| Keyword | Pattern | Meaning |
| :--- | :--- | :--- |
| `While` | State-Driven | Persistent precondition/state |
| `When` | Event-Driven | Discrete triggering event |
| `Where` | Optional Feature | Feature/configuration condition |
| `If ... then` | Unwanted Behavior | Undesirable condition and recovery |
| `shall` | All patterns | Mandatory obligation |

### Obligation Keywords

| Keyword | Level | Use in EARS |
| :--- | :--- | :--- |
| **shall** | Mandatory | Required. The standard EARS keyword. |
| **should** | Advisory | Do not use — creates ambiguity. |
| **may** | Permissive | Do not use in requirements. |
| **will** | Intent | Do not use — confused with "shall". |

Always use "shall" for requirements. It signals a testable, mandatory
obligation.

---

## Domain-Specific Examples

### Web Applications and APIs

```text
The REST API shall require authentication via OAuth 2.0 bearer tokens for
all endpoints except /health and /docs.

When the user clicks the "Submit Order" button, the e-commerce system shall
create an order record and redirect to the order confirmation page within
2 seconds.

While the application is offline, the system shall store task updates in
local storage.

If the API rate limit is exceeded, then the system shall return a 429
status code with a Retry-After header.

Where the enterprise license tier is active, the system shall enable
SAML-based single sign-on integration.

While the user is authenticated, when the user requests access to a
resource, if the user's role does not include the required permission,
then the system shall return a 403 Forbidden response and log the access
attempt.
```

### Embedded Systems and IoT

```text
The firmware shall use a watchdog timer with a maximum timeout of
2 seconds.

When the temperature sensor detects a reading above 80 degrees Celsius,
the cooling fan shall activate.

While the device is operating on battery power, the IoT sensor shall
reduce its reporting interval from 1 minute to 5 minutes.

If the watchdog timer expires without being reset, then the microcontroller
shall perform a hardware reset.

Where the device includes a GPS module, the asset tracker shall report its
position every 60 seconds when in motion.
```

### Medical Devices

```text
The infusion pump shall comply with IEC 62304 software lifecycle
requirements.

When the patient's heart rate exceeds 200 bpm, the cardiac monitor shall
trigger an audible alarm within 2 seconds.

While the patient monitor is connected to a patient, the monitor shall
sample vital signs at least once per second.

If the infusion pump detects an air bubble in the tubing, then the pump
shall stop infusion immediately and sound an alarm.

Where Bluetooth connectivity is included, the wearable health device shall
encrypt all transmitted patient data using AES-128 or stronger.
```

### Financial Systems

```text
The payment processing system shall comply with PCI DSS Level 1
requirements.

When a wire transfer request exceeds $10,000, the compliance system shall
flag the transaction for anti-money-laundering review.

While the market is closed, the trading platform shall accept orders but
mark them as "queued for next trading session."

If the fraud detection system identifies a transaction with a risk score
above 0.85, then the system shall hold the transaction, notify the account
holder via SMS, and require explicit confirmation before proceeding.
```

---

## Decomposing Complex Requirements

When faced with a multi-part requirement from the user, decompose it into
atomic EARS requirements.

### Strategy

1. **Separate normal behavior from error handling.** Normal flows use
   Event-Driven (`When`). Error flows use Unwanted Behavior (`If/Then`).
2. **Separate distinct triggers.** Different events producing different
   responses become separate requirements.
3. **Separate distinct states.** Behavior that differs across states gets one
   State-Driven requirement per state.
4. **Separate optional features.** Feature-dependent behavior gets extracted
   into `Where`-based requirements.

### Example: Login System

**User says:** "The system should make user login convenient and provide
error prompts."

**Decomposed EARS requirements:**

```text
When the user enters a username and password and clicks the "Login" button,
the authentication system shall verify the credentials within 2 seconds.

When credential verification succeeds, the authentication system shall
create a session token and redirect the user to the dashboard.

If credential verification fails, then the authentication system shall
display "Username or password incorrect."

If the user enters incorrect credentials three consecutive times, then the
authentication system shall lock the account for 30 minutes.
```

### Example: Permission Management

**User says:** "Only admins should be able to delete things."

**Decomposed EARS requirements:**

```text
When a user with the "admin" role selects "delete post," the content
management system shall delete the specified post and display a
confirmation.

If a user without the "admin" role attempts to delete a post, then the
content management system shall display "Insufficient permissions" and
prevent the deletion.
```

---

## EARS-to-Gherkin Structural Mapping

Each EARS element maps naturally to Gherkin:

| EARS Element | Gherkin Keyword | Purpose |
| :--- | :--- | :--- |
| `While <precondition>` | `Given <state>` | Establishes context |
| `When <trigger>` | `When <action>` | The triggering event |
| `the <system> shall <response>` | `Then <outcome>` | Expected result |
| `Where <feature>` | `Given <feature enabled>` or `Background` | Feature presence |
| `If <unwanted condition>` | `Given <error setup>` or `When <error>` | Unwanted situation |

**EARS** is the requirement (what must be true). **Gherkin** scenarios are
the proof (concrete examples demonstrating it is true).

---

## NFR Patterns

Non-functional requirements follow the same EARS patterns. Common shapes:

**Performance** (typically Event-Driven with measurable response time):

```text
When the user submits a search query, the search service shall return
results within 200 milliseconds.
```

**Availability** (typically Ubiquitous):

```text
The system shall maintain a minimum uptime of 99.99 percent measured
monthly.
```

**Security** (typically Ubiquitous or Unwanted Behavior):

```text
The system shall encrypt all data at rest using AES-256.

If authentication fails five consecutive times from the same IP address,
then the system shall block that IP for 1 hour.
```

**Accessibility** (typically Ubiquitous):

```text
The system shall comply with WCAG 2.1 Level AA accessibility guidelines.
```

**Scalability** (typically Ubiquitous with measurable limits):

```text
The system shall support a minimum of 10,000 concurrent user sessions
without degradation below the defined performance thresholds.
```
