---
title: "Barter Story Template — Medium Tier (Two to Four Independent Requirements)"
description: "The house story scaffold for a feature with two to four requirements that share no machinery: full Overview with promise bullets, Definition of Ready, per-requirement blocks with Story line, spec block, Which-means-that, and three Given/When/Then scenarios, and a Definition of Done."
---

# Barter Story Template — Medium

## When to use it

Use this for a Barter story that covers **two to four requirements** in one feature area, where each requirement will become (or already has) its own implementation task, and the requirements are **independent** — they do not share a common mechanism, sequence, or degradation ladder that has to be described once and inherited by all of them.

Pick a different tier when:

- You have **one requirement and a small change** → use [`barter-story-template-simple.md`](barter-story-template-simple.md).
- Your requirements **share the same machinery** — a shared pipeline, an ordered rule ladder, a state machine, a matching lifecycle — that would otherwise be re-explained in every block → use [`barter-story-template-complex.md`](barter-story-template-complex.md).

What Medium deliberately drops relative to Complex:

- The **"How {mechanism} works"** shared-mechanics section and its shared-concept subsections. At this tier requirements stand alone, so there is nothing shared to hoist above them.
- The single inline **`← PRIO`** marker. Medium requirements are independent peers; when one truly must be called out as leading the work, say so in that requirement's prose — and if requirements are competing because they share one mechanism, that is a signal to move up to Complex.

What Medium keeps (everything else): the full Overview with promise bullets, the Definition of Ready checklist, per-requirement blocks (Story line, prose, spec block, "Which means that", three scenarios), and the Definition of Done.

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
{One sentence: the mechanism that closes the gap}.

**Documentation**
[{link to the governing doc}]({url})
##   

## Definition of Ready
* * *
Check off as met; pull requirements into a sprint only when every box is checked:
*   [ ] Every requirement's Story line is written in the Connextra form with a clear value clause
*   [ ] Acceptance criteria present and testable for every requirement
*   [ ] Dependencies identified ({e.g. the service or API this relies on is live})
*   [ ] Sized by the team and each requirement fits comfortably in a sprint
##   

## Requirements
* * *
1\. **{Requirement name}**
`({technical identifier, e.g. endpoint or field name})`
* * *
**Task(s):** [{task number and name}]({task file or ticket link})
* * *
**Story:** As a {user role} {using this specific part}, I want {capability},
so that {the benefit in the user's terms}.

{Two or three lines of prose: what the user expects here, what breaks that
expectation, and what this requirement does about it.}

**{Spec block name, e.g. Rule}**
* * *
**{Step or rule 1}:** `{exact expression or threshold}`
{One plain-language line explaining it.}
* * *
**{Step or rule 2}:** `{exact expression or threshold}`
{One plain-language line explaining it.}
* * *

{Optional one-line summary of the rule shape.}

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

**Scenario:** {Degraded or short-supply path}
*   **Given** {the shortfall precondition}
*   **When** {the degradation or fallback trigger}
*   **Then** {the widened or fallback behavior, stated exactly}

**Scenario:** {The hard guarantee}
*   **Given** {the boundary condition}
*   **When** {the final state}
*   **Then** {the never/always promise the requirement exists to keep}
* * *

2\. **{Next requirement}**
`({technical identifier})`
* * *
{Repeat the same block: Task(s), Story, prose, spec block, Which means that,
Acceptance criteria. Keep every requirement self-contained.}
* * *
##   

## Definition of Done
* * *
Verify for every requirement above before its task closes:
*   [ ] The requirement's acceptance criteria all pass against {the live system or realistic data}
*   [ ] Unit and integration tests added covering {each rule / each guarantee stated above}; CI green
*   [ ] Reviewed by a second engineer
*   [ ] {Platform bar, e.g. accessible (keyboard + screen reader) on mobile and desktop, or performance within tolerance}
*   [ ] Deployed to {staging or equivalent} and verified with production-shaped data
```

## Filling notes

- The epic-level **User Story** in the Overview carries the promise bullets; the per-requirement **Story:** line narrows the same promise to one part. Both use the Connextra role/capability/value shape.
- Keep "Which means that" and "Acceptance criteria" as separate blocks: the first explains implications in prose-bullets, the second is the checkable contract. They overlap on purpose; they read differently.
- Three scenarios per requirement is the sweet spot: normal path, degraded path, hard guarantee. Add a fourth only when a requirement has a genuinely separate edge. Keep each scenario at three to five steps with an observable outcome, per the Gherkin guidance; use **And** sparingly for a second precondition or expectation.
- Number requirements with the escaped-dot form (`1\.`) that ClickUp exports use.
- When a requirement has no degradation (the rule never loosens), state it explicitly in the spec block (`no_relaxation`, `no_fallback`) and let the acceptance criteria carry the "shows fewer items instead" trade-off.
- The Definition of Ready is a living gate, not decoration: check each box as it becomes true (a fully checked DoR reads "met — pulled in"), and leave unmet boxes unchecked so it is obvious why the story is still in refinement. Sizing is usually the last open box.
- Keep DoR and DoD document-level by default. Split them per requirement only when requirements are pulled into different sprints, and then keep each copy just as short.
- If, while filling, you find every requirement re-stating the same sequence or degradation behavior, stop and move up to the Complex tier — that repetition is exactly what the "How {mechanism} works" section exists to absorb.

## Sources

- `../scratch/Story - Fv2.5 - Feed Function - Rulesets (conventional rewrite).md` — the reviewed exemplar this template generalizes.
- `barter-story-template.md` — the chooser and the shared principles this tier inherits; Medium holds what was the base scaffold.
- `barter-story-template-simple.md` — the tier below (one requirement).
- `barter-story-template-complex.md` — the tier above (shared machinery), which is Medium plus the "How {mechanism} works" section.
- `connextra-user-story.md` — the Story-line shape (role / capability / value).
- `gherkin-acceptance-criteria.md` — the Given/When/Then logic and the 3-5-step, observable-outcome guidance the scenario bullets follow.
- `definition-ready-done.md` — the Definition of Ready and Definition of Done brackets, trimmed to document level.
