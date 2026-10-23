---
title: "Acceptance Criteria: Phase 5: Tag key and created set"
description: "The criteria this packet must satisfy before it may be closed, each one met, waived by a decision record, or superseded by one."
trigger_phrases:
  - "tag key and set acceptance criteria"
importance_tier: "important"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: acceptance-criteria | v2.2 -->
# Acceptance Criteria: Phase 5: Tag key and created set

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** product-owner/017-figjam-flow-generation/029-extension-fixes/005-tag-key-and-set
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
| AC-001 | REQ-001 | Given the change is applied, When the files are read, Then the tag paragraph names setSharedPluginData, the namespace, the key, the created set and the departure from Figma's workflow-state rule | flow-mode.md Section 6 names setSharedPluginData with the namespace productowner, the diagram's name as the key, a value with the run id, the write time and the returned ids, the created set from the returned ids or the new page-level nodes with sections, no source text in a tag and the departure from Figma's workflow-state rule. Section 9 rebuilds the key from the diagram's name, and hybrid-workflow.md points at Section 6 | Met | - |
| AC-002 | REQ-002 | Given the final tree, When every gate runs, Then each passes | run_gates.sh all 12 gates pass. The format gate passes on 70 source files with 38 advisory warnings, the baseline count, and reference-parity.cjs is byte-identical. Router fixtures pass 141 of 141, the differential 219 of 219 and check_hub.py 37 gold rows, and the flow_check self-test passes 149 of 149. The playbook validator passes sk-create-figjam with 47 scenarios and 0 violations, and sk-product-owner with 48 scenarios and the baseline 37 warnings. validate_skill_package.py --strict passes on the hub and both packets, and the plugin rebuilds to 370 files and validates. In the scratch clone run_parity passes 62 of 62 pairs and run_residency passes for Product Owner | Met | - |
| AC-003 | REQ-003 | Given the worker's edits, When they are applied, Then each was checked against the current file before it landed | The hybrid-workflow cross-reference was changed to the references/ form so the Project mirror resolves it to its title | Met | - |

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
