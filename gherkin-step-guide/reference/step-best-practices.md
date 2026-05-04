# Step Definition Best Practices — Detailed Reference

This document provides comprehensive guidance for writing high-quality
Gherkin step definitions. Consult this when creating or refactoring step
implementation code.

---

## Parameterize Similar Steps

The single most impactful practice for step definition maintainability.
When multiple steps differ only by a noun, value, or label, consolidate
them into one parameterized step definition.

### Why It Matters

Every distinct step definition is code that must be maintained, tested, and
kept consistent. Three steps that do the same thing with different nouns
means three places to update when the underlying behavior changes. One
parameterized step means one.

### Before and After

**Before — three near-identical step definitions (Python/Behave):**

```python
@given('the user enters their email')
def step_enter_email(context):
    context.form.fill_field("email", "test@example.com")

@given('the user enters their phone number')
def step_enter_phone(context):
    context.form.fill_field("phone", "555-0100")

@given('the user enters their mailing address')
def step_enter_address(context):
    context.form.fill_field("address", "123 Main St")
```

**After — one parameterized step definition:**

```python
@given('the user enters their "{field}"')
def step_enter_field(context, field):
    defaults = {
        "email": "test@example.com",
        "phone number": "555-0100",
        "mailing address": "123 Main St",
    }
    context.form.fill_field(field, defaults.get(field, "test-value"))
```

**Before — three near-identical step definitions (Java/Cucumber):**

```java
@Given("the order status is pending")
public void orderStatusPending() {
    order.setStatus(Status.PENDING);
}

@Given("the order status is shipped")
public void orderStatusShipped() {
    order.setStatus(Status.SHIPPED);
}

@Given("the order status is delivered")
public void orderStatusDelivered() {
    order.setStatus(Status.DELIVERED);
}
```

**After — one parameterized step definition:**

```java
@Given("the order status is {word}")
public void orderStatusIs(String status) {
    order.setStatus(Status.valueOf(status.toUpperCase()));
}
```

**Before — three near-identical step definitions (Go/Godog):**

```go
func theOrderStatusIsPending(ctx context.Context) (context.Context, error) {
    return setOrderStatus(ctx, "pending")
}

func theOrderStatusIsShipped(ctx context.Context) (context.Context, error) {
    return setOrderStatus(ctx, "shipped")
}

func theOrderStatusIsDelivered(ctx context.Context) (context.Context, error) {
    return setOrderStatus(ctx, "delivered")
}
```

**After — one parameterized step definition:**

```go
func theOrderStatusIs(ctx context.Context, status string) (context.Context, error) {
    order := orderFromContext(ctx)
    order.Status = strings.ToUpper(status)
    return ctx, nil
}

// Registered as: ctx.Given(`^the order status is (\w+)$`, theOrderStatusIs)
```

### When NOT to Parameterize

Keep steps separate when the *behavior* differs, not just the data:

```python
# These look similar but do fundamentally different things — keep separate
@when('the user uploads a profile photo')
def step_upload_photo(context):
    context.uploader.upload_image(context.test_image)
    context.uploader.crop_to_square()

@when('the user enters their "{field}"')
def step_enter_field(context, field):
    context.form.fill_field(field, context.test_data[field])
```

### Recognizing Parameterization Opportunities

Look for these signals:

- Multiple step definitions with the same verb and structure
- Steps that differ only in a quoted value or a trailing noun
- Copy-pasted step bodies with one or two values changed
- A step file where many definitions call the same helper with different
  arguments

---

## Keep Step Definitions Declarative

Step definitions are translators — they convert scenario language into
code. The step definition itself should be a thin layer that delegates to
a support/helper module where the real implementation lives.

### Why It Matters

When implementation details live in step definitions, changes to the
system under test force changes across many step files. When steps
delegate to a support layer, changes are isolated to that layer.

### The Three-Layer Model

```text
Feature file (Gherkin)     → What the system does (business language)
Step definitions           → Wiring layer (maps words to code)
Support/helper modules     → How to interact with the system (implementation)
```

### Before and After

**Before — implementation details in the step (JS/Cucumber):**

```javascript
When('the customer places an order', async function () {
  await this.page.goto('/cart');
  await this.page.click('[data-testid="checkout-btn"]');
  await this.page.fill('#card-number', '4111111111111111');
  await this.page.fill('#expiry', '12/25');
  await this.page.fill('#cvv', '123');
  await this.page.click('#submit-order');
  await this.page.waitForSelector('.order-confirmation');
  this.orderId = await this.page.textContent('.order-id');
});
```

**After — step delegates to support layer:**

```javascript
When('the customer places an order', async function () {
  this.orderId = await this.checkout.placeOrderWithTestPayment();
});
```

The checkout page object handles the DOM interaction, selectors, and
payment details. If the checkout flow changes, only the page object needs
updating — every scenario that places an order continues to work.

**Go/Godog — same principle applies:**

```go
// Before — HTTP details in the step
func theCustomerPlacesAnOrder(ctx context.Context) (context.Context, error) {
    body, _ := json.Marshal(map[string]any{"items": cartFromCtx(ctx).Items})
    resp, err := http.Post("http://localhost:8080/orders", "application/json",
        bytes.NewReader(body))
    if err != nil { return ctx, err }
    defer resp.Body.Close()
    var order Order
    json.NewDecoder(resp.Body).Decode(&order)
    return context.WithValue(ctx, OrderKey{}, &order), nil
}

// After — step delegates to support layer
func theCustomerPlacesAnOrder(ctx context.Context) (context.Context, error) {
    order, err := support.PlaceOrder(cartFromCtx(ctx))
    if err != nil { return ctx, err }
    return context.WithValue(ctx, OrderKey{}, order), nil
}
```

### How Deep Should the Delegation Go?

A step definition should typically be 1–5 lines of code that call into
support modules. If you are writing loops, conditionals, or direct
framework API calls (Selenium selectors, HTTP requests, SQL queries)
inside a step definition, push that logic down.

---

## Step Reuse Across Features

In most BDD frameworks, step definitions are globally scoped — a step
defined in one file is available to scenarios in any `.feature` file.
Write steps to take advantage of this.

### Guidelines

- **Use domain language, not feature-specific language.** A step like
  `Given a registered user` is reusable. A step like `Given the user from
  the login test` is not.
- **Avoid hard-coded test data in step text.** Pass values as parameters
  instead of embedding them in the step pattern.
- **Keep Given steps composable.** Small, focused Given steps can be
  combined in different scenarios. One large Given that sets up an entire
  test fixture is hard to reuse.

### Example: Composable vs. Monolithic

```gherkin
# Reusable — each step can be mixed into other scenarios
Given a registered user with a "premium" subscription
And the user has 3 items in their cart
And the store is running a "20% off" promotion

# Not reusable — tightly coupled to one scenario
Given the premium user checkout test is set up
```

---

## Parameter Types

### Strings

The most common parameter type. Use quotes in the step text to make
parameters visually distinct.

```gherkin
When the user searches for "wireless headphones"
Then the page title should be "Search Results"
```

### Integers and Floats

Use for counts, amounts, thresholds.

```gherkin
Given the cart contains 3 items
Then the total should be 49.99
```

### Custom Parameter Types

Most frameworks support defining custom parameter types that convert
step text into domain objects. Use them to keep step definitions clean
and catch invalid values early.

**Cucumber (Java) example:**

```java
@ParameterType("pending|shipped|delivered|cancelled")
public OrderStatus orderStatus(String value) {
    return OrderStatus.valueOf(value.toUpperCase());
}

@Given("the order status is {orderStatus}")
public void orderHasStatus(OrderStatus status) {
    testOrder.setStatus(status);
}
```

**Behave (Python) — use `register_type`:**

```python
from behave import register_type
import parse

@parse.with_pattern(r"pending|shipped|delivered|cancelled")
def parse_order_status(text):
    return OrderStatus[text.upper()]

register_type(OrderStatus=parse_order_status)

@given('the order status is {status:OrderStatus}')
def step_order_status(context, status):
    context.order.status = status
```

### Data Tables

Use when a step needs structured input — a list of items, a set of
properties, or multiple entities.

```gherkin
Given the following products exist:
  | name         | price | category    |
  | Headphones   | 79.99 | Electronics |
  | Running Shoe | 129.99| Footwear    |
```

The step definition receives the table as a framework-specific object.
Convert it to domain objects in the step and pass them to the support
layer — do not iterate over table rows to drive UI interactions directly.

### Doc Strings

Use for multi-line text — error messages, JSON payloads, email content.

```gherkin
Then the API response should be:
  """json
  {
    "status": "created",
    "id": 42
  }
  """
```

---

## Hooks vs. Step Logic

Hooks run automatically before or after scenarios, features, or
individual steps. They handle infrastructure concerns that should not
appear in the scenario narrative.

### When to Use Hooks

- **Browser or driver setup/teardown** — open before each scenario, close
  after.
- **Database transactions** — begin before, rollback after, so each
  scenario runs in isolation.
- **Screenshot on failure** — capture the screen when a scenario fails.
- **Logging** — record scenario start/end for debugging.
- **Tagging-based setup** — use tags to conditionally run hooks
  (e.g., `@requires-admin` triggers admin user creation).

### When NOT to Use Hooks

- **Scenario-specific setup** that the reader needs to see. If the
  precondition matters for understanding the scenario, it belongs in a
  `Given`, not hidden in a hook.
- **Assertions.** Hooks should not verify outcomes — that is what `Then`
  steps are for.
- **Complex conditional logic.** If a hook has many branches based on
  tags or scenario names, the logic probably belongs in step definitions
  or the support layer.

### Hook Example (Python/Behave)

```python
# environment.py
def before_scenario(context, scenario):
    context.db = Database.connect()
    context.db.begin_transaction()

def after_scenario(context, scenario):
    context.db.rollback()
    context.db.close()
```

### Hook Example (JS/Cucumber)

```javascript
const { Before, After } = require('@cucumber/cucumber');

Before(async function () {
  this.browser = await puppeteer.launch();
  this.page = await this.browser.newPage();
});

After(async function (scenario) {
  if (scenario.result.status === 'FAILED') {
    await this.page.screenshot({ path: `screenshots/${scenario.pickle.name}.png` });
  }
  await this.browser.close();
});
```

### Hook Example (Go/Godog)

```go
func InitializeScenario(ctx *godog.ScenarioContext) {
    ctx.Before(func(ctx context.Context, sc *godog.Scenario) (context.Context, error) {
        db := support.ConnectDB()
        db.BeginTransaction()
        return context.WithValue(ctx, support.DBKey{}, db), nil
    })

    ctx.After(func(ctx context.Context, sc *godog.Scenario, err error) (context.Context, error) {
        db := ctx.Value(support.DBKey{}).(*support.DB)
        db.Rollback()
        db.Close()
        return ctx, nil
    })

    // Step registrations...
}
```

---

## Step Definition Naming Conventions

Step definitions are identified by their pattern (regex or expression),
but the function/method name still matters for code readability and
debugging.

### Guidelines

- Name the function after the behavior it implements, not the step text
  verbatim.
- Use a consistent prefix: `step_`, or the Given/When/Then keyword.
- Keep names short — the step pattern is the documentation.

```python
# Good function names
@given('a registered user with a "{role}" role')
def step_user_with_role(context, role): ...

@when('the user submits the form')
def step_submit_form(context): ...

@then('the confirmation email should be sent')
def step_verify_confirmation_email(context): ...
```

---

## Stub Steps (Pending Implementation)

When creating step files for steps that are not yet implemented — for
example, to satisfy the audit script or to scaffold a new feature —
always mark them as pending using the framework's built-in mechanism.
Never write a stub that silently passes (e.g., an empty function body
or `assert True`), because it hides missing implementation and lets
scenarios pass without actually testing anything.

### Framework Pending Markers

| Framework | Pending Marker |
| :--- | :--- |
| **Behave** (Python) | Raise `NotImplementedError` — Behave does not have a built-in pending status, so raising this error clearly signals the step needs implementation and fails the scenario. |
| **Cucumber** (Java) | `throw new io.cucumber.java.PendingException()` |
| **Cucumber** (JS/TS) | `return 'pending'` |
| **Cucumber** (Ruby) | `pending` (built-in method) |
| **SpecFlow** (C#) | `ScenarioContext.Current.Pending()` |
| **Godog** (Go) | `return godog.ErrPending` |
| **pytest-bdd** (Python) | `pytest.skip("Not yet implemented")` |

### Examples

```python
# features/steps/when/the_customer_checks_out.py (Behave)
from behave import when

@when('the customer checks out')
def step_impl(context):
    raise NotImplementedError("Step not yet implemented")
```

```java
// Cucumber (Java)
@When("the customer checks out")
public void theCustomerChecksOut() {
    throw new io.cucumber.java.PendingException();
}
```

```javascript
// Cucumber (JS)
When('the customer checks out', function () {
  return 'pending';
});
```

```go
// Godog (Go)
func theCustomerChecksOut(ctx context.Context) error {
    return godog.ErrPending
}
```

These markers cause the scenario to fail or be reported as pending,
making it obvious in test output that implementation is needed. They
are easy to find with a simple search across the codebase.

---

## Quality Checklist

Before considering step definitions complete, verify:

- [ ] Each step definition lives in its own file, named after the step
      in snake_case, in the correct keyword directory (`given/`, `when/`,
      `then/`)
- [ ] No two step definitions have patterns that differ only by a
      noun/value (consolidate them)
- [ ] Every step definition delegates to a support layer (no raw
      selectors, SQL, or HTTP calls in step bodies)
- [ ] Given steps set up state; When steps perform actions; Then steps
      assert outcomes — no mixing
- [ ] Parameters use appropriate types (strings, integers, custom types)
      not raw regex capture groups where avoidable
- [ ] Shared state passes through the context/world object, not
      module-level variables
- [ ] Hooks handle only infrastructure; scenario-visible setup uses Givens
- [ ] Stub steps use the framework's pending marker, not empty bodies
      or `assert True`
- [ ] The audit script (`scripts/audit_steps.py`) reports no unused step
      files and no missing step definitions
