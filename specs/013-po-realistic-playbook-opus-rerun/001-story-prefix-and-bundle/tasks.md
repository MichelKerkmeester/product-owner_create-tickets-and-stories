---
title: "Tasks: Phase 1, the Story prefix and the Story bundle"
description: "Task Format: T### [P?] Description (file path)"
trigger_phrases:
  - "story prefix tasks"
  - "story bundle tasks"
  - "prd to story rename tasks"
  - "phase 1 verification checklist"
importance_tier: "normal"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "013-po-realistic-playbook-opus-rerun/001-story-prefix-and-bundle"
    last_updated_at: "2026-09-25T20:40:00Z"
    last_updated_by: "claude-opus-5-5"
    recent_action: "Listed the phase tasks and the verification checklist"
    next_safe_action: "Start T002, the gate baselines"
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
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.2 -->
# Tasks: Phase 1, the Story prefix and the Story bundle

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

- [x] T001 D4: remove the 25 old Sonnet exports with `git rm` in the nested repo, staged there as 25 files and 1087 deleted lines. The Barter repo shows the same 25 as unstaged deletions (`AI Systems/Product Owner/export/benchmark/`)
- [x] T002 Save the gate baselines: format gate, playbook validator, router and format fixtures, parity, residency (`AI Systems/Product Owner/specs/013-po-realistic-playbook-opus-rerun/001-story-prefix-and-bundle/scratch/`) [EVIDENCE: `format-before.txt` identical to `format-gate-before.txt`, 40 files and 79 advisory lines. `playbook-before.txt` 14 scenarios, 0 violations. `router-before.txt` 117/117 and 189/189. `format-fixtures-before.txt` all pass. `residency-before.txt` passes. `parity-before.txt` kept at 38/38. `proof-grep-before.txt` 25 lines in 14 files. `counts-before.txt` totals 42 `$prd`, 31 `$p`, 7 H1 bans]
- [x] T003 Snapshot every line the playbook cites in `SKILL.md`, the kernel and `interactive-mode.md` (`scratch/cited-before.txt`) [EVIDENCE: 24 lines through `scratch/snapshot_cited.sh`, the plan's list plus `interactive-mode.md` line 93 and mirror lines 62 and 70, which the playbook root also cites. Line counts in `linecounts-before.txt`: kernel 253, `SKILL.md` 405]
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T004 [P] D1: lines 79 and 91 (`AI Systems/Product Owner/AGENTS.md`) [EVIDENCE: line 79 reads the `{task|bug|doc|Story|Epic}` lane, line 91 reads `export/006 - Story-saved-searches.md`]
- [x] T005 [P] D1: lines 207 and 208, "New PRD Story" to "New Story" (`AI Systems/Product Owner/sk-product-owner/SKILL.md`) [EVIDENCE: line 207 reads `New Story: export/[###] - Story-[description].md`, line 208 the `Story` lane]
- [x] T006 [P] D1: lines 25 and 375 (`AI Systems/Product Owner/sk-product-owner/references/story-mode.md`) [EVIDENCE: line 25 Output Path and the line 375 fence both read `Story-`]
- [x] T007 [P] D1: line 22 (`AI Systems/Product Owner/sk-product-owner/assets/story-template.md`) [EVIDENCE: line 22 Output Path reads `Story-`]
- [x] T008 [P] D1: lines 25 and 90 (`AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md`) [EVIDENCE: lines 25 and 90 read the `Story` lane]
- [x] T009 [P] D1: line 26 (`AI Systems/Product Owner/sk-product-owner/assets/interactive-response-templates.md`) [EVIDENCE: line 26 Output Path reads the `Story` lane]
- [x] T010 D2: the Routing Compatibility exception after line 197, the bundle naming block and example, the read-back and reply sentence (`AI Systems/Product Owner/AGENTS.md`) [EVIDENCE: exception bullet sits after the independent multi-artifact bullet in Routing Compatibility, spec wording verbatim. A "Story with its tasks" naming block, its paragraph with the read-back and reply sentence, and an `export/010 - Story-order-tracking/` example in Section 2]
- [x] T011 D2: bundle path and reply inside line 207, the task split inside line 252, no line added (`AI Systems/Product Owner/sk-product-owner/SKILL.md`) [EVIDENCE: bundle folder, names, Tasks and Story blocks and the reply inside line 207, the task split inside line 252, file still 405 lines]
- [x] T012 D2: Artifact Rules exception, the bundle subsection with the `#### **Tasks**` snippet, the Response Contract sentence (`AI Systems/Product Owner/sk-product-owner/references/story-mode.md`) [EVIDENCE: Artifact Rules bullet names the exception, a Story With Nested Tasks subsection after the Export Contract holds the folder, names, split, clarification, Tasks snippet and task template rule, and the Response Contract gained the skill and Project bundle reply]
- [x] T013 D2: the `**Story**` block in the Canonical Task template and a Notes For Use bullet (`AI Systems/Product Owner/sk-product-owner/assets/task-templates.md`) [EVIDENCE: `**Story**` block between `**Epic**` and `**Parent task**` holding `- [{Story H1}](<[###] - Story-[description].md>)`, plus a Notes For Use bullet]
- [x] T014 D2: the bundle clarification lane inside line 93 (`AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md`) [EVIDENCE: line 93 carries the Story lane sentence and still ends on reporting the path exactly as an artifact delivery does. Format gate after T010 to T014 shows no finding the baseline lacks]
- [x] T015 Kernel: H1 v0.15.0, lines 226 and 228 edited in place, the bundle sentence inside line 226 (`AI Systems/Product Owner/claude project/Custom Instructions.md`) [EVIDENCE: H1 reads v0.15.0, line 226 reads `New Story` with the bundle sentence on the same line, line 228 the `Story` lane, kernel still 253 lines]
- [x] T016 Mirrors in Project wording: Story Mode line 351 plus the bundle rules, Interactive Mode lines 67 and 70, Task Templates `**Story**` block (`AI Systems/Product Owner/claude project/knowledge/`) [EVIDENCE: Story Mode mirror Export Contract fence reads `Story-`, Artifact Rules exception, bundle subsection and Response Contract in Project wording. Interactive Mode mirror line 67 lane and the bundle sentence inside line 70. Task Templates mirror `**Story**` block and Notes bullet]
- [x] T017 Resync the kernel statement with `resync_statement.py --batch` (Sync Loop `systems.py`) [EVIDENCE: one pair spanning kernel lines 226 to 228 in `scratch/resync-pairs.json`. `resync_statement.py --batch` exit 0, `resynced b385bbbd58 -> d67063c3fa`, 1 statement. The residency gate refuses an uncommitted declaration by design (exit 2), so `scratch/residency_worktree.py` ran its `check_system` on the working copy: 0 findings, and 1 finding against the pre-resync copy as a control]
- [x] T018 Rename the three mirrors with `mv` and `repoint_rename.py`, dry run first, then the version fields and bare stems by hand (`AI Systems/Product Owner/claude project/knowledge/`, `sk-product-owner/references/`, `sk-product-owner/assets/task-templates.md`) [EVIDENCE: three `mv` renames, each `repoint_rename.py` dry run read before the real run. Story Mode 9 whole refs in 4 files, Interactive Mode 14 in 5, Task Templates 5 in 3, 0 split each, outputs in `scratch/repoint-*.txt`. Mirror H1s and each skill file's title, version and H1 bumped by hand. The bare-stem grep finds only two dated 2026-09-16 `SYNC.md` entries, left as history]
- [x] T019 Skill 0.11.0, `description.json` 0.11.0.0, skill README 0.11.0 and a new changelog entry (`AI Systems/Product Owner/sk-product-owner/changelog/v0.11.0.0.md`) [EVIDENCE: `SKILL.md` line 5 and `sk-product-owner/README.md` line 12 read 0.11.0, `description.json` reads 0.11.0.0, `changelog/v0.11.0.0.md` written in the v0.10.0.0 shape with no em dash]
- [x] T020 [P] Project README lines 11, 39 and 124 plus a bundle smoke line (`AI Systems/Product Owner/claude project/README.md`) [EVIDENCE: line 11 kernel v0.15.0, line 39 kernel v0.15.0 and Skill v0.11.0, line 124 the `Story` lane, and a bundle smoke line after it]
- [x] T021 [P] System README lines 300 to 307, 477, 492, 570 to 572, 644, 725 to 737 and 763 (`AI Systems/Product Owner/README.md`) [EVIDENCE: lead-in reads "Example names, one per lane" and the example says `Story-`. Lines 477 and 492 point at the tracked `SST-001` turn-2 reply instead of the removed file. File Naming takes `Story-`, the two bundle lines and the `Story` lane, with one sentence on the folder. Line 644 and the tree line read kernel v0.15.0 and skill v0.11.0. The old benchmark list became one paragraph saying the folder is empty until the next run is collected. Also changed, beyond the named lines: line 181 named `export/benchmark/skill/` and the tree line for `benchmark/` claimed 60 GLM files]
- [x] T022 [P] Playbook root line 140 and version 1.0.0.4, both scenario line 31 paths (`AI Systems/Product Owner/sk-product-owner/manual-testing-playbook/`) [EVIDENCE: root version 1.0.0.4, line 140 grades `Story` in place of `PRD`, both scenario line 31s read `Story-payout-pause` twice, prompts untouched. Playbook validator: 14 scenarios, 0 violations, 0 warnings]
- [x] T023 Line 18 version claims and a dated note saying the kernel review is pending (`AI Systems/Product Owner/SYNC.md`) [EVIDENCE: line 18 reads kernel v0.15.0 and skill 0.11.0. A dated 2026-09-25 note names the change and says the kernel review by the operator is pending. `git diff --stat SYNC.md` reads 2 insertions, 1 deletion, so no dated entry changed]
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T024 Run the proof grep from plan step 12 and confirm it prints nothing [EVIDENCE: `scratch/proof-grep-after.txt` holds 0 lines, against 25 lines in 14 files in `proof-grep-before.txt`]
- [x] T025 Count `$prd`, `$p` and "No `PRD -` prefix" in the skill, kernel and mirrors and match the counts from T002 [EVIDENCE: `scratch/counts-after.txt` is identical to `counts-before.txt` file by file: 42 `$prd`, 31 `$p`, 7 H1 bans]
- [x] T026 Diff the cited lines against `scratch/cited-before.txt` [EVIDENCE: 18 of 24 cited lines identical. `SKILL.md` 208 and kernel 228 differ by the lane word only. `SKILL.md` 207 and kernel 226 keep their text after the word swap and add the bundle sentence. `interactive-mode.md` 93 and mirror 70 keep every old sentence in order with one inserted. Kernel 253 lines and `SKILL.md` 405 lines, as before]
- [x] T027 Write a sample Story and two tasks and lint each with the format gate in artifact mode (`scratch/sample-bundle/`) [EVIDENCE: `scratch/sample-bundle/010 - Story-order-tracking/` holds the Story and tasks `010.1` and `010.2`, linked both ways. `validate-output-format.cjs --system product-owner <file>` passes each in artifact mode, exit 0. The plan's command without `--system` exits 64 on usage. A control copy with an em dash and a divider after a Mark-as-done line fails with 2 errors]
- [x] T028 Probe `route_request` with `$story Order tracking. Break it into tasks.` and expect `STORY` intent and shape (`AI Systems/Product Owner/benchmark/router/route_contract.py`) [EVIDENCE: `route_request('$story Order tracking. Break it into tasks.')` returns intent `STORY`, shape `STORY`, source `command`, no disambiguation. The `$story $task` control returns intent `INTERACTIVE`, source `conflict`. Output in `scratch/route-probe.txt`]
- [x] T029 Run the format gate against its baseline, both fixture runners, the playbook validator and residency on the working tree [EVIDENCE: format gate passes across 40 files with 79 advisory lines, and its line-number-free diff against `format-before.txt` is empty. Router 117/117 and 189/189, format fixtures all pass, playbook 14 scenarios and 0 violations. The residency gate exits 2 on the working tree because it reads only a committed declaration, and parity refuses the same way. `scratch/residency_worktree.py` runs residency's own `check_system` on the working copy: 0 findings, against 8 for the pre-resync declaration as a control. Residency and parity themselves run on the commit]
- [x] T030 Check that every `export/benchmark/` path the system README names exists (`AI Systems/Product Owner/README.md`) [EVIDENCE: the README names no path under `export/benchmark/`, 0 named and 0 missing. Its three remaining mentions name the folder itself, which it now describes as empty]
- [x] T031 Stage named paths only and commit in the nested repo with no attribution line, then in the Barter repo [EVIDENCE: Product Owner ab846b4 and Barter 1bb25170, named paths only, no attribution line]
- [x] T032 Run parity and residency on the commit, then `validate.sh --strict` on this folder, then mark the acceptance rows [EVIDENCE: parity PASSED 38/38 and residency PASSED on 1bb25170, acceptance rows marked Met]
- [ ] T033 Push only after the operator's go-ahead
<!-- /ANCHOR:phase-3 -->

---

<!-- ANCHOR:completion -->
## Completion Criteria

- [ ] All tasks marked `[x]`
- [ ] No `[B]` blocked tasks remaining
- [ ] Gates green on the committed state in both repositories
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

- [x] CHK-001 [P0] D1, D2 and D4 frozen in the parent goal, and the bundle design settled in spec section 3
- [x] CHK-002 [P0] Gate baselines and the cited-line snapshot saved to `scratch/` [EVIDENCE: T002 and T003]
- [x] CHK-003 [P1] Every live `PRD` site listed with its line number
<!-- /ANCHOR:pre-impl -->

---

<!-- ANCHOR:code-quality -->
## Code Quality

- [x] CHK-010 [P0] Source first, mirrors by hand per `SYNC.md` [EVIDENCE: skill sources edited in T004 to T014 before the kernel and mirrors in T015 and T016, which were written by hand in Project wording]
- [x] CHK-011 [P0] No declared statement edited except through `resync_statement.py` or `repoint_rename.py` [EVIDENCE: the `systems.py` diff holds only the one statement `resync_statement.py` rewrote and the names `repoint_rename.py` changed]
- [x] CHK-012 [P0] Kernel and `SKILL.md` edits add no line, so no cited line moves [EVIDENCE: kernel 253 lines and `SKILL.md` 405 lines, as in `linecounts-before.txt`]
- [x] CHK-013 [P1] No em dash in any added or changed line [EVIDENCE: `scratch/emdash-check.txt`: 196 added or changed lines in 24 files, 0 em dash, 0 prose semicolon]
<!-- /ANCHOR:code-quality -->

---

<!-- ANCHOR:testing -->
## Testing Checklist

- [x] CHK-020 [P0] Proof grep prints nothing [EVIDENCE: T024]
- [x] CHK-021 [P0] Format gate adds no finding its baseline lacks [EVIDENCE: T029, empty diff against `format-before.txt`]
- [ ] CHK-022 [P0] Parity passes on the committed state and residency passes
- [x] CHK-023 [P0] Router fixtures, format fixtures and the playbook validator pass [EVIDENCE: T029]
- [x] CHK-024 [P1] Sample bundle passes the format gate in artifact mode [EVIDENCE: T027]
- [x] CHK-025 [P1] `route_request` sends the bundle phrasing to Story Mode [EVIDENCE: T028]
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:fix-completeness -->
## Fix Completeness

- [x] CHK-FIX-001 [P0] `$prd`, `$p` and the H1 ban on a `PRD -` prefix still present wherever they were [EVIDENCE: T025, counts identical file by file]
- [x] CHK-FIX-002 [P0] No live reference to the three old mirror names, bare stems included [EVIDENCE: T018 bare-stem grep finds only two dated `SYNC.md` entries, and a wider version grep finds no live Product Owner reference]
- [x] CHK-FIX-003 [P0] Every stated skill and kernel version agrees [EVIDENCE: `SKILL.md`, skill README 0.11.0, `description.json` 0.11.0.0, kernel H1, Project README lines 11 and 39, system README kernel lines and `SYNC.md` line 18 all read kernel v0.15.0 and skill 0.11.0. Parity's own version check runs on the commit]
- [x] CHK-FIX-004 [P1] Changelog files and dated records unchanged, checked with `git diff --stat` [EVIDENCE: `git diff --stat` on `sk-product-owner/changelog/` is empty, the new entry is untracked, and 0 dated `SYNC.md` lines changed]
<!-- /ANCHOR:fix-completeness -->

---

<!-- ANCHOR:security -->
## Security

- [ ] CHK-030 [P0] No credentials or raw event streams committed
- [ ] CHK-031 [P1] Public repo commit carries no attribution line
<!-- /ANCHOR:security -->

---

<!-- ANCHOR:docs -->
## Documentation

- [x] CHK-040 [P0] The `SYNC.md` note says the kernel review is pending [EVIDENCE: T023]
- [x] CHK-041 [P1] Changelog entry `v0.11.0.0.md` written [EVIDENCE: T019]
- [x] CHK-042 [P1] Both READMEs name no removed file and state the new versions [EVIDENCE: T020, T021 and T030]
<!-- /ANCHOR:docs -->

---

<!-- ANCHOR:file-org -->
## File Organization

- [x] CHK-050 [P1] Baselines, snapshots and the sample bundle kept in `scratch/` only [EVIDENCE: every baseline, snapshot, control and the sample bundle sit in `scratch/`, and `specs/` is gitignored]
- [ ] CHK-051 [P1] `scratch/` cleaned before completion
<!-- /ANCHOR:file-org -->

---

<!-- ANCHOR:summary -->
## Verification Summary

| Category | Total | Verified |
|----------|-------|----------|
| P0 Items | 14 | 12/14 |
| P1 Items | 10 | 8/10 |
| P2 Items | 0 | 0/0 |

**Verification Date**: 2026-09-25
<!-- /ANCHOR:summary -->

---
