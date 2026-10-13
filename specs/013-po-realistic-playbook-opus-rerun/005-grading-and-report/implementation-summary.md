---
title: "Implementation Summary: Phase 5, grade the Opus run and write the report"
description: "Graded all 46 scenarios of the claude-opus-5-5 medium run, put every finding to the operator, carried two decided repairs and reran their scenarios in two remeasure rounds."
trigger_phrases:
  - "implementation summary"
  - "grading status"
  - "phase 5 grading done"
  - "continuation notes"
importance_tier: "normal"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "013-po-realistic-playbook-opus-rerun/005-grading-and-report"
    last_updated_at: "2026-09-26T05:10:00Z"
    last_updated_by: "claude-opus-5-5"
    recent_action: "Graded the run and both remeasure rounds and wrote the report"
    next_safe_action: "Commit the report, then push on the operator's go-ahead"
    blockers: []
    key_files: []
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "12f293fe-5421-46a0-b1ea-9fdc15ce0f8e"
      parent_session_id: null
    completion_pct: 95
    open_questions: []
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: impl-summary-core | v2.2 -->
# Implementation Summary

<!-- SPECKIT_LEVEL: 2 -->
<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

---

<!-- ANCHOR:metadata -->
## Metadata

| Field | Value |
|-------|-------|
| **Spec Folder** | 005-grading-and-report |
| **Status** | Complete |
| **Completed** | 2026-09-26 |
| **Level** | 2 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:what-built -->
## What Was Built

All 46 scenarios of the 2026-09-25 run are graded, each export has a realism entry, and the report sits in the run folder `AI Systems/Product Owner/benchmark/reports/2026-09-25--manual-testing-playbook--claude-opus-5-5-medium/`. The operator decided every finding that could move a verdict. Two repairs followed, and each reran its scenarios in its own graded round.

### Phase 5: grading-and-report

The main run grades skill 12 PASS and 11 FAIL, Project 8 PASS and 15 FAIL. The skill handover `SID-001` passes. The Project handover `PID-001` fails on a promise to write the task as a named file, so the other 22 Project rows carry `after_failed_gate` yes. Twenty rows failed because an explicit command drafted on Turn 1 instead of asking.

The first remeasure round (26 scenarios) shows the ask-first repair working on both sides: skill 7 PASS and 4 FAIL, Project 3 PASS and 12 FAIL. The Project still forecast a file in eight rows. The second round reran those eight on kernel v0.17.0: Project 5 PASS and 3 FAIL, with `PID-001` passing. A read-only investigation then traced each remaining value miss to its cause, the operator decided the changes, and a third round reran the 12 affected scenarios on skill 0.14.0: skill 6 PASS and Project 6 PASS.

### Operator decisions

| Date | Finding | Decision |
|------|---------|----------|
| 2026-09-25 | An explicit command drafted on Turn 1 when the attachments were rich | The command always asks first |
| 2026-09-25 | The Project Epics left out `#### **References**` with no link supplied | Optional without a supplied link |
| 2026-09-25 | The Project promised to write a file | A promise is a file claim |
| 2026-09-25 | `SDK-001` and `PDK-001` expected a question no rule requires | The scenario is wrong |
| 2026-09-25 | Kernel line 101 forbade claiming a save but not promising one | Tighten line 101 |
| 2026-09-25 | `SBG-003` labels a cause as an unverified hypothesis | Allowed |
| 2026-09-25 | The skill bugs assert "No error message is shown" with no source | Advisory, and the template slot is repaired |
| 2026-09-25 | The runbooks turn incident details into general "Expected result" lines | Allowed as runbook steps |
| 2026-09-26 | The Project still forecast the next artifact's file in eight rows of the first round | Repair once more |
| 2026-09-26 | `PST-003` Turn 1 says "I'll keep the draft's original filename" | It is a file claim, and `PST-003` stays FAIL |
| 2026-09-26 | Rows still missing a supplied value after round one | Find the source cause, propose rule changes, then rerun those rows |
| 2026-09-26 | A backticked Pass-clause value was graded word for word though the root never said so | Word for word only where the source backticks it, gives it as a defined label or the clause says verbatim |
| 2026-09-26 | Task Mode had no rule carrying supplied values unchanged | Add one Task Mode rule for values, names and status words |
| 2026-09-26 | Doc and Story rules let the Behavior rules heading, a backticked rule phrase and an open question be reworded | All three rule changes |
| 2026-09-26 | `TK-003` demanded retry values no agreed point uses, and the board in the task | Relax the clause |
| 2026-09-26 | `PDK-003` states `not decided` in other words | Other words meet it, and the row stays PASS |

One reading was settled from the evidence without a ruling: `Status: Approved direction` is a Doc Mode status class (`doc-mode.md` line 146), not an invented approval.

### Files Changed

| File | Action | Purpose |
|------|--------|---------|
| `<run folder>/results.csv`, `results.md`, `grading-notes.md`, `hvr-lint.csv` | Create | The 46 verdicts, their tables, the evidence and the reply lint |
| `<run folder>/README.md` | Modify | Handover status, counts with their command, decisions, both rounds and next steps above the run record |
| `<run folder>/remeasure-operator-repairs/run-1/` | Create | Round one: 26 scenarios, replies, results and grading notes |
| `<run folder>/remeasure-file-forecast/run-1/` | Create | Round two: 8 scenarios, replies, results and grading notes |
| `<run folder>/remeasure-supplied-values/run-1/` | Create | Round three: 12 scenarios, replies, results and grading notes |
| `AI Systems/Product Owner/export/benchmark/<side>/remeasure-*/` | Create | 102 collected round deliverables |
| `sk-product-owner/`, `claude project/`, `AGENTS.md`, `SYNC.md`, the playbook | Modify | The decided repairs, committed as Product Owner `39bcd29`, `b591571` and `b50f0a0`, Barter `df2de5f0`, `e9eec279` and `7396d79e` |
<!-- /ANCHOR:what-built -->

---

<!-- ANCHOR:how-delivered -->
## How It Was Delivered

Opus 5.5 graders drafted the evidence in six batches for the main run, with both twins of a pair in the same batch, then three batches for round one and one for round two. Each worked from a grading brief pinned to the run's commit. The orchestrator checked every draft row against its evidence, read every FAIL a second time and regraded one draft (`PDK-003` in round one) to keep backticked values graded word for word. The findings went to the operator through the ask tool in batches, and no source changed before its decision.

The first repair (skill 0.12.0, kernel v0.16.0, playbook 2.1.0.0) and the second (skill 0.13.0, kernel v0.17.0, playbook 2.1.1.0) each passed the format gate, the playbook validator (46 scenarios, 0 violations) and the run selftest (7 of 7) on the working tree, and parity (38 of 38) and residency on the commit. Each round ran through the same runner at effort medium, then `check_run.py`, the collector dry run and the collection.
<!-- /ANCHOR:how-delivered -->

---

<!-- ANCHOR:decisions -->
## Key Decisions

| Decision | Why |
|----------|-----|
| One grader batch per folder group, with both twins of every pair in the same batch | The grader that judges a pair reads both sides with one reading, so a twin disagreement comes from the runtimes and not from two graders |
| The realism review sits in `grading-notes.md`, one entry per export | Its Blocking items decide verdicts, so its evidence belongs beside the verdicts it decides |
| The main `results.csv` stays the verdicts of record, and each round keeps its own | A round reruns a subset on changed sources, so mixing its rows in would grade two versions as one |
| A forward statement attaching an `export/` path or the word file to the next artifact is a file claim, and naming only the next number is not | One dividing line for every batch, so the same sentence never passes in one batch and fails in another |
<!-- /ANCHOR:decisions -->

---

<!-- ANCHOR:verification -->
## Verification

| Check | Result |
|-------|--------|
| README count command, rerun | Every number equal: skill 12 and 11, Project 8 and 15, `facts_intact` yes 38 of 46, `after_failed_gate` yes 22, 4 of 23 twins differ |
| `results.md` against `results.csv` | 46 verdict rows and 23 twin rows, no cell differs |
| `bash benchmark/grader/check_report.sh <run folder>` | Exit 2, both checks ran and reported findings: 78 of 86 replies lint-dirty, 4 twins differ, all in `grading-notes.md` section 2 |
| `check_run.py` on each round | No finding for any scenario the round ran; the rest name the scenarios left out |
| `find export/benchmark -type f` in the Product Owner folder | 200 at close, each with a realism entry. 98 since the operator removed the round files on 2026-09-26 |
| Third repair gates | Format gate exit 0, validator 46 scenarios 0 violations, selftest 7 of 7, parity 38 of 38 and residency pass on `7396d79e` |
<!-- /ANCHOR:verification -->

---

<!-- ANCHOR:limitations -->
## Known Limitations

1. **Kernel review pending.** The operator's review has been pending since kernel v0.14.0, and the text now stands at v0.17.0. Nothing is deployed to claude.ai.
2. **`PST-004` not repaired.** The Project settles the task split from the brief instead of asking for it, against a rule both packagings state. It is recorded as a runtime fault, and no repair was proposed.
<!-- /ANCHOR:limitations -->

---
