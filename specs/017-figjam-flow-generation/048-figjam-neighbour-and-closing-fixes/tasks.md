---
title: "Tasks: Phase 48: FigJam neighbour and closing fixes"
description: "Task Format: T### [P?] Description (file path). Verify: <command> prints <expected output>"
trigger_phrases:
  - "figjam neighbour and closing fixes tasks"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.3 -->
# Tasks: Phase 48: FigJam neighbour and closing fixes

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

- [x] T001 Scaffold this phase under the parent (`specs/017-figjam-flow-generation/048-figjam-neighbour-and-closing-fixes/`). Verify: `ls` lists the Level 2 docs and `goal.md`. [EVIDENCE: spec, plan, tasks, acceptance criteria, goal and implementation summary are present]
- [x] T002 Map every 8.13 cause to a change or a reason it needs none. Verify: each maps to D1 to D8 or is named in the implementation summary. [EVIDENCE: FJ-023's decision read beside the accent maps to D1, FJ-036's trailing `Why:` line to D2, FJ-017's Finding to D3, the stranded `courier?` to D4, the gate dials to D5, the swapped pair to D6 and FJ-022's check before its playback to D7]
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T003 Lift the accent's row decision (`scripts/figjam_checks/board_geometry.py`, `scripts/flow_check.py`, `references/quality-rubric.md`, `assets/examples/process-fernhouse-refund.md`). Verify: the flow check self-test passes the case with a node between and the process example's Check block matches. [EVIDENCE: `reading_order` lifts a decision joined to the accent on its row with no node between, the self-test cases "a decision beside the accent on its row reads right after it" and "a decision joined to the accent with a node between them on the row keeps its column place" pass, rubric Section 3 states the exception and the process example's Check block matches the check]
- [x] T004 End each intake round on one closing question (`assets/flow-templates.md`, `references/flow-mode.md`, `manual-testing-playbook/manual-testing-playbook.md`). Verify: the three files state it. [EVIDENCE: flow templates Section 5 adds the closing question bullet, flow-mode Section 8 says an intake round ends on it and playbook Section 5 fails a round whose last line is anything else, with the kernel's Flow Mode Delivery paragraph carrying the same sentence]
- [x] T005 Align FJ-017's Finding with the skill (`manual-testing-playbook/board-write/hybrid-extension-written.md`, `manual-testing-playbook/manual-testing-playbook.md`, `references/hybrid-workflow.md`). Verify: the scenario reads 1.0.7.0 and every copy of the signal names a sticky that left its side. [EVIDENCE: `hybrid-extension-written.md` reads 1.0.7.0 and asks for a `Finding:` line only for a sticky that left its named side, the root playbook FJ-017 summary matches and hybrid-workflow Section 3 says the check names the second sticky's side on its `Sides:` line]
- [x] T006 Trace diamonds at FigJam's size and box (`scripts/compose-trace.mjs`, `scripts/figjam_checks/board_geometry.py`, `assets/examples/user-flow-fernhouse-return.md`). Verify: the self-test traces a 26-character decision at 336 px and the reworded user flow example prints no `Label:` line. [EVIDENCE: `compose-trace.mjs` rounds each line height, `_text_width` reads a diamond at half its width less 8 px, `compose_board.py` holds a 26-character decision to 336 by 216 and the user flow example reads `Within 30 days after delivery?` and `Drop-off or courier pickup?` with no `Label:` line]
- [x] T007 Keep the dials at the playback (`references/flow-mode.md`, `manual-testing-playbook/manual-testing-playbook.md`). Verify: flow-mode names the playback alone and playbook Section 5 checks it. [EVIDENCE: flow-mode Section 4 has the playback alone name the dials, the playback sentence names them by their words, the Flow Mode mirror matches and playbook Section 5 fails a playback that leaves one out]
- [x] T008 Rewrite the Composition levels and the swapped-pair sentence (`manual-testing-playbook/manual-testing-playbook.md`). Verify: the row carries the three levels. [EVIDENCE: the Composition row reads 2, 1 and 0 with the requested element held to its planned place and "When two parts swap, the part out of place is the one read earlier than its planned place"]
- [x] T009 Add the turn 1 intake rule (`manual-testing-playbook/manual-testing-playbook.md`). Verify: playbook Section 5 states it. [EVIDENCE: playbook Section 5 states the Standard energy turn 1 intake rule, and FJ-022 now scripts the intake turn its prompt calls for]
- [x] T010 Write the Project mirror for every changed skill file (`claude project/knowledge/`, `SYNC.md`). Verify: `validate_parity.py product-owner` and `pair_divergence.py product-owner` print PASSED. [EVIDENCE: kernel v1.2.14, seven Knowledge files and the composer mirror changed with their sources and the SYNC.md note of 2026-10-28 records each, parity is read after outer commit 2ea776e8e]
- [x] T011 Release v1.0.14.0 (`SYNC.md`, `README.md`, version files, changelogs). Verify: the hub, its JSON files and `sk-create-figjam/SKILL.md` read 1.0.14.0. [EVIDENCE: `SKILL.md`, `description.json`, `hub-router.json`, `mode-registry.json` and `sk-create-figjam/SKILL.md` read 1.0.14.0, both v1.0.14.0 changelogs exist and the kernel H1 reads v1.2.14, committed as PO e0a082d5]
- [x] T012 Review the whole diff with a fresh Opus reviewer and repair the confirmed findings. Verify: each repair is read back. [EVIDENCE: the fresh reviewer found 1 P1 and 9 P2 and no P0, each confirmed and repaired: a second accent-fill node named twice, the top-down reading of the accent's row, a test name, FJ-022's missing intake turn, the playback sentence without the dials, the Composition level against the revision exception, the README code figure, the SYNC section name, the changelog sizes and two serial commas, with 199 of 199 and 1251 of 1251 self-test checks after]
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T013 Run the self-tests and gates on the committed tree. Verify: both self-tests, the design check, pytest, 15 of 15 gates and the output format gate pass. [EVIDENCE: on the release tree committed as e0a082d5 the flow check printed 199 of 199, the composer 1251 of 1251, the design check exit 0, pytest 18 passed, all 15 gates and the output format gate across 72 source files]
- [x] T014 Commit and push both repositories. Verify: `validate_parity.py product-owner`, `residency_check.py --all` and `pair_divergence.py product-owner` each print PASSED. [EVIDENCE: PO commits e0a082d5 and 3a3a356a and outer commits 2ea776e8e, 8bc6d1014 and 997560542 pushed, parity PASSED 65 of 65, residency PASSED 7 systems, divergence PASSED 208 pairs and every `check_criteria.sh` row ok]
- [x] T015 Validate this phase and the parent. Verify: `validate.sh --strict` prints `RESULT: PASSED` for both after the closing edits. [EVIDENCE: `RESULT: PASSED` for this phase and for 017 after the closing edits]
- [x] T016 Rerun FJ-017, FJ-022, FJ-023 and FJ-036 on v1.0.14.0, each in a fresh draft file (`benchmark/reports/.../skill/sonnet-high-048/`). Verify: each run has a `meta.json` and every turn exited 0. [EVIDENCE: four `meta.json` files, 15 turns at rc 0, one attempt each on the relaunch after a first launch stopped on the weekly usage limit before any model ran]
- [x] T017 Grade the four runs with two readers per board and one Opus grader (`grades/sonnet-high-048.*`). Verify: every scenario has a verdict with its signals. [EVIDENCE: `sonnet-high-048.jsonl` holds 4 lines with their signals, FJ-017 and FJ-036 PASS and FJ-022 and FJ-023 FAIL, six reader files, and a completeness check corrected three scores against the notes]
- [x] T018 Record the rerun as run README section 8.14, refresh the gallery with each passing board and commit both repositories. Verify: `validate_parity.py product-owner` prints PASSED. [EVIDENCE: section 8.14 records 2 of 4, the process gallery image is FJ-023's board and PO commit 62320e19 carries the records]
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
- [x] CHK-003 [P1] Dependencies identified and available [EVIDENCE: `grades/sonnet-high-047.*` and README section 8.13]
<!-- /ANCHOR:pre-impl -->

---

<!-- ANCHOR:code-quality -->
## Code Quality

- [x] CHK-010 [P0] The composer and check self-tests pass with the new cases [EVIDENCE: flow check 199 of 199, composer 1251 of 1251, design check exit 0, and the two-accent case fails with its fix removed]
- [x] CHK-011 [P1] pytest passes [EVIDENCE: 18 passed]
<!-- /ANCHOR:code-quality -->

---

<!-- ANCHOR:testing -->
## Testing Checklist

- [x] CHK-020 [P0] All acceptance criteria met [EVIDENCE: AC-001 to AC-011 read Met, with SC-003 recorded as not met]
- [x] CHK-021 [P0] Gates pass [EVIDENCE: all 15 gates and the output format gate across 72 source files pass]
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:fix-completeness -->
## Fix Completeness

- [x] CHK-FIX-001 [P0] Each actionable finding has a finding class [EVIDENCE: each 8.13 cause is classed as script, skill, playbook or model in spec.md D1 to D8]
- [x] CHK-FIX-002 [P0] Same-class producer inventory completed [EVIDENCE: the reviewer searched the skill, the mirror and the examples for the six old phrases and found none left stating the old rule]
- [x] CHK-FIX-003 [P0] Consumer inventory completed [EVIDENCE: the playback sentence, FJ-022's turns and the revision exception, readers of the changed rules, were found and repaired in review]
- [x] CHK-FIX-004 [P0] Adversarial cases for parser fixes [EVIDENCE: cases for a node between, two accents, a decision joined both ways and a top-down flow were probed, and each new self-test fails with its fix removed]
- [x] CHK-FIX-005 [P1] Matrix axes and row count listed [EVIDENCE: four check changes with five new self-tests, nine rule files with their seven mirrors and the kernel]
- [x] CHK-FIX-006 [P1] Hostile env variant [EVIDENCE: the spec tools run with the PO links created only for each run and removed after, as the operator asked]
- [x] CHK-FIX-007 [P1] Evidence pinned to a diff range [EVIDENCE: `git diff e359b8a6..e0a082d5` in the PO repository]
<!-- /ANCHOR:fix-completeness -->

---

<!-- ANCHOR:security -->
## Security

- [x] CHK-030 [P0] No board URL, Figma file key, plan name or email in any committed file [EVIDENCE: the scan of the 245 added lines found no file key, URL, plan key, email or em dash]
<!-- /ANCHOR:security -->

---

<!-- ANCHOR:docs -->
## Documentation

- [x] CHK-040 [P1] Spec, plan and tasks synchronized [EVIDENCE: every task, acceptance row and goal criterion carries its evidence and `validate.sh --strict` passes]
- [x] CHK-041 [P1] Project mirror and SYNC note [EVIDENCE: see T010]
<!-- /ANCHOR:docs -->

---

<!-- ANCHOR:file-org -->
## File Organization

- [x] CHK-050 [P1] No change outside the files named in spec.md Section 3 [EVIDENCE: the release touches only the scripts, references, assets, playbook, mirror and release files Section 3 names, the composer among them by amendment]
- [x] CHK-051 [P1] scratch/ holds no file [EVIDENCE: this phase has no scratch folder]
<!-- /ANCHOR:file-org -->

---

<!-- ANCHOR:summary -->
## Verification Summary

| Category | Total | Verified |
|----------|-------|----------|
| P0 Items | 10 | 10 |
| P1 Items | 9 | 9 |
| P2 Items | 0 | 0 |

**Verification Date**: 2026-10-28
<!-- /ANCHOR:summary -->
