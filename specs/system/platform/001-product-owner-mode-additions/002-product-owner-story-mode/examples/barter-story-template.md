---
title: "Barter Story Template — Tier Chooser and Shared Principles"
description: "The house story format proven on the Fv2.5 Feed Function Rulesets rewrite: the shared principles that survived review, plus a selection rule pointing to three copyable tier scaffolds (Simple / Medium / Complex)."
---

# Barter Story Template

## When to use it

Use this family for any Barter story document written in the house format proven on `scratch/Story - Fv2.5 - Feed Function - Rulesets (conventional rewrite).md`: the narrative-first ClickUp original, enriched with three conventional elements that survived review — a Connextra Story line per requirement, Given/When/Then acceptance-criteria scenarios per requirement, and document-level Definition of Ready and Definition of Done checklists.

This file is the **chooser** and the home of the shared principles. The copyable scaffolds live in three tier files; pick one below and fill it — each is self-contained.

## Shared principles

These were settled through review and apply to every tier:

- Narrative first. The document explains the promise, the problem, and the mechanism in prose before any structured blocks. Do not replace prose with ticket boilerplate.
- One Story line per requirement, not a ticket header block. No Type/Epic/Priority/Estimate/Status fields inside the document; priority is marked inline on the requirement name (`← PRIO`) when needed.
- Acceptance criteria are Given/When/Then scenarios written in ClickUp bullet grammar (`*   **Given** ...`), one to three per requirement with each tier's notes giving its exact count — the Gherkin logic from `gherkin-acceptance-criteria.md` without fenced feature files or ticket blocks.
- ClickUp-native grammar throughout: `* * *` dividers, `*   ` unordered bullets, `*   [ ]` checklists, numbered requirement headings, `##   ` spacer headings between major sections.
- Preserve technical identifiers exactly (URLs, field names, thresholds, sort expressions), even when they look misspelled; flag oddities in prose instead of normalizing them.
- An optional shared-mechanics section ("How {mechanism} works") sits between the Overview and the Requirements when every requirement relies on the same machinery. Drop it when requirements are independent.
- The story's life is bracketed by two gates: a **Definition of Ready** before the Requirements (checked off as each condition is met; nothing is pulled into a sprint until it holds) and a **Definition of Done** at the end (verified before any task closes). Medium and Complex carry the DoR as a checklist; Simple deliberately condenses it to a single Readiness line, which remains a gate. Acceptance criteria describe one requirement's behavior; DoR and DoD are the start/finish gates around all of them.

## Pick a tier

Choose by requirement count and whether the requirements share machinery:

- **One requirement, a small change** (single behavior, copy tweak, one rule) → [`barter-story-template-simple.md`](barter-story-template-simple.md). Leanest shape: compact Overview with a single Story line, one spec block, one or two scenarios, a one-line readiness statement, and a short Definition of Done. Drops the shared-mechanics section, the DoR checklist, and the promise bullets. A five-minute fill.
- **Two to four independent requirements**, no shared machinery → [`barter-story-template-medium.md`](barter-story-template-medium.md). The full house shape: Overview with promise bullets, Definition of Ready, per-requirement blocks (Story line, prose, spec block, "Which means that", three scenarios), Definition of Done. This is what was the base scaffold. Drops only the "How {mechanism} works" section and the PRIO marker.
- **Several requirements that share a mechanism** (a shared pipeline, an ordered rule ladder, a state machine, a matching lifecycle) → [`barter-story-template-complex.md`](barter-story-template-complex.md). Medium plus the "How {mechanism} works" section with shared-concept subsections and per-requirement spec blocks that follow the mechanism; the exemplar's degradation ladder (Primary / Relaxed / Final fallback with `no_relaxation` / `no_fallback` opt-outs) is one proven shape, and a single `← PRIO` marker calls out the leading requirement.

If you start filling a tier and it feels wrong — a Medium requirement keeps re-stating the same mechanism (move up to Complex), or a Complex "How {mechanism} works" section has nothing to say (drop to Medium) — switch tiers rather than bending the scaffold.

## Sources

- `../scratch/Story - Fv2.5 - Feed Function - Rulesets (conventional rewrite).md` — the reviewed exemplar this family generalizes.
- `barter-story-template-simple.md`, `barter-story-template-medium.md`, `barter-story-template-complex.md` — the three copyable tier scaffolds.
- `connextra-user-story.md` — the Story-line shape (role / capability / value).
- `gherkin-acceptance-criteria.md` — the Given/When/Then logic and the 3-5-step, observable-outcome guidance the scenario bullets follow.
- `definition-ready-done.md` — the Definition of Ready and Definition of Done brackets, trimmed to document level.
