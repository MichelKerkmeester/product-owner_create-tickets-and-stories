---
title: "Tasks: Phase 40: FigJam Sonnet run findings"
description: "Task Format: T### [P?] Description (file path). Verify: <command> prints <expected output>"
trigger_phrases:
  - "figjam sonnet run findings tasks"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.3 -->
# Tasks: Phase 40: FigJam Sonnet run findings

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

- [x] T001 Scaffold this phase under the parent (`specs/017-figjam-flow-generation/040-figjam-sonnet-run-findings/`). Verify: `ls` lists the Level 2 docs and `goal.md`.
- [x] T002 Grade the 54 runs with one grader, then skeptics and adjudicators (`grades/sonnet-high.jsonl`). Verify: the file holds 54 lines, 23 PASS, 29 FAIL and 2 SKIP.
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T003 [P] Fix the skill contradictions (`sk-create-figjam/SKILL.md`, `references/flow-mode.md`, `quality-rubric.md`, the seven type references, `sk-product-owner/references/interactive-mode.md`). Verify: `rg -n 'asks that one question alone' sk-create-figjam` hits `SKILL.md` and `flow-mode.md`.
- [x] T004 [P] Draw kinds apart in greyscale and key every line (`assets/compose-board.js`, `assets/figjam-design.md`, `references/style-guide.md`, `scripts/`). Verify: `--design-check` prints 0 design warnings.
- [x] T005 [P] Correct the playbook and add the `driver:` key (`sk-create-figjam/manual-testing-playbook/`). Verify: `rg -l '^driver:'` lists seven scenario files.
- [x] T006 [P] Teach the driver the `driver:` key and scripted answers (`run/adaptive_compare.py`, `run/scenario_commands.py`). Verify: an `operator-only` scenario prints a skipped row and exits 0.
- [x] T007 [P] Fold the adjudications into the records (`grades/sonnet-high.jsonl`, `grades/sonnet-high.md`, `renders/`, `results.jsonl`, README section 8.5). Verify: `results.jsonl` holds the 54 sonnet-high rows.
- [x] T008 Mirror the changes and cut kernel v1.2.7 (`claude project/`, `SYNC.md`, `README.md`, `USER-GUIDE.md`, version files, changelogs). Verify: the Composer Knowledge code block equals `compose_board.py --template`.
- [x] T009 Review the diff and repair the confirmed findings. Verify: the repair lane's 15 fixes each byte-compare MATCH and the self-tests run 1,240 and 163 checks.
- [x] T010a Apply the shared Human Voice card change on the operator's yes (`z — Knowledge/Rules - Human Voice Core.md`, every system's copy and mirror, the Sales gate snapshot, kernel v1.2.8). Verify: all 12 copies share one md5 and every system's parity check prints PASSED.
- [x] T010 Apply the handoffs no lane owned: the gate's read of a named file, the composite state section, the outline weights, FJ-030 and FJ-041, the changelog figures, the version fields and `run/aggregate.py`. Verify: all 26 dispatched files byte-compare MATCH.
- [ ] T011 Commit and push both repositories with the Sync Loop resync and review records. Verify: `validate_parity.py product-owner` and `residency_check.py product-owner` each print PASSED.
- [ ] T012 Rerun the 31 scenarios that did not pass, no earlier than 22:00 UTC (`skill/sonnet-high-rerun/`). Verify: `run-log.jsonl` holds 31 rerun rows, the earliest at or after 22:00 UTC.
- [ ] T013 Render every rerun board at 100% (`renders/`). Verify: each board in the rerun has one render file.
- [ ] T014 Grade the rerun with one grader, then skeptics and adjudicators (`grades/sonnet-high-rerun.jsonl`). Verify: the file holds 31 lines.
- [ ] T015 Refresh the gallery and every doc that names an image (`sk-create-figjam/assets/screenshots/`, `sk-create-figjam/README.md`). Verify: the gallery holds one v1.0.6.0 board per type with a caption naming its scenario, model and score.
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T016 Run the self-tests and gates. Verify: 1,240 of 1,240 composer checks, 163 of 163 check checks, 18 pytest tests, 15 of 15 gates and the output format gate pass.
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

- [x] CHK-001 [P0] Requirements documented in spec.md [EVIDENCE: REQ-001 to REQ-008, each with an acceptance row]
- [x] CHK-002 [P0] Technical approach defined in plan.md [EVIDENCE: plan.md Section 1 and the seven decisions in spec.md Section 2]
- [x] CHK-003 [P1] Dependencies identified and available [EVIDENCE: `grades/sonnet-high.jsonl` and the 54 run folders under `skill/sonnet-high/`]
<!-- /ANCHOR:pre-impl -->

---

<!-- ANCHOR:code-quality -->
## Code Quality

- [x] CHK-010 [P0] The composer and checks agree on every new rule [EVIDENCE: `compose_board.py --self-test` 1,240 of 1,240 and `flow_check.py --self-test` 163 of 163]
- [x] CHK-011 [P1] The driver and aggregator compile [EVIDENCE: the expected copy of `run/aggregate.py` parsed before dispatch and pytest passes]
<!-- /ANCHOR:code-quality -->

---

<!-- ANCHOR:testing -->
## Testing Checklist

- [ ] CHK-020 [P0] All acceptance criteria met [EVIDENCE: pending the rerun]
- [x] CHK-021 [P0] Gates pass [EVIDENCE: `run_gates.sh` prints "all 15 gates pass", the output format gate passes across 72 source files]
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:fix-completeness -->
## Fix Completeness

- [x] CHK-FIX-001 [P0] Each actionable finding has a finding class [EVIDENCE: the one-board cut is `class-of-bug` across all seven types, the type question and the Quick threshold are `cross-consumer` across the skill and the mirror, the playbook corrections are `instance-only` and the driver keys are `matrix/evidence`]
- [x] CHK-FIX-002 [P0] Same-class producer inventory completed [EVIDENCE: the one-board cut was applied to every type reference, not only the three the finding named, and the dashed log edge to the example, the template and the process reference]
- [x] CHK-FIX-003 [P0] Consumer inventory completed [EVIDENCE: the Project mirror files, the kernel, the README and the user guide carry each changed rule]
- [x] CHK-FIX-004 [P0] Adversarial cases for parser fixes [EVIDENCE: the focus parser keeps a gantt task named with "because" whole, proven by a probe that composes and passes 8 of 8 drawn checks]
- [x] CHK-FIX-005 [P1] Matrix axes and row count listed [EVIDENCE: seven types by 1,240 composer checks, and 54 scenarios by two driver keys]
- [x] CHK-FIX-006 [P1] Hostile env variant [EVIDENCE: not applicable, no changed code reads process-wide state]
- [x] CHK-FIX-007 [P1] Evidence pinned to a diff range [EVIDENCE: the diff from PO `main` at 07d024be, the commit this phase started from]
<!-- /ANCHOR:fix-completeness -->

---

<!-- ANCHOR:security -->
## Security

- [ ] CHK-030 [P0] No board URL, Figma file key, plan name or email in any committed file [EVIDENCE: pending the leak scan before each commit]
<!-- /ANCHOR:security -->

---

<!-- ANCHOR:docs -->
## Documentation

- [x] CHK-040 [P1] Spec, plan and tasks synchronized [EVIDENCE: the finding groups in spec.md Section 3 map to T003 to T010]
- [x] CHK-041 [P1] Project mirror and SYNC note [EVIDENCE: the SYNC.md note of 2026-10-26 names what was mirrored and why the scratch folder line was not]
<!-- /ANCHOR:docs -->

---

<!-- ANCHOR:file-org -->
## File Organization

- [ ] CHK-050 [P1] No change outside the files named in spec.md Section 3 [EVIDENCE: pending the final `git status`]
- [x] CHK-051 [P1] scratch/ holds no file [EVIDENCE: `ls scratch` is empty]
<!-- /ANCHOR:file-org -->

---

<!-- ANCHOR:summary -->
## Verification Summary

| Category | Total | Verified |
|----------|-------|----------|
| P0 Items | 10 | 8/10 |
| P1 Items | 10 | 9/10 |
| P2 Items | 0 | 0/0 |

**Verification Date**: 2026-10-26
<!-- /ANCHOR:summary -->
