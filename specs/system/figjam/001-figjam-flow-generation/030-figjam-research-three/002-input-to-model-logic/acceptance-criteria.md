---
title: "Acceptance Criteria: Phase 2: Input to model logic research"
description: "The criteria this packet must satisfy before it may be closed, each one met, waived by a decision record, or superseded by one."
trigger_phrases:
  - "input to model logic research acceptance criteria"
importance_tier: "important"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: acceptance-criteria | v2.2 -->
# Acceptance Criteria: Phase 2: Input to model logic research

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** product-owner/017-figjam-flow-generation/030-figjam-research-three/002-input-to-model-logic
**Level:** 2
**Status:** Complete
**Date:** 2026-10-21
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:criteria -->
## 2. CRITERIA

One row per criterion. `AC-ID` is stable once written: supersede a criterion, never renumber it.

| AC-ID | REQ | Given / When / Then | Verification | Status | Waiver |
|-------|-----|---------------------|--------------|--------|--------|
| AC-001 | REQ-001 | Given the DeepSeek lineage, When the 5 iterations finish, Then the state log holds 5 iteration records and the run stopped on maxIterationsReached | research/lineages/deepseek/deep-research-state.jsonl holds 5 iteration records with stopReason maxIterationsReached, fanout exit 0 | Met | - |
| AC-002 | REQ-002 | Given the run ended, When the iterations are read, Then iteration-001.md to iteration-005.md exist and each cites at least one source | iteration-001.md to iteration-005.md exist and cite 13 to 29 sources each, none below 1 | Met | - |
| AC-003 | REQ-003 | Given the iterations, When the DeepSeek synthesis worker runs, Then research/research.md lists every claim it dropped or corrected | Section 5 lists 11 dropped or corrected iteration claims. All 105 local citations resolve to an existing file and line, and the orchestrator read the top cited lines against their claims | Met | - |
| AC-004 | REQ-004 | Given the synthesis, When it is read alone, Then research/research.md ranks at least 8 changes to how inputs become a model, each naming the Product Owner file it changes and the source it comes from | Section 3 ranks 12 changes, each with Changes, Comes from, The gap, What changes, Effort and Mirror or kernel | Met | - |
| AC-005 | REQ-005 | Given a long run, When agents are working, Then a one-line status is posted about every 3 minutes | Status lines in the session from 08:22 to 08:39 | Met | - |

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

Every row is Met with the evidence named in its Verification cell.
<!-- /ANCHOR:closure -->
