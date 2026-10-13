---
title: "Connextra User Story — Template and Examples"
description: "Ticket-ready examples of the 'As a / I want / so that' user-story format, with an INVEST check and a copyable blank template."
---

# Connextra User Story

## When to use it

This is the default format for feature work written from a user's perspective. It works best when you can name a concrete type of user and a clear benefit. The standard template (Mountain Goat Software) is:

> As a < type of user >, I want < some goal > so that < some reason >.

The three parts are the role (who), the capability (what), and the value (why). Mountain Goat stresses the written line is a placeholder: "every user story is a placeholder for a future conversation." Ron Jeffries' three aspects — Card (the written line), Conversation (the discussion), and Confirmation (the acceptance tests) — frame what surrounds it.

Two rules that keep these stories healthy:

- Write the role for the end user, not the product owner.
- Keep the "so that" clause — it is what makes the story negotiable and testable.

Before a story of this form is schedulable, run it through **INVEST** (Bill Wake, XP123): Independent, Negotiable, Valuable, Estimable, Small, Testable. The filled examples below include a quick INVEST note.

## Filled example 1 — checkout

```
Title:      Guest checkout for digital products
Type:       Story
Epic:       EPIC-42 Reduce cart abandonment
Priority:   High
Estimate:   3 points
Status:     Ready

As a shopper who is not signed in, I want to buy a digital product
without creating an account, so that I can complete my purchase quickly
and avoid a password.

Acceptance criteria:
- The cart offers a "Checkout as guest" option alongside sign-in.
- A guest can pay for digital-only items end to end and receive a
  download link by email.
- A guest order still records an email address for receipts.
- Creating an account is offered after payment, never required before.

INVEST note: Independent (no account prerequisite); Valuable (removes a
known drop-off step); Testable (criteria above are observable).
```

## Filled example 2 — notifications

```
Title:      Digest email for mentions
Type:       Story
Epic:       EPIC-17 Notifications overhaul
Priority:   Medium
Estimate:   5 points
Status:     Ready

As a team member in a busy workspace, I want a daily digest of my
mentions, so that I am not interrupted by per-message pings but still
do not miss being asked something.

Acceptance criteria:
- A user can opt into a daily digest of @mentions from their settings.
- The digest batches all mentions in the last 24h and is sent at 09:00
  local time.
- Each item links back to the originating message.
- When there are zero mentions, no email is sent.

INVEST note: Small (one trigger, one template); Negotiable (format of
the digest open to design); Testable (send/no-send cases are concrete).
```

## Blank template (copyable)

```
Title:      <short outcome phrase>
Type:       Story
Epic:       <parent epic key>
Priority:   <>
Estimate:   <> points
Status:     Ready

As a <specific end-user role>, I want <capability>,
so that <benefit/value>.

Acceptance criteria:
- <observable behavior>
- <observable behavior>
- <edge case handling>

INVEST check:
- Independent: <yes/no, note>
- Negotiable:  <yes — what detail is left open>
- Valuable:    <value to the user/customer>
- Estimable:   <yes/no; if no, run a spike>
- Small:       <fits in a sprint; yes/no>
- Testable:    <how it would be confirmed>
```

## Sources

- https://www.mountaingoatsoftware.com/agile/user-stories — Connextra template, card/conversation/confirmation, "placeholder for a future conversation."
- https://www.atlassian.com/agile/project-management/user-stories — "As a [user], I want [goal] so that [reason]." and "smallest unit of work... expressed from the software user's perspective."
- https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/ — INVEST quality checklist.
