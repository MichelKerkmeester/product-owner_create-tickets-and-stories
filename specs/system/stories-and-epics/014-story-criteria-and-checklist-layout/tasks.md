---
title: "Tasks: Story criteria and checklist layout"
description: "Task Format: T### [P?] Description (file path). Verify: <command> prints <expected output>"
trigger_phrases:
  - "story criteria and checklist layout tasks"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.4 -->
# Tasks: Story criteria and checklist layout

<!-- SPECKIT_LEVEL: 1 -->

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

`V` is `benchmark/format/validate-output-format.cjs`. `SL` is `../z — Claude Project Sync Loop`. Commands run from the Product Owner root.
<!-- /ANCHOR:notation -->

---

<!-- ANCHOR:phase-1 -->
## Phase 1: Setup

- [x] T001 Record the baseline before any edit (`benchmark/gates/run_gates.sh`). Verify: `run_gates.sh` prints `1 of 19 gates failed`, the vendor sync gate, and the fixture runners print 73 and 167 passes.
- [x] T002 Write a Story in the new layout and run the old gate on it as the red case (`V`). Verify: `node $V <story>` reports six `no divider below a Mark-as-done checkbox` errors.
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T003 Change the Mark-as-done check, its formatter and the Requirements layout check in both validators (`V`, `SL/validate-output-format.cjs`). Verify: `node $SL/reference-parity.cjs` prints `shared core is byte-identical to the reference implementation`.
- [x] T004 Flip the Mark-as-done fixtures, add the Requirements layout fixtures and update both runners (`benchmark/format/run_fixtures.sh`). Verify: `bash benchmark/format/run_fixtures.sh` prints `PASSED all format-validator fixtures`.
- [x] T005 Rewrite the rule in Story Mode, Doc Mode, `SKILL.md`, `AGENTS.md`, both templates and the six examples (`sk-product-owner/references/story-mode.md`). Verify: `node $V` prints `validation passed across 75 source files`.
- [x] T006 Update the contract pins and the rule parity span (`benchmark/gates/rule_parity.py`). Verify: `python3 benchmark/gates/rule_parity.py` prints `PASSED 9 rules`.
- [x] T007 Mirror the kernel and ten knowledge files by hand and resync five declared statements (`claude project/Custom Instructions.md`). Verify: `run_residency.sh` in a scratch clone prints `PASSED 1 system(s)`.
- [x] T008 Bump the hub to 1.0.36.0, the skill to 1.2.20.0 and the kernel to v1.2.22, and write both release notes (`changelog/v1.0.36.0.md`). Verify: `rg -c '1.0.36.0' hub-router.json` prints 1.
- [x] T009 Add the dated parity note (`SYNC.md`). Verify: `rg -c '2026-11-16 Claude Code' SYNC.md` prints 1.
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T010 Rerun every gate from the final state (`benchmark/gates/run_gates.sh`). Verify: `run_gates.sh` prints `1 of 19 gates failed`, the same vendor sync output as the baseline.
- [x] T011 Gate a Story written in the new layout. Verify: `node $V <story>` prints `validation passed across 1 artifact file(s)`.
- [x] T012 Confirm no source still states the old rule (`sk-product-owner/`). Verify: `rg 'between two dividers' sk-product-owner AGENTS.md 'claude project' --glob '!**/changelog/**'` prints nothing.
<!-- /ANCHOR:phase-3 -->

---

<!-- ANCHOR:phase-4 -->
## Phase 4: Design copy stays in the design

- [x] T013 Measure copy-like backtick spans in Requirements and Acceptance criteria across the examples, scaffolds, mirrors, exports and graded benchmark Stories, and the one transcribed Story. Verify: the shipped function counts at most 8 distinct strings across 262 benchmark Stories and 17 in the transcribed one.
- [x] T014 Check the Story playbook scenarios against the split rule (`sk-product-owner/manual-testing-playbook/`). Verify: every Story scenario's source is typed notes, so no expected result changes.
- [x] T015 Rewrite the copy rules in Story Mode, the Story template, the sectioned example and their mirrors, and add one clause to the kernel Story paragraph (`sk-product-owner/references/story-mode.md`). Verify: `rg 'its exact copy, its labels and its values|quote the copy in' sk-product-owner benchmark/format 'claude project' --glob '!**/changelog/**'` prints nothing.
- [x] T016 Add the design-copy advisory and the narration repair wording to both validators, the `designCopy` key to `systems.cjs`, two fixtures per folder and the runner cases (`V`). Verify: `node $SL/reference-parity.cjs` prints `shared core is byte-identical to the reference implementation`, and the pre-change validator prints no advisory on `design-copy-violation.md`.
- [x] T017 Update the omitted-line record and resync the kernel statement in the shared declaration (`SL/systems.py`). Verify: a second `resync_statement.py` run prints `0 statement(s) resynced`.
- [x] T018 Bump the hub to 1.0.37.0, the skill to 1.2.21.0 and the kernel to v1.2.23, write both release notes and add the dated parity note (`changelog/v1.0.37.0.md`). Verify: `rg -c '1.0.37.0' hub-router.json` prints 1.
- [x] T019 Rerun every gate, fixture suite and the scratch-clone checks from the final state. Verify: `run_gates.sh` prints `1 of 19 gates failed`, and the fixture runners print 84 and 181 passes.
<!-- /ANCHOR:phase-4 -->

---

<!-- ANCHOR:completion -->
## Completion Criteria

- [x] All tasks marked `[x]`
- [x] No `[B]` blocked tasks remaining
- [x] Manual verification passed: the gate runner, both fixture runners, the parity check and the residency check match the baseline apart from the intended changes
<!-- /ANCHOR:completion -->

---

<!-- ANCHOR:cross-refs -->
## Cross-References

- **Specification**: See `spec.md`
- **Plan**: See `plan.md`
<!-- /ANCHOR:cross-refs -->

---
