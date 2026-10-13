---
title: "Spec: Product Owner Story Format Audit"
description: "Adversarial audit of five real Barter ClickUp stories against the Product Owner Story Mode standard, and an honest verdict on whether the story-creation rules, guidelines, and templates need updating."
trigger_phrases:
  - "product owner story format audit"
  - "story mode template update"
  - "story house format reconciliation"
  - "five story analysis"
importance_tier: "high"
contextType: "specification"
_memory:
  continuity:
    packet_pointer: "003-product-owner-story-format-audit"
    last_updated_at: "2026-07-22T17:30:00Z"
    last_updated_by: "claude"
    recent_action: "Ran a 28-agent adversarial workflow over five real ClickUp stories vs the Story Mode standard, adjudicated 19 candidate template changes down to a small warranted set plus two owner-decision forks"
    next_safe_action: "Owner rules on the two decision forks (per-AC checkbox status, spike-on-story-surface policy); then apply the three warranted standard edits with example + SKILL.md propagation"
---
<!-- SPECKIT_LEVEL: 1 -->
# Spec: Product Owner Story Format Audit

## Headline verdict

The story-creation guidelines and templates largely do **not** need updating. The five audited stories need refinement.

Most of what looks like "the template is out of date" is an artifact of the comparison: the five stories are pre-existing ClickUp house drafts (refinement **inputs**, one literally titled `gfdgdfgfd`), not Story Mode create **outputs**. Story Mode's own refinement rule (`story-mode.md` section 4) would already preserve their house shape and add the missing conventional elements in place, so most "format deviations" are non-issues by design. The remainder are ordinary content defects the standard already forbids (malformed titles, an orphaned acceptance criterion, a value-less user story, typos), fixable by refining the drafts with zero guideline change.

An adversarial panel took 19 proposed template changes and rejected 13. A completeness pass then narrowed the survivors further and surfaced the single most valuable finding, which no earlier agent saw: a real **internal contradiction inside the standard itself**, independent of the five stories. That, plus two near-zero-cost clarifications and two genuine owner-decision forks, is the entire warranted scope.

## What this covers

Two things the owner asked for:

1. An analysis of five stories:
   - `Story - BO - Fv2.5 - Promo's - Country Specific Targeting`
   - `Story - BE - Managed Partners - Automate IG & TT Metric Collection`
   - `Story - BO - Managed Partners - Better 'Creator' Search`
   - `Story - BO - Managed Partners - Creator App Approval - Reject Reasons`
   - `Story - BO - Notifications - Push Messages - Scheduling & Targeting`
2. A judgment on whether the story-creation rules, guidelines, and templates in `Product Owner/` should change.

The standard under audit is the sk-product-owner Story Mode surface:

- `sk-product-owner/references/story-mode.md` (v0.103) — workflow, tier intelligence, refinement fidelity
- `sk-product-owner/assets/story-templates.md` (v0.102) — Simple / Medium / Complex scaffolds
- `sk-product-owner/SKILL.md` (v0.5.0) — router and global ALWAYS/NEVER rules
- `sk-product-owner/assets/examples/story/` — three worked examples
- `sk-product-owner/references/human-voice-rules.md` (v0.210) — global voice rules

The full per-story evidence lives in `analysis-five-stories.md`. The actionable follow-ups live in `tasks.md`.

## Method

An adversarial multi-agent workflow, chosen to guard against the obvious failure mode of an audit like this: talking yourself into changing the skill to match a small sample.

- **Analyze** — five independent agents, one per story, each classifying every format deviation as `template-gap`, `story-defect`, or `either-legitimate-variant`.
- **Synthesize** — three lenses over all five analyses (house-format reconciliation, missing story shapes, reusable conventions), producing 19 concrete candidate updates.
- **Challenge** — one skeptic per candidate, each required to make the strongest case against the change and check whether the standard already covers it before recommending an addition.
- **Critique** — a completeness pass asking what every prior agent missed.

28 agents, no errors. Adjudication: 1 adopt, 3 adopt-modified, 2 defer-to-user, 13 reject.

## The reframe that decides the whole question

The five stories are refinement inputs, not create outputs.

Every agent measured the drafts against the **create** scaffold, which structurally over-produces "the template must change" conclusions. But `story-mode.md` section 4 is explicit: refinement preserves the source's structure, headings, prose, and formatting, and only adds Story lines, scenarios, or gates in place. The `### About` naming, the H3 section anchors, the numbered acceptance blocks, and the per-criterion checkbox are exactly the kind of house-surface traits Story Mode would keep, not rewrite. The team already settled this once: the Fv2.5 Rulesets review rejected a full restructure of a narrative story into ticket blocks.

So the deviations sort into three piles, and only the third pile can possibly justify a guideline change:

- **Would be preserved on refinement** (no action, no guideline change): `### About` heading name, H3 anchoring, hyphen `- [ ]` markers, the ClickUp blockquote preamble, the `Mention @owner if design input needed` line.
- **Plain content defects** (refine the story, no guideline change): malformed or placeholder H1 titles, an acceptance criterion with no backing requirement, a user story with no value clause, single-vs-multi-select ambiguity, untested novel behavior, typos.
- **Genuine standard work** (the small warranted set below).

## Per-story summary

Two-column read; detail in `analysis-five-stories.md`.

| Story | Read |
| --- | --- |
| promo (Country Targeting) | Buildable, 3 loosely-independent requirements. 12 thorough acceptance criteria with real edge and migration thinking. Defects: placeholder H1 `gfdgdfgfd`; orphaned AC 9 (skip logging) with no backing requirement; Promo/promo and terminology drift. |
| metrics (IG & TT collection) | A feasibility **spike**, honestly framed ("does not commit to an approach yet"). Requirements are decide/confirm/document; acceptance asserts "documented in ClickUp". Its user story is written as Given/When/Then with no value clause, which is a category error. Cleanest fit for the "no spike home" question. |
| search (Better Creator Search) | Buildable, 5 filters. Title conforms. 10 thorough criteria. Defects: city missing from the user-story promise block; gender declared multi-select but only single-value tested with an open question still in-flight; duplicate city-column task; missing max-only and invalid-range age scenarios. |
| reject (Reject Reasons) | Buildable, well-linked (ClickUp catalog entry, Figma). Strong idempotency guarantee ("retries do not send a second email"). Defects: multi-vs-single reason-select ambiguity between requirement and AC; `rejection_reasons` / `RejectionMessage` casing mix left unflagged; "the the" typo; checklist indentation glitch. |
| push (Scheduling & Targeting) | Buildable, 3 requirements sharing one draft/send lifecycle. Well-formed Connextra promise block. Defects: non-conforming H1 `push messages`; the widen-not-narrow targeting semantics and the edit-returns-to-draft flow are specified but untested; timezone display untested; "Draft System" title-case heading. |

Recurring strengths worth stating plainly: all five are Human Voice clean (no em-dashes, no banned words, sentence-case headings, straight quotes), all carry concrete problem framing with real examples, and all trace acceptance criteria back to their requirements. This is competent product authoring. The issues are refinement polish, not a broken practice.

## Guidelines and template assessment

### Warranted standard edits (small, and mostly not about the five stories)

**E1. Resolve the export-gate vs refinement-preservation contradiction (highest value).**
`story-mode.md` Step 4 counts `**Scenario:**` headings as a blocking export gate ("Simple must have one or two... Otherwise block export"), and `story-templates.md` line 27 makes the scenario count a "blocking tier invariant". But section 4 refinement preserves source structure. A refined house story keeps its numbered bold-title acceptance blocks and therefore has **zero** `**Scenario:**` headings. Either the gate applies to refinements, in which case every preserved house story fails export, or it does not, in which case the standard never says so. This is a live self-contradiction in the standard, confirmed by direct reading, and it exists regardless of the five stories. Fix: state that the scenario-count and scenario-heading gates are create-time invariants and do not fire on a source-preserving refinement.

**E2. Say what fills the H1 `{Version/Area}` slot.**
Nothing in any file says what goes in `{Version/Area}`, so every author reverse-engineers it. Worse, the sources disagree: the three worked examples fill it with a product or workspace name (`Fieldstack Workspace`, `Lumen Consumer App`, `Northbeam Notifications`), while the real Barter stories use a platform code plus a version tag (`BO`, `BE`, `Fv2.5`). Do **not** freeze `BO/BE/FE` as a closed taxonomy on the strength of four sampled titles; the Barter workspace has more surfaces than that (Creator, Partner, Chat, Content Gallery, Notifications). Fix: annotate the slot with the intended convention and one real example, and make the three worked examples agree with whatever is chosen.

**E3. Route feasibility spikes explicitly (one pointer, not a new tier).**
The metrics story is investigation-only. The standard ejects it implicitly (via the observable-outcome scenario rule and the zero-requirements epic-brief ejector) but never says where such work goes. Fix: one sentence in `story-mode.md` section 1 and section 7 pointing decide/confirm/document work with no buildable behavior to Task Mode (or Doc Mode for a written recommendation). No fourth tier, no Discovery scaffold.

### Owner decision forks (the standard is silent or ambiguous; the owner must rule)

**F1. Per-acceptance-criterion "Mark as done" checkbox.**
All five stories append `- [ ] _Mark as done, if the criteria are met_` to each criterion. The audit brief assumed the template forbids this; on direct reading, neither file contains an explicit no-checkbox rule, so this is silence, not contradiction. A 5/5 recurring native ClickUp affordance sitting against an unstated rule is a latent ambiguity that will keep resurfacing. Decide one of: (a) bless it as an optional check-off on the Scenario scaffold, or (b) treat it as an export-time strip. Do not let it stay undefined.

**F2. Should spikes live on the story surface at all.**
E3 routes spikes away with one pointer, which is safe under either answer. But the deeper question is a product-policy fork the skill maintainer does not own: are feasibility spikes a Task, a Doc, or a first-class labelled Discovery story with relaxed machinery. Only decide this if you want spikes to carry story-style acceptance framing. Otherwise E3 is sufficient and this fork can stay closed.

### Considered and declined

The skeptic panel rejected 13 candidates; the completeness pass agreed and added the framing reason. Recorded so the discipline is visible and these do not get re-proposed:

- Absorb the house format wholesale into the template — declined; section 4 refinement already preserves it, so no scaffold change is needed.
- Add a canonical multi-select audience-filter snippet — declined; the Complex "How {mechanism} works" section is already the home for a shared filter mechanism, and the recurrence is inflated by shared-template copy-paste across three Managed Partners stories, not three independent authors converging.
- Relax `*   [ ]` checklist grammar to hyphen `- [ ]` — declined; the asterisk grammar is create-time house style and hyphen inputs are preserved on refinement anyway.
- Accept numbered bold-title AC blocks as an alternative to named `**Scenario:**` blocks — declined; that is a settled create-time decision, and refinement preserves the numbered blocks without the standard endorsing them as a create shape.
- Add a fourth Discovery tier, or a Discovery scaffold, or a guardrail that Discovery is orthogonal to tiers — declined as machinery; superseded by the E3 pointer and the F2 fork.
- Codify the `Mention @owner` line, the blockquote preamble, the "alternative suggestions welcome" notice, the "meet all AC or rescope" preamble, and H3 anchoring as conventions — declined; all are preserved on refinement by the existing catch-all, so codifying them adds bloat and protects nothing new.
- A house-draft refinement pre-flight checklist in Error Recovery — declined; five of its six items are already covered; at most fold the one genuinely new item (strip embedded implementation checklists) into E-scope if desired.

### Propagation caveat

Any adopted edit must be carried to surfaces no agent checked during synthesis: the three worked examples (especially for E2), `SKILL.md` NEVER rule 14 (the router-level refinement-fidelity rule), and the Claude Project knowledge mirror per `SYNC.md`. A change that touches Scenario, checkbox, or heading rules without updating these creates a new contradiction.

## Decisions

- **D001.** This packet is analysis and recommendation only. It does not modify any `Product Owner/` source file. Implementation is a separate, owner-gated pass, because two of the items (F1, F2) are decisions the owner must make.
- **D002.** The primary recommendation is refine the five stories, not change the guidelines. The five story-level refinement actions are enumerated in `tasks.md` and require no standard change.
- **D003.** The warranted standard edits are exactly E1, E2, E3. E1 is the strongest and is independent of the five stories; it should proceed regardless of how F1 and F2 are decided.
- **D004.** No new tier, no Discovery scaffold, and no absorption of the house format into the create scaffolds. The template family stays Simple / Medium / Complex.
- **D005.** Recurrence counts in this audit are discounted for shared origin. Three of the five stories share one copied ClickUp doc template, so "appears in N/5" overstates the mandate behind any house-format proposal.

## Verification

- E1 confirmed by direct read: `story-mode.md` Step 4 export gate and `story-templates.md` line 27 invariant vs section 4 refinement preservation.
- E2 confirmed by direct read: `{Version/Area}` appears in all three scaffolds and `story-mode.md` section 5 with no definition; the three worked examples use a product name; the real Barter stories use `BO`/`BE` plus `Fv2.5`.
- The refinement-fidelity rule is confirmed at two levels: `story-mode.md` line 129 and `SKILL.md` NEVER rule 14.
- Before any implementation pass, re-read the three worked examples and `SKILL.md` end to end so an adopted change does not introduce a fresh contradiction.

## Out of scope

- Editing the sk-product-owner skill, kernel, mirrors, or checksums (owner-gated follow-up).
- Rewriting the five stories in this packet (they live in the Barter documentation tree; refinement is a Story Mode run, tracked in `tasks.md`).
- Any other Product Owner mode (Task, Bug, Doc, Interactive).
- The ClickUp transport or push mechanics.
