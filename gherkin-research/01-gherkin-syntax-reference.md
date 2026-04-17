# Gherkin Syntax Reference

A comprehensive reference for the Gherkin language used by Cucumber
and other BDD (Behavior-Driven Development) frameworks. This document
covers every keyword, syntax construct, and convention needed to write
and generate well-formed `.feature` files.

---

## Table of Contents

1. [Overview](#1-overview)
2. [Feature File Structure](#2-feature-file-structure)
3. [Keywords at a Glance](#3-keywords-at-a-glance)
4. [Feature](#4-feature)
5. [Rule (Gherkin 6+)](#5-rule-gherkin-6)
6. [Background](#6-background)
7. [Scenario / Example](#7-scenario--example)
8. [Steps: Given / When / Then / And / But / *](#8-steps-given--when--then--and--but--)
9. [Scenario Outline / Scenario Template](#9-scenario-outline--scenario-template)
10. [Examples Tables](#10-examples-tables)
11. [Data Tables](#11-data-tables)
12. [Data Tables vs. Examples Tables](#12-data-tables-vs-examples-tables)
13. [Doc Strings](#13-doc-strings)
14. [Tags](#14-tags)
15. [Comments](#15-comments)
16. [Descriptions](#16-descriptions)
17. [Localization (i18n)](#17-localization-i18n)
18. [Formal Grammar](#18-formal-grammar)
19. [Indentation and Formatting Conventions](#19-indentation-and-formatting-conventions)
20. [Best Practices for Writing Gherkin](#20-best-practices-for-writing-gherkin)

---

## 1. Overview

Gherkin is a plain-text, line-oriented language for describing software behavior
without specifying implementation details. It serves three purposes:

- **Living documentation** -- human-readable specifications that stay in sync
  with the code.
- **Automated tests** -- each scenario maps to executable step definitions in
  a programming language.
- **Collaboration tool** -- a shared language between developers, testers, and
  business stakeholders.

Gherkin files use the `.feature` extension. Each file describes a single feature
of the system and contains one or more scenarios that illustrate how the feature
behaves.

The Gherkin parser (used by Cucumber, Behave, SpecFlow, pytest-bdd, godog,
and others) reads `.feature` files, builds an Abstract Syntax Tree (AST), and
compiles it into "Pickles" -- simplified, execution-ready data structures.

---

## 2. Feature File Structure

A `.feature` file has a well-defined hierarchical structure:

```text
GherkinDocument
  └── Feature
        ├── description (free-form text)
        ├── Background (optional, at most one)
        ├── Scenario* (zero or more)
        ├── Scenario Outline* (zero or more)
        └── Rule* (zero or more, Gherkin 6+)
              ├── description
              ├── Background (optional, at most one)
              ├── Scenario*
              └── Scenario Outline*
```

### Minimal example

```gherkin
Feature: User login

  Scenario: Successful login with valid credentials
    Given the user is on the login page
    When the user enters valid credentials
    Then the user is redirected to the dashboard
```

### Full-featured example

```gherkin
# language: en
@authentication
Feature: User login
  Users must be able to log in to access their account.
  The system supports email/password and SSO authentication.

  Background:
    Given the application is running
    And the user database is seeded

  @happy-path @smoke
  Scenario: Successful login with valid credentials
    Given the user "alice@example.com" exists with password "s3cret"
    When the user logs in with email "alice@example.com" and password "s3cret"
    Then the user should see the dashboard
    And the greeting should say "Welcome, Alice"

  @error-handling
  Scenario: Login fails with wrong password
    Given the user "alice@example.com" exists with password "s3cret"
    When the user logs in with email "alice@example.com" and password "wrong"
    Then the user should see the error "Invalid credentials"

  @edge-case
  Rule: Account lockout after repeated failures

    Background:
      Given the user "bob@example.com" exists with password "p@ssw0rd"

    Scenario: Account locks after 5 failed attempts
      Given the user has failed to log in 4 times
      When the user fails to log in a 5th time
      Then the account should be locked
      And the user should see "Account locked. Try again in 30 minutes."

    Scenario: Successful login resets the failure counter
      Given the user has failed to log in 3 times
      When the user logs in with the correct password
      Then the failure counter should be reset to 0
```

---

## 3. Keywords at a Glance

Gherkin has two categories of keywords:

### Keywords followed by a colon (`:`)

These are structural keywords that define sections of the feature file.

| Primary Keyword    | Synonym(s)                         | Purpose                                    |
|--------------------|------------------------------------|--------------------------------------------|
| `Feature`          | `Business Need`, `Ability`         | Top-level container; one per file          |
| `Rule`             | *(none)*                           | Groups scenarios under a business rule     |
| `Background`       | *(none)*                           | Shared preconditions for sibling scenarios |
| `Scenario`         | `Example`                          | A single concrete test case                |
| `Scenario Outline` | `Scenario Template`                | A parameterized scenario template          |
| `Examples`         | `Scenarios`                        | Data table for Scenario Outline parameters |

### Keywords NOT followed by a colon

These are step keywords that begin individual steps within a scenario.

| Keyword | Purpose                                                    |
|---------|------------------------------------------------------------|
| `Given` | Establishes initial context / preconditions                |
| `When`  | Describes the action or event under test                   |
| `Then`  | Specifies the expected outcome / observable result         |
| `And`   | Continues the previous step type (Given, When, or Then)    |
| `But`   | Continues previous step type with a contrasting clause     |
| `*`     | Wildcard; replaces any step keyword for bullet-point use   |

> **Important:** Keywords are followed by a single space before the step text.
> The parser does not distinguish between step types when matching step
> definitions -- `Given foo` and `When foo` match the same definition.
> The keywords exist solely for human readability.

---

## 4. Feature

The `Feature` keyword is **required** and must be the first keyword in the file
(after any language header or comments). Each `.feature` file contains exactly
one `Feature`.

### Syntax

```gherkin
Feature: <title>
  <optional multi-line description>

  <Background, Scenario, Scenario Outline, or Rule blocks>
```

### Synonyms

The following keywords are synonyms and can be used interchangeably:

- `Feature`
- `Business Need`
- `Ability`

### Purpose

- Names the feature under test.
- Provides a place for a free-form description (often user-story format).
- Acts as the top-level grouping for all scenarios in the file.
- Can carry tags that are inherited by all child elements.

### Examples

```gherkin
Feature: Shopping cart
  As a customer
  I want to manage items in my shopping cart
  So that I can purchase what I need
```

```gherkin
Business Need: Inventory management
  Warehouse staff need real-time visibility into stock levels.
```

```gherkin
Ability: Search products
  Users can search the product catalog by name, category, or SKU.
```

---

## 5. Rule (Gherkin 6+)

The `Rule` keyword was introduced in Gherkin 6 to group related scenarios
under a named business rule within a feature. Rules provide an additional
layer of organization between `Feature` and `Scenario`.

### Syntax (Rule)

```gherkin
Rule: <title>
  <optional description>

  Background:
    <steps>

  Scenario: <title>
    <steps>
```

### Key properties (Rule)

- A `Feature` can contain zero or more `Rule` blocks.
- Each `Rule` can have its own `Background` (at most one).
- Each `Rule` can contain multiple `Scenario` and `Scenario Outline` blocks.
- Tags on a `Rule` are inherited by all its child scenarios.
- Rules cannot be nested inside other rules.

### Example (Rule)

```gherkin
Feature: Highlander

  Rule: There can be only One

    Example: Only One -- More than one alive
      Given there are 3 ninjas
      And there are more than one ninja alive
      When 2 ninjas meet, they will fight
      Then one ninja dies (but not me)
      And there is one ninja less alive

    Example: Only One -- One alive
      Given there is only 1 ninja alive
      Then they will live forever ;-)

  Rule: There can be Two (in some cases)

    Example: Two -- Dead and Reborn as Phoenix
      Given there are 2 ninjas
      And one of them is a Phoenix
      When they fight
      Then the Phoenix is reborn
      And there are still 2 ninjas alive
```

### Background inside a Rule

```gherkin
Feature: Overdue tasks
  Let users know when tasks are overdue, even when using other
  features of the app

  Rule: Users are notified about overdue tasks on first use of the day

    Background:
      Given I have overdue tasks

    Example: First use of the day
      Given I last used the app yesterday
      When I use the app
      Then I am notified about overdue tasks

    Example: Already used today
      Given I last used the app earlier today
      When I use the app
      Then I am not notified about overdue tasks
```

---

## 6. Background

The `Background` keyword defines a set of steps that run
**before each scenario** in the same scope (Feature or Rule).
It factors out repeated `Given` steps.

### Syntax (Background)

```gherkin
Background:
  <optional title>
  <optional description>
  Given <step>
  And <step>
  ...
```

### Rules for Background

1. **At most one** `Background` per `Feature` or `Rule`.
2. A `Background` at the `Feature` level runs before every scenario in the
   entire feature (unless those scenarios are inside a `Rule` that has its own
   `Background` -- but note: the Feature-level Background still runs first,
   followed by the Rule-level Background).
3. A `Background` at the `Rule` level runs before every scenario in that rule.
4. `Background` runs **after** any `Before` hooks and **before** each scenario's
   own steps.
5. `Background` should contain only `Given` steps (preconditions). While the
   parser does not enforce this, using `When` or `Then` in a Background is
   strongly discouraged and considered bad practice.
6. **Tags cannot be placed on a `Background`.**
7. The Background must appear **before** the first `Scenario` or
   `Scenario Outline` in its scope.

### Example (Background)

```gherkin
Feature: Multiple site support
  Only blog owners can post to a blog, except administrators,
  who can post to all blogs.

  Background:
    Given a global administrator named "Greg"
    And a blog named "Greg's anti-tax rants"
    And a customer named "Dr. Bill"
    And a blog named "Expensive Therapy" owned by "Dr. Bill"

  Scenario: Dr. Bill posts to his own blog
    Given I am logged in as Dr. Bill
    When I try to post to "Expensive Therapy"
    Then I should see "Your article was published."

  Scenario: Dr. Bill tries to post to somebody else's blog, and fails
    Given I am logged in as Dr. Bill
    When I try to post to "Greg's anti-tax rants"
    Then I should see "Hey! That's not your blog!"

  Scenario: Greg posts to a client's blog
    Given I am logged in as Greg
    When I try to post to "Expensive Therapy"
    Then I should see "Your article was published."
```

### Tips

- Keep Backgrounds short -- ideally under 4 steps.
- Do not include steps that are only relevant to some scenarios; move those
  into the scenarios themselves.
- If a `Background` grows large, consider whether the feature file should be
  split into multiple files.
- Use a descriptive title (after `Background:`) when the setup might not be
  obvious.

---

## 7. Scenario / Example

A `Scenario` (or its synonym `Example`) describes a single concrete example
of a system behavior. It is the primary unit of testing in Gherkin.

### Syntax (Scenario)

```gherkin
Scenario: <title>
  <optional description>
  Given <precondition>
  When <action>
  Then <expected result>
```

### Synonyms (Scenario)

`Scenario` and `Example` are interchangeable:

```gherkin
Example: User sees welcome message
  Given the user is logged in
  When the user visits the home page
  Then the user sees "Welcome back!"
```

### Key properties (Scenario)

- Each scenario is **independent** -- it should not depend on the
  outcome of another scenario.
- A scenario consists of a sequence of steps
  (Given/When/Then/And/But/*).
- A scenario can carry tags.
- A scenario can have a multi-line description between the
  title and the first step.

### Example with all elements

```gherkin
@billing @critical
Scenario: Charge customer for subscription renewal
  When a subscription period ends, the system should automatically
  charge the customer's payment method on file.

  Given the customer "Jane" has an active subscription
  And the subscription renewal date is today
  And the customer has a valid credit card on file
  When the subscription renewal job runs
  Then the credit card should be charged $9.99
  And the customer should receive a renewal confirmation email
  But the customer should not receive a payment failure notice
```

---

## 8. Steps: Given / When / Then / And / But / *

Steps are the individual lines within a scenario that describe context, actions,
and outcomes.

### Given -- Establish context

`Given` steps describe the system's initial state before the behavior under
test occurs. They set up preconditions.

```gherkin
Given the user "Alice" is registered
Given the shopping cart contains 3 items
Given today is "2024-01-15"
```

Think of `Given` as "the system is in this state." Use past tense or present
tense to describe an existing condition.

### When -- Describe the action

`When` steps describe the action or event that triggers the behavior under test.
There should typically be **one** `When` block per scenario (one behavior per
scenario).

```gherkin
When the user clicks the "Submit" button
When the daily batch job runs
When the API receives a POST request to "/orders"
```

### Then -- Assert the outcome

`Then` steps describe the expected observable outcome. They should describe
something that can be **verified** -- an output, a side effect, a state change.

```gherkin
Then the order status should be "confirmed"
Then the user should receive an email
Then the response status code should be 201
```

### And / But -- Continue the previous keyword

`And` and `But` repeat the meaning of the preceding step keyword. They exist
purely for readability.

```gherkin
Scenario: Register a new user
  Given the registration form is displayed
  And the user has not registered before       # same as Given
  When the user fills in valid details
  And the user clicks "Register"               # same as When
  Then a confirmation email is sent
  And the user appears in the user database    # same as Then
  But the user's account is not yet activated  # same as Then (contrasting)
```

`And` and `But` are semantically identical. Use `But` when the step expresses
a contrasting or negative condition for improved readability:

```gherkin
Then the order should be created
But the inventory should not be decremented yet
```

### * (Asterisk) -- Generic step marker

The asterisk `*` can replace any step keyword. It is useful for bullet-point
style lists where Given/When/Then would feel awkward:

```gherkin
Scenario: All done
  Given I am out shopping
  * I have eggs
  * I have milk
  * I have butter
  When I check my list
  Then I don't need anything
```

This is equivalent to:

```gherkin
Scenario: All done
  Given I am out shopping
  And I have eggs
  And I have milk
  And I have butter
  When I check my list
  Then I don't need anything
```

### Step matching rules

- The parser ignores the keyword when matching steps to step definitions. That
  means `Given there is milk` and `When there is milk` and `Then there is milk`
  all match the **same** step definition.
- Because of this, avoid writing steps with identical text after the keyword
  but different semantic meanings. Instead, use distinct phrasing:

```gherkin
# BAD -- same text, different intent
Given there is money in my account
Then there is money in my account

# GOOD -- distinct phrasing
Given my account has a balance of $430
Then my account should have a balance of $430
```

---

## 9. Scenario Outline / Scenario Template

A `Scenario Outline` (synonym: `Scenario Template`) is a parameterized scenario
that runs once for each row in its `Examples` table. It eliminates duplication
when multiple scenarios differ only in their data values.

### Syntax (Scenario Outline)

```gherkin
Scenario Outline: <title>
  Given <step with <placeholder>>
  When <step with <placeholder>>
  Then <step with <placeholder>>

  Examples:
    | placeholder1 | placeholder2 | ... |
    | value1       | value2       | ... |
    | value3       | value4       | ... |
```

### Placeholders

- Placeholders use angle brackets: `<placeholder_name>`
- Placeholder names correspond to column headers in the
  `Examples` table.
- Each row in the Examples table generates a separate scenario
  execution.
- Placeholders can appear anywhere in a step, including inside
  quoted strings, Data Tables, and Doc Strings.

### Synonyms (Scenario Outline)

- `Scenario Outline` and `Scenario Template` are fully
  interchangeable.
- `Examples` and `Scenarios` are fully interchangeable as the
  table keyword.

### Example (Scenario Outline)

```gherkin
Scenario Outline: Eating cucumbers
  Given there are <start> cucumbers
  When I eat <eat> cucumbers
  Then I should have <left> cucumbers

  Examples:
    | start | eat | left |
    |    12 |   5 |    7 |
    |    20 |   5 |   15 |
```

This is equivalent to writing two separate scenarios:

```gherkin
Scenario: Eating cucumbers (row 1)
  Given there are 12 cucumbers
  When I eat 5 cucumbers
  Then I should have 7 cucumbers

Scenario: Eating cucumbers (row 2)
  Given there are 20 cucumbers
  When I eat 5 cucumbers
  Then I should have 15 cucumbers
```

### Multiple Examples blocks

A `Scenario Outline` can have **multiple** `Examples` blocks. Each block can
have its own tags and title. This is useful for grouping test data by category:

```gherkin
Scenario Outline: Withdraw cash
  Given the account balance is $<balance>
  And the card is valid
  When the account holder requests $<amount>
  Then the ATM should dispense $<amount>
  And the account balance should be $<remaining>

  @positive
  Examples: Successful withdrawals
    | balance | amount | remaining |
    |     500 |     50 |       450 |
    |     500 |    200 |       300 |

  @negative
  Examples: Insufficient funds
    | balance | amount | remaining |
    |     100 |    200 |       100 |
    |       0 |     50 |         0 |
```

### Placeholders in Data Tables

Placeholders can appear inside Data Tables within a Scenario Outline:

```gherkin
Scenario Outline: Create a user with role
  When I create a user with the following details:
    | name   | <name>   |
    | email  | <email>  |
    | role   | <role>   |
  Then the user should be created successfully

  Examples:
    | name  | email           | role    |
    | Alice | alice@test.com  | admin   |
    | Bob   | bob@test.com    | editor  |
```

### Placeholders in Doc Strings

Placeholders also work inside Doc Strings:

```gherkin
Scenario Outline: API response body
  When I request the user profile for "<username>"
  Then the response body should be:
    """json
    {
      "username": "<username>",
      "role": "<role>"
    }
    """

  Examples:
    | username | role    |
    | alice    | admin   |
    | bob      | viewer  |
```

---

## 10. Examples Tables

The `Examples` table (synonym: `Scenarios` table) provides the data
that drives a `Scenario Outline`. Each row generates a separate
scenario execution.

### Syntax (Examples Tables)

```gherkin
Examples: <optional title>
  | column1 | column2 | column3 |
  | value1a | value2a | value3a |
  | value1b | value2b | value3b |
```

### Rules

- The **first row** is always the header row, containing placeholder names
  that match the `<placeholder>` references in the Scenario Outline steps.
- Each subsequent row is a data row that generates one scenario execution.
- A `Scenario Outline` must have **at least one** `Examples` block.
- A `Scenario Outline` can have **multiple** `Examples` blocks.
- Each `Examples` block can have its own tags (which are inherited by the
  generated scenarios).
- Each `Examples` block can have a title and description.
- Cell values are always strings (type conversion happens in step definitions).

### Cell formatting

- Cells are delimited by pipe characters `|`.
- Leading and trailing whitespace in cells is trimmed.
- Pipes within cell values must be escaped: `\|`
- Newlines within cell values: `\n`
- Backslashes within cell values: `\\`
- Align the pipe characters for readability (this is a convention, not a
  requirement).

### Example with multiple Examples blocks

```gherkin
Scenario Outline: Validate email format
  When the user enters "<email>" as their email
  Then the validation result should be "<result>"

  Examples: Valid emails
    | email              | result |
    | user@example.com   | valid  |
    | first.last@co.uk   | valid  |

  Examples: Invalid emails
    | email              | result  |
    | not-an-email       | invalid |
    | @missing-local.com | invalid |
    | user@              | invalid |
```

---

## 11. Data Tables

Data Tables are step arguments that pass structured data to a step definition.
They appear **immediately below a step** and are part of that step.

### Syntax (Data Tables)

```gherkin
Given the following users exist:
  | name   | email              | twitter         |
  | Aslak  | aslak@cucumber.io  | @aslak_hellesoy |
  | Julien | julien@cucumber.io | @jbpros         |
  | Matt   | matt@cucumber.io   | @mattwynne      |
```

### Cell escaping

The same escaping rules apply as in Examples tables:

| Character | Escape Sequence |
|-----------|-----------------|
| Newline   | `\n`            |
| Pipe      | `\|`            |
| Backslash | `\\`            |

### Common Data Table patterns

#### List of values (single column)

```gherkin
Given the following products are in stock:
  | Laptop    |
  | Keyboard  |
  | Mouse     |
  | Monitor   |
```

#### Key-value pairs (two columns, no header)

```gherkin
When the user fills in the registration form:
  | First Name | John            |
  | Last Name  | Smith           |
  | Email      | john@smith.com  |
  | Password   | s3cret!         |
```

#### Tabular data with headers

```gherkin
Then the search results should contain:
  | Title            | Author       | Year |
  | The Great Gatsby | F. Fitzgerald | 1925 |
  | 1984             | George Orwell | 1949 |
```

### Data Tables vs. hard-coded values

Use Data Tables when you need to pass multiple data items to a single step.
Compare:

```gherkin
# Without Data Table -- awkward for many values
Given the user "John" with email "john@test.com" and role "admin" and status "active"

# With Data Table -- clean and extensible
Given the following user:
  | name   | John          |
  | email  | john@test.com |
  | role   | admin         |
  | status | active        |
```

---

## 12. Data Tables vs. Examples Tables

These two constructs use the same pipe-delimited syntax but serve fundamentally
different purposes. This distinction is critical.

| Aspect                 | Data Table                         | Examples Table                           |
|------------------------|------------------------------------|------------------------------------------|
| **Keyword**            | None (directly below a step)       | `Examples:` or `Scenarios:`              |
| **Belongs to**         | A single step                      | A `Scenario Outline`                     |
| **Scope**              | Argument to one step definition    | Parameterizes the entire scenario        |
| **Execution**          | Step runs **once** with table data | Scenario runs **once per row**           |
| **First row**          | Headers or data (up to step code)  | Always column headers (`<placeholders>`) |
| **Placeholder syntax** | Not applicable                     | `<column_name>` in steps                 |

### Side-by-side example

**Data Table** -- passes a list to a single step (the scenario runs once):

```gherkin
Scenario: Add multiple items to the cart
  Given the following items are available:
    | Item     | Price |
    | Laptop   | 999   |
    | Mouse    | 25    |
    | Keyboard | 75    |
  When the user adds all items to the cart
  Then the cart total should be 1099
```

**Examples Table** -- parameterizes the entire scenario (runs three times):

```gherkin
Scenario Outline: Add a single item to the cart
  Given the item "<item>" is available at price $<price>
  When the user adds "<item>" to the cart
  Then the cart should contain 1 item at $<price>

  Examples:
    | item     | price |
    | Laptop   | 999   |
    | Mouse    | 25    |
    | Keyboard | 75    |
```

### When to use which

- Use a **Data Table** when a single step needs structured input (e.g., creating
  multiple records, filling a form, passing configuration).
- Use an **Examples Table** (with `Scenario Outline`) when you want to repeat
  the **entire scenario** with different data values.

---

## 13. Doc Strings

Doc Strings are multi-line string arguments attached to a step, used when a
step needs to receive a large block of text (e.g., JSON payloads,
email bodies, configuration files).

### Syntax (Doc Strings)

Doc Strings are delimited by triple double-quotes (`"""`) or triple backticks
(`` ``` ``):

```gherkin
Given a blog post named "Random" with Markdown body
  """
  Some Title, Eh?
  ===============
  Here is the first paragraph of my blog post. Lorem ipsum dolor sit amet,
  consectetur adipiscing elit.
  """
```

Or using backticks:

````gherkin
Given a blog post named "Random" with Markdown body
  ```
  Some Title, Eh?
  ===============
  Here is the first paragraph of my blog post. Lorem ipsum dolor sit amet,
  consectetur adipiscing elit.
  ```
````

### Content type annotation

You can specify a content type immediately after the opening delimiter (no space
between the delimiter and the content type name):

```gherkin
Given the API response body is:
  """json
  {
    "id": 42,
    "name": "Widget",
    "price": 9.99
  }
  """
```

````gherkin
Given the configuration file contains:
  ```yaml
  database:
    host: localhost
    port: 5432
    name: myapp_dev
  ```
````

The content type annotation is passed to the step definition and can be used
for parsing or validation. Common content types include `json`, `xml`, `yaml`,
`markdown`, `html`, and `text`.

### Indentation handling

The opening delimiter's column position sets the "base indentation." All lines
of the Doc String are dedented by that amount. Internal indentation beyond the
base column is preserved.

```gherkin
    Given a config file:
      """yaml
      server:
        host: localhost
        port: 8080
      """
```

In this example, the `"""` starts at column 7 (0-indexed: 6). The content
lines `server:`, `host: localhost`, and `port: 8080` are all dedented by
6 spaces, preserving the YAML's internal indentation.

### Rules (Doc Strings)

- The opening and closing delimiters must use the same characters
  (`"""` / `"""` or `` ``` `` / `` ``` ``).
- The closing delimiter must be on its own line.
- The content type annotation is optional.
- Doc Strings support `<placeholder>` substitution when used
  inside a `Scenario Outline`.
- A step can have **either** a Doc String **or** a Data Table,
  but not both.
- Only one Doc String per step.

### Example with Scenario Outline placeholder

```gherkin
Scenario Outline: API error response
  When the user sends an invalid request of type "<error_type>"
  Then the response should be:
    """json
    {
      "error": "<error_type>",
      "message": "<message>"
    }
    """

  Examples:
    | error_type     | message                |
    | not_found      | Resource not found     |
    | unauthorized   | Authentication required |
```

---

## 14. Tags

Tags are metadata annotations that begin with `@` and are used to
organize, filter, and control the execution of features and scenarios.

### Syntax (Tags)

```gherkin
@tag-name
```

- Tags start with `@` immediately followed by the tag name (no space).
- Tag names can contain letters, digits, hyphens (`-`), underscores (`_`),
  and periods (`.`).
- Multiple tags on the same line are separated by spaces.
- Tags can also be placed on separate lines.

```gherkin
@smoke @fast
Feature: Quick checks

@billing @critical @sprint-42
Scenario: Charge customer
  Given ...
```

### Where tags can be placed

Tags can be placed above:

- `Feature`
- `Rule`
- `Scenario` / `Example`
- `Scenario Outline` / `Scenario Template`
- `Examples` / `Scenarios` (the table keyword)

Tags **cannot** be placed on:

- `Background`
- Individual steps (`Given`, `When`, `Then`, `And`, `But`, `*`)

### Tag inheritance

Tags are inherited by child elements:

```text
Feature tags
  └── inherited by Rule, Scenario, Scenario Outline, Examples

Rule tags
  └── inherited by Scenario, Scenario Outline, Examples within that Rule

Scenario Outline tags
  └── inherited by Examples blocks within that Scenario Outline
```

Example of inheritance:

```gherkin
@feature-tag
Feature: Tag inheritance demo

  @rule-tag
  Rule: Some business rule

    @scenario-tag
    Scenario: Inherits all three tags
      # This scenario has: @feature-tag, @rule-tag, @scenario-tag
      Given something

  @outline-tag
  Scenario Outline: Parameterized
    Given <input>

    @examples-tag
    Examples:
      # Each generated scenario has: @feature-tag, @outline-tag, @examples-tag
      | input |
      | foo   |
```

### Tag expressions (for filtering)

Tag expressions use boolean operators to select scenarios for execution:

| Expression                                 | Meaning                          |
|--------------------------------------------|----------------------------------|
| `@smoke`                                   | Has the `@smoke` tag             |
| `not @wip`                                 | Does not have the `@wip` tag     |
| `@smoke and @fast`                         | Has both tags                    |
| `@gui or @api`                             | Has at least one of the tags     |
| `(@smoke or @regression) and not @slow`    | Complex expression               |

### Command-line usage

```bash
# Cucumber.js
npx cucumber-js --tags "@smoke and not @wip"

# Cucumber (Ruby)
cucumber --tags "@smoke and not @wip"

# Cucumber (Java / Maven)
mvn test -Dcucumber.filter.tags="@smoke and not @wip"
```

### Common tag conventions

| Tag                | Purpose                                          |
|--------------------|--------------------------------------------------|
| `@wip`             | Work in progress; scenario is not yet complete   |
| `@smoke`           | Smoke test; part of a quick sanity check suite   |
| `@regression`      | Part of the full regression test suite           |
| `@slow`            | Marks slow-running scenarios                     |
| `@fast`            | Marks fast-running scenarios                     |
| `@manual`          | Requires manual testing (not automated)          |
| `@ignore`          | Skip this scenario during test execution         |
| `@critical`        | Business-critical scenario                       |
| `@api`             | Tests an API endpoint                            |
| `@ui`              | Tests the user interface                         |
| `@database`        | Involves database operations                     |
| `@flaky`           | Known to be intermittently failing               |
| `@JIRA-1234`       | Links to an issue tracker ticket                 |
| `@sprint-42`       | Associated with a specific sprint                |
| `@feature-toggle`  | Depends on a feature flag                        |

### Tags and hooks

In step definition code, tags can control which hooks run:

```java
// Java example
@Before("@database")
public void setupDatabase() { /* ... */ }

@After("@browser and not @headless")
public void closeBrowser(Scenario scenario) { /* ... */ }
```

---

## 15. Comments

Comments in Gherkin begin with `#` at the start of a line
(optionally preceded by whitespace/indentation). Everything from
the `#` to the end of the line is ignored by the parser.

### Syntax (Comments)

```gherkin
# This is a comment
Feature: My feature
  # This is also a comment
  Scenario: My scenario
    # Comments can appear between steps
    Given something
    # But they cannot appear mid-step
    When something else
```

### Rules (Comments)

- Comments must be on their own line. Inline comments (after a keyword or step
  text on the same line) are **not** supported.
- The `#` character must be the first non-whitespace character on the line.
- Comments can appear anywhere in the file: before `Feature`, between scenarios,
  between steps, etc.
- The language header (`# language: xx`) is technically a comment with special
  meaning -- it must appear on the **first line** of the file.

### What is NOT a comment

```gherkin
Feature: My feature # This is NOT a comment -- it's part of the title!
```

Gherkin does **not** support inline comments. The `#` above would be included
in the feature title.

### Convention

Use comments sparingly. Well-written Gherkin should be self-explanatory. When
comments are needed, use them to explain *why*, not *what*:

```gherkin
Feature: Order processing

  # Regulatory requirement: EU orders must include VAT
  Scenario: EU order includes VAT
    Given a customer in Germany
    When they place an order for $100
    Then the total should include 19% VAT
```

---

## 16. Descriptions

Free-form descriptions can appear below any keyword that is
followed by a colon (`Feature`, `Rule`, `Scenario`,
`Scenario Outline`, `Background`, `Examples`). The description
is all text between the keyword line and the first step, tag line,
or next keyword.

### Syntax (Descriptions)

```gherkin
Feature: Account management
  As an account holder
  I want to manage my personal information
  So that my account details are always up to date

  This feature covers profile editing, password changes,
  and account deletion workflows.

  Scenario: Update display name
    The user should be able to change their display name
    from the profile settings page.

    Given the user is on the profile settings page
    When the user changes their display name to "New Name"
    Then the display name should be updated
```

### Rules (Descriptions)

- Descriptions are optional.
- Descriptions cannot contain Gherkin keywords at the beginning
  of a line (the parser would interpret them as the start of a
  new section or step).
- Descriptions support Markdown formatting -- many reporting
  tools render it.
- Descriptions are included in the AST and are available in step
  definition code.

---

## 17. Localization (i18n)

Gherkin supports writing feature files in over 70 natural languages. This allows
non-English-speaking teams to write specifications in their native language.

### Specifying the language

Add a language header comment as the **very first line** of the `.feature` file:

```gherkin
# language: fr
```

If no language header is present, the parser defaults to English (`en`).

### Examples in different languages

#### French (fr)

```gherkin
# language: fr
Fonctionnalité: Connexion utilisateur
  En tant qu'utilisateur enregistré
  Je veux me connecter à mon compte
  Afin d'accéder à mes données personnelles

  Scénario: Connexion réussie
    Soit un utilisateur "alice@example.com" avec le mot de passe "s3cret"
    Quand l'utilisateur se connecte avec "alice@example.com" et "s3cret"
    Alors l'utilisateur voit le tableau de bord
```

#### German (de)

```gherkin
# language: de
Funktionalität: Benutzeranmeldung
  Als registrierter Benutzer
  möchte ich mich anmelden können
  um auf meine Daten zuzugreifen

  Szenario: Erfolgreiche Anmeldung
    Angenommen ein Benutzer "alice@example.com" mit Passwort "s3cret"
    Wenn der Benutzer sich mit "alice@example.com" und "s3cret" anmeldet
    Dann sieht der Benutzer das Dashboard
```

#### Japanese (ja)

```gherkin
# language: ja
フィーチャ: ユーザーログイン

  シナリオ: 正常なログイン
    前提 ユーザー "alice@example.com" がパスワード "s3cret" で登録されている
    もし ユーザーが "alice@example.com" と "s3cret" でログインする
    ならば ユーザーはダッシュボードを見る
```

#### Norwegian (no)

```gherkin
# language: no
Funksjonalitet: Gjett et ord

  Eksempel: Ordmaker starter et spill
    Når Ordmaker starter et spill
    Så må Ordmaker vente på at Gjetter blir med

  Eksempel: Gjetter blir med
    Gitt at Ordmaker har startet et spill med ordet "bløtt"
    Når Gjetter blir med på Ordmakers spill
    Så må Gjetter gjette et ord på 5 bokstaver
```

### English keyword variants

Even within English, Gherkin provides synonym keywords:

| Standard            | Synonym(s)                                    |
|---------------------|-----------------------------------------------|
| `Feature`           | `Business Need`, `Ability`                    |
| `Scenario`          | `Example`                                     |
| `Scenario Outline`  | `Scenario Template`                           |
| `Examples`          | `Scenarios`                                   |

### Fun localizations

Gherkin includes playful localizations:

- **Pirate English** (`en-pirate`): `Ahoy matey!` (Feature),
  `Heave to` (Background), `Blimey!` (Scenario)
- **LOLCAT** (`en-lol`): `OH HAI` (Feature), `I CAN HAZ` (Background),
  `MISHUN` (Scenario)
- **Old English** (`en-old`)
- **Australian English** (`en-au`)
- **Scouse English** (`en-Scouse`)

### How to find all supported languages

The complete list of supported languages and their keyword translations is
maintained in the
[gherkin-languages.json](https://github.com/cucumber/gherkin/blob/main/gherkin-languages.json)
file in the official Cucumber Gherkin repository.

Many Gherkin implementations also provide a CLI command to list languages:

```bash
# Cucumber (Ruby)
cucumber --i18n help

# Cucumber (Ruby) -- show keywords for a specific language
cucumber --i18n fr
```

---

## 18. Formal Grammar

The Gherkin grammar (defined in
[gherkin.berp](https://github.com/cucumber/gherkin/blob/main/gherkin.berp))
follows these production rules:

```text
GherkinDocument := Feature?

Feature := FeatureHeader Background? ScenarioDefinition* Rule*

FeatureHeader := Tags? #FeatureLine DescriptionHelper

Rule := RuleHeader Background? ScenarioDefinition*

RuleHeader := Tags? #RuleLine DescriptionHelper

Background := #BackgroundLine DescriptionHelper Step*

ScenarioDefinition := Tags? Scenario

Scenario := #ScenarioLine DescriptionHelper Step* ExamplesDefinition*

ExamplesDefinition := Tags? Examples

Examples := #ExamplesLine DescriptionHelper ExamplesTable?

ExamplesTable := #TableRow #TableRow*

Step := #StepLine StepArg?

StepArg := DataTable | DocString

DataTable := #TableRow+

DocString := #DocStringSeparator #Other* #DocStringSeparator

Tags := #TagLine+

DescriptionHelper := Description? #Comment*

Description := (#Other | #Comment)+
```

### Key structural constraints from the grammar

1. A `GherkinDocument` contains at most one `Feature`.
2. A `Feature` can have at most one `Background`, followed by zero or more
   `ScenarioDefinition`s, followed by zero or more `Rule`s.
3. A `Rule` can have its own `Background` (at most one) and its
   own scenarios.
4. `Scenario` and `Scenario Outline` are the same grammar
   production (`Scenario`); a Scenario with
   `ExamplesDefinition`s is a Scenario Outline.
5. Each `Step` can have at most one step argument: either a
   `DataTable` or a `DocString`, but not both.
6. `Tags` are one or more tag lines and must appear directly above the element
   they annotate.
7. Rules cannot be nested inside other rules.

---

## 19. Indentation and Formatting Conventions

Gherkin is whitespace-agnostic regarding indentation (spaces and
tabs both work), but consistent formatting is strongly recommended.

### Recommended indentation (2 spaces)

```gherkin
Feature: Shopping cart
  Background:
    Given the store has products

  Scenario: Add item to cart
    Given the user is on the product page
    When the user clicks "Add to Cart"
    Then the cart should contain 1 item

  Scenario Outline: Add multiple items
    Given the user has <count> items in the cart
    When the user adds another item
    Then the cart should contain <total> items

    Examples:
      | count | total |
      |     0 |     1 |
      |     3 |     4 |
```

### Standard indentation levels

| Element                 | Indentation Level |
|-------------------------|-------------------|
| `Feature:`              | 0 (column 1)      |
| Feature description     | 2 spaces          |
| `Background:`           | 2 spaces          |
| `Scenario:`             | 2 spaces          |
| `Scenario Outline:`     | 2 spaces          |
| `Rule:`                 | 2 spaces          |
| Steps (Given/When/Then) | 4 spaces          |
| `Examples:`             | 4 spaces          |
| Data Table rows         | 6 spaces          |
| Examples Table rows     | 6 spaces          |
| Doc String delimiters   | 6 spaces          |

### Table alignment

Align pipe characters in tables for readability:

```gherkin
# Good -- aligned columns
| name   | email              | role    |
| Alice  | alice@example.com  | admin   |
| Bob    | bob@example.com    | editor  |

# Acceptable but harder to read -- unaligned columns
| name | email | role |
| Alice | alice@example.com | admin |
| Bob | bob@example.com | editor |
```

### Spacing conventions

- **One blank line** between scenarios.
- **One blank line** between the Feature description and the
  first Background or Scenario.
- **No blank lines** between steps within a scenario.
- **One blank line** before an `Examples` block (optional but
  common).
- **Two blank lines** can be used to separate major sections
  (e.g., before a `Rule`).

---

## 20. Best Practices for Writing Gherkin

These practices are essential for anyone building or consuming
Gherkin specifications.

### One scenario, one behavior

Each scenario should test exactly one behavior. If you find yourself writing
multiple When-Then pairs, split them into separate scenarios:

```gherkin
# BAD -- multiple behaviors in one scenario
Scenario: User management
  When the admin creates a user
  Then the user exists
  When the admin deactivates the user
  Then the user is inactive

# GOOD -- one behavior per scenario
Scenario: Admin creates a user
  When the admin creates a user
  Then the user exists

Scenario: Admin deactivates a user
  Given a user exists
  When the admin deactivates the user
  Then the user is inactive
```

### Declarative over imperative

Write steps at the behavior level, not the UI interaction level:

```gherkin
# BAD -- imperative (describes HOW)
Scenario: Login
  Given the browser is open
  When I navigate to "http://example.com/login"
  And I type "alice" into the "#username" field
  And I type "s3cret" into the "#password" field
  And I click the "#login-button" element
  Then the "#dashboard" element should be visible

# GOOD -- declarative (describes WHAT)
Scenario: Successful login
  Given the user "alice" is registered with password "s3cret"
  When the user logs in with valid credentials
  Then the user should see the dashboard
```

### Keep scenarios short

Aim for 3-5 steps per scenario, with a maximum of about 10. Long scenarios
are a signal that the behavior might need to be broken down or that Background
should be used.

### Use Background wisely

- Only include steps that apply to **every** scenario in the Feature or Rule.
- Keep it short (1-4 steps).
- Only use `Given` steps in Background.
- Do not put anything in Background that the reader needs to remember while
  reading the scenarios -- a reader should be able to understand a scenario on
  its own.

### Write descriptive titles

Scenario titles should clearly describe the behavior being tested:

```gherkin
# BAD
Scenario: Test 1
Scenario: It works
Scenario: Error

# GOOD
Scenario: Registered user logs in with correct password
Scenario: Unregistered email shows "account not found" error
Scenario: Expired session redirects to login page
```

### Avoid technical jargon

Gherkin is meant to be readable by non-technical stakeholders. Avoid CSS
selectors, SQL queries, HTTP methods, and implementation details in steps.

### Use consistent phrasing

Reuse step text across scenarios to maximize step definition reuse:

```gherkin
# These all match the same step definition:
Given the user "alice" is logged in
Given the user "bob" is logged in
Given the user "charlie" is logged in
```

### Tag naming conventions

- Use lowercase with hyphens: `@smoke-test`, not `@SmokeTest` or `@SMOKE_TEST`.
- Prefix organizational tags consistently: `@team-payments`, `@sprint-42`.
- Reserve `@wip` for genuinely in-progress work.
- Avoid too many tags per scenario (3-5 is reasonable).

---

## Appendix A: Complete Feature File Example

This example demonstrates all major Gherkin constructs in a single file:

```gherkin
# language: en
@e-commerce @billing
Feature: Order checkout
  As a customer with items in my cart
  I want to complete the checkout process
  So that I can receive my purchased items

  Background:
    Given the following products exist:
      | name       | price  | stock |
      | Widget     |   9.99 |   100 |
      | Gadget     |  24.99 |    50 |
      | Doohickey  |   4.99 |   200 |
    And the shipping rates are:
      | method   | cost  | days |
      | Standard |  5.00 |    5 |
      | Express  | 15.00 |    2 |

  @happy-path @smoke
  Scenario: Successful checkout with credit card
    Given the customer has the following items in the cart:
      | product | quantity |
      | Widget  |        2 |
      | Gadget  |        1 |
    And the customer selects "Standard" shipping
    When the customer pays with a valid credit card
    Then the order should be confirmed
    And the order total should be $49.97
    And a confirmation email should be sent

  @error-handling
  Scenario: Checkout fails with expired credit card
    Given the customer has 1 "Widget" in the cart
    And the customer selects "Standard" shipping
    When the customer pays with an expired credit card
    Then the order should not be created
    And the error message should be "Payment declined: card expired"

  @parameterized
  Scenario Outline: Shipping cost calculation
    Given the customer has <quantity> "<product>" in the cart
    And the customer selects "<shipping>" shipping
    When the customer proceeds to payment
    Then the shipping cost should be $<shipping_cost>
    And the estimated delivery should be <days> days

    @domestic
    Examples: Domestic orders
      | product | quantity | shipping | shipping_cost | days |
      | Widget  |        1 | Standard |          5.00 |    5 |
      | Widget  |        1 | Express  |         15.00 |    2 |
      | Gadget  |        3 | Standard |          5.00 |    5 |

    @international
    Examples: International orders
      | product | quantity | shipping | shipping_cost | days |
      | Widget  |        1 | Standard |         12.00 |   10 |
      | Gadget  |        2 | Express  |         30.00 |    4 |

  Rule: Out-of-stock items cannot be ordered

    Background:
      Given the customer is logged in

    Scenario: Item goes out of stock during checkout
      Given the customer has 1 "Widget" in the cart
      And another customer buys all remaining "Widget" stock
      When the customer proceeds to payment
      Then the checkout should fail
      And the message should be:
        """
        Sorry, the following items are no longer available:
        - Widget (out of stock)

        Please update your cart and try again.
        """

    Scenario: Partial stock available
      Given the customer has 150 "Widget" in the cart
      When the customer proceeds to checkout
      Then a warning should display "Only 100 Widget in stock"
      But the customer should be able to adjust the quantity

  Rule: Discounts are applied before tax

    # Regional tax regulations require discounts to reduce the taxable amount
    Scenario: Percentage discount applied before tax
      Given the customer has 1 "Gadget" in the cart
      And a 20% discount code "SAVE20" is applied
      When the order summary is calculated
      Then the subtotal should be $19.99
      And the tax should be calculated on $19.99

    Scenario Outline: Fixed discount codes
      Given the customer has items totaling $<subtotal>
      And the discount code "<code>" is applied
      When the order summary is calculated
      Then the discount should be $<discount>
      And the final subtotal should be $<final>

      Examples:
        | subtotal | code     | discount | final  |
        |    50.00 | FIVE_OFF |     5.00 |  45.00 |
        |   100.00 | TEN_OFF  |    10.00 |  90.00 |
        |    25.00 | FIVE_OFF |     5.00 |  20.00 |
```

## Appendix B: Keyword Quick Reference Table

| Keyword              | Followed by | Synonyms                    | Purpose                                    |
|----------------------|-------------|-----------------------------|--------------------------------------------|
| `Feature`            | `:`         | `Business Need`, `Ability`  | Top-level container for scenarios          |
| `Rule`               | `:`         | --                          | Groups scenarios under a business rule     |
| `Background`         | `:`         | --                          | Shared setup steps                         |
| `Scenario`           | `:`         | `Example`                   | A single test case                         |
| `Scenario Outline`   | `:`         | `Scenario Template`         | Parameterized scenario template            |
| `Examples`           | `:`         | `Scenarios`                 | Data table for Scenario Outline            |
| `Given`              | ` ` (space) | --                          | Precondition / initial context             |
| `When`               | ` ` (space) | --                          | Action or event                            |
| `Then`               | ` ` (space) | --                          | Expected outcome                           |
| `And`                | ` ` (space) | --                          | Continues previous step type               |
| `But`                | ` ` (space) | --                          | Continues previous step type (contrasting) |
| `*`                  | ` ` (space) | --                          | Generic step (replaces any keyword)        |
| `"""`                | --          | ` ``` `                     | Doc String delimiter                       |
| `\|`                 | --          | --                          | Table cell delimiter                       |
| `@`                  | tag name    | --                          | Tag prefix                                 |
| `#`                  | --          | --                          | Comment (or language header)               |
| `# language:`        | lang code   | --                          | Language declaration (first line only)     |
