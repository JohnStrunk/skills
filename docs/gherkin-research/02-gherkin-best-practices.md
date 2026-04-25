# Gherkin Best Practices: A Comprehensive Guide

A synthesis of best practices from authoritative sources in the BDD community,
including the official Cucumber documentation, Automation Panda (Andy Knight),
the BDD Books series (Seb Rose and Gaspar Nagy), Dan North (creator of BDD),
Matt Wynne (Cucumber co-founder), and John Ferguson Smart.

---

## Table of Contents

1. [Writing Good Scenarios](#1-writing-good-scenarios)
2. [Naming Conventions](#2-naming-conventions)
3. [Anti-Patterns to Avoid](#3-anti-patterns-to-avoid)
4. [Scenario Granularity](#4-scenario-granularity)
5. [Given-When-Then Guidelines](#5-given-when-then-guidelines)
6. [Background Best Practices](#6-background-best-practices)
7. [Scenario Outline Best Practices](#7-scenario-outline-best-practices)
8. [Data Table Best Practices](#8-data-table-best-practices)
9. [Tag Conventions and Strategies](#9-tag-conventions-and-strategies)
10. [Feature File Organization](#10-feature-file-organization)
11. [Ubiquitous Language and Domain Language](#11-ubiquitous-language-and-domain-language)
12. [Collaboration Practices](#12-collaboration-practices)
13. [Common Pitfalls](#13-common-pitfalls)
14. [Sources](#14-sources)

---

## 1. Writing Good Scenarios

### The Golden Rule

> "Write Gherkin so that people who don't know the feature will understand it."
> -- Andy Knight, Automation Panda

A Gherkin scenario should read like a clear, concise story that anyone on the
team -- developer, tester, product owner, or executive -- can understand without
needing to ask questions.

### Declarative vs. Imperative Style

This is the single most important stylistic choice in Gherkin writing. The
Cucumber documentation frames it as: **describe behavior, not implementation**.

**Imperative style (avoid):** Step-by-step UI instructions that specify *how*
the user interacts with the system.

```gherkin
# BAD: Imperative -- tightly coupled to the UI
Scenario: User logs in successfully
  Given I visit "/login"
  When I enter "Bob" in the "user name" field
  And I enter "tester" in the "password" field
  And I press the "login" button
  Then I should see the text "Welcome, Bob"
  And I should see a link labeled "My Account"
```

**Declarative style (prefer):** Higher-level statements describing *what*
happens and *why* it matters.

```gherkin
# GOOD: Declarative -- focused on behavior
Scenario: Registered user can access their account
  Given Bob is a registered user
  When Bob logs in with valid credentials
  Then Bob should see his account dashboard
```

The Cucumber docs advise asking: *"Will this wording need to change if the
implementation does?"* If the answer is yes, the scenario is too imperative.

**Why declarative wins:**

- Remains valid if the UI changes (e.g., login moves from form-based to
  biometric or voice)
- Shorter and easier to read
- Focuses on business value rather than mechanics
- Reduces maintenance burden -- technical details live in step definitions
- Serves as better living documentation

### Clarity and Conciseness

- Each scenario should tell a complete, self-contained story
- Avoid incidental details that distract from the core behavior
- Use concrete, specific examples rather than vague descriptions
- Prefer real-world values over placeholder data when they add clarity

```gherkin
# BAD: Vague and unclear
Scenario: Process a thing
  Given stuff exists
  When I do something
  Then something happens

# BAD: Drowning in irrelevant details
Scenario: User searches for a product
  Given today is December 15, 2024
  And the user is using Chrome version 120
  And the screen resolution is 1920x1080
  And the user has a premium account created on January 3, 2020
  And the product catalog was last updated at 3:47 PM
  When the user searches for "wireless headphones"
  Then 42 results should be displayed

# GOOD: Focused on relevant details only
Scenario: Searching for a product returns matching results
  Given the product catalog contains wireless headphones
  When the user searches for "wireless headphones"
  Then the search results should include wireless headphones
```

---

## 2. Naming Conventions

### Feature Names

- Use a short, descriptive noun phrase that names the capability
- Align with the team's ubiquitous language (the shared vocabulary
  of the domain)
- Name features after business capabilities, not user stories or technical
  components

```gherkin
# BAD: Technical or story-oriented names
Feature: JIRA-4521
Feature: LoginControllerTest
Feature: Sprint 12 acceptance tests

# GOOD: Business capability names
Feature: User Authentication
Feature: Shopping Cart Checkout
Feature: Subscription Management
```

### Scenario Names

- Use a short, descriptive phrase that explains the specific behavior being
  illustrated
- Should be unique within a feature file
- Describe what is being demonstrated, not how

```gherkin
# BAD: Vague or procedural names
Scenario: Test 1
Scenario: It works
Scenario: Click login then enter credentials then see dashboard

# GOOD: Behavior-focused names
Scenario: Registered user logs in with valid credentials
Scenario: Expired subscription prevents access to premium content
Scenario: Empty cart displays a prompt to continue shopping
```

### Tag Names

- Use lowercase with hyphens as separators
- Be consistent across the project
- Use a clear prefix strategy for categorization

```gherkin
# Consistent tag examples
@smoke
@regression
@wip
@slow
@feature-authentication
@priority-high
@sprint-14
```

### File Names

- Use lowercase with underscores or hyphens
- Name files after the feature they contain
- Keep file names concise but descriptive

```text
# Good file names
user_authentication.feature
shopping_cart.feature
subscription-management.feature
```

---

## 3. Anti-Patterns to Avoid

### 3.1 Feature-Coupled Step Definitions

Step definitions organized by feature file rather than by domain concept. This
leads to duplicated code across step definition files.

```text
# BAD: Step definitions coupled to features
steps/
  edit_work_experience_steps.java
  edit_languages_steps.java
  edit_education_steps.java     # All three contain duplicate "I log in" steps

# GOOD: Step definitions organized by domain concept
steps/
  AuthenticationStepDefinitions.java
  EmployeeStepDefinitions.java
  EducationStepDefinitions.java
  ExperienceStepDefinitions.java
```

The Cucumber docs warn: *"This may lead to an explosion of step definitions,
code duplication, and high maintenance costs."*

### 3.2 Conjunction Steps

Steps that use "and" within the step text to combine multiple unrelated actions,
making them impossible to reuse independently.

```gherkin
# BAD: Conjunction step -- not reusable
Given I have shades and a brand new Mustang

# GOOD: Atomic steps -- independently reusable
Given I have shades
And I have a brand new Mustang
```

The principle: *"Strive to keep your steps atomic as much as possible."* Use
Gherkin's built-in `And` and `But` keywords to compose atomic steps.

### 3.3 Procedure-Driven Scenarios

Scenarios written as sequential test scripts rather than behavior illustrations.
They trace through multiple behaviors as step-by-step instructions.

```gherkin
# BAD: Procedure-driven -- multiple behaviors in one scenario
Scenario: Full user journey
  Given the user is on the home page
  When the user clicks "Register"
  And the user fills in the registration form
  And the user submits the form
  Then the user should see a confirmation message
  When the user clicks "Login"
  And the user enters their credentials
  Then the user should see the dashboard
  When the user clicks "Settings"
  And the user changes their password
  Then the user should see a success message
```

This should be three separate scenarios, each covering one behavior.

### 3.4 Testing Implementation Details

Scenarios that reference CSS selectors, database tables, API endpoints, or
specific technology choices.

```gherkin
# BAD: Leaking implementation details
Scenario: Add item to cart
  Given a row exists in the "products" table with id 42
  When I POST to "/api/v2/cart" with body '{"product_id": 42}'
  Then the "cart_items" table should have 1 row
  And the response status should be 201

# GOOD: Behavior-focused
Scenario: Adding a product to the shopping cart
  Given "Wireless Headphones" is available in the store
  When the customer adds "Wireless Headphones" to their cart
  Then the cart should contain "Wireless Headphones"
```

### 3.5 Over-Specification

Including details that are irrelevant to the behavior being tested, making
scenarios fragile and hard to understand.

```gherkin
# BAD: Over-specified
Scenario: User receives a welcome email
  Given a user named "John Smith" with email "john@example.com"
  And the user was born on "1985-03-15"
  And the user lives at "123 Main St, Springfield, IL 62701"
  And the user's phone number is "555-0123"
  When the user registers
  Then an email should be sent to "john@example.com"
  And the subject should be "Welcome to Our Platform, John!"
  And the email body should contain "Dear John Smith"

# GOOD: Only relevant details
Scenario: New user receives a welcome email after registration
  Given a new user with email "john@example.com"
  When the user completes registration
  Then a welcome email should be sent to "john@example.com"
```

---

## 4. Scenario Granularity

### One Scenario, One Behavior

This is what Automation Panda calls **"The Cardinal Rule of BDD"**:

> "One Scenario, One Behavior!"

Each scenario should cover a single, independently testable behavior. It should
have exactly one `When`-`Then` pair (though each may have multiple `And`/`But`
continuations).

```gherkin
# BAD: Multiple behaviors in one scenario
Scenario: User account management
  Given a registered user
  When the user logs in
  Then the dashboard is displayed
  When the user changes their email
  Then a confirmation email is sent
  When the user logs out
  Then the login page is displayed

# GOOD: Each behavior is its own scenario
Scenario: Registered user can log in
  Given a registered user
  When the user logs in with valid credentials
  Then the dashboard is displayed

Scenario: User can update their email address
  Given a logged-in user
  When the user changes their email address
  Then a confirmation email is sent to the new address

Scenario: User can log out
  Given a logged-in user
  When the user logs out
  Then the login page is displayed
```

### How Many Steps?

- **Target:** Fewer than 10 steps per scenario (ideally 3-5)
- **Maximum:** If a scenario exceeds 10 steps, it likely covers too much or is
  too imperative
- **Minimum:** A 3-step Given-When-Then is often the ideal scenario

If a scenario feels too long, check whether:

1. It covers multiple behaviors (split it)
2. It uses imperative style where declarative would suffice (raise the
   abstraction level)
3. Setup steps belong in a `Background` section (extract them)
4. Details can be hidden in step definitions (move them down)

### How Many Scenarios Per Feature?

- **Target:** Approximately a dozen scenarios per feature file
- A feature with only 1-2 scenarios may be too fine-grained
- A feature with 30+ scenarios likely needs to be split into multiple features
  or reorganized around more specific business rules

---

## 5. Given-When-Then Guidelines

### Given: Establish Context

Givens describe the **initial state** of the system before the behavior occurs.
They are preconditions, not actions.

**Guidelines:**

- Describe state, not user interaction
- Use past tense or present state descriptions
- Set up only the context that is relevant to this specific scenario
- Multiple Givens are fine when joined with `And`/`But`

```gherkin
# BAD: Givens that describe actions
Given the user navigates to the login page
Given the user clicks the "Premium" button

# GOOD: Givens that describe state
Given the user has a premium subscription
Given the product catalog contains 50 items
Given the user is logged in
```

### When: Perform the Action

Whens describe the **event or action** that triggers the behavior being
specified. This is the thing being tested.

**Guidelines:**

- There should be a **single When** per scenario (with `And` continuations if
  the action has multiple parts that form one logical event)
- Describe what happens, not how
- Avoid technology-specific interaction details
- The When is the pivot point -- everything before sets the stage, everything
  after checks the result

```gherkin
# BAD: Technology-specific When
When I click the button with id "submit-order"
When I send a POST request to /api/orders

# GOOD: Behavior-focused When
When the customer places an order
When the user submits the search query
```

### Then: Verify the Outcome

Thens describe the **expected outcome** -- the observable result of the action.

**Guidelines:**

- Verify observable outputs, not internal state
- An outcome should be something a user or external system can see
- Avoid checking implementation details (database state, internal variables)
- Multiple Thens are acceptable for verifying different aspects of the same
  outcome

```gherkin
# BAD: Checking internal implementation
Then the database should have a new row in the orders table
Then the OrderService.processOrder() method should have been called

# GOOD: Checking observable outcomes
Then the customer should receive an order confirmation
Then the order should appear in the customer's order history
And the inventory for the purchased item should be reduced
```

### Step Order Rules

Steps must appear in the correct order: **Given -> When -> Then**

- No `Given` after a `When` or `Then`
- No `When` after a `Then`
- `And` and `But` inherit the type of the preceding step
- If you find yourself needing a second `When` after a `Then`, you have two
  scenarios

### The `*` (Asterisk) Keyword

Gherkin supports `*` as a generic step keyword. It is useful for lists where
Given/When/Then feels forced:

```gherkin
Scenario: User selects multiple items
  Given the catalog is displayed
  * the user selects "Item A"
  * the user selects "Item B"
  * the user selects "Item C"
  When the user views the selection
  Then all three items should be listed
```

---

## 6. Background Best Practices

### What Background Is For

A `Background` section runs before each scenario in a feature file. It exists to
reduce repetition of common `Given` steps.

### When to Use Background

- When **every** scenario in the file shares the same setup steps
- When the background steps provide essential context for understanding each
  scenario
- When extracting shared setup makes each scenario shorter and more focused

### When NOT to Use Background

- When only some scenarios need the setup (use individual Givens instead)
- When it contains more than 4-5 lines (too much shared state obscures meaning)
- When it includes `When` or `Then` steps (Background is for
  Givens only)
- When it sets up state that not all scenarios need (incidental
  details for some)

### Keep It Short

```gherkin
# BAD: Background is too long and detailed
Background:
  Given the application is running
  And the database has been seeded with test data
  And the user "Alice" exists with email "alice@example.com"
  And the user "Alice" has a verified account
  And the user "Alice" has a premium subscription
  And the subscription started on "2024-01-01"
  And the subscription expires on "2025-01-01"
  And the user "Alice" is logged in
  And the user "Alice" has 3 items in their cart

# GOOD: Background is brief and universally needed
Background:
  Given Alice has an active premium subscription
  And Alice is logged in
```

### Background Must Be Visible

The Background should be so short and clear that readers can hold it in their
head while reading any scenario in the file. If a reader has to keep scrolling
back to the Background to understand a scenario, the Background is too complex.

```gherkin
# GOOD: Background + Scenario read together naturally
Feature: Premium Content Access

  Background:
    Given a user with a premium subscription

  Scenario: Premium user can view exclusive articles
    When the user opens an exclusive article
    Then the full article content is displayed

  Scenario: Premium user can download reports
    When the user downloads a quarterly report
    Then the report is saved to their downloads
```

---

## 7. Scenario Outline Best Practices

### When to Use Scenario Outlines

Scenario Outlines (also called Scenario Templates) run the same scenario
multiple times with different data. Use them when:

- Multiple examples illustrate the **same behavior** with different inputs
- You need to cover several **equivalence classes** of the same rule
- The scenario structure is identical, only the data varies

### When NOT to Use Scenario Outlines

- When different rows actually represent **different behaviors** (use separate
  scenarios)
- When the outline has only one example row (use a plain Scenario)
- When the table has many columns, making the template unreadable
- When combining unrelated test cases just because they share a similar
  structure

### Good Outline Practices

```gherkin
# GOOD: Each row represents a meaningful equivalence class
Scenario Outline: Password validation enforces minimum requirements
  Given the user is creating an account
  When the user enters a password "<password>"
  Then the system should display "<result>"

  Examples:
    | password       | result                          |
    | ab             | Password must be at least 8 characters |
    | abcdefgh       | Password accepted               |
    | Abcdefgh1!     | Password accepted               |

# GOOD: Using named Examples blocks for clarity
Scenario Outline: Shipping cost depends on order total
  Given the customer has items totaling <total> in their cart
  When the customer proceeds to checkout
  Then the shipping cost should be <shipping>

  Examples: Free shipping threshold
    | total  | shipping |
    | 100.00 | 0.00     |
    | 250.00 | 0.00     |

  Examples: Standard shipping
    | total | shipping |
    | 25.00 | 5.99     |
    | 49.99 | 5.99     |
```

### Avoid Outline Overuse

```gherkin
# BAD: Rows represent fundamentally different behaviors
Scenario Outline: User actions
  Given a <user_type> user
  When the user <action>
  Then <outcome>

  Examples:
    | user_type | action              | outcome                    |
    | admin     | deletes a user      | user is removed            |
    | guest     | views the home page | public content is shown    |
    | banned    | tries to log in     | access denied message shown|

# These are three different behaviors and should be three separate scenarios.
```

### Keep Examples Tables Focused

- Each row should represent a **distinct equivalence class**, not a redundant
  variation
- Ask: does each row genuinely test a different aspect of the rule?
- Consider whether some data can be hidden in step definitions rather than
  parameterized
- Split outlines if different columns represent different behaviors

---

## 8. Data Table Best Practices

### When to Use Data Tables

Data Tables pass structured data to a single step. Use them for:

- Providing a list of items to a step
- Specifying object properties compactly
- Setting up multiple entities at once

```gherkin
# GOOD: Data table for setting up multiple entities
Given the following products exist:
  | name                | price  | category    |
  | Wireless Headphones | 79.99  | Electronics |
  | Running Shoes       | 129.99 | Sports      |
  | Coffee Maker        | 49.99  | Kitchen     |

# GOOD: Data table for specifying properties
When the user creates an account with:
  | first name | Alice              |
  | last name  | Smith              |
  | email      | alice@example.com  |
```

### Formatting Guidelines

- Align the pipe characters vertically for readability
- Use a header row when the table has named columns
- Keep column count manageable (3-5 columns maximum)
- Only include columns relevant to the behavior being tested
- Use clear, descriptive header names

```gherkin
# BAD: Too many columns, hard to read
Given the following users:
  | name  | email           | phone      | address        | city       | state | zip   | country | role  | status |
  | Alice | alice@test.com  | 555-0001   | 123 Main St    | Springfield| IL    | 62701 | US      | admin | active |

# GOOD: Only include what matters for this scenario
Given the following users:
  | name  | role  | status |
  | Alice | admin | active |
  | Bob   | user  | active |
```

### Data Tables vs. Scenario Outlines

These serve different purposes:

- **Data Tables** pass multiple data items into a **single step** within one
  scenario execution
- **Scenario Outlines** run the **entire scenario** multiple times with
  different values

```gherkin
# Data Table: Sets up context within ONE scenario run
Given the shopping cart contains:
  | product            | quantity |
  | Wireless Headphones| 1        |
  | USB Cable          | 2        |

# Scenario Outline: Runs the FULL scenario multiple times
Scenario Outline: Discount rules based on quantity
  Given the customer orders <quantity> units
  When the order is processed
  Then a <discount>% discount is applied

  Examples:
    | quantity | discount |
    | 10       | 5        |
    | 50       | 10       |
    | 100      | 15       |
```

---

## 9. Tag Conventions and Strategies

### Tag Purposes

Tags in Gherkin serve several organizational functions:

1. **Filtering test execution** (run only `@smoke` tests)
2. **Categorizing by type** (`@functional`, `@performance`, `@security`)
3. **Marking work status** (`@wip`, `@pending`, `@deprecated`)
4. **Linking to external systems** (`@JIRA-1234`, `@story-456`)
5. **Controlling test infrastructure** (`@requires-database`, `@slow`)
6. **Cross-cutting concerns** that don't fit the directory hierarchy

### Naming Conventions

```gherkin
# Use lowercase with hyphens
@smoke
@regression
@wip

# Use prefixed categories for clarity
@priority-high
@priority-low
@feature-authentication
@feature-checkout
@layer-api
@layer-ui

# Link to external tracking
@jira-PROJ-1234
@story-user-login
```

### Tag Inheritance

Tags on a `Feature` are inherited by all scenarios within it. Tags on a `Rule`
are inherited by all scenarios within that rule. Use this to avoid repetition:

```gherkin
@authentication
Feature: User Login

  @smoke
  Scenario: Valid login
    ...

  @regression
  Scenario: Login with expired password
    ...

  # Both scenarios inherit @authentication
  # "Valid login" has both @authentication and @smoke
```

### Tag Strategy Guidelines

- Keep the tag vocabulary small and documented -- avoid tag proliferation
- Define team conventions for tag naming and update them in project
  documentation
- Do not use tags as a substitute for proper feature file organization
- Avoid tags that duplicate information already in the directory structure
- Use tags for cross-cutting concerns that span multiple features

---

## 10. Feature File Organization

### One Feature Per File

Each `.feature` file should contain exactly one `Feature`. This keeps files
focused, discoverable, and manageable.

### Directory Structure

Organize feature files by **business capability and domain area**, not by
technical layers or sprint numbers.

```text
# BAD: Organized by technical layer or sprint
features/
  api/
  ui/
  database/
  sprint-12/
  sprint-13/

# GOOD: Organized by business domain
features/
  authentication/
    user_login.feature
    password_reset.feature
    two_factor_authentication.feature
  shopping/
    product_search.feature
    shopping_cart.feature
    checkout.feature
  account/
    profile_management.feature
    subscription.feature
    notification_preferences.feature
```

The Cucumber community recommends a hierarchy where:

- Higher-level folders represent broad business capabilities
- Deeper nested folders contain increasingly specific behaviors
- The structure allows "zoom-in/zoom-out" navigation: executives find overviews
  near the root; detailed behaviors are deeper

### Features vs. User Stories

A critical distinction from the Cucumber blog: **do not create a new feature
file for each user story**. User stories are small delivery increments, while
features document persistent system behaviors. A single story may touch
multiple features, and a feature may be built across multiple stories. Feature
files should reflect the enduring structure of the product, not the cadence of
delivery.

### File Naming

- Use lowercase with underscores or hyphens: `user_login.feature`
- Name the file after the feature or capability it describes
- Keep file names concise but descriptive enough to identify the content

---

## 11. Ubiquitous Language and Domain Language

### Write From the User's Perspective

Scenarios should use the language of the business domain, not the language of
the development team.

```gherkin
# BAD: Developer language
Scenario: OrderService creates Order entity
  Given an OrderDTO with valid fields
  When OrderService.createOrder() is invoked
  Then the OrderRepository should persist a new Order entity
  And an OrderCreatedEvent should be published to the message bus

# GOOD: Domain language
Scenario: Customer places an order
  Given a customer has items in their shopping cart
  When the customer places the order
  Then the order should be confirmed
  And the customer should receive a confirmation notification
```

### Build a Shared Vocabulary

The concept of "ubiquitous language" comes from Domain-Driven Design (Eric
Evans). In BDD, this means:

- The same terms should be used in conversations, Gherkin files, and code
- If the business says "customer," the Gherkin says "customer" (not "user,"
  "client," or "account holder" -- unless those are genuinely
  different concepts)
- When a new domain term emerges, update all layers to use it consistently
- Glossaries or domain dictionaries can help maintain consistency across large
  teams

### Avoid Technical Jargon

```gherkin
# BAD: Technical jargon
Given a GET request to /api/products returns a 200 status
When the JSON response is parsed
Then the "items" array should contain 5 elements

# GOOD: Domain language
Given the store has 5 products available
When the customer browses the product catalog
Then 5 products should be displayed
```

### Person and Tense

- Write steps in **third person** for consistency
- Use **present tense** throughout
- Use named personas to add clarity when multiple actors are involved

```gherkin
# BAD: Mixed perspective and tense
Given I logged in yesterday
When I will click the button
Then the system showed me results

# GOOD: Consistent third-person present tense
Given the customer is logged in
When the customer searches for "headphones"
Then the search results are displayed
```

---

## 12. Collaboration Practices

### BDD Is Not a Testing Practice

BDD is fundamentally a **collaboration practice**. Dan North created it to
improve communication between developers, testers, and business stakeholders.
The Gherkin scenarios are a byproduct of that collaboration, not the primary
goal.

The Cucumber team describes three core practices:

1. **Discovery** -- exploring possibilities through structured conversation
2. **Formulation** -- documenting expectations as executable specifications
3. **Automation** -- implementing tests from those specifications

### Three Amigos

The Three Amigos workshop brings together three perspectives (not necessarily
three people -- 3-6 is ideal):

- **Someone to request** (product owner / business analyst) -- explains the
  user need and business rules
- **Someone to suggest** (developer) -- proposes solutions, asks "what if"
  questions
- **Someone to protest** (tester) -- challenges assumptions, identifies edge
  cases, spots ambiguities

**Best practices for Three Amigos sessions:**

- Hold sessions **shortly before work begins** on a feature (within 1-2 weeks)
- Time-box to **30-45 minutes** -- if sessions run longer, the feature needs
  decomposition
- Allow 24 hours before the meeting for participants to review and think
  creatively
- **Do not write Gherkin during the session** -- experienced teams capture
  examples in rough form, then a pair of amigos writes the formal Gherkin
  afterward
- Focus on building shared understanding, not on syntax

### Example Mapping

Example Mapping (created by Matt Wynne) is a lightweight discovery technique
using colored index cards:

| Card Color | Represents                                    |
|------------|-----------------------------------------------|
| **Yellow** | The user story being discussed                |
| **Blue**   | Rules / acceptance criteria                   |
| **Green**  | Concrete examples that illustrate each rule   |
| **Red**    | Questions the team cannot yet answer          |

**The process:**

1. Place the story (yellow card) at the top
2. Add known rules (blue cards) beneath the story
3. Place concrete examples (green cards) under their corresponding rules
4. Capture unanswered questions (red cards) as they arise
5. Continue until scope is clear or the time-box expires (~25 minutes)

**Key insight:** Examples at this stage are rough and conversational, not formal
Gherkin. A good example name is something like "The one where the customer
forgot his receipt." The formulation into Given-When-Then happens after the
session.

**Signals from the visual layout:**

- Too many blue cards? The story is too big -- split it
- Too many red cards? More research is needed before development
- A rule has no green cards? The team does not understand it yet

### From Examples to Gherkin

The flow from collaboration to specification is:

1. **Discovery session** (Three Amigos / Example Mapping) produces rough
   examples and rules
2. A **pair from the team** (typically developer + tester) formulates examples
   into Gherkin scenarios
3. The **product owner reviews** the Gherkin to confirm it captures the intent
4. The scenarios become **living documentation** that stays in sync with the
   code

---

## 13. Common Pitfalls

### 13.1 Bolting Gherkin onto Existing Test Scripts

Adding BDD keywords to traditional procedure-driven test scripts without
changing the underlying thinking. The result is imperative, brittle scenarios
that provide none of the communication benefits of BDD.

```gherkin
# BAD: An existing test script with Gherkin keywords slapped on
Scenario: Verify login functionality
  Given I open the browser
  And I navigate to "https://app.example.com"
  And I wait for the page to load
  When I find the element with id "username"
  And I type "testuser01" into the element
  And I find the element with id "password"
  And I type "P@ssw0rd!" into the element
  And I click the element with id "login-btn"
  And I wait 3 seconds
  Then the element with id "welcome-msg" should contain "Welcome"
```

### 13.2 Incidental Details

Including data or context that is irrelevant to the behavior being tested.
Incidental details obscure the intent and make scenarios fragile.

```gherkin
# BAD: Full of incidental details
Scenario: Customer receives loyalty points
  Given a customer named "Jane Doe" born on "1990-05-15"
  And the customer has email "jane@example.com"
  And the customer's phone is "555-0199"
  And the customer has been a member since "2020-01-01"
  And the customer lives at "456 Oak Ave, Portland, OR"
  When the customer makes a purchase of $50.00
  Then the customer should receive 50 loyalty points

# GOOD: Only relevant details
Scenario: Customer earns one loyalty point per dollar spent
  Given a loyalty program member
  When the member makes a purchase of $50.00
  Then the member should earn 50 loyalty points
```

### 13.3 Fragile Scenarios

Scenarios that break whenever the implementation changes, even if the behavior
remains the same. This usually results from imperative style, UI coupling, or
hard-coded values.

**Causes of fragility:**

- Referencing specific UI elements (button text, field labels, page titles)
- Hard-coding test data that depends on external systems
- Specifying exact error messages rather than error categories
- Coupling to specific URLs, API paths, or database structures

### 13.4 Missing the "Why"

Feature descriptions and scenario names that fail to communicate the business
value or purpose of the behavior.

```gherkin
# BAD: No context for why this matters
Feature: FR-042

  Scenario: Test case 1
    Given condition A
    When action B
    Then result C

# GOOD: Clear business context
Feature: Loyalty Points Program
  Customers earn loyalty points on purchases to encourage
  repeat business and reward long-term customers.

  Scenario: Customer earns points proportional to purchase amount
    Given an enrolled loyalty member
    When the member completes a $75 purchase
    Then the member should earn 75 loyalty points
```

### 13.5 Too Many Scenarios

Writing exhaustive scenario lists that attempt to cover every edge case,
boundary condition, and permutation. Gherkin is for **illustrating rules with
key examples**, not for exhaustive test coverage. Detailed edge-case testing is
better handled at the unit or integration test level.

### 13.6 Unused Step Definitions

Creating step definitions speculatively before scenarios need
them. The Cucumber docs advise: *"Only implement steps you
actually use."* Unused definitions become "cruft that will need
to be cleaned up later."

### 13.7 Not Involving the Whole Team

Writing Gherkin in isolation -- either by developers who use technical language,
or by testers who write procedural scripts, or by product owners who write
incomplete specs. Gherkin works best as a collaboration artifact owned by the
whole team.

---

## 14. Sources

The guidance in this document is synthesized from the following authoritative
sources:

- **Cucumber Official Documentation** --
  [cucumber.io/docs](https://cucumber.io/docs/)
  - Gherkin Reference
  - Better Gherkin
  - BDD Practices
  - Anti-Patterns
  - Step Organization
  - Feature File Organization
- **Automation Panda (Andy Knight)** --
  [automationpanda.com](https://automationpanda.com/bdd/)
  - "BDD 101: Writing Good Gherkin"
  - "BDD 101: The Gherkin Language"
- **BDD Books (Seb Rose and Gaspar Nagy)** --
  [bddbooks.com](https://www.bddbooks.com/)
  - *Discovery: Explore Behaviour Using Examples*
  - *Formulation: Document Examples with Given/When/Then*
- **Dan North** -- Creator of BDD
  - "Introducing BDD" -- [dannorth.net](https://dannorth.net/)
- **Matt Wynne** -- Cucumber co-founder
  - "Example Mapping: Introduction" -- Cucumber Blog
- **John Ferguson Smart** -- BDD practitioner and author
  - "Three Amigos: Requirements Discovery"
  - *BDD in Action* (Manning)
