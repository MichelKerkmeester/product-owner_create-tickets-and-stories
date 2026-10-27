---
title: "Tasks: Phase 42: FigJam glance plans and Left out"
description: "Task Format: T### [P?] Description (file path). Verify: <command> prints <expected output>"
trigger_phrases:
  - "figjam glance and left out tasks"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.3 -->
# Tasks: Phase 42: FigJam glance plans and Left out

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

- [x] T001 Scaffold this phase under the parent (`specs/017-figjam-flow-generation/042-figjam-glance-and-left-out/`). Verify: `ls` lists the Level 2 docs and `goal.md`.
- [x] T002 Write one brief per change with its file, the change and its check. Verify: every finding and critic gap names a brief or a reason it needs none. [EVIDENCE: the exact sentence swaps ran from one script with counted matches, the label warning went to DeepSeek as one brief and the router finding needs no brief, as spec D8 records]
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T003 Rewrite the state glance rule and the state example per D1 (`references/types/state.md`, `assets/examples/state-roamstay-booking.md`). Verify: `rg -n 'part of the frame' references/types/state.md` hits. [EVIDENCE: `rg -n 'part of the frame' references/types/state.md` hits line 91 and the state example plans Pending first]
- [x] T004 Add the light blue entry to the rubric's early kinds and align the glance lines of all seven examples (`references/quality-rubric.md`, `assets/examples/`). Verify: each example's glance lines name every outlined or entry kind its board draws. [EVIDENCE: the rubric names the light blue entry and the process, architecture, user flow and state examples plan the kinds their boards draw]
- [x] T005 Name every cut, split and later board in `Left out:` in the reply and the gate (`references/flow-mode.md`, `assets/flow-templates.md`, `SKILL.md`, `AGENTS.md`). Verify: `rg -n 'when the provenance table lists items left out' sk-create-figjam` finds nothing. [EVIDENCE: the search finds nothing, and the reply and gate rule reads `a cut, a split, a later board or a point the sources left open` in the skill, mirror, kernel, `AGENTS.md`, `sk-product-owner` and the user guide, with six example gates carrying the line]
- [x] T006 Fix the single sticky fallback, the same-title revision delete and the split title spelling (`references/hybrid-workflow.md`, `references/flow-mode.md`). Verify: `rg -n '1\. Signup' sk-create-figjam` finds nothing. [EVIDENCE: `rg -n '1\. Signup' sk-create-figjam` finds nothing and both rules are mirrored]
- [x] T007 Warn before the gate about a label that leaves one word alone (`scripts/flow_check.py`, `scripts/figjam_checks/board_geometry.py`). Verify: the flow check self-test counts the new cases and passes, and `compose-board.js` is unchanged. [EVIDENCE: flow check self-test 169 of 169, node text measured at 0.5 of the node size so the process example flags the two labels its rendered board wraps, `compose-board.js` unchanged]
- [x] T008 Fix the playbook rows (`manual-testing-playbook/manual-testing-playbook.md`, FJ-009, FJ-029, FJ-038, FJ-040, FJ-045). Verify: the Composition row names the composite and the unplanned part. [EVIDENCE: the Composition row names the composite and the unplanned part, FJ-045 asks Q1 to Q3 in its steps and signals, FJ-040 already expected the `Left out:` line and needed no change]
- [x] T009 Drop the FJ-017 scorecard, give the reader brief its persona and questions and each run its own temp folder (`grades/sonnet-high-041.jsonl`, `run/`). Verify: pytest passes and the FJ-017 line has a null scorecard. [EVIDENCE: the FJ-017 line parses with a null scorecard and pytest passes 18. The reader brief carries the persona and Q1 to Q3 at grading and the launcher gives each run its own temp folder]
- [x] T010 Mirror the changes, update the kernel and release v1.0.8.0 (`claude project/`, `SYNC.md`, `README.md`, version files, changelogs). Verify: the Composer Knowledge code block equals `compose_board.py --template`. [EVIDENCE: compose self-test confirms the Composer Knowledge file carries the current code, kernel v1.2.10, hub and `sk-create-figjam` 1.0.8.0, `sk-product-owner` 1.2.5.0]
- [x] T011 Review the whole diff with a fresh Opus reviewer and repair the confirmed findings. Verify: each repair is read back. [EVIDENCE: a fresh Opus reviewer reported 7 findings. Six were confirmed and repaired by counted swaps. The label finding was declined because the rendered boards wrap those labels]
- [x] T012 Commit and push both repositories. Verify: `validate_parity.py product-owner` and `residency_check.py --all` each print PASSED. [EVIDENCE: PO pushed through 0000153 and the outer repo through 0001087, with parity PASSED 65/65 and residency PASSED 7 systems]
- [x] T013 Rerun the 14 failures, each board scenario in a fresh file (`skill/sonnet-high-042/`). Verify: the driver exits 0 for each lane. [EVIDENCE: 14 runs, 47 turns, every turn exit 0 and none retried, after a relaunch once the disk had room]
- [x] T014 Render every board and grade the rerun with one grader, then skeptics and adjudicators (`renders/`, `grades/sonnet-high-042.jsonl`). Verify: one line per rerun scenario. [EVIDENCE: 13 board renders and the FJ-032 page, nine readers, one Opus grader, skeptics on 14 runs with 11 adjudications, a fold and a critic, and 14 lines in `grades/sonnet-high-042.jsonl`]
- [x] T015 Write README section 8.8 and check the gallery against the new boards. Verify: every remaining failure is named with its cause. [EVIDENCE: README section 8.8 names each of the 7 remaining failures with its cause, and the gallery takes the FJ-026 state board]
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T016 Run the self-tests and gates. Verify: both self-tests, pytest, 15 of 15 gates and the output format gate pass. [EVIDENCE: compose 1244 of 1244, design check exit 0, flow 169 of 169, pytest 18, 15 of 15 gates, output format gate passed]
- [x] T017 Validate this phase and the parent. Verify: `validate.sh --strict` prints `RESULT: PASSED` for both. [EVIDENCE: `validate.sh --strict` prints RESULT: PASSED for this phase and the parent]
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
- [x] CHK-003 [P1] Dependencies identified and available [EVIDENCE: `grades/sonnet-high-041.*` and the findings and critic results of the 041 analysis workflow]
<!-- /ANCHOR:pre-impl -->

---

<!-- ANCHOR:code-quality -->
## Code Quality

- [x] CHK-010 [P0] The composer and checks agree on every new rule [EVIDENCE: compose self-test 1244 of 1244 and flow self-test 169 of 169, with the composer unchanged and the label warning in the check alone]
- [x] CHK-011 [P1] The driver compiles and its tests pass [EVIDENCE: the driver is unchanged in this phase and pytest passes 18]
<!-- /ANCHOR:code-quality -->

---

<!-- ANCHOR:testing -->
## Testing Checklist

- [x] CHK-020 [P0] All acceptance criteria met [EVIDENCE: acceptance-criteria.md marks AC-001 to AC-009 Met and Closeable Yes]
- [x] CHK-021 [P0] Gates pass [EVIDENCE: 15 of 15 gates and the output format gate pass on the committed tree]
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:fix-completeness -->
## Fix Completeness

- [x] CHK-FIX-001 [P0] Each actionable finding has a finding class [EVIDENCE: each review and grading finding is classed skill, project-mirror, playbook, harness, composer or model-only in `grades/sonnet-high-042.md` and the implementation summary]
- [x] CHK-FIX-002 [P0] Same-class producer inventory completed [EVIDENCE: the Left out wording was fixed across every file that stated it, found by a repo grep, not only the files the reviewer named]
- [x] CHK-FIX-003 [P0] Consumer inventory completed [EVIDENCE: the mirror files, kernel, `AGENTS.md`, `sk-product-owner` and the user guide were read as consumers of the rule and updated together]
- [x] CHK-FIX-004 [P0] Adversarial cases for parser fixes [EVIDENCE: the label warning self-test holds a label that warns and labels that do not, and the check exits 0 without node]
- [x] CHK-FIX-005 [P1] Matrix axes and row count listed [EVIDENCE: seven examples by skill and mirror, 14 gate rows each checked by counted swaps]
- [x] CHK-FIX-006 [P1] Hostile env variant [EVIDENCE: the check runs with node absent and exits 0 with no Label line, as the review confirmed]
- [x] CHK-FIX-007 [P1] Evidence pinned to a diff range [EVIDENCE: PO commits 0000147 to 0000155 and outer 0001086 to 0001088]
<!-- /ANCHOR:fix-completeness -->

---

<!-- ANCHOR:security -->
## Security

- [x] CHK-030 [P0] No board URL, Figma file key, plan name or email in any committed file [EVIDENCE: leak scans of the added lines and the run output report 0 hits]
<!-- /ANCHOR:security -->

---

<!-- ANCHOR:docs -->
## Documentation

- [x] CHK-040 [P1] Spec, plan and tasks synchronized [EVIDENCE: spec, plan, tasks, acceptance criteria and implementation summary agree on Complete and 7 of 14]
- [x] CHK-041 [P1] Project mirror and SYNC note [EVIDENCE: the mirror took every skill sentence in the same commit and SYNC.md carries the phase 042 note]
<!-- /ANCHOR:docs -->

---

<!-- ANCHOR:file-org -->
## File Organization

- [x] CHK-050 [P1] No change outside the files named in spec.md Section 3 [EVIDENCE: the changed files fall in the spec's Files to Change table, plus `USER-GUIDE.md` and `sk-product-owner`, which the review found stating the old rule]
- [x] CHK-051 [P1] scratch/ holds no file [EVIDENCE: scratch/ holds only .gitkeep]
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
