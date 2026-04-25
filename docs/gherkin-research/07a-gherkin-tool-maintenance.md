# Gherkin Ecosystem Tool Maintenance Status

> **Last updated:** 2026-04-15
>
> Data sourced from GitHub via `gh` CLI. Dates and counts are approximate
> snapshots as of the date above.

---

## Summary by Status

### Actively Maintained

Active development, regular commits, recent releases, responsive issue
handling.

- **Cucumber-JVM** -- Java BDD framework
- **Cucumber-JS** -- JavaScript BDD framework
- **Cucumber-Ruby** -- Ruby BDD framework
- **Reqnroll** -- .NET BDD framework (SpecFlow successor)
- **Karate** -- Java API test automation
- **Behat** -- PHP BDD framework
- **pytest-bdd** -- Python BDD for pytest
- **Cucumber Gherkin Parser** -- Official multi-language parser
- **Cucumber Messages** -- Message protocol
- **Cucumber Expressions** -- Step definition pattern matching
- **Allure Report** -- Multi-language test reporting
- **godog** -- Go BDD framework
- **Cucumber VS Code Extension** -- Official IDE extension
- **multiple-cucumber-html-reporter** -- HTML report generator
- **gplint** -- Gherkin/Pickle linter (JS, fork of gherkin-lint)
- **gherkin-lint-php** -- PHP Gherkin linter
- **behave** -- Python BDD framework

### Maintenance Mode

Occasional updates, low commit frequency, but still functional and not
abandoned.

- **Gherklin** -- TypeScript Gherkin linter
- **gherlint** -- Python Gherkin linter
- **radish** -- Python BDD framework
- **Cucumber Common** -- Umbrella repo (libraries moved to own repos)
- **cucumber-reporting** -- Java HTML reports for Cucumber
- **VSCucumberAutoComplete** -- VS Code extension (community)

### Stale

No meaningful commits or releases in 1+ years, but not officially
archived.

- **gherkin-lint** (gherkin-lint/gherkin-lint) -- JS linter, last
  release Dec 2023
- **Pickles** -- Living documentation generator, last release Nov 2022
- **cucumber-html-reporter** -- HTML reporter, last release Mar 2023
- **funkwerk/gherkin_lint** -- D-language linter, last release 2017

### Abandoned / End-of-Life

Archived, deprecated, or repo removed.

- **SpecFlow** -- .NET BDD framework, EOL Dec 31 2024, repos removed.
  Succeeded by Reqnroll.
- **Lettuce** -- Python BDD, last commit Feb 2020, effectively
  abandoned.

---

## Detailed Assessment

### Test Runners / BDD Frameworks

| Tool | Repository | Stars | Last Push | Latest Release | Open Issues | Status | Notes |
| ------ | ----------- | ------- | ----------- | --------------- | ------------- | -------- | ------- |
| Cucumber-JVM | [cucumber/cucumber-jvm](https://github.com/cucumber/cucumber-jvm) | 2,800 | 2026-04-15 | v7.34.3 (2026-03-04) | 51 | **Actively Maintained** | Core Cucumber project for Java/JVM |
| Cucumber-JS | [cucumber/cucumber-js](https://github.com/cucumber/cucumber-js) | 5,308 | 2026-04-14 | v12.8.1 (2026-04-14) | 42 | **Actively Maintained** | Very active; release same day as last push |
| Cucumber-Ruby | [cucumber/cucumber-ruby](https://github.com/cucumber/cucumber-ruby) | 5,212 | 2026-04-14 | v11.0.0 (2026-04-14) | 22 | **Actively Maintained** | Major version bump indicates active evolution |
| behave | [behave/behave](https://github.com/behave/behave) | 3,472 | 2026-04-14 | v1.3.3 (2025-09-04) | 75 | **Actively Maintained** | Commits active; release cadence ~6 months |
| pytest-bdd | [pytest-dev/pytest-bdd](https://github.com/pytest-dev/pytest-bdd) | 1,443 | 2026-04-13 | 8.1.0 (tag; no GH Release) | 61 | **Actively Maintained** | Uses tags not GH Releases; under pytest-dev org |
| SpecFlow | SpecFlowOSS/SpecFlow (removed) | ~2,200 | N/A | N/A | N/A | **Abandoned / EOL** | Org description: "will no longer be available after December 31, 2024." All repos removed. Succeeded by Reqnroll. |
| Reqnroll | [reqnroll/Reqnroll](https://github.com/reqnroll/Reqnroll) | 739 | 2026-04-14 | v3.3.4 (2026-03-23) | 21 | **Actively Maintained** | .NET port of Cucumber, based on SpecFlow codebase. Growing fast. |
| Behat | [Behat/Behat](https://github.com/Behat/Behat) | 3,965 | 2026-04-10 | v3.30.0 (2026-03-26) | 50 | **Actively Maintained** | Strong PHP BDD community |
| godog | [cucumber/godog](https://github.com/cucumber/godog) | 2,614 | 2026-04-14 | v0.15.1 (2025-07-19) | 66 | **Actively Maintained** | Commits active; release slightly behind commits |
| Karate | [karatelabs/karate](https://github.com/karatelabs/karate) | 8,836 | 2026-04-15 | v2.0.2 (2026-04-09) | 32 | **Actively Maintained** | Most-starred Gherkin-adjacent tool; very active |
| radish | [radish-bdd/radish](https://github.com/radish-bdd/radish) | 194 | 2026-02-24 | v0.18.4 (2026-02-24) | 11 | **Maintenance Mode** | Small community; occasional releases |
| Lettuce | [gabrielfalcao/lettuce](https://github.com/gabrielfalcao/lettuce) | 1,281 | 2020-12-29 | None (last tag v0.2.23) | 102 | **Abandoned** | Last commit Feb 2020; 102 open issues; no activity in 6 years |

### Parsers and Core Libraries

| Tool | Repository | Stars | Last Push | Latest Release | Open Issues | Status | Notes |
| ------ | ----------- | ------- | ----------- | --------------- | ------------- | -------- | ------- |
| Gherkin Parser | [cucumber/gherkin](https://github.com/cucumber/gherkin) | 319 | 2026-04-15 | v39.0.0 (2026-03-01) | 42 | **Actively Maintained** | Multi-language parser (Java, JS, Ruby, Go, Python, etc.) |
| Cucumber Messages | [cucumber/messages](https://github.com/cucumber/messages) | 35 | 2026-04-15 | v32.3.1 (2026-04-13) | 28 | **Actively Maintained** | JSON message protocol; very active |
| Cucumber Expressions | [cucumber/cucumber-expressions](https://github.com/cucumber/cucumber-expressions) | 195 | 2026-04-14 | v19.0.0 (2026-01-25) | 23 | **Actively Maintained** | Human-friendly step patterns |
| Cucumber Common | [cucumber/common](https://github.com/cucumber/common) | 3,350 | 2026-03-11 | gherkin/go/v24.1.0 (2022-10-10) | 45 | **Maintenance Mode** | Umbrella/meta repo; libraries have moved to individual repos. Last release is stale but repo still used for cross-cutting issues. |

### Linting Tools

| Tool | Repository | Stars | Last Push | Latest Release | Open Issues | Status | Notes |
| ------ | ----------- | ------- | ----------- | --------------- | ------------- | -------- | ------- |
| gherkin-lint | [gherkin-lint/gherkin-lint](https://github.com/gherkin-lint/gherkin-lint) | 196 | 2024-08-19 | v4.2.4 (2023-12-20) | 57 | **Stale** | JS linter; no releases in 2+ years. Was originally vsiakka/gherkin-lint. |
| gplint | [gplint/gplint](https://github.com/gplint/gplint) | 12 | 2026-04-13 | v2.5.2 (2026-04-06) | 7 | **Actively Maintained** | Fork of gherkin-lint; actively developed replacement |
| Gherklin | [cjmarkham/Gherklin](https://github.com/cjmarkham/Gherklin) | 18 | 2026-02-23 | 1.0.14 (2026-02-18) | 1 | **Maintenance Mode** | Modern TypeScript/ESM linter; small but active |
| gherlint | [gherlint/gherlint](https://github.com/gherlint/gherlint) | 7 | 2026-04-10 | v2.0.0 (2025-12-15) | 8 | **Maintenance Mode** | Python linter; small community |
| gherkin-lint-php | [dantleech/gherkin-lint-php](https://github.com/dantleech/gherkin-lint-php) | 46 | 2026-03-30 | 0.2.4 (2026-03-30) | 4 | **Actively Maintained** | PHP linter; actively developed |
| funkwerk/gherkin_lint | [funkwerk/gherkin_lint](https://github.com/funkwerk/gherkin_lint) | 37 | 2019-05-09 | 1.2.2 (2017-12-03) | 3 | **Stale** | D-language linter; no activity since 2019 |

### IDE Extensions

| Tool | Repository | Stars | Last Push | Latest Release | Open Issues | Status | Notes |
| ------ | ----------- | ------- | ----------- | --------------- | ------------- | -------- | ------- |
| Cucumber for VS Code (Official) | [cucumber/vscode](https://github.com/cucumber/vscode) | 84 | 2026-04-15 | v1.11.0 (2025-05-18) | 49 | **Actively Maintained** | Official extension; commits active, release cadence ~yearly |
| VSCucumberAutoComplete | [alexkrechik/VSCucumberAutoComplete](https://github.com/alexkrechik/VSCucumberAutoComplete) | 359 | 2026-03-27 | None (no GH Releases) | 118 | **Maintenance Mode** | "Cucumber (Gherkin) Full Support" extension; community-driven. 118 open issues suggests limited maintainer bandwidth. Still receiving commits. |

### Reporting Tools

| Tool | Repository | Stars | Last Push | Latest Release | Open Issues | Status | Notes |
| ------ | ----------- | ------- | ----------- | --------------- | ------------- | -------- | ------- |
| Allure Report | [allure-framework/allure2](https://github.com/allure-framework/allure2) | 5,340 | 2026-04-15 | 2.39.0 (2026-04-09) | 102 | **Actively Maintained** | Industry-standard reporting; very active development |
| multiple-cucumber-html-reporter | [WasiqB/multiple-cucumber-html-reporter](https://github.com/WasiqB/multiple-cucumber-html-reporter) | 273 | 2026-04-15 | v3.10.0 (2026-02-12) | 43 | **Actively Maintained** | Active development and releases |
| cucumber-reporting (Java) | [damianszczepanik/cucumber-reporting](https://github.com/damianszczepanik/cucumber-reporting) | 567 | 2026-04-12 | 5.11.0 (tag; no GH Release) | 51 | **Maintenance Mode** | Commits active, but uses tags not GH Releases |
| Pickles | [picklesdoc/pickles](https://github.com/picklesdoc/pickles) | 479 | 2025-03-18 | v4.0.3 (2022-11-28) | 17 | **Stale** | Living doc generator; no release in 3+ years |
| cucumber-html-reporter | [gkushang/cucumber-html-reporter](https://github.com/gkushang/cucumber-html-reporter) | 237 | 2024-11-20 | 6.0.0 (2023-03-03) | 88 | **Stale** | 88 open issues; no release in 3+ years |

---

## Key Takeaways

1. **The Cucumber core ecosystem is healthy.** All official Cucumber
   repositories (JVM, JS, Ruby, Gherkin parser, Messages, Expressions,
   godog, VS Code extension) are actively maintained with recent commits
   and releases.

2. **SpecFlow is dead; Reqnroll is its successor.** The SpecFlowOSS
   GitHub organization was archived on 2025-01-13 and all public repos
   were removed. Reqnroll is the community fork, based on the SpecFlow
   codebase, and is actively maintained with growing adoption.

3. **Python BDD has a fragmented landscape.** behave and pytest-bdd are
   both actively maintained. radish is in maintenance mode with a small
   community. Lettuce is abandoned (last commit in 2020).

4. **Karate is the most-starred tool** in the ecosystem at 8,836 stars,
   actively maintained, and has broadened beyond Gherkin into general API
   testing.

5. **Linting is evolving.** The original gherkin-lint (JS) is stale, but
   its fork **gplint** is actively maintained. Newer entrants include
   Gherklin (TypeScript), gherlint (Python), and gherkin-lint-php (PHP).

6. **Allure dominates reporting.** It is the most actively maintained and
   widely adopted reporting framework. The older cucumber-html-reporter
   and Pickles projects are stale. multiple-cucumber-html-reporter is a
   solid active alternative for JS/Node ecosystems.

7. **IDE support is consolidating.** The official Cucumber VS Code
   extension is the recommended choice going forward. The older
   community extension VSCucumberAutoComplete has more stars but a large
   backlog of open issues and less structured maintenance.
