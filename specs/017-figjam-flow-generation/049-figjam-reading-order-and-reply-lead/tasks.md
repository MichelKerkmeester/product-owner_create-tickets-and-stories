---
title: "Tasks: Phase 49: FigJam reading order and reply lead"
description: "Task Format: T### [P?] Description (file path). Verify: <command> prints <expected output>"
trigger_phrases:
  - "figjam reading order and reply lead tasks"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.3 -->
# Tasks: Phase 49: FigJam reading order and reply lead

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

- [x] T001 Scaffold this phase under the parent (`specs/017-figjam-flow-generation/049-figjam-reading-order-and-reply-lead/`). Verify: `ls` lists the Level 2 docs and `goal.md`. [EVIDENCE: spec, plan, tasks, acceptance criteria, goal and implementation summary are present]
- [x] T002 Map every 8.14 cause to a change or a reason it needs none. Verify: each maps to D1 to D8 or is named in the spec. [EVIDENCE: FJ-023's entry read before the lifted decision maps to D1, FJ-022's announcing sentence to D2, FJ-023's turn 1 playback and queue store to D3, the examples FJ-023 copied to D4, FJ-036's stranded `old?` to D5, FJ-017's assumed dials to D6 and the misread reader orders to D7, and FJ-022's late exit read is recorded in spec.md as reader variance the rubric already charges]
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T003 Return the reading order to the plain order (`scripts/figjam_checks/board_geometry.py`, `scripts/flow_check.py`, `references/quality-rubric.md`, `assets/examples/process-fernhouse-refund.md`). Verify: the self-test reads FJ-023's shape entry before decision and the process example's Check block matches. [EVIDENCE: `flow_check.py --self-test` 201 of 201 with the case reading FJ-023's shape expecting the entry before the decision, and the process example's Check block printed by the check, which the reviewer reran and matched (PO 0000184)]
- [x] T004 Put the board URL first in every delivery (`references/flow-mode.md`, `SKILL.md`, `references/quality-rubric.md`, `assets/flow-templates.md`, `claude project/Custom Instructions.md`, `run/adaptive_compare.py`). Verify: each states the rule and the harness flags a non-URL first line. [EVIDENCE: flow-mode Section 8 first bullet, SKILL step 6, the rubric reply line, a wrong and a right first line in the flow templates and the kernel delivery sentence, with `lead_is_url` in `run/adaptive_compare.py` accepting a plain or redacted URL and rejecting a sentence before it on the reviewer's 16 strings]
- [x] T005 Script FJ-023's intake turn and draw a handoff queue as a label (`manual-testing-playbook/board-quality/process-board-quality.md`, `manual-testing-playbook/manual-testing-playbook.md`, `references/types/process.md`). Verify: the scenario scripts the intake turn and the process type names the queue rule. [EVIDENCE: `process-board-quality.md` and its root playbook block script the turn 1 intake round and `references/types/process.md` draws a queue between two lanes as the crossing connector's label]
- [x] T006 Name the reader in three examples and show an intake round in two (`assets/examples/`). Verify: every example's Check block still matches the check. [EVIDENCE: the gantt, ER and sequence requests name their reader and the process and user flow examples show an intake round, with the review's `Settled so far` line removed and both descriptions naming the round, every Check block matching the check]
- [x] T007 Wrap diamond labels by glyph width (`scripts/figjam_checks/board_geometry.py`, `scripts/flow_check.py`). Verify: the self-test flags `New price compared to old?` and `Drop-off point or courier?` and passes `Within 30 days of delivery?`. [EVIDENCE: `board_geometry.py` measures diamond labels by Inter Medium advance widths, and two new self-tests flag `New price compared to old?` and pass `Within 30 days of delivery?`, which the reviewer showed fail on the old measure]
- [x] T008 Keep the dials out of the row count (`references/flow-mode.md`, `manual-testing-playbook/manual-testing-playbook.md`). Verify: both state it. [EVIDENCE: flow-mode Section 2, root playbook Section 5 and Templates - Flow Mode each say the dials are not rows]
- [x] T009 Add the `Order:` line and the Composition script (`grades/reader-brief.md`, `run/composition_check.py`). Verify: the script reproduces the corrected 047 and 048 Composition scores. [EVIDENCE: `grades/reader-brief.md` and `run/composition_check.py` reproduce the corrected 047 and 048 Composition scores on six of six boards, the review's accent rule fix scores an accent read late by every reader 0 and `--self-test` passes 5 of 5, and the reader brief now says the Order line repeats the reader's own reading order (PO 0000185)]
- [x] T010 Write the Project mirror for every changed skill file (`claude project/knowledge/`, `SYNC.md`). Verify: `validate_parity.py product-owner` and `pair_divergence.py product-owner` print PASSED. [EVIDENCE: nine Project knowledge files, the kernel and a dated SYNC note, with `validate_parity.py product-owner` PASSED 65/65 and `pair_divergence.py --all` PASSED after the outer commits]
- [x] T011 Release v1.0.15.0 with kernel v1.2.15 (`SYNC.md`, `README.md`, version files, changelogs). Verify: the hub, its JSON files and `sk-create-figjam/SKILL.md` read 1.0.15.0 and the kernel H1 reads v1.2.15. [EVIDENCE: the hub `SKILL.md`, `description.json`, `hub-router.json`, `mode-registry.json`, `sk-create-figjam/SKILL.md` and the README read 1.0.15.0, both changelogs exist and the kernel H1 reads v1.2.15]
- [x] T012 Review the whole diff with a fresh reviewer and repair the confirmed findings. Verify: each repair is read back. [EVIDENCE: one fresh Claude Sonnet 5.5 high reviewer found two P1 and three P2 findings and every one was repaired: the accent rule and a self-test in `composition_check.py`, the reader brief scope, the playbook intake sentence, the AGENTS.md reply lead, the `Settled so far` line and the SYNC sentence]
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T013 Run the self-tests and gates on the committed tree. Verify: both self-tests, the design check, pytest, 15 of 15 gates and the output format gate pass. [EVIDENCE: flow check 201 of 201, composer 1251 of 1251, design check exit 0, pytest 18 passed, `run_gates.sh` all 15 gates pass and the output format gate passed across 72 files]
- [x] T014 Commit and push both repositories. Verify: `validate_parity.py product-owner`, `residency_check.py --all` and `pair_divergence.py product-owner` each print PASSED. [EVIDENCE: PO 0000184 pushed, outer 0001123 (mirror and the resynced kernel statement) and 0001124 (the flow-mode review pin) pushed under the operator's one-push override, then `validate_parity.py product-owner` PASSED 65/65, `residency_check.py --all` PASSED and `pair_divergence.py --all` PASSED]
- [x] T015 Validate this phase and the parent. Verify: `validate.sh --strict` prints `RESULT: PASSED` for both after the closing edits. [EVIDENCE: `validate.sh --strict` prints RESULT: PASSED for this phase and the parent after the closing edits]
- [x] T016 Rerun FJ-022 and FJ-023 on v1.0.15.0 one after the other, each in a fresh draft file (`benchmark/reports/.../skill/sonnet-high-049/`). Verify: each run has a `meta.json` and every turn exited 0. [EVIDENCE: `skill/sonnet-high-049/` holds both runs, each with `meta.json`, one board and every turn exiting 0, FJ-022 from 05:41 to 05:48 and FJ-023 from 05:48 to 05:52]
- [x] T017 Grade the two runs with two readers per board, the Composition script and one grader (`grades/sonnet-high-049.*`). Verify: every scenario has a verdict with its signals. [EVIDENCE: `grades/sonnet-high-049.*`: both boards 22 of 22 and both scenarios FAIL, FJ-022 on its three-zone signal and FJ-023 on a sentence after its intake round's closing question, with Composition 2 on both from the script]
- [x] T018 Record the rerun as run README section 8.15, refresh the gallery with each passing board and commit both repositories. Verify: `validate_parity.py product-owner` prints PASSED. [EVIDENCE: run README section 8.15 and the file rows, the 22-point FJ-023 board as the process gallery image, PO 0000185 and outer 0001125]
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
- [x] CHK-003 [P1] Dependencies identified and available [EVIDENCE: `grades/sonnet-high-048.*` and README section 8.14]
<!-- /ANCHOR:pre-impl -->

---

<!-- ANCHOR:code-quality -->
## Code Quality

- [x] CHK-010 [P0] The composer and check self-tests pass with the new cases [EVIDENCE: flow check 201 of 201, composer 1251 of 1251 and `composition_check.py --self-test` 5 of 5]
- [x] CHK-011 [P1] pytest passes [EVIDENCE: 18 passed]
<!-- /ANCHOR:code-quality -->

---

<!-- ANCHOR:testing -->
## Testing Checklist

- [x] CHK-020 [P0] All acceptance criteria met [EVIDENCE: AC-001 to AC-011 Met in acceptance-criteria.md, with SC-003 not met and recorded as a known limitation]
- [x] CHK-021 [P0] Gates pass [EVIDENCE: all 15 gates pass and the output format gate passed]
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:fix-completeness -->
## Fix Completeness

- [x] CHK-FIX-001 [P0] Each actionable finding has a finding class [EVIDENCE: each 8.14 cause maps to D1 to D7 or to reader variance in spec.md]
- [x] CHK-FIX-002 [P0] Same-class producer inventory completed [EVIDENCE: the reviewer grepped the skill, playbook, examples, Project files, AGENTS.md, USER-GUIDE.md and READMEs for each old rule and found only AGENTS.md, now fixed]
- [x] CHK-FIX-003 [P0] Consumer inventory completed [EVIDENCE: the check, the examples' Check blocks, the harness delivery check and the grader brief consume the changed order and are updated]
- [x] CHK-FIX-004 [P0] Adversarial cases for parser fixes [EVIDENCE: `lead_is_url` on 16 strings and `composition_check.py` on constructed edge cases and the six stored boards]
- [x] CHK-FIX-005 [P1] Matrix axes and row count listed [EVIDENCE: seven example types against the check, two rerun scenarios and six rescored boards]
- [x] CHK-FIX-006 [P1] Hostile env variant [EVIDENCE: the spec tools run with the PO links created only for each run and removed after, as the operator asked]
- [x] CHK-FIX-007 [P1] Evidence pinned to a diff range [EVIDENCE: PO ee2492cf..730231e9 for the release and 730231e9..dbb84f81 for the rerun]
<!-- /ANCHOR:fix-completeness -->

---

<!-- ANCHOR:security -->
## Security

- [x] CHK-030 [P0] No board URL, Figma file key, plan name or email in any committed file [EVIDENCE: the new lines and files hold no key from the redact list, no plan key and no board URL, and the one README match sits in older records the operator chose to keep]
<!-- /ANCHOR:security -->

---

<!-- ANCHOR:docs -->
## Documentation

- [x] CHK-040 [P1] Spec, plan and tasks synchronized [EVIDENCE: the spec scope names the operator's stop at this rerun and every task carries evidence]
- [x] CHK-041 [P1] Project mirror and SYNC note [EVIDENCE: SYNC.md 2026-10-28 note for v1.0.15.0 and the flow-mode review pin at 63ebbdb0]
<!-- /ANCHOR:docs -->

---

<!-- ANCHOR:file-org -->
## File Organization

- [x] CHK-050 [P1] No change outside the files named in spec.md Section 3 [EVIDENCE: the release, the rerun records, the gallery and these docs, plus `AGENTS.md` for the review's reply-lead finding]
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
