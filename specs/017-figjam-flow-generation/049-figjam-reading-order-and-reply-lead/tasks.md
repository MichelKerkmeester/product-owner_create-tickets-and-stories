---
title: "Tasks: Phase 49: FigJam reading order and reply lead"
description: "Task Format: T### [P?] Description (file path). Verify: <command> prints <expected output>"
trigger_phrases:
  - "figjam reading order and reply lead tasks"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.3 -->
# Tasks: Phase 49: FigJam reading order and reply lead

<!-- SPECKIT_LEVEL: 2 -->

---

<!-- ANCHOR:notation -->
## Task Notation

| Prefix | Meaning |
|--------|---------|
| `[ ]` | Pending |
| `[x]` | Completed |
| `[P]` | Parallelizable |
| `[B]` | Blocked |

**Task Format**: `T### [P?] Description (file path). Verify: <command> prints <expected output>`
<!-- /ANCHOR:notation -->

---

<!-- ANCHOR:phase-1 -->
## Phase 1: Setup

- [x] T001 Scaffold this phase under the parent (`specs/017-figjam-flow-generation/049-figjam-reading-order-and-reply-lead/`). Verify: `ls` lists the Level 2 docs and `goal.md`. [EVIDENCE: spec, plan, tasks, acceptance criteria, goal and implementation summary are present]
- [x] T002 Map every 8.14 cause to a change or a reason it needs none. Verify: each maps to D1 to D8 or is named in the spec. [EVIDENCE: FJ-023's entry read before the lifted decision maps to D1, FJ-022's announcing sentence to D2, FJ-023's turn 1 playback and queue store to D3, the examples FJ-023 copied to D4, FJ-036's stranded `old?` to D5, FJ-017's assumed dials to D6 and the misread reader orders to D7, and FJ-022's late exit read is recorded in spec.md as reader variance the rubric already charges]
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [ ] T003 Return the reading order to the plain order (`scripts/figjam_checks/board_geometry.py`, `scripts/flow_check.py`, `references/quality-rubric.md`, `assets/examples/process-fernhouse-refund.md`). Verify: the self-test reads FJ-023's shape entry before decision and the process example's Check block matches.
- [ ] T004 Put the board URL first in every delivery (`references/flow-mode.md`, `SKILL.md`, `references/quality-rubric.md`, `assets/flow-templates.md`, `claude project/Custom Instructions.md`, `run/adaptive_compare.py`). Verify: each states the rule and the harness flags a non-URL first line.
- [ ] T005 Script FJ-023's intake turn and draw a handoff queue as a label (`manual-testing-playbook/board-quality/process-board-quality.md`, `manual-testing-playbook/manual-testing-playbook.md`, `references/types/process.md`). Verify: the scenario scripts the intake turn and the process type names the queue rule.
- [ ] T006 Name the reader in three examples and show an intake round in two (`assets/examples/`). Verify: every example's Check block still matches the check.
- [ ] T007 Wrap diamond labels by glyph width (`scripts/figjam_checks/board_geometry.py`, `scripts/flow_check.py`). Verify: the self-test flags `New price compared to old?` and `Drop-off point or courier?` and passes `Within 30 days of delivery?`.
- [ ] T008 Keep the dials out of the row count (`references/flow-mode.md`, `manual-testing-playbook/manual-testing-playbook.md`). Verify: both state it.
- [ ] T009 Add the `Order:` line and the Composition script (`grades/reader-brief.md`, `run/composition_check.py`). Verify: the script reproduces the corrected 047 and 048 Composition scores.
- [ ] T010 Write the Project mirror for every changed skill file (`claude project/knowledge/`, `SYNC.md`). Verify: `validate_parity.py product-owner` and `pair_divergence.py product-owner` print PASSED.
- [ ] T011 Release v1.0.15.0 with kernel v1.2.15 (`SYNC.md`, `README.md`, version files, changelogs). Verify: the hub, its JSON files and `sk-create-figjam/SKILL.md` read 1.0.15.0 and the kernel H1 reads v1.2.15.
- [ ] T012 Review the whole diff with a fresh reviewer and repair the confirmed findings. Verify: each repair is read back.
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [ ] T013 Run the self-tests and gates on the committed tree. Verify: both self-tests, the design check, pytest, 15 of 15 gates and the output format gate pass.
- [ ] T014 Commit and push both repositories. Verify: `validate_parity.py product-owner`, `residency_check.py --all` and `pair_divergence.py product-owner` each print PASSED.
- [ ] T015 Validate this phase and the parent. Verify: `validate.sh --strict` prints `RESULT: PASSED` for both after the closing edits.
- [ ] T016 Rerun FJ-022 and FJ-023 on v1.0.15.0 one after the other, each in a fresh draft file (`benchmark/reports/.../skill/sonnet-high-049/`). Verify: each run has a `meta.json` and every turn exited 0.
- [ ] T017 Grade the two runs with two readers per board, the Composition script and one grader (`grades/sonnet-high-049.*`). Verify: every scenario has a verdict with its signals.
- [ ] T018 Record the rerun as run README section 8.15, refresh the gallery with each passing board and commit both repositories. Verify: `validate_parity.py product-owner` prints PASSED.
<!-- /ANCHOR:phase-3 -->

---

<!-- ANCHOR:completion -->
## Completion Criteria

- [ ] All tasks marked `[x]`
- [x] No `[B]` blocked tasks remaining
- [ ] Manual verification passed
<!-- /ANCHOR:completion -->

---

<!-- ANCHOR:cross-refs -->
## Cross-References

- **Specification**: See `spec.md`
- **Plan**: See `plan.md`
<!-- /ANCHOR:cross-refs -->

---

## Verification Checklist

<!-- ANCHOR:protocol -->
## Verification Protocol

| Priority | Handling | Completion Impact |
|----------|----------|-------------------|
| **[P0]** | HARD BLOCKER | Cannot claim done until complete |
| **[P1]** | Required | Must complete OR get user approval |
| **[P2]** | Optional | Can defer with documented reason |
<!-- /ANCHOR:protocol -->

---

<!-- ANCHOR:pre-impl -->
## Pre-Implementation

- [x] CHK-001 [P0] Requirements documented in spec.md [EVIDENCE: REQ-001 to REQ-011, each with an acceptance row]
- [x] CHK-002 [P0] Technical approach defined in plan.md [EVIDENCE: plan.md Section 1 and the eight decisions in spec.md Section 2]
- [x] CHK-003 [P1] Dependencies identified and available [EVIDENCE: `grades/sonnet-high-048.*` and README section 8.14]
<!-- /ANCHOR:pre-impl -->

---

<!-- ANCHOR:code-quality -->
## Code Quality

- [ ] CHK-010 [P0] The composer and check self-tests pass with the new cases
- [ ] CHK-011 [P1] pytest passes
<!-- /ANCHOR:code-quality -->

---

<!-- ANCHOR:testing -->
## Testing Checklist

- [ ] CHK-020 [P0] All acceptance criteria met
- [ ] CHK-021 [P0] Gates pass
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:fix-completeness -->
## Fix Completeness

- [ ] CHK-FIX-001 [P0] Each actionable finding has a finding class
- [ ] CHK-FIX-002 [P0] Same-class producer inventory completed
- [ ] CHK-FIX-003 [P0] Consumer inventory completed
- [ ] CHK-FIX-004 [P0] Adversarial cases for parser fixes
- [ ] CHK-FIX-005 [P1] Matrix axes and row count listed
- [x] CHK-FIX-006 [P1] Hostile env variant [EVIDENCE: the spec tools run with the PO links created only for each run and removed after, as the operator asked]
- [ ] CHK-FIX-007 [P1] Evidence pinned to a diff range
<!-- /ANCHOR:fix-completeness -->

---

<!-- ANCHOR:security -->
## Security

- [ ] CHK-030 [P0] No board URL, Figma file key, plan name or email in any committed file
<!-- /ANCHOR:security -->

---

<!-- ANCHOR:docs -->
## Documentation

- [ ] CHK-040 [P1] Spec, plan and tasks synchronized
- [ ] CHK-041 [P1] Project mirror and SYNC note
<!-- /ANCHOR:docs -->

---

<!-- ANCHOR:file-org -->
## File Organization

- [ ] CHK-050 [P1] No change outside the files named in spec.md Section 3
- [x] CHK-051 [P1] scratch/ holds no file [EVIDENCE: this phase has no scratch folder]
<!-- /ANCHOR:file-org -->

---

<!-- ANCHOR:summary -->
## Verification Summary

| Category | Total | Verified |
|----------|-------|----------|
| P0 Items | 10 | 2 |
| P1 Items | 9 | 3 |
| P2 Items | 0 | 0 |

**Verification Date**: Pending
<!-- /ANCHOR:summary -->
