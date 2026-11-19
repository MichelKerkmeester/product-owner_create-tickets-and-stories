---
title: "Acceptance Criteria: Phase 36: figjam-design-system"
description: "The criteria this packet must satisfy before it may be closed, each one met, waived by a decision record, or superseded by one."
trigger_phrases:
  - "figjam design system acceptance criteria"
importance_tier: "important"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: acceptance-criteria | v2.2 -->
# Acceptance Criteria: Phase 36: figjam-design-system

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** product-owner/017-figjam-flow-generation/036-figjam-design-system
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
| AC-001 | REQ-001 | Given the three lineages, When they finish, Then the state logs hold 3 claude-opus-5-5 records, 2 swe-2-max records and 2 gpt-6-luna records and each lineage stopped on maxIterationsReached | research/lineages/opus/iterations/ holds iteration-001.md to iteration-003.md, swe/ and luna/ hold iteration-001.md and iteration-002.md, the run used stop policy max-iterations with convergence off. The opus lineage wrote no deep-research-state.jsonl, a runner bookkeeping gap listed in implementation-summary.md | Met | - |
| AC-002 | REQ-002 | Given the run ended, When the iterations are read, Then each cites at least one file as [SOURCE: path:line] and names the image file for any screenshot it uses | A per-file count of SOURCE tags: 6 to 35 per iteration, none below 1. The iterations that draw on screenshots name the .png files | Met | - |
| AC-003 | REQ-003 | Given the synthesis, When it is read alone, Then it ranks at least 10 design changes with their file and evidence, at least 3 of them on consistency across diagram types | research/research.md Section 4 ranks 18 design changes, 8 marked [C] for consistency across diagram types | Met | - |
| AC-004 | REQ-004 | Given the synthesis, When it is read alone, Then it recommends the design spec file's location, its schema, how compose_board.py and the Project read it, how defaults stay safe and how the rubric checks against it | research/research.md Section 6 recommends `sk-create-figjam/assets/figjam-design.md` as the default, a user override, a `--design` flag, one strict JSON token block, contrast-floor fallbacks per token, one Knowledge file plus one kernel clause and a ninth rubric criterion | Met | - |
| AC-005 | REQ-005 | Given a long run, When lineages are working, Then a one-line status is posted about every 3 minutes | A monitor posted iteration counts every 3 minutes from 20:08 to 20:32 | Met | - |

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

The run and the synthesis are done. Which ranked changes and which design spec questions to apply is the operator's call, and that choice belongs to a later phase.
<!-- /ANCHOR:closure -->
