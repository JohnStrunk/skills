# Gherkin for Software Specification

A comprehensive guide to using Gherkin as a specification language for software
systems, focusing on the specification aspect rather than test automation.

---

## Table of Contents

1. [Gherkin as Living Documentation](#1-gherkin-as-living-documentation)
2. [Using Gherkin for Requirements Specification](#2-using-gherkin-for-requirements-specification)
3. [Specification by Example (SbE)](#3-specification-by-example-sbe)
4. [Feature File as a Specification Document](#4-feature-file-as-a-specification-document)
5. [Mapping User Stories to Gherkin Features](#5-mapping-user-stories-to-gherkin-features)
6. [Edge Cases and Error Scenarios](#6-edge-cases-and-error-scenarios)
7. [Non-Functional Requirements in Gherkin](#7-non-functional-requirements-in-gherkin)
8. [Completeness of Specifications](#8-completeness-of-specifications)
9. [The Rule Keyword: Grouping Business Rules](#9-the-rule-keyword-grouping-business-rules)
10. [Organizing Specs for Complex Systems](#10-organizing-specs-for-complex-systems)
11. [Declarative vs. Imperative Style](#11-declarative-vs-imperative-style)
12. [Ubiquitous Language and Domain-Driven Design](#12-ubiquitous-language-and-domain-driven-design)
13. [Real-World Examples](#13-real-world-examples)
14. [Key References and Further Reading](#14-key-references-and-further-reading)

---

## 1. Gherkin as Living Documentation

### The Core Idea

Traditional requirement documents become outdated the moment code
changes. Gherkin feature files solve this problem by serving a
dual purpose: they are both **human-readable specifications** and
**executable tests**. Because they are tied
to automated tests that run regularly, they create a "living" record of how the
system works, always reflecting its current state.

Gojko Adzic defined Living Documentation in his book *Specification by Example*
as "a source of information about system functionality that's as reliable as
programming language code but much easier to access and understand."

### Why Feature Files Are Better Than Traditional Specs

| Aspect        | Traditional Spec Document     | Gherkin Feature File                    |
|---------------|-------------------------------|-----------------------------------------|
| Freshness     | Stale within days of writing  | Always current (validated by CI)        |
| Ambiguity     | Prone to interpretation gaps  | Concrete examples eliminate ambiguity   |
| Audience      | Usually only BAs or PMs       | Readable by all stakeholders            |
| Verifiability | Manual review required        | Automatically verified against code     |
| Location      | Separate wiki/Confluence page | Lives alongside code in version control |

### How It Works in Practice

A Gherkin feature file is versioned in source control alongside the code it
specifies. When the CI pipeline runs, the feature files are parsed by a test
runner (Cucumber, SpecFlow, Behave, etc.) and executed against the
system. If the
system's behavior diverges from the specification, the build fails. This means
the specification can never silently drift out of sync with the implementation.

The key insight is that living documentation is not a report of test results. It
is a dynamic, human-readable record of each verified feature. Unlike test
reports, which are transient artifacts, living documentation represents the
ongoing contract between stakeholders and the development team.

### Benefits for Developers

For developers specifically, living documentation provides:

- **A reliable reference** when implementing features or fixing bugs. You read
  the feature file to understand what the system is supposed to do.
- **Regression safety**. If you change behavior that a feature file specifies,
  the build tells you immediately.
- **Onboarding aid**. New team members can read the feature files to understand
  the system's behavior without needing to reverse-engineer the code.

---

## 2. Using Gherkin for Requirements Specification

### From User Stories to Executable Requirements

User stories describe what users want to accomplish and why, following the
familiar format:

```text
As a [role],
I want [capability],
So that [benefit].
```

Gherkin acceptance criteria define the specific conditions that must be met for
the user story to be considered complete. They transform abstract requirements
into concrete, testable scenarios.

Sometimes these are called "Gherkin User Stories," but technically
the user story
expresses a business need while Gherkin expresses scenarios that validate the
story is correctly implemented.

### The Given-When-Then Structure as Requirements Language

The Given-When-Then pattern provides a natural structure for requirements:

- **Given** establishes the preconditions (the world as it exists before the
  action).
- **When** describes the action or event (what the user does, or what happens).
- **Then** specifies the expected outcome (what must be true after the action).

This structure forces precision. Instead of writing "the system should handle
invalid input gracefully," you write:

```gherkin
Scenario: User enters an invalid email address
  Given the user is on the registration page
  When the user enters "not-an-email" as their email address
  And the user submits the form
  Then the system displays "Please enter a valid email address"
  And the registration is not created
```

### Why Gherkin Requirements Are Better Than Prose

Research shows that **56% of software defects are introduced during the
requirements and design stages**. Gherkin addresses this by:

1. **Forcing concreteness**. You cannot write a Gherkin scenario without
   specifying concrete inputs, actions, and expected outputs.
2. **Eliminating ambiguity**. Natural-language prose is inherently ambiguous.
   Gherkin's structured format constrains the language enough to reduce
   misinterpretation.
3. **Enabling early validation**. Teams can review scenarios before any code is
   written, catching misunderstandings when they are cheapest to fix.
4. **Reducing rework**. Well-written acceptance criteria reduce back-and-forth
   questions by an estimated 60% and cut story refinement time in half.

### A Requirement, Not a Script

A critical distinction: Gherkin is for writing **requirements**,
not **scripts**. A script is a sequence of actions to be performed
(which may or may not be related). A requirement has a value or a
business purpose. When you find yourself
writing step-by-step UI interactions ("click this button, fill in that field"),
you have crossed from specification into scripting.

Good requirement (declarative):

```gherkin
Scenario: Successful login
  Given a registered user with valid credentials
  When the user logs in
  Then the user sees their dashboard
```

Bad script (imperative):

```gherkin
Scenario: Successful login
  Given the user navigates to "/login"
  When the user enters "alice@example.com" in the "email" field
  And the user enters "password123" in the "password" field
  And the user clicks the "Sign In" button
  Then the page URL should be "/dashboard"
  And the element "#welcome-message" should contain "Welcome, Alice"
```

The first version specifies *what*. The second specifies *how* (and will break
the moment the UI changes).

---

## 3. Specification by Example (SbE)

### The Methodology

Specification by Example (SbE) is a collaborative approach to defining software
requirements using concrete examples to illustrate expected behavior. It was
formalized by Gojko Adzic and is closely related to BDD (Behavior-Driven
Development), though the two are not identical.

SbE treats development as **a process of constant discovery through reducing
uncertainty about requirements**. The model of the system is not fully defined
from the beginning --- it is only defined well enough. It evolves continuously
based on feedback from stakeholders, and new examples and domain concepts enter
the specification as new elements are added to the code.

### SbE Process Patterns

The SbE method consists of several key process patterns:

1. **Deriving scope from goals**. Start with business goals and derive the scope
   of work from them, rather than starting with a solution.
2. **Illustrating specifications using examples**. Instead of writing abstract
   rules, illustrate them with concrete examples of inputs and expected outputs.
3. **Refining the specifications**. Collaboratively refine the examples until
   they are precise, unambiguous, and agreed upon by all stakeholders.
4. **Automating the specifications**. When the team agrees on a specification
   with key examples, automate them as tests.
5. **Validating frequently**. Keep the system and the executable specification
   constantly synchronized by running them regularly.

### How Gherkin Fits In

Gherkin is the most widely used language for expressing SbE specifications. It
provides:

- A **structured format** (Feature / Rule / Scenario / Given-When-Then) that
  maps naturally to the SbE process.
- **Machine-processability**. Because Gherkin has a formally defined syntax,
  feature files can be parsed and executed by tools like Cucumber.
- **Human readability**. Gherkin is a domain-specific language that can be
  understood by product owners, developers, and QA --- all the roles involved in
  software development.

### The Key Distinction: SbE vs. Test Automation

A common pitfall that Seb Rose and others have pointed out:

> "I see far more people using Given/When/Then for test automation than to
> support BDD/SbE."

Many teams confuse BDD with "test automation using Given-When-Then syntax."
The point of SbE is **collaborative specification** --- using examples to build
shared understanding. The automation is a valuable byproduct, not the primary
goal. Teams that skip the collaborative discovery phase and jump straight to
writing Gherkin as test scripts miss the most valuable part of the process.

### The Two Layers of Executable Specification

As Kamil Nicieja describes in *Writing Great Specifications*, an executable
specification has two layers:

1. **The specification layer**: The document you read when you want to know what
   you are going to build. This layer contains acceptance criteria, scenarios,
   and ubiquitous language.
2. **The automation layer**: The step definitions and supporting code that
   connect the specification to the system under test.

The specification layer is the one that matters for developers reading the spec.
The automation layer is an implementation detail.

---

## 4. Feature File as a Specification Document

### Structure of a Feature File

A well-structured feature file reads like a specification document:

```gherkin
Feature: Shopping cart checkout
  As a customer with items in my cart,
  I want to complete a purchase,
  So that I receive the products I selected.

  Background:
    Given the product catalog contains the following items:
      | SKU    | Name           | Price  | Stock |
      | WDG-01 | Blue Widget    | $10.00 | 100   |
      | WDG-02 | Red Widget     | $15.00 | 5     |
      | WDG-03 | Gold Widget    | $99.00 | 0     |

  Rule: Customers can only purchase items that are in stock

    Scenario: Purchasing an in-stock item
      Given the customer has added 2 "Blue Widget" to their cart
      When the customer proceeds to checkout
      Then the order total is $20.00
      And the order is placed successfully

    Scenario: Attempting to purchase an out-of-stock item
      Given the customer has added 1 "Gold Widget" to their cart
      When the customer proceeds to checkout
      Then the system informs the customer that "Gold Widget" is out of stock
      And no order is placed

  Rule: Stock is reserved during checkout to prevent overselling

    Scenario: Two customers compete for limited stock
      Given customer A has added 3 "Red Widget" to their cart
      And customer B has added 3 "Red Widget" to their cart
      When customer A proceeds to checkout
      Then customer A's order is placed successfully for 3 items
      When customer B proceeds to checkout
      Then customer B is informed that only 2 "Red Widget" remain
```

### What Makes a Good Specification vs. a Good Test

A feature file must serve both purposes simultaneously, but the
priorities differ:

| Aspect         | Good Specification                   | Good Test                              |
|----------------|--------------------------------------|----------------------------------------|
| **Focus**      | *What* the system does (behavior)    | *Whether* the system does it correctly |
| **Audience**   | Business stakeholders, developers    | Developers, testers, CI pipelines      |
| **Language**   | Declarative, business-readable       | Concrete examples with specific data   |
| **Durability** | Resilient to implementation changes  | Sensitive to behavioral changes        |
| **Purpose**    | Shared understanding and docs        | Verification and validation            |
| **Detail**     | High-level business rules            | Specific inputs, actions, outputs      |

The art is finding the balance: scenarios that are **declarative enough** to
serve as documentation but **concrete enough** to be executable and meaningful
as tests.

### Specification Principles

When writing feature files as specifications, follow these principles:

1. **Describe behavior, not implementation**. Your scenarios should describe the
   intended behavior of the system, not how it is implemented. Ask: "Will this
   wording need to change if the implementation does?"

2. **Keep scenarios concise**. Cucumber recommends 3-5 steps per scenario.
   Having too many steps causes the example to lose its expressive power as a
   specification. A good ceiling is 10 steps maximum.

3. **One behavior per scenario**. Each scenario should illustrate exactly one
   behavior or business rule. If you find yourself writing more than one
   When-Then pair, split into separate scenarios.

4. **Use the feature description to capture context**. The free-text area
   between the `Feature:` line and the first scenario (or rule) is a
   "specification brief" --- use it to explain *why* the feature exists, who it
   is for, and what business problem it solves.

5. **Feature files should be small and focused**. Convention: one feature per
   file. Many small files are better than a few large ones.

6. **Limit scenarios per feature**. A good measure is roughly a dozen scenarios
   per feature. If you have significantly more, the feature may be too broad and
   should be split.

---

## 5. Mapping User Stories to Gherkin Features

### The Three Amigos Session

The "Three Amigos" meeting is a collaborative session that turns user stories
into clean, thorough Gherkin scenarios. It involves at least three perspectives:

- **Product Owner**: Defines scope. As edge cases surface, the PO decides what
  is in scope and what is not.
- **Developer**: Adds technical details to the scenarios. Identifies
  behind-the-scenes requirements, dependencies, and roadblocks.
- **Tester**: Generates scenarios and edge cases. Thinks about what could go
  wrong, what boundary conditions exist, and what negative scenarios matter.

The key goal is to **build shared understanding** --- to ensure everyone has a
clear picture of the objectives and motivations behind a feature, and to avoid
misunderstandings, incorrect assumptions, and overlooked details.

### Example Mapping

Example Mapping, developed by Matt Wynne of the Cucumber team, is a structured
technique for these collaborative sessions. It uses colored index cards:

| Card Color | Represents | Purpose                                          |
|------------|------------|--------------------------------------------------|
| **Yellow** | Story      | The user story under discussion                  |
| **Blue**   | Rule       | Each known acceptance criterion or business rule |
| **Green**  | Example    | A concrete example that illustrates a rule       |
| **Red**    | Question   | An open question that cannot be answered now     |

#### How to Run an Example Mapping Session

1. Write the story on a **yellow card** and place it at the top.
2. Write each known acceptance criterion as a **rule** on a **blue card**.
3. For each rule, write concrete **examples** on **green cards**.
4. When a question arises that the group cannot answer, write it on a **red
   card** and set it aside.
5. Continue until the team is satisfied (typically ~25 minutes per story).

#### Reading the Results

After the session, the arrangement of cards tells you important things:

- **Too many red cards**: The story is not well-understood. More research or
  stakeholder input is needed before development can start.
- **Too many blue cards**: The story is too large. Consider splitting it.
- **Many green cards under one blue card**: The rule is complex. Consider
  simplifying or splitting the rule.
- **Few or no green cards**: The rule may be trivial, or the
  team has not thought about it enough.

### Feature Mapping

Feature Mapping, designed by John Ferguson Smart, extends Example Mapping by
adding flow awareness:

1. Define a feature or pick one from the backlog.
2. Identify what **actors** are involved.
3. Break the feature into **tasks** to identify the main flows.
4. Identify **examples** that illustrate principles or variant flows.
5. Ask challenge questions: "But what if...?", "What else could lead to this
   outcome?", "What other outcomes might happen?"

### From Cards to Gherkin

The output of Example Mapping translates directly to Gherkin:

- **Yellow card** (Story) becomes the `Feature:` with its description.
- **Blue cards** (Rules) become `Rule:` blocks (Gherkin 6+) or groups of
  related scenarios.
- **Green cards** (Examples) become `Scenario:` / `Example:` blocks.
- **Red cards** (Questions) become comments or are resolved before writing.

### When to Write the Gherkin

A practical workflow:

1. **During grooming/planning**: Conduct Example Mapping sessions. Produce
   cards, not Gherkin.
2. **After the session**: The developer and tester draft Gherkin feature files
   from the cards.
3. **Review with PO**: The product owner reviews the drafted Gherkin and
   provides feedback.
4. **Sprint start**: Feature files are already written. Developers know what to
   build. Testers know what to verify. There is no ambiguity.

Writing formal Gherkin *during* the Three Amigos session is generally
discouraged --- it can distract from the true purpose of building shared
understanding. The exception is early in a project when the team is still
developing its ubiquitous language.

---

## 6. Edge Cases and Error Scenarios

### Why Edge Cases Belong in Specifications

Edge cases are behaviors too. If a behavior matters to the business, it deserves
representation in the specification. The question is not "should we specify edge
cases?" but rather "which edge cases are worth specifying at the Gherkin level?"

### Categories of Edge Cases to Consider

When specifying a feature, systematically think through these categories:

1. **Invalid input**: What happens when the user provides data in the wrong
   format, leaves required fields empty, or exceeds length limits?
2. **Boundary conditions**: What happens at the exact limits? (e.g., exactly 0
   items, exactly the maximum allowed, one more than the maximum)
3. **Concurrency**: What happens when two users perform the same action
   simultaneously?
4. **Unavailable dependencies**: What happens when an external service is down,
   a database is unreachable, or a file is missing?
5. **Authorization failures**: What happens when a user without the right
   permissions attempts an action?
6. **State violations**: What happens when an action is attempted in an invalid
   state? (e.g., canceling an already-shipped order)

### Structuring Negative Scenarios

Use the `Rule` keyword to group negative scenarios with their positive
counterparts:

```gherkin
Feature: Money transfer between accounts

  Rule: Transfers require sufficient funds

    Scenario: Transfer with sufficient balance
      Given the source account has a balance of $500.00
      When the user transfers $200.00 to the destination account
      Then the source account balance is $300.00
      And the destination account balance increases by $200.00

    Scenario: Transfer with insufficient balance
      Given the source account has a balance of $50.00
      When the user transfers $200.00 to the destination account
      Then the transfer is declined
      And the source account balance remains $50.00
      And the user is informed of insufficient funds

    Scenario: Transfer of exactly the available balance
      Given the source account has a balance of $200.00
      When the user transfers $200.00 to the destination account
      Then the transfer succeeds
      And the source account balance is $0.00

  Rule: Transfer amounts must be positive and within daily limits

    Scenario: Transfer of zero amount
      Given the source account has a balance of $500.00
      When the user attempts to transfer $0.00
      Then the transfer is rejected with "Amount must be greater than zero"

    Scenario: Transfer of negative amount
      Given the source account has a balance of $500.00
      When the user attempts to transfer -$50.00
      Then the transfer is rejected with "Amount must be greater than zero"

    Scenario: Transfer exceeding daily limit
      Given the source account has a balance of $50,000.00
      And the daily transfer limit is $10,000.00
      And the user has already transferred $8,000.00 today
      When the user attempts to transfer $5,000.00
      Then the transfer is declined
      And the user is informed they have exceeded their daily transfer limit
```

### Guidelines for Specifying Edge Cases

1. **For every happy path, write at least one error scenario**. This is the
   minimum standard for specification completeness.

2. **Use testing heuristics sparingly**. Techniques like equivalence
   partitioning and boundary value analysis can guide which examples to choose,
   but avoid turning the specification into an exhaustive test matrix.

3. **Reserve Gherkin for business-visible edge cases**. Technical edge cases
   (null pointer handling, thread safety of internal data structures) belong in
   unit tests. Gherkin edge cases should represent situations that stakeholders
   would understand and care about.

4. **Use Scenario Outlines for boundary variations**:

```gherkin
  Rule: Passwords must meet complexity requirements

    Scenario Outline: Password validation
      When the user sets their password to "<password>"
      Then the system <result>

      Examples: Accepted passwords
        | password         | result                |
        | Str0ng!Pass      | accepts the password  |
        | MyP@ssw0rd123    | accepts the password  |

      Examples: Rejected passwords — too short
        | password | result                                      |
        | Ab1!     | rejects with "Must be at least 8 characters"|

      Examples: Rejected passwords — missing complexity
        | password         | result                                        |
        | alllowercase1!   | rejects with "Must contain an uppercase letter"|
        | ALLUPPERCASE1!   | rejects with "Must contain a lowercase letter" |
        | NoNumbers!!      | rejects with "Must contain a digit"            |
        | NoSpecialChar1s  | rejects with "Must contain a special character"|
```

---

## 7. Non-Functional Requirements in Gherkin

### Can You Specify NFRs in Gherkin?

Yes. While Gherkin is most naturally suited to functional requirements, it can
effectively express non-functional requirements (NFRs) when they are framed in
terms of **user-observable behavior** with **measurable criteria**.

The structure of a Gherkin scenario maps naturally to quality scenario templates
used in software architecture:

| Gherkin Keyword | Quality Scenario Element                         |
|-----------------|--------------------------------------------------|
| `Feature:`      | Quality attribute (e.g., Performance, Security)  |
| `Given`         | Source + Stimulus context                        |
| `When`          | Stimulus + Environment                           |
| `Then`          | Response + Response measure                      |

### Performance Requirements

```gherkin
Feature: Search response time

  Rule: Search results must return within acceptable time under load

    Scenario: Search performance under normal load
      Given the product catalog contains 50,000 products
      And 100 users are actively browsing the system
      When a user searches for "wireless headphones"
      Then search results are displayed within 2 seconds

    Scenario: Search performance under peak load
      Given the product catalog contains 50,000 products
      And 1,000 users are simultaneously searching
      When a user searches for "wireless headphones"
      Then search results are displayed within 5 seconds

    Scenario: Bulk data export performance
      Given a report contains 100,000 records
      When the user requests a CSV export
      Then the download begins within 10 seconds
```

### Security Requirements

```gherkin
Feature: Authentication security

  Rule: Accounts are protected against brute-force attacks

    Scenario: Account lockout after failed login attempts
      Given a registered user account
      When 5 consecutive failed login attempts occur within 15 minutes
      Then the account is locked for 30 minutes
      And the account owner receives a notification email

    Scenario: Session expiration for inactive users
      Given an authenticated user session
      When the user has been inactive for 30 minutes
      Then the session expires
      And the user must re-authenticate to continue

  Rule: Sensitive data is protected in transit and at rest

    Scenario: Password storage
      Given a user sets their password to a new value
      When the password is stored in the system
      Then it is stored as a one-way cryptographic hash
      And the original password is not recoverable from the stored value
```

### Accessibility Requirements

```gherkin
Feature: Screen reader compatibility

  Rule: All interactive elements are accessible via keyboard

    Scenario: Form navigation without a mouse
      Given a user who navigates using only a keyboard
      When the user tabs through the checkout form
      Then every input field and button receives focus in logical order
      And the currently focused element has a visible focus indicator

  Rule: Content meets minimum contrast requirements

    Scenario: Text readability for low-vision users
      Given the default application theme is active
      When any text is displayed on the screen
      Then the contrast ratio between the text and background meets
        WCAG 2.1 AA minimum (4.5:1 for normal text, 3:1 for large text)
```

### Practical Considerations

- **NFR scenarios often cannot be automated with Cucumber alone**. The Gherkin
  serves as the specification (the "what"), while the automation layer may use
  specialized tools (JMeter for performance, OWASP ZAP for security, axe-core
  for accessibility). The step definitions simply orchestrate those tools.

- **Not every NFR needs a Gherkin scenario**. Some NFRs are better expressed as
  architectural constraints, operational guidelines, or configuration
  requirements. Use Gherkin for NFRs that have clear, measurable acceptance
  criteria from the user's perspective.

- **Tag NFR scenarios for selective execution**. Since NFR tests are often
  slow or require special infrastructure, use tags like `@performance`,
  `@security`, or `@accessibility` to separate them from functional scenarios.

---

## 8. Completeness of Specifications

### The Completeness Paradox

Creating a truly complete specification is extremely difficult, perhaps
impossible. SbE embraces this reality: specifications are defined "well enough"
and evolve continuously. The goal is not exhaustive documentation but sufficient
coverage of important behaviors to guide implementation and catch regressions.

### Practical Guidelines for Coverage

A typical feature should have **5-20 scenarios** to completely specify its
important behaviors. This includes:

- **Happy paths**: The primary success scenarios (usually 1-3).
- **Validation errors**: What happens with invalid input (1-3 per input type).
- **Boundary conditions**: Behavior at limits (1-2 per boundary).
- **Authorization/permission variations**: Different user roles (1 per role if
  behavior differs).
- **Error handling**: System failures, unavailable dependencies (1-2).
- **State-dependent behavior**: Different starting states that affect outcomes.

### Example Mapping as a Completeness Tool

The Example Mapping technique (described in Section 5) is the most
effective tool for ensuring completeness. The colored cards provide
a visual indicator:

- If a rule has no examples, it is under-specified.
- If questions remain (red cards), the team is not ready to implement.
- If scenarios keep multiplying, the feature may need to be decomposed.

### Completeness Heuristics

Apply these questions to each rule in your specification:

1. **What is the happy path?** (The most common, expected scenario.)
2. **What can go wrong?** (Error conditions, invalid input.)
3. **What are the boundary conditions?** (Minimum, maximum, exactly-at-limit.)
4. **Who else might do this?** (Different user roles, permissions.)
5. **What if the preconditions are not met?** (Missing data, wrong state.)
6. **What are the timing considerations?** (Too early, too late, concurrent.)
7. **What happens with unusual but valid input?** (Unicode, very long strings,
   special characters.)

### Iterative Refinement

Rather than trying to capture everything upfront, specifications evolve through
iterative refinement:

1. **Before sprint**: Capture the known rules and examples (Example Mapping).
2. **During development**: Developers discover new edge cases and add scenarios.
3. **During testing**: Testers identify gaps and propose additional scenarios.
4. **After release**: Production issues lead to new scenarios that prevent
   regression.

This continuous discovery model means the specification is always
growing and improving. The key discipline is that **every
behavioral change or bug fix should
be accompanied by a new or updated scenario** that documents the correct
behavior.

---

## 9. The Rule Keyword: Grouping Business Rules

### What Is the Rule Keyword?

Introduced in Gherkin 6 (2018), the `Rule` keyword provides an additional level
of grouping between `Feature` and `Scenario`. Its purpose is to represent **one
business rule that should be implemented**, grouping together the scenarios that
illustrate that rule.

Before Gherkin 6, scenarios could only be grouped by `Feature`. This was
acceptable for features with a handful of scenarios but encouraged
overly complex
scenarios when features had many business rules.

### Syntax and Structure

```gherkin
Feature: Feature name

  Rule: First business rule
    Example: An example illustrating the first rule
      Given ...
      When ...
      Then ...

    Example: Another example for the first rule
      Given ...
      When ...
      Then ...

  Rule: Second business rule
    Example: An example illustrating the second rule
      Given ...
      When ...
      Then ...
```

Key points:

- `Scenario` and `Example` are synonyms in Gherkin.
- A `Rule` can contain a `Background` that applies only to its own scenarios.
- Tags on a `Rule` are inherited by all scenarios within it.

### The Relationship Between Rules and Examples

This relationship is critical to specification quality:

- **Without examples, a rule may be ambiguous**. Abstract rules are open to
  interpretation. Concrete examples pin down exactly what the rule means.
- **Without a rule, an example lacks context**. A scenario floating on its own
  does not tell you *why* that behavior matters or what business rule it
  illustrates.
- **Together, they fully specify expected behavior** and guide the development
  team's efforts.

### Connection to Example Mapping

The `Rule` keyword directly corresponds to the **blue cards** in Example
Mapping. The mapping is:

| Example Mapping      | Gherkin                   |
|----------------------|---------------------------|
| Yellow card (Story)  | `Feature:`                |
| Blue card (Rule)     | `Rule:`                   |
| Green card (Example) | `Scenario:` / `Example:`  |

This means the output of an Example Mapping session can be transcribed almost
directly into a Gherkin feature file with rules and scenarios.

### Practical Example: Library System

```gherkin
Feature: Library book lending

  Rule: Members can borrow up to 5 books at a time

    Example: Borrowing when under the limit
      Given a member has 3 books checked out
      When they borrow 1 more book
      Then they have 4 books checked out

    Example: Attempting to borrow when at the limit
      Given a member has 5 books checked out
      When they attempt to borrow another book
      Then the request is declined
      And they are informed of the 5-book limit

  Rule: Books are due within 14 days

    Example: Returning a book on time
      Given a member borrowed a book 10 days ago
      When they return the book
      Then no late fee is charged

    Example: Returning a book late
      Given a member borrowed a book 20 days ago
      When they return the book
      Then a late fee of $0.50 per overdue day is charged
      And the total late fee is $3.00

  Rule: Members with overdue books cannot borrow new ones

    Example: Blocked from borrowing due to overdue book
      Given a member has a book that is 3 days overdue
      When they attempt to borrow a new book
      Then the request is declined
      And they are informed they must return overdue items first
```

### IDE and Tooling Support

Modern IDEs display scenarios grouped by rule, and many text editors allow you
to "fold" Gherkin files at the `Rule` level, hiding the scenarios and giving an
overview of all the business rules in a feature. Automation results are also
grouped by rule, making it easy to see which business rules are
passing and which
are failing.

---

## 10. Organizing Specs for Complex Systems

### Principles of Organization

For complex systems with many features and cross-cutting concerns, how you
organize feature files matters as much as how you write individual scenarios.

The overriding principle, articulated by Matt Wynne:

> "Because every one of the other options leaks solution domain; this is the
> only one that's pure problem domain."

Feature files should be organized around the **problem domain** (business
concepts, user workflows) rather than the **solution domain** (technical
components, architecture layers).

### Recommended Folder Structure

Organize feature files hierarchically by business domain:

```text
features/
  accounts/
    registration.feature
    authentication.feature
    profile-management.feature
    password-recovery.feature
  orders/
    cart-management.feature
    checkout.feature
    payment-processing.feature
    order-tracking.feature
    returns-and-refunds.feature
  inventory/
    stock-management.feature
    product-catalog.feature
    pricing-rules.feature
  reporting/
    sales-reports.feature
    inventory-reports.feature
```

This structure mirrors the business domain, not the technical architecture.
A developer looking for "how does checkout work?" goes to
`features/orders/checkout.feature`, not
`features/controllers/orders_controller.feature`.

### Handling Cross-Cutting Concerns with Tags

Cross-cutting concerns (authorization, auditing, notifications) span multiple
features. Tags are the primary mechanism for managing these:

```gherkin
@authorization @admin-only
Feature: User management

  Scenario: Admin creates a new user
    ...

@authorization @manager-only
Feature: Inventory adjustments

  Scenario: Manager adjusts stock count
    ...
```

You can then query all authorization-related scenarios across all features:

```bash
# Run all scenarios tagged with @authorization
cucumber --tags @authorization

# Find all features that involve admin-only access
grep -r "@admin-only" features/
```

Tags serve as an **index** that lets you slice the specification in ways that
cut across the primary organizational hierarchy.

### Common Tag Categories

| Tag Purpose     | Examples                                       |
|-----------------|------------------------------------------------|
| User role       | `@admin`, `@manager`, `@customer`, `@guest`    |
| Priority        | `@critical`, `@high`, `@low`                   |
| NFR type        | `@performance`, `@security`, `@accessibility`  |
| Feature area    | `@payments`, `@search`, `@notifications`       |
| Execution speed | `@smoke`, `@slow`, `@nightly`                  |
| Status          | `@wip`, `@pending`, `@deprecated`              |

### Naming Conventions

Establish consistent naming conventions:

- **Feature files**: Use kebab-case, named after the feature or capability
  (e.g., `password-recovery.feature`).
- **Feature names**: Use clear, descriptive business language
  (e.g., "Password recovery", not "PasswordController reset endpoint").
- **Scenario names**: Describe the specific behavior being illustrated
  (e.g., "User resets password with valid reset token", not "Test case 42").

### Scaling Across Teams

For large organizations, Kamil Nicieja's *Writing Great Specifications* covers
how to structure feature files by domains and sub-domains, using principles from
Domain-Driven Design. Key strategies include:

- **Bounded contexts as top-level directories**: If your system has distinct
  bounded contexts (e.g., "Billing", "Fulfillment", "Customer Support"), use
  them as the top-level organization.
- **Shared language glossaries**: Maintain a glossary of domain terms to ensure
  consistent language across feature files written by different teams.
- **Cross-referencing**: Use comments or links in feature files to reference
  related features in other domains.

---

## 11. Declarative vs. Imperative Style

### Why This Matters for Specification

The choice between declarative and imperative style is the single most important
decision when writing Gherkin for specification. It determines whether your
feature files serve as useful documentation or become brittle scripts that
no one reads.

### Declarative Style (Preferred for Specifications)

Declarative scenarios describe **what** the system should do, not **how**:

```gherkin
Scenario: Customer receives a discount on their birthday
  Given today is the customer's birthday
  And the customer has items in their cart totaling $100.00
  When the customer checks out
  Then a 10% birthday discount is applied
  And the customer pays $90.00
```

Advantages:

- Reads like a requirement, not a procedure.
- Resilient to implementation changes (UI redesigns, workflow changes).
- Business stakeholders can understand and validate it.
- Encourages step reusability.

### Imperative Style (Avoid for Specifications)

Imperative scenarios describe the **how** --- every click, every field:

```gherkin
Scenario: Customer receives a discount on their birthday
  Given the user navigates to the login page
  And the user enters "alice@example.com" in the email field
  And the user enters "password123" in the password field
  And the user clicks "Log In"
  And the user navigates to the products page
  And the user clicks "Add to Cart" on "Blue Widget"
  And the user clicks the cart icon
  And the user clicks "Proceed to Checkout"
  Then the field "discount" shows "10%"
  And the field "total" shows "$90.00"
```

Problems:

- Reads like a test script, not a specification.
- Breaks when any UI element changes.
- Obscures the business rule under procedural noise.
- Non-technical stakeholders will not read or validate it.
- Creates massive maintenance burden.

### The Litmus Test

Ask yourself: **"Will this wording need to change if the implementation
changes?"** If the answer is yes, the scenario is too imperative.

Another test: **"Could a product owner read this and confirm it's correct?"**
If not, it is too technical.

### When Some Imperative Detail Is Acceptable

There are rare cases where specifying interaction details matters:

- **Accessibility specifications**: The specific keyboard navigation order may
  be part of the requirement.
- **API specifications**: The exact request/response format may be the
  specification.
- **Regulatory requirements**: Specific wording or workflow steps may be
  mandated.

Even in these cases, keep the imperative details minimal and explain *why* they
are specified.

---

## 12. Ubiquitous Language and Domain-Driven Design

### The Connection

Behavior-Driven Development borrows the concept of **ubiquitous language** from
Domain-Driven Design (DDD). As Eric Evans described in *Domain-Driven Design*
(2003), the approach "consists notably of striving to use the vocabulary of a
given business domain, not only in discussions about the requirements for a
software product but in discussions of design as well and all the way into the
product's source code itself."

Gherkin serves as a practical implementation of ubiquitous language. It provides
a structured yet readable format that turns shared domain vocabulary into
executable specifications.

### Why It Matters for Specifications

If your Gherkin scenarios use different terms than your product owner uses, or
different terms than your code uses, you have a translation gap.
Translation gaps
create misunderstandings and bugs.

**The same word should mean the same thing** in:

- Conversations with stakeholders
- Gherkin feature files
- Source code (class names, method names, variable names)
- Database schemas
- API endpoints and documentation

### Building a Ubiquitous Language Through Gherkin

Gherkin scenarios are one of the best tools for discovering and refining
ubiquitous language:

1. **During Example Mapping or Three Amigos sessions**, pay attention to the
   words people use. When different people use different words for the same
   concept, stop and agree on one term.

2. **Maintain a domain glossary** alongside your feature files. This can be a
   simple text file that defines key terms:

   ```text
   Order: A customer's request to purchase one or more items. An order
          goes through states: pending, confirmed, shipped, delivered,
          cancelled.

   Cart: A temporary collection of items a customer intends to purchase.
         A cart becomes an order when the customer checks out.

   SKU: Stock Keeping Unit. A unique identifier for a product variant.
   ```

3. **Review Gherkin for consistency**. During code reviews,
   check that new scenarios use glossary terms. If a scenario
   introduces new terminology, either reject it or update the
   glossary first.

4. **Let Gherkin drive the code vocabulary**. If a scenario
   says "the customer checks out," the code should have a
   `Customer` class with a `checkout` method,
   not a `UserService.processTransaction()` method.

### Anti-Patterns

- **Technical jargon in scenarios**: "Given a POST request to /api/v2/orders"
  --- this is solution-domain language, not problem-domain language.
- **Inconsistent terminology**: Using "customer" in one scenario and "user" in
  another when they mean the same thing.
- **Implementation leakage**: "Given the OrderRepository contains 5 records"
  --- `OrderRepository` is an implementation detail.

---

## 13. Real-World Examples

### Notable Open-Source Projects Using Gherkin for Specification

#### Cucumber's Own Projects

The Cucumber ecosystem uses its own tools extensively. The Aruba project
([github.com/cucumber/aruba](https://github.com/cucumber/aruba)) is a
particularly good example. Aruba is a tool for testing
command-line applications,
and its `features/` directory serves as both its specification and its
documentation. The project explicitly states: "You can expect Aruba to work as
documented" --- the feature files *are* the contract with users.

#### The Gherkin Parser Itself

The Gherkin parser project
([github.com/cucumber/gherkin](https://github.com/cucumber/gherkin))
uses Gherkin
feature files to specify its own behavior. This is a powerful example of
self-referential specification: the parser is specified using the language it
parses.

#### Gherkin-by-Example

The GitHub organization
[gherkin-by-example](https://github.com/gherkin-by-example) provides Gherkin
specifications implemented across multiple languages (Java/Cucumber,
Python/Behave, Dart/Gherkin). Problems are first modeled using Gherkin at two
levels --- system level and domain level --- demonstrating how Gherkin can
specify behavior at different levels of abstraction.

#### Gherkin Best Practices Repository

The
[andredesousa/gherkin-best-practices](https://github.com/andredesousa/gherkin-best-practices)
repository provides a comprehensive guideline of best practices for Gherkin and
BDD, with concrete examples of good and bad patterns.

### Example: Well-Structured Feature File

Here is an example of a well-structured feature file that demonstrates
specification principles (adapted from multiple sources):

```gherkin
Feature: Subscription plan management
  Customers can upgrade, downgrade, or cancel their subscription plan.
  Plan changes take effect at the start of the next billing cycle,
  unless the customer is on a trial, in which case changes are immediate.

  Background:
    Given the following subscription plans exist:
      | Plan       | Monthly Price | Storage | Users |
      | Starter    | $10           | 5 GB    | 1     |
      | Team       | $30           | 50 GB   | 5     |
      | Enterprise | $100          | 500 GB  | 50    |

  Rule: Plan upgrades take effect at the start of the next billing cycle

    Example: Customer upgrades from Starter to Team
      Given a customer is on the "Starter" plan
      And their next billing date is January 15
      When the customer upgrades to the "Team" plan
      Then they continue on the "Starter" plan until January 15
      And the "Team" plan activates on January 15
      And they are charged $30 on January 15

    Example: Customer is notified of the pending upgrade
      Given a customer has requested an upgrade to the "Team" plan
      When the upgrade is scheduled
      Then the customer receives a confirmation email
      And their account shows "Team plan (activates Jan 15)"

  Rule: Plan downgrades take effect at the start of the next billing cycle

    Example: Customer downgrades from Enterprise to Team
      Given a customer is on the "Enterprise" plan
      And their next billing date is February 1
      When the customer downgrades to the "Team" plan
      Then they retain "Enterprise" features until February 1
      And the "Team" plan activates on February 1
      And they are charged $30 on February 1

  Rule: Trial customers receive plan changes immediately

    Example: Trial customer upgrades immediately
      Given a customer is on a trial of the "Starter" plan
      When the customer upgrades to the "Team" plan
      Then the "Team" plan activates immediately
      And the trial period applies to the "Team" plan

  Rule: Cancellation stops billing but maintains access until period end

    Example: Customer cancels mid-cycle
      Given a customer is on the "Team" plan
      And they last paid on March 1
      And their next billing date is April 1
      When the customer cancels their subscription on March 15
      Then they retain access to "Team" features until April 1
      And no charge is made on April 1
      And their account reverts to a free tier on April 1
```

This example demonstrates:

- A clear feature description explaining the business context.
- Business rules captured with the `Rule` keyword.
- Concrete examples with specific data (dates, prices, plan names).
- Declarative style --- focuses on *what* happens, not *how* the UI works.
- Coverage of happy paths (upgrade, downgrade) and important variations (trial,
  cancellation).

---

## 14. Key References and Further Reading

### Books

- **Specification by Example** by Gojko Adzic (2011). The foundational text on
  the SbE methodology. Introduces living documentation and the process patterns
  for collaborative specification.

- **Writing Great Specifications** by Kamil Nicieja (Manning, 2017). A
  practical tutorial focused specifically on writing Gherkin as specifications
  (not tests). Covers the INVEST philosophy, specification layers, scaling SbE
  across organizations, and the connection to Domain-Driven Design. Foreword by
  Gojko Adzic.

- **BDD in Action** by John Ferguson Smart (Manning, 2014). Comprehensive guide
  to BDD practices including Feature Mapping, discovery techniques, and
  integrating BDD into the development lifecycle.

- **The Cucumber Book** by Matt Wynne and Aslak Hellesoy (Pragmatic
  Programmers). Practical guide to Cucumber with emphasis on writing good
  feature files.

- **Domain-Driven Design** by Eric Evans (2003). The source of the ubiquitous
  language concept that underpins effective Gherkin specifications.

### Online Resources

- [Cucumber Official Documentation: Gherkin Reference](https://cucumber.io/docs/gherkin/reference/)
  --- The canonical reference for Gherkin syntax and keywords.

- [Cucumber Blog: Gherkin Rules](https://cucumber.io/blog/bdd/gherkin-rules/)
  --- Explains the `Rule` keyword, its history, and its connection to Example
  Mapping.

- [Cucumber Blog: Introducing Example Mapping](https://cucumber.io/blog/bdd/example-mapping-introduction/)
  --- Matt Wynne's introduction to the Example Mapping technique.

- [Cucumber Blog: Solving "How to organise feature files?"](https://cucumber.io/blog/bdd/solving-how-to-organise-feature-files/)
  --- Problem-domain vs. solution-domain organization.

- [Writing Better Gherkin (Cucumber Docs)](https://cucumber.io/docs/bdd/better-gherkin/)
  --- Official guide to declarative vs. imperative style and other best
  practices.

- [BDD 101: Writing Good Gherkin (Automation Panda)](https://automationpanda.com/2017/01/30/bdd-101-writing-good-gherkin/)
  --- Comprehensive guide to Gherkin best practices and anti-patterns.

- [Specification by Example, 10 years later (Gojko Adzic)](https://gojko.net/2020/03/17/sbe-10-years.html)
  --- Gojko Adzic's retrospective on what worked and what didn't in SbE.

- [Three Amigos Requirements Discovery Workshop (John Ferguson Smart)](https://johnfergusonsmart.com/three-amigos-requirements-discovery/)
  --- Detailed guide to running effective Three Amigos sessions.

- [Tom Egan: Writing Business Rules with Gherkin](https://tomegan.tech/articles/writing-business-rules-with-gherkin/)
  --- Practical guidance on using the `Rule` keyword effectively.

- [Using Gherkin for Specifying Quality Requirements (Software Architecturology)](http://www.software-architecturology.com/2021/01/16/using-gherkin-for-specifying-quality-requirements-initial-thoughts/)
  --- Mapping Gherkin to quality attribute scenarios for NFRs.

- [Gherkin Best Practices (GitHub)](https://github.com/andredesousa/gherkin-best-practices)
  --- Community-maintained guideline with concrete examples.

- [Gherkin Features for User Requirements (Jiby's Toolbox)](https://jiby.tech/post/gherkin-features-user-requirements/)
  --- Practical post on using Gherkin for requirements, including NFRs.

- [Writing Specification by Example Requirements with Gherkin (Octobot)](https://octobot.medium.com/writing-specification-by-example-requirements-with-gherkin-5a818ea24425)
  --- Step-by-step guide to writing SbE requirements.

- [Declarative vs. Imperative Gherkin Scenarios (It's a Delivery Thing)](https://itsadeliverything.com/declarative-vs-imperative-gherkin-scenarios-for-cucumber)
  --- Detailed comparison with examples.
