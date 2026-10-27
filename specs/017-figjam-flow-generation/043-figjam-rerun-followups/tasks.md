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
- [x] T002 Write the exact sentence swaps and the one code brief, each with its file and its check. Verify: every finding and critic gap of the v1.0.8.0 rerun names a change or a reason it needs none. [EVIDENCE: `scratchpad/r043/swaps.py` and `swaps2.py` matched every target once in the skill and the mirror, and `brief-label.md` carried the one code change]
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T003 Plan a composite's inner states second per D1 (`references/types/state.md`, `assets/examples/state-roamstay-booking.md`). Verify: the state rule and the example plan the first state, the inner states and the end states in that order. [EVIDENCE: `references/types/state.md:91` plans the inner states second with their section and the end states last, and the state example, whose request names the end states, focuses Cancelled and plans Pending with Upcoming and InStay second, on the operator's ruling of 2026-10-27]
- [x] T004 Spell the second split title one way and name the split under `Left out:` (`assets/flow-templates.md`, `references/flow-mode.md`). Verify: `rg -n '2\. Setup' sk-create-figjam` finds nothing. [EVIDENCE: `rg -n '2\. Setup' sk-create-figjam "claude project"` finds nothing outside the changelogs, and flow-templates and flow-mode name the split under `Left out:`]
- [x] T005 Make a revision's changed end the second glance alone and keep the old title on a revision that deletes (`references/quality-rubric.md`, `references/flow-mode.md`). Verify: both rules read in the skill and the mirror. [EVIDENCE: the rubric's revision line names the changed end alone with the entry and decisions last, and flow-mode Section 5 step 7 keeps the old title on a revision that deletes]
- [x] T006 Open every delivery reply and the delete reply on the board URL (`references/flow-mode.md`, the kernel). Verify: the reply rule says nothing comes before the URL. [EVIDENCE: flow-mode Section 8 opens the reply on the URL with nothing before it and shapes the delete reply, and `SKILL.md`, `AGENTS.md`, the figjam README and kernel v1.2.11 say the same]
- [x] T007 Place two stickies on adjacent rows and add a missing-route gate to the gantt example (`references/hybrid-workflow.md`, `assets/examples/gantt-loomlist-offline.md`). Verify: both read in the skill and the mirror. [EVIDENCE: `references/hybrid-workflow.md:122` places the second sticky below or left with a `Finding:` line, and both gantt examples show the missing-route gate, the mirror in connector words]
- [x] T008 Print a skipped `Label:` line when node is missing or the trace fails (`scripts/flow_check.py`). Verify: the flow check self-test counts the new case and passes. [EVIDENCE: `flow_check.py --self-test` prints 171 of 171 with node and 168 of 168 without it, both skipped-line cases passing]
- [x] T009 Reword the elbow rule and write lanes, zones, inner states and two readers into the playbook and rubric (`references/style-guide.md`, `manual-testing-playbook/manual-testing-playbook.md`). Verify: the Composition row names D1, D3 and D5. [EVIDENCE: style-guide line 239 reads the 56 pixel rule on the path estimate, and the playbook Composition row reads lanes and zones as frame, counts inner states, needs both readers and exempts the entry on a revision, on the operator's ruling of 2026-10-27]
- [x] T010 Mirror the changes, update the kernel when its rules change and release v1.0.9.0 (`claude project/`, `SYNC.md`, `README.md`, version files, changelogs). Verify: the Composer Knowledge code block equals `compose_board.py --template`. [EVIDENCE: 8 Knowledge files mirrored, kernel H1 v1.2.11, hub and `sk-create-figjam` at 1.0.9.0 with both changelogs and the SYNC note, and the Composer Knowledge block still equals `--template`]
- [x] T011 Review the whole diff with a fresh Opus reviewer and repair the confirmed findings. Verify: each repair is read back. [EVIDENCE: a fresh Opus medium reviewer found no P0 and 3 P1 findings, two settled by the operator and all confirmed ones repaired by `swaps2.py` and read back]
- [x] T012 Commit and push both repositories. Verify: `validate_parity.py product-owner` and `residency_check.py --all` each print PASSED. [EVIDENCE: PO 0000157 and outer 7337c9dfa plus 0001090 pushed, `validate_parity.py product-owner` PASSED 65/65 and `residency_check.py --all` PASSED 7 after the kernel statement resync]
- [x] T013 Rerun the 7 failures, each board scenario in a fresh file (`skill/sonnet-high-043/`). Verify: the driver exits 0 for each lane. [EVIDENCE: all seven lanes exited 0 between 12:59 and 13:08 UTC, five board scenarios in fresh draft files, FJ-017 in its own new file and FJ-031 paused once for the operator sticky, recorded in PO 0000158]
- [x] T014 Render every board, read each with two readers and grade the rerun with one grader, then skeptics and adjudicators (`renders/`, `grades/sonnet-high-043.jsonl`). Verify: one line per rerun scenario. [EVIDENCE: 10 renders, two readers per scored board, one Opus grader, 6 skeptic disputes adjudicated, folded into 7 lines, plus the operator's FJ-017 ruling: 1 PASS and 6 FAIL]
- [x] T015 Write README section 8.9 and check the gallery against the new boards. Verify: every remaining failure is named with its cause. [EVIDENCE: README section 8.9 names every failure with its cause, and the gallery judge kept every image]
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T016 Run the self-tests and gates. Verify: both self-tests, pytest, 15 of 15 gates and the output format gate pass. [EVIDENCE: composer 1244/1244, flow check 171/171, pytest 18, 15 of 15 gates and the format gate]
- [x] T017 Validate this phase and the parent. Verify: `validate.sh --strict` prints `RESULT: PASSED` for both. [EVIDENCE: `validate.sh --strict` prints `RESULT: PASSED` for this phase and the parent]
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

- [x] CHK-001 [P0] Requirements documented in spec.md [EVIDENCE: REQ-001 to REQ-011, each with an acceptance row]
- [x] CHK-002 [P0] Technical approach defined in plan.md [EVIDENCE: plan.md Section 1 and the eight decisions in spec.md Section 2]
- [x] CHK-003 [P1] Dependencies identified and available [EVIDENCE: `grades/sonnet-high-042.*`, README section 8.8 and the findings and critic results of the 042 analysis workflow]
<!-- /ANCHOR:pre-impl -->

---

<!-- ANCHOR:code-quality -->
## Code Quality

- [x] CHK-010 [P0] The composer and checks agree on every new rule [EVIDENCE: the composer is unchanged and its self-test passes 1244/1244 beside the new rules]
- [x] CHK-011 [P1] The driver compiles and its tests pass [EVIDENCE: `flow_check.py` self-test 171/171 and pytest 18 passed]
<!-- /ANCHOR:code-quality -->

---

<!-- ANCHOR:testing -->
## Testing Checklist

- [x] CHK-020 [P0] All acceptance criteria met [EVIDENCE: AC-001 to AC-011 Met in acceptance-criteria.md]
- [x] CHK-021 [P0] Gates pass [EVIDENCE: 15 of 15 gates and the output format gate pass]
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:fix-completeness -->
## Fix Completeness

- [x] CHK-FIX-001 [P0] Each actionable finding has a finding class [EVIDENCE: each finding of the v1.0.8.0 rerun maps to a swap in `swaps.py` or the code brief]
- [x] CHK-FIX-002 [P0] Same-class producer inventory completed [EVIDENCE: every file holding the old wording was found by `rg` and changed, skill and mirror alike]
- [x] CHK-FIX-003 [P0] Consumer inventory completed [EVIDENCE: the reply contract readers (SKILL.md, AGENTS.md, README, kernel, Templates - Flow Mode) were all updated]
- [x] CHK-FIX-004 [P0] Adversarial cases for parser fixes [EVIDENCE: the label check has a missing-node case and a failed-trace case]
- [x] CHK-FIX-005 [P1] Matrix axes and row count listed [EVIDENCE: 7 scenarios by 1 model, two readers on each of the 5 scored boards]
- [x] CHK-FIX-006 [P1] Hostile env variant [EVIDENCE: the self-test passes with node removed from PATH, 168/168]
- [x] CHK-FIX-007 [P1] Evidence pinned to a diff range [EVIDENCE: PO 0000157 for the fixes and 0000158 for the rerun]
<!-- /ANCHOR:fix-completeness -->

---

<!-- ANCHOR:security -->
## Security

- [x] CHK-030 [P0] No board URL, Figma file key, plan name or email in any committed file [EVIDENCE: leak scan 0 hits on 108 rerun files and the 12 grade files]
<!-- /ANCHOR:security -->

---

<!-- ANCHOR:docs -->
## Documentation

- [x] CHK-040 [P1] Spec, plan and tasks synchronized [EVIDENCE: spec D1 to D10, plan and tasks agree]
- [x] CHK-041 [P1] Project mirror and SYNC note [EVIDENCE: 8 Knowledge files mirrored and the SYNC note names each]
<!-- /ANCHOR:docs -->

---

<!-- ANCHOR:file-org -->
## File Organization

- [x] CHK-050 [P1] No change outside the files named in spec.md Section 3 [EVIDENCE: every changed file sits under spec.md Section 3]
- [x] CHK-051 [P1] scratch/ holds no file [EVIDENCE: scratch/ holds only .gitkeep]
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
