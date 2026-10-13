---
title: "Implementation Plan: Phase 1, the Story prefix and the Story bundle"
description: "The skill sources take the Story- word and the bundle rule first, the kernel and three knowledge mirrors follow by hand per SYNC.md, and the Sync Loop declaration changes only through its own tools. Kernel and SKILL.md edits stay on their existing lines so no line the playbook cites moves, and the parity gate runs on the committed state."
trigger_phrases:
  - "story prefix plan"
  - "story bundle plan"
  - "resync statement batch"
  - "cited lines snapshot"
importance_tier: "normal"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "013-po-realistic-playbook-opus-rerun/001-story-prefix-and-bundle"
    last_updated_at: "2026-09-25T20:40:00Z"
    last_updated_by: "claude-opus-5-5"
    recent_action: "Planned the source-first edit order and the gates"
    next_safe_action: "Run the setup steps and save their output to scratch"
    blockers: []
    key_files:
      - "AI Systems/Product Owner/claude project/Custom Instructions.md"
      - "AI Systems/Product Owner/SYNC.md"
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "12f293fe-5421-46a0-b1ea-9fdc15ce0f8e"
      parent_session_id: null
    completion_pct: 0
    open_questions: []
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: plan-core | v2.2 -->
# Implementation Plan: Phase 1, the Story prefix and the Story bundle

<!-- SPECKIT_LEVEL: 2 -->

---

<!-- ANCHOR:summary -->
## 1. SUMMARY

### Technical Context

| Aspect | Value |
|--------|-------|
| **Language/Stack** | Markdown rule files, a Python declaration, Python and JavaScript gates |
| **Framework** | The `sk-product-owner` skill, the Claude Project kernel and knowledge, the Sync Loop parity and residency tools |
| **Storage** | The Barter repo plus the Product Owner public repo at `AI Systems/Product Owner/.git` |
| **Testing** | Format gate, router and format fixtures, playbook validator, parity gate, residency, a proof grep, a sample bundle |

### Overview
The skill sources change first: the `Story-` word at every naming site, then the bundle rule in `AGENTS.md`, `SKILL.md`, `story-mode.md`, `task-templates.md` and `interactive-mode.md`. The kernel and the Story Mode, Interactive Mode and Task Templates mirrors follow by hand, per the manual parity method in `SYNC.md`, and the declared kernel statement changes only through `resync_statement.py`. Kernel and `SKILL.md` edits stay on their existing lines, so no line the playbook cites moves. The gates run before and after, and the parity gate runs after the commit because it reads committed files only.
<!-- /ANCHOR:summary -->

---

<!-- ANCHOR:quality-gates -->
## 2. QUALITY GATES

### Definition of Ready
- [x] Operator decisions D1, D2 and D4 frozen in the parent `goal.md`
- [x] D4 clean-up staged in the nested repo
- [x] Every live `PRD` site listed with its line number
- [ ] Gate baselines saved to `scratch/`

### Definition of Done
- [ ] Every row in `acceptance-criteria.md` reads `Met`
- [ ] Gates green on the committed state in both repositories
- [ ] The kernel review recorded as pending, never as done
<!-- /ANCHOR:quality-gates -->

---

<!-- ANCHOR:architecture -->
## 3. ARCHITECTURE

### Pattern
Source first, mirrors by hand, declaration through its tools, version bookkeeping, commit, then the gates that read the committed tree.

### Key Components
- **Skill sources**: `AGENTS.md`, `SKILL.md`, `story-mode.md`, `story-template.md`, `task-templates.md`, `interactive-mode.md`, `interactive-response-templates.md`
- **Kernel**: `claude project/Custom Instructions.md`, lines 226 and 228 and the H1
- **Knowledge mirrors**: Templates - Story Mode, System - Interactive Mode, Assets - Task Templates
- **Declaration**: the Sync Loop `systems.py`, whose kernel statement quotes the naming lines verbatim
- **Documents**: both READMEs, `SYNC.md`, the changelog and three playbook sites

### Data Flow
Decision, then skill source, then Project mirror in Project wording, then declaration resync and renames, then versions and changelog, then commit in both repositories, then parity and residency on the commit.
<!-- /ANCHOR:architecture -->

---

<!-- ANCHOR:affected-surfaces -->
## FIX ADDENDUM: AFFECTED SURFACES

| Surface | Current Role | Action | Verification |
|---------|--------------|--------|--------------|
| Skill naming sites | State the export names | Update | Proof grep |
| Skill routing and Story Mode | Own the multi-artifact rule and the Story shape | Update with the bundle | Read against spec section 3, sample bundle through the format gate |
| Kernel and three mirrors | Project copies of the rules | Update by hand | Parity gate on the commit |
| Sync Loop declaration | Quotes the kernel naming lines | Resync and repoint | Residency |
| Router contract and `route_contract.py` | Route `$story` requests | Unchanged | Router fixtures, `route_request` probe |
| Playbook root and story scenarios | Grade the export word | Minimal update | Playbook validator |
| READMEs, `SYNC.md`, `description.json` | State versions and names | Update | Parity version check, existence check |

Required inventories:
- Every live `PRD-` and `|PRD|` site: the proof grep in step 12, 25 lines in 14 files at the start
- Every line the playbook cites by number, snapshotted in step 2
- Every stated skill and kernel version: `SKILL.md` line 5, `sk-product-owner/README.md` line 12, `description.json`, the kernel H1, `claude project/README.md` lines 11 and 39, the system README lines 644 and 763, `SYNC.md` line 18
<!-- /ANCHOR:affected-surfaces -->

---

<!-- ANCHOR:phases -->
## 4. IMPLEMENTATION PHASES

Follow the ordered tasks in `tasks.md`. It owns the Setup, Implementation and Verification phase checkboxes and task state.

Run every command from the repository root. `SL` names the Sync Loop folder, whose name holds a dash this document may not print: `SL=$(ls -d "AI Systems"/z*Sync\ Loop)`. `S` is this phase's `scratch/` folder.

1. **Baselines.** `node "$SL/validate-output-format.cjs" --system product-owner > "$S/format-before.txt"`, then the playbook validator, both fixture runners, `python3 "$SL/validate_parity.py" product-owner` and `bash "$SL/run_residency.sh" product-owner`. On 2026-09-25 they read: format passes across 40 files with 79 advisory lines, playbook 14 scenarios and 0 violations, router 117/117 fixtures and 189/189 differential inputs, format fixtures pass, parity 38/38, residency passes
2. **Cited lines.** Save `SKILL.md` lines 207, 208, 217 and 283, kernel lines 58, 76, 79, 85, 89, 104, 130, 217, 223 to 228 and 233, and `interactive-mode.md` lines 85 and 124 to `$S/cited-before.txt` with `sed -n`
3. **D1, skill sources.** `AGENTS.md` lines 79 and 91. `SKILL.md` lines 207 and 208, with "New PRD Story" becoming "New Story". `story-mode.md` lines 25 and 375. `story-template.md` line 22. `interactive-mode.md` lines 25 and 90. `interactive-response-templates.md` line 26
4. **D2, skill sources.** `AGENTS.md`: the exception bullet from spec section 3 after line 197, a "Story with its tasks" naming block with an example, and one sentence on reading back every file and the reply shape. `SKILL.md`: the bundle path and reply inside the line 207 bullet, and the task split inside the line 252 Story consolidation, both without adding a line. `story-mode.md`: the Artifact Rules bullet gains "except the Story with nested Tasks bundle", a new subsection after the Export Contract holds the whole bundle rule with the `#### **Tasks**` snippet, and the Response Contract gains the bundle reply. `task-templates.md`: a `**Story**` block between `**Epic**` and `**Parent task**` in the Canonical Task template, and a Notes For Use bullet. `interactive-mode.md`: the bundle clarification lane inside line 93
5. **Project side, by hand.** Kernel H1 to v0.15.0. Line 226 becomes the New Story line with the bundle sentence on the same line, including one Deliverable Block per file, each `Export-equivalent path:` inside the folder, one `HVR self-scan:` line and Task Templates for the task files. Line 228 takes the `Story` lane. The Story Mode mirror line 351 and its Artifact Rules, bundle subsection and Response Contract in Project wording. The Interactive Mode mirror lines 67 and 70. The Task Templates mirror `**Story**` block and note
6. **Declaration.** Write the old and new kernel lines 226 and 228 as pairs to `$S/resync-pairs.json`, then `python3 "$SL/resync_statement.py" "$SL/systems.py" --batch "$S/resync-pairs.json"`. Exit 65 means the rewrite was rolled back: stop and read it
7. **Renames.** For each mirror, `mv` the file to its new version, then `python3 "$SL/repoint_rename.py" "<old>.md" "<new>.md" --dry-run`, read the list, run it without `--dry-run`, then bump the mirror H1 and the skill file's `title` and `version` fields by hand. Story Mode v0.401 to v0.402, Interactive Mode v0.404 to v0.405, Task Templates v0.101 to v0.102. Then `grep -rnF --exclude-dir=.git --exclude-dir=reports --exclude-dir=episodes -e 'Story Mode - v0.401' -e 'Interactive Mode - v0.404' -e 'Task Templates - v0.101' "AI Systems"` for bare stems, and repoint any live one by hand
8. **Bookkeeping.** `SKILL.md` 0.11.0, `sk-product-owner/README.md` 0.11.0, `description.json` 0.11.0.0, `changelog/v0.11.0.0.md` in the shape of `v0.10.0.0.md`. `SYNC.md` line 18 to kernel v0.15.0 and Skill 0.11.0, and one dated 2026-09-25 note that names the change and says the kernel review by the operator is pending
9. **Documents.** `claude project/README.md` lines 11, 39 and 124, plus one bundle smoke line. The system README: the lead-in at line 300 stops calling the names real names from a run and line 306 says `Story-`, lines 477 and 492 name no removed file, lines 570 to 572 take `Story-` and the bundle folder, lines 644 and 763 take the new versions, and lines 725 to 737 say `export/benchmark/` is empty until phase 004 collects the Opus run
10. **Playbook.** Root line 140 lists `Story` in place of `PRD`, root version 1.0.0.4, and both `story-shape-hard-values.md` line 31 paths say `Story-payout-pause`. Prompts stay as they are, so the twins stay in sync. Phase 003 replaces these files, and this edit keeps them truthful until then
11. **Sample bundle.** Write one Story and two tasks in the settled shape to `$S/sample-bundle/` and run `node "$SL/validate-output-format.cjs" <file>` on each
12. **Proof grep.** Must print nothing:

```bash
grep -rnF --exclude-dir=.git --exclude-dir=changelog --exclude-dir=reports --exclude-dir=episodes --exclude-dir=export -e 'PRD-' -e '|PRD|' "AI Systems/Product Owner" "$SL" | grep -vE ':[0-9]+:- 20[0-9]{2}-[0-9]{2}-[0-9]{2} '
```

13. **Gates on the working tree.** Format gate diffed against `$S/format-before.txt` with line numbers set aside, both fixture runners, the playbook validator, residency, the cited lines diffed against `$S/cited-before.txt`, and `route_request` on `$story Order tracking. Break it into tasks.` returning intent and shape `STORY`
14. **Commit.** Read `git status` and the diff in both repositories. Stage named paths only, the 25 deletions included. The nested repo commit carries no attribution line, the Barter commit carries the session's attribution lines
15. **Gates on the commit.** `python3 "$SL/validate_parity.py" product-owner` and `bash "$SL/run_residency.sh" product-owner`. Then `validate.sh --strict` on this folder. Push waits for the operator's go-ahead
<!-- /ANCHOR:phases -->

---

<!-- ANCHOR:testing -->
## 5. TESTING STRATEGY

| Test Type | Scope | Tools |
|-----------|-------|-------|
| Naming | Every live file | The proof grep in step 12, and a count of `$prd` and "No `PRD -` prefix" before and after |
| Format | Instruction surface and the sample bundle | `validate-output-format.cjs`, system mode and artifact mode |
| Routing | Router contract and its mirror | `benchmark/router/run_fixtures.sh`, the `route_request` probe |
| Parity | 38 declared pairs, on the commit | `validate_parity.py product-owner` |
| Residency | Declared kernel statements | `run_residency.sh product-owner` |
| Playbook | 14 scenarios | `validate-playbook-package.cjs` |
| Line stability | Cited lines | `sed -n` snapshot diff |
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:dependencies -->
## 6. DEPENDENCIES

| Dependency | Type | Status | Impact if Blocked |
|------------|------|--------|-------------------|
| Operator decisions D1, D2, D4 | Internal | Green | No edits |
| `resync_statement.py`, `repoint_rename.py` | Internal | Green | Declaration and references drift from the files |
| Commit in both repositories | Internal | Pending | Parity cannot run on the new state |
| Operator push go-ahead | External | Pending | Commits stay local |
| Kernel review | External | Pending, operator only | Review not recorded |
<!-- /ANCHOR:dependencies -->

---

<!-- ANCHOR:rollback -->
## 7. ROLLBACK PLAN

- **Trigger**: A gate fails on the committed state, a mirror contradicts its source, or a cited line moved
- **Procedure**: `git revert` the phase commit in each repository, which restores the old names, versions and declaration together. The D4 removal reverts with it, so re-stage it if the rest is redone
<!-- /ANCHOR:rollback -->

---

<!-- ANCHOR:phase-deps -->
## L2: PHASE DEPENDENCIES

```
Baselines ──► D1 skill ──► D2 skill ──► Project side ──► Declaration ──► Renames ──► Bookkeeping ──► Commit ──► Parity
                                                              Docs and playbook ──┘
```

| Phase | Depends On | Blocks |
|-------|------------|--------|
| Baselines | None | Every edit |
| Skill sources | Baselines | Project side |
| Project side | Skill sources | Declaration, renames |
| Commit | All edits, working-tree gates | Parity on the commit |
<!-- /ANCHOR:phase-deps -->

---

<!-- ANCHOR:effort -->
## L2: EFFORT ESTIMATION

| Phase | Complexity | Estimated Effort |
|-------|------------|------------------|
| Setup | Low | Minutes, all read-only |
| Core Implementation | Med | Direct edits in about 20 files, one agent |
| Verification | Med | Gates twice, once on the tree and once on the commit |
| **Total** | | **About two hours** |
<!-- /ANCHOR:effort -->

---

<!-- ANCHOR:enhanced-rollback -->
## L2: ENHANCED ROLLBACK

### Pre-deployment Checklist
- [ ] Gates green on the committed state
- [ ] Kernel review recorded as pending
- [ ] Nothing pushed without the operator's go-ahead

### Rollback Procedure
1. Revert the phase commit in the Barter repo
2. Revert the matching commit in the Product Owner public repo
3. Rerun parity and residency for Product Owner

### Data Reversal
- **Has data migrations?** No
- **Reversal procedure**: N/A. The live claude.ai Project is untouched until the operator uploads a reviewed kernel
<!-- /ANCHOR:enhanced-rollback -->

---
