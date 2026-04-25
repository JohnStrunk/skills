# Existing Gherkin Skills for Claude Code -- Part 1

Analysis of 4 publicly available Claude Code skills related to
Gherkin BDD specifications. Research conducted 2026-04-15.

---

## Table of Contents

1. [cucumber-gherkin (el-feo/ai-context)](#1-cucumber-gherkin)
2. [playwright-bdd-gherkin-syntax (thebushidocollective/han)](#2-playwright-bdd-gherkin-syntax)
3. [bdd-gherkin-specification (jzallen/fred_simulations)](#3-bdd-gherkin-specification)
4. [gherkin (tsipotu/gherkin-skill)](#4-gherkin)
5. [Comparative Analysis](#5-comparative-analysis)

---

## 1. cucumber-gherkin

| Field | Value |
| ----- | ----- |
| **Name** | `cucumber-gherkin` |
| **Source** | [el-feo/ai-context](https://github.com/el-feo/ai-context) |
| **Path in repo** | `plugins/ruby-rails/skills/cucumber-gherkin/` |
| **Install count** | 112 |
| **Author** | Jeb Coleman |
| **Part of** | `ruby-rails` plugin (v0.2.8) within the `jebs-dev-tools` plugin collection |

### Purpose (cucumber-gherkin)

Helps users write BDD tests using Cucumber and Gherkin
specifically for **Ruby and Rails** applications. This is the
only skill of the four that goes beyond writing `.feature` files
and also covers Ruby step definitions, hooks, configuration, and
Capybara integration. It is a full Cucumber-in-Ruby development
skill.

### Workflow (cucumber-gherkin)

This skill is structured as a **reference card**, not an
interactive workflow. It provides:

1. Quick-reference Gherkin syntax (Feature, Scenario,
   Background, Rule, Scenario Outline)
2. Ruby step definition patterns using Cucumber
   Expressions
3. Hook lifecycle (Before/After/BeforeAll/AfterAll)
4. Running commands (`bundle exec cucumber`, tag filtering,
   parallel execution)
5. Best practices summary
6. Links to 4 detailed reference files for deeper guidance

The skill does **not** define a step-by-step interactive process.
It is designed as contextual knowledge that the agent loads when
the user is working on Cucumber/Gherkin tasks in a Ruby project.

### Automation (cucumber-gherkin)

- **No file generation workflow.** The skill provides
  knowledge, not a generation process.
- **No scanning for existing files.** It does not instruct the
  agent to check existing `.feature` files.
- **No conflict detection.**
- The agent is expected to use the reference material to
  produce correct code when asked.

### Key Instructions / Gherkin Guidelines (cucumber-gherkin)

- Declarative over imperative style ("When 'Bob' logs in" vs.
  "When I visit '/login'")
- Describe WHAT, not HOW
- One behavior per scenario, 3-5 steps per scenario
- Keep Background short (4 or fewer lines), essential context
  only
- Use domain language stakeholders understand
- Cucumber Expressions preferred over regex
- Covers Ruby-specific patterns: World modules, ParameterType,
  data table methods (.hashes, .rows_hash,
  .symbolic_hashes, .raw)

### Reference Files (cucumber-gherkin)

| File | Size | Content |
| ---- | ---- | ------- |
| `references/gherkin-syntax.md` | 8,126 bytes | Complete Gherkin language reference |
| `references/step-definitions.md` | 5,673 bytes | Ruby step definition patterns, data tables, doc strings, World context |
| `references/hooks-config.md` | 5,794 bytes | Hooks, cucumber.yml configuration, reporters, Capybara integration |
| `references/best-practices.md` | 11,191 bytes | Anti-patterns, naming conventions, collaboration patterns (Three Amigos, Example Mapping), refactoring |

### Strengths (cucumber-gherkin)

- **Full-stack Ruby/Cucumber coverage.** The only skill that
  covers step definitions, hooks, configuration, and test
  execution, not just Gherkin syntax.
- **Practical code examples.** Shows real Ruby code patterns
  alongside the Gherkin syntax.
- **Rich best-practices reference.** The best-practices.md file
  is the most comprehensive of the four, covering collaboration
  patterns like Three Amigos and Example Mapping.
- **Part of a larger ecosystem.** Sits within a well-organized
  plugin collection that includes RSpec, RuboCop, Rails, and
  other Ruby tools.
- **Cucumber Expressions coverage.** Provides detailed guidance
  on parameter types, optional text, alternatives.

### Weaknesses (cucumber-gherkin)

- **Ruby-only.** Entirely tied to the Ruby/Rails ecosystem. Not
  useful for teams using Cucumber with Java, JS, or other
  languages.
- **No interactive workflow.** Does not walk users through
  creating feature files step by step -- no clarifying
  questions, no scenario expansion.
- **No existing-file scanning.** Does not check for duplicate
  or conflicting scenarios.
- **No file organization guidance.** No instructions on where
  to place `.feature` files in the project tree.
- **No conflict detection.** If the project already has a
  scenario covering the same behavior, this skill won't flag
  it.
- **No i18n support.** Does not mention the `# language:`
  header for non-English scenarios.

### Full SKILL.md Content (cucumber-gherkin)

> ```text
> ---
> name: cucumber-gherkin
> description: BDD testing with Cucumber and Gherkin for Ruby and Rails applications. Use when writing feature files (.feature), step definitions, hooks, or implementing Behaviour-Driven Development in Ruby/Rails projects. Covers Gherkin keywords (Feature, Scenario, Given/When/Then, Background, Scenario Outline, Rule), Ruby step definition patterns, Cucumber Expressions, hooks (Before/After/BeforeAll/AfterAll), tags, data tables, doc strings, World modules, and Capybara integration. Triggers on cucumber, gherkin, BDD, feature files, step definitions, acceptance testing, executable specifications.
> ---
>
> # Cucumber & Gherkin
>
> BDD testing framework with plain-text executable specifications and Ruby step definitions.
>
> ```text
>
> Feature file (.feature) ──> Step Definitions (Ruby) ──> System under test
>
> ```
>
> ## Gherkin Quick Reference
>
> ```gherkin
> Feature: Short description
>   Optional multi-line description.
>
>   Background:
>     Given common setup for all scenarios
>
>   Rule: Business rule grouping (Gherkin 6+)
>
>     Scenario: Concrete example
>       Given an initial context
>       When an action occurs
>       Then expected outcome
>       And additional assertion
>       But negative assertion
>
>     Scenario Outline: Parameterized
>       Given there are <start> items
>       When I remove <remove> items
>       Then I should have <remaining> items
>
>       Examples:
>         | start | remove | remaining |
>         |    12 |      5 |         7 |
>         |    20 |      5 |        15 |
> ```
>
> **Step keywords:** `Given` (setup), `When` (action),
> `Then` (assertion), `And`/`But` (continuation),
> `*` (bullet)
>
> **Data tables:**
>
> ```gherkin
> Given the following users exist:
>   | name  | email             | role  |
>   | Alice | alice@example.com | admin |
> ```
>
> **Doc strings:**
>
> ```gherkin
> Given a blog post with content:
>   """markdown
>   # My Post Title
>   Content here.
>   """
> ```
>
> **Tags:** `@smoke @critical` on
> Feature/Rule/Scenario/Examples.
> Expressions: `@smoke and not @slow`,
> `(@smoke or @critical) and not @wip`
>
> ## Ruby Step Definitions
>
> ```ruby
> # Cucumber Expressions (preferred)
> Given('I have {int} cucumbers in my belly') do |count|
>   @belly = Belly.new
>   @belly.eat(count)
> end
>
> When('I wait {int} hour(s)') do |hours|
>   @belly.wait(hours)
> end
>
> Then('my belly should growl') do
>   expect(@belly.growling?).to be true
> end
>
> # Data table
> Given('the following users exist:') do |table|
>   table.hashes.each { |row| User.create!(row) }
> end
>
> # Doc string
> Given('a JSON payload:') do |json|
>   @payload = JSON.parse(json)
> end
> ```
>
> **Cucumber Expressions:** `{int}`, `{float}`, `{word}`,
> `{string}`, `{}` (anonymous). Optional: `cucumber(s)`.
> Alternatives: `color/colour`.
>
> **State sharing:** Use instance variables (`@user`) or World modules:
>
> ```ruby
> module MyWorld
>   def current_user
>     @current_user ||= create(:user)
>   end
> end
> World(MyWorld)
> ```
>
> ## Hooks
>
> ```ruby
> Before do |scenario|
>   @browser = Browser.new
> end
>
> After do |scenario|
>   save_screenshot("failure.png") if scenario.failed?
> end
>
> Before('@database') do
>   DatabaseCleaner.start
> end
>
> After('@database') do
>   DatabaseCleaner.clean
> end
>
> BeforeAll do
>   # once before any scenario
> end
>
> AfterAll do
>   # once after all scenarios
> end
> ```
>
> **Order:** `BeforeAll` > (`Before` > Background > Steps >
> `After`) per scenario > `AfterAll`
>
> ## Running
>
> ```bash
> bundle exec cucumber
> cucumber --tags "@smoke and not @wip"
> cucumber features/login.feature:10
> cucumber --dry-run
> cucumber --format html --out report.html
> bundle exec parallel_cucumber features/
> ```
>
> ## Best Practices
>
> **Declarative over imperative:**
>
> ```gherkin
> # Good                          # Avoid
> When "Bob" logs in              When I visit "/login"
> Then he sees his dashboard      And I enter "bob" in "username"
>                                 And I click "Login"
> ```
>
> - Describe *what* the system does, not *how*
> - One behavior per scenario, 3-5 steps
> - Keep Background short (≤4 lines), essential context only
> - Use domain language stakeholders understand
>
> ## References
>
> For comprehensive details:
>
> - `references/gherkin-syntax.md` -- Complete Gherkin
>   language reference (keywords, data tables, tags, i18n)
> - `references/step-definitions.md` -- Ruby step definition
>   patterns (data tables, doc strings, custom parameter
>   types, World context, organization)
> - `references/hooks-config.md` -- Hooks, cucumber.yml
>   configuration, reporters, Capybara integration
> - `references/best-practices.md` -- Anti-patterns, naming
>   conventions, collaboration patterns, refactoring
>
> ```text

---

## 2. playwright-bdd-gherkin-syntax

| Field | Value |
| ----- | ----- |
| **Name** | `playwright-bdd-gherkin-syntax` |
| **Source** | [TheBushidoCollective/han](https://github.com/TheBushidoCollective/han) |
| **Path in repo** | `plugins/tools/playwright-bdd/skills/playwright-bdd-gherkin-syntax/` |
| **Install count** | 59 |
| **Author** | TheBushidoCollective |
| **Part of** | `playwright-bdd` tool plugin within the large `han` plugin collection |
| **Sibling skills** | `playwright-bdd-configuration`, `playwright-bdd-step-definitions` |
| **Marked** | `user-invocable: false` (supporting skill, not directly triggered) |

### Purpose (playwright-bdd-gherkin-syntax)

Provides comprehensive Gherkin syntax knowledge specifically
for use with
[playwright-bdd](https://vitalets.github.io/playwright-bdd/),
which integrates Gherkin feature files with Playwright's test
runner. The skill covers all Gherkin keywords, data tables, doc
strings, tags (including Playwright-specific tags like `@skip`,
`@only`, `@fail`, `@fixme`), i18n, and best practices.

This skill is one of three in a `playwright-bdd` plugin suite:

- **playwright-bdd-gherkin-syntax** (this one) -- Gherkin syntax reference
- **playwright-bdd-configuration** -- Setup and configuration of playwright-bdd
- **playwright-bdd-step-definitions** -- Writing TypeScript step definitions

### Workflow (playwright-bdd-gherkin-syntax)

Like the cucumber-gherkin skill, this is a **reference-style
skill**, not an interactive workflow. It is marked as
`user-invocable: false`, meaning it is loaded as supporting
context for the other playwright-bdd skills rather than being
triggered directly by the user.

It provides:

1. Complete Gherkin syntax reference with examples
2. Playwright-specific tag guidance (`@skip`, `@only`, `@fail`, `@fixme`)
3. Tag filtering via Playwright CLI (`--grep`, `--grep-invert`)
4. Data tables and doc strings (including JSON and JavaScript content types)
5. Internationalization with German, French, Spanish examples
6. Best practices (declarative steps, meaningful names,
   independent scenarios, step count limits)
7. Common patterns (setup/verification, state transition, error handling)
8. File organization template

### Automation (playwright-bdd-gherkin-syntax)

- **No file generation workflow.** Pure reference material.
- **No scanning for existing files.**
- **No conflict detection.**
- The `bddgen` code generation tool is mentioned in passing
  (feature files are transformed into Playwright test files) but
  the skill does not instruct the agent to run it.

### Key Instructions / Gherkin Guidelines (playwright-bdd)

- Write declarative steps (good: "Given I am logged in as an
  admin" / bad: "Given I navigate to '/login'")
- Use meaningful scenario names (good: "Logged-in user can add
  items to wishlist" / bad: "Test 1")
- Keep scenarios independent -- each should set up its own state
- Use Background wisely -- only truly common setup
- 3-7 steps per scenario (slightly more generous than the
  other skills' 3-5)
- Organize features into subdirectories by domain area
- Playwright-specific: `@skip`, `@only`, `@fail`, `@fixme` tags
- Tags inherit from Feature to Scenario

### Strengths (playwright-bdd-gherkin-syntax)

- **Playwright-specific guidance.** The only skill that covers
  Playwright BDD's special tags and CLI integration.
- **Comprehensive Gherkin syntax coverage.** Thorough examples
  of every keyword, data tables, doc strings, Scenario Outlines
  with multiple example tables, Rule blocks.
- **i18n examples.** Shows complete keyword translations for
  German, French, and Spanish.
- **Common patterns.** Provides named patterns
  (setup/verification, state transition, error handling) that
  serve as templates.
- **File organization template.** Shows a suggested directory
  structure for feature files.
- **Part of a larger ecosystem.** The `han` repo is a massive
  plugin collection with 100+ plugins covering many tools and
  frameworks.

### Weaknesses (playwright-bdd-gherkin-syntax)

- **Not user-invocable.** Marked as `user-invocable: false`, so
  users cannot trigger it directly. It serves as background
  context for sibling skills.
- **No interactive workflow.** Does not walk users through
  creating scenarios, asking clarifying questions, or expanding
  test coverage.
- **No scanning for existing files or conflict detection.**
- **Playwright-coupled.** While the Gherkin syntax guidance is
  generally applicable, the skill is specifically designed for
  the playwright-bdd ecosystem. Users working with Cucumber
  (Ruby, Java, JS) would find some of the tag guidance
  misleading.
- **No step definition in this skill.** Step definitions are
  covered by the sibling `playwright-bdd-step-definitions`
  skill.
- **State transition pattern example is questionable.** The
  "Order lifecycle" example chains multiple When/Then pairs in
  a single scenario, which contradicts the "one behavior per
  scenario" principle.
- **Very long.** At ~13.5KB, it is a large context window burden
  for a reference document.

### Full SKILL.md Content (playwright-bdd-gherkin-syntax)

> ```markdown
> ---
> name: playwright-bdd-gherkin-syntax
> user-invocable: false
> description: Use when writing Gherkin feature files, using Scenario Outline with Examples, applying tags for test organization, and leveraging Background sections for shared setup.
> allowed-tools: [Read, Write, Edit, Bash, Glob, Grep]
> ---
>
> # Playwright BDD Gherkin Syntax
>
> Expert knowledge of Gherkin syntax for writing feature files in Playwright BDD, including scenarios, outlines, backgrounds, tags, and internationalization.
>
> [... ~13,500 bytes of comprehensive Gherkin syntax reference, best practices, patterns, i18n support, and file organization guidance ...]
> ```
>
> *(Full content omitted for length -- see the source repo
> for the complete file. Key sections: Feature File
> Structure, Keywords, Scenario Types, Tags (including
> Playwright-specific @skip/@only/@fail/@fixme), Data Tables,
> Doc Strings, Internationalization, Best Practices, Common
> Patterns, File Organization.)*

---

## 3. bdd-gherkin-specification

| Field | Value |
| ----- | ----- |
| **Name** | `bdd-gherkin-specification` |
| **Source** | [jzallen/fred_simulations](https://github.com/jzallen/fred_simulations) |
| **Path in repo** | `.claude/skills/bdd/` |
| **Install count** | 55 |
| **Author** | jzallen |
| **Version** | 2.0.0 |
| **Context** | Located in a FRED epidemiological simulation project (public health domain) |

### Purpose (bdd-gherkin-specification)

A **language-agnostic BDD specification writing skill** that
helps users create Gherkin feature files as requirements
documentation, acceptance criteria, and living documentation.
It is framework-agnostic -- it does not target any specific test
runner (Cucumber, playwright-bdd, etc.) and focuses purely on
writing good Gherkin specifications.

### Workflow (bdd-gherkin-specification)

This skill is structured as a **knowledge hub with navigation
guidance**, not an interactive generation workflow. It provides:

1. A "What is BDD?" / "What is Gherkin?" explanation
2. Clear guidance on when to use (and when NOT to use) BDD
3. A basic Gherkin structure example
4. A table of contents pointing to 6 reference files for
   different needs
5. Key principles (declarative, focused, independent, business
   language, readable)
6. A suggested workflow: Examples -> Syntax -> Write -> Review
   -> Avoid Mistakes
7. Quick tips for common patterns

The skill explicitly defines when NOT to use BDD:

- Purely technical requirements (architecture, refactoring)
- Small co-located teams with constant communication
- Features too simple to warrant formal specification

### Automation (bdd-gherkin-specification)

- **No file generation.** The skill provides guidance, not
  automated generation.
- **No existing-file scanning.**
- **No conflict detection.**
- **No commands to run.** It is purely a
  documentation/specification authoring skill.

### Key Instructions / Gherkin Guidelines (bdd-gherkin-spec)

- Be Declarative -- describe WHAT, not HOW
- Stay Focused -- one scenario = one behavior, 5-10 steps max
  (more generous than other skills)
- Stay Independent -- scenarios should not depend on each other
- Use Business Language -- avoid technical jargon
- Make it Readable -- anyone on the team should understand
- Write scenarios BEFORE code (they are specifications, not
  tests)
- Use Background for common setup, Scenario Outline for data
  variations, Rule for grouping
- Keep feature files under 20 scenarios (split if larger)
- File naming: lowercase with underscores
  (`user_authentication.feature`)

### Reference Files (bdd-gherkin-specification)

| File | Size | Content |
| ---- | ---- | ------- |
| `reference/gherkin-syntax.md` | 8,328 bytes | Complete Gherkin language reference |
| `reference/best-practices.md` | 8,964 bytes | Writing effective scenarios |
| `reference/examples.md` | 7,836 bytes | Real-world feature file examples |
| `reference/anti-patterns.md` | 6,706 bytes | Common mistakes and how to avoid them |
| `reference/organization.md` | 7,146 bytes | Structuring large feature file suites |
| `reference/quick-reference.md` | 6,588 bytes | Cheat sheet and templates |

Total reference material: ~45,568 bytes across 6 files, making
this the most comprehensive reference set.

### Strengths (bdd-gherkin-specification)

- **Language and framework agnostic.** Works for any project
  regardless of tech stack. The only skill that explicitly
  positions itself as specification-writing rather than
  test-writing.
- **"When NOT to use" guidance.** Uniquely provides clear
  boundaries on when BDD is not the right approach.
- **Most comprehensive reference library.** 6 reference files
  covering syntax, best practices, examples, anti-patterns,
  organization, and a quick-reference cheat sheet.
- **Good pedagogical structure.** The SKILL.md serves as a
  navigational hub pointing users to the right reference file
  for their current need.
- **Real-world examples file.** Has a dedicated examples file
  with complete feature files across multiple domains.
- **Quick-reference cheat sheet.** Has a dedicated
  quick-reference file with templates and decision trees.

### Weaknesses (bdd-gherkin-specification)

- **No interactive workflow.** Does not walk users through
  creating scenarios or ask clarifying questions.
- **No file scanning or conflict detection.** Does not check
  existing `.feature` files.
- **No actual scenario generation process.** It provides
  knowledge but does not guide the agent through a creation
  flow.
- **5-10 steps max is generous.** Most BDD best practices
  suggest 3-5 steps. Allowing up to 10 risks overly complex
  scenarios.
- **Sits in an unrelated repo.** The skill lives inside a FRED
  epidemiological simulation project, which may confuse users
  browsing the repo.
- **No i18n support.** Does not mention non-English Gherkin
  scenarios.
- **No glossary integration.**

### Full SKILL.md Content (bdd-gherkin-specification)

> ```markdown
> ---
> name: bdd-gherkin-specification
> description: Create Behavior-Driven Development (BDD) feature files using Gherkin syntax. Write clear, executable specifications that describe system behavior from the user's perspective. Use for requirements documentation, acceptance criteria, and living documentation.
> version: 2.0.0
> ---
>
> # BDD & Gherkin Specification
>
> You are an expert in Behavior-Driven Development (BDD) and Gherkin specification writing. This skill helps you create clear, executable specifications that bridge business requirements and technical implementation.
>
> ## What is BDD?
>
> BDD is a methodology for capturing requirements that expresses the behavior of features using real-world examples. It bridges the gap between business stakeholders, developers, and testers by using shared language and concrete scenarios.
>
> ## What is Gherkin?
>
> Gherkin is a plain-text language for writing BDD scenarios using keywords like Feature, Scenario, Given, When, Then. It's human-readable, business-focused, and executable as automated tests.
>
> ## When to Use This Skill
>
> **USE when:**
> - Defining acceptance criteria for user stories
> - Creating living documentation
> - Bridging communication gaps between technical and non-technical stakeholders
> - Specifying complex business rules
> - Working in cross-functional teams
>
> **DO NOT USE when:**
> - Requirements are purely technical (architecture, refactoring)
> - Team is small and co-located with constant communication
> - Features are too simple to warrant formal specification
>
> ## Quick Start
>
> **Basic Gherkin Structure:**
> ```gherkin
> Feature: User Login
>
>   Scenario: Successful login with valid credentials
>     Given the user is on the login page
>     When the user enters valid credentials
>     Then the user should be redirected to the dashboard
> ```
>
> ## Available Resources
>
> ### Core Documentation
>
> - **gherkin-syntax.md** - Complete Gherkin language reference
> - **best-practices.md** - Writing effective scenarios
> - **examples.md** - Real-world feature file examples
>
> ### Advanced Topics
>
> - **anti-patterns.md** - Common mistakes and how to avoid them
> - **organization.md** - Structuring large feature file suites
> - **quick-reference.md** - Cheat sheet and templates
>
> ## Key Principles
>
> 1. **Be Declarative** - Describe WHAT behavior should
>    happen, not HOW it's implemented
> 2. **Stay Focused** - One scenario = one behavior
>    (5-10 steps max)
> 3. **Stay Independent** - Scenarios should not depend on each other
> 4. **Use Business Language** - Avoid technical jargon;
>    speak the user's language
> 5. **Make it Readable** - Anyone on the team should understand the scenario
>
> ## Typical Workflow
>
> 1. **Start with Examples** - Read examples.md to see patterns
> 2. **Learn Syntax** - Reference gherkin-syntax.md for keywords
> 3. **Write Scenarios** - Use quick-reference.md template
> 4. **Review Quality** - Check against best-practices.md
> 5. **Avoid Mistakes** - Scan anti-patterns.md during review
>
> ## Quick Tips
>
> - Write scenarios BEFORE code (they're specifications, not tests)
> - Each scenario should be understandable in isolation
> - Use Background for common setup across scenarios
> - Use Scenario Outline for testing multiple similar cases
> - Use Rule to group related scenarios
> - Keep feature files under 20 scenarios (split if larger)
>
> ## File Naming Convention
>
> Use lowercase with underscores:
> `user_authentication.feature`,
> `shopping_cart_checkout.feature`
>
> ## Remember
>
> BDD scenarios are **conversations written down**, not test
> scripts. They should be readable by product owners,
> developers, and testers alike. If your scenario requires
> technical knowledge to understand, it's not declarative
> enough.
>
> ```text

---

## 4. gherkin

| Field | Value |
| ----- | ----- |
| **Name** | `gherkin` |
| **Source** | [tsipotU/gherkin-skill](https://github.com/tsipotU/gherkin-skill) |
| **Path in repo** | `skills/gherkin/` |
| **Install count** | 10 |
| **Author** | Emiel |
| **Version** | 1.0.0 (plugin.json); 1.1.0 per README changelog |
| **Dedicated repo** | Yes -- the entire repo exists solely for this skill |

### Purpose (gherkin / tsipotu)

An **interactive Gherkin scenario creation skill** that walks
users through the entire process of specifying behavior:
understanding what they want, asking clarifying questions,
scanning for existing specs, detecting conflicts, writing
well-structured `.feature` files, and checking the project
glossary. This is the most workflow-oriented and interactive of
all four skills.

### Workflow (gherkin / tsipotu)

This skill defines a detailed 7-step interactive workflow:

1. **Understand the Feature** -- For broad requests, ask 2-3
   targeted questions before proposing scenarios (about actors,
   state, error handling philosophy, scope boundaries). For
   specific requests, confirm scope and mention related
   scenarios. Present suggested scenarios as a checklist for
   user approval.

2. **Scan for Existing Gherkins** -- Search for `**/*.feature`
   files and Gherkin-style content in other files. Read existing
   files to understand style conventions. Check for behavioral
   equivalence (not just identical wording) to detect conflicts.
   Flag conflicts explicitly with the exact conflicting scenario
   quoted.

3. **Write the Scenarios** -- Apply reference files for syntax
   (`references/gherkin-syntax.md`), quality
   (`references/best-practices.md`), and anti-pattern review
   (`references/anti-patterns.md`).

4. **Present and Confirm** -- Show the complete `.feature` file
   before writing. Walk through design decisions (grouping,
   Outline vs. individual, edge case reasoning).

5. **Write or Append** -- Append to existing files when
   appropriate. Create new files when no existing file covers
   the area. Follow project conventions for directory layout
   and naming (`references/organization.md`).

6. **Glossary Check** -- Check if the project has a
   `glossary/glossary.config.yml`. Scan new scenarios for
   domain terms. Compare against existing glossary. Flag new
   terms and offer to add definitions.

7. **Summary** -- Report scenario count, file created/updated,
   conflicts flagged, new glossary terms, and suggest next
   scenarios to explore.

### Automation (gherkin / tsipotu)

- **File generation: Yes.** Creates or appends to `.feature`
  files.
- **File scanning: Yes.** Searches for existing `.feature`
  files with Glob and Grep.
- **Conflict detection: Yes.** Detects behavioral equivalence
  across existing scenarios.
- **Glossary integration: Yes.** Checks project glossary and
  flags new domain terms.
- **Style matching: Yes.** Reads existing files to match the
  project's conventions.

### Key Instructions / Gherkin Guidelines (gherkin / tsipotu)

From `references/best-practices.md`:

- Write for the Product Manager, not the Programmer
- One behavior per scenario
- Keep scenarios to 3-5 steps (1-2 Given, 1 When, 1-2 Then)
- Write descriptive scenario names using
  [Actor] [action/condition] [outcome]
- Use Background for shared setup (keep under 4 steps)
- Use Scenario Outline for data variations (only when
  variations represent distinct business rules)
- Use Rules to group related scenarios
- Tag thoughtfully (@smoke, @wip, @slow, @critical,
  @regression)
- Then steps observe outcomes, not internals

From `references/anti-patterns.md`:

- No technical language in steps (no class names, HTTP methods, SQL)
- No dependent scenarios
- No testing implementation instead of behavior
- No vague step names
- No more than ~5 steps per scenario
- No mixing setup and action in Given/When
- No overloaded feature files (20+ scenarios = split)
- No assertion-heavy Given steps

From `references/organization.md`:

- Match existing project structure before imposing conventions
- Standard layouts: flat, grouped by area, mirroring
  application modules
- File naming: lowercase, specific feature names, one feature
  per file
- Append when same feature area and under 15-20 scenarios;
  create new otherwise
- For brand-new projects: start flat, establish naming and
  tagging conventions early, ask the user to confirm

From `references/gherkin-syntax.md`:

- Full keyword reference table
- Step arguments (doc strings, data tables)
- Scenario Outline with Examples
- i18n support with `# language: xx` header
- Common language codes table

### Reference Files (gherkin / tsipotu)

| File | Size | Content |
| ---- | ---- | ------- |
| `references/gherkin-syntax.md` | 3,491 bytes | Compact syntax reference with keyword table, step arguments, i18n |
| `references/best-practices.md` | 6,480 bytes | 9 practices: audience, focus, step count, naming, Background, Outline, Rules, tags, Then-step guidance |
| `references/anti-patterns.md` | 6,614 bytes | 8 anti-patterns with before/after examples |
| `references/organization.md` | 5,161 bytes | Project structure scanning, directory layouts, naming, when to create vs. append |

### Strengths (gherkin / tsipotu)

- **The only truly interactive skill.** Defines a
  conversation-driven workflow that asks questions, proposes
  checklists, and confirms before writing. This is
  qualitatively different from the other three reference-style
  skills.
- **Conflict detection.** The only skill that checks existing
  `.feature` files for behavioral equivalence and flags
  potential duplicates.
- **Glossary integration.** The only skill that integrates with
  a project glossary to track domain terminology.
- **Style matching.** Instructs the agent to read existing
  files and match their conventions before writing.
- **Well-structured references.** Four focused reference files
  that are loaded as needed rather than dumping everything into
  the SKILL.md.
- **Excellent anti-patterns guide.** 8 clearly explained
  anti-patterns with concrete before/after examples.
- **File organization guidance.** Detailed instructions on
  where to place files, when to append vs. create, and how to
  set up conventions for new projects.
- **Language-agnostic.** Works for any project in any language
  -- not tied to Ruby, Playwright, or any specific framework.
- **i18n support.** Covers the `# language:` header and common
  language codes.
- **Dedicated repo.** The entire repo exists for this skill,
  making it easy to install and understand.
- **Clear README with usage examples.** Good user-facing
  documentation.

### Weaknesses (gherkin / tsipotu)

- **Lowest install count (10).** Despite being arguably the
  most complete skill, it has the fewest installs, suggesting
  discoverability issues or that it is newer.
- **No step definition guidance.** Does not help with writing
  step definitions in any language. Purely focused on
  `.feature` file authoring.
- **No test runner integration.** Does not help with running
  the tests, configuring the test framework, or interpreting
  results.
- **Glossary integration assumes a specific format.** Expects
  `glossary/glossary.config.yml` and specific field names
  (`name`, `aliases`, `code_name`, `ui_label`). This may not
  match many projects' glossary formats.
- **Relies on user engagement.** The interactive workflow
  requires the user to answer questions and review checklists.
  For users who just want to "generate gherkins for X", the
  conversation steps may feel slow.
- **No automation hooks.** Does not define any Claude Code
  hooks for automated checking or validation.

### Full SKILL.md Content (gherkin)

> ```markdown
> ---
> name: gherkin
> description: Create and manage Gherkin feature specifications (.feature files) following the Cucumber BDD standard. Use this skill whenever the user mentions "gherkin", "feature file", "BDD scenarios", "behavior specs", "acceptance criteria", or asks to write test scenarios in Given/When/Then format. Works for any project in any language — from a brand-new repo to a mature codebase. Even if no .feature files exist yet, this skill helps scaffold the first ones. Also use when the user wants to review, organize, or expand existing Gherkin specifications.
> ---
>
> # Gherkin Scenario Creator
>
> Write Gherkin specifications that capture business behavior clearly and completely. This skill walks users through the process interactively — understanding what they want to specify, thinking through the scenarios they might not have considered, checking for conflicts with existing specs, and producing well-structured `.feature` files.
>
> ## How It Works
>
> When a user asks to create Gherkins for a feature, follow this sequence:
>
> ### 1. Understand the Feature
> [... asks 2-3 targeted questions, proposes scenario checklist ...]
>
> ### 2. Scan for Existing Gherkins
> [... Glob **/*.feature, Grep for Gherkin content, conflict detection ...]
>
> ### 3. Write the Scenarios
> [... applies reference files for syntax, quality, anti-patterns ...]
>
> ### 4. Present and Confirm
> [... shows complete file, explains design decisions ...]
>
> ### 5. Write or Append
> [... creates or appends, follows project conventions ...]
>
> ### 6. Glossary Check
> [... checks glossary.config.yml, flags new domain terms ...]
>
> ### 7. Summary
> [... reports additions, conflicts, glossary suggestions, next scenarios ...]
> ```
>
> *(Full content: ~10,150 bytes. The complete SKILL.md
> includes a detailed password-reset example showing the full
> interactive workflow from asking questions through proposing
> a checklist to writing the final feature file.)*

---

## 5. Comparative Analysis

### Feature Matrix

| Feature | cucumber-gherkin | playwright-bdd-gherkin-syntax | bdd-gherkin-specification | gherkin (tsipotu) |
| ------- | :---: | :---: | :---: | :---: |
| Installs | 112 | 59 | 55 | 10 |
| Interactive workflow | No | No | No | **Yes** |
| Clarifying questions | No | No | No | **Yes** |
| Scenario checklist | No | No | No | **Yes** |
| Existing file scanning | No | No | No | **Yes** |
| Conflict detection | No | No | No | **Yes** |
| Glossary integration | No | No | No | **Yes** |
| Style matching | No | No | No | **Yes** |
| File generation | No | No | No | **Yes** |
| Step definitions | **Yes** (Ruby) | No (sibling skill) | No | No |
| Test runner integration | **Yes** (Cucumber) | Partial (tags) | No | No |
| Hook/lifecycle guidance | **Yes** | No | No | No |
| i18n support | No | **Yes** | No | **Yes** |
| Language-agnostic | No (Ruby) | No (Playwright) | **Yes** | **Yes** |
| Anti-patterns guide | **Yes** | Partial | **Yes** | **Yes** |
| Best practices | **Yes** | **Yes** | **Yes** | **Yes** |
| File organization | No | **Yes** (template) | **Yes** | **Yes** |
| Collaboration patterns | **Yes** (Three Amigos) | No | No | No |
| Quick-reference/cheat sheet | No | No | **Yes** | No |
| Examples file | No | No | **Yes** | No |
| "When NOT to use" guidance | No | No | **Yes** | No |
| Dedicated repo | No | No | No | **Yes** |
| Reference file count | 4 | 0 (inline) | 6 | 4 |
| SKILL.md size | 4,502 bytes | 13,514 bytes | 5,291 bytes | 10,150 bytes |

### Positioning

The four skills occupy distinct positions:

1. **cucumber-gherkin** -- Full-stack Cucumber/Ruby development
   tool. Best for Ruby/Rails teams already using Cucumber.
   Covers the complete pipeline from `.feature` files through
   step definitions to test execution.

2. **playwright-bdd-gherkin-syntax** -- Playwright-specific BDD
   syntax reference. Best for teams using playwright-bdd. Part
   of a three-skill suite. Not standalone.

3. **bdd-gherkin-specification** -- Framework-agnostic
   specification writing guide. Best for teams that want
   comprehensive BDD knowledge resources. Pedagogically strong
   but provides no automation.

4. **gherkin (tsipotu)** -- Interactive specification creator.
   Best for teams that want an AI pair-programmer experience
   for writing Gherkin. The only skill that actually generates
   files through a guided conversation.

### Key Takeaways

1. **The market is split between "reference" and "interactive"
   approaches.** Three of the four skills are essentially
   knowledge references; only tsipotu's skill defines an
   interactive workflow. The interactive approach is more
   aligned with how Claude Code skills are designed to work.

2. **No skill covers both Gherkin writing and step definition
   writing across multiple languages.** cucumber-gherkin covers
   Ruby step definitions. playwright-bdd has a sibling skill
   for TypeScript step definitions. But no single skill helps
   users write both the `.feature` file and the corresponding
   step definitions in their chosen language.

3. **Conflict detection and file scanning are rare.** Only
   tsipotu's skill checks existing specifications. This is a
   significant gap since duplicate or conflicting scenarios are
   a common problem in large codebases.

4. **i18n is underserved.** Only two of four skills mention
   non-English Gherkin. For global teams, this is an important
   capability.

5. **Glossary integration is novel.** tsipotu's glossary check
   is a unique feature that none of the others offer. It
   addresses the important BDD concept of "ubiquitous language"
   from Domain-Driven Design.

6. **Install counts don't correlate with quality.** The most
   feature-rich skill (tsipotu) has the fewest installs. The
   most-installed skill (cucumber-gherkin) benefits from being
   part of a popular Ruby toolkit.

7. **Step count guidance varies.** cucumber-gherkin: 3-5 steps.
   playwright-bdd: 3-7 steps. bdd-gherkin: 5-10 steps.
   tsipotu: 3-5 steps. The most common expert recommendation
   is 3-5 steps per scenario.

8. **None include validation hooks.** No skill defines Claude
   Code hooks to automatically validate `.feature` files on
   save or before commit.

9. **None integrate with CI/CD.** No skill helps users set up
   CI pipelines that run their Gherkin specs automatically.

10. **The "when NOT to use BDD" guidance from jzallen is
    uniquely valuable.** Helping users understand when Gherkin
    is the wrong tool prevents wasted effort and
    over-specification.
