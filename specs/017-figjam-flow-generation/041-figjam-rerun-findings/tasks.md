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
- [x] T002 Turn the 35 findings into exact edits, one owner file each, with the finding each edit closes. Verify: every finding names an edit or a reason it needs none.
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T003 [P] Fix the skill rules (`references/flow-mode.md`, `quality-rubric.md`, `hybrid-workflow.md`, `types/state.md`, `types/process.md`, the type references' one-board sentence, `sk-product-owner/references/interactive-mode.md`). Verify: `rg -n 'is a destination' sk-create-figjam/references` hits `flow-mode.md`.
- [x] T004 [P] Fix the composer and the checks (`assets/compose-board.js`, `scripts/flow_check.py`, `scripts/compose_board.py`). Verify: both self-tests pass with the new self-loop, spacing and guard checks counted.
- [x] T005 [P] Fix the playbook rows and scenarios (`manual-testing-playbook/manual-testing-playbook.md`, FJ-020, FJ-029). Verify: the Composition row names the rubric's second-glance case.
- [x] T006 [P] Fix the driver pins, the fresh file per board scenario and the scripted operator steps (`run/adaptive_compare.py`, `run/scenario_commands.py`). Verify: pytest passes and a dry run prints one destination per pinned scenario.
- [x] T007 Correct the 040 rerun records the critic named (`grades/sonnet-high-rerun.jsonl`, `grades/sonnet-high-rerun.md`). Verify: FJ-029 and FJ-032 score Reply 1, eight board records carry the scorecard signal and FJ-035 lists one row per signal.
- [x] T008 Mirror the changes and release v1.0.7.0 (`claude project/`, `SYNC.md`, `README.md`, version files, changelogs). Verify: the Composer Knowledge code block equals `compose_board.py --template`.
- [x] T009 Review the diff and repair the confirmed findings. Verify: every repair byte-compares MATCH.
- [x] T010 Commit and push both repositories. Verify: `validate_parity.py product-owner` and `residency_check.py --all` each print PASSED.
- [x] T011 Rerun every scenario that did not pass on the v1.0.6.0 rerun, each board scenario in a fresh file (`skill/sonnet-high-041/`). Verify: the driver prints one row per turn and exits 0 for each lane.
- [x] T012 Render every board at full size (`renders/`). Verify: each board still on its file has one render.
- [x] T013 Grade the rerun with one grader, then skeptics and adjudicators (`grades/sonnet-high-041.jsonl`). Verify: one line per rerun scenario.
- [x] T014 Write the rerun up in the run README and check the gallery against the new boards. Verify: every remaining failure is named with its cause.
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T015 Run the self-tests and gates. Verify: both self-tests, pytest, 15 of 15 gates and the output format gate pass.
- [x] T016 Validate this phase and the parent. Verify: `validate.sh --strict` prints `RESULT: PASSED` for both.
<!-- /ANCHOR:phase-3 -->

---

<!-- ANCHOR:completion -->
## Completion Criteria

- [x] All tasks marked `[x]`
- [x] No `[B]` blocked tasks remaining
- [x] Manual verification passed
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

- [x] CHK-010 [P0] The composer and checks agree on every new rule [EVIDENCE: self-test 1244 of 1244 and flow check 167 of 167, both covering the self-loop, arrival and guard checks]
- [x] CHK-011 [P1] The driver compiles and its tests pass [EVIDENCE: 18 pytest passes and the driver ran 50 turns, every one exit 0]
<!-- /ANCHOR:code-quality -->

---

<!-- ANCHOR:testing -->
## Testing Checklist

- [x] CHK-020 [P0] All acceptance criteria met [EVIDENCE: acceptance-criteria.md marks AC-001 to AC-009 Met]
- [x] CHK-021 [P0] Gates pass [EVIDENCE: all 15 gates pass and the output format gate passes, both exit 0]
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:fix-completeness -->
## Fix Completeness

- [x] CHK-FIX-001 [P0] Each actionable finding has a finding class [EVIDENCE: each of the 35 findings is classed as skill, composer, playbook, harness, mirror or model slip in implementation-summary.md]
- [x] CHK-FIX-002 [P0] Same-class producer inventory completed [EVIDENCE: the one-board sentence landed in all seven type references and `assets/flow-templates.md`]
- [x] CHK-FIX-003 [P0] Consumer inventory completed [EVIDENCE: every Project counterpart is named in the 2026-10-27 SYNC note and parity passes 65/65]
- [x] CHK-FIX-004 [P0] Adversarial cases for parser fixes [EVIDENCE: `figjam_checks/fixtures.py` lines 231 and 450 hold a self-looping flowchart and architecture model that the check refuses]
- [x] CHK-FIX-005 [P1] Matrix axes and row count listed [EVIDENCE: seven types by two sides, skill and Project, 14 rows, each carrying the one-board sentence]
- [x] CHK-FIX-006 [P1] Hostile env variant [EVIDENCE: `adaptive_compare.py` line 193 refuses a new-file scenario when `NEW_FILE_PLAN` is unset]
- [x] CHK-FIX-007 [P1] Evidence pinned to a diff range [EVIDENCE: the diff range 7c077be2..0991e759 plus the close-out commit]
<!-- /ANCHOR:fix-completeness -->

---

<!-- ANCHOR:security -->
## Security

- [x] CHK-030 [P0] No board URL, Figma file key, plan name or email in any committed file [EVIDENCE: the leak scan of every added line reports 0 hits, and URLs, keys and plan names are redacted]
<!-- /ANCHOR:security -->

---

<!-- ANCHOR:docs -->
## Documentation

- [x] CHK-040 [P1] Spec, plan and tasks synchronized [EVIDENCE: spec.md, tasks.md and the implementation summary all read Complete]
- [x] CHK-041 [P1] Project mirror and SYNC note [EVIDENCE: the release commit carries the mirror and SYNC.md records the release and the gallery change]
<!-- /ANCHOR:docs -->

---

<!-- ANCHOR:file-org -->
## File Organization

- [x] CHK-050 [P1] No change outside the files named in spec.md Section 3 [EVIDENCE: the changes sit in the files spec.md Section 3 names plus the run folder and gallery the rerun required]
- [x] CHK-051 [P1] scratch/ holds no file [EVIDENCE: scratch/ holds only `.gitkeep`]
<!-- /ANCHOR:file-org -->

---

<!-- ANCHOR:summary -->
## Verification Summary

| Category | Total | Verified |
|----------|-------|----------|
| P0 Items | 10 | 10 |
| P1 Items | 9 | 9 |
| P2 Items | 0 | 0 |

**Verification Date**: 2026-10-27
<!-- /ANCHOR:summary -->
