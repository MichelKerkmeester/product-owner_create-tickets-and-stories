---
title: "Acceptance Criteria: Phase 7: Give the Product Owner lane a board block and one named exception"
description: "The criteria this packet must satisfy before it may be closed, each one met, waived by a decision record, or superseded by one."
trigger_phrases:
  - "po lane board block acceptance criteria"
importance_tier: "important"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: acceptance-criteria | v2.2 -->
# Acceptance Criteria: Phase 7: Give the Product Owner lane a board block and one named exception

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** product-owner/017-figjam-flow-generation/031-round-three-apply/007-po-lane-board-block
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
| AC-001 | REQ-001 | Given the change is applied, When the files are read, Then the change from the interactive intake rank 7 synthesis is in place: when FLOW is detected, the comprehensive question gains one block naming the reader, the question the board answers and what the reader should decide. Core rule 1 names a board intake as a legal second round, bounded by Rank 2's stop rule, so the ban on a second round keeps its force everywhere else | Applied to sk-product-owner/assets/interactive-response-templates.md, claude project/knowledge/Product Owner - Assets - Interactive Response Templates.md, sk-product-owner/references/interactive-mode.md, claude project/knowledge/Product Owner - System - Interactive Mode.md: when FLOW is detected, the comprehensive question gains one block naming the reader, the question the board answers and what the reader should decide. Core rule 1 names a board intake as a legal second round, bounded by Rank 2's stop rule, so the ban on a second round keeps its force everywhere else | Met | - |
| AC-002 | REQ-002 | Given the final tree, When every gate runs, Then each passes | On the final tree run_gates.sh printed all 12 gates pass, the format gate passed across 70 source files at the 38 baseline advisories, reference parity was byte-identical, the playbooks passed at 51 scenarios with 0 warnings and 48 scenarios at the 37 baseline warnings, the topology check passed, the three skill packages validated, the plugin rebuilt to 375 files and validates, the flow_check self-test passed 154 of 154, the router passed 141 of 141 fixtures and 219 of 219 differential inputs, check_hub passed 37 gold rows, and in the scratch clone the Sync Loop parity passed 62 of 62 and Product Owner residency passed | Met | - |
| AC-003 | REQ-003 | Given the worker's edits, When they are applied, Then each was checked against the current file before it landed | Reviewed against the operator's rule that every question carries the AI's reading and a recommended answer and never dead-ends. Applied with apply.py against the current files, with no edit refused | Met | - |

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
