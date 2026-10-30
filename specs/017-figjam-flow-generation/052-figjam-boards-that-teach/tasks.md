---
title: "Tasks: Phase 52: FigJam boards that teach the reader something"
description: "Task Format: T### [P?] Description (file path). Verify: <command> prints <expected output>"
trigger_phrases:
  - "figjam boards that teach tasks"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.3 -->
# Tasks: Phase 52: FigJam boards that teach the reader something

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

- [x] T001 Scaffold this phase under the parent (`specs/017-figjam-flow-generation/052-figjam-boards-that-teach/`). Verify: `ls` lists the Level 2 docs and `goal.md`.
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T002 Checker: `%% about:`, detail levels on four types, the focus reason (`sk-create-figjam/scripts/`). Verify: the self-test and fixture suites pass. [EVIDENCE: flow_check --self-test 237 of 237, compose_board --self-test 1305 of 1305, with new fixtures for each rule and its refusal]
- [x] T003 Composer: notes under zone and lane titles, the compact key (`sk-create-figjam/assets/compose-board.js`). Verify: a scratch board shows both. [EVIDENCE: the traced board draws each zone's notes under its title and above its nodes and an 88 px key; the live Figma check moves to the first rerun board, see the goal log]
- [x] T004 Docs, templates and examples (`sk-create-figjam/references/`, `assets/`). Verify: every example checks clean. [EVIDENCE: every shipped model and its Project copy passes the self-test]
- [x] T005 Scorecard Substance and the ten scenarios (`sk-create-figjam/manual-testing-playbook/`). Verify: each scored scenario totals 24 and names two source questions. [EVIDENCE: root Section 3 defines Substance; each of the ten files carries Q4 and Q5 twice and 20 of 24 four times; FJ-047 moved to Balanced and Faithful]
- [x] T006 Release 1.0.17.0, hub 1.0.18.0 and the Claude Project mirror. Verify: parity passes. [EVIDENCE: changelogs, versions and SYNC.md; run_gates.sh 15 of 15; residency and divergence pass; parity runs on the commit]
- [ ] T007 Run the ten scenarios on `glm-5-3-flash-max` (`skill/glm-052/`). Verify: each run has a meta.json and a board.
- [ ] T008 Read and grade each board. Verify: twenty reader notes and ten scorecard rows.
- [ ] T009 Gallery, captions and report section 8.17. Verify: every caption names its run and score.
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [ ] T010 Redact, scan and run the gates. Verify: the scan prints nothing and `run_gates.sh` passes.
- [ ] T011 Commit both repositories, push on Michel's yes. Verify: `main` matches `origin`.
- [ ] T012 Validate this phase and the parent. Verify: `validate.sh --strict` prints `RESULT: PASSED`.
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

- [x] CHK-001 [P0] Requirements documented in spec.md [EVIDENCE: spec.md REQ-001 to REQ-009]
- [x] CHK-002 [P0] Technical approach defined in plan.md [EVIDENCE: plan.md Sections 1 and 3]
- [x] CHK-003 [P1] Approach and board maker confirmed by Michel [EVIDENCE: answers of 2026-10-30: skill and tests then rerun, child 052, GLM via Devin]
<!-- /ANCHOR:pre-impl -->

---

<!-- ANCHOR:code-quality -->
## Code Quality

- [x] CHK-010 [P0] Each new rule has a passing fixture and a refusal fixture [EVIDENCE: fixtures.py GOOD and PLANTED cases for about, Balanced bodies, state bodies, focus reasons]
- [x] CHK-011 [P1] The compact composer stays inside the Claude Project's room [EVIDENCE: two Project code blocks leave 8,188 characters for a graph model, the largest example needs 2,822]
<!-- /ANCHOR:code-quality -->

---

<!-- ANCHOR:testing -->
## Testing Checklist

- [ ] CHK-020 [P0] All acceptance criteria met
- [ ] CHK-021 [P0] Gates pass
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:security -->
## Security

- [ ] CHK-030 [P0] No board URL, Figma file key, plan name or email in any committed file
- [ ] CHK-031 [P0] Test sources name fictional brands only
<!-- /ANCHOR:security -->

---

<!-- ANCHOR:docs -->
## Documentation

- [ ] CHK-040 [P1] Spec, plan and tasks synchronized
- [ ] CHK-041 [P1] Changelog, captions and report section 8.17
<!-- /ANCHOR:docs -->

---

<!-- ANCHOR:file-org -->
## File Organization

- [ ] CHK-050 [P1] No change outside the files named in spec.md Section 3
<!-- /ANCHOR:file-org -->

---

<!-- ANCHOR:summary -->
## Verification Summary

| Category | Total | Verified |
|----------|-------|----------|
| P0 Items | 7 | 2 |
| P1 Items | 5 | 1 |
| P2 Items | 0 | 0 |

**Verification Date**: Pending
<!-- /ANCHOR:summary -->
