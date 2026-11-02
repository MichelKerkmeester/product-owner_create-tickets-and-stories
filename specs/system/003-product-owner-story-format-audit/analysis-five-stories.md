---
title: "Analysis: Five Barter Stories vs Story Mode Standard"
description: "Per-story evidence appendix for the Product Owner Story Format Audit: format deviations classified as template-gap, story-defect, or legitimate variant, plus content defects, strengths, and reusable patterns."
contextType: "reference"
---

# Analysis: Five Barter Stories vs Story Mode Standard

Evidence backing `spec.md`. Each story is read against the sk-product-owner Story Mode standard. The key column is **classification**: whether a divergence signals the template is out of sync (`template-gap`), the story broke a sound rule (`story-defect`), or the standard should simply acknowledge a legitimate variant (`variant`). The dominant classification per story tells you whether to refine the story or touch the guidelines.

A cross-cutting fact frames all five: they are refinement inputs in the team's ClickUp house format (`### About` / `### Requirements` with per-requirement `**Checklist**` blocks / `### Acceptance criteria` as numbered Given/When/Then with a per-criterion `- [ ] Mark as done` checkbox). Story Mode section 4 would preserve that surface and add missing elements in place, so the house-surface deviations are expected, not faults.

---

## 1. promo — BO - Fv2.5 - Promo's - Country Specific Targeting

Type: buildable. On-disk H1: `gfdgdfgfd`. Title conforms: no. Acceptance criteria: 12, thorough.

Deviation classification tally: story-defect 6, variant 2, template-gap 2.

Content defects (refine the story):

- **High.** H1 is the placeholder `gfdgdfgfd`. In ClickUp this renders as no title. The doc is an unfinished draft.
- **Medium.** Orphaned acceptance criterion. AC 9 "Record a skipped promo" asserts skip logging so the team can later confirm reach, but no requirement or checklist item covers skip logging. Acceptance without a backing requirement.
- **Low.** `Promo` and `promo` used interchangeably, sometimes in one requirement.
- **Low.** Anglo-Dutch plural `promo's` used for the English plural throughout, while the acceptance section uses `promos` ("four promos"). Internally inconsistent.
- **Low.** Terminology drift for one surface: "feed pattern manager", "feed pattern builder", "Feed Manager", "feed block list".
- **Low.** Stray leading space before the Solution paragraph.

Strengths:

- Genuinely thorough acceptance criteria: normal paths, the deal-inherit default, manual override, the migration case, both location edges (current-location match and mismatch-with-collapse), the unknown-location home fallback, and both nested-block behaviors, with a standalone-unaffected guard.
- Sound migration thinking baked in: existing promos stay global until the team opts in.
- Concrete problem framing with real examples ("a Dutch-only campaign promo still shows to German, Belgian and other creators").
- The user story carries a well-judged negative constraint ("I don't want a separate feed block per country, otherwise it adds promo bloat").
- Human Voice clean.

Reusable patterns surfaced here: inherit-from-linked-entity with manual override; current-location match with home-country fallback; a backward-compatibility migration guarantee; a one-of-N variant container. These are good product patterns; they do not need to become template snippets (see spec, declined list).

---

## 2. metrics — BE - Managed Partners - Automate IG & TT Metric Collection

Type: spike-research. On-disk H1: conforms. Acceptance criteria: 3, adequate for a spike.

Deviation classification tally: template-gap 7, story-defect 2, variant 2.

This is the one story where a real coverage question sits, because it is a feasibility spike and the three-tier model assumes buildable, testable behavior. The high template-gap count reflects that the create scaffold has no shape for decide/confirm/document work. The spec resolves this with a routing pointer (E3), not a new tier.

Content defects (refine the story):

- **Medium.** The user story block states no value clause. It lists a Given/When/Then mechanism instead of why the campaign team needs it. This is the "user story written as GWT" category error. The fix is a Connextra line with a real "so that", or explicit reframing as a spike whose acceptance is a documented decision.
- **Low.** "Ask Product to supply a Instagram and TikTok video link" should read "an Instagram".
- **Low.** Heading "Test and Collect the metrics from a video link" capitalizes "Collect" mid-heading (sentence-case violation).
- **Low.** Awkward comma in "Collect links from product, to an Instagram video and a TikTok video".

Strengths:

- Honest, low-spin framing: openly states it does not commit to an approach yet because feasibility per platform still needs backend review. This is exactly right for a spike.
- The "if possible or relevant" grouping separates certain deliverables from feasibility-contingent ones rather than over-promising all five metrics.
- Acceptance criteria trace cleanly to requirements and stay outcome-observable; AC3's "with unavailable metrics identified" honestly scopes for partial platform support.
- Clean ClickUp grammar and Human Voice.

---

## 3. search — BO - Managed Partners - Better 'Creator' Search

Type: buildable. On-disk H1: conforms exactly. Acceptance criteria: 10, thorough.

Deviation classification tally: story-defect 12, variant 3.

The high story-defect count is mostly the per-requirement implementation `**Checklist**` blocks measured against the create scaffold. On refinement those checklists are the one house element that should be reworked into spec blocks or dropped, since they are Task-Mode content. Everything else is preserved.

Content defects (refine the story):

- **Medium.** Gender is declared multi-select but acceptance 4 only tests a single gender value, and the checklist still holds the open question "confirm the exact list of gender options". An unresolved decision is buried in a build task.
- **Low.** City is missing from the user-story promise block, though it is a full requirement with its own acceptance criteria.
- **Low.** City checklist duplicates the column task ("Add a City column..." and "Add city column and show it by default..." are the same work).
- **Low.** Acceptance omits a max-only age scenario and an invalid-range (min greater than max) scenario, though the checklist allows leaving either side blank.
- **Low.** City has no "no city set drops out only when the filter is active" criterion, though the checklist asserts that guarantee. The same untested guarantee exists for interest.
- **Low.** Backend-existence unknowns are hedged inside build tasks ("if it does not already exist") with no Definition of Ready to surface them as dependencies.

Strengths:

- Title conforms exactly to `Story - {Area} - {Feature} - {Name}`.
- Overview narrative is coherent: four concrete failures map one-to-one onto five concrete filters.
- Acceptance criteria show real edge thinking: open-ended age, combine-to-narrow, an empty state that keeps filter pills, independent single-filter clear.
- Correct ClickUp grammar and Human Voice.

---

## 4. reject — BO - Managed Partners - Creator App Approval - Reject Reasons

Type: buildable. On-disk H1: conforms. Acceptance criteria: 7, thorough.

Deviation classification tally: story-defect 8, variant 3.

Reads as a story half-merged with a task: a strong narrative Overview and acceptance set wrapped around two build checklists. The two requirements share one mechanism (the reject form triggers the event; the event drives the email), so under the create rules this is a Complex-tier candidate with a "How the rejection event works" section. That is a create-time observation, not a refinement instruction.

Content defects (refine the story):

- **Medium.** Multi-vs-single reason-select ambiguity. AC6 and AC7 say "at least one reason is selected" and "the selected reasons render" (plural, multi-select), but requirement 1 describes "a reason selector with 4 reasons" without pinning cardinality.
- **Low.** Optional-message trigger is inconsistent. Requirement 1 says the message area is triggered when "Other" is selected; AC4 and AC6 treat the message as generally optional regardless.
- **Low.** Field-name casing mix left unflagged: `rejection_reasons` (snake_case) beside `RejectionMessage` (PascalCase) in the same criterion. The standard says preserve identifiers exactly but flag the oddity in prose.
- **Low.** Double-word typo "like the the Partner App".
- **Low.** The About paragraph and the final Problem bullet repeat the same "clutter an already busy inbox" sentence almost verbatim.
- **Low.** Stray space before colon ("with 4 reasons :") and irregular nested-list indentation in the reason-selector checklist item.

Strengths:

- Disciplined backticks on every exact token: the event name, both statuses, and the reason values.
- A real idempotency guarantee ("retries or event replays do not send a second email").
- Governing references wired in: the ClickUp Account catalog entry A1 and the Figma email design.
- Preserves the European-notation threshold `Below 2.500 followers` verbatim rather than silently normalizing it.

---

## 5. push — BO - Notifications - Push Messages - Scheduling & Targeting

Type: buildable. On-disk H1: `push messages`. Title conforms: no. Acceptance criteria: 8, adequate.

Deviation classification tally: story-defect 8, variant 3, template-gap 2.

Three requirements share one draft/send lifecycle (draft, scheduled, sending/locked, sent; editable and cancellable until send starts; edit returns to draft; audit trail). Under the create rules this is a Complex-tier candidate with a "How the send lifecycle works" section. Again, a create observation.

Content defects (refine the story):

- **High-ish.** Non-conforming H1 `push messages`. Should be `Story - BO - Notifications - Push Messages - Scheduling & Targeting`.
- **Medium.** The widen-not-narrow targeting semantics (more countries widen, more values widen, empty filter equals everyone, selecting every value equals empty) are specified in the checklist but under-tested in acceptance. This is novel, counter-intuitive behavior and deserves explicit scenarios.
- **Medium.** "Put an edited send back to a draft" has no acceptance scenario, though cancel, lock, save, and schedule each do.
- **Low.** "Show the chosen time in the user's own timezone" has no acceptance coverage.
- **Low.** Heading "Draft System" is title case; house and voice style want "Draft system".

Strengths:

- Well-formed Connextra promise block with proper "I want X so that Y" for all four capabilities.
- Clear Problem/Solution grounded in real workflow pain (tied to the screen at send time, no way to catch a typo, no draft state).
- Preserves the current default (an unfiltered send reaches everyone) and requires an audit trail of who cancelled or edited and when.
- Honest scoping preamble ("discuss and rescope any that cannot be met").

---

## Cross-cutting observations the completeness pass added

- **Category error.** Almost every recorded deviation measures a refinement input against the create scaffold. Under section 4 refinement, the house surface is preserved, which collapses most deviations to non-issues.
- **A real internal conflict in the standard.** The Step-4 export gate counts `**Scenario:**` headings, but refinement preserves numbered house AC blocks that contain zero such headings. This is the strongest finding and is independent of the sample. It is E1 in the spec.
- **The scenario-per-requirement count invariant was never applied.** Under `story-templates.md` line 27 (Simple one or two total; Medium and Complex three per requirement), "search" (10 AC across 5 filters) and "metrics" (3 AC across 3 requirements) would not map to the create counts. This is another reason the create invariants should be stated as create-time only.
- **The worked examples are decisive on the H1 slot.** They fill `{Version/Area}` with a product or workspace name, not a `BO/BE/FE` code. The real Barter stories use a platform code plus a version tag. Three interpretations, no definition. This is E2 in the spec.
- **Shared provenance inflates recurrence.** Three stories (metrics, search, reject) are a Managed Partners cluster sharing one copied ClickUp doc template. "Appears in 5/5" is closer to "one template, copied" and should not be read as five authors independently converging on a need.
