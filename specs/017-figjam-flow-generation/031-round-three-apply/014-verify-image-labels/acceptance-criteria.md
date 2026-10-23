---
title: "Acceptance Criteria: Phase 14: Verify an image-derived label before it becomes a node"
description: "The criteria this packet must satisfy before it may be closed, each one met, waived by a decision record, or superseded by one."
trigger_phrases:
  - "verify image labels acceptance criteria"
importance_tier: "important"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: acceptance-criteria | v2.2 -->
# Acceptance Criteria: Phase 14: Verify an image-derived label before it becomes a node

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** product-owner/017-figjam-flow-generation/031-round-three-apply/014-verify-image-labels
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
| AC-001 | REQ-001 | Given the change is applied, When the files are read, Then the change from the input to model logic rank 3 synthesis is in place: a label taken from an image is re-read on a crop or an upscale, and the row names which read produced it. Where two reads disagree the label goes to the one question or carries the unknown class, and the existing `read visually` wording becomes the model's rule as well as the reply's | Applied to sk-create-figjam/references/flow-mode.md: a label taken from an image is re-read on a crop or an upscale, and the row names which read produced it. Where two reads disagree the label goes to the one question or carries the unknown class, and the existing `read visually` wording becomes the model's rule as well as the reply's | Met | - |
| AC-002 | REQ-002 | Given the final tree, When every gate runs, Then each passes | On the final tree run_gates.sh printed all 12 gates pass, the format gate passed across 70 source files at the 38 baseline advisories, reference parity was byte-identical, the playbooks passed at 51 scenarios with 0 warnings and 48 scenarios at the 37 baseline warnings, the topology check passed, the three skill packages validated, the plugin rebuilt to 375 files and validates, the flow_check self-test passed 154 of 154, the router passed 141 of 141 fixtures and 219 of 219 differential inputs, check_hub passed 37 gold rows, and in the scratch clone the Sync Loop parity passed 62 of 62 and Product Owner residency passed | Met | - |
| AC-003 | REQ-003 | Given the worker's edits, When they are applied, Then each was checked against the current file before it landed | Reviewed against the operator's rule that every question carries the AI's reading and a recommended answer and never dead-ends. This edit, phase 16's and phase 19's all appended to one Screenshots bullet, so the three were combined into one edit | Met | - |

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
