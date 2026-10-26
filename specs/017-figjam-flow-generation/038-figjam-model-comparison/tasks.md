---
title: "Tasks: Phase 38: figjam-model-comparison"
description: "Task Format: T### [P?] Description (file path)"
trigger_phrases:
  - "figjam model comparison tasks"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.2 -->
# Tasks: Phase 38: figjam-model-comparison

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

**Task Format**: `T### [P?] Description (file path)`
<!-- /ANCHOR:notation -->

---

<!-- ANCHOR:phase-1 -->
## Phase 1: Setup

- [x] T001 Write the spec folder and add row 38 to the parent phase table (spec.md)
- [x] T002 Copy the Devin runner into the run folder and write the adaptive driver and batch script (run/)
- [x] T003 Probe Figma's whoami on each of the three models through Devin
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T004 Run FJ-022 to FJ-028 on DeepSeek V4.1 Flash max through Devin (skill/deepseek/)
- [x] T005 Run FJ-022 to FJ-028 on SWE 2 Max through Devin (skill/swe/)
- [x] T006 Run FJ-022 to FJ-028 on GLM 5.3 Flash max through Devin (skill/glm/)
- [x] T007 Render every written board at overview, 100% and greyscale (23 renders each, the overview set kept in renders/)
- [x] T008 [P] Give fresh readers the colour renders and the questions (grades/), three readers rotated across the models as the ADR-003 note records
- [x] T009 [P] Grade each type's three boards on the 22-point scorecard (grades/)
- [x] T010 Write results.jsonl and the run README with the per-type and per-model result
- [x] T011 Replace the seven type images with the best board per type and update the captions (sk-create-figjam/assets/screenshots/, README.md, sk-create-figjam/README.md)
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T012 Redact the run folder and scan it and every changed file for the file key, board URLs, plan names and emails
- [x] T013 Run the benchmark gates and validate.sh --strict on this folder and the parent
<!-- /ANCHOR:phase-3 -->

---

<!-- ANCHOR:phase-4 -->
## Phase 4: Findings

The operator reopened the phase on 2026-10-26 to fix the six findings in the run README Section 7.

- [x] T014 Reopen this folder: status, scope, REQ-006 to REQ-011, AC-006 to AC-011 and ADR-005 (spec.md, acceptance-criteria.md, decision-record.md)
- [x] T015 Delete only on a reply that names the boards, and the missing `fileKey` recovery (sk-create-figjam/references/flow-mode.md)
- [x] T016 Require every expected signal in each board-quality PASS line (sk-create-figjam/manual-testing-playbook/)
- [x] T017 Rank the gallery on the board points first, rebuild `results.jsonl` and swap any image the rule changes (run/aggregate.py, sk-create-figjam/assets/screenshots/)
- [x] T018 Read a board id from any `use_figma` result (run/adaptive_compare.py)
- [x] T019 Draw gantt dependency arrows and ER end marks, with their fixtures and self-test checks (assets/compose-board.js, scripts/)
- [x] T020 Write the gantt, ER and state guidance (references/types/, assets/examples/state-roamstay-booking.md)
- [x] T021 Hand-write the Project mirror, the SYNC note and the changelogs (claude project/knowledge/, SYNC.md, changelog/)
- [x] T022 Compose a gantt and an ER board on the test file and read the renders
- [x] T023 Run every gate, a fresh review and validate.sh --strict, then close
- [x] T024 Draw the gantt, ER, existing-board and dense-flow gallery boards again from their best run's model and update the captions (sk-create-figjam/assets/screenshots/, sk-create-figjam/README.md)
- [x] T025 Add Codex and Claude Code turn backends to the driver, each in the runner's sandbox and seatbelt with only Figma reachable (run/runtimes.py, run/adaptive_compare.py, run/run_more.sh)
- [x] T026 Run FJ-022 to FJ-028 on GPT 6 Luna max fast and Claude Opus 5.5 low on today's skill [EVIDENCE: 14 runs in skill/luna/ and skill/opus-low/, each meta.json completed, placement check clean]
- [x] T027 Render and grade the fourteen boards with one fresh Opus 5.5 medium grader, ranked against the first run's boards [EVIDENCE: grades/luna-opus-low.jsonl 14 rows, totals recomputed 142 and 139]
- [x] T028 Report the five-model result to the operator before any further run [EVIDENCE: reported 2026-10-26, the operator chose Claude Opus 5.5 medium for the full run]
- [x] T029 Note how a Claude Code or Codex child reaches Figma's hosted server, in the vendored wiring guide from Code_Environment `mcp-tooling/025-figma-hosted-from-cli-children` and in the hosted-connection paragraph (mcp-figma/, sk-create-figjam/references/flow-mode.md, SYNC.md)
- [x] T030 Run all 54 FigJam playbook scenarios on Claude Opus 5.5 medium through Claude Code, new files only in drafts of the Barter team plan (run/run_full.sh) [EVIDENCE: the operator stopped the run after 24 scenarios, skill/opus-medium/ holds 24 completed runs]
- [x] T031 Render every board the full run drew and redact, scan and commit the run [EVIDENCE: 20 renders in renders/opus-medium-*, leak scan 0 hits on 511 files]
- [x] T032 Report the full run to the operator with the board per template [EVIDENCE: reported 2026-10-26 with a private gallery page of the 20 boards]
- [x] T033 Compare each gallery type image with the day's best Luna, Opus 5.5 low and Opus 5.5 medium boards and swap any a fresh judge prefers (sk-create-figjam/assets/screenshots/, sk-create-figjam/README.md) [EVIDENCE: the judge kept six images and swapped state for Opus 5.5 medium's FJR-005 board, 13 of 14 visible points against 10]
<!-- /ANCHOR:phase-4 -->

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
- **Decisions**: See `decision-record.md`
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

- [x] CHK-001 [P0] Requirements documented in spec.md [EVIDENCE: REQ-001 to REQ-005 in spec.md, each with an acceptance row]
- [x] CHK-002 [P0] Technical approach defined in plan.md [EVIDENCE: plan.md and the four decision records]
- [x] CHK-003 [P1] Dependencies identified and available [EVIDENCE: Devin 3000.11.205 with Figma's hosted server, Figma whoami answered on all three models, Code Mode for the renders]
<!-- /ANCHOR:pre-impl -->

---

<!-- ANCHOR:code-quality -->
## Code Quality

- [x] CHK-010 [P1] The driver reuses the runners' sandbox, isolation proof and redaction unchanged [EVIDENCE: cmp finds run/devin_playbook_runner.py identical to the 2026-10-24 copy and run/redact_run.py identical to the first-glance run's copy]
<!-- /ANCHOR:code-quality -->

---

<!-- ANCHOR:testing -->
## Testing Checklist

- [x] CHK-020 [P0] All acceptance criteria met [EVIDENCE: AC-001 to AC-011 Met in acceptance-criteria.md]
- [x] CHK-021 [P1] Every written board has its three renders and a scorecard [EVIDENCE: 23 overview, 23 full and 23 greyscale renders, and 21 rows in results.jsonl each with a scorecard]
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:security -->
## Security

- [x] CHK-030 [P0] No secrets, board URLs, Figma file keys, plan names or emails in any changed file [EVIDENCE: the leak scan reads 0 hits on every scenario commit and on the grades, and the one README hit is the repository owner's name in the existing badges]
<!-- /ANCHOR:security -->

---

<!-- ANCHOR:docs -->
## Documentation

- [x] CHK-040 [P1] Spec, plan, tasks and decision record synchronized [EVIDENCE: ADR-003 carries the as-run reader note, and T008 points at it]
<!-- /ANCHOR:docs -->

---

<!-- ANCHOR:file-org -->
## File Organization

- [x] CHK-050 [P1] No change outside the files named in spec.md Section 3 [EVIDENCE: the commits touch the run folder, sk-create-figjam/assets/screenshots/, the two READMEs, the reports index and this folder]
<!-- /ANCHOR:file-org -->

---

<!-- ANCHOR:findings -->
## Findings

- [x] CHK-060 [P0] Flow Mode never deletes on a bare yes [EVIDENCE: `references/flow-mode.md` Section 6 bullet "A delete of anything that was on the file before this write runs only on a reply that names the boards it removes", the rollback and revision bullets and Section 9's read-back step all name the board, mirrored in Templates - Flow Mode]
- [x] CHK-061 [P1] Each board-quality PASS line names the expected signals [EVIDENCE: "every expected signal is present" twice in each of the nine board-quality and eight board-creation files, and root playbook Section 3 ties the scorecard to Section 5]
- [x] CHK-062 [P1] The composer still fits one `use_figma` call with the largest planted model [EVIDENCE: `compose_board.py --self-test` 1029 of 1029, the largest planted model fits, and `--design-check` leaves 2,869 characters for the model]
- [x] CHK-063 [P1] A live gantt and ER board show the arrows and the end marks [EVIDENCE: on the operator-approved test file, gantt 147:5390 drew 6 nodes and 5 connectors with 0 warnings and ER 148:5423 drew 6 nodes and 6 connectors with 0 warnings. Both renders show the arrows and the crow's-foot marks. One gantt arrow crosses a bar end, recorded as a known limitation]
<!-- /ANCHOR:findings -->

---

<!-- ANCHOR:summary -->
## Verification Summary

| Category | Total | Verified |
|----------|-------|----------|
| P0 Items | 5 | 5/5 |
| P1 Items | 8 | 8/8 |
| P2 Items | 0 | 0/0 |

**Verification Date**: 2026-10-26
<!-- /ANCHOR:summary -->
