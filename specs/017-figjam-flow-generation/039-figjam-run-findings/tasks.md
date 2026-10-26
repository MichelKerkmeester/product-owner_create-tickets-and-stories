---
title: "Tasks: Phase 39: FigJam run findings"
description: "Task Format: T### [P?] Description (file path). Verify: <command> prints <expected output>"
trigger_phrases:
  - "figjam run findings tasks"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.3 -->
# Tasks: Phase 39: FigJam run findings

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

- [x] T001 Scaffold this phase under the parent (`specs/017-figjam-flow-generation/039-figjam-run-findings/`). Verify: `ls` lists the five Level 2 docs.
- [x] T002 Back up the composer before the move (`compose-board.js`). Verify: the backup sits in the session scratchpad, outside the repository.
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T003 List a file the user named as a valid target (`sk-create-figjam/references/flow-mode.md` Section 2 step 7, and `claude project/knowledge/Product Owner - Templates - Flow Mode.md`). Verify: `rg -n 'a file the user named by its link or key'` hits both.
- [x] T004 Add the clean-up step and point the Section 8 file rule at it (`sk-create-figjam/references/flow-mode.md`). Verify: `rg -n '\*\*Clean up\.\*\*'` hits step 11 and the reply is step 12.
- [x] T005 Make each stop the last message of its turn (`flow-mode.md` and the Flow Mode mirror). Verify: `rg -n 'Each is the last message of its turn'` hits both.
- [x] T006 Exempt a section a gated extension widens from the hygiene rule (`sk-create-figjam/manual-testing-playbook/manual-testing-playbook.md`). Verify: `rg -n 'gated extension widens'` hits the hygiene bullet.
- [x] T007 Move the arrow primitives to Section 3 (`sk-create-figjam/assets/compose-board.js`). Verify: the arrows block sits before `// 4. LAYERED LAYOUT`.
- [x] T008 Cut the composer to the model's type (`sk-create-figjam/scripts/compose_board.py` `for_type`). Verify: `--design-check` prints 9,678 for a graph model, 33,362 for a sequence and 33,189 for a gantt.
- [x] T009 Read the composer code block of the mirror off `--template` again (`Product Owner - Assets - Flow Board Composer.md`). Verify: the block equals `--template`, 1,170 lines and 47,148 characters.
- [x] T010 Stop the follow-up yes on a scenario that grades an earlier stop, and run a no-Figma scenario without the server (`run/adaptive_compare.py`, `run/runtimes.py`). Verify: 21 of 54 FigJam scenarios expect a board and only FJ-009 is no-Figma.
- [x] T011 Say why a sandbox prints a SKIP line for each Project mirror (`pre-write-check/self-test-every-type.md` and the root playbook). Verify: `rg -n 'is not in this install'` hits both.
- [x] T012 Cut v1.0.5.0 for the hub and `sk-create-figjam` with changelogs, the SYNC note and the run README section 8.4. Verify: every hub version file reads 1.0.5.0.
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T013 Run the self-tests and gates. Verify: 1,032 of 1,032 composer checks, 158 of 158 check checks, 18 pytest tests, 15 of 15 gates and the output format gate pass.
- [x] T014 Get a fresh review of the diff. Verify: every finding it returns is confirmed or refuted by reading the file.
- [x] T015 Validate this phase and the parent. Verify: `validate.sh --strict` prints `RESULT: PASSED` for both.
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

- [x] CHK-001 [P0] Requirements documented in spec.md [EVIDENCE: REQ-001 to REQ-008, each with an acceptance row]
- [x] CHK-002 [P0] Technical approach defined in plan.md [EVIDENCE: plan.md Section 3 and the four decisions in spec.md Section 2]
- [x] CHK-003 [P1] Dependencies identified and available [EVIDENCE: the run README section 8.3 and the transcripts in `skill/opus-medium/`]
<!-- /ANCHOR:pre-impl -->

---

<!-- ANCHOR:code-quality -->
## Code Quality

- [x] CHK-010 [P0] The cut composer holds its own builder and no other [EVIDENCE: the self-test check "a {kind} call carries its own builder and no other, shorter than the whole composer" passes for graph, sequence and gantt]
- [x] CHK-011 [P1] The driver compiles and selects the right scenarios [EVIDENCE: `py_compile` passes, FJ-002, FJ-004, FJ-005, FJ-013, FJ-014 and FJ-015 expect no board and FJ-022 and FJ-028 do]
<!-- /ANCHOR:code-quality -->

---

<!-- ANCHOR:testing -->
## Testing Checklist

- [x] CHK-020 [P0] All acceptance criteria met [EVIDENCE: AC-001 to AC-008 Met in acceptance-criteria.md]
- [x] CHK-021 [P0] Gates pass [EVIDENCE: `run_gates.sh` prints "all 15 gates pass", the output format gate passes across 72 source files]
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:fix-completeness -->
## Fix Completeness

- [x] CHK-FIX-001 [P0] Each actionable finding has a finding class [EVIDENCE: the composer room is `class-of-bug` across all types, the stop rule and the clean-up are `cross-consumer` across the skill and the mirror, the target file, hygiene and FJ-004 findings are `instance-only` and the two driver findings are `matrix/evidence`]
- [x] CHK-FIX-002 [P0] Same-class producer inventory completed [EVIDENCE: `fill_template` is the one producer of composed code, and the self-test, design check and CLI all call it]
- [x] CHK-FIX-003 [P0] Consumer inventory completed [EVIDENCE: the Project mirror reads `--template`, which keeps the whole composer, and `rg` finds no step-number reference to the renumbered reply step]
- [x] CHK-FIX-004 [P0] Adversarial cases for parser fixes [EVIDENCE: not a security, path or redaction fix. The section cut is proven by the per-type self-test check and by every fixture composing through it]
- [x] CHK-FIX-005 [P1] Matrix axes and row count listed [EVIDENCE: three cut types by 1,032 self-test checks, and 54 scenarios by two driver flags]
- [x] CHK-FIX-006 [P1] Hostile env variant [EVIDENCE: not applicable, no changed code reads process-wide state]
- [x] CHK-FIX-007 [P1] Evidence pinned to a diff range [EVIDENCE: the diff from PO `main` at 87f1ac18, the commit this phase started from]
<!-- /ANCHOR:fix-completeness -->

---

<!-- ANCHOR:security -->
## Security

- [x] CHK-030 [P0] No board URL, Figma file key, plan name or email in any changed file [EVIDENCE: the leak scan over the changed files reads 0 hits]
<!-- /ANCHOR:security -->

---

<!-- ANCHOR:docs -->
## Documentation

- [x] CHK-040 [P1] Spec, plan and tasks synchronized [EVIDENCE: the eight findings in spec.md Section 2 map to T003 to T011]
- [x] CHK-041 [P1] Project mirror and SYNC note [EVIDENCE: the SYNC.md note of 2026-10-26 names what was mirrored and why the clean-up step was not]
<!-- /ANCHOR:docs -->

---

<!-- ANCHOR:file-org -->
## File Organization

- [x] CHK-050 [P1] No change outside the files named in spec.md Section 3 [EVIDENCE: `git status` lists those files, this folder, the parent's phase rows and the two gitignored tool links the validator needs]
- [x] CHK-051 [P1] scratch/ holds no file [EVIDENCE: `ls scratch` is empty]
<!-- /ANCHOR:file-org -->

---

<!-- ANCHOR:summary -->
## Verification Summary

| Category | Total | Verified |
|----------|-------|----------|
| P0 Items | 10 | 10/10 |
| P1 Items | 10 | 10/10 |
| P2 Items | 0 | 0/0 |

**Verification Date**: 2026-10-26
<!-- /ANCHOR:summary -->
