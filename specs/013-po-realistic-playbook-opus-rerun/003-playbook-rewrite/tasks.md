---
title: "Tasks: Phase 3, the playbook rewrite and the approval gate"
description: "Task Format: T### [P?] Description (file path)"
trigger_phrases:
  - "playbook rewrite tasks"
  - "scenario writer groups"
  - "run tooling selftest tasks"
  - "approval gate task"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.2 -->
# Tasks: Phase 3, the playbook rewrite and the approval gate

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

- [x] T001 Confirm phases 001 and 002 are committed: `Story-` naming, the bundle rule and the renamed knowledge files in place, and every fixture the phase 002 manifest names on disk. Stop here if either is missing (`AI Systems/Product Owner/specs/013-po-realistic-playbook-opus-rerun/001-story-prefix-and-bundle/`, `AI Systems/Product Owner/specs/013-po-realistic-playbook-opus-rerun/002-company-context-fixtures/spec.md`) [EVIDENCE: Product Owner ab846b4 and ff5c80f, Barter 1bb25170 and 37591a16 committed; 25 fixtures on disk]
- [x] T002 Read every `file:line` the root cites on the post-001 commit, the four identity greps included, and list old line, new line and the rule text (`scratch/root-citations.md`) [EVIDENCE: scratch/root-citations.md lists 15 old citations, none moved line since phase 001 edited inside existing lines. Identity grep 1 moved from 1 to 2, AGENTS.md lines 47 and 91. The other three stay 0, 0 and 4]
- [x] T003 Write the `### Ticket realism` subsection into root section 5 exactly as `spec.md` section 3 settles it, and read the six existing advisory readings back unchanged (`AI Systems/Product Owner/sk-product-owner/manual-testing-playbook/manual-testing-playbook.md`) [EVIDENCE: root section 5 holds ### Ticket realism with 5 Blocking and 4 Advisory rows after Defect severity. The Defect severity lists are untouched and the six readings grep at count 1 in both HEAD and the working root. One wording change: the PRD- token in row 1 reads as the old `PRD` export word, so the package PRD- grep stays empty]
- [x] T004 Write the writer brief: the authoring rules from `plan.md`, the file manifest, each ID's attachment list from the phase 002 manifest and the phase 001 export names (`scratch/scenario-brief.md`) [EVIDENCE: the brief embedded in each group writer's dispatch prompt, pointing at the authoring rules, the manifest, the 002 attachments table and the 001 export names]
- [x] T005 Delete the 12 retired scenario files, six slugs on each side (`AI Systems/Product Owner/sk-product-owner/manual-testing-playbook/{skill,project}-*/`) [EVIDENCE: 12 files removed with rm, six slugs per side. Each backup in scratch/old-scenarios matched HEAD by cmp first. Both identity-handover.md files kept]
- [x] T006 Create the report folder and copy `.gitignore` and the three `run/` scripts from the Sonnet folder unchanged (`AI Systems/Product Owner/benchmark/reports/2026-09-25--manual-testing-playbook--claude-opus-5-5-medium/`) [EVIDENCE: `cmp` identical for `.gitignore` and all three scripts before any edit. `.gitignore` still identical. Sonnet folder: `git diff --stat` and `git status --porcelain` empty in both repos]
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T007 [P] Identity group: `SID-001` and `PID-001`, the four greps re-read on the post-001 tree and both `- Playbook ID:` lines kept (`skill-identity/identity-handover.md`, `project-identity/identity-handover.md`) [EVIDENCE: SID-001 and PID-001 rewritten, greps read 2, 0, 0 and 4, both Playbook ID lines kept]
- [x] T008 [P] Backlog group, tasks: `STK-001` to `STK-006` and `PTK-001` to `PTK-006` (`skill-backlog-modes/`, `project-backlog-modes/`) [EVIDENCE: 12 files, twins match on turns and attachments]
- [x] T009 [P] Backlog group, bugs: `SBG-001` to `SBG-003` and `PBG-001` to `PBG-003` (`skill-backlog-modes/`, `project-backlog-modes/`) [EVIDENCE: 6 files, twins match]
- [x] T010 [P] Document group: `SDK-001` to `SDK-004` and `PDK-001` to `PDK-004` (`skill-document-modes/`, `project-document-modes/`) [EVIDENCE: 8 files, twins match]
- [x] T011 [P] Story group: `SST-001` to `SST-004`, `SEP-001` to `SEP-003` and their `PST` and `PEP` twins, the bundle pair per the `SST-004` expected behavior in `spec.md` section 3 (`skill-story-modes/`, `project-story-modes/`) [EVIDENCE: 14 files, twins match, bundle and refinement paths match the selftest patterns]
- [x] T012 [P] Interactive group: `SIR-001`, `SIR-002`, `PIR-001` and `PIR-002` (`skill-interactive-routing/`, `project-interactive-routing/`) [EVIDENCE: 4 files, twins match, Turn 1s route as intended]
- [x] T013 Root policy: intro count, coverage map, natural Turn 1 list, preconditions and ledger, the "Company context and attachments" section, Clarification turns and Export names with `Story-` and the bundle path, the Identity handover rule, re-anchored citations and the wave table for waves 1 to 6 (`manual-testing-playbook.md`) [EVIDENCE: intro 46, coverage map for 10 folders, natural Turn 1 list of 5 per side, preconditions 1 to 9 and ledger, new ### Company context and attachments in section 2 with 4 resolving links, Clarification turns lane, Export names with Epic, the bundle and the refinement name, Identity handover rule for the two-turn $task chain, wave table 1 to 6. load_waves returns the manifest wave for all 46 IDs. Summaries 7 to 16 and index 18 are placeholders until T014]
- [x] T014 Root summaries: one block per ID with its Prompt copied by script from the file's contract Prompt line, the section 18 index for 46 IDs, the section 17 overlap IDs and version `2.0.0.0` (`manual-testing-playbook.md`) [EVIDENCE: 46 summary blocks in sections 7 to 16, each Prompt copied by script from its file's contract Prompt line. Section 18 indexes all 46 files, section 17 names the router overlap IDs and all 46 for manual runs, version 2.0.0.0. Six writer amendments applied to the root. Validator: PASS scenarios=46 categories=10 operator=46 violations=0 warnings=0, exit=0. load_waves right for all 46, 60 root links resolve, package PRD- and em dash greps empty]
- [x] T015 [P] Runner: parse `- Attachments:`, exit 2 on a missing file or a basename collision, stage each file into `context/` before the baseline, record basename, source and sha256 (`run/playbook_runner.py`) [EVIDENCE: selftest parse-synthetic PASS with dead link, collision and link-less bullet each exiting 2 before the run folder exists, and staging-order PASS with an in-place edit logged as modified. Dry run on the current 14-scenario playbook exits 0]
- [x] T016 Runner: `prove_isolation` accepts `context/` only when it holds exactly the declared files, byte for byte (`run/playbook_runner.py`) [EVIDENCE: selftest isolation PASS, 8 planted faults caught (extra, missing, one-byte change, subfolder on each side), clean sandboxes unflagged, no-attachment builds byte-identical to the Sonnet runner]
- [x] T017 [P] Collector: bundle subfolders on both sides, the `[NNN]` rule applied to folder names, `context/` skipped with a warning line when an attachment changed (`run/collect_exports.py`) [EVIDENCE: selftest collector PASS, the Sonnet collector flattens the same input, the dry run writes nothing, and the unnumbered refinement `fernhouse-save-card-draft.md` is collected on both sides]
- [x] T018 [P] check_run: default model `claude-opus-5-5`, and a finding for any engine, model or effort in `manifest.json` other than `claude`, the expected model and `medium` (`run/check_run.py`) [EVIDENCE: selftest check-run PASS, 4 planted faults caught, and the Sonnet check_run rejects the clean run and passes effort high]
- [x] T019 Selftest: the parse, isolation, collector and check_run tests in `plan.md` section 5, each with its planted fault, exit 0 or 1 (`run/selftest.py`) [EVIDENCE: 6 of 7 tests PASS in 1.2s. parse-real FAILs as designed until the 46 scenarios and their fixtures land, which T021 reruns. Mutation run: 18 of 18 mutants killed]
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T020 Run the playbook validator and read `scenarios=46 categories=10 operator=46 ... violations=0 warnings=0` and `exit=0` [EVIDENCE: scenarios=46 categories=10 operator=46 violations=0 warnings=0, exit=0]
- [x] T021 Run `run/selftest.py` and read exit 0 with every planted fault reported as caught [EVIDENCE: selftest 7 of 7 passed, parse-real 463 checks]
- [x] T022 Run the runner's `--dry-run` into `scratch/dry-run`, count 46 rows each with its attachments, then delete `scratch/dry-run` [EVIDENCE: dry run 46 rows, 86 turns, 46 with attachments, 23 per side, waves 2/12/6/8/14/4; scratch/dry-run deleted]
- [x] T023 Run the greps and the Sonnet diff in `plan.md` section 4, plus a search for the four forbidden verdict words and for `/Users/` in the new `run/` scripts, and read no output [EVIDENCE: Sonnet diff empty, no PRD-, em dash, verdict word, semicolon in scenarios or /Users/ path]
- [x] T024 Read each twin pair side by side and confirm they differ only in the runtime lines: profile, precondition, expected delivery shape, source files and metadata [EVIDENCE: diffs differ only in ID, profile, precondition, delivery shape, pass wording and evidence; parse-real proves identical turns and attachments for all 23 pairs]
- [x] T025 Write or refresh this phase's entry in the packet changelog (`AI Systems/Product Owner/specs/013-po-realistic-playbook-opus-rerun/changelog/`) [EVIDENCE: not applicable here, the nested-changelog tool resolves its project root to the linked Public repo and refuses packets in this repo; 075 has none for the same reason]
- [x] T026 Commit in the Barter repo and in the Product Owner public repo, the public one with no attribution line. Note both SHAs. No push [EVIDENCE: Product Owner 3023c5e, Barter c15c05e9, no attribution line, no push]
- [x] T027 Approval gate: print the scenario plan as a terminal table, publish a private artifact page with the catalog, the companies, the attachments and the rubric, ask through AskUserQuestion, confirm the new report folder holds no run output and record the answer with its date and both SHAs in `goal.md` and `implementation-summary.md`. Nothing in phase 004 starts before this is recorded [EVIDENCE: terminal table printed, private page https://claude.ai/artifact/YE9rqVDigYxfRXTs8u3NR8 published, the operator answered "Approve and run" through AskUserQuestion on 2026-09-25 against Product Owner 3023c5e and Barter c15c05e9, the report folder held only .gitignore and the four run scripts at that moment]
<!-- /ANCHOR:phase-3 -->

---

<!-- ANCHOR:completion -->
## Completion Criteria

- [x] All tasks marked `[x]`
- [x] No `[B]` blocked tasks remaining
- [x] The operator's approval recorded against named commits
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

- [x] CHK-001 [P0] Phases 001 and 002 committed, their deliverables on disk [EVIDENCE: Product Owner ab846b4 and ff5c80f, Barter 1bb25170 and 37591a16, 25 fixtures on disk (T001)]
- [x] CHK-002 [P0] The rubric's Blocking and Advisory lists sit in root section 5 before any scenario file is written [EVIDENCE: T003 wrote the subsection before the group writers ran T007 to T012]
- [x] CHK-003 [P1] The writer brief names every file, attachment and export word before the writers start [EVIDENCE: The brief sat in each group writer's dispatch prompt rather than in a scratch file (T004)]
<!-- /ANCHOR:pre-impl -->

---

<!-- ANCHOR:code-quality -->
## Code Quality

- [x] CHK-010 [P0] No turn input holds a backtick, a pipe, an ISO date or a line break [EVIDENCE: All 86 turn inputs in the dry run checked, 0 with a backtick, pipe, ISO date or line break]
- [x] CHK-011 [P0] No Pass clause and no 9-column Pass/fail cell names the size band or commentary, or expects a discipline code in a Story or Epic H1 [EVIDENCE: A search of every Pass line and 9-column table row for size band, commentary and discipline code prints nothing]
- [x] CHK-012 [P0] The Sonnet report folder shows no diff [EVIDENCE: `git diff --stat` on the Sonnet folder empty in both repositories]
- [x] CHK-013 [P1] No em dash in any changed file [EVIDENCE: The em dash search over the package and the new report folder prints nothing]
<!-- /ANCHOR:code-quality -->

---

<!-- ANCHOR:testing -->
## Testing Checklist

- [x] CHK-020 [P0] Validator: `scenarios=46 categories=10 operator=46`, `violations=0 warnings=0`, `exit=0` [EVIDENCE: `PASS ... scenarios=46 categories=10 operator=46 routing_gold_excluded=0 violations=0 warnings=0`, `exit=0`]
- [x] CHK-021 [P0] `run/selftest.py` exits 0 and reports each planted fault as caught [EVIDENCE: `selftest: 7 of 7 tests passed`, every planted fault reported as caught]
- [x] CHK-022 [P0] The dry run lists 46 rows, each with its attachments and the manifest's wave [EVIDENCE: 46 rows, 86 turns, 46 with attachments, 23 per side, waves 2/12/6/8/14/4, dry run folder deleted]
- [x] CHK-023 [P1] Every root link to `benchmark/fixtures/companies/` resolves [EVIDENCE: selftest root-links PASS and no validator PATH_MISSING]
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:fix-completeness -->
## Fix Completeness

- [x] CHK-FIX-001 [P0] Every `file:line` citation in the root and the scenarios read back at its line on the post-001 commit [EVIDENCE: `scratch/root-citations.md`, 15 citations read back (T002)]
- [x] CHK-FIX-002 [P0] The six existing advisory readings in root section 5 read the same after the rubric lands [EVIDENCE: The six readings grep at count 1 in HEAD and the working root (T003)]
- [x] CHK-FIX-003 [P1] The four identity greps rerun on the post-001 tree, with the counts the handover files state [EVIDENCE: The greps read 2, 0, 0 and 4, both Playbook ID lines kept (T007)]
<!-- /ANCHOR:fix-completeness -->

---

<!-- ANCHOR:security -->
## Security

- [x] CHK-030 [P0] No real person, real brand, credential or developer-absolute path in any scenario or script [EVIDENCE: The brand, credential and `/Users/` search over the scenarios and `run/` prints nothing]
- [x] CHK-031 [P0] No scenario turn runs before the recorded approval [EVIDENCE: The report folder held no manifest.json, run-status.json or run-log.jsonl at approval]
<!-- /ANCHOR:security -->

---

<!-- ANCHOR:docs -->
## Documentation

- [x] CHK-040 [P1] The root coverage map, wave table and index agree with the 46 files [EVIDENCE: The validator reports no INDEX_ORPHAN_FILE and load_waves returns the manifest wave for all 46 IDs]
- [x] CHK-041 [P1] `goal.md` and `implementation-summary.md` record the approval with its date and both SHAs [EVIDENCE: Both files carry the approval row with 2026-09-25, 3023c5e and c15c05e9]
<!-- /ANCHOR:docs -->

---

<!-- ANCHOR:file-org -->
## File Organization

- [x] CHK-050 [P1] Temp files in scratch/ only [EVIDENCE: Only `scratch/root-citations.md` remains, the dry run removed]
- [x] CHK-051 [P1] scratch/ cleaned before completion [EVIDENCE: `scratch/old-scenarios/` removed, the retired files stay in git history at Product Owner ff5c80f]
<!-- /ANCHOR:file-org -->

---

<!-- ANCHOR:summary -->
## Verification Summary

| Category | Total | Verified |
|----------|-------|----------|
| P0 Items | 12 | 12/12 |
| P1 Items | 8 | 8/8 |
| P2 Items | 0 | 0/0 |

**Verification Date**: 2026-09-25
<!-- /ANCHOR:summary -->

---
