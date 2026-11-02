---
title: "Barter Story Template — Simple Tier (One Requirement)"
description: "Leanest copyable story scaffold for a single small change: one Story line, a compact Overview, one spec block, one or two Given/When/Then scenarios, and a short Definition of Done. Five-minute fill."
---

# Barter Story Template — Simple

## When to use it

Use this for a story that covers **one requirement** and a **small change** — a single behavior, a copy tweak, one new rule — that fits in one task. There is no shared machinery, no degradation ladder, no second requirement to keep consistent with the first.

Pick a different tier when:

- You have **two to four independent requirements** → use [`barter-story-template-medium.md`](barter-story-template-medium.md).
- You have **several requirements that share the same mechanism** (a shared pipeline, rule ladder, state machine or lifecycle) → use [`barter-story-template-complex.md`](barter-story-template-complex.md).

What Simple deliberately drops relative to Medium:

- The **"How {mechanism} works"** shared-mechanics section (Simple has no shared machinery).
- The full checklist **Definition of Ready** — replaced by a one-line readiness statement, because a single small change rarely needs a four-box gate. Promote to the Medium DoR the moment readiness is genuinely in doubt.
- The **promise bullets** under the epic User Story — one requirement means the epic promise and the requirement promise are the same line.
- **"Which means that"** is optional here; keep it only if an implication is not obvious from the scenarios.

Everything a PO needs is in the scaffold below; you should not have to open another file to fill it.

## Copyable template

```markdown
# Story - {Version/Area} - {Feature} - {Name}

## Overview
* * *
**Story:** As a {end-user role}, I want {the one capability}, so that {the benefit in the user's terms}.

**Problem:** {What breaks this today, in one or two lines — the observable failure and why the current behavior cannot prevent it.}

**Solution:** {One sentence: the change that closes the gap.}

**Documentation:** [{governing doc}]({url})

**Readiness:** Story line and acceptance criteria below are written and testable; dependencies ({service / API / data this relies on — or "none"}) are live or confirmed absent. Not pulled into a sprint until this line is true.
* * *

## Requirement
* * *
1\. **{Requirement name}**
`({technical identifier, e.g. endpoint or field name})`
* * *
**Task(s):** [{task number and name}]({task link})
* * *
{One or two lines of prose: what the user expects, and what this requirement does about it.}

**{Spec block name, e.g. Rule}**
* * *
**{Rule}:** `{exact expression or threshold}`
{One plain-language line explaining it.}
* * *

Which means that:
*   {The hard guarantee, stated from the user's view — keep this block only if it adds something the scenarios don't}

**Acceptance criteria**

**Scenario:** {Normal path in a few words}
*   **Given** {precondition, exact expressions in `backticks`}
*   **When** {the user action or system event}
*   **Then** {the observable outcome}

**Scenario:** {The guarantee, or the one edge that matters}
*   **Given** {the boundary condition}
*   **When** {the final state or trigger}
*   **Then** {the never/always promise this change exists to keep}
* * *

## Definition of Done
* * *
Verify before the task closes:
*   [ ] The acceptance criteria pass against {the live system or realistic data}
*   [ ] Tests added covering {the rule and its guarantee}; CI green
*   [ ] Reviewed by a second engineer
*   [ ] Deployed to {staging or equivalent} and verified with production-shaped data
```

## Filling notes

- One **Story:** line carries the whole promise — it sits in the Overview, not repeated per requirement, because there is only one requirement.
- Keep it to **one or two scenarios**: the normal path, plus the single guarantee or edge that matters. Add a third only if the change genuinely has one; if you find yourself wanting three-plus scenarios or a degradation path, you are on the wrong tier — move up to Medium. Keep each scenario at three to five steps with an observable outcome; use **And** only for a needed second precondition or expectation.
- Preserve technical identifiers exactly (URLs, field names, thresholds) even when they look misspelled; flag oddities in prose rather than normalizing them.
- The **Readiness** line replaces the Medium DoR checklist. It is still a gate — do not pull the story into a sprint until the line is true — it is just short because a single small change does not warrant four boxes.
- Number the requirement with the escaped-dot form (`1\.`) that ClickUp exports use, even though there is only one. There is no `← PRIO` marker at this tier — with one requirement nothing needs prioritizing against anything.
- When the rule never loosens, say so in the spec block with an exact opt-out token (the exemplar uses `no_relaxation`, `no_fallback`) and let a scenario carry the trade-off. If the rule has a real multi-step ladder or lifecycle, that is a signal you want the Complex tier.

## Sources

- `barter-story-template-medium.md` — the tier above; Simple is this scaffold trimmed to one requirement with the DoR reduced to a readiness line.
- `barter-story-template.md` — the chooser and the shared principles this tier inherits.
- `../scratch/Story - Fv2.5 - Feed Function - Rulesets (conventional rewrite).md` — the reviewed exemplar the whole set generalizes; a single one of its rulesets is a Simple-tier story.
- `connextra-user-story.md` — the Story-line shape (role / capability / value).
- `gherkin-acceptance-criteria.md` — the Given/When/Then logic and the 3-5-step, observable-outcome guidance the scenario bullets follow.
- `definition-ready-done.md` — the Definition of Done bracket; Simple's readiness line is the DoR trimmed to a sentence.
