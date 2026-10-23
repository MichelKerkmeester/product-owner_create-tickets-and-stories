---
title: "Acceptance Criteria: Phase 2: sk-create-figjam deep review"
description: "The criteria this packet must satisfy before it may be closed, each one met, waived by a decision record, or superseded by one."
trigger_phrases:
  - "sk create figjam deep review acceptance criteria"
importance_tier: "important"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: acceptance-criteria | v2.2 -->
# Acceptance Criteria: Phase 2: sk-create-figjam deep review

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** product-owner/018-product-owner-deep-review/002-sk-create-figjam
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
| AC-001 | REQ-001 | Given the DeepSeek lineage, When the 5 iterations finish, Then the state log holds 5 iteration records and the run stopped on maxIterationsReached | `review/lineages/deepseek/deep-review-state.jsonl:1` deep-review-state.jsonl holds 5 iteration records, stopReason maxIterationsReached, fanout exit 0 | Met | - |
| AC-002 | REQ-002 | Given the run ended, When the iterations are read, Then every finding carries a severity and a SOURCE citation | `review/lineages/deepseek/deep-review-findings-registry.json:1` All 11 findings in deep-review-findings-registry.json carry a severity and a file and line, and every cited file exists | Met | - |
| AC-003 | REQ-003 | Given the report, When the orchestrator opens every P0 and P1 citation, Then implementation-summary.md records each as holding or not | `implementation-summary.md:45` implementation-summary.md records a verdict for all 1 P1 findings, 1 holding. There were 0 P0 | Met | - |
| AC-004 | REQ-004 | Given the checked findings, When they are read alone, Then each names the file to change | `implementation-summary.md:45` Each finding names its file, and each P1 verdict names the fix site in the Product Owner file | Met | - |
| AC-005 | REQ-005 | Given a long run, When agents are working, Then a one-line status is posted about every 3 minutes | `goal.md:1` A monitor posted a one-line count every 3 minutes from 13:00 to 13:21 | Met | - |

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

Every criterion is Met.
<!-- /ANCHOR:closure -->
