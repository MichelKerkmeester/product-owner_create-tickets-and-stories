---
title: "Definition of Ready and Definition of Done — Checklists and Examples"
description: "Ticket-ready DoR and DoD checklists that gate a story's lifecycle, with a worked example and copyable blank templates."
---

# Definition of Ready (DoR) and Definition of Done (DoD)

## When to use them

DoR and DoD are team-level checklists that bracket a story's life. They are different from acceptance criteria, and Atlassian is explicit about the distinction: "the definition of done is not the same thing as acceptance criteria." Acceptance criteria describe the behavior of one story; DoR and DoD describe the team-wide bars for *starting* and *finishing* any work.

- **Definition of Ready (DoR)** "allows you to evaluate work before your team starts on it." It answers: is this item clear and feasible enough to pull into a sprint without scrambling?
- **Definition of Done (DoD)** is "a set of criteria that a product increment must meet for the team to consider it complete and ready for customers." It is team-owned and a living document — Atlassian suggests reviewing it every quarter so new lessons are captured.

Keep them short and real. A DoR that nobody enforces, or a DoD so long nothing ever passes it, both fail in practice.

## Worked example — one ticket showing both gates

This is how DoR and DoD look attached to a concrete story a developer would receive.

```
Title:      Rate a completed order
Type:       Story
Epic:       EPIC-17 Post-purchase engagement
Priority:   Medium
Estimate:   3 points
Status:     In Progress

As a shopper, I want to rate a delivered order with stars and a comment,
so that I can share my experience and help other buyers.

Acceptance criteria:
- A 1–5 star selector and optional comment are shown on a delivered order.
- A submitted rating is saved and visible on the product page.
- A rating cannot be submitted without selecting at least one star.

Definition of Ready (met — pulled in):
- [x] Written in the Connextra form with a clear value clause.
- [x] Acceptance criteria present and testable.
- [x] Dependencies identified (rating service API is live).
- [x] Sized at 3 points; fits comfortably in the sprint.

Definition of Done (to verify before close):
- [ ] Acceptance criteria all pass.
- [ ] Unit and integration tests added; CI green.
- [ ] Reviewed by a second engineer.
- [ ] Accessible (keyboard + screen reader) on mobile and desktop.
- [ ] Deployed to staging and verified.
```

## Worked example 2 — a story that fails DoR

This shows the gates doing their job: an item that is **not** ready is kept out of the sprint.

```
Title:      AI-powered product recommendations
Type:       Story
Epic:       EPIC-09 Catalog engagement
Priority:   Medium
Estimate:   (not set)
Status:     Blocked — not Ready

As a shopper, I want the homepage to recommend products I might like,
so that I discover relevant items without searching.

Definition of Ready (NOT met — do not pull in):
- [ ] Acceptance criteria missing (what counts as a "good" recommendation?).
- [ ] Dependency unresolved (no recommendation model or data contract yet).
- [ ] Not sized (complexity unknown).
- [ ] Not testable in its current form.

Action: split off a Spike to investigate the model and data, then rewrite
this story with concrete acceptance criteria before the next refinement.
```

## Blank template — Definition of Ready (copyable)

```
Definition of Ready (check before pulling a story in):
- [ ] Story written from an end-user perspective (role + value).
- [ ] Acceptance criteria are present and testable.
- [ ] Dependencies (design, API, data) are identified and available.
- [ ] Sized; small enough to finish within a sprint.
- [ ] Ranked and unblocked relative to other work.
- [ ] Definition of Done is understood for this item.
```

## Blank template — Definition of Done (copyable)

```
Definition of Done (check before closing a story):
- [ ] All acceptance criteria pass.
- [ ] Tests added (unit + integration); existing tests still pass.
- [ ] Code reviewed and merged.
- [ ] Non-functional needs met (performance, accessibility, security).
- [ ] Documentation updated where behavior changed.
- [ ] Deployed/verified in a non-production environment.
- [ ] Product owner has accepted the increment.
```

## Sources

- https://www.atlassian.com/agile/project-management/definition-of-ready — DoR purpose: evaluate work before the team starts.
- https://www.atlassian.com/agile/project-management/definition-of-done — DoD purpose: criteria for "complete and ready for customers"; DoD-vs-acceptance-criteria distinction; living-document guidance.
- https://www.mountaingoatsoftware.com/agile/user-stories — "conditions of satisfaction," which DoD generalizes team-wide.
