---
title: "Tasks: Phase 51: FigJam gallery rerun on v1.0.16.0"
description: "Task Format: T### [P?] Description (file path). Verify: <command> prints <expected output>"
trigger_phrases:
  - "figjam gallery rerun tasks"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.3 -->
# Tasks: Phase 51: FigJam gallery rerun on v1.0.16.0

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

- [x] T001 Scaffold this phase under the parent (`specs/017-figjam-flow-generation/051-figjam-gallery-rerun/`). Verify: `ls` lists the Level 2 docs and `goal.md`.
- [x] T002 Write FJ-049 and list it in the playbook root (`sk-create-figjam/manual-testing-playbook/`). Verify: the root lists FJ-049. [EVIDENCE: board-quality/status-lane-board-quality.md, listed in Section 10 and wave 4; its reference model passes the check at 11 nodes and 15 connectors; the driver loads it with 4 turns]
- [x] T003 Create one draft file per run and prepare the FJ-032 board with content. Verify: each file key opens. [EVIDENCE: ten FigJam drafts in the operator's team plan, keys kept outside the repository; FJ-032's file holds a Sprint retro section with six stickies]
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T004 Run the ten scenarios one at a time with `claude:claude-sonnet-5-5:medium` (`benchmark/reports/.../skill/sonnet-medium-051/`). Verify: each run has a `meta.json` and one board. [EVIDENCE: ten runs from 21:05 to 21:50, each exit 0 with a meta.json naming the medium model; FJ-025 wrote two boards, a split]
- [x] T005 Render each board and read it with two fresh readers (`grades/sonnet-medium-051/`). Verify: twenty reader notes, each closing on an `Order:` line. [EVIDENCE: twelve renders, twenty notes, each ending on an Order: line; one reader session per reader across the ten boards]
- [x] T006 Score Composition and grade each board with one Sonnet 5.5 high grader. Verify: ten scorecard rows. [EVIDENCE: grades/sonnet-medium-051.jsonl, 10 lines, totals equal their parts; 3 PASS and 7 FAIL]
- [x] T007 Judge each image under D4 and update the gallery and both READMEs. Verify: each caption names its run, model, version and score. [EVIDENCE: sequence, ER, gantt, existing-board and status lane images replaced; user flow, process, architecture, state and dense flow kept]
- [x] T008 Record report section 8.16. Verify: it names every result and swap. [EVIDENCE: run report section 8.16 and the files table]
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T009 Redact, scan and run the gates. Verify: the scan prints nothing and `run_gates.sh` passes 15 of 15. [EVIDENCE: the scan prints nothing; the vendor gate failed on another session's upstream commits, the three vendored packages were pulled at pins already on origin, and run_gates.sh then passed 15 of 15]
- [ ] T010 Commit both repositories and push on the operator's standing yes. Verify: `main` matches `origin` in both.
- [x] T011 Validate this phase and the parent. Verify: `validate.sh --strict` prints `RESULT: PASSED`. [EVIDENCE: RESULT: PASSED for this phase and the parent]
<!-- /ANCHOR:phase-3 -->

---

<!-- ANCHOR:completion -->
## Completion Criteria

- [ ] All tasks marked `[x]`
- [ ] No `[B]` blocked tasks remaining
- [ ] Manual verification passed
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

- [x] CHK-001 [P0] Requirements documented in spec.md [EVIDENCE: spec.md REQ-001 to REQ-006]
- [x] CHK-002 [P0] Technical approach defined in plan.md [EVIDENCE: plan.md Sections 1 and 3]
- [x] CHK-003 [P1] The scenarios, model and grading confirmed by the operator [EVIDENCE: operator answers of 2026-10-29: Sonnet medium, ten scenarios, full grading]
<!-- /ANCHOR:pre-impl -->

---

<!-- ANCHOR:code-quality -->
## Code Quality

- [x] CHK-010 [P0] Every run names `claude:claude-sonnet-5-5:medium` in its meta.json [EVIDENCE: ten meta.json files name the medium model]
- [x] CHK-011 [P1] Every board has two reader notes and a scorecard row [EVIDENCE: twenty notes and ten rows]
<!-- /ANCHOR:code-quality -->

---

<!-- ANCHOR:testing -->
## Testing Checklist

- [x] CHK-020 [P0] All acceptance criteria met [EVIDENCE: AC-001 to AC-006 Met]
- [x] CHK-021 [P0] Gates pass [EVIDENCE: run_gates.sh 15 of 15]
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:security -->
## Security

- [x] CHK-030 [P0] No board URL, Figma file key, plan name or email in any committed file [EVIDENCE: the scan prints nothing]
- [x] CHK-031 [P0] Each scenario's output was redacted as it finished [EVIDENCE: run_full.sh redacted each scenario as it finished]
<!-- /ANCHOR:security -->

---

<!-- ANCHOR:docs -->
## Documentation

- [x] CHK-040 [P1] Spec, plan and tasks synchronized [EVIDENCE: tasks, acceptance criteria and summary carry the results]
- [x] CHK-041 [P1] Gallery captions and report section 8.16 [EVIDENCE: run report section 8.16 and both gallery READMEs]
<!-- /ANCHOR:docs -->

---

<!-- ANCHOR:file-org -->
## File Organization

- [x] CHK-050 [P1] No change outside the files named in spec.md Section 3 [EVIDENCE: beyond spec.md Section 3, the three vendored packages were pulled to clear the vendor gate, on the operator's answer]
<!-- /ANCHOR:file-org -->

---

<!-- ANCHOR:summary -->
## Verification Summary

| Category | Total | Verified |
|----------|-------|----------|
| P0 Items | 7 | 7 |
| P1 Items | 5 | 5 |
| P2 Items | 0 | 0 |

**Verification Date**: 2026-10-30
<!-- /ANCHOR:summary -->
