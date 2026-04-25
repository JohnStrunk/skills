# Gherkin Tooling Ecosystem: Comprehensive Reference

> Last updated: April 2026

This document provides a comprehensive reference for all major tools in the
Gherkin ecosystem, organized by category. Each entry includes the tool's name,
language/platform, purpose, key features, current maintenance status, and
relevant links.

---

## Table of Contents

1. [Test Runners / BDD Frameworks](#1-test-runners--bdd-frameworks)
2. [Gherkin Parsers and Libraries](#2-gherkin-parsers-and-libraries)
3. [Linting and Style Checking Tools](#3-linting-and-style-checking-tools)
4. [IDE Support and Editor Plugins](#4-ide-support-and-editor-plugins)
5. [Reporting and Documentation Tools](#5-reporting-and-documentation-tools)
6. [Other Tools](#6-other-tools)

---

## 1. Test Runners / BDD Frameworks

Tools that execute `.feature` files against step definitions.

### 1.1 Cucumber-Ruby

| Attribute | Details |
| --- | --- |
| **Language** | Ruby |
| **Repository** | [github.com/cucumber/cucumber-ruby](https://github.com/cucumber/cucumber-ruby) |
| **GitHub Stars** | ~5,200 |
| **License** | MIT |
| **Latest Release** | v11.0.0 (April 2026) |
| **Status** | **Actively maintained.** The original Cucumber implementation; turned 17 in 2025. Support for Ruby 4.0+ added; minimum Ruby 3.1. |

**What it does:** The original BDD framework. Parses `.feature` files written in
Gherkin and executes them against step definitions written in Ruby.

**Step definitions:** Defined using `Given`, `When`, `Then` methods with regular
expressions or Cucumber Expressions as matchers. Steps are typically placed in
files under `features/step_definitions/`.

**Key features:**

- Full Gherkin support including `Rule`, `Background`, `Scenario Outline`,
  `Examples`, tags, data tables, and doc strings
- Hooks (`Before`, `After`, `BeforeAll`, `AfterAll`, `Around`)
- World object for sharing state between steps
- Tagged hooks and conditional execution
- Wire protocol for cross-language step definitions
- Built-in formatters: pretty, progress, JSON, HTML, JUnit, rerun

**Test framework integration:** Standalone runner; does not require a separate
test framework, though it is commonly used alongside RSpec.

**Reporting:** Built-in formatters produce JSON, HTML, and JUnit XML output.
Third-party reporters (Allure, Serenity) also supported.

---

### 1.2 Cucumber-JVM (Java / Kotlin / Scala)

| Attribute | Details |
| --- | --- |
| **Language** | Java, Kotlin, Scala (JVM) |
| **Repository** | [github.com/cucumber/cucumber-jvm](https://github.com/cucumber/cucumber-jvm) |
| **GitHub Stars** | ~2,800 |
| **License** | MIT |
| **Latest Release** | v7.34.3 (March 2026) |
| **Status** | **Actively maintained.** 20 releases in 2025 alone. |

**What it does:** The JVM implementation of Cucumber. Executes Gherkin feature
files against step definitions written in Java, Kotlin, or Scala.

**Step definitions:** Annotated methods using `@Given`, `@When`, `@Then`
annotations with Cucumber Expressions or regular expressions. Step definitions
live in Java/Kotlin/Scala classes.

**Key features:**

- Full Gherkin support
- Cucumber Expressions and regular expressions for step matching
- Dependency injection support (PicoContainer, Spring, Guice, CDI, OpenEJB)
- `@BeforeAll` / `@AfterAll` lifecycle hooks
- `@ScenarioScope` for Spring beans to prevent state leakage
- Parallel execution support
- Bill of Materials (BOM) for dependency alignment (`cucumber-bom`)

**Test framework integration:**

- **JUnit 5 (recommended):** Uses `cucumber-junit-platform-engine` with
  `@Suite` and `@IncludeEngines("cucumber")` annotations
- **JUnit 4:** Uses `@RunWith(Cucumber.class)` and `@CucumberOptions`
- **TestNG:** Supported via adapter

**Reporting:** JSON, HTML, JUnit XML built-in. Integrates with Allure, Serenity
BDD, Cluecumber, and cucumber-reporting.

---

### 1.3 Cucumber-JS (JavaScript / TypeScript)

| Attribute | Details |
| --- | --- |
| **Language** | JavaScript, TypeScript |
| **Repository** | [github.com/cucumber/cucumber-js](https://github.com/cucumber/cucumber-js) |
| **GitHub Stars** | ~5,300 |
| **License** | MIT |
| **Latest Release** | v12.8.1 (April 2026) |
| **Status** | **Actively maintained.** 8 releases in 2025. Work in progress on `@cucumber/node` built around the Node.js test runner. |

**What it does:** The JavaScript/TypeScript implementation of Cucumber. Runs
Gherkin feature files against step definitions in JS/TS.

**Step definitions:** Defined using imported `Given`, `When`, `Then` functions
with Cucumber Expressions or regular expressions. Steps reference `this` (the
World object), so arrow functions must not be used. Supports synchronous,
callback, and async/await patterns.

**Key features:**

- Full Gherkin support
- Native TypeScript support via tsx, ts-node, or Babel transpilation
- ESM and CommonJS module support
- World object for state management
- Parallel execution across worker threads
- Sharding to split tests across machines
- Retry for flaky scenarios
- Rerun failed scenarios
- Profiles for composable configuration
- Plugin system for extending functionality

**Test framework integration:** Standalone runner (not tied to Mocha/Jest). IDE
support via JetBrains (WebStorm, IntelliJ, Rider) for running/debugging.

**Reporting:** Built-in formatters (pretty, progress, JSON, HTML, JUnit).
Integrates with Allure, Serenity/JS, and ReportPortal.

---

### 1.4 Behave (Python)

| Attribute | Details |
| --- | --- |
| **Language** | Python |
| **Repository** | [github.com/behave/behave](https://github.com/behave/behave) |
| **GitHub Stars** | ~3,500 |
| **License** | BSD |
| **Latest Release** | v1.3.3 (September 2025) |
| **Status** | **Actively maintained.** Not officially part of the Cucumber project but functions very similarly. |

**What it does:** A standalone BDD framework for Python that uses Gherkin syntax
for feature files. Often described as "Cucumber for Python."

**Step definitions:** Decorated functions using `@given`, `@when`, `@then`
decorators with string patterns or regular expressions. Step functions receive a
`context` object for sharing state. Steps are placed in `features/steps/`
directory.

**Key features:**

- Full Gherkin support (note: `Rule` keyword support is limited in older
  versions)
- Context object for sharing state between steps
- Environment hooks (`before_all`, `after_all`, `before_feature`,
  `after_feature`, `before_scenario`, `after_scenario`, `before_step`,
  `after_step`)
- Tag-based execution filtering
- Data-driven testing with Scenario Outlines
- Integration with Django and Flask
- Support for user-defined data types

**Test framework integration:** Standalone runner; does not integrate with
pytest. For pytest integration, use pytest-bdd instead.

**Reporting:** Built-in formatters (plain, pretty, progress, JSON, JUnit).
Allure-Behave plugin for rich visual reports.

**Limitations:**

- No built-in parallel execution (workarounds exist but are complex)
- Designed primarily for black-box/acceptance testing

---

### 1.5 pytest-bdd (Python)

| Attribute | Details |
| --- | --- |
| **Language** | Python |
| **Repository** | [github.com/pytest-dev/pytest-bdd](https://github.com/pytest-dev/pytest-bdd) |
| **GitHub Stars** | ~1,400 |
| **License** | MIT |
| **Latest Release** | v8.x (2025) |
| **Status** | **Actively maintained.** Switched to the official Gherkin parser in v8.0.0. |

**What it does:** A pytest plugin that enables BDD-style testing using Gherkin
feature files. Unlike Behave, it is not a standalone framework but integrates
directly into the pytest ecosystem.

**Step definitions:** Decorated functions using `@given`, `@when`, `@then` from
`pytest_bdd`. Steps can use pytest fixtures via dependency injection. Shared
steps can be placed in `conftest.py`.

**Key features:**

- Since v8.0.0: uses the official Cucumber Gherkin parser, supporting
  DataTables, DocStrings, `Rule` keyword, and localization
- Full pytest ecosystem integration (800+ plugins)
- Pytest fixtures usable in step definitions for dependency injection
- Parallel execution via pytest-xdist
- Step parametrization
- Tag-based filtering via pytest markers
- No context object needed -- state shared via fixtures

**Test framework integration:** Native pytest plugin. Works with all pytest
plugins including pytest-html, pytest-xdist, pytest-cov, and pytest-allure.

**Reporting:** All pytest reporters work (pytest-html, Allure via
allure-pytest-bdd, JUnit XML).

---

### 1.6 Reqnroll (.NET / C#)

| Attribute | Details |
| --- | --- |
| **Language** | .NET (C#, F#, VB) |
| **Repository** | [github.com/reqnroll/Reqnroll](https://github.com/reqnroll/Reqnroll) |
| **Website** | [reqnroll.net](https://reqnroll.net/) |
| **GitHub Stars** | ~740 |
| **License** | BSD-3-Clause |
| **Latest Release** | v3.3.4 (March 2026) |
| **Status** | **Actively maintained.** The community-driven successor to SpecFlow. |

**What it does:** An open-source Cucumber-style BDD test automation framework
for .NET. A direct fork of SpecFlow, created to provide a maintained alternative
after SpecFlow's end of life (December 31, 2024).

**Step definitions:** C# methods decorated with `[Given]`, `[When]`, `[Then]`
attributes using regex or Cucumber Expressions. Step definitions are placed in
binding classes annotated with `[Binding]`.

**Key features:**

- Full Gherkin support including tagged Rule blocks
- .NET 8.0 and .NET 9.0 support
- Runs on Windows, Linux, macOS
- Regex and Cucumber Expressions for step matching
- Context injection for sharing state between steps
- Hooks (`BeforeScenario`, `AfterScenario`, `BeforeFeature`, `AfterFeature`,
  `BeforeTestRun`, `AfterTestRun`)
- Scoped bindings (tag-scoped, feature-scoped)
- Completely open-source with no licensing restrictions

**Test framework integration:** Supports MsTest, NUnit, xUnit, and TUnit.

**IDE support:** Visual Studio 2022/2026 extension, Visual Studio Code, and
JetBrains Rider.

**Reporting:** Integrates with common .NET reporting tools. Living documentation
support is in development.

**Migration from SpecFlow:** Replace SpecFlow NuGet packages with Reqnroll
equivalents, update namespaces from `TechTalk.SpecFlow` to `Reqnroll`, and run
tests. Feature files are fully compatible.

---

### 1.7 SpecFlow (.NET / C#) -- End of Life

| Attribute | Details |
| --- | --- |
| **Language** | .NET (C#, F#, VB) |
| **Status** | **End of life.** Official support ended December 31, 2024. Migrate to Reqnroll. |

**What it was:** The primary BDD framework for .NET for over a
decade, maintained by Tricentis. Functionally equivalent to Cucumber
for .NET.

**Migration path:** Reqnroll is the direct successor. Migration is
straightforward -- replace NuGet packages, update namespaces, and existing
feature files work without modification.

---

### 1.8 Behat (PHP)

| Attribute | Details |
| --- | --- |
| **Language** | PHP |
| **Repository** | [github.com/Behat/Behat](https://github.com/Behat/Behat) |
| **GitHub Stars** | ~4,000 |
| **License** | MIT |
| **Latest Release** | v3.30.0 (March 2026) |
| **Status** | **Actively maintained.** Requires PHP >=8.1. |

**What it does:** An open-source BDD framework for PHP inspired by Ruby's
Cucumber. Uses Gherkin syntax via its own PHP Gherkin parser
([Behat/cucumber-gherkin](https://github.com/Behat/cucumber-gherkin)).

**Step definitions:** PHP methods annotated with `@Given`, `@When`, `@Then` in
Context classes. Supports regular expressions and turnip-style patterns. Context
classes extend `Behat\Behat\Context\Context`.

**Key features:**

- Full Gherkin support
- Highly extensible via extensions
- Mink extension for browser automation (Selenium, Goutte, etc.)
- Symfony integration via dedicated bundles
- Supports multiple context classes
- Hook system (`BeforeSuite`, `AfterSuite`, `BeforeFeature`, `AfterFeature`,
  `BeforeScenario`, `AfterScenario`, `BeforeStep`, `AfterStep`)
- Tag-based filtering and execution
- AGENTS.md support for LLM-assisted BDD workflow

**Test framework integration:** Standalone runner. Often used alongside PHPUnit
for unit tests and Mink for browser testing.

**Reporting:** Built-in formatters (pretty, progress, JUnit). HTML reports via
third-party extensions.

**Dependencies:** Uses Symfony components (config, console,
dependency-injection, event-dispatcher, translation, yaml) supporting
Symfony ^5.4, ^6.4, and ^7.0.

---

### 1.9 Godog (Go)

| Attribute | Details |
| --- | --- |
| **Language** | Go |
| **Repository** | [github.com/cucumber/godog](https://github.com/cucumber/godog) |
| **GitHub Stars** | ~2,600 |
| **License** | MIT |
| **Latest Release** | v0.15.1 (July 2025) |
| **Status** | **Actively maintained.** Official Cucumber BDD framework for Go, part of the Cucumber organization. ~4% of Go developers use it. |

**What it does:** The official Cucumber BDD framework for Go. Parses Gherkin
feature files and runs them against step definitions written in Go.

**Step definitions:** Go functions registered via `ScenarioContext` methods
(`s.Step`) with Cucumber Expressions or regular expressions. Step functions
receive `context.Context` and return `error`.

**Key features:**

- Does not interfere with `go test` -- can work alongside standard tests
- Uses the Go compiler and linker to produce test executables
- `TestFeatures` function acts as a regular Go test
- Supports all Gherkin keywords including `Rule`
- Tags for filtering scenarios
- Hooks (`BeforeSuite`, `AfterSuite`, `BeforeScenario`, `AfterScenario`,
  `BeforeStep`, `AfterStep`)
- Formatters: pretty, progress, JUnit, Cucumber JSON

**Test framework integration:** Integrates with `go test` via `TestMain` or
`TestFeatures`. Compatible with standard Go testing tools and IDE test runners.

**Reporting:** Built-in formatters for JUnit XML and Cucumber JSON. Third-party
integration with Allure-Go available.

---

### 1.10 Karate (Java / API Testing)

| Attribute | Details |
| --- | --- |
| **Language** | Java (JVM) |
| **Repository** | [github.com/karatelabs/karate](https://github.com/karatelabs/karate) |
| **GitHub Stars** | ~8,800 |
| **License** | MIT |
| **Latest Release** | v2.0.2 (April 2026) |
| **Status** | **Actively maintained.** One of the most popular API testing frameworks. |

**What it does:** An open-source unified test automation framework
that combines API testing, mocking, performance testing, and UI
automation. Uses a Gherkin-like DSL -- tests are written in `.feature`
files but **do not require separate step definition files**.

**Step definitions:** Unlike traditional Cucumber implementations, Karate has
built-in step definitions. Assertions, HTTP calls, and JSON/XML manipulation are
part of the DSL itself. No glue code is needed.

**Key features:**

- **No separate step definitions needed** -- the DSL handles everything
- Multi-protocol: REST, SOAP, GraphQL, WebSocket, gRPC
- Built-in JSON and XML assertion library
- Data-driven testing with dynamic expressions
- Built-in parallel execution
- Performance testing via Gatling integration
- UI automation (browser testing) built in
- Mock server capabilities
- Automatic HTML report generation
- CI/CD integration via Maven or Gradle

**Test framework integration:** Runs via JUnit 5 or standalone. Can be executed
through Maven or Gradle.

**Reporting:** Automatically produces detailed HTML reports. Integrates with
Allure and Cluecumber.

**Important distinction:** While Karate uses Gherkin-like syntax, it is not a
traditional BDD framework. It is primarily an API and test automation tool that
leverages the Given/When/Then format for readability.

---

### 1.11 Other BDD Frameworks

#### GoBDD (Go -- Alternative)

| Attribute | Details |
| --- | --- |
| **Repository** | [github.com/go-bdd/gobdd](https://github.com/go-bdd/gobdd) |
| **Status** | Stable (API stable since v1.0). Alternative to Godog. |

An alternative BDD framework for Go with Gherkin support. Simpler API than
Godog.

#### Radish (Python -- Extended Gherkin)

| Attribute | Details |
| --- | --- |
| **Repository** | [github.com/radish-bdd/radish](https://github.com/radish-bdd/radish) |
| **Status** | Maintained but less widely adopted than Behave or pytest-bdd. |

Extends standard Gherkin with scenario loops, preconditions, and constants.
Offers more programmatic control at the Gherkin layer.

#### Lettuce (Python -- Deprecated)

| Attribute | Details |
| --- | --- |
| **Repository** | [github.com/gabrielfalcao/lettuce](https://github.com/gabrielfalcao/lettuce) |
| **Status** | **Abandoned.** Not updated since 2016. No Python 3 migration. Do not use for new projects. |

#### CWT-Cucumber (C++)

| Attribute | Details |
| --- | --- |
| **Repository** | [github.com/ThoSe1990/cwt-cucumber](https://github.com/ThoSe1990/cwt-cucumber) |
| **Status** | **Actively maintained.** Last updated November 2025. Modern C++20. |

A lightweight C++20 BDD testing framework. Interprets Gherkin feature files with
no mandatory dependencies. Supports Scenario, Scenario Outline, Background,
Rules, Hooks, Doc Strings, and Tables.

#### Cucumber-cpp (C++)

| Attribute | Details |
| --- | --- |
| **Website** | [cucumber.io/docs/installation/cplusplus/](https://cucumber.io/docs/installation/cplusplus/) |
| **Status** | **Less active.** The original C++ Cucumber implementation. Supports step definitions with gtest or CppUnit. |

#### Cucumber-Rust (Rust)

| Attribute | Details |
| --- | --- |
| **Repository** | [github.com/cucumber-rs/cucumber](https://github.com/cucumber-rs/cucumber) |
| **Status** | Unofficial implementation for Rust. |

#### Test::BDD::Cucumber (Perl)

| Attribute | Details |
| --- | --- |
| **Status** | Semi-official Cucumber implementation for Perl. |

---

## 2. Gherkin Parsers and Libraries

Standalone parsers that read `.feature` files and produce structured data.

### 2.1 Official Cucumber Gherkin Parser (Multi-Language)

| Attribute | Details |
| --- | --- |
| **Repository** | [github.com/cucumber/gherkin](https://github.com/cucumber/gherkin) |
| **GitHub Stars** | ~320 |
| **License** | MIT |
| **Latest Release** | v39.0.0 (March 2026) |
| **Status** | **Actively maintained.** The canonical Gherkin parser used by all official Cucumber implementations. |

**What it does:** A parser and compiler for the Gherkin language, available as
libraries for multiple programming languages.

**Available implementations:** Java, C#, Ruby, JavaScript/TypeScript, Go,
Python, PHP, C, C++, Dart, Objective-C.

**Architecture -- Two-stage pipeline:**

1. **Scanner + Parser => AST:** The scanner reads a `.feature` file, creating
   tokens for each line. The parser (generated by the Berp parser generator)
   outputs an Abstract Syntax Tree (AST) representing the full document
   structure.

2. **Compiler: AST => Pickles:** The AST is compiled into a simpler
   representation called *Pickles*, which are suitable for execution
   by Cucumber.

**Pickle format details:**

- Each `Scenario` compiles into one Pickle with a list of PickleSteps
- Each `Examples` row under `Scenario Outline` compiles into a separate Pickle
- `Background` steps are prepended to each Pickle
- Tags are inherited from parent elements (Feature, Rule)
- The Pickle format decouples Gherkin from Cucumber, allowing alternative input
  formats (e.g., Markdown)

**Multi-language support:** The parser supports the `# language:` header
directive, dynamically reconfiguring keyword recognition. All supported keywords
are defined in `gherkin-languages.json` (76+ languages/dialects).

**Package names by language:**

- Java: `io.cucumber:gherkin` (Maven Central)
- Python: `gherkin-official` (PyPI)
- JavaScript: `@cucumber/gherkin` (npm)
- Ruby: `cucumber-gherkin` (RubyGems)
- Go: `github.com/cucumber/gherkin/go`
- PHP: `behat/cucumber-gherkin` (Packagist)

**Cucumber Messages:** The parser outputs structured data as Cucumber Messages
(Protobuf/JSON), a protocol used by all Cucumber tools for interoperability.

---

### 2.2 Behat Gherkin Parser (PHP)

| Attribute | Details |
| --- | --- |
| **Repository** | [github.com/Behat/cucumber-gherkin](https://github.com/Behat/cucumber-gherkin) |
| **Status** | **Actively maintained.** Updated January 2026. |

A PHP implementation of the Cucumber Gherkin parser, used by Behat. Follows the
official Cucumber Gherkin specification.

---

### 2.3 Tree-sitter Gherkin Grammars

| Attribute | Details |
| --- | --- |
| **Repository** | [github.com/binhtran432k/tree-sitter-gherkin](https://github.com/binhtran432k/tree-sitter-gherkin) |
| **Status** | **Maintained.** Updated February 2025. |

A tree-sitter grammar for Gherkin, providing fast incremental parsing for use in
editors like Neovim, Helix, and Zed. Enables accurate syntax highlighting and
structural code navigation.

An alternative implementation exists at
[github.com/SamyAB/tree-sitter-gherkin](https://github.com/SamyAB/tree-sitter-gherkin).

---

## 3. Linting and Style Checking Tools

### 3.1 gherkin-lint (JavaScript / Node.js)

| Attribute | Details |
| --- | --- |
| **Repository** | [github.com/gherkin-lint/gherkin-lint](https://github.com/gherkin-lint/gherkin-lint) |
| **npm** | [npmjs.com/package/gherkin-lint](https://www.npmjs.com/package/gherkin-lint) |
| **GitHub Stars** | ~196 |
| **License** | ISC |
| **Latest Release** | v4.2.4 |
| **Status** | **Maintained but infrequent updates.** Last release December 2023. |

**What it does:** Parses Gherkin feature files and runs configurable lint rules
against them.

**Key features:**

- Default rules (always on) and configurable rules (off by default)
- Configuration via `.gherkin-lintrc` file (JSON with comments)
- Ignore files via `.gherkin-lintignore` or `--ignore` CLI flag
- Custom rules directories via `--rulesdir`
- Output formats: stylish (default), JSON, xunit
- Integrated into [MegaLinter](https://megalinter.io/) for CI/CD pipelines

**Rules include:**

- `no-dupe-scenario-names` -- no duplicate scenario names
- `no-dupe-feature-names` -- no duplicate feature names
- `no-trailing-spaces` -- no trailing whitespace
- `no-multiple-empty-lines` -- no consecutive blank lines
- `indentation` -- consistent indentation
- `new-line-at-eof` -- newline at end of file
- `no-unnamed-features` / `no-unnamed-scenarios` -- all elements must be named
- `max-scenarios-per-file` -- limit scenario count
- `no-background-only-scenario` -- Background must serve multiple scenarios
- Many more configurable rules

**Installation:** `npm install gherkin-lint`

---

### 3.2 gherlint (Python)

| Attribute | Details |
| --- | --- |
| **Repository** | [github.com/DudeNr33/gherlint](https://github.com/DudeNr33/gherlint) |
| **PyPI** | [pypi.org/project/gherlint](https://pypi.org/project/gherlint/) |
| **License** | MIT |
| **Latest Release** | November 2025 |
| **Status** | **Actively maintained.** Early development phase, new checks being added. Requires Python >=3.10. |

**What it does:** A Python-based linter for Gherkin feature files.

**Key features:**

- CLI commands: `gherlint lint <path>` for recursive linting, `gherlint stats
  <path>` for metrics
- `fix-language-tags` command to auto-fix missing/incorrect language tags
- Checks for unparseable files, missing parameters, and structural issues
- Growing set of rules

**Installation:** `pip install gherlint`

---

### 3.3 gherkin_lint (Ruby / Docker)

| Attribute | Details |
| --- | --- |
| **Repository** | [github.com/funkwerk/gherkin_lint](https://github.com/funkwerk/gherkin_lint) |
| **Docker** | [hub.docker.com/r/gherkin/lint](https://hub.docker.com/r/gherkin/lint) |
| **Status** | **Maintained.** |

**What it does:** A Ruby-based linter for Gherkin feature files, also available
as a Docker image.

**Key features:**

- Enable/disable checks via `--enable`/`--disable` flags
- Disable checks per-feature using `@disableCHECK` tags
- Configuration via `.gherkin_lint.yml`
- Docker support: `docker run -ti -v $(pwd):/src -w /src gherkin/lint *.feature`
- Errors (affect return code) and warnings (informational)

**Installation:** `gem install gherkin_lint` or via Docker.

---

### 3.4 MegaLinter Gherkin Integration

| Attribute | Details |
| --- | --- |
| **Repository** | [github.com/oxsecurity/megalinter](https://github.com/oxsecurity/megalinter) |
| **Documentation** | [megalinter.io/latest/descriptors/gherkin/](https://megalinter.io/latest/descriptors/gherkin/) |
| **Status** | **Actively maintained.** v9 released 2025. |

**What it does:** MegaLinter is a comprehensive multi-language linter aggregator
(50+ languages) that includes built-in Gherkin linting via gherkin-lint.

**Key features:**

- Runs gherkin-lint as `GHERKIN_GHERKIN_LINT` descriptor
- Works on `.feature` files
- Configurable include/exclude regex patterns
- Pre/post command hooks
- Docker-based -- runs in CI/CD pipelines (GitHub Actions, GitLab CI, Jenkins,
  Azure DevOps)
- Auto-generates configuration via `npx mega-linter-runner --install`

---

### 3.5 Gherkin Linter (VS Code Extension)

| Attribute | Details |
| --- | --- |
| **Marketplace** | [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=undertest.undertest-featurelint) |
| **Status** | Available on VS Code Marketplace. |

An opinionated VS Code extension that lints Gherkin feature files inline as you
type.

---

## 4. IDE Support and Editor Plugins

### 4.1 VS Code Extensions

#### 4.1.1 Cucumber Official Extension

| Attribute | Details |
| --- | --- |
| **Publisher** | CucumberOpen |
| **Marketplace** | [Cucumber for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=CucumberOpen.cucumber-official) |
| **Repository** | [github.com/cucumber/vscode](https://github.com/cucumber/vscode) |
| **GitHub Stars** | ~84 |
| **Status** | **Actively maintained** by the Cucumber team. |

**Features:**

- Powered by the Cucumber Language Server
- Syntax highlighting for Gherkin keywords and step parameters
- Auto-complete suggestions from existing step definitions (best with Cucumber
  Expressions)
- Go-to-step-definition navigation
- Step definition snippet generation via Quick Fix
- Underlines undefined steps and syntax errors
- Available on both VS Code Marketplace and Open VSX Registry

#### 4.1.2 Cucumber (Gherkin) Full Support

| Attribute | Details |
| --- | --- |
| **Publisher** | alexkrechik |
| **Marketplace** | [Cucumber (Gherkin) Full Support](https://marketplace.visualstudio.com/items?itemName=alexkrechik.cucumberautocomplete) |
| **Repository** | [github.com/alexkrechik/VSCucumberAutoComplete](https://github.com/alexkrechik/VSCucumberAutoComplete) |
| **Status** | Maintained; widely used. |

**Features:**

- Full language support for Gherkin
- Auto-complete for steps from step definition files
- Go-to-step-definition
- Formatting
- Multi-language step definition support (JS, TS, Python, Ruby, Kotlin, Java)

#### 4.1.3 Gherkin Extension (Enhanced Fork)

| Attribute | Details |
| --- | --- |
| **Publisher** | viktor-silakov |
| **Repository** | [github.com/viktor-silakov/gherkin-extension](https://github.com/viktor-silakov/gherkin-extension) |
| **Status** | Actively maintained fork of CucumberAutoComplete. |

**Features:**

- Automatic step definition generation via Quick Fix
- Enhanced autocompletion with context-aware filtering
- Custom templates with multi-language support (JS, TS, Ruby, Java, Python,
  Kotlin)
- Bug fixes over the original CucumberAutoComplete

#### 4.1.4 Cucumber Step Definition Generator

| Attribute | Details |
| --- | --- |
| **Marketplace** | [Step Definition Generator](https://marketplace.visualstudio.com/items?itemName=nguyenngoclong.cypress-cucumber-step-definition-generator) |
| **Status** | Available. |

Generates step definitions for Cypress, Playwright, and CucumberJS from feature
files. Auto-detects DataTable, DocString, int, float, string types.

#### 4.1.5 Other VS Code Extensions

- **Snippets and Syntax Highlight for Gherkin** (`stevejpurves.cucumber`) --
  Lightweight; provides code snippets and syntax highlighting.
- **Gherkin Editor** (`nguyenngoclong.gherkin-editor`) -- Beautiful syntax
  highlighting, code completion, formatting, and validation.
- **Gherkin Syntax Highlight and Formatter** (`korostylov.gherkin-highlight`) --
  Syntax highlighting and formatting.
- **Gherkin Beautifier** (`siarheikuchuk.gherkin-beautifier-vs-code-plugin`) --
  Multilingual indentation plugin for `.feature` files.
- **Gherkin VSCode**
  ([github.com/kieran-ryan/gherkin-vscode](https://github.com/kieran-ryan/gherkin-vscode))
  -- TextMate-based syntax highlighting.

---

### 4.2 JetBrains / IntelliJ Plugins

#### 4.2.1 Gherkin Plugin (Core)

| Attribute | Details |
| --- | --- |
| **Marketplace** | [Gherkin Plugin](https://plugins.jetbrains.com/plugin/9164-gherkin) |
| **Status** | **Bundled in IntelliJ Ultimate.** Available for all JetBrains IDEs. |

Adds Gherkin language support with syntax highlighting and coding assistance for
step definitions. The foundation for language-specific Cucumber plugins.

#### 4.2.2 Cucumber for Java

| Attribute | Details |
| --- | --- |
| **Marketplace** | [Cucumber for Java](https://plugins.jetbrains.com/plugin/7212-cucumber-for-java) |
| **Status** | **Actively maintained.** Bundled in IntelliJ Ultimate. |

**Features:**

- Coding assistance for Java step definitions
- Dedicated run/debug configuration for Cucumber scenarios
- Go-to-step-definition navigation
- Step usage search

#### 4.2.3 Cucumber.js

| Attribute | Details |
| --- | --- |
| **Marketplace** | [Cucumber.js Plugin](https://plugins.jetbrains.com/plugin/7418-cucumber-js) |
| **Status** | **Actively maintained.** Works in WebStorm, IntelliJ, Rider. |

Cucumber.js-aware syntax highlighting for JavaScript and TypeScript step
definitions. Supports running/debugging scenarios directly from the IDE.

#### 4.2.4 Cucumber+

| Attribute | Details |
| --- | --- |
| **Marketplace** | [Cucumber+](https://plugins.jetbrains.com/plugin/16289-cucumber-) |
| **Status** | Maintained. |

Enhanced Cucumber experience with support for Java, Kotlin, and Scala. Includes
rewriting breakpoint support and improved editing/printing of Gherkin features.

#### 4.2.5 Cucumber for Kotlin and Android

| Attribute | Details |
| --- | --- |
| **Marketplace** | [Cucumber for Kotlin and Android](https://plugins.jetbrains.com/plugin/22107-cucumber-for-kotlin-and-android) |

Step definitions in Kotlin; run Cucumber as Android Instrumented tests directly
from the IDE.

#### 4.2.6 Cucumber Go

| Attribute | Details |
| --- | --- |
| **Marketplace** | [Cucumber Go](https://plugins.jetbrains.com/plugin/24323-cucumber-go) |

Gherkin support in GoLand: syntax highlighting, code completion, go-to-step-
definition, and find usages for Godog projects.

#### 4.2.7 Gherkin Overview

| Attribute | Details |
| --- | --- |
| **Marketplace** | [Gherkin Overview](https://plugins.jetbrains.com/plugin/16716-gherkin-overview) |

Visualizes the structure of test projects with `.feature` files, providing a
bird's-eye view of features, scenarios, and tags.

---

### 4.3 Vim / Neovim

#### 4.3.1 vim-cucumber (Tim Pope)

| Attribute | Details |
| --- | --- |
| **Repository** | [github.com/tpope/vim-cucumber](https://github.com/tpope/vim-cucumber/) |
| **Status** | **Maintained.** The definitive Vim plugin for Gherkin. |

**Features:**

- Syntax highlighting for `.feature` files
- Indentation support
- Jump to step definitions: `[<C-d>`, `]<C-d>` (replace buffer), `<C-W>d`
  (split)
- Works with Ruby Cucumber step definitions

#### 4.3.2 Neovim Built-in Syntax

Neovim ships with a built-in `cucumber.vim` syntax file
(`runtime/syntax/cucumber.vim`) providing Gherkin highlighting out of
the box for `.feature` files.

#### 4.3.3 vim-polyglot

| Attribute | Details |
| --- | --- |
| **Repository** | [github.com/sheerun/vim-polyglot](https://github.com/sheerun/vim-polyglot) |

A comprehensive language pack that bundles Gherkin/Cucumber syntax highlighting.
Lazy-loaded for performance.

#### 4.3.4 tree-sitter-gherkin (Neovim/Helix/Zed)

For editors supporting tree-sitter (Neovim with `nvim-treesitter`, Helix, Zed),
the
[tree-sitter-gherkin](https://github.com/binhtran432k/tree-sitter-gherkin)
grammar provides accurate incremental parsing and highlighting.

---

### 4.4 Emacs

#### 4.4.1 cucumber.el / feature-mode

| Attribute | Details |
| --- | --- |
| **Repository** | [github.com/freesteph/cucumber.el](https://github.com/michaelklishin/cucumber.el) |
| **Status** | **Actively maintained.** Copyright 2008--2025. Requires Emacs 28.1+. |

**Features:**

- Syntax highlighting for Gherkin with multi-language keyword support via
  `# language:` directive
- Key bindings for running scenarios and features
- Docker-compose integration (auto-detected)
- Jump to step definitions
- Available via MELPA

#### 4.4.2 pickle-mode

| Attribute | Details |
| --- | --- |
| **Repository** | [github.com/ahungry/pickle-mode](https://github.com/ahungry/pickle-mode) |

An alternative Emacs major mode for Gherkin feature files.

#### 4.4.3 Ecukes

| Attribute | Details |
| --- | --- |
| **Repository** | [github.com/ecukes/ecukes](https://github.com/ecukes/ecukes) |

Cucumber for Emacs -- a BDD testing framework for Emacs Lisp packages (not a
feature file editor, but uses Gherkin for Emacs package testing).

---

### 4.5 Visual Studio

#### Reqnroll for Visual Studio

| Attribute | Details |
| --- | --- |
| **Marketplace** | [Reqnroll for Visual Studio 2022 and 2026](https://marketplace.visualstudio.com/items?itemName=Reqnroll.ReqnrollForVisualStudio2022) |
| **Repository** | [github.com/reqnroll/Reqnroll.VisualStudio](https://github.com/reqnroll/Reqnroll.VisualStudio) |
| **Status** | **Actively maintained.** |

Features syntax highlighting, IntelliSense for Gherkin, go-to-step-definition,
step definition generation, and test explorer integration for Reqnroll and
SpecFlow projects.

---

## 5. Reporting and Documentation Tools

### 5.1 Cucumber Built-in Reporting

All official Cucumber implementations include built-in formatters:

| Format | Description |
| --- | --- |
| **Pretty** | Colored terminal output showing steps and results |
| **Progress** | Compact dot-based output |
| **JSON** | Machine-readable JSON (input for other reporting tools) |
| **JUnit XML** | Standard CI/CD test result format |
| **HTML** | Self-contained HTML report |
| **Rerun** | Lists failed scenarios for re-execution |
| **Message** | Cucumber Messages protocol (Protobuf/JSON) |

The **Cucumber Messages** protocol is the modern standard for tool
interoperability.

---

### 5.2 Allure Report

| Attribute | Details |
| --- | --- |
| **Repository** | [github.com/allure-framework/allure2](https://github.com/allure-framework/allure2) |
| **Website** | [allurereport.org](https://allurereport.org/) |
| **GitHub Stars** | ~5,300 |
| **License** | Apache-2.0 |
| **Latest Release** | v2.39.0 (April 2026) |
| **Status** | **Actively maintained.** One of the most popular test reporting tools. |

**What it does:** A flexible, lightweight multi-language test
reporting tool that generates rich interactive HTML reports with
charts, timelines, and drill-down
capabilities.

**Cucumber integrations:**

- `allure-cucumber` (Ruby)
- `allure-cucumberjvm` (Java)
- `allure-cucumberjs` (JavaScript)
- `allure-pytest-bdd` (Python pytest-bdd)
- `allure-behave` (Python Behave)

**Key features:**

- Interactive dashboards with pass/fail statistics
- Step-by-step execution details with attachments (screenshots, logs)
- History and trend analysis across builds
- Categories and severity classification
- Links to issues and TMS tickets
- CI/CD integration (Jenkins, GitLab CI, GitHub Actions)
- Allure TestOps for centralized reporting and analytics

---

### 5.3 Serenity BDD (Java)

| Attribute | Details |
| --- | --- |
| **Repository** | [github.com/serenity-bdd/serenity-core](https://github.com/serenity-bdd/serenity-core) |
| **GitHub Stars** | ~750 |
| **License** | Apache-2.0 |
| **Latest Release** | v5.3.9 |
| **Status** | **Actively maintained**, though a 2026 critique highlights growing dependency management challenges. |

**What it does:** An acceptance testing and reporting library for Java
(previously known as Thucydides). Provides deep Cucumber integration with rich,
narrative-style HTML reports.

**Key features:**

- Requirements-based reporting (Capabilities, Features)
- Screenplay pattern support
- Cucumber 6.x+ integration via `serenity-cucumber`
- Step-by-step reporting with screenshots
- JUnit 5 integration
- Parallel execution (since v3.6.0)
- Living documentation from feature files

**Considerations:** Heavy dependency footprint. For simpler needs, Allure +
Cucumber may be lighter-weight.

---

### 5.4 Serenity/JS (JavaScript / TypeScript)

| Attribute | Details |
| --- | --- |
| **Repository** | [github.com/serenity-js/serenity-js](https://github.com/serenity-js/serenity-js) |
| **Website** | [serenity-js.org](https://serenity-js.org/) |
| **GitHub Stars** | ~610 |
| **License** | Apache-2.0 |
| **Latest Release** | v3.42.1 (April 2026) |
| **Status** | **Actively maintained.** |

**What it does:** A full-stack acceptance testing framework for
JavaScript/TypeScript with in-depth HTML reports. Integrates with every version
of Cucumber.js, as well as Playwright, Protractor, and WebdriverIO.

**Key features:**

- `@serenity-js/cucumber` adapter for Cucumber.js
- Serenity BDD Reporter for rich HTML reports
- Ships with Serenity BDD CLI .jar (since v3.30.0)
- Screenplay pattern
- ConsoleReporter for terminal output

---

### 5.5 Cucumber-Reporting (Java)

| Attribute | Details |
| --- | --- |
| **Repository** | [github.com/damianszczepanik/cucumber-reporting](https://github.com/damianszczepanik/cucumber-reporting) |
| **GitHub Stars** | ~566 |
| **License** | LGPL |
| **Status** | **Actively maintained.** |

**What it does:** Converts Cucumber JSON reports into pretty HTML reports with
charts. Originally created to publish on Jenkins.

**Key features:**

- Feature overview with pass/fail statistics
- Detailed feature reports with step-level results
- Trend charts across builds
- Offline-capable (no external dependencies in generated reports)
- Available as standalone library or Maven plugin
  ([maven-cucumber-reporting](https://github.com/damianszczepanik/maven-cucumber-reporting))

---

### 5.6 Cluecumber (Java / Maven)

| Attribute | Details |
| --- | --- |
| **Repository** | [github.com/trivago/cluecumber](https://github.com/trivago/cluecumber) |
| **GitHub Stars** | ~290 |
| **License** | Apache-2.0 |
| **Latest Release** | v3.14.0 (March 2026) |
| **Status** | **Actively maintained** by trivago. |

**What it does:** Creates clear, concise aggregated test reports from
Cucumber-compatible JSON files (works with Cucumber BDD and Karate output).

**Key features:**

- Scenarios grouped by status (passed, failed, skipped)
- Scenario sequence in running order
- Step details with hooks, stack traces, and attachments
- Tag overview and exception types
- Custom parameters on report start page
- Maven plugin or Core API integration
- Requirements: Java >= 8, Maven >= 3.3.9

**Usage:** `mvn cluecumber-report:reporting` or programmatic via Cluecumber Core
API.

---

### 5.7 Pickles (Living Documentation -- End of Life)

| Attribute | Details |
| --- | --- |
| **Repository** | [github.com/picklesdoc/pickles](https://github.com/picklesdoc/pickles) |
| **GitHub Stars** | ~479 |
| **License** | Apache-2.0 |
| **Latest Release** | v4.0.3 (November 2022) |
| **Status** | **End of life.** Since SpecFlow has been end-of-lifed and Pickles was built around SpecFlow, the project has been discontinued. |

**What it was:** An open-source living documentation generator that transformed
Gherkin feature files into navigable HTML, Word, Excel, or JSON documentation.
Could include Markdown files for additional context and integrate test results.

---

### 5.8 ReportPortal

| Attribute | Details |
| --- | --- |
| **Website** | [reportportal.io](https://reportportal.io/) |
| **Status** | **Actively maintained.** |

**What it does:** An AI-powered test automation dashboard that stores and
analyzes test results from multiple frameworks, including Cucumber.

**Cucumber agents:**

- `agent-java-cucumber` (Java)
- `agent-js-cucumber` (JavaScript)
- `agent-python-pytest-bdd` (Python)

**Key features:**

- Real-time test result aggregation
- Root cause analysis and failure classification (product bug, automation issue,
  system issue)
- ML-based auto-analysis of failures
- Integration with Jenkins, Jira, and many test frameworks
- Trend analysis across builds

---

## 6. Other Tools

### 6.1 Formatters and Pretty-Printers

#### prettier-plugin-gherkin (Prettier / npm)

| Attribute | Details |
| --- | --- |
| **Repository** | [github.com/mapado/prettier-plugin-gherkin](https://github.com/mapado/prettier-plugin-gherkin) |
| **npm** | [npmjs.com/package/prettier-plugin-gherkin](https://www.npmjs.com/package/prettier-plugin-gherkin) |
| **GitHub Stars** | ~19 |
| **Latest Release** | v3.1.2 (March 2025) |
| **Status** | **Actively maintained.** |

Formats `.feature` files using Prettier. Ideal for CI/CD enforcement via
`prettier --check`. Install: `npm install prettier-plugin-gherkin`.

#### @cucumber/pretty-formatter (npm)

| Attribute | Details |
| --- | --- |
| **npm** | [npmjs.com/package/@cucumber/pretty-formatter](https://www.npmjs.com/package/@cucumber/pretty-formatter) |
| **Status** | **Actively maintained.** Updated February 2026. |

Prints Cucumber test progress in a prettified Gherkin-style format for terminal
output.

#### gherkin-formatter (Python / PyPI)

| Attribute | Details |
| --- | --- |
| **PyPI** | [pypi.org/project/gherkin-formatter](https://pypi.org/project/gherkin-formatter/) |

A CLI tool to format Gherkin `.feature` files. Suitable for Python-based CI/CD
pipelines.

#### gherkin-formatter (Java / GitLab)

| Attribute | Details |
| --- | --- |
| **Repository** | [gitlab.com/jamietanna/gherkin-formatter](https://gitlab.com/jamietanna/gherkin-formatter) |

A Java utility to convert parsed Gherkin files to pretty-printed strings.

---

### 6.2 GherKing (Gherkin Precompiler / JavaScript)

| Attribute | Details |
| --- | --- |
| **Repository** | [github.com/gherking/gherking](https://github.com/gherking/gherking) |
| **Website** | [gherking.github.io](https://gherking.github.io/) |
| **npm** | [npmjs.com/package/gherking](https://www.npmjs.com/package/gherking) |
| **Status** | **Actively maintained.** Updated November 2025. |

**What it does:** A tool to programmatically handle Cucumber/Gherkin feature
files in JavaScript/TypeScript. Provides a precompiler pipeline that transforms
`.feature` files before they are executed.

**Available precompilers (gpc-* packages):**

| Package | Purpose |
| --- | --- |
| `gpc-filter` | Include/exclude scenarios based on tag expressions |
| `gpc-for-loop` | Loop scenarios and outlines for repetition |
| `gpc-license` | Add license statements to feature files |
| `gpc-macro` | Create and execute macros |
| `gpc-remove-comments` | Remove semantic comments |
| `gpc-remove-duplicates` | Remove duplicate tags or example rows |
| `gpc-replacer` | Replace keywords/strings in feature files |
| `gpc-scenario-numbering` | Add index numbers to scenario names |
| `gpc-step-groups` | Correct Gherkin step keywords for readability |
| `gpc-test-data` | Load external data (JSON, CSV, XLSX) into Examples tables |

**Usage:**

```bash
npm install -g gherking
gherking --config .gherking.json --base e2e/features/src --destination e2e/features/dist
```

---

### 6.3 Test Management Tools with Gherkin Support

#### CucumberStudio (SmartBear)

| Attribute | Details |
| --- | --- |
| **Website** | [cucumberstudio.com](https://cucumber.io/tools/cucumberstudio/) |
| **Atlassian Marketplace** | [CucumberStudio - BDD & Test Management](https://marketplace.atlassian.com/apps/1212743/cucumberstudio-bdd-test-management) |
| **Status** | **Active.** v1.1.28-AC (April 2025) for Jira Cloud. |

Collaboration platform for BDD teams. Allows authoring Gherkin scenarios,
linking to Jira issues, generating test scripts for Cucumber/SpecFlow/RSpec, and
Git integration.

#### Xray for Jira

| Attribute | Details |
| --- | --- |
| **Website** | [getxray.app](https://docs.getxray.app/) |
| **Status** | **Actively maintained.** Market leader for BDD in Jira. |

Write Gherkin scenarios directly as Jira issues, export to Cucumber for
execution, and import results back. Full traceability from requirements to
scenarios to defects. Deep Jira integration (not available outside Jira).

#### AssertThat for Jira

| Attribute | Details |
| --- | --- |
| **Website** | [assertthat.com](https://www.assertthat.com/) |
| **Status** | **Active.** Atlassian Cloud and Data Center. |

Author Gherkin feature files within Jira, link scenarios to issues, manage
execution results, and export features for CI/CD. Free online Gherkin editor
available.

#### Testomat.io

| Attribute | Details |
| --- | --- |
| **Website** | [testomat.io](https://testomat.io/) |
| **Status** | **Actively maintained.** |

Test management with a built-in Gherkin editor, AI-assisted BDD scenario
generation, and Jira integration (via Advanced Jira plugin). Can import manual
test cases and auto-convert to BDD scenarios.

#### TestQuality

| Attribute | Details |
| --- | --- |
| **Website** | [testquality.com](https://www.testquality.com/gherkin) |
| **Status** | **Active.** |

Natively imports Gherkin feature files, integrates with GitHub and Jira, and
centralizes automated test results from Cucumber and other BDD frameworks.

---

### 6.4 AI / LLM-Based Gherkin Tools

#### Gherkinizer

| Attribute | Details |
| --- | --- |
| **Website** | [gherkinizer.com](https://gherkinizer.com/) |
| **Status** | **Active** (2025--2026). |

AI-powered tool that converts natural-language requirements into BDD
Gherkin test cases. Identifies edge cases, generates step bindings,
and produces executable
specifications.

#### Workik Cucumber Test Case Generator

| Attribute | Details |
| --- | --- |
| **Website** | [workik.com/cucumber-test-case-generator](https://workik.com/cucumber-test-case-generator) |
| **Status** | **Active.** |

AI-powered generator that creates Cucumber scenarios from user stories.
Auto-detects UI changes and updates Gherkin steps. Identifies redundant
scenarios and refactors tests.

#### LLM-Based Approaches (GPT-4, Claude, etc.)

Large language models are increasingly used to:

- Generate Gherkin feature files from plain-English user stories or
  requirements
- Generate step definition code in Java, JavaScript, Python, Ruby, and other
  languages
- Suggest edge cases and negative scenarios
- Refactor and maintain existing feature files
- Use Gherkin as a structured prompt format for code generation (the
  Given/When/Then format constrains LLM output for more reliable results)

**Key trend (2025--2026):** Gherkin's structured natural-language
format makes it an ideal interface between human intent and
LLM-generated code. BDD workflows
increasingly use AI to generate specifications and AI to generate
implementations from those specifications.

---

### 6.5 CI/CD Integration Summary

Most Gherkin tools integrate with CI/CD through standard mechanisms:

| CI/CD Tool | Integration Method |
| --- | --- |
| **GitHub Actions** | Run Cucumber/BDD tests as workflow steps; MegaLinter action for linting |
| **Jenkins** | Cucumber Reports plugin; cucumber-reporting library; Allure plugin |
| **GitLab CI** | JUnit XML artifacts; Allure reports; Docker-based linting |
| **Azure DevOps** | Reqnroll extension; Xray integration; JUnit test results |
| **CircleCI** | JUnit XML test results; Allure report generation |

**Recommended CI/CD patterns:**

1. **Lint:** Run `gherkin-lint` or MegaLinter on `.feature` files
2. **Format check:** Run `prettier --check` with `prettier-plugin-gherkin`
3. **Execute:** Run BDD tests with chosen framework
4. **Report:** Generate Allure/HTML reports and publish as artifacts
5. **Analyze:** Import results to ReportPortal or Allure TestOps for trend
   analysis

---

## Quick Reference: Choosing a Tool

### By Language

| Language | Primary BDD Framework | Alternative |
| --- | --- | --- |
| **Ruby** | Cucumber-Ruby | -- |
| **Java/JVM** | Cucumber-JVM | Karate (API), Serenity BDD |
| **JavaScript/TS** | Cucumber-JS | Serenity/JS |
| **Python** | pytest-bdd (pytest users), Behave (standalone) | Radish |
| **.NET/C#** | Reqnroll | -- |
| **PHP** | Behat | -- |
| **Go** | Godog | GoBDD |
| **C++** | CWT-Cucumber | cucumber-cpp |
| **Rust** | cucumber-rs | -- |

### By Need

| Need | Recommended Tool |
| --- | --- |
| **Parse feature files** | Official Cucumber Gherkin parser (`cucumber/gherkin`) |
| **Lint feature files** | gherkin-lint (JS), gherlint (Python), gherkin_lint (Ruby) |
| **Format feature files** | prettier-plugin-gherkin, gherkin-formatter |
| **VS Code editing** | Official Cucumber extension or Gherkin Extension (viktor-silakov) |
| **JetBrains editing** | Gherkin + Cucumber for Java/JS/Kotlin/Go plugins |
| **Test reporting** | Allure Report (multi-language), Serenity BDD (Java), Cluecumber (Maven) |
| **Living documentation** | Allure, Serenity BDD, Testomat.io |
| **Test management** | Xray (Jira), CucumberStudio, TestQuality |
| **AI/LLM generation** | Gherkinizer, Workik, or direct LLM prompting |
| **Feature file preprocessing** | GherKing |
| **CI/CD linting** | MegaLinter with gherkin-lint |

---

## Sources

- [Cucumber Official Documentation](https://cucumber.io/docs/)
- [Cucumber Installation Guide (All Languages)](https://cucumber.io/docs/installation/)
- [Cucumber in 2025, Year in Review](https://cucumber.io/blog/open-source/cucumber-in-2025-year-in-review/)
- [Cucumber GitHub Organization](https://github.com/cucumber)
- [cucumber-jvm on GitHub](https://github.com/cucumber/cucumber-jvm)
- [cucumber-js on GitHub](https://github.com/cucumber/cucumber-js)
- [cucumber-ruby on GitHub](https://github.com/cucumber/cucumber-ruby)
- [cucumber/gherkin Parser on GitHub](https://github.com/cucumber/gherkin)
- [cucumber/godog on GitHub](https://github.com/cucumber/godog)
- [cucumber/vscode on GitHub](https://github.com/cucumber/vscode)
- [Reqnroll Official Website](https://reqnroll.net/)
- [Reqnroll on GitHub](https://github.com/reqnroll/Reqnroll)
- [Behat on GitHub](https://github.com/Behat/Behat)
- [Behave on GitHub](https://github.com/behave/behave)
- [pytest-bdd on GitHub](https://github.com/pytest-dev/pytest-bdd)
- [Karate on GitHub](https://github.com/karatelabs/karate)
- [Allure Report](https://allurereport.org/)
- [Allure Report on GitHub](https://github.com/allure-framework/allure2)
- [Serenity BDD on GitHub](https://github.com/serenity-bdd/serenity-core)
- [Serenity/JS Website](https://serenity-js.org/)
- [Serenity/JS on GitHub](https://github.com/serenity-js/serenity-js)
- [Cluecumber on GitHub](https://github.com/trivago/cluecumber)
- [cucumber-reporting on GitHub](https://github.com/damianszczepanik/cucumber-reporting)
- [Pickles on GitHub](https://github.com/picklesdoc/pickles)
- [gherkin-lint on GitHub](https://github.com/gherkin-lint/gherkin-lint)
- [gherlint on PyPI](https://pypi.org/project/gherlint/)
- [gherkin_lint on GitHub](https://github.com/funkwerk/gherkin_lint)
- [MegaLinter Gherkin Support](https://megalinter.io/latest/descriptors/gherkin/)
- [GherKing on GitHub](https://github.com/gherking/gherking)
- [prettier-plugin-gherkin on GitHub](https://github.com/mapado/prettier-plugin-gherkin)
- [vim-cucumber on GitHub](https://github.com/tpope/vim-cucumber/)
- [cucumber.el on GitHub](https://github.com/michaelklishin/cucumber.el)
- [tree-sitter-gherkin on GitHub](https://github.com/binhtran432k/tree-sitter-gherkin)
- [CWT-Cucumber on GitHub](https://github.com/ThoSe1990/cwt-cucumber)
- [Gherkinizer](https://gherkinizer.com/)
- [Workik Cucumber Generator](https://workik.com/cucumber-test-case-generator)
- [ReportPortal](https://reportportal.io/)
- [Xray Documentation](https://docs.getxray.app/)
- [AssertThat](https://www.assertthat.com/)
- [Testomat.io](https://testomat.io/)
- [TestQuality Gherkin](https://www.testquality.com/gherkin)
- [CucumberStudio on Atlassian Marketplace](https://marketplace.atlassian.com/apps/1212743/cucumberstudio-bdd-test-management)
- [JetBrains Cucumber Documentation](https://www.jetbrains.com/help/idea/cucumber-support.html)
- [Reqnroll for Visual Studio](https://marketplace.visualstudio.com/items?itemName=Reqnroll.ReqnrollForVisualStudio2022)
- [BDD & Cucumber Reality Check 2025](https://303software.com/behavior-driven-testing-a-cucumber-test-automation-framework)
- [Cucumber Testing in 2026 (BrowserStack)](https://www.browserstack.com/guide/learn-about-cucumber-testing-tool)
- [Behave Overview 2026 (TestAutomationTools.dev)](https://testautomationtools.dev/behave-overview-advantages-and-disadvantages/)
- [Python BDD Framework Comparison (Automation Panda)](https://automationpanda.com/2019/04/02/python-bdd-framework-comparison/)
- [SpecFlow is Dead, Long Live Reqnroll (Medium)](https://medium.com/@ish2hewage/specflow-is-dead-long-live-reqnroll-a-new-era-for-bdd-850047ded7ee)
- [Serenity BDD in 2026 (Medium)](https://medium.com/@andrei.oleynik/serenity-bdd-in-2026-a-framework-or-dependency-hell-015e3d16d33e)
