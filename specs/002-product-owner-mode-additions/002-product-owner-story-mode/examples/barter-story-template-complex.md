---
title: "Barter Story Template — Complex Tier (Multi-Requirement Feature with Shared Machinery)"
description: "The full house story scaffold for a feature whose requirements share a mechanism: everything in Medium plus a 'How {mechanism} works' section with shared-concept subsections, mechanism-following spec blocks, and a single PRIO marker. The Fv2.5 Rulesets exemplar (a degradation ladder) is one proven instance of the shape."
---

# Barter Story Template — Complex

## When to use it

Use this for a Barter story that covers **several requirements** (typically four or more) in one feature area where the requirements **share the same machinery** — a shared pipeline, an ordered rule ladder, a state machine, a matching lifecycle, any mechanism that would otherwise be re-explained in every block. The shared behavior is described **once** in a "How {mechanism} works" section and every requirement inherits it, so each block stays short and only states what makes that requirement different. The reviewed exemplar `../scratch/Story - Fv2.5 - Feed Function - Rulesets (conventional rewrite).md` is one instance of this tier, whose shared mechanism happens to be a filter-then-score degradation ladder; your mechanism can be anything requirements genuinely share.

Pick a different tier when:

- You have **one requirement and a small change** → use [`barter-story-template-simple.md`](barter-story-template-simple.md).
- You have **two to four requirements that share no machinery** — each stands entirely on its own → use [`barter-story-template-medium.md`](barter-story-template-medium.md). If you find there is nothing to write in "How {mechanism} works", you are on the wrong tier; drop to Medium.

What Complex adds relative to Medium:

- The **"How {mechanism} works"** section between the Overview and the Definition of Ready, with shared-concept subsections that every requirement below inherits. Name the subsections after your mechanism's real concepts (the exemplar uses **Sequence** and **Degradation**; yours might be **Stages**, **States**, **Escalation**, **Rollout**).
- **Spec blocks that follow the shared mechanism** per requirement: each requirement states its own exact values for the shared concepts. A degradation ladder with Primary / Relaxed / Final fallback rows and the `no_relaxation` / `no_fallback` skip conventions is one proven shape, not a requirement of this tier.
- A single inline **`← PRIO`** marker on the one requirement that leads the work.

Everything a PO needs is in the scaffold below; you should not have to open another file to fill it.

## Copyable template

```markdown
# Story - {Version/Area} - {Feature} - {Name}

## Overview
* * *
**User Story**
As a {user role}, I want {the feature's core promise}:
*   {Named part 1} should {what its name promises}
*   {Named part 2} should {what its name promises}
*   {Named part 3} should {what its name promises}

**Problem**
{What breaks the promise today}:
*   {Observable failure 1}
*   {Observable failure 2}
*   {Why the current mechanism cannot prevent this}

**Solution**
{One sentence: the shared mechanism that closes the gap}.

**Documentation**
[{link to the governing doc}]({url})
##   

## How {mechanism} works
* * *
{Two or three short paragraphs: what the mechanism is, where it runs, and what it
guarantees. This is the machinery every requirement below inherits.}

#### **{Shared concept 1, e.g. Sequence / Stages / States}**
* * *
{The ordered steps, rules or states every requirement below follows. Spell the
shape out once so requirements only fill in their own values. Example: a
degradation mechanism would list its tiers here, from the rule at full strength
down to what replaces it when every tier is exhausted.}

{One paragraph on any step that behaves differently and why.}

#### **{Shared concept 2, e.g. Degradation / Exceptions / Opt-outs}**
* * *
{Edge behavior every requirement inherits, and what happens when a requirement
opts out of part of it. State the shared guarantee the mechanism protects, and
the trade-off when a requirement opts out.}
* * *
##   

## Definition of Ready
* * *
Check off as met; pull requirements into a sprint only when every box is checked:
*   [ ] Every requirement's Story line is written in the Connextra form with a clear value clause
*   [ ] Acceptance criteria present and testable for every requirement
*   [ ] Dependencies identified ({e.g. the shared mechanism / service this relies on is live})
*   [ ] Sized by the team and each requirement fits comfortably in a sprint
##   

## Requirements
* * *
1\. **{Requirement name}** ← PRIO
`({technical identifier, e.g. endpoint or url name})`
* * *
**Task(s):** [{task number and name}]({task file or ticket link})
* * *
**Story:** As a {user role} {using this specific part}, I want {capability},
so that {the benefit in the user's terms}.

{Two or three lines of prose: what the user expects here, what breaks that
expectation, and what this requirement does about it.}

**{Spec block name — reuse Shared concept 1's name, e.g. Sequence / Stages / States}**
* * *
**{Step, rule or state 1}:** `{exact expression, threshold or value}`
{One plain-language line explaining it.}
* * *
**{Step, rule or state 2}:** `{exact expression, threshold or value}`
{One plain-language line explaining it — or the skip convention, written as an
exact token in backticks, when this requirement opts out of this step.}
* * *
**{Step, rule or state 3}:** `{exact expression, or the opt-out token}`
{What happens when everything before it is exhausted.}
* * *

{Optional one-line summary of the rule shape, followed by a short numbered list
when the shape benefits from being restated plainly.}

Which means that:
*   {Hard guarantee stated from the user's view}
*   {Behavior when the normal path comes up short}
*   {Trade-off the requirement accepts, e.g. fewer items rather than a broken promise}

**Acceptance criteria**

**Scenario:** {Normal path in a few words}
*   **Given** {precondition, with exact expressions in `backticks`}
*   **When** {the user action or system event}
*   **Then** {the observable outcome}
*   **And** {additional expectation, only when needed}

**Scenario:** {Degraded, exception or short-supply path}
*   **Given** {the shortfall or exception precondition}
*   **When** {the degradation, exception or fallback trigger}
*   **Then** {the widened or fallback behavior, stated exactly}

**Scenario:** {The hard guarantee}
*   **Given** {the boundary condition}
*   **When** {every tier has been tried}
*   **Then** {the never/always promise the requirement exists to keep}
* * *

2\. **{Next requirement}**
`({technical identifier})`
* * *
{Repeat the same block: Task(s), Story, prose, spec block, Which means that,
Acceptance criteria. Every requirement inherits the shared machinery above, so
only state what differs here. Keep each block self-contained.}
* * *
##   

## Definition of Done
* * *
Verify for every requirement above before its task closes:
*   [ ] The requirement's acceptance criteria all pass against {the live system or realistic data}
*   [ ] Unit and integration tests added covering {each shared-mechanism step or state and each hard guarantee}; CI green
*   [ ] Reviewed by a second engineer
*   [ ] {Platform bar, e.g. performance within tolerance, or accessibility on the affected surfaces}
*   [ ] Deployed to {staging or equivalent} and verified with production-shaped data
```

## Filling notes

- Write the **"How {mechanism} works"** section once and let every requirement lean on it. If a requirement re-explains the mechanism instead of inheriting it, move that explanation up into the shared section. If there is genuinely nothing shared to write there, you are on the wrong tier — use Medium.
- Name the spec block after Shared concept 1 and give each requirement its own exact values for the shared steps. **When your mechanism is a rule ladder** (the exemplar's case), the proven three-row shape is **Primary** (the rule at full strength), **Relaxed** (how it widens, possibly in multiple steps written `` `≤ 14d`, then `≤ 21d` ``), and **Final fallback** (the plain production sort that replaces the rule — a single-column database order like `created_at DESC`, no weights, no scoring). Other mechanisms define their own row names; keep them identical across requirements.
- When a requirement opts out of a shared step, write the opt-out as an exact backticked token, the way the exemplar uses **`no_relaxation`** (the rule never loosens) and **`no_fallback`** (a failing item is simply excluded). When every optional step is opted out, the requirement is a pure hard rule; let the "Which means that" and the scenarios carry the "shows fewer items instead of breaking the promise" trade-off.
- The epic-level **User Story** carries the promise bullets; the per-requirement **Story:** line narrows the same promise to one part. Both use the Connextra role/capability/value shape.
- Keep "Which means that" and "Acceptance criteria" as separate blocks: the first explains implications in prose-bullets, the second is the checkable contract. They overlap on purpose; they read differently.
- Three scenarios per requirement is the sweet spot: normal path, degraded path, hard guarantee. For a `no_relaxation` / `no_fallback` requirement the middle scenario becomes "either filter fails → never appears" and the third becomes "a short pool never degrades relevance — shows fewer deals instead". Keep each scenario at three to five steps with an observable outcome; use **And** sparingly.
- Number requirements with the escaped-dot form (`1\.`) that ClickUp exports use, and mark **at most one** requirement `← PRIO` — the one that leads the work. Never more than one per document.
- Preserve technical identifiers exactly (URLs, field names, thresholds, sort expressions), even when they look misspelled; flag oddities in prose instead of normalizing them.
- The Definition of Ready is a living gate: check each box as it becomes true, leave unmet boxes unchecked. Sizing is usually the last open box. Keep DoR and DoD document-level; split per requirement only when requirements go into different sprints, and keep each copy just as short.

## Sources

- `../scratch/Story - Fv2.5 - Feed Function - Rulesets (conventional rewrite).md` — the reviewed exemplar this tier maps onto 1:1 (shared "How rulesets work" section with Sequence and Degradation, per-ruleset Sequence blocks, the `← PRIO` marker, `no_relaxation` / `no_fallback` conventions).
- `barter-story-template.md` — the chooser and the shared principles this tier inherits.
- `barter-story-template-medium.md` — the tier below; Complex is Medium plus the "How {mechanism} works" section and degradation-style spec blocks.
- `barter-story-template-simple.md` — the tier for a single small change.
- `connextra-user-story.md` — the Story-line shape (role / capability / value).
- `gherkin-acceptance-criteria.md` — the Given/When/Then logic and the 3-5-step, observable-outcome guidance the scenario bullets follow.
- `definition-ready-done.md` — the Definition of Ready and Definition of Done brackets, trimmed to document level.
