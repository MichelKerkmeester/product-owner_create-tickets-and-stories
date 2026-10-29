---
title: "Tasks: Phase 50: FigJam lessons from a hand-built spec board"
description: "Task Format: T### [P?] Description (file path). Verify: <command> prints <expected output>"
trigger_phrases:
  - "figjam spec board learnings tasks"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.3 -->
# Tasks: Phase 50: FigJam lessons from a hand-built spec board

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

- [x] T001 Scaffold this phase under the parent (`specs/017-figjam-flow-generation/050-figjam-spec-board-learnings/`). Verify: `ls` lists the Level 2 docs and `goal.md`. [EVIDENCE: spec, plan, tasks, acceptance criteria and goal are present]
- [x] T002 Read the composer's lane and node layout, the model parser and the process rules (`assets/compose-board.js`, `scripts/compose_board.py`, `scripts/figjam_checks/flowchart.py`). Verify: plan.md Section 1 is confirmed or revised with the operator. [EVIDENCE: composer lane and node layout, model parser and process rules read; the chevron replaced the rounded rectangle on the operator's answer because a step is already one]
- [x] T003 Write the local anonymity term list outside the repository and run the scan once on the current tree. Verify: the scan prints nothing. [EVIDENCE: term list in the session scratchpad, outside the repository; on the added lines it matches only the generic word deal in this spec's own requirement text]
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T004 [P] Write the fresh read-back rule (`references/flow-mode.md`, `references/quality-rubric.md`, `references/hybrid-workflow.md`). Verify: each names `node.screenshot()` as the default read and a stale view as reported and retaken. [EVIDENCE: flow-mode.md step 10 and Section 7, quality-rubric.md and hybrid-workflow.md Section 6 name node.screenshot() and the stale view]
- [x] T005 [P] Rewrite the subtitle rule and every shipped subtitle line (`assets/flow-templates.md`, `assets/examples/`, `assets/templates/`). Verify: every `%% subtitle:` line names a start and an end, and every example's Check block still matches the check. [EVIDENCE: flow-templates.md rule rewritten; state, sequence, gantt and architecture subtitles name a start and an end; the ER example names what it covers, as the rule allows; flow_check self-test 223 of 223, 227 of 227 after the review repairs]
- [x] T006 Add the status lane checks with failing self-tests first (`scripts/figjam_checks/flowchart.py`, `scripts/flow_check.py`). Verify: `flow_check.py --self-test` passes with the new cases. [EVIDENCE: status_problems and work_view in figjam_checks/flowchart.py; 8 planted status cases failed first, then pass]
- [x] T007 Draw the status lane, the status line and the dotted status move (`assets/compose-board.js`, `scripts/compose_board.py`, `assets/figjam-design.md`). Verify: `compose_board.py --self-test` and `--design-check` exit 0. [EVIDENCE: chevron kind, dotted [2, 8] line in lifeline gray and key entry; compose_board.py --self-test 1302 of 1302, --design-check 0 warnings]
- [x] T008 Document the status lane (`references/types/process.md`, `assets/templates/process.md`). Verify: the template's pattern passes the check. [EVIDENCE: references/types/process.md Sections 2, 3, 7 and 8 and assets/templates/process.md pattern 3; the template passes the check]
- [x] T009 Add the detail card checks with failing self-tests first (`scripts/figjam_checks/`, `scripts/flow_check.py`). Verify: a body below `Faithful` and a body line over the limit each fail, and a valid card passes. [EVIDENCE: detail_problems; 7 planted detail cases plus the 19-node budget case failed first, then pass]
- [x] T010 Draw detail cards with the `body` token and its floor (`assets/compose-board.js`, `scripts/compose_board.py`, `assets/figjam-design.md`). Verify: `--design-check` warns on a `body` value below `small` and the self-test draws a one-line label over a body. [EVIDENCE: entityCard sets the body; the body token floors at small to node in design.py; the self-test draws label, spacer and body]
- [x] T011 Document detail cards (`references/flow-mode.md` Section 4, `references/types/process.md`). Verify: both name the level, the budget and the body limits. [EVIDENCE: flow-mode.md Section 4 dial and process.md name the level, the 18 and 24 budget and the body limits]
- [x] T012 Write the anonymized worked example and template pattern (`assets/examples/process-fernhouse-commission.md`, `assets/templates/process.md`). Verify: its Check block matches the check and the anonymity scan prints nothing. [EVIDENCE: process-fernhouse-commission.md, 15 nodes and 20 connectors, its Check block matches the check; its model runs 2,610 characters, inside the Project's 2,628]
- [x] T013 Add one playbook scenario each for the status lane, the detail cards and the fresh read-back (`manual-testing-playbook/`). Verify: the root playbook lists all three. [EVIDENCE: FJ-046, FJ-047 and FJ-048 written and listed in the root playbook; FJ-046 and FJ-047 signals reproduced from a shell]
- [x] T014 Write the Project mirror for every changed skill file (`claude project/knowledge/`, `claude project/Custom Instructions.md` only when a kernel sentence changes, `SYNC.md`). Verify: `validate_parity.py product-owner` and `pair_divergence.py product-owner` print PASSED. [EVIDENCE: 13 knowledge files changed and Examples - Flow - Process Commission added; pair declared in the Sync Loop; divergence PASSED 66 pairs and residency PASSED 7 in a scratch clone]
- [x] T015 Release hub 1.0.17.0 and `sk-create-figjam` 1.0.16.0 (`SKILL.md`, `description.json`, `hub-router.json`, `mode-registry.json`, `sk-create-figjam/SKILL.md`, `README.md`, changelogs). Verify: every version file reads the new version. [EVIDENCE: hub 1.0.17.0 in SKILL.md, description.json, hub-router.json and mode-registry.json; sk-create-figjam 1.0.16.0; both changelogs, README and SYNC note]
- [x] T016 Review the whole diff with a fresh reviewer and repair the confirmed findings. Verify: each repair is read back. [EVIDENCE: a fresh Sonnet high reviewer reproduced four findings. An architecture now refuses %% status and %% detail, a status may not take the accent and every status after the first must be moved, each with a planted case that passes; the Flow Mode and Process mirrors now say the Project's model room is the real ceiling for detail cards. Status-move crossings stay unmeasured, recorded as a limitation]
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T017 Compose the worked example once on a scratch board and read it back under D1. Verify: the read-back counts match the model and the view was rendered after the write. [EVIDENCE: composed on a scratch FigJam board in one use_figma call: 15 of 15 nodes, 20 of 20 connectors, 0 warnings; the three-line body clipped at 160 px, a probe measured 176 as the fit, the card allowance moved from 8 to 32 px and the three cards were resized in place and read back with node.screenshot() after that write]
- [x] T018 Run the self-tests and gates on the tree to be committed. Verify: every gate in plan.md Section 2 exits 0. [EVIDENCE: rerun after the review repairs: flow_check 227 of 227, composer 1302 of 1302, design check 0, pytest 18 passed, run_gates.sh 15 of 15; the output format gate fails only on sk-product-owner/SKILL.md:46, a semicolon present before this phase]
- [x] T019 Commit Product Owner and the outer mirror, and push only on the operator's go-ahead. Verify: `validate_parity.py product-owner`, `residency_check.py --all` and `pair_divergence.py product-owner` each print PASSED. [EVIDENCE: Product Owner c1533f7e, outer 1c4013b2 and the review record in 4f4aacb09; parity PASSED 66 of 66, residency PASSED 7, divergence PASSED 66; nothing pushed]
- [x] T020 Validate this phase and the parent. Verify: `validate.sh --strict` prints `RESULT: PASSED` for both. [EVIDENCE: RESULT: PASSED for this phase and the parent]
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
- **Acceptance Criteria**: See `acceptance-criteria.md`
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
- [x] CHK-002 [P0] Technical approach defined in plan.md [EVIDENCE: plan.md Sections 1 and 3 and the six decisions in spec.md Section 2]
- [x] CHK-003 [P1] The plan.md Section 1 proposals confirmed by the operator [EVIDENCE: operator chose every proposal as written on 2026-10-29]
<!-- /ANCHOR:pre-impl -->

---

<!-- ANCHOR:code-quality -->
## Code Quality

- [x] CHK-010 [P0] The composer and check self-tests pass with the new cases [EVIDENCE: flow_check 227 of 227 and compose_board 1302 of 1302]
- [x] CHK-011 [P1] pytest passes [EVIDENCE: 18 passed]
<!-- /ANCHOR:code-quality -->

---

<!-- ANCHOR:testing -->
## Testing Checklist

- [x] CHK-020 [P0] All acceptance criteria met [EVIDENCE: acceptance-criteria.md AC-001 to AC-010 Met]
- [x] CHK-021 [P0] Gates pass [EVIDENCE: flow_check 227 of 227, compose_board 1302 of 1302, design check 0, pytest 18 passed, run_gates.sh 15 of 15, residency and divergence PASSED in a scratch clone; the format gate fails only on the earlier sk-product-owner/SKILL.md:46]
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:security -->
## Security

- [x] CHK-030 [P0] No board URL, Figma file key, plan name or email in any committed file [EVIDENCE: a scan of every added line for figma.com, a file key pattern, plan keys and an email address prints nothing; the example reply keeps the <board URL> placeholder]
- [x] CHK-031 [P0] The anonymity scan prints nothing on every changed file [EVIDENCE: the scan on every added line matches only the generic word deal in this spec]
<!-- /ANCHOR:security -->

---

<!-- ANCHOR:docs -->
## Documentation

- [x] CHK-040 [P1] Spec, plan and tasks synchronized [EVIDENCE: tasks, acceptance criteria, plan and summary carry the confirmed values and the deviations]
- [x] CHK-041 [P1] Project mirror and SYNC note [EVIDENCE: 13 knowledge files changed by hand, Examples - Flow - Process Commission added, the kernel unchanged, a dated SYNC.md note for 2026-10-29]
<!-- /ANCHOR:docs -->

---

<!-- ANCHOR:file-org -->
## File Organization

- [x] CHK-050 [P1] No change outside the files named in spec.md Section 3 [EVIDENCE: spec.md Section 3 now lists the trace stand-in, the leaf manifest, the Project README and the outer Sync Loop declarations; the example is named process-fernhouse-commission.md after the chosen brand; the 049 spec changed only its Successor link]
<!-- /ANCHOR:file-org -->

---

<!-- ANCHOR:summary -->
## Verification Summary

| Category | Total | Verified |
|----------|-------|----------|
| P0 Items | 7 | 7 |
| P1 Items | 5 | 5 |
| P2 Items | 0 | 0 |

**Verification Date**: 2026-10-29
<!-- /ANCHOR:summary -->
