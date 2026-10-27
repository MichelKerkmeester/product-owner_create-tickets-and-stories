---
title: "Tasks: Phase 45: FigJam findings fixes"
description: "Task Format: T### [P?] Description (file path). Verify: <command> prints <expected output>"
trigger_phrases:
  - "figjam findings fixes tasks"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.3 -->
# Tasks: Phase 45: FigJam findings fixes

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

- [x] T001 Scaffold this phase under the parent (`specs/017-figjam-flow-generation/045-figjam-findings-fixes/`). Verify: `ls` lists the Level 2 docs and `goal.md`. [EVIDENCE: spec, plan, tasks, acceptance criteria, goal and implementation summary are present]
- [x] T002 Map every 8.10 finding to a change or a reason it needs none, and write the swap script with its targets in the skill and the mirror. Verify: the script refuses a missing or doubled target. [EVIDENCE: `swaps.py` and `swaps2.py` refuse a missing or doubled target and applied 25 and 12 swaps. Every 8.10 finding maps to D1 to D8, and the model-only, harness and record findings are named in the implementation summary with why they need no skill change]
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T003 Plan a state board as drawn (`references/types/state.md`, `references/quality-rubric.md`, the playbook Composition row). Verify: the rule reads the same in the skill and the mirror. [EVIDENCE: the state reference, the rubric's first-glance line, the gate step in Flow Mode, the style guide, the state example and the playbook Composition row plan a state board as drawn, in the skill and the mirror]
- [x] T004 Define the flow glance lines on the main row as drawn (`references/quality-rubric.md`, the playbook, `assets/examples/`). Verify: no source keeps "two decisions share a line". [EVIDENCE: the rubric names the main row as the longest path the composer draws, both flow examples plan it so, and a search finds no live file with "two decisions share a line"]
- [x] T005 Give the boxed-in sticky its gate question and the sticky's size (`references/hybrid-workflow.md`). Verify: the rule reads the same in the skill and the mirror. [EVIDENCE: `references/hybrid-workflow.md` and its mirror state the 240 pixel sticky, the in-call probe and the boxed-in gate question, and FJ-017 allows the gate's offer]
- [x] T006 Reconcile the intake sentences and the board scenarios' intake wording (`references/flow-mode.md`, `manual-testing-playbook/`). Verify: no file keeps the single-round wording. [EVIDENCE: Flow Mode's two intake sentences both name the last round, and no scenario keeps the single-round wording]
- [x] T007 Read the board before a revision playback, name the changed end on the revision read-back and state how connector labels are read (`references/flow-mode.md`). Verify: the rule reads the same in the skill and the mirror. [EVIDENCE: Flow Mode and `sk-create-figjam/SKILL.md` read the board before a revision playback, the read-back names the changed end and connector labels are counted from the write and the screenshot]
- [x] T008 Write the grading conventions and FJ-031's write-time signal (`manual-testing-playbook/`). Verify: the Composition and Shared trunks rows and the FJ-031 file carry them. [EVIDENCE: the Composition, Shared trunks and turn rule rows carry the conventions, and FJ-031 expects the read and the write time]
- [x] T009 Release v1.0.11.0 (`SYNC.md`, `README.md`, version files, changelogs). Verify: the hub, its JSON files and `sk-create-figjam/SKILL.md` read 1.0.11.0. [EVIDENCE: the hub, its three JSON files and `sk-create-figjam/SKILL.md` read 1.0.11.0, both changelogs and the SYNC note are written]
- [x] T010 Review the whole diff with a fresh Opus reviewer and repair the confirmed findings. Verify: each repair is read back. [EVIDENCE: a fresh Opus reviewer found 1 P0, 4 P1 and 6 P2. All are repaired, with P1 item 4 narrowed as spec.md D6 records]
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T011 Run the self-tests and gates. Verify: both self-tests, pytest, 15 of 15 gates and the output format gate pass. [EVIDENCE: composer self-test 1245 of 1245, design check exit 0, flow check 172 of 172 and all 7 examples, pytest 18, 15 of 15 gates and the output format gate pass]
- [ ] T012 Commit and push both repositories. Verify: `validate_parity.py product-owner` and `residency_check.py --all` each print PASSED.
- [ ] T013 Validate this phase and the parent. Verify: `validate.sh --strict` prints `RESULT: PASSED` for both.
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

- [x] CHK-001 [P0] Requirements documented in spec.md [EVIDENCE: REQ-001 to REQ-009, each with an acceptance row]
- [x] CHK-002 [P0] Technical approach defined in plan.md [EVIDENCE: plan.md Section 1 and the eight decisions in spec.md Section 2]
- [x] CHK-003 [P1] Dependencies identified and available [EVIDENCE: `grades/sonnet-high-044.*`, README section 8.10 and the findings and critic results of the 044 analysis workflow]
<!-- /ANCHOR:pre-impl -->

---

<!-- ANCHOR:code-quality -->
## Code Quality

- [ ] CHK-010 [P0] The composer and checks are unchanged and their self-tests pass [EVIDENCE: pending]
- [ ] CHK-011 [P1] pytest passes [EVIDENCE: pending]
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
