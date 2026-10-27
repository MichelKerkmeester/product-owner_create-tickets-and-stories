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
- [ ] T012 Commit and push both repositories. Verify: `validate_parity.py product-owner` and `residency_check.py --all` each print PASSED.
- [ ] T013 Rerun the 14 failures, each board scenario in a fresh file (`skill/sonnet-high-042/`). Verify: the driver exits 0 for each lane.
- [ ] T014 Render every board and grade the rerun with one grader, then skeptics and adjudicators (`renders/`, `grades/sonnet-high-042.jsonl`). Verify: one line per rerun scenario.
- [ ] T015 Write README section 8.8 and check the gallery against the new boards. Verify: every remaining failure is named with its cause.
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T016 Run the self-tests and gates. Verify: both self-tests, pytest, 15 of 15 gates and the output format gate pass. [EVIDENCE: compose 1244 of 1244, design check exit 0, flow 169 of 169, pytest 18, 15 of 15 gates, output format gate passed]
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

- [x] CHK-001 [P0] Requirements documented in spec.md [EVIDENCE: REQ-001 to REQ-009, each with an acceptance row]
- [x] CHK-002 [P0] Technical approach defined in plan.md [EVIDENCE: plan.md Section 1 and the eight decisions in spec.md Section 2]
- [x] CHK-003 [P1] Dependencies identified and available [EVIDENCE: `grades/sonnet-high-041.*` and the findings and critic results of the 041 analysis workflow]
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
