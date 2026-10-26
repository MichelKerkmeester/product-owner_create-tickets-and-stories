---
title: "Acceptance Criteria: Phase 38: figjam-model-comparison"
description: "The criteria this packet must satisfy before it may be closed, each one met, waived by a decision record or superseded by one."
trigger_phrases:
  - "figjam model comparison acceptance criteria"
importance_tier: "important"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: acceptance-criteria | v2.2 -->
# Acceptance Criteria: Phase 38: figjam-model-comparison

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** product-owner/017-figjam-flow-generation/038-figjam-model-comparison
**Level:** 2
**Status:** Complete
**Date:** 2026-10-25
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:criteria -->
## 2. CRITERIA

One row per criterion. `AC-ID` is stable once written: supersede a criterion, never renumber it.

| AC-ID | REQ | Given / When / Then | Verification | Status | Waiver |
|-------|-----|---------------------|--------------|--------|--------|
| AC-001 | REQ-001 | Given the driver and the three models, When the batch finishes, Then each of the 21 runs has its replies, tool calls and `meta.json` in the run folder and ran alone on the fictional test file | 21 `meta.json` files with `completed: true` under `skill/`, every turn's `response_models` naming the model asked for, and `batch.log` showing one run at a time | Met | - |
| AC-002 | REQ-002 | Given every written board, When it is graded, Then it has an overview, a 100% and a greyscale render and a 22-point scorecard from a grader that is none of the three models, with Clarity from a fresh reader | 23 overview, 23 full and 23 greyscale renders, seven Sonnet 5.5 grader files in `grades/` and three reader answer files scored against `grades/reader-key.md` | Met | - |
| AC-003 | REQ-003 | Given the run folder and every changed file, When they are scanned, Then no board URL, Figma file key, plan name or email appears | The leak scan read 0 hits on each scenario commit, on `grades/` and `results.jsonl` and on every changed file, apart from the repository owner's name in the root README's existing badges | Met | - |
| AC-004 | REQ-004 | Given `results.jsonl`, When the gallery rule picks the best board per type, Then each of the seven type images is that board and its caption names the scenario, the model and the score | The seven images are the `gallery: true` rows of `results.jsonl`, and `assets/screenshots/README.md` names the scenario, the model and the score for each | Met | - |
| AC-005 | REQ-005 | Given the graded runs, When the run README is read, Then it says which model draws boards best per type and overall, with the losses that decided it | The run README's Verdict and Results sections, with the deciding losses per model and per type | Met | - |

### Status values

| Value | Meaning |
|-------|---------|
| `Met` | Verified. The Verification cell names evidence that was actually observed. |
| `Unmet` | Not yet satisfied. Blocks closure. |
| `Waived` | Deliberately not pursued. Requires an ADR in the Waiver cell. |
| `Superseded` | Replaced by a different criterion or decision. Requires an ADR in the Waiver cell. |

### Waiver cell

Write `-` when the row is `Met` or `Unmet`. Write `ADR-NNN` when the row is
`Waived` or `Superseded`, naming a decision record that exists in
`decision-record.md`. A waiver naming an ADR that is not there fails validation:
the point of a waiver is that someone recorded the reasoning, so an unbacked
waiver is treated as an unmet criterion rather than as a pass.
<!-- /ANCHOR:criteria -->

---

<!-- ANCHOR:closure -->
## 3. CLOSURE STATEMENT

**Closeable:** Yes

Every criterion is Met. The 21 runs finished, every board was graded by a neutral grader, the gallery holds the best board per type and the run README names the recommended model with the losses that decided it.
<!-- /ANCHOR:closure -->
