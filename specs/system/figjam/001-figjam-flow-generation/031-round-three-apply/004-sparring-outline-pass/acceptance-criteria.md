---
title: "Acceptance Criteria: Phase 4: Add the sparring step and the outline pass"
description: "The criteria this packet must satisfy before it may be closed, each one met, waived by a decision record, or superseded by one."
trigger_phrases:
  - "sparring outline pass acceptance criteria"
importance_tier: "important"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: acceptance-criteria | v2.2 -->
# Acceptance Criteria: Phase 4: Add the sparring step and the outline pass

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** product-owner/017-figjam-flow-generation/031-round-three-apply/004-sparring-outline-pass
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
| AC-001 | REQ-001 | Given the change is applied, When the files are read, Then the change from the interactive intake rank 4 synthesis is in place: three proposals in cost order. An outline, one line per node and edge with its Brief row, which the remove test can run on. Two named framings with what each buys and costs, with one recommended. A Mermaid sketch in chat, never written to a board. The look is then settled with four proposed choices: the accent by the keep-one test, the detail level and audience from the captured rows, whether the  | Applied to sk-create-figjam/references/flow-mode.md, sk-create-figjam/references/quality-rubric.md: three proposals in cost order. An outline, one line per node and edge with its Brief row, which the remove test can run on. Two named framings with what each buys and costs, with one recommended. A Mermaid sketch in chat, never written to a board. The look is then settled with four proposed choices: the accent by the keep-one test, the detail level and audience from the captured rows, whether the board needs sections at all, and four critique questions asked about the sketch, opening with where the eye goes first and whether that is the most important node | Met | - |
| AC-002 | REQ-002 | Given the final tree, When every gate runs, Then each passes | On the final tree run_gates.sh printed all 12 gates pass, the format gate passed across 70 source files at the 38 baseline advisories, reference parity was byte-identical, the playbooks passed at 51 scenarios with 0 warnings and 48 scenarios at the 37 baseline warnings, the topology check passed, the three skill packages validated, the plugin rebuilt to 375 files and validates, the flow_check self-test passed 154 of 154, the router passed 141 of 141 fixtures and 219 of 219 differential inputs, check_hub passed 37 gold rows, and in the scratch clone the Sync Loop parity passed 62 of 62 and Product Owner residency passed | Met | - |
| AC-003 | REQ-003 | Given the worker's edits, When they are applied, Then each was checked against the current file before it landed | Reviewed against the operator's rule that every question carries the AI's reading and a recommended answer and never dead-ends. The outline pass was re-anchored after phase 2's draw-ready rule so intake reads before modelling, and the userIntent sentence was merged by hand after phase 2 rewrote step 3 | Met | - |

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
