---
title: "Acceptance Criteria: Phase 28: Read-back direction"
description: "The criteria this packet must satisfy before it may be closed, each one met, waived by a decision record, or superseded by one."
trigger_phrases:
  - "readback direction acceptance criteria"
importance_tier: "important"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: acceptance-criteria | v2.2 -->
# Acceptance Criteria: Phase 28: Read-back direction

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** product-owner/017-figjam-flow-generation/028-readback-direction
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
| AC-001 | REQ-001 | Given the change is applied, When the files are read, Then section 7 names how direction is read and how a busy board is read | flow-mode.md Section 7 reads direction from the two endpoint ids and the two end caps, never from position, counts a reversed, two-way or swapped connector as a mismatch and retries a timed-out read on half as many nodes. The Flow Mode mirror carries both paragraphs | Met | - |
| AC-002 | REQ-002 | Given the final tree, When every gate runs, Then each passes | run_gates.sh all 12 gates pass. Both format gates pass on 70 source files with 38 advisory warnings, the baseline count. reference-parity.cjs byte-identical. The playbook validator passes 47 scenarios with 0 violations and topology 9 of 9. validate_skill_package.py --strict passes on the hub and both packets, leaf-manifest.json is fresh, the plugin rebuilds to 370 skill files and validates. In the scratch clone run_parity passes 62 of 62 pairs and run_residency passes for Product Owner | Met | - |
| AC-003 | REQ-003 | Given the worker's edits, When they are applied, Then each was checked against the current file before it landed | Applied with apply.py against the current file | Met | - |

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
