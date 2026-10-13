---
title: "Goal: realistic Product Owner playbook, rerun on Opus 5.5 medium"
description: "The durable directive this packet executes against and the criteria that decide when it is done."
trigger_phrases:
  - "packet goal"
  - "realistic playbook goal"
  - "076 completion criteria"
  - "goal binding"
importance_tier: "important"
contextType: "planning"
_memory:
  continuity:
    packet_pointer: "013-po-realistic-playbook-opus-rerun"
    last_updated_at: "2026-09-25T18:30:00Z"
    last_updated_by: "claude-opus-5-5"
    recent_action: "Authored the durable directive"
    next_safe_action: "Execute phase 001 against its child goal"
    blockers: []
    key_files: []
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "12f293fe-5421-46a0-b1ea-9fdc15ce0f8e"
      parent_session_id: null
    completion_pct: 0
    open_questions: []
    answered_questions: []
---
# Goal: realistic Product Owner playbook, rerun on Opus 5.5 medium

<!-- SPECKIT_TEMPLATE_SOURCE: goal | v2.2 -->
<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> Everything between the frontmatter and the log is the DURABLE SLICE. A phase
> parent has one limit, 4000 characters, measured from the frontmatter's
> closing fence to the log anchor.

---

<!-- ANCHOR:directive -->
## 1. DURABLE DIRECTIVE

**Objective:** Rewrite the Product Owner manual testing playbook so every scenario produces a real engineering Task, Bug, Story, Epic or Doc for one of three fictional companies, rename the Story export prefix, add the Story with nested Tasks bundle, and after the operator approves the scenario plan rerun both packagings on claude-opus-5-5 medium, then make its writing concise without a rerun.

### Decisions

| ID | Decision |
|----|----------|
| D1 | Story exports use `Story-`, the clarification lane is `{task\|bug\|doc\|Story\|Epic}`, `$prd`/`$p` stay aliases and the H1 ban on `PRD -` stays |
| D2 | A Story with its task breakdown saves as one subfolder holding the Story and its Task exports |
| D3 | Company context documents are files the runner copies into both sandboxes at `context/` |
| D4 | The old Sonnet files in `export/benchmark/` are removed first |
| D5 | Product Owner only, both packagings |
| D6 | No scenario runs before the operator approves the scenario plan |
| D7 | Repairs after grading need the operator's decision, and a kernel review is recorded only once the operator confirms it |
| D8 | Length caps go into the rules without a rerun; exports are hand-edited after grading, verdicts citing the graded originals |
| D9 | No clarification file stays in `export/benchmark/` or a run's `exports/`. Replies and transcripts keep them |
| D10 | A second pass cuts the exports to the operator's depth, keeping every supplied fact; the rules gain a per-artifact word budget |
| D11 | Story and Epic openings are H4, Expected outcomes bold inside Solution, About H2 everywhere; Story requirements stay constraints as `- []` items and every checklist is `[]` |

### Operator copy

The operator holds this directive as the session objective and gets the
`chat_slice` of `goal.cjs packet` again whenever anything above the log changes.
A child goal change to a decision or criterion lands here first.
<!-- /ANCHOR:directive -->

---

<!-- ANCHOR:binding -->
## 2. BINDING

Each child goal rules its phase as if written here.

| Phase | Goal document |
|-------|---------------|
| 001-story-prefix-and-bundle | `001-story-prefix-and-bundle/goal.md` |
| 002-company-context-fixtures | `002-company-context-fixtures/goal.md` |
| 003-playbook-rewrite | `003-playbook-rewrite/goal.md` |
| 004-opus-run | `004-opus-run/goal.md` |
| 005-grading-and-report | `005-grading-and-report/goal.md` |
| 006-concise-writing | `006-concise-writing/goal.md` |

Decisions above outrank child detail. Only the criteria below decide done.
<!-- /ANCHOR:binding -->

---

<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

- [ ] `validate.sh --recursive` on this packet reports 0 errors and every phase's `acceptance-criteria.md` reads `Closeable: Yes`
- [ ] No live Product Owner skill, kernel or knowledge file names a `PRD-` export, and `validate_parity.py product-owner` and the format gate pass on the committed state
- [ ] The playbook validator reports 0 violations for 46 scenarios, each side holding at least 5 tasks, 3 bugs, 3 stories, 3 epics, 3 docs and 1 Story with nested Tasks at Roamstay, Loomlist or Fernhouse
- [ ] The operator approved the scenario plan before any scenario ran
- [ ] The claude-opus-5-5 medium run has a `results.csv` row per scenario, and its README counts match it
- [ ] `export/benchmark/` holds only that run's deliverables, with no clarification
- [ ] Every change is committed in the Barter and Product Owner repos and pushed on the operator's go-ahead
<!-- /ANCHOR:completion -->

---

<!-- ANCHOR:log -->
## 4. LOG

Everything below is VOLATILE. It is not part of the directive, it is not copied
into the objective, and it is expected to grow.

### Progress

| Item | State | Evidence |
|------|-------|----------|
| Scaffold | Done | `create.sh --phase --with-goal`, five children |
| Phase 001 | Pending | |
| D4 clean-up | Done | 25 old Sonnet exports removed with git rm in the Product Owner repo, commit pending |
| Phase docs | In Progress | Four Opus 5.5 writers scoping 001 to 005 in parallel |
| Phase 001 | In Progress | Docs validated 0 errors; Opus implementer running T002 to T030; commits stay with the orchestrator and carry no attribution lines |
| Writer model | Deviation | opus-medium agent type does not load mid-session; writers run as general-purpose on model opus at session effort |
| Phase 002 | In Progress | Manifest 25 files 512 values; three Opus company writers running beside phase 001 (disjoint files, logged as a phase-order deviation) |
| Phase 001 | Done | Product Owner ab846b4, Barter 1bb25170; parity 38/38 and residency pass on commit; 13/13 AC met; not pushed |
| Phase 002 | Done | 25 fixtures, 512 values, 0 misses; Product Owner ff5c80f, Barter 37591a16; 12/12 AC met; not pushed |
| Phase 003 | At approval gate | 46 scenarios, validator 0 violations 0 warnings, selftest 7/7; Product Owner 3023c5e, Barter c15c05e9; not pushed |
| Scenario plan | Approved | Operator, 2026-09-25 19:31 UTC via AskUserQuestion, against Product Owner 3023c5e and Barter c15c05e9; no run output existed |
| Phase 003 | Done | 18/18 AC met, closeable; not pushed |
| Phase 004 | In Progress | Smoke run SID-001 and PID-001 on claude-opus-5-5 medium |
| Phase 004 | In Progress | Smoke SID-001 and PID-001 ok, claude-opus-5-5 alone, 0.57 USD and 36 s per turn; full run of 46 started with --jobs 4 |
| Phase 004 | Done | 46/46 ok first attempt, check_run clean, 98 deliverables collected; Product Owner e9edb95, Barter 7652158c; not pushed |
| Phase 005 | In Progress | Six Opus graders dispatched, one per group (identity and interactive, tasks, bugs, docs, stories, epics) |
| Grader batches | Deviation | Plan named five batches; ran six by splitting backlog into tasks and bugs and story into stories and epics, and joining identity with interactive, to balance the load |
| Grading | Draft done | Six batches: skill 12 PASS 11 FAIL, Project 8 PASS 15 FAIL; check_report: 78 of 86 replies lint-dirty, 4 twins differ |
| Operator rulings | Decided | 2026-09-25: explicit command always asks (repair modes + rerun); Epic References optional without links; a promise to write a file is a file claim (PID-001 FAIL, Project gate flag yes) and kernel line 101 tightened; SDK-001/PDK-001 scenario rewritten to accept a direct draft |
| Repairs | In Progress | Opus implementer editing skill sources, mirrors, kernel v0.16.0 and playbook; remeasure round of 26 scenarios follows the commit |
| Operator rulings 2 | Decided | Labelled hypothesis allowed under no root cause (SBG-003 PASS, wording clarified); No error message is shown advisory, bug template slot fixed; runbook expected results allowed; Approved direction is a Doc Mode class, not invented |
| Repairs | Committed | Product Owner 39bcd29, Barter df2de5f0: skill 0.12.0, kernel v0.16.0, seven mirrors renamed, playbook 2.1.0.0; format gate, validator 46/0/0, selftest 7/7, parity 38/38 and residency pass on the commit; kernel review pending |
| Remeasure round | Running | remeasure-operator-repairs/run-1, 26 scenarios on claude-opus-5-5 medium |
| Remeasure round | Run | 26 of 26 ok, 52 turns, claude-opus-5-5 alone, USD 37.36; every explicit command now asks first; 59 deliverables collected under export/benchmark remeasure folders; three Opus graders dispatched |
| Remeasure round | Graded | skill 7 PASS 4 FAIL, Project 3 PASS 12 FAIL; ask-first fixed on both sides; 8 Project rows still forecast a file, PID-001 among them; 7 rows miss a verbatim value; operator chose one more repair and a Project-only second round |
| Forecast repair | Committed | Product Owner b591571, Barter e9eec279: kernel v0.17.0, skill 0.13.0, Interactive Mode v0.407, playbook 2.1.1.0; parity 38/38, residency pass; second round of 8 Project rows running |
| Second round | Run | remeasure-file-forecast/run-1: 8 of 8 ok, 16 turns, USD 10.38; Turn 1 replies now say the artifact comes next without a path; 177 files in export/benchmark; one Opus grader dispatched |
| Second round | Graded | Project 5 PASS 3 FAIL, PID-001 PASS, no row after a failed gate; PST-003 kept FAIL on the operator's ruling of 2026-09-26 that keeping the draft's filename is a file claim |
| Phase 005 | Done | Report committed as Product Owner 01200fa and Barter 3b55bfbe, pushed on the operator's go-ahead; 13/13 AC met; kernel review still pending on the operator's word |
| Criterion 1 | Met | validate.sh --recursive --strict: Errors 0 in all six folders; grep -L for Closeable: Yes over 0*/acceptance-criteria.md prints nothing (2026-09-26) |
| Criterion 2 | Met | grep for PRD- over sk-product-owner, claude project and AGENTS.md outside changelog and playbook: no match; validate_parity.py 38/38 and run_residency.sh pass on 3b55bfbe; format gate exit 0 across 40 files (2026-09-26) |
| Criterion 3 | Met | Playbook validator: 46 scenarios, 0 violations, 0 warnings; each side 6 tasks plus the handover task, 3 bugs, 4 docs, 4 stories, 3 epics and the SST-004/PST-004 bundle, all at Roamstay, Loomlist or Fernhouse (2026-09-26) |
| Criterion 4 | Met | Scenario plan approved 2026-09-25 19:31 UTC; the first smoke turn ran after it (log above) |
| Criterion 5 | Met | results.csv 46 rows, one per scenario; README count command reprints skill 12/11, Project 8/15, facts_intact 38 of 46, after_failed_gate 22, 4 of 23 twins differing, all equal to the README (2026-09-26) |
| Criterion 6 | Met | export/benchmark holds 177 files, all from this run: 98 main and 79 from its two remeasure rounds, each filed under its round; every file carries a scenario ID of this playbook, no Sonnet file remains (2026-09-26) |
| Criterion 7 | Met | Product Owner ab846b4 to 01200fa pushed a02f3b2..01200fa; Barter 1bb25170 to 3b55bfbe pushed 0545f2a4..3b55bfbe via the barter account; both trees clean and level with origin (2026-09-26) |
| Content-miss repair | In Progress | Operator chose 2026-09-26 to find the cause of the values still dropped or reworded, then rerun; three Opus investigators dispatched read-only on one brief; phase 005 reopened |
| Content-miss repair | Committed | Operator decisions 2026-09-26: Task rule, Behavior rules heading, backticked phrase literal, open question quoted, root grades verbatim only where marked, TK-003 relaxed; Product Owner b50f0a0, Barter 7396d79e; skill 0.14.0, kernel unchanged v0.17.0; parity 38/38, residency pass; rerun of 12 scenarios next |
| Third round | Graded | remeasure-supplied-values/run-1: 12 of 12 ok first attempt, 24 turns, USD 18.90; skill 6 PASS, Project 6 PASS; every repaired value present on both sides; PDK-003 status in other words ruled PASS by the operator 2026-09-26 |
| Content-miss repair | Done | Product Owner b50f0a0 and 3fdce37, Barter 7396d79e and d214c160, pushed on the operator's go-ahead (a02f3b2..3fdce37, 0545f2a4..d214c160); export/benchmark at 200 files; kernel unchanged at v0.17.0, review still pending; phase 005 closed again, 13/13 AC met |
| 006 phase docs | Done | spec, plan, tasks, criteria, goal written; validate PASSED |
| 006 caps home | Decided | operator chose SKILL.md and kernel lines only; shared Conciseness card untouched |
| 006 rules and gate | Done | SKILL.md 276 and kernel 90 carry the caps; length-cap advice in shared core and PO reference; 4 fixture suites PASS; reference parity identical |
| 006 report and collector | Done | README 1-5 and four review sections meet the caps; collector --rounds and edit guard, selftest 7 of 7 with 19 collector checks |
| 006 exports | Done | 98 of 98 verify, 7 About openings kept for facts, 7 fact findings repaired |
| 006 commits | Done | Product Owner fdc8a28, Barter 48ca7a3f; parity 38/38 and residency PASSED on the commit |
| 006 push | Done | Product Owner 3fdce37..fdc8a28, Barter d214c160..48ca7a3f after the operator authorized the mass-deletion gate |
| kernel v0.18.0 review | done | operator confirmed; write_review.py line in Product Owner SYNC.md; validate_parity --reviews PASSED 38/38 |
| 007 scope | Decided | operator chose published files only; evidence and git-ignored run copies stay |
| 007 collector and exports | Done | 20 clarifications git rm'd, 78 remain; collector skips the suffix; selftest old exit 1, new 7 of 7; dry run 20 skips |
| 007 push | Done | Product Owner 1fc3657..e042272, Barter e324ecdf..c6493c1b on the second attempt |
| 008 decisions | Decided | operator chose all 46 local copies, about 30% cut, all 78 files, a word budget in the rules |
| 008 round one | Done | 78 of 78 verify, words 73942 to 62906 (14.9%); operator chose a second round at group 2 depth (25%) and label dashes matching the Doc template |
| 008 cut and budget | Done | 78 of 78 verify, 73942 to 57138 words (22.7%); 81 fact findings, 75 restored; budget on SKILL 276, kernel 90, root 209; skill 0.16.0, kernel v0.19.0 |
| 008 commits | Done | Product Owner bb9210f pushed; Barter 0b08add1, mirror-parity skipped once on the operator's approval |
| 008 push | Done | Product Owner e042272..bb9210f, Barter c6493c1b..0b08add1, no bypass on the push |
| 009 decisions | Decided | operator chose Epic too, all 78 exports converted, [] in every artifact checklist, Story requirements stay constraints; D11 added, slice 3991 |
| 009 forms and gate | Done | templates, rules, kernel v0.20.0, skill 0.17.0; gate reads [] and blocks the retired forms; 75 of 78 exports and 17 examples converted, transform check 0 fails; fixtures, parity, residency, playbook pass |
| 009 commits | Done | Product Owner 0d085cb, Barter b6ac9d86, no bypass; parity 38/38 and residency PASSED on the commit; push waits on the operator |
| 009 push | Done | Product Owner bb9210f..0d085cb, Barter 0b08add1..b6ac9d86, no hook bypass |
| 009 parity check and em dash fix | Done | strict parity 0 format drift, 317 of 317 source edits mirrored; 4 em dashes replaced in interactive-response-templates.md; Product Owner cfa662f, Barter c2542393 pushed, parity 38/38 |
| 009 Quality Scoring mirror | Done | per-item scoring reason restored, Story paragraph identical to source; Product Owner b7e89fe, Barter 8923ad82 pushed, parity 38/38 |

### Deviations and findings

| Item | Note |
|------|------|
| None yet | |
<!-- /ANCHOR:log -->
