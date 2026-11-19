---
title: "Job Story — Template and Examples"
description: "Ticket-ready examples of the situation-first job-story format (When / I want to / so I can) and a copyable blank template."
---

# Job Story

## When to use it

Job stories are a situation-first alternative to role-based user stories, rooted in Jobs-to-be-Done thinking. Reach for them when the *context* a person is in matters more than *who* they are, or when the benefit is better expressed as progress on a job than as a feature request. The widely-used structure is:

- When **[situation]** ...
- I want to **[motivation]** ...
- so I can **[expected outcome]**.

> Note on sourcing: the canonical source for job stories is Alan Klement's article on jtbd.io proposing this format. That page was **not reachable during this research (timed out)**, so no quotation is reproduced from it and it is cited only as "not reachable." The structure above is presented as established industry convention.

The key difference from the Connextra "As a... I want... so that..." form: a job story opens with a situation, not a persona. This tends to surface *why* someone needs the capability and reduces the temptation to design for a generic "user."

Use a job story when:

- The trigger is a situation or life/event moment, not a job title.
- Multiple personas share the same situation and motivation.
- You want to keep the focus on the underlying problem, not a requested solution.

## Filled example 1 — search

```
Title:      Search my own past orders
Type:       Story
Epic:       EPIC-09 Self-service account
Priority:   Medium
Estimate:   3 points
Status:     Ready

When I need to find an older purchase to re-download or return it,
I want to search my order history by keyword and date,
so I can find the exact order without scrolling through months of items.

Acceptance criteria:
- Order history supports a free-text search over product names and
  order numbers.
- Results can be filtered by date range.
- Empty-state guidance is shown when a search matches nothing.
```

## Filled example 2 — onboarding

```
Title:      Re-enter interrupted onboarding
Type:       Story
Epic:       EPIC-03 First-run experience
Priority:   High
Estimate:   2 points
Status:     Ready

When I return to finish setting up my workspace after closing the tab
midway,
I want the app to resume exactly where I left off,
so I do not have to repeat steps I already completed.

Acceptance criteria:
- Onboarding progress is persisted per step.
- Returning users land on the next incomplete step.
- Completed steps show a done state and remain editable.
```

## Blank template (copyable)

```
Title:      <short outcome phrase>
Type:       Story
Epic:       <parent epic key>
Priority:   <>
Estimate:   <> points
Status:     Ready

When <situation / trigger>,
I want to <motivation>,
so I can <expected outcome>.

Acceptance criteria:
- <observable behavior>
- <observable behavior>
- <edge case handling>
```

## Sources

- https://jtbd.info/replacing-the-user-story-with-the-job-story-297884fcb07c — (not reachable during research; timed out). Canonical job-story proposal by Alan Klement; cited for attribution only, no quotation reproduced.
- https://www.mountaingoatsoftware.com/agile/user-stories — role-based Connextra format, used here as the contrast that job stories respond to.
