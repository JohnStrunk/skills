# Gherkin Feature File Examples: A Comprehensive Collection

This document collects high-quality, real-world examples of
Gherkin feature files that demonstrate excellent specification
writing. Examples are sourced from official Cucumber
documentation, prominent open-source BDD projects, and
established best-practice guides.

---

## Table of Contents

1. [Simple Feature Examples](#1-simple-feature-examples)
2. [Complex Feature Examples](#2-complex-feature-examples)
3. [Examples Using All Gherkin Features](#3-examples-using-all-gherkin-features)
4. [Domain-Specific Examples](#4-domain-specific-examples)
5. [Good vs Bad Examples](#5-good-vs-bad-examples)
6. [Template Structures](#6-template-structures)
7. [Sources and References](#7-sources-and-references)

---

## 1. Simple Feature Examples

### 1.1 User Login

A clean, declarative login specification that focuses on behavior
rather than UI mechanics.

```gherkin
@authentication
Feature: User login
  As a registered user
  I want to log in to my account
  So that I can access my personalized dashboard

  Background:
    Given the user is already registered with email "user@example.com"

  Scenario: Successful login with valid credentials
    Given the login page is displayed
    When the user logs in with valid credentials
    Then the user should be redirected to their dashboard
    And a welcome message should be displayed

  Scenario: Failed login with incorrect password
    Given the login page is displayed
    When the user logs in with an incorrect password
    Then an error message "Invalid email or password" should be displayed
    And the user should remain on the login page

  Scenario: Account locked after repeated failures
    Given the login page is displayed
    And the user has failed to log in 4 times
    When the user logs in with an incorrect password
    Then the account should be temporarily locked
    And a message "Account locked. Try again in 30 minutes." should be displayed
```

**Why this is good:**

- Uses a Background to establish shared preconditions
- Each scenario tests exactly one behavior
- Declarative style (says "logs in" not "types in field, clicks button")
- Third person, present tense throughout
- Clear expected outcomes in Then steps

### 1.2 User Registration

```gherkin
@registration
Feature: New user registration
  As a visitor
  I want to create an account
  So that I can access member-only features

  Scenario: Successful registration with valid details
    Given the registration page is displayed
    When the user registers with the following details:
      | field           | value               |
      | first name      | Jane                |
      | last name       | Smith               |
      | email           | jane@example.com    |
      | password        | SecurePass123!      |
      | confirm password| SecurePass123!      |
    Then the account should be created successfully
    And a confirmation email should be sent to "jane@example.com"
    And the user should be redirected to the welcome page

  Scenario: Registration rejected for existing email
    Given a user already exists with email "jane@example.com"
    And the registration page is displayed
    When the user attempts to register with email "jane@example.com"
    Then the registration should be rejected
    And an error message "An account with this email already exists" should be displayed

  Scenario: Registration rejected for weak password
    Given the registration page is displayed
    When the user attempts to register with password "123"
    Then the registration should be rejected
    And an error message should indicate the password requirements
```

**Why this is good:**

- Uses a Data Table for structured input in the first scenario
- Keeps each scenario focused on one validation rule
- Uses "attempts to register" for failure cases (implies the
  action, not the outcome)

### 1.3 Search Functionality

Based on Automation Panda's well-known examples with improvements applied.

```gherkin
Feature: Product search
  As a shopper
  I want to search for products
  So that I can quickly find what I need

  Scenario: Search returns matching results
    Given the product catalog contains items
    When the user searches for "wireless headphones"
    Then search results related to "wireless headphones" are displayed
    And the number of results is shown

  Scenario: Search with no matching results
    Given the product catalog contains items
    When the user searches for "xyznonexistent123"
    Then a message "No products found" is displayed
    And search suggestions are offered

  Scenario: Search results can be filtered
    Given search results for "laptop" are displayed
    When the user filters results by price range "$500 to $1000"
    Then only laptops within the price range are shown
    And the active filter is displayed
```

### 1.4 Basic CRUD -- From Cucumber's Official 10-Minute Tutorial

This progression shows how Cucumber's own tutorial builds from
simple to parameterized.

```gherkin
Feature: Is it Friday yet?
  Everybody wants to know when it's Friday

  Scenario: Sunday isn't Friday
    Given today is Sunday
    When I ask whether it's Friday yet
    Then I should be told "Nope"

  Scenario: Friday is Friday
    Given today is Friday
    When I ask whether it's Friday yet
    Then I should be told "TGIF"
```

Refactored with Scenario Outline:

```gherkin
Feature: Is it Friday yet?
  Everybody wants to know when it's Friday

  Scenario Outline: Today is or is not Friday
    Given today is "<day>"
    When I ask whether it's Friday yet
    Then I should be told "<answer>"

    Examples:
      | day            | answer |
      | Friday         | TGIF   |
      | Sunday         | Nope   |
      | anything else! | Nope   |
```

*Source: [Cucumber 10-Minute Tutorial](https://cucumber.io/docs/guides/10-minute-tutorial/)*

---

## 2. Complex Feature Examples

### 2.1 E-Commerce Order Workflow

A multi-rule feature demonstrating a complete ordering process
with business rules.

```gherkin
@e-commerce @orders
Feature: Order placement and fulfillment
  As an online shopper
  I want to place orders for products
  So that I can receive goods at my delivery address

  Background:
    Given the following products exist in the catalog:
      | name              | price  | stock |
      | Wireless Mouse    | 29.99  | 50    |
      | Mechanical KB     | 89.99  | 20    |
      | USB-C Hub         | 45.00  | 0     |
      | Monitor Stand     | 35.00  | 100   |

  Rule: Customers can only order products that are in stock

    Example: Adding an in-stock product to the cart
      Given the customer is viewing "Wireless Mouse"
      When the customer adds it to their cart
      Then the cart should contain 1 item
      And the cart total should be "$29.99"

    Example: Cannot add an out-of-stock product
      Given the customer is viewing "USB-C Hub"
      Then the "Add to Cart" action should be unavailable
      And a message "Out of Stock" should be displayed

  Rule: Order totals must include applicable taxes and shipping

    Example: Order with standard shipping
      Given the customer has the following items in their cart:
        | product           | quantity | unit price |
        | Wireless Mouse    | 2        | 29.99      |
        | Monitor Stand     | 1        | 35.00      |
      And the delivery address is in "California"
      When the customer proceeds to checkout
      Then the order summary should show:
        | line item         | amount  |
        | Subtotal          | $94.98  |
        | Tax (7.25%)       | $6.89   |
        | Shipping          | $5.99   |
        | Total             | $107.86 |

    Example: Free shipping for orders over $100
      Given the customer has items totaling "$120.00" in their cart
      When the customer proceeds to checkout
      Then shipping should be "$0.00"
      And a message "Free shipping applied!" should be displayed

  Rule: Inventory is reserved when an order is placed

    Example: Stock decreases after order placement
      Given the customer has 3 "Wireless Mouse" in their cart
      When the customer places the order
      Then the order confirmation is displayed
      And the stock for "Wireless Mouse" should be 47

    Example: Concurrent orders cannot exceed available stock
      Given "Mechanical KB" has 2 units in stock
      And Customer A has 2 "Mechanical KB" in their cart
      And Customer B has 1 "Mechanical KB" in their cart
      When Customer A places their order
      And Customer B attempts to place their order
      Then Customer A's order should be confirmed
      And Customer B should see "Insufficient stock for Mechanical KB"
```

**Why this is good:**

- Uses the `Rule` keyword to group scenarios by business rule
- Background provides shared test data with a structured Data Table
- Tests both happy paths and edge cases (concurrency, stock limits)
- Each Rule reads as a clear, testable business requirement
- Monetary values use realistic formatting

### 2.2 Banking -- Account Transfers with Business Rules

```gherkin
@banking @transfers @critical
Feature: Inter-account money transfers
  As a bank customer
  I want to transfer money between accounts
  So that I can manage my finances flexibly

  Background:
    Given the following accounts exist:
      | account number | owner       | balance   | type     |
      | ACC-001        | Alice Brown | 5,000.00  | Checking |
      | ACC-002        | Alice Brown | 10,000.00 | Savings  |
      | ACC-003        | Bob Green   | 2,500.00  | Checking |

  Rule: Transfers between own accounts are processed immediately

    Example: Successful transfer between own accounts
      Given Alice is logged in
      When Alice transfers $500.00 from ACC-001 to ACC-002
      Then ACC-001 balance should be $4,500.00
      And ACC-002 balance should be $10,500.00
      And a confirmation with reference number should be displayed
      And both accounts should show the transaction in their history

  Rule: Transfers must not exceed available balance

    Example: Transfer rejected for insufficient funds
      Given Alice is logged in
      When Alice attempts to transfer $6,000.00 from ACC-001 to ACC-002
      Then the transfer should be declined
      And an error "Insufficient funds" should be displayed
      And ACC-001 balance should remain $5,000.00
      And ACC-002 balance should remain $10,000.00

    Example: Transfer of exact available balance succeeds
      Given Alice is logged in
      When Alice transfers $5,000.00 from ACC-001 to ACC-002
      Then the transfer should be processed
      And ACC-001 balance should be $0.00

  Rule: Transfers to other customers require additional verification

    Example: Transfer to another customer triggers verification
      Given Alice is logged in
      When Alice initiates a transfer of $200.00 from ACC-001 to ACC-003
      Then a verification code should be sent to Alice's registered phone
      And the transfer should be pending until verified

    Example: Verified transfer to another customer completes
      Given Alice has initiated a transfer of $200.00 to ACC-003
      And a verification code has been sent
      When Alice enters the correct verification code
      Then the transfer should be processed
      And ACC-001 balance should be $4,800.00
      And ACC-003 balance should be $2,700.00

  Rule: Daily transfer limits apply based on account type

    Scenario Outline: Transfer limits vary by account type
      Given a customer with a <type> account containing $50,000.00
      When the customer attempts to transfer <amount>
      Then the transfer should be <result>

      Examples:
        | type     | amount     | result   |
        | Checking | $5,000.00  | approved |
        | Checking | $10,001.00 | declined |
        | Savings  | $2,000.00  | approved |
        | Savings  | $5,001.00  | declined |
```

### 2.3 Insurance Claim Processing

A complex business workflow with multiple states and decision points.

```gherkin
@insurance @claims
Feature: Insurance claim processing
  As a policyholder
  I want to file and track insurance claims
  So that I can receive compensation for covered losses

  Rule: Claims must be filed within the policy coverage period

    Example: Claim filed within coverage period is accepted
      Given a policy "POL-2024-001" with coverage from "2024-01-01" to "2024-12-31"
      And the current date is "2024-06-15"
      When the policyholder files a claim for an incident on "2024-06-10"
      Then the claim should be accepted for processing
      And the claim status should be "Under Review"

    Example: Claim filed after coverage expiry is rejected
      Given a policy "POL-2024-001" with coverage from "2024-01-01" to "2024-12-31"
      And the current date is "2025-02-01"
      When the policyholder files a claim for an incident on "2024-12-20"
      Then the claim should be rejected
      And the rejection reason should be "Policy expired at time of filing"

  Rule: Claims below the deductible are the policyholder's responsibility

    Scenario Outline: Deductible determines payout amount
      Given a policy with a deductible of $<deductible>
      And an approved claim for $<claim_amount>
      When the claim payout is calculated
      Then the payout amount should be $<payout>

      Examples:
        | deductible | claim_amount | payout   |
        | 500        | 2,000        | 1,500.00 |
        | 500        | 500          | 0.00     |
        | 500        | 300          | 0.00     |
        | 1,000      | 5,000        | 4,000.00 |

  Rule: High-value claims require senior adjuster review

    Example: Claim over $10,000 is escalated
      Given an approved claim for $15,000.00
      When the claim is assigned for processing
      Then the claim should be assigned to a senior adjuster
      And the policyholder should be notified of the escalation
      And the expected processing time should be "10-15 business days"

    Example: Claim under $10,000 follows standard processing
      Given an approved claim for $3,000.00
      When the claim is assigned for processing
      Then the claim should follow standard processing
      And the expected processing time should be "3-5 business days"
```

---

## 3. Examples Using All Gherkin Features

### 3.1 Comprehensive Feature -- All Keywords in One File

This example demonstrates every Gherkin keyword in a single,
coherent feature file.

```gherkin
# language: en
@subscription @billing @sprint-42
Feature: Subscription management
  As a SaaS platform operator
  I want to manage customer subscriptions
  So that billing is accurate and customers can self-serve

  Subscription management covers plan selection, upgrades, downgrades,
  cancellations, and billing cycle management. This feature is critical
  to revenue operations.

  Background:
    Given the following subscription plans are available:
      | plan name  | monthly price | annual price | max users |
      | Starter    | $9.99         | $99.00       | 5         |
      | Pro        | $29.99        | $299.00      | 25        |
      | Enterprise | $99.99        | $999.00      | unlimited |
    And the current date is "2024-07-15"

  # --- Basic subscription scenarios ---

  Scenario: New customer subscribes to a plan
    Given a new customer "Acme Corp"
    When "Acme Corp" subscribes to the "Pro" plan with monthly billing
    Then "Acme Corp" should have an active "Pro" subscription
    And the next billing date should be "2024-08-15"
    And the billing amount should be "$29.99"

  # --- Rule keyword groups related business rules ---

  Rule: Upgrades are effective immediately and prorated

    Example: Mid-cycle upgrade from Starter to Pro
      Given "Acme Corp" has an active "Starter" subscription since "2024-07-01"
      When "Acme Corp" upgrades to the "Pro" plan on "2024-07-15"
      Then the "Pro" plan should be active immediately
      And the prorated charge should be calculated for the remaining 16 days
      And the next full billing cycle should use the "Pro" price

    Example: Upgrade preserves existing data and settings
      Given "Acme Corp" has an active "Starter" subscription
      And "Acme Corp" has 3 active users
      When "Acme Corp" upgrades to the "Pro" plan
      Then all 3 users should retain their access
      And all existing data should be preserved

  Rule: Downgrades take effect at the end of the billing cycle

    @pending
    Example: Downgrade is scheduled, not immediate
      Given "Acme Corp" has an active "Pro" subscription
      And the current billing period ends on "2024-08-01"
      When "Acme Corp" downgrades to the "Starter" plan
      Then the "Pro" plan should remain active until "2024-08-01"
      And the "Starter" plan should activate on "2024-08-01"
      And a confirmation email should be sent with the scheduled change date

  # --- Scenario Outline with multiple Examples tables ---

  Rule: User limits are enforced per plan

    Scenario Outline: Adding users up to plan limits
      Given a company on the "<plan>" plan with <current> users
      When the company attempts to add <add> more users
      Then the result should be "<outcome>"

      @happy-path
      Examples: Within limits
        | plan       | current | add | outcome  |
        | Starter    | 3       | 2   | success  |
        | Pro        | 20      | 5   | success  |
        | Starter    | 0       | 5   | success  |

      @edge-case
      Examples: Exceeding limits
        | plan       | current | add | outcome  |
        | Starter    | 5       | 1   | rejected |
        | Pro        | 25      | 1   | rejected |
        | Starter    | 4       | 3   | rejected |

      @enterprise
      Examples: Enterprise has no limits
        | plan       | current | add  | outcome |
        | Enterprise | 100     | 50   | success |
        | Enterprise | 500     | 500  | success |

  # --- Doc Strings for complex data ---

  Scenario: Subscription webhook sends JSON notification
    Given "Acme Corp" has an active "Pro" subscription
    When the subscription is renewed
    Then a webhook notification should be sent with the payload:
      """json
      {
        "event": "subscription.renewed",
        "customer": "Acme Corp",
        "plan": "Pro",
        "amount": 29.99,
        "currency": "USD",
        "next_renewal": "2024-09-15"
      }
      """

  # --- Data Tables for structured input ---

  Scenario: Bulk import of subscription data
    When the following subscriptions are imported:
      | customer      | plan       | billing | start date |
      | Alpha Inc     | Starter    | monthly | 2024-01-01 |
      | Beta LLC      | Pro        | annual  | 2024-03-15 |
      | Gamma Corp    | Enterprise | annual  | 2024-06-01 |
    Then 3 subscriptions should be created
    And each customer should receive a welcome email

  # --- Asterisk as generic step keyword ---

  Scenario: Subscription trial to paid conversion checklist
    Given a customer is on a 14-day trial of the "Pro" plan
    And the trial ends tomorrow
    * the customer has added a payment method
    * the customer has not cancelled the trial
    When the trial period expires
    Then the subscription should convert to a paid "Pro" plan
    And the first payment should be charged
```

**Keywords demonstrated:**

- `# language:` -- language declaration
- `@tags` -- at Feature, Rule, Scenario, Scenario Outline, and Examples levels
- `Feature:` with description and user story
- `Background:` with Data Table
- `Scenario:` (basic scenarios)
- `Rule:` with description, grouping related Examples
- `Example:` (synonym for Scenario, used within Rule blocks)
- `Scenario Outline:` with angle-bracket `<parameters>`
- `Examples:` -- multiple named Examples tables with different tags
- `Given`, `When`, `Then`, `And` -- step keywords
- `*` -- generic step keyword (asterisk)
- `"""` Doc String with content type annotation
- `|` Data Tables
- `#` Comments

### 3.2 Cucumber's Own Test Data -- Rule with Background

From the official Gherkin parser test suite (`cucumber/gherkin` repository):

```gherkin
Feature: Complex background
  To ensure PickleStep all have different IDs

  Background:
    Given the minimalism inside a background

  Scenario: minimalistic
    Given the minimalism

  Scenario: also minimalistic
    Given the minimalism

  Rule: My Rule

    Background:
      Given a rule background step

    Scenario Outline: with examples
      Given the <value>

      Examples:
        | value |
        | 1     |
        | 2     |
```

**Key insight:** This demonstrates that both the Feature and
individual Rules can have their own Background sections. The
Feature-level Background runs before every scenario in the
entire file, while the Rule-level Background runs only before
scenarios within
that Rule.

### 3.3 Cucumber's Own Test Data -- Highlander Rule Example

From the official Cucumber documentation:

```gherkin
Feature: Highlander

  Rule: There can be only One

    Background:
      Given there are 3 ninjas

    Example: Only One -- More than one alive
      Given there are more than one ninja alive
      When 2 ninjas meet, they will fight
      Then one ninja dies
      And there is one ninja less alive

    Example: Only One -- One alive
      Given there is only 1 ninja alive
      Then they will live forever ;-)

  Rule: There can be Two (in some cases)

    Example: Two -- Dead and Reborn as Phoenix
      Given there are 2 ninjas
      And one of them is a phoenix ninja
      When they fight
      Then the phoenix ninja dies
      And the phoenix ninja is reborn
```

*Source: [Cucumber Gherkin Reference](https://cucumber.io/docs/gherkin/reference/)*

### 3.4 Doc Strings with Content Types

From the Gherkin parser test suite, showing all Doc String variations:

```gherkin
Feature: DocStrings

  Scenario: A DocString with plain text
    Given a blog post named "Random" with body
      """
      Some Title, Eh?
      ===============
      Here is the first paragraph of my blog post.
      Keywords like Given, When, Then are not parsed inside Doc Strings.
      """

  Scenario: A DocString with content type
    Given a blog post named "Random" with Markdown body
      """markdown
      Some Title, Eh?
      ===============
      Here is the first paragraph of my blog post.
      """

  Scenario: A DocString with backtick delimiter
    Given a step with a doc string
      ```
      This uses backticks instead of triple quotes.
      Useful when your content contains triple quotes.
      ```

  Scenario: A DocString containing the other delimiter
    Given a step with a doc string
      ```
      This doc string contains """ triple quotes inside it.
      ```
```

### 3.5 Tags at Every Level

Demonstrating tag inheritance and organization:

```gherkin
@feature-tag @billing
Feature: Invoice generation

  @smoke @quick
  Scenario: Generate invoice for single item
    Given an order with one item
    When the invoice is generated
    Then the invoice should contain one line item

  @regression
  Rule: Tax calculation rules

    @domestic
    Scenario Outline: Domestic tax rates
      Given an order shipping to <state>
      When the invoice is generated
      Then the tax rate should be <rate>

      @us-states
      Examples: US states with sales tax
        | state      | rate  |
        | California | 7.25% |
        | Texas      | 6.25% |
        | New York   | 8.00% |

      @tax-free
      Examples: Tax-free states
        | state      | rate |
        | Oregon     | 0%   |
        | Montana    | 0%   |
```

**Tag inheritance chain:** A scenario in the "US states"
examples table inherits: `@feature-tag`, `@billing`,
`@regression`, `@domestic`, `@us-states` -- all five tags.

---

## 4. Domain-Specific Examples

### 4.1 E-Commerce -- Shopping Cart

```gherkin
@e-commerce @cart
Feature: Shopping cart management
  As a shopper
  I want to manage items in my shopping cart
  So that I can purchase the products I want

  Background:
    Given the following products are available:
      | name              | price | category    |
      | Running Shoes     | 89.99 | Footwear    |
      | Cotton T-Shirt    | 24.99 | Apparel     |
      | Sports Watch      | 199.99| Accessories |

  Scenario: Adding a product to an empty cart
    Given the shopping cart is empty
    When the customer adds "Running Shoes" to the cart
    Then the cart should contain 1 item
    And the cart total should be "$89.99"

  Scenario: Removing a product from the cart
    Given the cart contains "Running Shoes"
    When the customer removes "Running Shoes" from the cart
    Then the cart should be empty
    And the cart total should be "$0.00"

  Scenario: Updating product quantity
    Given the cart contains 1 "Cotton T-Shirt"
    When the customer changes the quantity to 3
    Then the cart should show 3 "Cotton T-Shirt"
    And the cart total should be "$74.97"

  Scenario: Cart persists across sessions
    Given the customer is logged in
    And the cart contains "Sports Watch"
    When the customer logs out and logs back in
    Then the cart should still contain "Sports Watch"

  Scenario: Applying a discount code
    Given the cart contains items totaling "$114.98"
    When the customer applies discount code "SAVE10"
    Then a 10% discount should be applied
    And the cart total should be "$103.48"
    And the discount should be shown as a line item

  Scenario: Empty cart displays appropriate message
    Given the shopping cart is empty
    When the customer views the cart
    Then a message "Your cart is empty" should be displayed
    And a "Continue Shopping" link should be available
```

### 4.2 Banking -- ATM Withdrawal

```gherkin
@banking @atm
Feature: ATM cash withdrawal
  As a bank customer
  I want to withdraw cash from an ATM
  So that I can have physical currency when I need it

  Background:
    Given the ATM has been stocked with $10,000
    And the customer's account has a balance of $1,000.00

  Rule: The ATM dispenses only valid denominations

    Scenario Outline: Valid withdrawal amounts
      When the customer requests $<amount>
      Then the ATM should dispense $<amount>
      And the account balance should be $<remaining>
      And the ATM should print a receipt

      Examples:
        | amount | remaining |
        | 20     | 980.00    |
        | 100    | 900.00    |
        | 500    | 500.00    |

    Scenario: Invalid amount rejected
      When the customer requests $35
      Then the ATM should display "Please enter a multiple of $20"
      And no cash should be dispensed
      And the account balance should remain $1,000.00

  Rule: Withdrawals must not exceed daily limits or available balance

    Scenario: Withdrawal exceeding balance is declined
      When the customer requests $1,200
      Then the ATM should display "Insufficient funds"
      And no cash should be dispensed

    Scenario: Daily limit prevents excessive withdrawal
      Given the daily withdrawal limit is $500
      And the customer has already withdrawn $400 today
      When the customer requests $200
      Then the ATM should display "Daily limit exceeded"
      And no cash should be dispensed

  Rule: The card is retained after too many PIN failures

    Scenario: Card retained after 3 wrong PIN attempts
      Given the customer has entered the wrong PIN 2 times
      When the customer enters the wrong PIN again
      Then the ATM should retain the card
      And the ATM should display "Card retained. Please contact your bank."
      And the account should be flagged for security review
```

### 4.3 REST API Specification

```gherkin
@api @v2 @users
Feature: User management API
  As an API consumer
  I want to manage users through the REST API
  So that I can integrate user management into my application

  Background:
    Given the API base URL is "/api/v2"
    And the client is authenticated with a valid API key

  Scenario: Create a new user
    When the client sends a POST request to "/users" with body:
      """json
      {
        "name": "Jane Doe",
        "email": "jane.doe@example.com",
        "role": "editor"
      }
      """
    Then the response status code should be 201
    And the response body should contain:
      | field      | value                |
      | name       | Jane Doe             |
      | email      | jane.doe@example.com |
      | role       | editor               |
    And the response should include a "Location" header
    And the response should include a generated "id" field

  Scenario: Retrieve an existing user
    Given a user exists with id "usr-123"
    When the client sends a GET request to "/users/usr-123"
    Then the response status code should be 200
    And the response body should contain the user's details

  Scenario: Update a user with partial data
    Given a user exists with id "usr-123" and name "Jane Doe"
    When the client sends a PATCH request to "/users/usr-123" with body:
      """json
      {
        "name": "Jane Smith"
      }
      """
    Then the response status code should be 200
    And the user's name should be updated to "Jane Smith"
    And all other fields should remain unchanged

  Scenario: Delete a user
    Given a user exists with id "usr-123"
    When the client sends a DELETE request to "/users/usr-123"
    Then the response status code should be 204
    And the user should no longer exist in the system

  Scenario Outline: API error responses for invalid requests
    When the client sends a <method> request to "<endpoint>"
    Then the response status code should be <status>
    And the response body should contain error "<message>"

    Examples:
      | method | endpoint           | status | message           |
      | GET    | /users/nonexistent | 404    | User not found    |
      | POST   | /users             | 400    | Validation failed |
      | DELETE | /users/nonexistent | 404    | User not found    |

  Scenario: API validates authentication
    Given the client has no API key
    When the client sends a GET request to "/users"
    Then the response status code should be 401
    And the response body should contain error "Authentication required"
```

### 4.4 UI Specification -- Dashboard

```gherkin
@ui @dashboard
Feature: Analytics dashboard
  As a marketing manager
  I want to view an analytics dashboard
  So that I can monitor campaign performance at a glance

  Background:
    Given the user is logged in as a marketing manager
    And there are active campaigns with performance data

  Scenario: Dashboard displays key metrics on load
    When the user navigates to the dashboard
    Then the following metric cards should be displayed:
      | metric             | format    |
      | Total Impressions  | number    |
      | Click-Through Rate | percent   |
      | Conversions        | number    |
      | Revenue            | currency  |
    And the data should reflect the current month by default

  Scenario: Filtering dashboard by date range
    Given the dashboard is displayed
    When the user selects the date range "2024-01-01" to "2024-03-31"
    Then all metrics should update to reflect the selected period
    And the date range selector should show "Jan 1 - Mar 31, 2024"

  Scenario: Exporting dashboard data
    Given the dashboard is displaying data for "March 2024"
    When the user clicks the "Export" button
    And selects "CSV" format
    Then a CSV file should be downloaded
    And the file should contain all visible metrics
    And the filename should include the date range
```

### 4.5 Data Processing -- ETL Pipeline

```gherkin
@data @etl @nightly
Feature: Customer data synchronization
  As a data engineer
  I want customer data synchronized between systems
  So that all departments work with consistent information

  Background:
    Given the source CRM system is accessible
    And the target data warehouse is accessible

  Rule: New records are inserted into the target

    Example: New customers are synchronized
      Given the source contains 5 customers not in the target
      When the synchronization job runs
      Then 5 new records should be inserted in the target
      And the sync log should show "5 inserts, 0 updates, 0 deletes"

  Rule: Modified records are updated in the target

    Example: Updated customer information is synchronized
      Given customer "C-001" exists in both systems
      And the source has a newer email address for "C-001"
      When the synchronization job runs
      Then customer "C-001" in the target should have the updated email
      And the last_modified timestamp should be updated

  Rule: Synchronization handles errors gracefully

    Example: Network interruption during sync
      Given the synchronization job is running
      And 50 of 100 records have been processed
      When the network connection is interrupted
      Then the job should retry 3 times with exponential backoff
      And if all retries fail, the job should log the failure
      And already-processed records should not be rolled back
      And the operations team should be notified

    Example: Invalid data is quarantined
      Given the source contains a record with an invalid email format
      When the synchronization job runs
      Then the invalid record should be moved to the quarantine table
      And the remaining records should be processed normally
      And the sync report should include the quarantine details:
        | field        | value                           |
        | record_id    | C-042                           |
        | field        | email                           |
        | value        | not-an-email                    |
        | reason       | Invalid email format            |
```

### 4.6 Notification System -- Multi-channel

```gherkin
@notifications
Feature: Multi-channel notification delivery
  As a platform
  I want to send notifications through multiple channels
  So that users receive timely alerts through their preferred method

  Background:
    Given the following users with notification preferences:
      | user    | email              | sms         | push | preferences       |
      | Alice   | alice@example.com  | +1555000111 | yes  | email, push       |
      | Bob     | bob@example.com    | +1555000222 | yes  | sms, push         |
      | Charlie | charlie@example.com| +1555000333 | no   | email             |

  Rule: Notifications are sent only to preferred channels

    Example: User receives notification through preferred channels only
      When a "payment received" notification is triggered for Alice
      Then an email should be sent to "alice@example.com"
      And a push notification should be sent to Alice's device
      But no SMS should be sent to Alice

  Rule: Critical notifications override channel preferences

    Example: Security alert goes to all available channels
      When a "suspicious login" security alert is triggered for Bob
      Then an email should be sent to "bob@example.com"
      And an SMS should be sent to "+1555000222"
      And a push notification should be sent to Bob's device

  Scenario Outline: Notification delivery confirmation
    Given a <channel> notification is sent to <user>
    When the delivery is <status>
    Then the notification log should record status as "<log_status>"

    Examples:
      | channel | user    | status     | log_status |
      | email   | Alice   | delivered  | delivered  |
      | email   | Alice   | bounced    | failed     |
      | sms     | Bob     | delivered  | delivered  |
      | sms     | Bob     | timed out  | retry      |
      | push    | Alice   | delivered  | delivered  |
      | push    | Alice   | rejected   | failed     |
```

---

## 5. Good vs Bad Examples

### 5.1 Imperative vs Declarative Style

**BAD -- Imperative (too detailed, UI-coupled):**

```gherkin
# BAD: This reads like a test script, not a specification
Feature: User login

  Scenario: Successful login
    Given I open the browser
    And I navigate to "https://app.example.com/login"
    And I wait for the page to load
    When I click on the "email" input field
    And I type "user@example.com" in the email field
    And I click on the "password" input field
    And I type "SecurePass123" in the password field
    And I click the "Log In" button
    And I wait 3 seconds
    Then I should see the text "Welcome" on the page
    And the URL should be "https://app.example.com/dashboard"
```

**GOOD -- Declarative (behavior-focused):**

```gherkin
# GOOD: Describes WHAT happens, not HOW
Feature: User login

  Scenario: Successful login with valid credentials
    Given a registered user with email "user@example.com"
    When the user logs in with valid credentials
    Then the user should be on their dashboard
    And a welcome message should be displayed
```

**Why the declarative version is better:**

- Resilient to UI changes (redesign, different framework, mobile vs web)
- Readable by non-technical stakeholders
- Focuses on business behavior
- Implementation details live in step definitions, where they belong
- Shorter and easier to maintain

*Source: [Cucumber -- Better Gherkin](https://cucumber.io/docs/bdd/better-gherkin/)*

### 5.2 Multiple Behaviors vs Single Behavior

**BAD -- Multiple behaviors in one scenario:**

```gherkin
# BAD: Tests two things -- search AND image filter
Feature: Google Searching

  Scenario: Google Image search shows pictures
    Given the user opens a web browser
    And the user navigates to "https://www.google.com/"
    When the user enters "panda" into the search bar
    Then links related to "panda" are shown on the results page
    When the user clicks on the "Images" link at the top of the results page
    Then images related to "panda" are shown on the results page
```

**GOOD -- One behavior per scenario:**

```gherkin
# GOOD: Each scenario tests exactly one behavior
Feature: Google Searching

  Scenario: Search from the search bar
    Given a web browser is at the Google home page
    When the user enters "panda" into the search bar
    Then links related to "panda" are shown on the results page

  Scenario: Image search
    Given Google search results for "panda" are shown
    When the user clicks on the "Images" link
    Then images related to "panda" are shown on the results page
```

**Key principle:** "One Scenario, One Behavior" -- the cardinal
rule of BDD. The second scenario uses the result of the first
as its Given (precondition), creating a clear chain without
coupling.

*Source: [Automation Panda -- BDD 101](https://automationpanda.com/2017/01/30/bdd-101-writing-good-gherkin/)*

### 5.3 Inconsistent vs Consistent Language

**BAD -- Mixed tense, no subjects, inconsistent voice:**

```gherkin
# BAD: Tense shifts, incomplete sentences, poor grammar
Scenario: Google search result page elements
  Given the user navigates to the Google home page
  When the user entered "panda" at the search bar
  Then the results page shows links related to "panda"
  And image links for "panda"
  And video links for "panda"
```

Problems:

- "navigates" (present) then "entered" (past) -- tense shift
- "image links for panda" -- no verb, incomplete sentence
- "video links for panda" -- same problem

**GOOD -- Consistent tense, complete sentences:**

```gherkin
# GOOD: Present tense, third person, complete sentences
Scenario: Search results display multiple content types
  Given the Google home page is displayed
  When the user searches for "panda"
  Then the results page shows links related to "panda"
  And the results page shows image links for "panda"
  And the results page shows video links for "panda"
```

*Source: [Automation Panda -- BDD 101](https://automationpanda.com/2017/01/30/bdd-101-writing-good-gherkin/)*

### 5.4 Hardcoded Duplication vs Scenario Outline

**BAD -- Duplicated scenarios with hardcoded values:**

```gherkin
# BAD: Copy-paste with only values changed
Feature: Mario controls

  Scenario: Mario jumps with A button
    Given a level is started
    When the player pushes the "A" button
    Then Mario jumps straight up

  Scenario: Mario jumps with B button
    Given a level is started
    When the player pushes the "B" button
    Then Mario jumps straight up
```

**GOOD -- Scenario Outline eliminates duplication:**

```gherkin
# GOOD: Parameterized scenario, no duplication
Feature: Mario controls

  Scenario Outline: Mario jumps
    Given a level is started
    When the player pushes the "<button>" button
    Then Mario jumps straight up

    Examples: Jump buttons
      | button |
      | A      |
      | B      |
```

*Source: [Automation Panda -- BDD 101](https://automationpanda.com/2017/01/30/bdd-101-writing-good-gherkin/)*

### 5.5 Poor Style vs Professional Style

**BAD -- Sloppy formatting, spelling, and tagging:**

```gherkin
# BAD: Everything wrong
 @AUTOMATE @Automated @automation @Sprint32GoogleSearchFeature
Scenario outline: GOOGLE STUFF
Given a Web Browser is on the Google page,
when The seach phrase "<phrase>" Enter,
Then  "<phrase>" shown.
and The relatedd   results include "<related>".

Examples: animals
| phrase | related |
| panda | Panda Express        |
| elephant    | elephant Man  |
```

Problems:

- Inconsistent/excessive tags
- ALL CAPS in title
- Misspellings ("seach", "relatedd")
- Punctuation at end of lines
- Inconsistent capitalization of keywords ("when", "Then")
- Unaligned table columns
- Missing Feature keyword entirely

**GOOD -- Professional formatting:**

```gherkin
@search @regression
Feature: Google search suggestions

  Scenario Outline: Search displays related results
    Given the Google search page is displayed
    When the user searches for "<phrase>"
    Then results related to "<phrase>" are displayed
    And the related results include "<related>"

    Examples: Popular searches
      | phrase   | related       |
      | panda    | Panda Express |
      | elephant | Elephant Man  |
```

*Source: [Automation Panda -- BDD 101](https://automationpanda.com/2017/01/30/bdd-101-writing-good-gherkin/)*

### 5.6 Testing Implementation vs Testing Behavior

**BAD -- Tests the implementation (database queries, HTTP methods):**

```gherkin
# BAD: Coupled to implementation details
Scenario: User profile update
  Given a row exists in the users table with id 42
  When a PUT request is sent to /api/users/42 with JSON payload
  And the SQL query "UPDATE users SET name='New Name' WHERE id=42" executes
  Then the HTTP response code should be 200
  And the users table row with id 42 should have name "New Name"
```

**GOOD -- Tests the behavior (what the user/system does):**

```gherkin
# GOOD: Describes business behavior, not implementation
Scenario: User updates their display name
  Given a user exists with the display name "Old Name"
  When the user changes their display name to "New Name"
  Then the user's profile should show "New Name"
  And the change should be reflected across the platform
```

---

## 6. Template Structures

### 6.1 Basic Feature Template

```gherkin
@domain-tag
Feature: [Feature name]
  As a [role]
  I want [capability]
  So that [business value]

  Background:
    Given [common precondition for all scenarios]

  Scenario: [Happy path description]
    Given [specific precondition]
    When [action]
    Then [expected outcome]

  Scenario: [Edge case or error case description]
    Given [specific precondition]
    When [action that should fail or trigger edge case]
    Then [expected error handling or alternative outcome]
```

### 6.2 CRUD Operations Template

```gherkin
@resource-name @crud
Feature: [Resource] management
  As a [role]
  I want to manage [resources]
  So that [business value]

  Background:
    Given [the system is in a known state]

  # --- Create ---
  Scenario: Create a new [resource] with valid data
    When the user creates a [resource] with the following details:
      | field   | value     |
      | field_1 | value_1   |
      | field_2 | value_2   |
    Then the [resource] should be created successfully
    And the [resource] should appear in the list

  Scenario: Cannot create a [resource] with invalid data
    When the user attempts to create a [resource] with missing required fields
    Then the creation should be rejected
    And a validation error should be displayed

  # --- Read ---
  Scenario: View [resource] details
    Given a [resource] exists with id "[id]"
    When the user views the [resource] details
    Then all [resource] information should be displayed

  Scenario: List all [resources] with pagination
    Given 25 [resources] exist
    When the user views the [resource] list
    Then the first 10 [resources] should be displayed
    And pagination controls should be available

  # --- Update ---
  Scenario: Update an existing [resource]
    Given a [resource] exists with [field] "[old value]"
    When the user updates [field] to "[new value]"
    Then [field] should be changed to "[new value]"
    And the modification timestamp should be updated

  # --- Delete ---
  Scenario: Delete an existing [resource]
    Given a [resource] exists with id "[id]"
    When the user deletes the [resource]
    Then the [resource] should no longer exist
    And a confirmation message should be displayed

  Scenario: Cannot delete a [resource] that is in use
    Given a [resource] exists that is referenced by other records
    When the user attempts to delete the [resource]
    Then the deletion should be prevented
    And an error "Cannot delete: resource is in use" should be displayed
```

### 6.3 Authentication and Authorization Template

```gherkin
@auth @security
Feature: [Feature] access control
  As a system administrator
  I want to control access to [feature]
  So that only authorized users can perform sensitive actions

  # --- Authentication ---
  Rule: Users must be authenticated to access [feature]

    Example: Unauthenticated user is redirected to login
      Given the user is not logged in
      When the user attempts to access the [feature]
      Then the user should be redirected to the login page

    Example: Authenticated user can access [feature]
      Given the user is logged in
      When the user navigates to the [feature]
      Then the [feature] should be displayed

  # --- Authorization ---
  Rule: Only users with appropriate roles can perform actions

    Scenario Outline: Role-based access control
      Given the user is logged in with role "<role>"
      When the user attempts to <action>
      Then the action should be <result>

      Examples:
        | role    | action              | result  |
        | admin   | view settings       | allowed |
        | admin   | modify settings     | allowed |
        | editor  | view settings       | allowed |
        | editor  | modify settings     | denied  |
        | viewer  | view settings       | allowed |
        | viewer  | modify settings     | denied  |

  # --- Session management ---
  Rule: Sessions expire after inactivity

    Example: Session expires after 30 minutes of inactivity
      Given the user is logged in
      And the user has been inactive for 30 minutes
      When the user attempts any action
      Then the session should be expired
      And the user should be redirected to the login page
      And a message "Session expired. Please log in again." should be displayed
```

### 6.4 Validation Rules Template (Scenario Outline pattern)

```gherkin
@validation
Feature: [Form/Input] validation
  As a [user role]
  I want input to be validated
  So that only correct data enters the system

  Scenario Outline: [Field] validation
    Given the user is on the [form] page
    When the user enters "<value>" in the [field] field
    And the user submits the form
    Then the result should be "<outcome>"
    And the message should be "<message>"

    @valid
    Examples: Valid inputs
      | value              | outcome  | message           |
      | valid_value_1      | accepted | Success           |
      | valid_value_2      | accepted | Success           |
      | edge_case_value    | accepted | Success           |

    @invalid
    Examples: Invalid inputs
      | value              | outcome  | message                  |
      |                    | rejected | Field is required        |
      | too_short          | rejected | Minimum 8 characters     |
      | invalid_format     | rejected | Invalid format           |

    @boundary
    Examples: Boundary values
      | value              | outcome  | message                  |
      | exactly_min_length | accepted | Success                  |
      | exactly_max_length | accepted | Success                  |
      | one_over_max       | rejected | Maximum exceeded         |
```

### 6.5 Event-Driven / Workflow Template

```gherkin
@workflow
Feature: [Process] workflow
  As a [role]
  I want [process] to follow defined stages
  So that [business value]

  Rule: [Process] moves through stages in order

    Example: [Entity] progresses from [Stage A] to [Stage B]
      Given a [entity] in "[Stage A]" status
      When [trigger action]
      Then the [entity] status should change to "[Stage B]"
      And [side effect, e.g., notification sent]
      And the state change should be recorded in the audit log

    Example: [Entity] cannot skip stages
      Given a [entity] in "[Stage A]" status
      When an attempt is made to move it to "[Stage C]"
      Then the transition should be rejected
      And the [entity] should remain in "[Stage A]" status

  Rule: Only authorized roles can trigger stage transitions

    Scenario Outline: Stage transition permissions
      Given a [entity] in "<from_stage>" status
      And the user has the "<role>" role
      When the user attempts to transition to "<to_stage>"
      Then the transition should be "<result>"

      Examples:
        | from_stage | to_stage  | role      | result  |
        | Draft      | Submitted | author    | allowed |
        | Draft      | Submitted | viewer    | denied  |
        | Submitted  | Approved  | manager   | allowed |
        | Submitted  | Approved  | author    | denied  |
        | Approved   | Published | publisher | allowed |

  Rule: Rejected items return to the previous stage with feedback

    Example: Rejection includes reason and returns to author
      Given a [entity] in "Submitted" status
      When the reviewer rejects the [entity] with reason "Incomplete data"
      Then the [entity] status should change to "Draft"
      And the author should be notified with the rejection reason
      And the rejection should appear in the [entity] history
```

### 6.6 API Error Handling Template

```gherkin
@api @errors
Feature: API error handling
  As an API consumer
  I want consistent error responses
  So that I can handle failures gracefully in my application

  Rule: All errors follow a standard response format

    Scenario: Error response includes standard fields
      When an error occurs during API processing
      Then the response should contain:
        | field     | description                           |
        | status    | HTTP status code                      |
        | error     | Short error identifier                |
        | message   | Human-readable description            |
        | timestamp | ISO 8601 timestamp                    |
        | path      | The request path that caused the error|

  Rule: Validation errors include field-level details

    Example: Multiple validation errors returned together
      When the client sends a POST request with invalid data:
        """json
        {
          "name": "",
          "email": "not-an-email",
          "age": -5
        }
        """
      Then the response status code should be 400
      And the response should contain validation errors:
        | field | error                          |
        | name  | Name is required               |
        | email | Invalid email format           |
        | age   | Age must be a positive number  |

  Rule: Rate limiting returns appropriate headers

    Example: Rate limit exceeded
      Given the client has made 100 requests in the last minute
      When the client sends another request
      Then the response status code should be 429
      And the response should include headers:
        | header               | description                |
        | X-RateLimit-Limit    | Maximum requests per window|
        | X-RateLimit-Remaining| Requests remaining         |
        | Retry-After          | Seconds until reset        |
```

### 6.7 Data Import/Export Template

```gherkin
@data @import
Feature: [Data type] import
  As a [role]
  I want to import [data] from files
  So that I can bulk-load information efficiently

  Rule: Valid files are imported successfully

    Example: Import a well-formed CSV file
      Given the user has a CSV file with 100 valid records
      When the user uploads the file for import
      Then 100 records should be imported
      And a success message should display "100 records imported"

    Example: Import results are summarized
      Given the user has imported a file
      Then the import summary should show:
        | metric     | value |
        | Total rows | 100   |
        | Imported   | 95    |
        | Skipped    | 3     |
        | Errors     | 2     |

  Rule: Invalid data is reported without blocking valid records

    Example: Partial import with errors
      Given the user has a CSV file with 5 valid and 2 invalid records
      When the user uploads the file for import
      Then 5 records should be imported
      And 2 errors should be reported with row numbers and reasons

  Rule: Only supported file formats are accepted

    Scenario Outline: File format validation
      When the user attempts to upload a file named "<filename>"
      Then the upload should be "<result>"

      Examples:
        | filename       | result   |
        | data.csv       | accepted |
        | data.xlsx      | accepted |
        | data.json      | accepted |
        | data.txt       | rejected |
        | data.exe       | rejected |
        | image.png      | rejected |
```

### 6.8 Multi-Step Wizard / Form Template

```gherkin
@wizard @onboarding
Feature: [Process] wizard
  As a [role]
  I want to complete [process] through a guided wizard
  So that I don't miss any required steps

  Background:
    Given the user has started the [process] wizard

  Rule: The wizard enforces step completion order

    Example: User must complete Step 1 before Step 2
      Given the user has not completed Step 1
      When the user attempts to navigate to Step 2
      Then the user should remain on Step 1
      And a message "Please complete this step first" should be displayed

    Example: User can go back to previous steps
      Given the user is on Step 3
      When the user navigates back to Step 1
      Then Step 1 should be displayed with previously entered data

  Rule: Progress is saved between sessions

    Example: User can resume an incomplete wizard
      Given the user has completed Steps 1 and 2
      And the user leaves the wizard
      When the user returns to the wizard
      Then the user should resume at Step 3
      And Steps 1 and 2 data should be preserved

  Rule: All steps must be complete before final submission

    Example: Summary page shows data from all steps
      Given the user has completed all wizard steps
      When the user reaches the summary page
      Then data from all steps should be displayed for review
      And the user should be able to edit any step
      And a "Submit" button should be available

    Example: Incomplete wizard cannot be submitted
      Given the user has completed only Steps 1 and 2 of 4
      Then the "Submit" button should not be available
      And the progress indicator should show "2 of 4 steps complete"
```

---

## 7. Sources and References

### Official Documentation

- **Cucumber Gherkin Reference**:
  <https://cucumber.io/docs/gherkin/reference/>
  The authoritative syntax reference with examples of every
  keyword.
- **Cucumber BDD -- Better Gherkin**:
  <https://cucumber.io/docs/bdd/better-gherkin/>
  Official best practices for writing declarative,
  behavior-focused scenarios.
- **Cucumber 10-Minute Tutorial**:
  <https://cucumber.io/docs/guides/10-minute-tutorial/>
  Beginner tutorial showing progressive refinement from
  Scenario to Scenario Outline.

### Open-Source Projects Using Gherkin

- **cucumber/cucumber-js** (`features/` directory):
  ~80 feature files testing Cucumber.js itself -- includes
  hooks, rules, scenario outlines, data tables, doc strings,
  tags, formatters, and more.
  <https://github.com/cucumber/cucumber-js/tree/main/features>
- **cucumber/gherkin** (`testdata/good/` directory):
  Canonical test files for the Gherkin parser -- minimal but
  correct examples of every syntax feature.
  <https://github.com/cucumber/gherkin/tree/main/testdata/good>
- **cucumber/cucumber-jvm** (`test/resources/` directories):
  Java-ecosystem examples including Rule usage and scenario outlines.
  <https://github.com/cucumber/cucumber-jvm>
- **behave/behave** (`features/` directory):
  Python BDD framework using Gherkin, extensive real-world features.
  <https://github.com/behave/behave/tree/main/features>

### Best Practice Guides

- **Automation Panda -- BDD 101: Writing Good Gherkin**:
  <https://automationpanda.com/2017/01/30/bdd-101-writing-good-gherkin/>
  Comprehensive guide with good vs bad examples and anti-patterns.
- **BDD Books** (by Seb Rose and Gaspar Nagy):
  - *Discovery* -- exploring behavior using examples
  - *Formulation* -- expressing examples as Given/When/Then
  <https://www.bddbooks.com/>

### Anti-Pattern Summary

| Anti-Pattern                    | Problem                   | Fix                                |
|---------------------------------|---------------------------|------------------------------------|
| Imperative steps                | UI-coupled, fragile       | Use declarative language           |
| Multiple behaviors per scenario | Hard to diagnose failures | One scenario, one behavior         |
| Inconsistent tense/voice        | Confusing to read         | Present tense, third person        |
| Hardcoded duplication           | Maintenance burden        | Use Scenario Outline               |
| Testing implementation          | Brittle, not readable     | Test behavior, not code            |
| Long scenarios (>10 steps)      | Hard to understand        | Split or use Background            |
| Missing Background              | Repetitive Given steps    | Extract shared preconditions       |
| Overloaded Scenario Outline     | Too many columns/rows     | Split into focused outlines        |
| No tags                         | Cannot filter test runs   | Tag by feature, priority, type     |
| Non-existent "Or" keyword       | Gherkin has no Or         | Use Scenario Outline for variants  |
