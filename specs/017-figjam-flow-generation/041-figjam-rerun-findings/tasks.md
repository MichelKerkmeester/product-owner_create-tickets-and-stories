---
title: "Tasks: Phase 41: FigJam rerun findings"
description: "Task Format: T### [P?] Description (file path). Verify: <command> prints <expected output>"
trigger_phrases:
  - "figjam rerun findings tasks"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.3 -->
# Tasks: Phase 41: FigJam rerun findings

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

- [x] T001 Scaffold this phase under the parent (`specs/017-figjam-flow-generation/041-figjam-rerun-findings/`). Verify: `ls` lists the Level 2 docs and `goal.md`.
- [ ] T002 Turn the 35 findings into exact edits, one owner file each, with the finding each edit closes. Verify: every finding names an edit or a reason it needs none.
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [ ] T003 [P] Fix the skill rules (`references/flow-mode.md`, `quality-rubric.md`, `hybrid-workflow.md`, `types/state.md`, `types/process.md`, the type references' one-board sentence, `sk-product-owner/references/interactive-mode.md`). Verify: `rg -n 'is a destination' sk-create-figjam/references` hits `flow-mode.md`.
- [ ] T004 [P] Fix the composer and the checks (`assets/compose-board.js`, `scripts/flow_check.py`, `scripts/compose_board.py`). Verify: both self-tests pass with the new self-loop, spacing and guard checks counted.
- [ ] T005 [P] Fix the playbook rows and scenarios (`manual-testing-playbook/manual-testing-playbook.md`, FJ-020, FJ-029). Verify: the Composition row names the rubric's second-glance case.
- [ ] T006 [P] Fix the driver pins, the fresh file per board scenario and the scripted operator steps (`run/adaptive_compare.py`, `run/scenario_commands.py`). Verify: pytest passes and a dry run prints one destination per pinned scenario.
- [ ] T007 Correct the 040 rerun records the critic named (`grades/sonnet-high-rerun.jsonl`, `grades/sonnet-high-rerun.md`). Verify: FJ-029 and FJ-032 score Reply 1, eight board records carry the scorecard signal and FJ-035 lists one row per signal.
- [ ] T008 Mirror the changes and release v1.0.7.0 (`claude project/`, `SYNC.md`, `README.md`, version files, changelogs). Verify: the Composer Knowledge code block equals `compose_board.py --template`.
- [ ] T009 Review the diff and repair the confirmed findings. Verify: every repair byte-compares MATCH.
- [ ] T010 Commit and push both repositories. Verify: `validate_parity.py product-owner` and `residency_check.py --all` each print PASSED.
- [ ] T011 Rerun every scenario that did not pass on the v1.0.6.0 rerun, each board scenario in a fresh file (`skill/sonnet-high-041/`). Verify: the driver prints one row per turn and exits 0 for each lane.
- [ ] T012 Render every board at full size (`renders/`). Verify: each board still on its file has one render.
- [ ] T013 Grade the rerun with one grader, then skeptics and adjudicators (`grades/sonnet-high-041.jsonl`). Verify: one line per rerun scenario.
- [ ] T014 Write the rerun up in the run README and check the gallery against the new boards. Verify: every remaining failure is named with its cause.
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [ ] T015 Run the self-tests and gates. Verify: both self-tests, pytest, 15 of 15 gates and the output format gate pass.
- [ ] T016 Validate this phase and the parent. Verify: `validate.sh --strict` prints `RESULT: PASSED` for both.
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
- [x] CHK-003 [P1] Dependencies identified and available [EVIDENCE: `grades/sonnet-high-rerun.jsonl` and the findings and critic results of the 040 analysis workflow]
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
