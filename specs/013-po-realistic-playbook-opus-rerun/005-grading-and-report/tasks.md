---
title: "Tasks: Phase 5, grade the Opus run and write the report"
description: "Task Format: T### [P?] Description (file path)"
trigger_phrases:
  - "grading tasks"
  - "phase 5 verification"
  - "realism review tasks"
  - "packet closure tasks"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.2 -->
# Tasks: Phase 5, grade the Opus run and write the report

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

- [x] T001 Take the commits from the phase 004 run record and extract the root, scenario files, rule sources and fixtures at them with `git show` (`scratch/root-at-run.md`, `scratch/sources-at-run.txt`) [EVIDENCE: Run record names Product Owner 3023c5e and Barter c15c05e9; scratch/root-at-run.md from git show 3023c5e (1074 lines) and scratch/sources-at-run.txt (72 paths)]
- [x] T002 List the 23 twin pairs and each scenario's folder group from the playbook at the run's commit [EVIDENCE: scratch/twin-pairs.txt, 23 pairs with each side's folder and file]
- [x] T003 List every file in `export/benchmark/` and count the event streams against the declared turns (`scratch/exports.txt`) [EVIDENCE: scratch/exports.txt, 98 files; 86 event streams for 86 declared turns]
- [x] T004 Write the grading brief: commits, root sections, verdict rule, addition-naming rule, realism rubric, evidence rule and `results.csv` row contract (`scratch/grading-brief.md`) [EVIDENCE: scratch/grading-brief.md: paths and commits, the root sections by line, the verdict, addition-naming, protected-fact, delivery-proof, format-gate and realism rules, and the nine-column row contract]
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T005 [P] Grade identity: `SID-001` and `PID-001` [EVIDENCE: scratch/grades/identity-interactive.md, joined with the interactive batch: SID-001 and PID-001 graded, PID-001 regraded FAIL under the file-promise ruling]
- [x] T006 [P] Grade backlog: `STK-001` to `STK-006`, `SBG-001` to `SBG-003` and their twins [EVIDENCE: Graded as two batches, scratch/grades/tasks.md (12 scenarios) and scratch/grades/bugs.md (6), to balance the load, logged as a deviation]
- [x] T007 [P] Grade document: `SDK-001` to `SDK-004` and their twins [EVIDENCE: scratch/grades/docs.md, 8 scenarios]
- [x] T008 [P] Grade story: `SST-001` to `SST-004`, `SEP-001` to `SEP-003` and their twins [EVIDENCE: Graded as two batches, scratch/grades/stories.md (8 scenarios) and scratch/grades/epics.md (6)]
- [x] T009 [P] Grade interactive routing: `SIR-001`, `SIR-002` and their twins [EVIDENCE: scratch/grades/identity-interactive.md, SIR-001, SIR-002 and their twins]
- [x] T010 Review every draft verdict against its evidence, settle each cross-batch reading once and read every FAIL a second time (`<run folder>/grading-notes.md`) [EVIDENCE: Every draft row checked against its evidence; all 20 early-draft FAILs confirmed against their Turn 1 Pass clause and the absent clarification; each cross-batch reading settled once or put to the operator; every FAIL read twice (grading-notes.md sections 1 and 3)]
- [x] T011 Write the 46 rows (`<run folder>/results.csv`) [EVIDENCE: results.csv: 46 rows, nine columns in order, model claude-opus-5-5-medium only]
- [x] T012 Run `check_report.sh` and fold its findings into the grading (`<run folder>/hvr-lint.csv`, `<run folder>/grading-notes.md`) [EVIDENCE: check_report.sh exit 2, both checks reporting findings and neither unable to run: 78 of 86 replies lint-dirty, 4 twins differ; folded into grading-notes.md section 2]
- [x] T013 Classify every twin disagreement and confirm each on both sides (`<run folder>/grading-notes.md`) [EVIDENCE: Four differing pairs classed in grading-notes.md section 3, each checked in both packagings: DK-003 runtime fault, ID-001, IR-002 and EP-002 a Project rule gap now repaired]
- [x] T014 Write the realism review, one entry per export (`<run folder>/grading-notes.md`) [EVIDENCE: One realism block per scenario, 46 in all, each with an entry per export or block, in grading-notes.md sections 5 to 10]
- [x] T015 Write the verdict and twin tables, and the README with any handover failure first and the count command (`<run folder>/results.md`, `<run folder>/README.md`) [EVIDENCE: results.md 46 verdict rows and 23 twin rows, each cell matching results.csv; README sections 1 handover, 2 counts with the command, 3 findings and decisions, 4 remeasure rounds, 5 next steps, above the run record]
- [x] T016 Put every finding to the operator through the ask tool and record each decision (`implementation-summary.md`) [EVIDENCE: Seven findings put through AskUserQuestion in three rounds on 2026-09-25, each answered; one reading settled from evidence (Approved direction, doc-mode.md line 146); all recorded in implementation-summary.md and grading-notes.md section 1]
- [x] T017 Add each decided repair below as its own tasks, naming its source files, mirrors and the rerun of its scenarios into a `remeasure-<slug>/run-<n>/` round (`tasks.md`) [EVIDENCE: T024 to T032 added below]

### Decided repairs, operator rulings of 2026-09-25

- [x] T024 Explicit command always asks: give `bug-mode.md` line 61, `story-mode.md` line 64 and `doc-mode.md` line 67 the explicit-command exception `task-mode.md` line 50 carries, add `$epic` and the short aliases to `AGENTS.md` line 287, then the kernel line 108 and the Bug, Story and Doc Mode mirrors (`AI Systems/Product Owner/sk-product-owner/references/`, `AI Systems/Product Owner/claude project/`) [EVIDENCE: AGENTS.md 287 and kernel 108 list $epic and every alias; bug-mode 61, story-mode 64, doc-mode 67 and their mirrors carry the explicit-command exception; SKILL.md 252 and interactive-mode aligned in place]
- [x] T025 Epic References optional without a supplied link, as the Story rule already says: `assets/epic-template.md`, the Epic part of `story-mode.md`, kernel line 140, the Epic Template and Story Mode mirrors, and every Epic scenario clause that requires the block (`AI Systems/Product Owner/sk-product-owner/`, `AI Systems/Product Owner/claude project/`) [EVIDENCE: epic-template.md 74, story-mode.md 206, kernel 140 and both mirrors omit References with no supplied link; six Epic scenarios updated]
- [x] T026 A promise to write or save a file is a file claim: root lines 179 and 189 and kernel line 101, each edited in place (`manual-testing-playbook.md`, `Custom Instructions.md`) [EVIDENCE: Root 179 and 189 and kernel 101 name a promise to write or save a file as a file claim, each edited in place]
- [x] T027 `SDK-001` and `PDK-001` expect a direct draft on Turn 1, since no rule requires the question for a request with no command, and Turn 2 becomes a follow-up change request (`skill-document-modes/behavior-reference.md`, `project-document-modes/behavior-reference.md`) [EVIDENCE: SDK-001 and PDK-001 at 2.0.0.0: Turn 1 kept word for word and expected to draft at once, Turn 2 a follow-up change, in-place versus next number left ungraded since no rule settles it]
- [x] T031 `SBG-003` and `PBG-003` say "no root cause" means none stated as fact, a labelled unverified hypothesis allowed as root line 187 says (`skill-backlog-modes/two-platform-log-bug.md`, `project-backlog-modes/two-platform-log-bug.md`) [EVIDENCE: SBG-003 and PBG-003 at 1.1.0.0 read no root cause stated as fact, a labelled hypothesis allowed]
- [x] T032 The bug template's error-message slot reads `Not provided` or is left out when no error message is supplied, in the skill asset and its Project mirror (`assets/bug-report-template.md`, `Product Owner - Assets - Bug Report Template`) [EVIDENCE: bug-report-template.md 105, bug-mode.md 158 and 217 and their mirrors: Not provided or left out when no error message is supplied]
- [x] T028 Versions, mirror renames, changelog and a dated `SYNC.md` note with the kernel review pending, then the format gate, the playbook validator and the run selftest, a commit in both repos, and parity and residency on the commit [EVIDENCE: Skill 0.12.0, kernel v0.16.0, seven mirrors renamed, changelog v0.12.0.0, SYNC.md note with the kernel review pending; format gate passed across 40 files, validator 46/0/0, selftest 7/7; Product Owner 39bcd29 and Barter df2de5f0 with no attribution line; parity 38/38 and residency pass on the commit]
- [x] T029 Remeasure round `remeasure-operator-repairs/run-1` from the run folder: both twins of `TK-002` to `TK-005`, `BG-002`, `DK-001`, `DK-003`, `ST-002` to `ST-004` and `EP-001`, plus `PID-001`, `PEP-002`, `PTK-006` and `PIR-002`, 26 scenarios, then `check_run.py`, the collector dry run and the collection into `export/benchmark/` [EVIDENCE: remeasure-operator-repairs/run-1 on Product Owner 39bcd29 and Barter df2de5f0: runner exit 0, 26 of 26 ok on attempt 1, 52 turns, claude-opus-5-5 alone, USD 37.36; check_run's 20 findings are the 20 scenarios outside the round; collector dry run 157 lines, 59 new, then 157 files collected with the main run's 98 unchanged and no warning]
- [x] T033 Stop the Project forecasting a file: kernel line 101 states the rule without quoting the bad example, and the clarification reporting rule in `interactive-mode.md` line 93 and its mirror says the artifact comes next without naming its path, kernel v0.17.0, skill 0.13.0, root 2.1.1.0, then commit in both repos with parity and residency on the commit [EVIDENCE: Kernel NEVER 3 without the quoted example, kernel 228 and interactive-mode.md 93 with its mirror say the artifact comes next without naming its path; Product Owner b591571 and Barter e9eec279 with no attribution line; format gate, validator 46/0/0, selftest 7/7, parity 38/38 and residency pass]
- [x] T034 Second round `remeasure-file-forecast/run-1`: `PID-001`, `PBG-002`, `PTK-005`, `PTK-006`, `PST-003`, `PST-004`, `PEP-001` and `PEP-002`, then `check_run.py`, the collector dry run and the collection [EVIDENCE: remeasure-file-forecast/run-1 on Product Owner b591571 and Barter e9eec279: runner exit 0, 8 of 8 ok on attempt 1, 16 turns, claude-opus-5-5 alone, USD 10.38; check_run's 38 findings are the scenarios outside the round; 20 deliverables collected, 177 files in export/benchmark with earlier files unchanged and no warning]
- [x] T035 Grade the second round and report both rounds beside the main results [EVIDENCE: remeasure-file-forecast/run-1/results.csv 8 rows (Project 5 PASS 3 FAIL, PID-001 PASS, after_failed_gate no throughout) and grading-notes.md with the orchestrator review; README section 4 reports both rounds, the main results.csv unchanged]
- [x] T030 Grade the round like the main run and report it beside the main results, the main `results.csv` unchanged by it [EVIDENCE: remeasure-operator-repairs/run-1/results.csv 26 rows (skill 7 PASS 4 FAIL, Project 3 PASS 12 FAIL) and grading-notes.md with the orchestrator review; PDK-003 regraded FAIL for a reworded backticked value]
### Content-miss repair, operator choice of 2026-09-26

- [x] T036 Find the source cause of each value still dropped or reworded after round one: `TK-003` both twins, `STK-005`, `TK-006` both twins, `SDK-001`, `PDK-001`, `PDK-003` and `ST-002` both twins, read-only, three Opus investigators on one brief (`scratch/miss-cause-brief.md`, `scratch/miss-causes-*.md`) [EVIDENCE: miss-causes-tk003.md, miss-causes-tk005-tk006.md and miss-causes-docs-story.md: rule gap for HMAC-SHA256, deprecated, proposed, booking-service, the Behavior rules heading and the backticked rule phrase; rule conflict for the open question (story-mode.md line 80); scenario defect for 5 attempts, the retry schedule, the board placement, 1 to 99 and block-level last-writer-wins, where the word-for-word reading is a grading convention the root never states]
- [x] T037 Verify every cited line in the investigators' returns, then put each proposed change to the operator through the ask tool [EVIDENCE: Sampled citations in all three files resolve to the quoted text; four decisions through AskUserQuestion on 2026-09-26: grade word for word only where the source or clause marks the value, add the Task rule, all three Doc and Story rules, relax TK-003]
- [x] T038 Carry each decided change into the skill source first, then its Project counterpart, with versions, changelog and a dated `SYNC.md` note, the kernel review still pending [EVIDENCE: Task Mode, Doc Templates and Story Mode edited on both sides, each on its existing line; mirrors renamed to v0.306, v0.108 and v0.404 with 62 live references repointed; skill 0.14.0, changelog v0.14.0.0, SYNC.md note with the kernel review pending, kernel unchanged at v0.17.0; root 2.2.0.0 and three scenario pairs at 1.1.0.0]
- [x] T039 Format gate, playbook validator, run selftest, commit in both repos without attribution, then parity and residency on the commit [EVIDENCE: Format gate exit 0 with no finding on an edited line, validator 46 scenarios 0 violations, selftest 7 of 7; Product Owner b50f0a0 and Barter 7396d79e without attribution; parity 38/38 and residency pass on the commit]
- [x] T040 Rerun the affected rows into a graded `remeasure-<slug>/run-1/` round, collect its deliverables, and report it beside the earlier rounds [EVIDENCE: remeasure-supplied-values/run-1: 12 of 12 ok on attempt 1, 24 turns, claude-opus-5-5 alone, USD 18.90; check_run's 34 findings are the scenarios outside the round; 23 deliverables collected, export/benchmark at 200 with earlier files unchanged; two Opus graders, orchestrator review with every cited line checked; results.csv 12 rows, skill 6 PASS, Project 6 PASS; PDK-003 status reading ruled by the operator 2026-09-26, PASS stands; README sections 3 and 4 report the repair and the round]
- [x] T041 Push on the operator's go-ahead [EVIDENCE: Operator go-ahead 2026-09-26; Product Owner 01200fa..3fdce37 and Barter 3b55bfbe..d214c160 pushed, gh switched back]
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T018 Recompute every count in the report from `results.csv` (`<run folder>/README.md`) [EVIDENCE: The README count command prints project FAIL 15, project PASS 8, skill FAIL 11, skill PASS 12, facts_intact yes 38 of 46, after_failed_gate yes 22, twin pairs differing 4 of 23, each equal to the README; both rounds' counts equal their results.csv; check_report.sh exit 2 with the same 4 differing twins]
- [x] T019 `validate.sh --recursive` on the packet reports 0 errors [EVIDENCE: validate.sh --recursive --strict on the packet: Errors 0 in every folder after the commits]
- [x] T020 Every phase's `acceptance-criteria.md` reads `Closeable: Yes` [EVIDENCE: grep -L for Closeable: Yes over 0*/acceptance-criteria.md prints nothing]
- [x] T021 Check each parent goal completion criterion with fresh output and log it (`../goal.md`) [EVIDENCE: Parent goal.md log rows of 2026-09-26, one per completion criterion, each from fresh output]
- [x] T022 Commit in the Product Owner public repo without attribution and in Barter with it, then push on the operator's go-ahead [EVIDENCE: Product Owner 01200fa and Barter 3b55bfbe, no attribution line in either; pushed on the operator's go-ahead, a02f3b2..01200fa and 0545f2a4..3b55bfbe via the barter account, gh switched back]
- [x] T023 Confirm the kernel review is still pending unless the operator confirmed it (`AI Systems/Product Owner/SYNC.md`) [EVIDENCE: The operator answered Still pending on 2026-09-26; SYNC.md notes still say the review is pending and none marks it done]
<!-- /ANCHOR:phase-3 -->

---

<!-- ANCHOR:completion -->
## Completion Criteria

- [x] All tasks marked `[x]` [EVIDENCE: T001 to T035 all checked]
- [x] No `[B]` blocked tasks remaining [EVIDENCE: None]
- [x] Report committed and every parent goal criterion checked with fresh output [EVIDENCE: 01200fa and 3b55bfbe pushed; parent log rows of 2026-09-26]
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

- [x] CHK-001 [P0] Phase 004 closed and its commits recorded [EVIDENCE: Phase 004 Closeable Yes, Product Owner e9edb95 and Barter 7652158c]
- [x] CHK-002 [P0] Grading brief written from the sources at the run's commit [EVIDENCE: scratch/grading-brief.md from git show at 3023c5e, with addenda for 39bcd29 and b591571]
- [x] CHK-003 [P1] Twin pairs, folder groups and the export list written down [EVIDENCE: scratch/twin-pairs.txt and scratch/exports.txt]
<!-- /ANCHOR:pre-impl -->

---

<!-- ANCHOR:code-quality -->
## Code Quality

- [x] CHK-010 [P0] Every scenario has one verdict with its evidence [EVIDENCE: results.csv 46 rows, each note citing its evidence; rounds 26 and 8 rows]
- [x] CHK-011 [P0] No PASS on a scenario with a turn that missed a Pass clause [EVIDENCE: Every PASS checked clause by clause in the drafts; PDK-003 regraded FAIL in round one on a reworded value]
- [x] CHK-012 [P0] Every verdict reviewed by the orchestrator before it was written [EVIDENCE: Review sections in all three grading-notes.md files]
- [x] CHK-013 [P1] Report prose follows the voice rules, no em dashes [EVIDENCE: 0 em dashes in README, results.md and all three grading-notes.md heads]
- [x] CHK-014 [P1] `results.csv` uses the header of the 2026-09-25 Sonnet report [EVIDENCE: id,runtime,model,result,turns_run,turns_declared,after_failed_gate,facts_intact,note in all three results.csv]
<!-- /ANCHOR:code-quality -->

---

<!-- ANCHOR:testing -->
## Testing Checklist

- [x] CHK-020 [P0] `check_report.sh` ran with both checks executing [EVIDENCE: Exit 2, both checks reported findings, neither unable to run]
- [x] CHK-021 [P0] Every count recomputed from `results.csv` [EVIDENCE: README count command rerun, every number equal; results.md cell for cell]
- [x] CHK-022 [P0] One realism entry per file in `export/benchmark/` [EVIDENCE: 200 files at close, 98 main entries and 59, 20 and 23 round entries. 98 since the operator removed the round files on 2026-09-26]
- [x] CHK-023 [P0] `validate.sh --recursive` reports 0 errors and every phase is closeable [EVIDENCE: Errors 0; every phase Closeable Yes]
- [x] CHK-024 [P1] Every twin disagreement classified and confirmed on both sides [EVIDENCE: grading-notes.md section 3, four pairs]
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:fix-completeness -->
## Fix Completeness

- [x] CHK-FIX-001 [P0] Every FAIL names its rule and the file that states it at the run's commit [EVIDENCE: Each FAIL note names its Pass clause or root and source line at its round's commit]
- [x] CHK-FIX-002 [P0] A failure pattern seen on one side checked on the other [EVIDENCE: Twin table and cause column in grading-notes.md section 3; the file forecast checked as Project-only]
- [x] CHK-FIX-003 [P0] Every disagreement tested from a second direction [EVIDENCE: Each disagreement read in both packagings' rule files]
- [x] CHK-FIX-004 [P0] No source file edited without the operator's decision [EVIDENCE: 39bcd29 and b591571 each follow their decisions of 2026-09-25 and 2026-09-26]
- [x] CHK-FIX-005 [P1] Every finding has the operator's decision recorded [EVIDENCE: Ten decisions in implementation-summary.md]
- [x] CHK-FIX-006 [P1] Every decided repair reran its affected scenarios and graded the round [EVIDENCE: remeasure-operator-repairs/run-1 and remeasure-file-forecast/run-1, both graded]
- [x] CHK-FIX-007 [P1] Evidence pinned to the run's commits and any remeasure round [EVIDENCE: 3023c5e for the main run, 39bcd29 and b591571 for the rounds]
<!-- /ANCHOR:fix-completeness -->

---

<!-- ANCHOR:security -->
## Security

- [x] CHK-030 [P0] No credentials or raw streams committed [EVIDENCE: Secret scan of the 262 committed files found none; jsonl, stderr, transcripts, progress and exports/ copies ignored]
- [x] CHK-031 [P0] Quoted replies carry fixture data only [EVIDENCE: Replies quote Roamstay, Loomlist and Fernhouse fixtures only]
- [x] CHK-032 [P1] Public repo commit carries no attribution line [EVIDENCE: 01200fa message has none]
<!-- /ANCHOR:security -->

---

<!-- ANCHOR:docs -->
## Documentation

- [x] CHK-040 [P1] Spec, plan and tasks synchronized [EVIDENCE: tasks.md evidence matches spec.md and plan.md; repair tasks T024 to T035 added under T017]
- [x] CHK-041 [P1] README says how to rerun and how each count was derived [EVIDENCE: README section 2 count command, section 4 round command, run record command]
- [x] CHK-042 [P2] Parent spec phase map updated [EVIDENCE: Parent spec.md phase map reads Complete for 001 to 005]
- [x] CHK-043 [P0] No `SYNC.md` marks a kernel review done without the operator's confirmation [EVIDENCE: SYNC.md notes say pending; the operator answered Still pending]
<!-- /ANCHOR:docs -->

---

<!-- ANCHOR:file-org -->
## File Organization

- [x] CHK-050 [P1] Grading brief and working lists kept in scratch/ [EVIDENCE: grading-brief*.md, twin-pairs.txt, exports.txt, draft rows and grades/ in scratch/]
- [x] CHK-051 [P1] scratch/ cleaned before completion [EVIDENCE: Nothing temporary left; the briefs, draft rows and grades/ stay as the evidence the criteria cite]
<!-- /ANCHOR:file-org -->

---

<!-- ANCHOR:summary -->
## Verification Summary

| Category | Total | Verified |
|----------|-------|----------|
| P0 Items | 16 | 16/16 |
| P1 Items | 12 | 12/12 |
| P2 Items | 1 | 1/1 |

**Verification Date**: 2026-09-25
<!-- /ANCHOR:summary -->

---
