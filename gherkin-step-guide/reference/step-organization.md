# Step File Organization — Detailed Reference

This document covers how to structure step definition files, support
layers, and shared state management. Consult this when setting up a new
BDD project or reorganizing an existing one.

---

## Core Principle: One Step Per File

Every step definition lives in its own file. This makes each step
independently discoverable, auditable, and version-controlled:

- An unused step is an unused file — easy to spot and delete.
- Adding a step means adding a file — no merge conflicts in shared files.
- Each file has a single responsibility — open it, see one step, done.

---

## Directory Structure

Step files are organized into directories by their Gherkin keyword type.

### Typical Layout

```text
project/
├── features/                          ← .feature files
│   ├── authentication.feature
│   ├── shopping_cart.feature
│   └── checkout.feature
├── features/steps/                    ← Step definitions
│   ├── given/                         ← All Given step files
│   │   ├── a_registered_user.py
│   │   ├── the_shopping_cart_is_empty.py
│   │   └── the_shopping_cart_contains_items.py
│   ├── when/                          ← All When step files
│   │   ├── the_customer_adds_to_the_cart.py
│   │   ├── the_customer_removes_from_the_cart.py
│   │   └── the_user_logs_in.py
│   └── then/                          ← All Then step files
│       ├── the_cart_should_display_items.py
│       ├── the_cart_total_should_be.py
│       └── the_dashboard_should_appear.py
├── support/                           ← Helper/support modules
│   ├── pages/                         ← Page objects (UI testing)
│   │   ├── login_page.py
│   │   └── cart_page.py
│   ├── api_client.py
│   ├── database.py
│   └── factories.py
└── environment.py                     ← Hooks
```

### File Naming Convention

Derive the filename from the step pattern:

1. Take the step text (e.g., `the customer adds "{product}" to the cart`)
2. Remove quotes and parameter placeholders → `the customer adds to the cart`
3. Convert to snake_case → `the_customer_adds_to_the_cart`
4. Add the framework's file extension → `the_customer_adds_to_the_cart.py`

| Step Pattern | Filename |
| :--- | :--- |
| `a registered user named "{name}"` | `a_registered_user_named.py` |
| `the shopping cart is empty` | `the_shopping_cart_is_empty.py` |
| `the cart should display {count} items` | `the_cart_should_display_items.py` |
| `the user enters "{value}" into the "{field}" field` | `the_user_enters_into_the_field.py` |

### What Goes in Each File

A step file contains exactly one step definition and any imports it needs.
Nothing else.

```python
# features/steps/given/the_shopping_cart_is_empty.py
from behave import given
from support.cart_helper import ShoppingCart

@given("the shopping cart is empty")
def step_impl(context):
    context.cart = ShoppingCart()
```

```python
# features/steps/when/the_customer_adds_to_the_cart.py
from behave import when

@when('the customer adds "{product_name}" to the cart')
def step_impl(context, product_name):
    context.cart.add_item(product_name)
```

### Framework-Specific Conventions

| Framework | Steps Root | Given | When | Then |
| :--- | :--- | :--- | :--- | :--- |
| **Behave** | `features/steps/` | `given/` | `when/` | `then/` |
| **pytest-bdd** | `tests/step_defs/` | `given/` | `when/` | `then/` |
| **Cucumber (JS)** | `features/step_definitions/` | `given/` | `when/` | `then/` |
| **Cucumber (Java)** | `src/test/java/steps/` | `given/` | `when/` | `then/` |
| **Cucumber (Ruby)** | `features/step_definitions/` | `given/` | `when/` | `then/` |
| **SpecFlow** | `StepDefinitions/` | `Given/` | `When/` | `Then/` |
| **Godog** (Go) | `features/steps/` | `given/` | `when/` | `then/` |

For Python frameworks (Behave, pytest-bdd), Behave only loads step files
from `features/steps/` by default — it does not recurse into
subdirectories. To enable discovery of steps in `given/`, `when/`, and
`then/` subdirectories, add a `features/steps/__init__.py` that
auto-imports them:

```python
# features/steps/__init__.py
import glob
import importlib.util
import os

_steps_dir = os.path.dirname(__file__)
for _subdir in ("given", "when", "then"):
    _subdir_path = os.path.join(_steps_dir, _subdir)
    if not os.path.isdir(_subdir_path):
        continue
    for _filepath in sorted(glob.glob(os.path.join(_subdir_path, "*.py"))):
        _basename = os.path.basename(_filepath)
        if _basename.startswith("_"):
            continue
        _spec = importlib.util.spec_from_file_location(_basename[:-3], _filepath)
        _mod = importlib.util.module_from_spec(_spec)
        _spec.loader.exec_module(_mod)
```

Also include an empty `__init__.py` in each keyword subdirectory.

### Godog (Go) — One Step Per File

Godog (`github.com/cucumber/godog`) is the official Cucumber framework
for Go. Step definitions live in `*_test.go` files and are registered
via an `InitializeScenario` function. This requires a slightly different
approach to one-step-per-file than decorator-based frameworks.

**Directory layout:**

```text
project/
├── features/                          ← .feature files
│   └── shopping_cart.feature
├── features/steps/                    ← Step definition files
│   ├── given/
│   │   ├── the_shopping_cart_is_empty_test.go
│   │   └── the_shopping_cart_contains_items_test.go
│   ├── when/
│   │   └── the_customer_adds_to_the_cart_test.go
│   └── then/
│       ├── the_cart_should_display_items_test.go
│       └── the_cart_total_should_be_test.go
├── support/                           ← Helper modules
│   └── cart.go
├── steps_test.go                      ← InitializeScenario (registers all steps)
├── go.mod
└── go.sum
```

Each step file defines one exported step function. A central
`steps_test.go` registers them all:

```go
// features/steps/given/the_shopping_cart_is_empty_test.go
package steps

import (
    "context"
    "myproject/support"
)

func TheShoppingCartIsEmpty(ctx context.Context) (context.Context, error) {
    cart := support.NewCart()
    return context.WithValue(ctx, support.CartKey{}, cart), nil
}
```

```go
// steps_test.go
package myproject_test

import (
    "testing"

    "github.com/cucumber/godog"

    "myproject/features/steps/given"
    "myproject/features/steps/when"
    "myproject/features/steps/then"
)

func InitializeScenario(ctx *godog.ScenarioContext) {
    ctx.Given(`^the shopping cart is empty$`, given.TheShoppingCartIsEmpty)
    ctx.When(`^the customer adds "([^"]*)" to the cart$`, when.TheCustomerAddsToTheCart)
    ctx.Then(`^the cart should display (\d+) items?$`, then.TheCartShouldDisplayItems)
}

func TestFeatures(t *testing.T) {
    suite := godog.TestSuite{
        ScenarioInitializer: InitializeScenario,
        Options: &godog.Options{
            Format:   "pretty",
            Paths:    []string{"features"},
            TestingT: t,
        },
    }
    if suite.Run() != 0 {
        t.Fatal("feature tests failed")
    }
}
```

Adding a new step means creating a new `*_test.go` file and adding one
registration line to `InitializeScenario`.

**State management in Go:** Godog uses Go's `context.Context` with typed
keys rather than a world object. Each step receives the context and
returns an updated copy:

```go
type CartKey struct{}

func TheShoppingCartIsEmpty(ctx context.Context) (context.Context, error) {
    return context.WithValue(ctx, CartKey{}, support.NewCart()), nil
}

func TheCustomerAddsToTheCart(ctx context.Context, product string) (context.Context, error) {
    cart := ctx.Value(CartKey{}).(*support.Cart)
    cart.Add(product)
    return ctx, nil
}
```

---

## Support Layer Patterns

The support layer holds the implementation logic that step definitions
delegate to. This is where framework-specific, UI-specific, and
infrastructure-specific code lives.

### Page Object Pattern (UI Testing)

A page object encapsulates the structure and interactions of a single
page or component. Step definitions call page object methods; they never
touch selectors directly.

```python
# support/pages/login_page.py
class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def login_as(self, username, password):
        self.browser.fill("#username", username)
        self.browser.fill("#password", password)
        self.browser.click("#login-button")

    def error_message(self):
        return self.browser.text(".login-error")
```

```python
# features/steps/when/the_user_logs_in.py
from behave import when

@when('the user logs in as "{username}" with password "{password}"')
def step_impl(context, username, password):
    context.login_page.login_as(username, password)
```

### API Client Pattern (API Testing)

An API client encapsulates HTTP interactions — base URL, headers,
authentication, serialization.

```python
# support/api_client.py
class APIClient:
    def __init__(self, base_url, token=None):
        self.base_url = base_url
        self.session = requests.Session()
        if token:
            self.session.headers["Authorization"] = f"Bearer {token}"

    def create_product(self, name, price):
        resp = self.session.post(
            f"{self.base_url}/products",
            json={"name": name, "price": price}
        )
        resp.raise_for_status()
        return resp.json()
```

### Factory Pattern (Test Data)

Factories create test entities with sensible defaults, reducing boilerplate
in Given steps.

```python
# support/factories.py
class UserFactory:
    @staticmethod
    def create(name="Test User", role="member", **overrides):
        defaults = {
            "name": name,
            "email": f"{name.lower().replace(' ', '.')}@test.com",
            "role": role,
            "active": True,
        }
        defaults.update(overrides)
        return User.create(**defaults)
```

```python
# features/steps/given/a_registered_user.py
from behave import given
from support.factories import UserFactory

@given('a registered user named "{name}" with a "{role}" role')
def step_impl(context, name, role):
    context.current_user = UserFactory.create(name=name, role=role)
```

---

## Shared State Management

Steps within a scenario need to share state — the user created in a
`Given`, the result captured in a `When`, the value asserted in a `Then`.
Every BDD framework provides a mechanism for this.

In the one-step-per-file model, shared state is especially important
because steps cannot share local variables through a common file scope.
The context/world object is the only path for inter-step communication.

### The Context/World Object

| Framework | State Object | Scope |
| :--- | :--- | :--- |
| **Behave** | `context` (passed to every step) | Per-scenario by default |
| **pytest-bdd** | Fixtures (via `@pytest.fixture`) | Per-function or wider |
| **Cucumber (Ruby)** | Instance variables (`@var`) in World | Per-scenario |
| **Cucumber (Java)** | Dependency-injected step classes | Per-scenario (with DI) |
| **Cucumber (JS)** | `this` (World object) | Per-scenario |
| **SpecFlow** | `ScenarioContext` / constructor injection | Per-scenario |
| **Godog** (Go) | `context.Context` with typed keys | Per-scenario |

### Guidelines

- **Use the framework's state mechanism.** Do not use module-level
  globals, class-level variables, or file-based state.
- **Name context attributes clearly.** `context.current_user` is better
  than `context.u`. `this.lastApiResponse` is better than `this.res`.
- **Set state in Given, read it in When/Then.** If a Then step cannot
  find the expected attribute, the scenario is missing a Given — that is a
  signal, not a bug to work around.
- **Clean up automatically.** Use hooks or framework lifecycle management
  to reset state between scenarios. Never rely on one scenario cleaning
  up after itself for the next one.

### Example: State Flow Across Files

```python
# features/steps/given/a_registered_user.py
from behave import given
from support.factories import UserFactory

@given('a registered user named "{name}"')
def step_impl(context, name):
    context.current_user = UserFactory.create(name=name)
```

```python
# features/steps/when/the_user_places_an_order.py
from behave import when

@when('the user places an order for "{product}"')
def step_impl(context, product):
    context.order = context.order_service.place(
        user=context.current_user,
        product=product
    )
```

```python
# features/steps/then/the_order_should_be_confirmed.py
from behave import then

@then('the order should be confirmed')
def step_impl(context):
    assert context.order.status == "confirmed"
```

Each step reads from and writes to `context`. The chain of state is
explicit and traceable across files.

---

## Scaling Patterns

### Large Projects

When the project has 100+ step definitions:

- **Use the audit script regularly** to detect unused step files and
  near-duplicates.
- **Review new steps** against existing filenames before merging — the
  directory listing serves as a searchable index.
- **Agree on naming conventions.** Inconsistent step phrasing leads to
  duplicates. Maintain a glossary of standard step phrases.

### Multi-Team Projects

When multiple teams contribute scenarios and steps:

- **Share common steps via a dedicated package.** Extract shared steps
  into a library that all teams depend on.
- **The keyword directories naturally prevent collisions** since each step
  is in its own file with a descriptive name.
