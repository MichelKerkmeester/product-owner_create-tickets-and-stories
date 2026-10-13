---
title: "Tasks: Product Owner Story Format Audit"
description: "Follow-up actions split into story refinements (no guideline change), warranted standard edits, and two owner-decision forks."
contextType: "reference"
importance_tier: "normal"
level: 1
---

# Tasks: Product Owner Story Format Audit

Three tracks. Track A needs no guideline change and can start now. Track B is a small, owner-gated standard edit. Track C is two decisions only the owner can make.

## Track A — Refine the five stories (no guideline change)

Run each as a Story Mode refinement, which preserves the house structure and fixes content in place. Do not restructure the narrative.

- [ ] **promo.** Replace the placeholder H1 `gfdgdfgfd` with `Story - BO - Fv2.5 - Promo's - Country Specific Targeting`. Add a requirement covering the skip logging that AC 9 assumes, or drop AC 9. Settle Promo vs promo and the promo's vs promos plural. Pick one name for the pattern-management surface.
- [ ] **metrics.** Rewrite the user story with a value clause, or reframe it explicitly as a spike whose acceptance is a documented decision. Fix "a Instagram" and the mid-heading capital in "Test and Collect".
- [ ] **search.** Pin gender cardinality and resolve or surface the "confirm gender options" open question out of the build checklist. Add city to the promise block. De-duplicate the city-column task. Add max-only and invalid-range age scenarios, and the city null-drop criterion.
- [ ] **reject.** Pin reason-select cardinality (single vs multi) consistently across requirement and acceptance. Reconcile the optional-message trigger. Flag the `rejection_reasons` / `RejectionMessage` casing mix in prose. Fix "the the".
- [ ] **push.** Replace the H1 `push messages` with `Story - BO - Notifications - Push Messages - Scheduling & Targeting`. Add scenarios for the widen-not-narrow targeting semantics, edit-returns-to-draft, and timezone display. Lowercase "Draft system".

## Track B — Warranted standard edits (owner-gated, small)

Apply to `sk-product-owner/`, then propagate to the three worked examples, `SKILL.md` NEVER rule 14, and the Claude Project mirror per `SYNC.md`.

- [ ] **E1 (do this first, independent of C).** In `story-mode.md` Step 4 and `story-templates.md` line 27, state that the `**Scenario:**` count and heading gates are create-time invariants and do not fire on a source-preserving refinement. This removes a real self-contradiction in the standard.
- [ ] **E2.** Annotate the H1 `{Version/Area}` slot with the intended convention and one real example. Do not freeze `BO/BE/FE` as a closed set. Make the three worked examples agree with the chosen convention.
- [ ] **E3.** Add one sentence in `story-mode.md` section 1 and section 7 routing decide/confirm/document work with no buildable behavior to Task Mode, or Doc Mode for a written recommendation. No new tier.

## Track C — Owner decision forks

- [ ] **F1. Per-acceptance-criterion "Mark as done" checkbox.** All five stories use it; the standard is silent. Decide: (a) bless it as an optional check-off on the Scenario scaffold, or (b) strip it on export. Then encode the decision so it stops resurfacing.
- [ ] **F2. Should spikes live on the story surface at all.** Only open this if you want spikes to carry story-style acceptance framing. Options: Task, Doc, or a first-class labelled Discovery story with relaxed machinery. If left closed, the E3 pointer is sufficient.

## Sequencing

1. Track A can proceed immediately; it validates the "refine, do not re-guideline" verdict on real drafts.
2. E1 can proceed immediately; it is independent of the two forks.
3. E2 and E3 proceed once the owner confirms the H1 convention and the spike-routing target.
4. F1 and F2 gate any further template change. Nothing else in Track B depends on them.
