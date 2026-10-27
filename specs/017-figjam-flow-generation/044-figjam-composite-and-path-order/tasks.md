---
title: "Tasks: Phase 44: FigJam composite placement and path order"
description: "Task Format: T### [P?] Description (file path). Verify: <command> prints <expected output>"
trigger_phrases:
  - "figjam composite and path order tasks"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.3 -->
# Tasks: Phase 44: FigJam composite placement and path order

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

- [x] T001 Scaffold this phase under the parent (`specs/017-figjam-flow-generation/044-figjam-composite-and-path-order/`). Verify: `ls` lists the Level 2 docs and `goal.md`. [EVIDENCE: spec, plan, tasks, acceptance criteria, goal, implementation summary and the metadata pair are present]
- [x] T002 Write the composer brief and the sentence swaps, each with its file and its check. Verify: every cause in README section 8.9 names a change or a reason it needs none. [EVIDENCE: the 043 causes map to D1 to D8 in spec.md Section 2, and the four out-of-scope findings are listed there with the reason they wait]
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T003 Place a composite after the state that enters it (`assets/compose-board.js`, `scripts/compose_board.py`). Verify: a self-test case with a label line declared first puts the first state left of the composite, and every shipped example and board fixture traces to the same geometry. [EVIDENCE: `firstOf` prefers the composite's inner start, `state.py` fails a composite with no inner `[*]`, the composer self-test passes 1245 of 1245 with the label-line case and the 38-model geometry trace moved only the two composite fixtures]
- [x] T004 Write the path-order glance rule and the wider revision exemption (`references/quality-rubric.md`, the playbook Composition row). Verify: both read in the skill and the mirror. [EVIDENCE: the path-order sentence and the wider revision line read the same in `references/quality-rubric.md` and its Knowledge file, and playbook row 83 carries both]
- [x] T005 Bring the examples' glance lines in line with the path-order rule (`assets/examples/`). Verify: each example names every node it draws, the main row in path order. [EVIDENCE: the user flow and process examples name every drawn node in path order in the skill and the mirror, and the flow check passes all seven examples]
- [x] T006 Mirror the changes and release v1.0.10.0 (`claude project/`, `SYNC.md`, `README.md`, version files, changelogs). Verify: the Composer Knowledge code block equals `compose_board.py --template` and the room is named. [EVIDENCE: the Composer Knowledge block equals `--template` (47,600 bytes), the file names 156 lines and under 2,410 characters of room, and both v1.0.10.0 changelogs and the SYNC note are written]
- [x] T007 Review the whole diff with a fresh Opus reviewer and repair the confirmed findings. Verify: each repair is read back. [EVIDENCE: the fresh Opus reviewer's P1s (the rubric reword, the composite check, the playbook path-order sentence and the FJ-017 condition) are repaired and read back in spec.md]
- [ ] T008 Commit and push both repositories. Verify: `validate_parity.py product-owner` and `residency_check.py --all` each print PASSED.
- [x] T009 Pin the working node in the launcher and prove the trace. Verify: a fixture with a known orphan wrap prints a `Label:` line through the launcher's PATH. [EVIDENCE: the launcher's pinned PATH runs node v26.8.2 and the orphan-wrap fixture prints its `Label:` line]
- [ ] T010 Rerun the 6 failures, each board scenario in a fresh file (`skill/sonnet-high-044/`). Verify: the driver exits 0 for each lane.
- [ ] T011 Render every board, read each with two readers and grade the rerun with one grader, then skeptics and adjudicators (`renders/`, `grades/sonnet-high-044.jsonl`). Verify: one line per rerun scenario.
- [ ] T012 Write README section 8.10 and check the gallery against the new boards. Verify: every remaining failure is named with its cause.
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [ ] T013 Run the self-tests and gates. Verify: both self-tests, pytest, 15 of 15 gates and the output format gate pass.
- [ ] T014 Validate this phase and the parent. Verify: `validate.sh --strict` prints `RESULT: PASSED` for both.
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

- [x] CHK-001 [P0] Requirements documented in spec.md [EVIDENCE: REQ-001 to REQ-008, each with an acceptance row]
- [x] CHK-002 [P0] Technical approach defined in plan.md [EVIDENCE: plan.md Section 1 and the eight decisions in spec.md Section 2]
- [x] CHK-003 [P1] Dependencies identified and available [EVIDENCE: `grades/sonnet-high-043.*`, README section 8.9 and the findings and critic results of the 043 analysis workflow]
<!-- /ANCHOR:pre-impl -->

---

<!-- ANCHOR:code-quality -->
## Code Quality

- [ ] CHK-010 [P0] The composer and checks agree on every new rule [EVIDENCE: pending]
- [ ] CHK-011 [P1] The driver compiles and its tests pass [EVIDENCE: pending]
<!-- /ANCHOR:code-quality -->

---

<!-- ANCHOR:testing -->
## Testing Checklist

- [ ] CHK-020 [P0] All acceptance criteria met [EVIDENCE: pending]
- [ ] CHK-021 [P0] Gates pass [EVIDENCE: pending]
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:fix-completeness -->
## Fix Completeness

- [ ] CHK-FIX-001 [P0] Each actionable finding has a finding class [EVIDENCE: pending]
- [ ] CHK-FIX-002 [P0] Same-class producer inventory completed [EVIDENCE: pending]
- [ ] CHK-FIX-003 [P0] Consumer inventory completed [EVIDENCE: pending]
- [ ] CHK-FIX-004 [P0] Adversarial cases for parser fixes [EVIDENCE: pending]
- [ ] CHK-FIX-005 [P1] Matrix axes and row count listed [EVIDENCE: pending]
- [ ] CHK-FIX-006 [P1] Hostile env variant [EVIDENCE: pending]
- [ ] CHK-FIX-007 [P1] Evidence pinned to a diff range [EVIDENCE: pending]
<!-- /ANCHOR:fix-completeness -->

---

<!-- ANCHOR:security -->
## Security

- [ ] CHK-030 [P0] No board URL, Figma file key, plan name or email in any committed file [EVIDENCE: pending]
<!-- /ANCHOR:security -->

---

<!-- ANCHOR:docs -->
## Documentation

- [ ] CHK-040 [P1] Spec, plan and tasks synchronized [EVIDENCE: pending]
- [ ] CHK-041 [P1] Project mirror and SYNC note [EVIDENCE: pending]
<!-- /ANCHOR:docs -->

---

<!-- ANCHOR:file-org -->
## File Organization

- [ ] CHK-050 [P1] No change outside the files named in spec.md Section 3 [EVIDENCE: pending]
- [ ] CHK-051 [P1] scratch/ holds no file [EVIDENCE: pending]
<!-- /ANCHOR:file-org -->

---

<!-- ANCHOR:summary -->
## Verification Summary

| Category | Total | Verified |
|----------|-------|----------|
| P0 Items | 10 | 2 |
| P1 Items | 9 | 1 |
| P2 Items | 0 | 0 |

**Verification Date**: Pending
<!-- /ANCHOR:summary -->
