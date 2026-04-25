# EARS: Easy Approach to Requirements Syntax -- Examples and Best Practices

## Table of Contents

- [1. Overview and Background](#1-overview-and-background)
- [2. The Six EARS Patterns with Extensive Examples](#2-the-six-ears-patterns-with-extensive-examples)
  - [2.1 Ubiquitous Requirements](#21-ubiquitous-requirements)
  - [2.2 Event-Driven Requirements](#22-event-driven-requirements)
  - [2.3 State-Driven Requirements](#23-state-driven-requirements)
  - [2.4 Unwanted Behavior Requirements](#24-unwanted-behavior-requirements)
  - [2.5 Optional Feature Requirements](#25-optional-feature-requirements)
  - [2.6 Complex (Combined) Requirements](#26-complex-combined-requirements)
- [3. Domain-Specific Examples](#3-domain-specific-examples)
  - [3.1 Aerospace and Defense](#31-aerospace-and-defense)
  - [3.2 Automotive and ADAS](#32-automotive-and-adas)
  - [3.3 Medical Devices](#33-medical-devices)
  - [3.4 Embedded Systems and IoT](#34-embedded-systems-and-iot)
  - [3.5 Web Applications and APIs](#35-web-applications-and-apis)
  - [3.6 Software Systems and Cloud](#36-software-systems-and-cloud)
  - [3.7 Consumer Electronics](#37-consumer-electronics)
  - [3.8 Financial Systems](#38-financial-systems)
- [4. Good vs Bad Requirement Comparisons](#4-good-vs-bad-requirement-comparisons)
- [5. Common Mistakes and Anti-Patterns](#5-common-mistakes-and-anti-patterns)
  - [5.1 The Eight Problems EARS Addresses](#51-the-eight-problems-ears-addresses)
  - [5.2 Anti-Patterns in EARS Usage](#52-anti-patterns-in-ears-usage)
  - [5.3 Words and Phrases to Avoid](#53-words-and-phrases-to-avoid)
- [6. Best Practices for Writing EARS Requirements](#6-best-practices-for-writing-ears-requirements)
  - [6.1 Structural Rules](#61-structural-rules)
  - [6.2 Writing Quality Guidelines](#62-writing-quality-guidelines)
  - [6.3 Organizational Adoption](#63-organizational-adoption)
- [7. Decomposing Complex Requirements](#7-decomposing-complex-requirements)
- [8. EARS Requirements and Testing](#8-ears-requirements-and-testing)
  - [8.1 Pattern-to-Test Mapping](#81-pattern-to-test-mapping)
  - [8.2 Test Case Derivation Strategy](#82-test-case-derivation-strategy)
- [9. EARS and Gherkin: Bridging Requirements and Behavior Specifications](#9-ears-and-gherkin-bridging-requirements-and-behavior-specifications)
  - [9.1 Structural Mapping](#91-structural-mapping)
  - [9.2 Pattern-by-Pattern Conversion Examples](#92-pattern-by-pattern-conversion-examples)
  - [9.3 Complementary Strengths](#93-complementary-strengths)
  - [9.4 Workflow for Using EARS and Gherkin Together](#94-workflow-for-using-ears-and-gherkin-together)
- [10. Sources and References](#10-sources-and-references)

---

## 1. Overview and Background

### What is EARS?

From the
[authoritative EARS page](https://alistairmavin.com/ears/)
maintained by EARS creator Alistair Mavin:

> *"The Easy Approach to Requirements Syntax (EARS) is
> a mechanism to gently constrain textual
> requirements."*

EARS provides structured guidance using a small set of
keywords and sentence templates that enable authors to
write high-quality, unambiguous requirements while
remaining in natural language.

### Origin

EARS was developed by Alistair Mavin and colleagues at
Rolls-Royce PLC while analyzing the airworthiness
regulations for a jet engine's control system. The
regulations contained high-level objectives, a mixture
of implicit and explicit requirements at different
levels, lists, guidelines, and supporting information.
In the process of extracting and simplifying the
requirements, Mavin noticed that the requirements all
followed a similar structure and were easiest to read
when the clauses always appeared in the same order.
These patterns were refined and evolved to create EARS.
The notation was first published at the Requirements
Engineering (RE 09) conference in 2009.

### Adoption

EARS is used worldwide by organizations including
Airbus, Bosch, Daimler, Dyson, Honeywell, Intel, NASA,
Rolls-Royce, and Siemens. It is taught at universities
across China, France, Germany, Sweden, the UK, and
the USA.

### Generic EARS Syntax Template and Ruleset

From the
[authoritative EARS page](https://alistairmavin.com/ears/),
the **generic EARS syntax template** is:

> While \<optional pre-condition\>, when
> \<optional trigger\>, the \<system name\> shall
> \<system response\>

The **EARS ruleset** requires that every EARS
requirement contain:

- **Zero or many** preconditions (the "While" clause)
- **Zero or one** trigger (the "When" clause)
- **Exactly one** system name (the subject)
- **One or many** system responses (the "shall" clause)

The clauses always appear in the same order, following
temporal logic.

### Why EARS Works

A senior engineer at a major engineering company once
said: **"If you can't write it in EARS, then you don't
understand it."** This captures a key strength of EARS:
it prevents authors from writing incomplete
requirements. Where other notations may hide missing or
incomplete information in ambiguous statements, EARS
exposes what must be discovered.

EARS frees up cognitive capacity to consider the
**semantics** of a requirement. Authors no longer need
to think about structure -- instead they concentrate on
meaning.

---

## 2. The Six EARS Patterns with Extensive Examples

### 2.1 Ubiquitous Requirements

**Template:**
`The <system name> shall <system response>.`

Ubiquitous requirements are **always active** -- they
have no precondition or trigger. They define fundamental
properties, constraints, or behaviors that must hold at
all times. There is no EARS keyword because no condition
limits when they apply.

**When to use:** For properties, constraints, or
behaviors that are unconditionally true throughout the
system's operation.

#### Ubiquitous Examples

The canonical example from
[alistairmavin.com/ears/](https://alistairmavin.com/ears/):

> "The mobile phone shall have a mass of less than
> XX grams."

```text
The mobile phone shall have a mass of less than
120 grams.

The software shall be written in Python.

The system shall encrypt all data at rest using
AES-256.

The system shall validate all user inputs before
processing.

The system shall be developed using secure coding
practices.

The cell phone shall weigh less than 120 grams.

The system shall provide power to the device at
all times.

The API shall return responses in JSON format.

The system shall log all authentication attempts.

The system shall comply with WCAG 2.1 Level AA
accessibility guidelines.

The database shall maintain referential integrity
across all foreign key relationships.

The system shall use TLS 1.3 or later for all
network communications.

The system shall respond to health check requests
within 100 milliseconds.

The password storage module shall hash all passwords
using bcrypt with a minimum cost factor of 12.
```

### 2.2 Event-Driven Requirements

**Template:**
`When <trigger>, the <system name> shall <system response>.`

Event-driven requirements specify how a system must
respond when a triggering event occurs. The keyword
**When** denotes a discrete, instantaneous event that
initiates a system response.

**When to use:** For behaviors triggered by a specific
event -- a user action, a signal, a threshold being
crossed, a message being received, or a timer expiring.

#### Event-Driven Examples

The canonical example from
[alistairmavin.com/ears/](https://alistairmavin.com/ears/):

> "When 'mute' is selected, the laptop shall suppress
> all audio output."

```text
When the payment is received, the application shall
send a confirmation notification.

When the user clicks the submit button, the system
shall validate the input fields.

When the disconnect button is pressed, the software
shall terminate the network connection.

When the user presses the power button, the system
shall power on.

When the aircraft issues a continuous ignition
command, the engine control system shall initiate
continuous ignition.

When the user submits valid credentials, the
authentication service shall generate a session
token and redirect to the dashboard within 1 second.

When a new user account is created, the system shall
send a verification email to the registered address
within 30 seconds.

When a file upload completes, the document management
system shall generate a thumbnail preview and index
the file contents.

When the temperature sensor detects a reading above
80 degrees Celsius, the cooling fan shall activate.

When the user stops typing in the edit box for more
than 5 seconds, the system shall automatically save
the current content to the draft folder.

When the API receives a GET request for a resource,
the system shall return the resource representation
with a 200 status code.

When a user drags a task card to a different column,
the system shall update the task status to match the
destination column.

When the application reconnects to the network, the
system shall synchronize locally stored updates with
the server.

When the user selects "Export to PDF," the reporting
system shall generate a PDF document containing all
visible data within 10 seconds.
```

### 2.3 State-Driven Requirements

**Template:**
`While <precondition(s)>, the <system name> shall <system response>.`

State-driven requirements are active **as long as** the
specified state remains true. The keyword **While**
denotes a continuing state or condition. The behavior
described must be maintained for the entire duration of
the state.

**When to use:** For behaviors that must be continuously
active during a particular system state, operational
mode, or environmental condition.

#### State-Driven Examples

The canonical example from
[alistairmavin.com/ears/](https://alistairmavin.com/ears/):

> "While there is no card in the ATM, the ATM shall
> display 'insert card to begin'."

```text
While the system is in maintenance mode, the system
shall not accept new user logins.

While the system is in maintenance mode, the system
shall display a maintenance banner on all pages.

While the system is in Do Not Disturb mode, the
software shall silence incoming calls.

While the system is in standby mode, the system
shall monitor for incoming commands.

While the aircraft is in flight and the engine is
running, the engine control system shall maintain
fuel flow above 200 pounds per second.

While the vehicle is traveling above 10 km/h, the
door lock system shall prevent doors from being
opened.

While battery level is below 15 percent, the mobile
device shall disable background application refresh.

While the database connection pool is at maximum
capacity, the application server shall queue incoming
requests.

While the user session is active, the web application
shall refresh the authentication token every
15 minutes.

While the microphone is active, the conferencing
application shall display a red recording indicator.

While the patient monitor is connected to a patient,
the monitor shall sample vital signs at least once
per second.

While the vehicle is in reverse gear, the rear camera
system shall display the rear view on the
infotainment screen.
```

### 2.4 Unwanted Behavior Requirements

**Template:**
`If <unwanted condition>, then the <system name> shall <system response>.`

Unwanted behavior requirements specify the required
system response to **undesired situations** such as
errors, failures, faults, disturbances, or boundary
violations. The keywords **If** and **then** distinguish
these from event-driven requirements -- the "If" signals
that the condition is *undesirable* rather than a normal
operational trigger.

**When to use:** For error handling, fault tolerance,
safety responses, boundary conditions, and recovery
from undesirable states.

#### Unwanted Behavior Examples

The canonical example from
[alistairmavin.com/ears/](https://alistairmavin.com/ears/):

> "If an invalid credit card number is entered, then
> the website shall display 'please re-enter credit
> card details'."

```text
If the password is entered incorrectly three times,
then the application shall lock the user account for
30 minutes.

If an invalid password is entered, then the system
shall display an error message.

If the sensor connection is lost, then the blood
glucose monitor shall display a fault indicator and
cease reporting readings.

If computed airspeed is unavailable, then the engine
control system shall use model airspeed.

If the database is unavailable, then the system
shall queue incoming requests and retry every
30 seconds.

If authentication fails, then the system shall lock
the account after five consecutive failures.

If synchronization conflicts occur, then the system
shall display a resolution dialog to the user.

If the battery level drops below 5 percent and the
device is not plugged into power, then the system
shall initiate an emergency shutdown sequence.

If the API rate limit is exceeded, then the system
shall return a 429 status code with a Retry-After
header.

If a single failure leads to deficient
aircraft-supplied data, then the engine control
system shall not cause a hazardous engine effect.

If the user enters a username and password and
verification fails, then the system shall display
a "username or password incorrect" prompt.

If the primary server fails to respond within
5 seconds, then the load balancer shall route
traffic to the secondary server.

If disk usage exceeds 90 percent, then the
monitoring system shall send an alert to the
operations team and begin log rotation.

If the infusion pump detects an air bubble in the
tubing, then the pump shall stop infusion and sound
an alarm.
```

### 2.5 Optional Feature Requirements

**Template:**
`Where <feature is included>, the <system name> shall <system response>.`

Optional feature requirements apply only in products or
systems that include a specified feature. The keyword
**Where** denotes feature presence or configuration.
This pattern is particularly useful for product lines,
variant configurations, and optional modules.

**When to use:** For requirements that are conditional
on a feature, module, or configuration option being
present in a particular product variant.

#### Optional Feature Examples

The canonical example from
[alistairmavin.com/ears/](https://alistairmavin.com/ears/):

> "Where the car has a sunroof, the car shall have a
> sunroof control panel on the driver door."

```text
Where the DisplayPort is present, the software shall
allow users to select the maximum supported refresh
rate.

Where Bluetooth connectivity is included, the
wearable device shall encrypt all transmitted patient
data.

Where dark mode is enabled, the system shall use the
dark color theme for all UI components.

Where the user has two-factor authentication enabled,
the system shall prompt for a verification code after
password entry.

Where the control system has an overspeed protection
feature, before takeoff, the control system shall
test the feature's validity.

Where the vehicle is equipped with adaptive cruise
control, the system shall maintain a minimum
following distance of 2 seconds.

Where the application includes an offline mode, the
system shall cache the most recent 7 days of data
for offline access.

Where the enterprise license tier is active, the
system shall enable SAML-based single sign-on
integration.

Where the API supports webhook notifications, the
system shall allow users to register up to
10 webhook endpoints per account.

Where the printer has a duplex unit, the printer
shall default to double-sided printing.

Where the medical device includes a wireless data
module, the device shall comply with IEC 62443
cybersecurity requirements.
```

### 2.6 Complex (Combined) Requirements

**Template:** Combinations of multiple EARS keywords.

Complex requirements use more than one EARS keyword to
specify richer system behavior. The simple building
blocks of the individual patterns can be combined. The
most common combinations are:

- **While + When:**
  `While <state>, when <trigger>, the <system> shall <response>.`
- **Where + When:**
  `Where <feature>, when <trigger>, the <system> shall <response>.`
- **While + If/Then:**
  `While <state>, if <unwanted condition>, then the <system> shall <response>.`
- **While + When + If/Then:**
  `While <state>, when <trigger>,`
  `if <unwanted condition>,`
  `then the <system> shall <response>.`
- **Where + While + When:**
  `Where <feature>, while <state>,`
  `when <trigger>,`
  `the <system> shall <response>.`

**When to use:** When a single behavior depends on
multiple conditions -- a combination of state, trigger,
feature presence, or error handling.

#### Complex Pattern Examples

**While + When (State + Event):**

The canonical example from
[alistairmavin.com/ears/](https://alistairmavin.com/ears/):

> "While the aircraft is on ground, when reverse thrust
> is commanded, the engine control system shall enable
> reverse thrust."

```text
While the vehicle is in park, when the ignition is
turned off, the vehicle shall engage the electronic
parking brake.

While the user session is active, when the user
requests a password change, the system shall require
re-authentication before displaying the password
change form.

While the system is in debug mode, when an unhandled
exception occurs, the logging service shall capture
the full stack trace and local variable state.

While the patient is connected to the ventilator,
when the tidal volume falls below 200 mL, the
ventilator shall trigger an alarm.
```

**Where + When (Feature + Event):**

```text
Where voice control is enabled, when the user says
"navigate home," the navigation system shall
calculate a route to the saved home address.

Where the API versioning module is active, when a
request specifies a deprecated API version, the
system shall include a deprecation warning header
in the response.

Where biometric authentication is available, when
the user taps the login button, the system shall
prompt for fingerprint verification instead of
password entry.
```

**While + If/Then (State + Unwanted Behavior):**

```text
While the aircraft is in flight, if engine oil
pressure drops below 40 PSI, then the engine
monitoring system shall illuminate the warning
light and alert the pilot.

While the system is processing a batch job, if
memory usage exceeds 85 percent, then the batch
processor shall pause execution and release cached
resources.

While the vehicle is in motion, if the driver's
seatbelt is unfastened, then the vehicle shall sound
an audible warning every 30 seconds.
```

**While + When + If/Then (State + Event + Unwanted):**

```text
While the aircraft is on ground, when reverse thrust
is commanded, if the thrust reverser fails to deploy
within 3 seconds, then the engine control system
shall alert the pilot and log the failure.

While the user is logged in, when a file upload is
initiated, if the file size exceeds 100 MB, then the
system shall reject the upload and display a
"file too large" message.
```

**Where + While + When (Feature + State + Event):**

```text
Where adaptive cruise control is installed, while
the vehicle is traveling above 30 km/h, when the
lead vehicle decelerates, the ACC system shall reduce
speed to maintain a 2-second following gap.

Where the premium analytics module is licensed, while
a report is being generated, when the dataset exceeds
1 million rows, the system shall switch to the
distributed processing engine.
```

---

## 3. Domain-Specific Examples

### 3.1 Aerospace and Defense

```text
[Ubiquitous]
The engine control system shall comply with EASA
CS-E airworthiness requirements.

[Event-Driven]
When the aircraft issues a continuous ignition
command, the engine control system shall initiate
continuous ignition.

[State-Driven]
While the aircraft is in flight and the engine is
running, the engine control system shall maintain
fuel flow above 200 pounds per second.

[Unwanted Behavior]
If computed airspeed is unavailable, then the engine
control system shall use model airspeed.

If a single failure leads to deficient
aircraft-supplied data, then the engine control
system shall not cause a hazardous engine effect.

[Optional Feature]
Where the control system has an overspeed protection
feature, before takeoff, the control system shall
test the feature's validity.

[Complex]
While the aircraft is on ground, when reverse thrust
is commanded, the engine control system shall enable
reverse thrust.

While the aircraft is in flight, if engine oil
temperature exceeds 160 degrees Celsius, then the
engine monitoring system shall reduce engine power
to idle and alert the crew.

While the aircraft is on approach and below 500 feet
AGL, when a windshear warning is received, the
flight control system shall disengage the
autothrottle and command a go-around pitch attitude.
```

### 3.2 Automotive and ADAS

```text
[Ubiquitous]
The braking system shall comply with UN Regulation
No. 13H performance requirements.

The vehicle control unit shall complete a full
self-diagnostic cycle within 500 milliseconds of
ignition-on.

[Event-Driven]
When the driver presses the emergency stop button,
the autonomous driving system shall bring the vehicle
to a controlled stop within the current lane.

When the driver selects "Park" on the gear selector,
the transmission control module shall engage the
parking pawl.

When the forward-facing camera detects a pedestrian
in the vehicle path at a closing speed above 10 km/h,
the AEB system shall apply maximum braking force.

[State-Driven]
While the vehicle is traveling above 10 km/h, the
door lock system shall prevent doors from being
opened from the inside.

While the vehicle is in reverse gear, the rear camera
system shall display the rear view on the
infotainment screen.

While adaptive cruise control is engaged, the vehicle
shall maintain a minimum following distance of
2 seconds from the lead vehicle.

[Unwanted Behavior]
If the steering angle sensor signal is lost, then
the electronic stability control system shall
activate the ESC warning light and disable torque
vectoring.

If the battery management system detects a cell
voltage above 4.3V, then the BMS shall disconnect
the charging circuit and log a fault code.

[Optional Feature]
Where the vehicle is equipped with lane departure
warning, the system shall provide a haptic steering
wheel vibration when an unintentional lane departure
is detected at speeds above 60 km/h.

[Complex]
When the reverse gear button is pressed once, if the
software detects that the reverse gear does not
engage, then the software shall display a
notification to the driver.

While the vehicle is traveling above 30 km/h, when
the lane-keep assist detects the vehicle drifting
toward a lane boundary without a turn signal active,
the LKAS shall apply corrective steering torque.

Where the trailer tow package is installed, while a
trailer is electrically connected, when the driver
activates the turn signal, the vehicle shall also
activate the corresponding trailer turn signal.
```

### 3.3 Medical Devices

```text
[Ubiquitous]
The infusion pump shall comply with IEC 62304
software lifecycle requirements.

The patient monitoring system shall maintain a
minimum uptime of 99.99 percent.

The blood pressure cuff shall be accurate to within
plus or minus 3 mmHg.

[Event-Driven]
When the patient's heart rate exceeds 200 bpm, the
cardiac monitor shall trigger an audible alarm within
2 seconds.

When the clinician scans a patient wristband, the
medication administration system shall display the
patient's active medication orders.

When the surgeon activates the electrosurgical unit,
the device shall deliver the selected power within
0.5 seconds.

[State-Driven]
While the device is in sterilization mode, the
surgical instrument tracker shall disable all user
input.

While the patient monitor is connected to a patient,
the monitor shall sample vital signs at least once
per second.

While the MRI system is performing a scan, the
system shall prevent the examination room door from
being opened.

[Unwanted Behavior]
If the sensor connection is lost, then the blood
glucose monitor shall display a fault indicator and
cease reporting readings.

If the infusion pump detects an air bubble in the
tubing, then the pump shall stop infusion immediately
and sound an alarm.

If the defibrillator detects an impedance outside
the range of 25-175 ohms, then the defibrillator
shall display "Check Electrodes" and withhold shock
delivery.

If the sterilizer fails to reach the required
temperature within 10 minutes, then the sterilizer
shall abort the cycle and display a failure code.

[Optional Feature]
Where Bluetooth connectivity is included, the
wearable health device shall encrypt all transmitted
patient data using AES-128 or stronger.

Where the medical device includes a wireless data
module, the device shall comply with IEC 62443
cybersecurity requirements.

[Complex]
While the ventilator is delivering oxygen, when the
oxygen supply pressure drops below 2 bar, the
ventilator shall activate an emergency alarm and
switch to the backup supply.

While the patient is undergoing anesthesia, when the
end-tidal CO2 reading exceeds 45 mmHg, the
anesthesia monitor shall alert the anesthesiologist
with a high-priority alarm.

Where the insulin pump supports closed-loop mode,
while the patient's glucose reading is below
70 mg/dL, the pump shall suspend insulin delivery
and alert the patient.
```

### 3.4 Embedded Systems and IoT

```text
[Ubiquitous]
The firmware shall use a watchdog timer with a
maximum timeout of 2 seconds.

The IoT gateway shall support a minimum of 100
simultaneous device connections.

[Event-Driven]
When the temperature sensor detects a reading above
80 degrees Celsius, the cooling fan shall activate.

When the motion sensor detects movement in the
monitored zone, the security system shall capture a
10-second video clip and upload it to the cloud.

When the OTA update server pushes a new firmware
version, the device shall download and verify the
update integrity before applying it.

[State-Driven]
While the device is operating on battery power, the
IoT sensor shall reduce its reporting interval from
1 minute to 5 minutes.

While the system is in low-power sleep mode, the
microcontroller shall consume no more than
10 microamps.

While the network connection is unavailable, the
edge device shall buffer up to 1000 sensor readings
in local flash storage.

[Unwanted Behavior]
If the watchdog timer expires without being reset,
then the microcontroller shall perform a hardware
reset.

If the over-the-air update fails checksum
verification, then the device shall roll back to the
previous firmware version.

If the MQTT broker connection is lost, then the IoT
device shall attempt reconnection with exponential
backoff starting at 1 second.

[Optional Feature]
Where the device includes a GPS module, the asset
tracker shall report its position every 60 seconds
when in motion.

Where the device supports Zigbee, the hub shall
allow mesh network formation with up to 32 nodes.

[Complex]
While the device is operating on battery, when the
battery level drops below 10 percent, the IoT sensor
shall transmit a low-battery alert and enter deep
sleep mode.

While the environmental monitoring station is in
active mode, when the air quality index exceeds 150,
the station shall increase its sampling rate to once
every 10 seconds.

Where the industrial controller includes a safety
relay, while the safety interlock is engaged, if
the emergency stop button is pressed, then the
controller shall de-energize all outputs within
50 milliseconds.
```

### 3.5 Web Applications and APIs

```text
[Ubiquitous]
The API shall return responses in JSON format
conforming to the JSON:API specification.

The web application shall render correctly in Chrome,
Firefox, Safari, and Edge (latest two major
versions).

The REST API shall require authentication via
OAuth 2.0 bearer tokens for all endpoints except
/health and /docs.

[Event-Driven]
When the user clicks the "Submit Order" button, the
e-commerce system shall create an order record and
redirect to the order confirmation page within
2 seconds.

When the API receives a POST request to /users, the
system shall create a new user record and return a
201 status code with the created resource.

When a user submits a form with an invalid email
address, the system shall display "Please enter a
valid email address" below the email field without
reloading the page.

When the user selects "Export to CSV," the system
shall generate and initiate a download of the data
file within 5 seconds for datasets up to
100,000 rows.

[State-Driven]
While the application is offline, the system shall
store task updates in local storage.

While the user session is active, the web application
shall refresh the authentication token every
15 minutes.

While the application is in read-only mode during
database migration, the system shall disable all form
submission buttons and display a maintenance notice.

[Unwanted Behavior]
If the API rate limit is exceeded, then the system
shall return a 429 status code with a Retry-After
header indicating the number of seconds until the
limit resets.

If the CDN returns a 5xx error, then the web
application shall serve content from the origin
server and log the CDN failure.

If a database query takes longer than 30 seconds,
then the system shall terminate the query, return a
timeout error to the client, and log the slow query
details.

If the user submits a duplicate form submission
within 5 seconds, then the system shall reject the
second submission and display "Your request is
already being processed."

[Optional Feature]
Where the enterprise license tier is active, the
system shall enable SAML-based single sign-on
integration.

Where the API supports webhook notifications, the
system shall allow users to register up to 10
webhook endpoints per account.

Where the application includes real-time
collaboration features, the system shall synchronize
document changes across all connected clients within
500 milliseconds.

[Complex]
While the user is authenticated, when the user
requests access to a resource, if the user's role
does not include the required permission, then the
system shall return a 403 Forbidden response and log
the access attempt.

Where the multi-tenant module is active, while a
tenant's storage quota is above 90 percent, when the
tenant attempts to upload a file, the system shall
reject the upload with a "storage quota exceeded"
message.

Where the API versioning module is active, when a
request specifies a deprecated API version, the
system shall include a Deprecation header with the
sunset date in the response.
```

### 3.6 Software Systems and Cloud

```text
[Ubiquitous]
The deployment pipeline shall complete a full
build-and-test cycle in under 15 minutes.

The container orchestrator shall maintain a minimum
of 2 healthy replicas for each production service.

The log aggregation service shall retain all logs for
a minimum of 90 days.

[Event-Driven]
When a deployment fails health checks after
3 consecutive attempts, the CI/CD pipeline shall
automatically roll back to the last known good
version.

When a new container image is pushed to the registry,
the deployment system shall scan the image for known
vulnerabilities before allowing promotion to
production.

When the autoscaler detects average CPU utilization
above 75 percent for 5 consecutive minutes, the
cluster shall add one additional pod replica.

[State-Driven]
While the primary database is unavailable, the
application shall route all read queries to the read
replica.

While the system is performing a rolling update, the
load balancer shall drain connections from pods being
terminated over a 30-second grace period.

While the message queue depth exceeds 10,000
messages, the monitoring system shall emit a
high-priority alert every 5 minutes.

[Unwanted Behavior]
If the primary server fails to respond within
5 seconds, then the load balancer shall route traffic
to the secondary server.

If disk usage exceeds 90 percent, then the monitoring
system shall send an alert to the operations team
and begin log rotation.

If the configuration service is unreachable at
startup, then the application shall load the last
cached configuration and log a warning.

[Complex]
While the system is processing a batch import, when
memory usage exceeds 85 percent, if the import is
less than 50 percent complete, then the batch
processor shall checkpoint progress, release
resources, and schedule a retry.

Where the disaster recovery module is configured,
while the primary region is unreachable for more than
60 seconds, when a client request arrives, the
traffic manager shall route the request to the DR
region.
```

### 3.7 Consumer Electronics

```text
[Ubiquitous]
The mobile phone shall have a mass of less than
200 grams.

The smart speaker shall support voice recognition in
at least 5 languages.

[Event-Driven]
When the user double-presses the home button, the
smartphone shall display the app switcher.

When the user says "Hey Assistant," the smart speaker
shall activate the voice recognition system and emit
an acknowledgment tone.

When the headphones are removed from the charging
case, the headphones shall connect to the last paired
device within 3 seconds.

[State-Driven]
While the e-reader battery is below 5 percent, the
e-reader shall disable the backlight and display a
low-battery warning.

While the noise-canceling mode is active, the
headphones shall reduce ambient sound by at least
30 dB across the 100 Hz to 1 kHz frequency range.

[Unwanted Behavior]
If the smart thermostat loses Wi-Fi connectivity,
then the thermostat shall continue operating on the
last programmed schedule.

If the smart lock battery voltage drops below 4.5V,
then the smart lock shall send a push notification
to the owner's phone and emit a low-battery beep on
each lock operation.

[Optional Feature]
Where the television supports HDR10+, the TV shall
automatically switch to HDR processing when HDR
content is detected.

Where the printer has a duplex unit, the printer
shall default to double-sided printing.
```

### 3.8 Financial Systems

```text
[Ubiquitous]
The trading platform shall maintain an audit trail
of all transactions with nanosecond-precision
timestamps.

The payment processing system shall comply with
PCI DSS Level 1 requirements.

[Event-Driven]
When a wire transfer request exceeds $10,000, the
compliance system shall flag the transaction for
anti-money-laundering review.

When the user initiates a stock trade, the order
management system shall route the order to the best
available exchange within 50 milliseconds.

When the end-of-day batch process completes, the
reconciliation system shall generate a discrepancy
report and email it to the finance team.

[State-Driven]
While the market is closed, the trading platform
shall accept orders but mark them as "queued for
next trading session."

While the account balance is negative, the banking
system shall block all debit transactions except
recurring bill payments.

[Unwanted Behavior]
If a transaction is declined by the payment
processor, then the checkout system shall display
the decline reason and allow the customer to try a
different payment method.

If the fraud detection system identifies a
transaction with a risk score above 0.85, then the
system shall hold the transaction, notify the account
holder via SMS, and require explicit confirmation
before proceeding.

If the real-time market data feed is interrupted,
then the trading dashboard shall display a
"stale data" indicator and show the timestamp of the
last received data.

[Complex]
While the account is flagged for enhanced due
diligence, when a transfer request is submitted to a
high-risk jurisdiction, the compliance system shall
require dual authorization from two separate
compliance officers before processing.

Where the premium trading tier is active, while
extended trading hours are in effect, when a limit
order is placed, the order management system shall
validate the order against extended-hours price
bands.
```

---

## 4. Good vs Bad Requirement Comparisons

The following table shows vague or ambiguous
requirements alongside their EARS reformulations. The
EARS versions add explicit triggers, preconditions,
measurable criteria, and clear system responses.

### 4.1 Missing Trigger

| Bad Requirement | Problem | EARS Requirement |
| --- | --- | --- |
| "The system shall break network connection." | No trigger -- when should this happen? | "When the disconnect button is pressed, the software shall terminate the network connection." |
| "The driver is able to override/disable the system at all times." | No trigger specified for the override action. | "When the driver presses the override button, the ADAS system shall disable all driver-assistance functions." |
| "The system should auto-save user edits." | No trigger -- when does the save occur? Vague "should." | "When the user stops typing in the edit box for more than 5 seconds, the system shall automatically save the current content to the draft folder." |

### 4.2 Vague Language

| Bad Requirement | Problem | EARS Requirement |
| --- | --- | --- |
| "Page loading shouldn't be too slow." | "Too slow" is subjective and unmeasurable. | "The system shall return page content within 2 seconds of a user request (excluding network latency)." |
| "The system must refresh the data reasonably quickly." | "Reasonably quickly" is ambiguous. | "The system shall refresh the displayed data within 500 milliseconds of receiving updated values from the data source." |
| "The system should make user login convenient and provide error prompts." | "Convenient" is subjective. Multiple concerns in one statement. | Decomposed into: (1) "When the user enters a username and password and clicks the Login button, the system shall verify the credentials within 2 seconds." (2) "If credential verification fails, then the system shall display 'Username or password incorrect.'" |
| "The system should be user-friendly." | Completely subjective, untestable. | "The system shall enable a first-time user to complete the core workflow (create account, add item, checkout) without external assistance in under 5 minutes." |

### 4.3 Missing Preconditions

| Bad Requirement | Problem | EARS Requirement |
| --- | --- | --- |
| "The engine control system shall enable reverse thrust." | Missing critical safety context -- when? Under what conditions? | "While the aircraft is on ground, when reverse thrust is commanded, the engine control system shall enable reverse thrust." |
| "Admins can delete user posts, but regular users cannot." | Two requirements mixed. No clear structure. | (1) "When a user with the 'admin' role selects 'delete post,' the system shall delete the post and display a confirmation message." (2) "When a user with a role other than 'admin' attempts to delete a post, the system shall display 'Insufficient permissions' and prevent the deletion." |

### 4.4 Multiple Concerns

| Bad Requirement | Problem | EARS Requirement |
| --- | --- | --- |
| "The system shall validate input, log errors, and send notifications." | Three requirements combined into one. | (1) "When the user submits input, the system shall validate all fields against the defined schema." (2) "If input validation fails, then the system shall log the validation errors with a timestamp and user ID." (3) "If a critical validation error occurs, then the system shall send a notification to the system administrator." |

### 4.5 Inappropriate Implementation

| Bad Requirement | Problem | EARS Requirement |
| --- | --- | --- |
| "The system shall use a MySQL database to store user data." | Specifies implementation, not need. | "The system shall persist all user data in a durable data store with ACID transaction support." |
| "The system shall use WebSockets for real-time updates." | Specifies technology, not behavior. | "The system shall deliver data updates to all connected clients within 500 milliseconds of the data change occurring." |

### 4.6 Ambiguous Scope

| Bad Requirement | Problem | EARS Requirement |
| --- | --- | --- |
| "All data shall be encrypted." | "All" is ambiguous -- at rest? In transit? Both? | (1) "The system shall encrypt all data at rest using AES-256." (2) "The system shall encrypt all data in transit using TLS 1.3 or later." |
| "Users can access the system." | Which users? What kind of access? | "When an authenticated user with a valid session token sends a request to a protected endpoint, the API shall process the request and return the appropriate response." |

---

## 5. Common Mistakes and Anti-Patterns

### 5.1 The Eight Problems EARS Addresses

The original EARS research at Rolls-Royce identified
eight common problems in natural language requirements
that EARS was specifically designed to reduce or
eliminate:

1. **Ambiguity** -- A word or phrase has two or more
   different meanings. Example: "The system shall
   process the record" (which record? what does
   "process" mean?).

2. **Vagueness** -- Lack of precision, structure, or
   detail. Example: "The system shall be fast" (how
   fast? measured how?).

3. **Complexity** -- A requirement is too complicated,
   trying to capture multiple behaviors in a single
   statement. Example: "The system shall validate,
   store, and notify when data is received and if
   errors occur log them and retry."

4. **Omission** -- Important information is missing.
   Example: "The system shall display the error"
   (which error? to whom? on what screen?).

5. **Duplication** -- The same requirement is stated in
   multiple places, often with slight variations that
   create contradictions.

6. **Wordiness** -- Excessive words that obscure the
   requirement's intent. Example: "In the event that
   it should so happen that the user, at any point
   during their interaction with the system, should
   decide to change their password..."

7. **Inappropriate Implementation** -- The requirement
   specifies *how* instead of *what*. Example: "The
   system shall use a linked list to maintain the
   transaction queue."

8. **Untestability** -- The requirement cannot be
   verified. Example: "The system shall be reliable"
   (no measurable criterion).

Application of EARS demonstrated **a significant
reduction in all eight problem types** when requirements
were rewritten using the EARS patterns.

### 5.2 Anti-Patterns in EARS Usage

#### Anti-Pattern 1: Using the Wrong Pattern

Misclassifying the requirement type leads to confusion:

```text
BAD (using Event-Driven for a State):
  "When the system is in maintenance mode, the system
  shall reject logins."

GOOD (correctly using State-Driven):
  "While the system is in maintenance mode, the system
  shall reject logins."
```

The distinction matters: "When" implies a one-time
trigger event, while "While" implies a continuous state.
A system entering maintenance mode is a state, not a
discrete event.

#### Anti-Pattern 2: Compound Requirements

Packing multiple behaviors into a single requirement:

```text
BAD:
  "The system shall validate input and log errors and
  send notifications."

GOOD (decomposed):
  "When the user submits input, the system shall
  validate all fields."
  "If input validation fails, then the system shall
  log the error details."
  "If a critical validation error occurs, then the
  system shall notify the administrator."
```

#### Anti-Pattern 3: Using "Should" Instead of "Shall"

```text
BAD:
  "The system should encrypt data at rest."

GOOD:
  "The system shall encrypt all data at rest using
  AES-256."
```

"Should" implies optionality. "Shall" is mandatory.
EARS requires "shall" to indicate that the requirement
is binding.

#### Anti-Pattern 4: Passive Voice

```text
BAD:
  "Data shall be encrypted by the system."

GOOD:
  "The system shall encrypt all data at rest."
```

Active voice makes the responsible entity clear.

#### Anti-Pattern 5: Too Many Preconditions

When a requirement accumulates more than three
preconditions, the sentence becomes unwieldy:

```text
BAD:
  "While the system is online, while the user is
  authenticated, while the database is available,
  while the cache is warm, when the user requests
  data, the system shall return results."

BETTER:
  Use a table, list, or separate the requirement
  into multiple statements.
```

If a requirement needs more than 3 preconditions,
consider whether it should be decomposed or expressed
in a different format (table, state chart, or decision
matrix).

#### Anti-Pattern 6: Specifying Implementation

```text
BAD:
  "When the user logs in, the system shall query the
  MySQL users table and compare the bcrypt hash."

GOOD:
  "When the user submits credentials, the
  authentication system shall verify the credentials
  and return the result within 500 milliseconds."
```

EARS requirements should describe **what** the system
does, not **how** it does it.

#### Anti-Pattern 7: Negative Requirements Where Positive Is Clearer

```text
BAD:
  "The system shall not prevent authorized users from
  accessing resources."

GOOD:
  "The system shall allow authenticated users with
  the required role to access protected resources."
```

Prefer positive phrasing. Substitute "shall enable" for
"shall not prohibit," and "shall prohibit" for "shall
not allow." Never use double negatives ("shall not
prevent" means "shall allow").

#### Anti-Pattern 8: Vague Quantifiers

```text
BAD:
  "The system shall handle many concurrent users."

GOOD:
  "The system shall support a minimum of 10,000
  concurrent user sessions."
```

#### Anti-Pattern 9: Mixing Wanted and Unwanted Behavior

```text
BAD (using If/Then for normal behavior):
  "If the user clicks submit, then the system shall
  save the form."

GOOD (using When for normal behavior):
  "When the user clicks submit, the system shall save
  the form."
```

The If/Then pattern is reserved for **unwanted**
conditions (errors, faults, boundary violations). Normal
operational triggers use "When."

### 5.3 Words and Phrases to Avoid

The following categories of language should be
eliminated from EARS requirements:

#### Vague Modal Verbs (Use "shall" Instead)

- should, could, might, may, can, ought to, would

#### Vague Adverbs

- usually, approximately, sufficiently, typically,
  generally, normally, frequently, occasionally,
  reasonably, properly, adequately, soon, later,
  eventually, immediately, quickly, slowly

#### Unmeasurable Performance Terms

- user-friendly, flexible, easy-to-use, fast,
  intuitive, robust, scalable, efficient, seamless,
  responsive, smart, reliable, powerful

#### Vague Quantifiers

- various, some, any, a lot, many, few, several, most,
  every (when scope is ambiguous), up to,
  approximately, at least (without a number)

#### Escape Clauses

- as appropriate, if possible, as needed, where
  practical, to the extent feasible, if necessary,
  as required, when applicable (without specifying
  when it applies)

#### Continuation Terms

- etc., and so on, and/or, such as (without exhaustive
  list), for example (when used as the complete
  specification)

#### Indefinite Temporal Terms

- timely, in a timely manner, in real time (without
  defining latency), promptly, without delay, as soon
  as possible, periodic (without period)

---

## 6. Best Practices for Writing EARS Requirements

### 6.1 Structural Rules

1. **Use "shall" exclusively** for mandatory
   requirements. Not "should," "must," "will," or
   "may." The word "shall" signals a binding
   obligation.

2. **Active voice required.** The system performs the
   action. Write "The system shall encrypt data" not
   "Data shall be encrypted by the system."

3. **One behavior per requirement.** Each EARS
   statement describes a single, atomic system
   response. If you write "and" between two actions,
   consider splitting into two requirements.

4. **Measurable and testable criteria.** Every
   requirement must be verifiable. Include specific
   values: "within 200 milliseconds," "at least
   99.9 percent," "no more than 50 MB."

5. **Describe "what," not "how."** Requirements specify
   behavior, not implementation. Say what the system
   must achieve, not which technology or algorithm
   to use.

6. **Match the pattern to the behavior type:**
   - Constant property or constraint -> Ubiquitous
   - Response to a discrete event -> Event-Driven
     (When)
   - Behavior during a continuing state ->
     State-Driven (While)
   - Response to an error or fault -> Unwanted
     Behavior (If/Then)
   - Behavior dependent on feature presence ->
     Optional Feature (Where)

7. **Maintain consistent clause ordering.**
   Preconditions before triggers before system name
   before system response. Always follow the temporal
   logic order.

8. **Name the system explicitly.** Do not use pronouns
   like "it." Always state the system name: "the
   engine control system," "the API gateway," "the
   patient monitor."

### 6.2 Writing Quality Guidelines

1. **Start with the EARS pattern selection.** Before
   writing a requirement, ask: "Is this always true?
   Is it triggered by an event? Is it active during a
   state? Is it handling an error? Does it depend on a
   feature?" The answer determines the pattern.

2. **If you can't write it in EARS, you don't
   understand it.** Missing clauses (no trigger? no
   precondition? no measurable response?) signal that
   more analysis is needed. EARS exposes gaps.

3. **Write requirements and test cases together.**
   Defining the test at the same time as the
   requirement ensures testability and reveals missing
   details.

4. **Use consistent terminology.** Create a glossary.
   If the system is called "the navigation system" in
   one requirement, do not call it "the nav module" or
   "GPS system" in another.

5. **Limit preconditions to three or fewer.** Beyond
   three preconditions, use a table, decision matrix,
   or decompose into multiple requirements.

6. **Replace universal quantifiers with specifics.**
   Instead of "all users," specify "users with the
   'admin' role." Instead of "any input," specify
   "text input in the search field."

7. **Specify boundary values.** Instead of "large
   files," say "files exceeding 100 MB." Instead of
   "high traffic," say "more than 10,000 requests per
   second."

8. **Include units and precision.** "200 milliseconds,"
   not "200ms." "Plus or minus 3 mmHg," not "about
   3 mmHg." "99.99 percent uptime measured monthly,"
   not "high availability."

9. **Review requirements in peer groups.** Multiple
   reviewers catch ambiguity that individual authors
   miss. EARS makes reviews faster because the
   structure is consistent.

10. **Use the EARS pattern as a checklist during
    review:**
    - Does the requirement have exactly one system
      name?
    - Is the correct EARS keyword used
      (When/While/If/Where)?
    - Is the system response specific and measurable?
    - Can I write a test case for this requirement?
    - Is it a single behavior, or should it be split?

### 6.3 Organizational Adoption

1. **Start with a pilot project.** Apply EARS to a
   small, well-scoped project before rolling out
   organization-wide.

2. **Half-day training is sufficient.** Many
   organizations complete EARS training in half a day
   and see immediate improvement in requirement
   quality.

3. **No special tooling required.** EARS works in any
   text editor, word processor, or requirements
   management tool. It layers on top of existing
   processes.

4. **Assign EARS champions.** Designate experienced
   practitioners within teams to mentor colleagues
   and review requirements for EARS compliance.

5. **Create a domain-specific example library.**
   Maintain a curated set of EARS examples relevant
   to your industry and product domain for reference.

6. **Integrate EARS checks into reviews.** Add EARS
   compliance as a review criterion alongside existing
   quality gates.

7. **Combine with models.** EARS works alongside
   activity diagrams, state charts, sequence diagrams,
   and other notations. Use EARS for the textual
   requirements; use diagrams for complex interactions.

---

## 7. Decomposing Complex Requirements

### Strategy: Break Down by EARS Pattern

When faced with a complex, multi-part requirement,
identify the distinct behaviors and assign each to an
appropriate EARS pattern.

#### Decomposition Example: Login System

**Original (monolithic):**
> "The system should make user login convenient and
> provide error prompts."

**Decomposed EARS requirements:**

```text
REQ-LOGIN-001 [Event-Driven]:
  When the user enters a username and password and
  clicks the "Login" button, the authentication system
  shall verify the credentials against the user
  database within 2 seconds.

REQ-LOGIN-002 [Unwanted Behavior]:
  If credential verification fails, then the
  authentication system shall display "Username or
  password incorrect."

REQ-LOGIN-003 [Unwanted Behavior]:
  If the user enters incorrect credentials three
  consecutive times, then the authentication system
  shall lock the account for 30 minutes.

REQ-LOGIN-004 [Event-Driven]:
  When credential verification succeeds, the
  authentication system shall create a session token
  and redirect the user to the dashboard.
```

#### Decomposition Example: Data Handling System

**Original (monolithic):**
> "The system shall validate, store, and process
> incoming data, handling errors appropriately."

**Decomposed EARS requirements:**

```text
REQ-DATA-001 [Event-Driven]:
  When the system receives incoming data, the data
  processing module shall validate the data against
  the defined schema within 500 milliseconds.

REQ-DATA-002 [Event-Driven]:
  When data validation succeeds, the data processing
  module shall persist the data to the primary data
  store.

REQ-DATA-003 [Unwanted Behavior]:
  If data validation fails, then the data processing
  module shall reject the data, log the validation
  errors, and return an error response to the sender.

REQ-DATA-004 [Unwanted Behavior]:
  If the primary data store is unavailable, then the
  data processing module shall write the data to the
  local queue and retry persistence every 60 seconds.
```

#### Decomposition Example: Permission Management

**Original (monolithic):**
> "Admins can delete user posts, but regular users
> cannot."

**Decomposed EARS requirements:**

```text
REQ-PERM-001 [Event-Driven]:
  When a user with the "admin" role selects "delete
  post," the content management system shall delete
  the specified post and display a confirmation.

REQ-PERM-002 [Unwanted Behavior]:
  If a user without the "admin" role attempts to
  delete a post, then the content management system
  shall display "Insufficient permissions" and prevent
  the deletion.
```

### Decomposition Guidelines

1. **Separate normal behavior from error handling.**
   Normal flows use Event-Driven (When). Error flows
   use Unwanted Behavior (If/Then).

2. **Separate distinct triggers.** If two different
   events produce different responses, write two
   requirements.

3. **Separate distinct states.** If behavior differs
   across states, write one State-Driven requirement
   per state.

4. **Separate optional features.** If behavior depends
   on feature presence, extract it into a Where-based
   requirement.

5. **Use linked requirement IDs.** Give decomposed
   requirements related IDs (e.g., REQ-LOGIN-001
   through REQ-LOGIN-004) to maintain traceability to
   the original need.

6. **When complexity exceeds 3 preconditions,
   restructure.** Use tables, decision matrices, or
   state diagrams supplemented by simpler EARS
   statements.

7. **Test each decomposed requirement independently.**
   If you cannot write a standalone test for a
   decomposed requirement, it may need further
   decomposition.

---

## 8. EARS Requirements and Testing

### 8.1 Pattern-to-Test Mapping

Each EARS pattern maps naturally to specific test
structures:

#### Ubiquitous -> Continuous/Invariant Tests

Since ubiquitous requirements are always true, they
require **invariant verification** -- tests that check
the property holds across all system states and
operations.

| EARS Requirement | Test Strategy |
| --- | --- |
| "The API shall return responses in JSON format." | Verify every API endpoint returns valid JSON. Run across all operations (GET, POST, PUT, DELETE). |
| "The system shall encrypt all data at rest using AES-256." | Inspect storage at rest across all data stores. Verify encryption algorithm. Run after every data write operation. |

#### Event-Driven -> Stimulus-Response Tests

Event-driven requirements map to **trigger-and-verify**
tests: stimulate the trigger, then verify the response.

| EARS Requirement | Test Case |
| --- | --- |
| "When 'mute' is selected, the laptop shall suppress all audio output." | **Precondition:** Audio is playing. **Action:** Select mute. **Verify:** Audio output level is zero. |
| "When the user clicks Submit, the system shall save the form data." | **Precondition:** Form is filled with valid data. **Action:** Click Submit. **Verify:** Data appears in database. Form shows confirmation. |

#### State-Driven -> State-Based Tests

State-driven requirements require tests that establish
the state, verify the behavior is active during the
state, and verify it ceases when the state ends.

| EARS Requirement | Test Cases |
| --- | --- |
| "While in maintenance mode, the system shall reject logins." | **Test 1:** Enter maintenance mode. Attempt login. Verify rejection. **Test 2:** Exit maintenance mode. Attempt login. Verify success. **Test 3:** Verify rejection message content during maintenance. |

#### Unwanted Behavior -> Negative/Fault-Injection Tests

Unwanted behavior requirements map to **negative
tests** and **fault injection** -- deliberately creating
the unwanted condition and verifying the system responds
correctly.

| EARS Requirement | Test Cases |
| --- | --- |
| "If the password is entered incorrectly three times, then the system shall lock the account for 30 minutes." | **Test 1:** Enter wrong password 3 times. Verify account is locked. **Test 2:** Enter wrong password 2 times, then correct. Verify access. **Test 3:** After lock, wait 30 minutes. Verify unlock. **Test 4:** During lock, attempt correct password. Verify still locked. |

#### Optional Feature -> Configuration-Based Tests

Optional feature requirements require tests that run in
**both configurations**: with the feature present and
without.

| EARS Requirement | Test Cases |
| --- | --- |
| "Where dark mode is enabled, the system shall use the dark color theme." | **Test 1 (feature ON):** Enable dark mode. Verify dark theme is applied. **Test 2 (feature OFF):** Disable dark mode. Verify dark theme is NOT applied. |

#### Complex -> Combined Test Scenarios

Complex requirements require multi-dimensional tests
covering the combinations of preconditions, triggers,
and error conditions.

| EARS Requirement | Test Matrix |
| --- | --- |
| "While the aircraft is on ground, when reverse thrust is commanded, the engine control system shall enable reverse thrust." | **Test 1:** On ground + command reverse thrust -> verify enabled. **Test 2:** In flight + command reverse thrust -> verify NOT enabled (out of scope, but important boundary test). **Test 3:** On ground + no command -> verify reverse thrust not enabled. |

### 8.2 Test Case Derivation Strategy

1. **One requirement, at least one test.** Every EARS
   requirement must be covered by at least one test
   case. If you cannot define a test, the requirement
   is undertestable and needs rewriting.

2. **Test the boundaries.** For every trigger, test the
   boundary conditions. For numerical thresholds, test
   at, above, and below the threshold.

3. **Test state transitions.** For State-Driven
   requirements, test behavior at state entry, during
   the state, and at state exit.

4. **Test the negative path.** For Event-Driven
   requirements, verify the system does NOT perform
   the action when the trigger does NOT occur.

5. **Test error recovery.** For Unwanted Behavior
   requirements, verify both the error response and
   the recovery path back to normal operation.

6. **Test feature absence.** For Optional Feature
   requirements, verify the system behaves correctly
   when the feature is NOT present (no errors, no
   unexpected behavior).

7. **Write requirements and tests simultaneously.**
   Defining test cases during requirement authoring is
   a form of preliminary testing that ensures
   completeness, consistency, and correctness.

---

## 9. EARS and Gherkin: Bridging Requirements and Behavior Specifications

### 9.1 Structural Mapping

EARS and Gherkin (Given/When/Then) share a remarkably
similar structure. The mapping between them is natural
and direct:

| EARS Element | Gherkin Keyword | Purpose |
| --- | --- | --- |
| `While <precondition>` | `Given <initial state>` | Establishes the context or starting state |
| `When <trigger>` | `When <action or event>` | The event or action that triggers the behavior |
| `the <system> shall <response>` | `Then <expected outcome>` | The expected result or system response |
| `Where <feature>` | `Given <feature is enabled>` or Background | Feature presence as a precondition |
| `If <unwanted condition>` | `Given <error condition>` or `When <error occurs>` | The unwanted situation that triggers error handling |
| (additional preconditions) | `And <additional condition>` | Chaining multiple conditions |

### The Key Difference

**EARS** operates at the **requirements** level -- it
states what the system *shall* do. It is a contract
between stakeholders and engineers.

**Gherkin** operates at the **behavior specification**
level -- it describes concrete scenarios with specific
examples that can be automated as tests. It is a
contract between business and development.

EARS says "what must be true." Gherkin says "here is a
specific example proving it is true."

### 9.2 Pattern-by-Pattern Conversion Examples

#### Ubiquitous -> Scenario (invariant check)

**EARS:**

```text
The API shall return responses in JSON format.
```

**Gherkin:**

```gherkin
Feature: API Response Format

  Scenario: GET request returns JSON
    Given the API is running
    When I send a GET request to "/users/1"
    Then the response Content-Type header shall be "application/json"
    And the response body shall be valid JSON

  Scenario: POST request returns JSON
    Given the API is running
    When I send a POST request to "/users" with valid user data
    Then the response Content-Type header shall be "application/json"
    And the response body shall be valid JSON
```

Note: Ubiquitous requirements often generate **multiple
scenarios** because they must be verified across all
operations.

#### Event-Driven -> Scenario (trigger and verify)

**EARS:**

```text
When the user clicks the "Submit Order" button,
the e-commerce system shall create an order record
and redirect to the order confirmation page within
2 seconds.
```

**Gherkin:**

```gherkin
Feature: Order Submission

  Scenario: Successful order submission
    Given I am logged in as a registered customer
    And I have items in my shopping cart
    And I am on the checkout page
    When I click the "Submit Order" button
    Then an order record shall be created in the system
    And I shall be redirected to the order confirmation page
    And the total elapsed time shall be less than 2 seconds
```

#### State-Driven -> Scenario with Given establishing the state

**EARS:**

```text
While the system is in maintenance mode, the system
shall not accept new user logins.
```

**Gherkin:**

```gherkin
Feature: Maintenance Mode Access Control

  Scenario: Login rejected during maintenance mode
    Given the system is in maintenance mode
    When a user attempts to log in with valid credentials
    Then the system shall reject the login attempt
    And the system shall display "System is under maintenance. Please try again later."

  Scenario: Login accepted when maintenance mode ends
    Given the system was in maintenance mode
    And maintenance mode has been deactivated
    When a user attempts to log in with valid credentials
    Then the system shall accept the login attempt
```

#### Unwanted Behavior -> Scenario (negative test)

**EARS:**

```text
If the API rate limit is exceeded, then the system
shall return a 429 status code with a Retry-After
header.
```

**Gherkin:**

```gherkin
Feature: API Rate Limiting

  Scenario: Rate limit exceeded
    Given a client has made 100 API requests in the last minute
    And the rate limit is 100 requests per minute
    When the client sends another API request
    Then the response status code shall be 429
    And the response shall include a "Retry-After" header
    And the "Retry-After" value shall indicate the seconds until the limit resets
```

#### Optional Feature -> Scenario with feature context

**EARS:**

```text
Where the user has two-factor authentication
enabled, the system shall prompt for a verification
code after password entry.
```

**Gherkin:**

```gherkin
Feature: Two-Factor Authentication

  @2fa-enabled
  Scenario: Login with two-factor authentication enabled
    Given the user has two-factor authentication enabled
    And the user is on the login page
    When the user enters valid credentials and clicks "Login"
    Then the system shall display the verification code prompt
    And the system shall not grant access until a valid code is entered

  @2fa-disabled
  Scenario: Login without two-factor authentication
    Given the user does not have two-factor authentication enabled
    And the user is on the login page
    When the user enters valid credentials and clicks "Login"
    Then the system shall grant access and redirect to the dashboard
```

#### Complex -> Scenario with multiple Given/When conditions

**EARS:**

```text
While the aircraft is on ground, when reverse thrust
is commanded, the engine control system shall enable
reverse thrust.
```

**Gherkin:**

```gherkin
Feature: Reverse Thrust Control

  Scenario: Reverse thrust enabled on ground
    Given the aircraft is on the ground
    When the pilot commands reverse thrust
    Then the engine control system shall enable reverse thrust

  Scenario: Reverse thrust not enabled in flight
    Given the aircraft is in flight
    When the pilot commands reverse thrust
    Then the engine control system shall not enable reverse thrust
```

**EARS:**

```text
While the user is authenticated, when the user
requests access to a resource, if the user's role
does not include the required permission, then the
system shall return a 403 Forbidden response and
log the access attempt.
```

**Gherkin:**

```gherkin
Feature: Role-Based Access Control

  Scenario: Unauthorized access to admin resource
    Given the user is authenticated
    And the user has the role "viewer"
    When the user requests access to the admin settings page
    Then the system shall return a 403 Forbidden response
    And the system shall log the access attempt with the user ID, resource, and timestamp

  Scenario: Authorized access to admin resource
    Given the user is authenticated
    And the user has the role "admin"
    When the user requests access to the admin settings page
    Then the system shall return the admin settings page with a 200 status code
```

### 9.3 Complementary Strengths

| Aspect | EARS | Gherkin |
| --- | --- | --- |
| **Purpose** | Define system requirements | Specify testable behavior examples |
| **Audience** | Systems engineers, stakeholders, regulators | Developers, testers, product owners |
| **Abstraction** | Abstract -- states what the system shall do | Concrete -- provides specific examples |
| **Testability** | Implicitly testable through structure | Directly executable as automated tests |
| **Tooling** | No special tools required | Cucumber, SpecFlow, Behave, etc. |
| **Traceability** | Requirement IDs link to design and tests | Scenarios link to step definitions and code |
| **Regulatory** | Satisfies safety standard requirement documentation (ISO 26262, IEC 62304, DO-178C) | Satisfies acceptance test documentation |
| **Scope** | All requirement types (functional, non-functional, safety, performance) | Primarily functional behavior |

### Using Them Together

- **EARS is the "what"** -- the contractual requirement
  that the system must satisfy.
- **Gherkin is the "proof"** -- the concrete examples
  demonstrating that the requirement is satisfied.

For every EARS requirement, one or more Gherkin
scenarios provide the executable acceptance test. The
EARS requirement serves as the parent specification;
the Gherkin scenarios serve as the children that
verify it.

### 9.4 Workflow for Using EARS and Gherkin Together

```text
1. ELICIT stakeholder needs
       |
       v
2. WRITE EARS requirements (using the 5 patterns)
       |
       v
3. REVIEW EARS requirements for completeness
   (peer review)
       |
       v
4. DERIVE Gherkin scenarios from each EARS requirement
   - Map While -> Given
   - Map When -> When
   - Map shall <response> -> Then
   - Add concrete examples with specific data
       |
       v
5. REVIEW Gherkin scenarios with product owners
   and testers
       |
       v
6. IMPLEMENT step definitions
   (Cucumber/SpecFlow/Behave)
       |
       v
7. TRACE: Link each Gherkin scenario back to its
   EARS requirement ID
       |
       v
8. MAINTAIN: When EARS requirements change, update
   the corresponding Gherkin scenarios
```

### Mapping Summary Table

| EARS Pattern | Gherkin Scenario Structure |
| --- | --- |
| **Ubiquitous:** The X shall Y. | Multiple scenarios verifying Y holds across all conditions. Given any state, Then Y. |
| **Event-Driven:** When A, X shall Y. | Given [context]. When A. Then Y. |
| **State-Driven:** While S, X shall Y. | Given S is active. When [any action]. Then Y. Also: Given S is NOT active. Then Y does NOT apply. |
| **Unwanted:** If E, then X shall Y. | Given [setup for E]. When E occurs. Then Y. |
| **Optional:** Where F, X shall Y. | Given F is enabled. [When action.] Then Y. Also: Given F is NOT enabled. Then Y does NOT apply. |
| **Complex:** While S, when A, X shall Y. | Given S. When A. Then Y. |
| **Complex:** While S, when A, if E, then X shall Y. | Given S. When A. And E occurs. Then Y. |

---

## 10. Sources and References

### Primary Sources

- [Alistair Mavin EARS: Official Guide](https://alistairmavin.com/ears/)
  -- The official EARS reference by the creator of EARS
  at Rolls-Royce PLC.

- [Easy Approach to Requirements Syntax (EARS) -- IEEE Xplore](https://ieeexplore.ieee.org/document/5328509/)
  -- The original 2009 academic paper by Mavin,
  Wilkinson, Harwood, and Novak.

- [EARS: The Easy Approach to Requirements Syntax (IARIA Tutorial, Intel)](https://www.iaria.org/conferences2013/filesICCGI13/ICCGI_2013_Tutorial_Terzakis.pdf)
  -- Comprehensive tutorial by George Terzakis at Intel,
  presented at ICCGI 2013.

### Practitioner Guides

- [Adopting EARS Notation for Requirements Engineering -- Jama Software](https://www.jamasoftware.com/requirements-management-guide/writing-requirements/adopting-the-ears-notation-to-improve-requirements-engineering/)
  -- Practical adoption guide with ten benefits of EARS.

- [FAQ about the EARS Notation -- Jama Software](https://www.jamasoftware.com/requirements-management-guide/writing-requirements/frequently-asked-questions-about-the-ears-notation-and-jama-connect-requirements-advisor/)
  -- Frequently asked questions about applying EARS in
  practice.

- [EARS: The Easy Approach to Requirements Syntax -- DEV Community](https://dev.to/sebastian_dingler/ears-the-easy-approach-to-requirements-syntax-39a5)
  -- Developer-oriented guide with software examples.

- [EARS: The Easy Approach to Requirements Syntax -- Medium (ParamTech)](https://medium.com/paramtech/ears-the-easy-approach-to-requirements-syntax-b09597aae31d)
  -- Practical overview with before/after comparisons.

- [EARS Requirements Syntax -- ReqAssist](https://reqassist.com/blog/ears-requirements-syntax)
  -- Implementation guidance with software-focused
  examples.

- [Writing Better Requirements with EARS -- Systems Engineering Trends](https://www.se-trends.de/en/requirements-with-ears/)
  -- German systems engineering perspective on EARS
  adoption.

- [Understanding EARS and How to Better Specify Requirements for AI -- MakerNeo](https://makerneo.com/en/articles/what-is-ears-requirements-syntax-how-to-write-better-ai-prompts.html)
  -- EARS applied to AI prompt engineering and modern
  software.

### Limitations and Edge Cases

- [When Not to Use EARS -- QRA Corp](https://qracorp.com/when-not-to-use-ears/)
  -- Guidance on situations where EARS is not the right
  fit.

- [Adopting EARS Notation for Requirements Specification -- Visure Solutions](https://visuresolutions.com/requirements-management-traceability-guide/adopting-ears-notation-for-requirements-engineering/)
  -- Enterprise requirements management perspective.

### EARS and BDD/Gherkin Integration

- [Easy Approach to Requirements Syntax and the Segue to Behavior Driven Development -- Conduct of Code](https://conductofcode.io/post/easy-approach-to-requirements-syntax-and-the-segue-to-behavior-driven-development/)
  -- Demonstrates direct mapping from EARS requirements
  to SpecFlow/BDD scenarios.

- [BDD/Gherkin Scenarios -- RequireKit](https://requirekit.ai/core-concepts/bdd-scenarios/)
  -- Automated EARS-to-Gherkin conversion tool and
  mapping rules.

- [Translating EARS Requirements to Gherkin Scenarios with AI -- LinkedIn](https://www.linkedin.com/pulse/bridging-gap-translating-ears-requirements-gherkin-ai-menzione-hwxef)
  -- AI-assisted approach to EARS-to-Gherkin
  translation.

- [Bridging the Gap between Requirements Modeling and Behavior-Driven Development -- ResearchGate](https://www.researchgate.net/publication/337527890_Bridging_the_Gap_between_Requirements_Modeling_and_Behavior-Driven_Development)
  -- Academic research on requirements-to-BDD bridging.

### Testing and Traceability

- [An Empirical Investigation of Requirements Engineering and Testing Utilizing EARS Notation in PLC Programs -- Springer](https://link.springer.com/article/10.1007/s42979-025-03843-3)
  -- Empirical study on EARS for embedded/PLC testing.

- [EARS2TF: A Tool for Automated Planning Test from Semi-formalized Requirements -- SEKE 2022](https://ksiresearch.org/seke/seke22paper/paper179.pdf)
  -- Tool for automated test framework generation from
  EARS requirements.

- [EARS Authoring Skill (Claude Code Plugin)](https://playbooks.com/skills/melodic-software/claude-code-plugins/ears-authoring)
  -- EARS validation rules and anti-patterns reference.

### Academic Papers

- [Easy Approach to Requirements Syntax (EARS) -- ResearchGate (PDF)](https://www.researchgate.net/publication/224079416_Easy_approach_to_requirements_syntax_EARS)
  -- Full text of the original RE 09 paper.

- [Easy Approach to Requirements Syntax (EARS) -- Semantic Scholar](https://www.semanticscholar.org/paper/Easy-Approach-to-Requirements-Syntax-(EARS)-Mavin-Wilkinson/b125caf51c17b432010a5b370512695088dad0ce)
  -- Academic references and citation analysis.

- [Adv-EARS: A Formal Requirements Syntax for Derivation of Use Case Models -- Springer](https://link.springer.com/chapter/10.1007/978-3-642-22555-0_5)
  -- Advanced EARS extensions for use case model
  derivation.

### Standards Referenced

- **ISO 26262** -- Road vehicles, Functional safety
  (automotive)
- **IEC 62304** -- Medical device software lifecycle
  processes
- **ISO 13485** -- Medical devices, Quality management
  systems
- **DO-178C** -- Software considerations in airborne
  systems (aerospace)
- **IEC 61508** -- Functional safety of
  electrical/electronic systems
- **IEC 62443** -- Industrial cybersecurity
- **INCOSE Guide for Writing Requirements** -- Systems
  engineering best practices
