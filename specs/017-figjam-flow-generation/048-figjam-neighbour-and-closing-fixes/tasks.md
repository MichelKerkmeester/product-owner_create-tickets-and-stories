---
title: "Tasks: Phase 48: FigJam neighbour and closing fixes"
description: "Task Format: T### [P?] Description (file path). Verify: <command> prints <expected output>"
trigger_phrases:
  - "figjam neighbour and closing fixes tasks"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.3 -->
# Tasks: Phase 48: FigJam neighbour and closing fixes

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

- [x] T001 Scaffold this phase under the parent (`specs/017-figjam-flow-generation/048-figjam-neighbour-and-closing-fixes/`). Verify: `ls` lists the Level 2 docs and `goal.md`. [EVIDENCE: spec, plan, tasks, acceptance criteria, goal and implementation summary are present]
- [x] T002 Map every 8.13 cause to a change or a reason it needs none. Verify: each maps to D1 to D8 or is named in the implementation summary. [EVIDENCE: FJ-023's decision read beside the accent maps to D1, FJ-036's trailing `Why:` line to D2, FJ-017's Finding to D3, the stranded `courier?` to D4, the gate dials to D5, the swapped pair to D6 and FJ-022's check before its playback to D7]
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [ ] T003 Lift the accent's row decision (`scripts/figjam_checks/board_geometry.py`, `scripts/flow_check.py`, `references/quality-rubric.md`, `assets/examples/process-fernhouse-refund.md`). Verify: the flow check self-test passes the case with a node between and the process example's Check block matches.
- [ ] T004 End each intake round on one closing question (`assets/flow-templates.md`, `references/flow-mode.md`, `manual-testing-playbook/manual-testing-playbook.md`). Verify: the three files state it.
- [ ] T005 Align FJ-017's Finding with the skill (`manual-testing-playbook/board-write/hybrid-extension-written.md`, `manual-testing-playbook/manual-testing-playbook.md`, `references/hybrid-workflow.md`). Verify: the scenario reads 1.0.7.0 and every copy of the signal names a sticky that left its side.
- [ ] T006 Trace diamonds at FigJam's size and box (`scripts/compose-trace.mjs`, `scripts/figjam_checks/board_geometry.py`, `assets/examples/user-flow-fernhouse-return.md`). Verify: the self-test traces a 26-character decision at 336 px and the reworded user flow example prints no `Label:` line.
- [ ] T007 Keep the dials at the playback (`references/flow-mode.md`, `manual-testing-playbook/manual-testing-playbook.md`). Verify: flow-mode names the playback alone and playbook Section 5 checks it.
- [ ] T008 Rewrite the Composition levels and the swapped-pair sentence (`manual-testing-playbook/manual-testing-playbook.md`). Verify: the row carries the three levels.
- [ ] T009 Add the turn 1 intake rule (`manual-testing-playbook/manual-testing-playbook.md`). Verify: playbook Section 5 states it.
- [ ] T010 Write the Project mirror for every changed skill file (`claude project/knowledge/`, `SYNC.md`). Verify: `validate_parity.py product-owner` and `pair_divergence.py product-owner` print PASSED.
- [ ] T011 Release v1.0.14.0 (`SYNC.md`, `README.md`, version files, changelogs). Verify: the hub, its JSON files and `sk-create-figjam/SKILL.md` read 1.0.14.0.
- [ ] T012 Review the whole diff with a fresh Opus reviewer and repair the confirmed findings. Verify: each repair is read back.
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [ ] T013 Run the self-tests and gates on the committed tree. Verify: both self-tests, the design check, pytest, 15 of 15 gates and the output format gate pass.
- [ ] T014 Commit and push both repositories. Verify: `validate_parity.py product-owner`, `residency_check.py --all` and `pair_divergence.py product-owner` each print PASSED.
- [ ] T015 Validate this phase and the parent. Verify: `validate.sh --strict` prints `RESULT: PASSED` for both after the closing edits.
- [ ] T016 Rerun FJ-017, FJ-022, FJ-023 and FJ-036 on v1.0.14.0, each in a fresh draft file (`benchmark/reports/.../skill/sonnet-high-048/`). Verify: each run has a `meta.json` and every turn exited 0.
- [ ] T017 Grade the four runs with two readers per board and one Opus grader (`grades/sonnet-high-048.*`). Verify: every scenario has a verdict with its signals.
- [ ] T018 Record the rerun as run README section 8.14, refresh the gallery with each passing board and commit both repositories. Verify: `validate_parity.py product-owner` prints PASSED.
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
- [x] CHK-003 [P1] Dependencies identified and available [EVIDENCE: `grades/sonnet-high-047.*` and README section 8.13]
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
