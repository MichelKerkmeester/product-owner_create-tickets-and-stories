---
title: "Epic-to-Story Splitting — Patterns and Examples"
description: "How to split a large epic into ticket-ready stories using vertical slices and the SPIDR prompts, with worked examples and a copyable template."
---

# Epic-to-Story Splitting

## When to use it

Epics are large stories too big for one sprint. They have to be split into smaller stories that still each represent meaningful progress. Mountain Goat Software defines the practice:

> "Story splitting is the practice of breaking a large user story into smaller user stories that still represent meaningful progress toward an outcome."

The single most important rule, repeated across the source: **split by value, not by technical layer.** Creating separate "build the UI", "build the backend", "build the database" stories "rarely helps the team finish anything meaningful" because "nothing can be demonstrated as a working user flow." Instead, cut a **vertical slice** — enough of every layer to deliver a narrower but working capability end to end.

The **SPIDR** prompts give five ways to find a split:

- **S**pike — a short investigation when uncertainty blocks a good split.
- **P**aths — alternate paths through a workflow.
- **I**nterfaces — UI, platform, channel, or interaction mode.
- **D**ata — type, amount, source, or complexity of data.
- **R**ules — business rules, validations, calculations, exceptions.

A sizing warning to watch for is the "90% syndrome": "software is 90% done for 90% of the schedule." Be wary of bringing a story into a sprint if it could consume half or more of the sprint. Split collaboratively, roughly two sprints ahead: product owners bring outcomes, developers bring knowledge of where the real complexity sits.

Also remember: story splitting is not task splitting. A story describes an outcome; a task describes an activity. "A customer can pay with one payment method on the happy path" is a story; "create database tables for payments" is a task.

## Worked split 1 — payments epic (split by Paths + Rules)

Start with an epic that is too big:

```
Epic EPIC-21: Customers can pay for orders
  (covers multiple payment methods, refunds, failure handling,
   invoicing, and receipts — clearly more than one sprint)
```

Split into vertical, value-bearing stories. Each one works end to end for a narrower case:

```
Title:      Pay by card on the happy path          (split by Paths)
Type:       Story  | Epic: EPIC-21 | Priority: High | 5 pts | Status: Ready
As a shopper, I want to pay for my cart with a credit card,
so that I can complete my purchase without leaving checkout.
Acceptance criteria:
- Card payment succeeds for a valid card and shows an order-confirmed page.
- The order is recorded and an emailed receipt is queued.

Title:      Handle a declined card gracefully      (split by Rules/exceptions)
Type:       Story  | Epic: EPIC-21 | Priority: High | 3 pts | Status: Ready
As a shopper, I want a clear error when my card is declined,
so that I can correct it or try another card.
Acceptance criteria:
- A declined card shows the issuer's reason in plain language.
- The cart and entered address are preserved for a retry.

Title:      Refund a card payment                  (split by Paths)
Type:       Story  | Epic: EPIC-21 | Priority: Medium | 5 pts | Status: Ready
As a support agent, I want to refund a completed card order,
so that I can resolve a customer's problem.
Acceptance criteria:
- A full refund can be issued from the order view.
- The customer is emailed a refund confirmation.
```

The deferred scope (other payment methods, partial refunds, invoicing) becomes later stories — each still a working slice, not a technical layer.

## Worked split 2 — home search epic (split by Data + Interfaces)

```
Epic EPIC-09: Prospective buyers can search homes
  (size, rooms, status, type, age, amenities, map, mobile)
```

Split by narrowing data and interface first, expanding later:

```
Title:      Search by size and rooms               (split by Data)
Type:       Story  | Epic: EPIC-09 | Priority: High | 5 pts | Status: Ready
As a prospective buyer, I want to filter homes by size and room count,
so that I see only homes that fit my needs.
Acceptance criteria:
- Results filter by min/max area and min rooms.
- A matching result set is shown and is empty-stated when none match.

Title:      Search on the web only                  (split by Interfaces)
Type:       Story  | Epic: EPIC-09 | Priority: High | 3 pts | Status: Ready
As a prospective buyer, I want to run the search in a desktop browser,
so that I can browse listings from my computer.
Acceptance criteria:
- The filters and results render on desktop widths.
- (Mobile is a separate later story, not part of this one.)

Title:      Add a spike for map-based search        (SPIDR Spike)
Type:       Spike   | Epic: EPIC-09 | Priority: Low | 1 pt  | Status: Ready
As the team, we want a time-boxed investigation into map-tile licensing,
so that we can estimate the map-search story accurately.
Definition of done:
- A short note with a recommended approach and a rough estimate.
```

## Blank template (copyable)

```
Epic:       <epic key and name>
Split trigger: <too big for a sprint / failed the half-sprint check>

For each resulting story:

Title:      <outcome phrase>
Type:       Story
Epic:       <parent epic key>
Priority:   <>
Estimate:   <> points
Status:     Ready
Split used: <Paths | Interfaces | Data | Rules | Spike>

As a <role>, I want <narrower capability>,
so that <value>.
Acceptance criteria:
- <observable behavior>
- <observable behavior>

Checklist for a good split:
- It is a vertical slice (works end to end), not a technical layer.
- It is an outcome, not an activity/task.
- It is small enough to finish and demonstrable on its own.
- Deferred scope is captured as named future stories.
```

## Sources

- https://www.mountaingoatsoftware.com/agile/user-stories/story-splitting-how-to-split-user-stories-so-teams-can-finish — definition, "split by value not by layer," SPIDR, vertical slices, 90% syndrome, story-vs-task distinction.
- https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/ — "Small" and "Valuable" INVEST attributes that splitting protects.
- https://www.mountaingoatsoftware.com/agile/user-stories — epics as large stories to be decomposed.
