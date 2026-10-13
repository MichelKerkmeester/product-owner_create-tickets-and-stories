---
title: "Tasks: Phase 4, run the realistic playbook on Opus 5.5 medium"
description: "Task Format: T### [P?] Description (file path)"
trigger_phrases:
  - "opus run tasks"
  - "phase 4 verification"
  - "smoke run tasks"
  - "resume by scenario id"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.2 -->
# Tasks: Phase 4, run the realistic playbook on Opus 5.5 medium

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

`<run folder>` is `AI Systems/Product Owner/benchmark/reports/<run date>--manual-testing-playbook--claude-opus-5-5-medium/`. Commands for every task are in `plan.md` section 4.

- [x] T001 Confirm the operator's approval of the scenario plan is on record before anything runs (phase 003 record, `../goal.md` log) [EVIDENCE: Approval recorded in 003 implementation-summary.md and goal logs: 2026-09-25 19:31 UTC, Approve and run, against Product Owner 3023c5e and Barter c15c05e9]
- [x] T002 Record Barter and Product Owner HEADs, the `run/*.py` hashes and `claude --version`, and confirm the source paths are clean (`<run folder>/README.md`) [EVIDENCE: Product Owner 3023c5ecbdd418e41cdc0a1454dad6826becc2c0, Barter c15c05e947a063b7fa831d9c7d31002156ef8b6f, source status empty in both repos, claude 2.1.282, run/*.py sha256 check_run 4bc16f13, collect_exports 34427b7c, playbook_runner 868cad27, selftest 5e79b00f]
- [x] T003 Confirm no other runner is live on Product Owner, `pgrep -fl playbook_runner.py` printing nothing [EVIDENCE: pgrep -fl playbook_runner.py printed nothing]
- [x] T004 Put the `.gitignore` in place before the first stream is written (`<run folder>/.gitignore`) [EVIDENCE: .gitignore already in place from phase 003, ignoring *.jsonl, stderr, transcripts, failed-attempts/, exports/ and run-progress.txt]
- [x] T005 Dry run, and compare its scenarios, turns and attachments with the approved catalog (`scratch/dry-run.json`) [EVIDENCE: scratch/dry-run.json: 46 scenarios 86 turns 23 skill, 0 rows differing from the approved catalog in turns, wave or attachments, each attachment list equal to its scenario's bullet]
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T006 Smoke run `SID-001` and `PID-001` (`scratch/smoke/`) [EVIDENCE: scratch/smoke/, runner exit 0, SID-001 and PID-001 ok on attempt 1, 2 of 2 turns each]
- [x] T007 Check the smoke with `check_run.py --model claude-opus-5-5` and list every model name its streams carry (`scratch/smoke/run-log.jsonl`) [EVIDENCE: check_run names neither smoke ID, its 44 other findings are the unrun scenarios; every stream names claude-opus-5-5 alone]
- [x] T008 Widen the allowed model set only if T007 shows a second name, and record the stream, field and name (`<run folder>/run/check_run.py`, `<run folder>/README.md`) [EVIDENCE: No second model name in any stream, so check_run.py and the allowed set stay unchanged]
- [x] T009 Record cost and wall time per smoke turn and the estimate for the full run (`implementation-summary.md`) [EVIDENCE: Mean USD 0.57 and 36.3 s per smoke turn, about USD 49 and 52 minutes of turn time for 86 turns, recorded as a floor in implementation-summary.md]
- [x] T010 Full run of all 46 scenarios in waves 1 to 6, both sides, `--jobs 4` (`<run folder>/`) [EVIDENCE: runner exit 0, 46 scenarios on both sides, event time 19:35:44 to 20:06:05 UTC]
- [x] T011 Resume by `--ids` any scenario that failed for a harness or account cause, after moving its failed attempts aside, and record every other failure as a run defect (`<run folder>/run-status.json`, `<run folder>/README.md`) [EVIDENCE: Nothing to resume: 46 of 46 ok on attempt 1, no failed-attempts folder, no run defect]
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T012 `check_run.py --model claude-opus-5-5` on the run folder exits 0, and `run-status.json` holds 46 rows (`<run folder>/`) [EVIDENCE: check_run exit 0, 46 scenarios, 86 declared turns, 86 event streams read, 0 findings; run-status.json 46 rows 46 ok 0 retried]
- [x] T013 HEADs and source status unchanged since T002 (`<run folder>/README.md`) [EVIDENCE: Product Owner 3023c5e and Barter c15c05e9 after the run, source status empty]
- [x] T014 Collector dry run lists only new files, each a deliverable of this run (`scratch/collect-dry-run.txt`) [EVIDENCE: scratch/collect-dry-run.txt, 98 lines, 41 skill and 57 project, each naming one of the 46 IDs and a deliverable; export/benchmark held 0 files]
- [x] T015 Collect into `export/benchmark/` and review every Project extraction line against its reply (`AI Systems/Product Owner/export/benchmark/`) [EVIDENCE: 98 files collected, same as the dry run, no attachment warning; 41 skill files byte-identical to the runtime exports, 57 Project files each found verbatim in its reply, listed in the run README]
- [x] T016 Write the run record (`<run folder>/README.md`) [EVIDENCE: Run record in the run README: commits, hashes, CLI, model, effort, jobs, smoke, time, cost, retries, collection and the extraction review]
- [x] T017 Commit in the Product Owner public repo without attribution and in Barter with it, then push on the operator's go-ahead [EVIDENCE: Product Owner e9edb95 and Barter 7652158c, 319 paths each, no attribution line in either, no push; the push waits for the operator's go-ahead]
<!-- /ANCHOR:phase-3 -->

---

<!-- ANCHOR:completion -->
## Completion Criteria

- [x] All tasks marked `[x]`
- [x] No `[B]` blocked tasks remaining
- [x] `check_run.py --model claude-opus-5-5` exits 0 and the collection is committed
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

- [x] CHK-001 [P0] Operator approval of the scenario plan on record before T006 [EVIDENCE: Approval 19:31 UTC, smoke manifest written after it]
- [x] CHK-002 [P0] HEADs, harness hashes and CLI version recorded [EVIDENCE: Run README Sources and harness table]
- [x] CHK-003 [P1] No other Product Owner runner live, concurrency set to four [EVIDENCE: pgrep empty before the smoke and the full run, --jobs 4]
<!-- /ANCHOR:pre-impl -->

---

<!-- ANCHOR:code-quality -->
## Code Quality

- [x] CHK-010 [P0] No isolation proof failed, so the runner never exited 2 [EVIDENCE: runner exit 0 and no isolation problem in run-progress.txt]
- [x] CHK-011 [P0] Runner and collector used as phase 003 committed them [EVIDENCE: run/*.py sha256 unchanged from T002 and equal to the phase 003 commit]
- [x] CHK-012 [P1] `check_run.py` changed only on smoke evidence, with its diff in the run README [EVIDENCE: No change: every smoke stream named claude-opus-5-5 alone]
- [x] CHK-013 [P1] Retries and failed attempts counted [EVIDENCE: 0 retries, 0 failed attempts]
<!-- /ANCHOR:code-quality -->

---

<!-- ANCHOR:testing -->
## Testing Checklist

- [x] CHK-020 [P0] Smoke: both identity handovers whole, and no `check_run.py` finding names either [EVIDENCE: Both handovers 2 of 2 turns, the SID/PID grep on check_run output empty]
- [x] CHK-021 [P0] `check_run.py --model claude-opus-5-5` exits 0 on 46 scenarios [EVIDENCE: exit 0, 46 scenarios, 0 findings]
- [x] CHK-022 [P1] Single-turn scenarios confirmed single-turn by their files [EVIDENCE: 6 scenarios at 1 of 1: STK-001, SBG-001, SEP-003 and their twins, as their files declare]
- [x] CHK-023 [P1] Every failed turn listed with its cause [EVIDENCE: No failed turn]
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:fix-completeness -->
## Fix Completeness

- [x] CHK-FIX-001 [P0] Every run problem classed as runner, CLI, account or scenario [EVIDENCE: No run problem arose to class]
- [x] CHK-FIX-002 [P0] A problem seen on one side checked on the other [EVIDENCE: No one-sided problem arose]
- [x] CHK-FIX-003 [P0] No scenario that did not finish counted as run [EVIDENCE: 46 of 46 finished, turns_run equal to turns_declared in every row]
- [x] CHK-FIX-004 [P0] No output kept from a round whose isolation proof failed [EVIDENCE: No isolation proof failed]
- [x] CHK-FIX-005 [P1] Scenario and turn totals stated before completion [EVIDENCE: 46 scenarios and 86 turns stated in the run README]
- [x] CHK-FIX-006 [P1] Peer changes to the sources checked by HEAD and status before and after [EVIDENCE: HEADs and source status identical before the smoke and after the full run]
- [x] CHK-FIX-007 [P1] Evidence pinned to the recorded commits [EVIDENCE: Evidence pinned to Product Owner 3023c5e and Barter c15c05e9]
<!-- /ANCHOR:fix-completeness -->

---

<!-- ANCHOR:security -->
## Security

- [x] CHK-030 [P0] No credentials in any tracked file [EVIDENCE: The staged run files hold replies, meta and exports only, no credential]
- [x] CHK-031 [P0] Streams, stderr, transcripts, failed attempts and `exports/` copies ignored by the run folder's `.gitignore` [EVIDENCE: git status offers no jsonl, stderr, transcript, failed attempt, exports/ copy or progress file]
- [x] CHK-032 [P1] CLI ran without setting sources or MCP servers, and the public repo commit carries no attribution line [EVIDENCE: The runner passes empty --setting-sources and an empty --mcp-config under --strict-mcp-config; the public commit carries no attribution line]
<!-- /ANCHOR:security -->

---

<!-- ANCHOR:docs -->
## Documentation

- [x] CHK-040 [P1] Spec, plan and tasks synchronized [EVIDENCE: tasks.md evidence matches spec.md and plan.md step for step]
- [x] CHK-041 [P1] Run record complete in the run README [EVIDENCE: Run README written]
- [x] CHK-042 [P2] Wall time, cost and retry counts noted [EVIDENCE: USD 71.36, about 30 minutes, 0 retries]
<!-- /ANCHOR:docs -->

---

<!-- ANCHOR:file-org -->
## File Organization

- [x] CHK-050 [P1] Dry run, smoke output and listings kept in scratch/ [EVIDENCE: dry-run.json, smoke/, collect-dry-run.txt, collect.txt and check-run.txt in scratch/]
- [x] CHK-051 [P1] scratch/ cleaned before completion, with the smoke evidence summarized first [EVIDENCE: Smoke summarized in implementation-summary.md and the run README; smoke/ and the check listings kept as evidence the criteria cite]
<!-- /ANCHOR:file-org -->

---

<!-- ANCHOR:summary -->
## Verification Summary

| Category | Total | Verified |
|----------|-------|----------|
| P0 Items | 12 | 12/12 |
| P1 Items | 13 | 13/13 |
| P2 Items | 1 | 1/1 |

**Verification Date**: 2026-09-25
<!-- /ANCHOR:summary -->

---
