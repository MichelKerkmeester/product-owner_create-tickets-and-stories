---
title: "Tasks: Phase 43: FigJam rerun follow-ups"
description: "Task Format: T### [P?] Description (file path). Verify: <command> prints <expected output>"
trigger_phrases:
  - "figjam rerun follow-ups tasks"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.3 -->
# Tasks: Phase 43: FigJam rerun follow-ups

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

- [x] T001 Scaffold this phase under the parent (`specs/017-figjam-flow-generation/043-figjam-rerun-followups/`). Verify: `ls` lists the Level 2 docs and `goal.md`.
- [ ] T002 Write the exact sentence swaps and the one code brief, each with its file and its check. Verify: every finding and critic gap of the v1.0.8.0 rerun names a change or a reason it needs none.
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [ ] T003 Plan a composite's inner states second per D1 (`references/types/state.md`, `assets/examples/state-roamstay-booking.md`). Verify: the state rule and the example plan the first state, the inner states and the end states in that order.
- [ ] T004 Spell the second split title one way and name the split under `Left out:` (`assets/flow-templates.md`, `references/flow-mode.md`). Verify: `rg -n '2\. Setup' sk-create-figjam` finds nothing.
- [ ] T005 Make a revision's changed end the second glance alone and keep the old title on a revision that deletes (`references/quality-rubric.md`, `references/flow-mode.md`). Verify: both rules read in the skill and the mirror.
- [ ] T006 Open every delivery reply and the delete reply on the board URL (`references/flow-mode.md`, the kernel). Verify: the reply rule says nothing comes before the URL.
- [ ] T007 Place two stickies on adjacent rows and add a missing-route gate to the gantt example (`references/hybrid-workflow.md`, `assets/examples/gantt-loomlist-offline.md`). Verify: both read in the skill and the mirror.
- [ ] T008 Print a skipped `Label:` line when node is missing or the trace fails (`scripts/flow_check.py`). Verify: the flow check self-test counts the new case and passes.
- [ ] T009 Reword the elbow rule and write lanes, zones, inner states and two readers into the playbook and rubric (`references/style-guide.md`, `manual-testing-playbook/manual-testing-playbook.md`). Verify: the Composition row names D1, D3 and D5.
- [ ] T010 Mirror the changes, update the kernel when its rules change and release v1.0.9.0 (`claude project/`, `SYNC.md`, `README.md`, version files, changelogs). Verify: the Composer Knowledge code block equals `compose_board.py --template`.
- [ ] T011 Review the whole diff with a fresh Opus reviewer and repair the confirmed findings. Verify: each repair is read back.
- [ ] T012 Commit and push both repositories. Verify: `validate_parity.py product-owner` and `residency_check.py --all` each print PASSED.
- [ ] T013 Rerun the 7 failures, each board scenario in a fresh file (`skill/sonnet-high-043/`). Verify: the driver exits 0 for each lane.
- [ ] T014 Render every board, read each with two readers and grade the rerun with one grader, then skeptics and adjudicators (`renders/`, `grades/sonnet-high-043.jsonl`). Verify: one line per rerun scenario.
- [ ] T015 Write README section 8.9 and check the gallery against the new boards. Verify: every remaining failure is named with its cause.
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [ ] T016 Run the self-tests and gates. Verify: both self-tests, pytest, 15 of 15 gates and the output format gate pass.
- [ ] T017 Validate this phase and the parent. Verify: `validate.sh --strict` prints `RESULT: PASSED` for both.
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
- [x] CHK-003 [P1] Dependencies identified and available [EVIDENCE: `grades/sonnet-high-042.*`, README section 8.8 and the findings and critic results of the 042 analysis workflow]
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
