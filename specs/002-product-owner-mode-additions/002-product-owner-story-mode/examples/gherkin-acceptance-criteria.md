---
title: "Gherkin Acceptance Criteria — Template and Examples"
description: "Ticket-ready examples of Given-When-Then acceptance criteria (Gherkin) for user stories, with a copyable blank template."
---

# Gherkin Acceptance Criteria

## When to use it

Acceptance criteria are the "confirmation" half of a story. Given-When-Then is the most codified way to write them. Per the Cucumber Gherkin reference:

- **Given** puts the system in a known state — the preconditions.
- **When** describes an event or action.
- **Then** describes an expected outcome, ideally on an observable output.

Cucumber recommends 3-5 steps per scenario and warns that outcomes should be observable (a UI change, report, or message) rather than buried in a database. Two supporting keywords make criteria cleaner:

- `Background` — shared preconditions repeated in every scenario of a feature.
- `Scenario Outline` + an `Examples` table — run one scenario across several data rows instead of copy-pasting.

The convention is optional but powerful: when criteria are written this way they can later be wired to automated checks with no rewriting.

## Filled example 1 — login lockout

```
Title:      Lock account after repeated failed logins
Type:       Story
Epic:       EPIC-11 Auth hardening
Priority:   High
Estimate:   3 points
Status:     Ready

As a security-conscious user, I want the system to lock my account
after repeated failed logins, so that my account resists brute-force
attempts.

Acceptance criteria (Gherkin):

  Feature: Login lockout

    Background:
      Given the account lockout threshold is set to 5 failed attempts

    Scenario: Account locks after the threshold is reached
      Given a user "ada" has entered a wrong password 4 times
      When "ada" enters a wrong password a 5th time
      Then the account "ada" is locked
      And a reset email is queued to "ada"

    Scenario: Correct password resets the failed-attempt counter
      Given a user "ada" has entered a wrong password 4 times
      When "ada" enters the correct password
      Then the failed-attempt counter for "ada" is reset to 0
```

## Filled example 2 — search with a data table

```
Title:      Product search results are capped and paginated
Type:       Story
Epic:       EPIC-09 Catalog search
Priority:   Medium
Estimate:   5 points
Status:     Ready

As a shopper, I want search results capped per page with a pager, so
that a large catalog loads quickly and I can move through it.

Acceptance criteria (Gherkin):

  Feature: Search result pagination

    Scenario Outline: Results page respects the page size
      Given the catalog contains more than <total> matching items
      When a shopper searches and is on page <page>
      Then at most <pagesize> items are shown
      And a pager offers navigation to neighbouring pages

      Examples:
        | total | page | pagesize |
        |   100 |    1 |       20 |
        |   100 |    5 |       20 |
        |     3 |    1 |       20 |
```

## Blank template (copyable)

```
Title:      <short outcome phrase>
Type:       Story
Epic:       <parent epic key>
Priority:   <>
Estimate:   <> points
Status:     Ready

As a <role>, I want <capability>,
so that <benefit>.

Acceptance criteria (Gherkin):

  Feature: <feature name>

    Background:           # only if preconditions repeat
      Given <shared precondition>

    Scenario: <happy path>
      Given <precondition>
      When <action>
      Then <observable outcome>
      And <additional expectation>

    Scenario Outline: <parameterised case>   # optional
      Given <precondition with <param>>
      When <action with <param>>
      Then <outcome with <param>>

      Examples:
        | param | <other> |
        |  val  |   val   |
```

## Sources

- https://cucumber.io/docs/gherkin/reference/ — Given/When/Then, Background, Scenario Outline/Examples, the observable-outcome guidance.
- https://www.mountaingoatsoftware.com/agile/user-stories — "conditions of satisfaction," the concept acceptance criteria confirm.
