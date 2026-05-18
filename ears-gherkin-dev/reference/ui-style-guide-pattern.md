# UI Style Guide Pattern — Detailed Reference

This document describes how to specify UI component appearance and
behavior within the EARS/Gherkin framework. Consult this when working
with visual requirements, design systems, or component libraries.

---

## The Problem

Many UI properties are testable system requirements: contrast ratios,
font sizes, responsive breakpoints, component states (error, disabled,
loading), accessibility attributes. But embedding visual details
directly in feature scenarios creates brittle, unreadable specifications
that couple behavior to presentation.

```gherkin
# BAD: Visual details in a feature scenario
Scenario: Invalid email shows an error
  Given the user is on the registration form
  When the user submits an invalid email address
  Then a red div with class "alert-danger" should appear
  And the text color should be "#dc3545"
  And the font-weight should be "700"
```

The scenario above tests implementation details, not behavior. If the
design team changes the error color from `#dc3545` to `#b02a37`, every
scenario referencing that color breaks — even though the system behavior
is unchanged.

The solution is a layer of abstraction: define a **component
vocabulary** using EARS requirements and Gherkin scenarios, then
reference that vocabulary by name in feature scenarios.

---

## The Style Guide as EARS/Gherkin Specifications

The style guide is not a separate artifact or a PDF from the design
team. It is a set of `.feature` files that specify what each styled
component looks like and how it behaves, using the same EARS
requirements and Gherkin scenarios as every other part of the system.

A component specification file defines the visual vocabulary:

```gherkin
Feature: Alert Components

  The alert component library provides styled feedback messages
  for user interactions. Each alert variant has defined visual
  properties that ensure consistency and accessibility.

  Rule: The error alert component shall display text with a minimum contrast ratio of 4.5:1 against its background.

    Scenario: Error alert meets contrast requirements
      Given an error alert is rendered with default styling
      Then the text-to-background contrast ratio should be
        at least 4.5:1

  Rule: The error alert component shall use the "destructive" color token for its border and icon.

    Scenario: Error alert uses the correct color token
      Given an error alert is rendered with default styling
      Then the border color should match the "destructive" token
      And the icon color should match the "destructive" token

  Rule: The success alert component shall use the "positive" color token for its border and icon.

    Scenario: Success alert uses the correct color token
      Given a success alert is rendered with default styling
      Then the border color should match the "positive" token
      And the icon color should match the "positive" token
```

These are ordinary EARS requirements. They use the same patterns,
the same `Rule:` structure, and the same scenario conventions as any
other feature file. The only difference is that they specify
**component properties** rather than user-facing workflows.

---

## Two Layers of Specification

The style guide pattern creates two layers, both using EARS and
Gherkin:

```text
Component-level specs     Define the vocabulary
  "The error alert component shall display text with a
   minimum contrast ratio of 4.5:1"
       ↓ referenced by name ↓
Feature-level specs       Use the vocabulary
  "Then the form shall display an error alert"
```

### Component-Level (the style guide)

These feature files live in a `components/` subdirectory (or similar
grouping) within `features/`. They specify what each component
looks like and how it responds to state changes. Their scenarios
test the component library directly — render the component, verify
its properties.

### Feature-Level (the application)

These are the feature files that specify user-facing behavior. They
reference components by name: "an error alert is displayed," "a
primary button is enabled," "a loading spinner appears." They never
mention colors, fonts, CSS classes, or pixel dimensions.

### Why This Works

This is the same abstraction pattern used everywhere in software.
A feature scenario says "the customer places an order" without
specifying HTTP methods or database queries. Similarly, it says "an
error alert is displayed" without specifying border colors or font
weights. The details live one layer down, verified by their own
specifications.

---

## EARS Patterns for UI Components

Each EARS pattern has natural applications in component
specification:

### Ubiquitous — Always-On Visual Properties

Properties that must hold at all times, regardless of component
state:

```text
The primary button component shall use a minimum font size
of 16 pixels.

The text input component shall maintain a minimum contrast
ratio of 4.5:1 between its label text and background.

The icon button component shall have a minimum touch target
size of 44 by 44 pixels.
```

### State-Driven — Component State Variations

Visual properties that change based on component state:

```text
While the text input is in the error state, the text input
component shall display a border using the "destructive"
color token.

While the submit button is in the disabled state, the submit
button component shall reduce its opacity to 50 percent.

While the navigation menu is in the collapsed state, the
navigation component shall display only icon indicators.
```

### Event-Driven — Interactions and Transitions

Visual responses to user interactions:

```text
When the user hovers over a primary button, the button
component shall increase its background brightness by
10 percent.

When the text input receives focus, the text input component
shall display a 2-pixel focus ring using the "focus" color
token.

When a toast notification is dismissed, the toast component
shall animate out over 200 milliseconds.
```

### Unwanted Behavior — Degraded Visual States

Responses to error conditions or missing resources:

```text
If an image fails to load, then the image component shall
display a placeholder icon and alt text.

If the custom font fails to load within 3 seconds, then the
typography system shall fall back to the system font stack.
```

---

## Feature-Level Scenarios Using Component Vocabulary

Once the component vocabulary is defined, feature scenarios
reference it by name. The scenario describes **what component
appears**, not what it looks like:

### Before — Visual Details in Feature Scenarios

```gherkin
# BAD: Visual details leak into a feature scenario
Scenario: Form shows validation feedback
  Given the user is filling out the registration form
  When the user submits the form with an empty name field
  Then a red-bordered div with a warning icon should appear
    below the name field
  And the div should contain the text "Name is required"
  And the field border should change to #dc3545
```

### After — Component Vocabulary in Feature Scenarios

```gherkin
# GOOD: References component vocabulary
Scenario: Form shows validation feedback
  Given the user is filling out the registration form
  When the user submits the form with an empty name field
  Then the name field should display an error state
  And an error alert should display "Name is required"
```

The scenario says "error state" and "error alert" — terms defined
in the component-level specifications. What those look like
visually (red border, destructive color token, contrast ratio) is
verified by the component-level scenarios, not repeated here.

### More Examples

```gherkin
# BAD: Leaking button styling
Scenario: User submits the form
  Given the user has completed all required fields
  When the user clicks the blue button labeled "Submit"
  Then a green banner should appear with the text "Success"

# GOOD: Using component vocabulary
Scenario: User submits the form
  Given the user has completed all required fields
  When the user clicks the "Submit" primary button
  Then a success alert should display "Your form has been submitted"
```

```gherkin
# BAD: Specifying loading implementation
Scenario: Dashboard loads data
  Given the user navigates to the dashboard
  When the data is being fetched
  Then a spinning SVG animation should appear centered on the page

# GOOD: Using component vocabulary
Scenario: Dashboard loads data
  Given the user navigates to the dashboard
  When the data is being fetched
  Then a loading indicator should be displayed
```

---

## Step Definitions and the Support Layer

Step definitions bridge component vocabulary to concrete
verification. They work at two levels:

### Component-Level Step Definitions

These verify visual properties directly. They live in the support
layer and interact with the rendering engine (browser, test
renderer):

```python
# features/steps/then/the_contrast_ratio_should_be_at_least.py
from behave import then

@then('the text-to-background contrast ratio should be at least {ratio}')
def step_impl(context, ratio):
    actual = context.component.measure_contrast_ratio()
    assert actual >= float(ratio), (
        f"Contrast ratio {actual} is below minimum {ratio}"
    )
```

```python
# features/steps/then/the_border_color_should_match_the_token.py
from behave import then

@then('the border color should match the "{token}" token')
def step_impl(context, token):
    expected = context.design_tokens[token]
    actual = context.component.computed_style("border-color")
    assert actual == expected, (
        f"Expected border color {expected} ({token}), got {actual}"
    )
```

### Feature-Level Step Definitions

These verify that the correct component is rendered, without
re-checking its visual properties (the component specs already
cover that):

```python
# features/steps/then/an_error_alert_should_display.py
from behave import then

@then('an error alert should display "{message}"')
def step_impl(context, message):
    alert = context.page.find_alert(variant="error")
    assert alert is not None, "No error alert found"
    assert alert.text == message, (
        f"Expected '{message}', got '{alert.text}'"
    )
```

```python
# features/steps/then/the_field_should_display_an_error_state.py
from behave import then

@then('the {field} field should display an error state')
def step_impl(context, field):
    input_component = context.page.find_input(field)
    assert input_component.has_state("error"), (
        f"Field '{field}' is not in error state"
    )
```

### Design Tokens in the Support Layer

A support module maps token names to concrete values. This is the
single source of truth for the mapping between vocabulary and
visual properties:

```python
# support/design_tokens.py
TOKENS = {
    "destructive": "#dc3545",
    "positive": "#198754",
    "warning": "#ffc107",
    "focus": "#0d6efd",
    "neutral": "#6c757d",
}
```

When the design team changes the destructive color from `#dc3545`
to `#b02a37`, one file changes. The component-level scenarios
verify the new color renders correctly. Feature-level scenarios are
untouched.

---

## What Stays Outside Gherkin

Even with the style guide pattern, some visual properties resist
behavioral specification because they have no testable criterion:

- **Color palette harmony** — whether colors "look good together"
  is an aesthetic judgment, not a measurable property
- **Spacing rhythm and proportion** — whether whitespace "feels
  balanced" is subjective
- **Illustration and iconography style** — whether artwork matches
  brand tone is a design review, not a test
- **Typography aesthetics** — whether a font "feels right" for the
  brand is a human judgment
- **Animation easing curves** — whether a transition "feels smooth"
  is perceptual

These belong in design documentation (brand guides, Figma files,
art direction briefs) that inform the design tokens and component
implementations but cannot be meaningfully automated.

**The test:** If you can write a pass/fail assertion for a visual
property, it belongs in an EARS requirement. If you cannot, it
belongs in a design spec.

---

## Anti-Patterns

### Skipping the Component Layer

Writing feature-level scenarios that verify visual properties
directly:

```gherkin
# BAD: Feature scenario testing component internals
Rule: When the user submits invalid data, the form shall display an error alert.

  Scenario: Invalid data shows error
    Given the user is on the order form
    When the user submits the form without a shipping address
    Then a div with class "alert-error" should appear
    And its background color should be "#f8d7da"
    And its border color should be "#dc3545"
    And the text "Shipping address is required" should appear
```

The visual properties belong in the component spec for "error
alert," not in the order form feature. The feature scenario should
say `Then an error alert should display "Shipping address is
required"`.

### Duplicating Visual Checks Across Layers

If the component spec already verifies that error alerts use the
destructive color token, feature scenarios should not re-verify the
color. This duplicates coverage and creates multiple places to
update when the design changes.

### Testing Purely Aesthetic Properties

```gherkin
# BAD: No testable criterion
Rule: The dashboard shall have a visually appealing layout.

  Scenario: Dashboard looks good
    Given the user navigates to the dashboard
    Then the layout should be aesthetically pleasing
```

"Aesthetically pleasing" has no pass/fail criterion. Either
decompose it into testable properties (alignment, spacing values,
contrast ratios) or leave it in design review.

### Hardcoding Values Instead of Tokens

```gherkin
# BAD: Hardcoded color value
Scenario: Error alert uses the correct color
  Given an error alert is rendered
  Then the border color should be "#dc3545"

# GOOD: References a design token
Scenario: Error alert uses the correct color
  Given an error alert is rendered
  Then the border color should match the "destructive" token
```

Hardcoded values spread across scenarios become a maintenance
burden when the design changes. Token references centralize the
mapping in one place.
