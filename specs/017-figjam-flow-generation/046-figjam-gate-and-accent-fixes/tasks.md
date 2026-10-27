---
title: "Tasks: Phase 46: FigJam gate and accent fixes"
description: "Task Format: T### [P?] Description (file path). Verify: <command> prints <expected output>"
trigger_phrases:
  - "figjam gate and accent fixes tasks"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.3 -->
# Tasks: Phase 46: FigJam gate and accent fixes

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

- [x] T001 Scaffold this phase under the parent (`specs/017-figjam-flow-generation/046-figjam-gate-and-accent-fixes/`). Verify: `ls` lists the Level 2 docs and `goal.md`. [EVIDENCE: spec, plan, tasks, acceptance criteria, goal and implementation summary are present]
- [x] T002 Map every 8.11 finding to a change or a reason it needs none. Verify: each maps to D1 to D7 or is named in the implementation summary. [EVIDENCE: FJ-017 maps to D1, FJ-036 to D2 and D3, the self-scan after a stop to D4, the end-state reading to D5, the skipped sketch to D6 and the missed `tip` to D7]
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T003 Add the `%% notes:` line and the `--notes` sides check, with a placed sticky blocking the next node (`scripts/compose_board.py`, `scripts/flow_check.py`, `scripts/figjam_checks/board_geometry.py`, `assets/compose-board.js`). Verify: both self-tests pass with the notes cases. [EVIDENCE: the composer self-test passes 1250 of 1250 with the key-gap and missing-node cases, and the flow check 175 of 175 with the small-board, hemmed, freed and stacked cases]
- [x] T004 Add the `%% goal:` line and keep the accent off the goal, then re-accent the nine shipped flows (`scripts/compose_board.py`, `references/`, `assets/`). Verify: every example and template passes the check with its goal drawn as the goal. [EVIDENCE: the composer refuses a goal line naming a step, all seven examples pass the check and the six flow and two process templates and the Fernhouse example accent a decision or a step with their goal named]
- [x] T005 Read labels at two measures (`scripts/figjam_checks/board_geometry.py`). Verify: the self-test's lone `tip` case prints a `Label:` line. [EVIDENCE: the "Editor with welcome tip" case passes in the flow check self-test]
- [x] T006 Write the stop rule, the gate's sketch and critique and the end-state reading (`references/flow-mode.md`, `references/quality-rubric.md`, `AGENTS.md`, `manual-testing-playbook/manual-testing-playbook.md`). Verify: each script swap matched its target once. [EVIDENCE: the swap script reported ok for all six files, and the mirror files took the same sentences]
- [x] T007 Rewrite FJ-017 and FJ-022 (`manual-testing-playbook/board-write/hybrid-extension-written.md`, `manual-testing-playbook/board-quality/user-flow-board-quality.md` and their root copies). Verify: no copy keeps the adjacent-rows or goal-styling wording. [EVIDENCE: a search finds no "style the confirmation as the goal" and no "adjacent rows" in a scenario]
- [x] T008 Release v1.0.12.0 (`SYNC.md`, `README.md`, version files, changelogs). Verify: the hub, its JSON files and `sk-create-figjam/SKILL.md` read 1.0.12.0. [EVIDENCE: the hub, its three JSON files and `sk-create-figjam/SKILL.md` read 1.0.12.0, both changelogs and the SYNC note are written]
- [x] T009 Review the whole diff with a fresh Opus reviewer and repair the confirmed findings. Verify: each repair is read back. [EVIDENCE: the reviewer found 6 P1 and 7 P2 and no P0. Each was confirmed against the files and repaired: the check now fails what the composer refuses and an unknown notes id, the Project composer takes the goal rule and the re-accented model, four stale goal sentences changed, every example gate shows its sketch and critique answers, the kernel gate does too, the comment-line list names both new lines and the serial commas are gone. Finding 12 led to choosing the sides together, and the shipped state layout boxes NoShow in for real, as FJ-017's triage records]
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T010 Run the self-tests and gates. Verify: both self-tests, pytest, 15 of 15 gates and the output format gate pass. [EVIDENCE: composer 1250 of 1250, flow check 177 of 177, design check exit 0, every example passes, pytest 18, 15 of 15 gates and the output format gate across 72 source files]
- [ ] T011 Commit and push both repositories. Verify: `validate_parity.py product-owner`, `residency_check.py --all` and `pair_divergence.py product-owner` each print PASSED.
- [ ] T012 Validate this phase and the parent. Verify: `validate.sh --strict` prints `RESULT: PASSED` for both.
- [ ] T013 Rerun FJ-017, FJ-036, FJ-022 and FJ-023 on v1.0.12.0, each in a fresh draft file (`benchmark/reports/.../skill/sonnet-high-046/`). Verify: each run has a `meta.json` and every turn exited 0.
- [ ] T014 Grade the four runs with two readers per board and one Opus grader (`grades/sonnet-high-046.*`). Verify: every scenario has a verdict with its signals.
- [ ] T015 Record the rerun as run README section 8.12, refresh the gallery with each passing board and commit both repositories. Verify: `validate_parity.py product-owner` prints PASSED.
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

- [x] CHK-001 [P0] Requirements documented in spec.md [EVIDENCE: REQ-001 to REQ-010, each with an acceptance row]
- [x] CHK-002 [P0] Technical approach defined in plan.md [EVIDENCE: plan.md Section 1 and the eight decisions in spec.md Section 2]
- [x] CHK-003 [P1] Dependencies identified and available [EVIDENCE: `grades/sonnet-high-045.*` and README section 8.11]
<!-- /ANCHOR:pre-impl -->

---

<!-- ANCHOR:code-quality -->
## Code Quality

- [x] CHK-010 [P0] The composer and check self-tests pass with the new cases [EVIDENCE: composer 1250 of 1250, flow check 177 of 177, design check exit 0]
- [x] CHK-011 [P1] pytest passes [EVIDENCE: pytest 18 passed]
<!-- /ANCHOR:code-quality -->

---

<!-- ANCHOR:testing -->
## Testing Checklist

- [ ] CHK-020 [P0] All acceptance criteria met
- [x] CHK-021 [P0] Gates pass [EVIDENCE: 15 of 15 gates and the output format gate across 72 source files pass on the working tree]
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:fix-completeness -->
## Fix Completeness

- [x] CHK-FIX-001 [P0] Each actionable finding has a finding class [EVIDENCE: each 8.11 finding is classed as script, skill, playbook or model slip in the implementation summary]
- [x] CHK-FIX-002 [P0] Same-class producer inventory completed [EVIDENCE: a search for goal accents across the skill, the models, the mirror and the playbook found the nine flows and every rule sentence, all changed]
- [x] CHK-FIX-003 [P0] Consumer inventory completed [EVIDENCE: the reviewer read every sibling sentence and found the look bullet, the edit lever, the style guide goal row, the composer kind table and the example gates, all repaired]
- [x] CHK-FIX-004 [P0] Adversarial cases for parser fixes [EVIDENCE: the composer refuses a goal line naming a step and a notes line naming a missing node, and the sides check has hemmed, freed and stacked cases]
- [x] CHK-FIX-005 [P1] Matrix axes and row count listed [EVIDENCE: nine re-accented flows over five skill files and their four mirrors, and six rule files with their mirrors]
- [x] CHK-FIX-006 [P1] Hostile env variant [EVIDENCE: the spec tools run with the PO links created only for each run and removed after, as the operator asked]
- [ ] CHK-FIX-007 [P1] Evidence pinned to a diff range
<!-- /ANCHOR:fix-completeness -->

---

<!-- ANCHOR:security -->
## Security

- [x] CHK-030 [P0] No board URL, Figma file key, plan name or email in any committed file [EVIDENCE: the leak scan of the diff and the new files found no file key, URL, plan key, plan name, email or em dash]
<!-- /ANCHOR:security -->

---

<!-- ANCHOR:docs -->
## Documentation

- [ ] CHK-040 [P1] Spec, plan and tasks synchronized
- [x] CHK-041 [P1] Project mirror and SYNC note [EVIDENCE: sixteen Knowledge files and the kernel changed with their sources, and the SYNC note names them]
<!-- /ANCHOR:docs -->

---

<!-- ANCHOR:file-org -->
## File Organization

- [ ] CHK-050 [P1] No change outside the files named in spec.md Section 3
- [ ] CHK-051 [P1] scratch/ holds no file
<!-- /ANCHOR:file-org -->

---

<!-- ANCHOR:summary -->
## Verification Summary

| Category | Total | Verified |
|----------|-------|----------|
| P0 Items | 10 | 6 |
| P1 Items | 9 | 5 |
| P2 Items | 0 | 0 |

**Verification Date**: Pending
<!-- /ANCHOR:summary -->
