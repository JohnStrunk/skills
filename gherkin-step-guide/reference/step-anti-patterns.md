# Step Definition Anti-Patterns — Detailed Reference

This document catalogs common step definition mistakes. Each anti-pattern
includes an explanation of the problem and a concrete before/after fix.
Consult this when reviewing or refactoring step definitions.

---

## Near-Duplicate Steps

**Problem:** Multiple step definitions with nearly identical patterns and
bodies, differing only by a noun, value, or minor wording. Each duplicate
adds maintenance cost and increases the chance of inconsistency when one is
updated and the others are not.

### How to Spot It

- Two or more step definitions whose patterns share the same structure
- Step bodies that are copy-pasted with one or two values changed
- A step file where several definitions call the same method with
  different hard-coded arguments

### Before

```python
@then('the success notification should be displayed')
def step_success_notification(context):
    assert context.page.notification_visible("success")

@then('the error notification should be displayed')
def step_error_notification(context):
    assert context.page.notification_visible("error")

@then('the warning notification should be displayed')
def step_warning_notification(context):
    assert context.page.notification_visible("warning")
```

### After

```python
@then('the {notification_type} notification should be displayed')
def step_notification_displayed(context, notification_type):
    assert context.page.notification_visible(notification_type)
```

One definition replaces three. Adding "info" notifications in the future
requires zero step definition changes.

---

## Multiple Steps Per File

**Problem:** A file containing more than one step definition. Even a small
multi-step file obscures which steps exist and makes it harder to detect
unused code. With one step per file, an unused step is an unused file —
immediately visible in a directory listing or audit.

### How to Spot It

- Any step file with more than one `@given`, `@when`, or `@then` decorator
- Step files named after a domain rather than a step
  (e.g., `authentication_steps.py` instead of `the_user_logs_in.py`)

### Before

```text
steps/
  all_steps.py        ← 200+ step definitions covering everything
```

### After

```text
features/steps/
  given/
    a_registered_user.py
    the_shopping_cart_is_empty.py
  when/
    the_user_logs_in.py
    the_customer_adds_to_the_cart.py
  then/
    the_dashboard_should_appear.py
    the_cart_total_should_be.py
```

Each file contains exactly one step. Finding a step means scanning
filenames. Adding a step means adding a file. Removing a step means
deleting a file.

---

## Implementation Leakage

**Problem:** Step definitions contain raw implementation details — CSS
selectors, SQL queries, HTTP calls, XPath expressions — instead of
delegating to a support layer. This couples every step to the current
implementation and breaks steps whenever the UI, API, or database
changes.

### How to Spot It

- Selenium/Playwright selectors in step bodies
- Raw SQL or ORM queries in step bodies
- Direct HTTP request construction (`fetch`, `requests.post`, etc.)
- Framework-specific API calls (Spring beans, Rails models)

### Before (JS/Cucumber)

```javascript
Given('a product named {string} exists', async function (name) {
  await this.page.goto('/admin/products/new');
  await this.page.fill('#product-name', name);
  await this.page.fill('#product-price', '9.99');
  await this.page.selectOption('#product-category', 'General');
  await this.page.click('button[type="submit"]');
  await this.page.waitForSelector('.flash-success');
});
```

### After

```javascript
Given('a product named {string} exists', async function (name) {
  await this.productHelper.createProduct({ name, price: 9.99 });
});
```

The helper handles the mechanics. If product creation moves from a UI form
to an API call, only the helper changes.

---

## Overloaded Steps

**Problem:** A single step definition does too much — it sets up state,
performs an action, and asserts an outcome, all in one. This makes steps
unreusable and violates the Given/When/Then separation.

### How to Spot It

- A `Given` step that also clicks buttons or submits forms
- A `When` step that also contains assertions
- A step body longer than ~10 lines
- A step that calls both setup methods and assertion methods

### Before

```python
@when('the user logs in and sees the dashboard')
def step_login_and_dashboard(context):
    context.login_page.enter_credentials("alice", "password")
    context.login_page.submit()
    assert context.dashboard.is_displayed()
    assert context.dashboard.welcome_message() == "Welcome, Alice"
```

### After

```python
@when('the user logs in with valid credentials')
def step_login(context):
    context.login_page.login_as("alice", "password")

@then('the dashboard should be displayed')
def step_dashboard_displayed(context):
    assert context.dashboard.is_displayed()

@then('the welcome message should greet the user')
def step_welcome_message(context):
    assert "Welcome" in context.dashboard.welcome_message()
```

Each step has one job. The login step is now reusable in any scenario that
needs authentication.

---

## Tight Coupling Between Steps

**Problem:** Steps depend on other steps having run first, sharing state
through implicit side effects rather than through the framework's context
or world object. This creates hidden dependencies and makes steps fail
when reordered or used in new scenarios.

### How to Spot It

- Steps that read module-level variables set by other steps
- Steps that assume a previous step set up specific page state or
  navigation
- Steps that break when moved to a different scenario
- A step comment saying "must run after step X"

### Before

```python
# Module-level variable shared between steps — fragile
_last_created_order = None

@when('the customer places an order')
def step_place_order(context):
    global _last_created_order
    _last_created_order = context.checkout.place_order()

@then('the order confirmation should be sent')
def step_order_confirmation(context):
    # Depends on _last_created_order being set by the previous step
    assert context.email.was_sent_for(_last_created_order.id)
```

### After

```python
@when('the customer places an order')
def step_place_order(context):
    context.current_order = context.checkout.place_order()

@then('the order confirmation should be sent')
def step_order_confirmation(context):
    assert context.email.was_sent_for(context.current_order.id)
```

The context/world object is the framework's designated way to share state
between steps. Module-level globals bypass this and create hidden coupling.

In Go/Godog, the same anti-pattern appears as package-level variables
instead of using `context.Context`:

```go
// Bad — package-level variable
var lastOrder *Order

func theCustomerPlacesAnOrder(ctx context.Context) error {
    lastOrder = placeOrder(cartFromCtx(ctx))
    return nil
}

// Good — context threading
func theCustomerPlacesAnOrder(ctx context.Context) (context.Context, error) {
    order := placeOrder(cartFromCtx(ctx))
    return context.WithValue(ctx, OrderKey{}, order), nil
}
```

---

## Regex Overengineering

**Problem:** Step patterns use complex regular expressions when simpler
alternatives (Cucumber Expressions, parse patterns) would do the same job
more readably. Overly complex regex patterns are hard to understand, error-
prone, and hostile to contributors.

### How to Spot It

- Regexes with multiple lookaheads, lookbehinds, or nested groups
- Patterns that try to match many different phrasings in a single regex
- Developers unable to tell what step text a pattern matches

### Before

```ruby
Given(/^(?:the |a )?(?:registered |existing )?user (?:named |called )?["']?(\w+)["']?(?: exists)?$/i) do |name|
  create_user(name)
end
```

### After

```ruby
Given('a registered user named {string}') do |name|
  create_user(name)
end
```

If you need to support multiple phrasings, write multiple simple step
definitions that call the same helper — or standardize on one phrasing
across your feature files. Readable step patterns are more valuable than
flexible ones.

---

## Assertion-Free Then Steps

**Problem:** A `Then` step performs actions or sets state but never asserts
anything. This means the scenario can pass even when the expected behavior
does not occur.

### How to Spot It

- `Then` steps with no assertion or expectation calls
- `Then` steps that only log, print, or navigate
- Scenarios that never fail (always green regardless of behavior)

### Before

```python
@then('the report should be generated')
def step_report_generated(context):
    context.reports_page.open()
    context.reports_page.click_latest()
    # No assertion — this step always passes
```

### After

```python
@then('the report should be generated')
def step_report_generated(context):
    report = context.reports.latest()
    assert report is not None, "Expected a report to be generated"
    assert report.status == "complete"
```

---

## Silent Stub Steps

**Problem:** Step definition files are created as placeholders but contain
empty bodies or trivially-passing logic (`pass`, `assert True`, `return`).
These stubs satisfy the audit script and compile without errors, but they
let scenarios pass without testing anything — hiding the fact that
implementation is missing.

### How to Spot It

- Step bodies that are empty or contain only `pass`
- `Then` steps with `assert True` or no assertion at all
- Steps whose body is a comment like `# TODO: implement`
- Scenarios that pass unexpectedly early in development

### Before

```python
@when('the customer checks out')
def step_impl(context):
    pass  # Scenario passes silently — checkout is never tested
```

```javascript
When('the customer checks out', function () {
  // nothing here — scenario passes
});
```

### After

```python
@when('the customer checks out')
def step_impl(context):
    raise NotImplementedError("Step not yet implemented")
```

```javascript
When('the customer checks out', function () {
  return 'pending';
});
```

```go
func theCustomerChecksOut(ctx context.Context) error {
    return godog.ErrPending
}
```

Every framework has a pending/not-implemented marker that causes the
scenario to fail or be flagged. Use it. See the Stub Steps section in
`step-best-practices.md` for the full list of markers by framework.

---

## Hard-Coded Test Data in Step Patterns

**Problem:** Step patterns embed specific test data values, making the step
usable only for that exact case.

### How to Spot It

- Step patterns that mention specific names, IDs, or values
- Steps that work for one scenario but cannot be reused with different data

### Before

```java
@Given("Alice has a premium account")
public void aliceHasPremiumAccount() {
    createUser("Alice", AccountType.PREMIUM);
}

@Given("Bob has a basic account")
public void bobHasBasicAccount() {
    createUser("Bob", AccountType.BASIC);
}
```

### After

```java
@Given("{string} has a {word} account")
public void userHasAccount(String name, String accountType) {
    createUser(name, AccountType.valueOf(accountType.toUpperCase()));
}
```

---

## Quality Checklist

Use this checklist when reviewing step definitions:

1. **One step per file** — Each file contains exactly one step definition,
   named after the step in snake_case, placed in the correct keyword
   directory (`given/`, `when/`, `then/`).
2. **No near-duplicates** — Every parameterization opportunity has been
   taken.
3. **Thin step bodies** — Steps delegate to support modules; no raw
   selectors, queries, or API calls.
4. **Correct responsibility** — Given = state, When = action, Then =
   assertion. No mixing.
5. **No hidden coupling** — State passes through context/world, not
   globals or side effects.
6. **Readable patterns** — Simple expressions preferred over complex
   regex.
7. **Assertions present** — Every Then step asserts something.
8. **No hard-coded data** — Parameters used for variable values.
9. **No silent stubs** — Placeholder steps use the framework's pending
   marker, not empty bodies or `assert True`.
10. **All step files used** — The audit script reports no unused step files.
