---
title: "Acceptance Criteria: Phase 16: figjam-improvement-research"
description: "The criteria this packet must satisfy before it may be closed, each one met, waived by a decision record, or superseded by one."
trigger_phrases:
  - "figjam improvement research acceptance criteria"
importance_tier: "important"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: acceptance-criteria | v2.2 -->
# Acceptance Criteria: Phase 16: figjam-improvement-research

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** product-owner/017-figjam-flow-generation/016-figjam-improvement-research
**Level:** 2
**Status:** Complete
**Date:** 2026-10-20
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:criteria -->
## 2. CRITERIA

One row per criterion. `AC-ID` is stable once written: supersede a criterion, never renumber it.

| AC-ID | REQ | Given / When / Then | Verification | Status | Waiver |
|-------|-----|---------------------|--------------|--------|--------|
| AC-001 | REQ-001 | Given the DeepSeek lineage, When the 10 iterations finish, Then the state log holds 10 iteration records and the run stopped on maxIterationsReached | research/lineages/deepseek/deep-research-state.jsonl: 10 iteration records, stopReason maxIterationsReached, fanout exit 0 | Met | - |
| AC-002 | REQ-002 | Given the run ended, When the iterations are read, Then iteration-001.md to iteration-010.md exist and each cites at least one file | A per-file count of SOURCE tags: 20 to 47 per iteration, none below 1 | Met | - |
| AC-003 | REQ-003 | Given the iterations, When a fresh Opus 5.5 high agent synthesizes, Then research/research.md lists every claim it dropped or corrected | research/research.md Sections 6 and 7 list 18 corrected or dropped claims, and five claims were rechecked by the orchestrator | Met | - |
| AC-004 | REQ-004 | Given the synthesis, When it is read alone, Then it ranks at least 10 changes with their file and source, at least 3 of them on the integration | research/research.md Section 4 ranks 12 changes, 5 marked INTEGRATION | Met | - |
| AC-005 | REQ-005 | Given a long run, When agents are working, Then a one-line status is posted about every 3 minutes | Status lines in the session from 22:11 to 22:43 | Met | - |
| AC-006 | REQ-004 | Given the 2026-10-21 extension of 5 iterations, When a fresh Opus 5.5 high agent synthesizes it, Then research/research.md Section 9 names the implemented changes found wanting and ranks further changes with their file and source | research/lineages/deepseek-extension/deep-research-state.jsonl: 5 iteration records, stopReason maxIterationsReached. Section 9 finds 8 of the 12 ranks wanting, ranks 13 to 17 (2 INTEGRATION) and corrects or drops 20 claims. The orchestrator reran four of its probes and the repeated-label check | Met | - |

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

The run and the synthesis are done. Which changes to apply is the operator's call, and that choice belongs to a later phase.
<!-- /ANCHOR:closure -->
