---
title: "Implementation Plan: Phase 3, the playbook rewrite and the approval gate"
description: "The rubric and the writer brief are fixed first, so five writer groups can author skill and Project twins in parallel against one set of rules. The root summaries are then copied from the scenario files, the run tooling is extended and self-tested with planted faults, both repos commit and the phase stops at the operator's approval."
trigger_phrases:
  - "playbook rewrite plan"
  - "scenario writer brief"
  - "attachment staging runner"
  - "bundle subfolder collector"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: plan-core | v2.2 -->
# Implementation Plan: Phase 3, the playbook rewrite and the approval gate

<!-- SPECKIT_LEVEL: 2 -->

---

<!-- ANCHOR:summary -->
## 1. SUMMARY

### Technical Context

| Aspect | Value |
|--------|-------|
| **Language/Stack** | Markdown scenario files, Python 3 run scripts, the Node playbook validator |
| **Framework** | The operator-scenario contract of `sk-create-manual-testing-playbook` and the benchmark runner and collector |
| **Storage** | Barter repo plus the Product Owner public repo at `AI Systems/Product Owner/.git` |
| **Testing** | `validate-playbook-package.cjs`, `run/selftest.py`, the runner's `--dry-run` |

### Overview
The rubric goes into the root first and the writer brief into `scratch/`, so every writer works from the same rules, names and attachments. Five writer groups each author a skill file and its Project twin together. The root summaries are then copied from the scenario files' contract Prompt lines rather than typed twice. In parallel the Sonnet `run/` folder is copied into a new report folder and extended for attachments and bundles, and `run/selftest.py` proves each change against planted faults. Both repos commit, and the phase ends at the operator's approval.
<!-- /ANCHOR:summary -->

---

<!-- ANCHOR:quality-gates -->
## 2. QUALITY GATES

### Definition of Ready
- [ ] Phase 001 committed, with `Story-` naming, the bundle rule and the renamed knowledge files
- [ ] Phase 002 committed, with every fixture its manifest names on disk
- [ ] The rubric split in `spec.md` section 3 accepted as the one to write

### Definition of Done
- [ ] Every row in `acceptance-criteria.md` is `Met`
- [ ] Validator `violations=0 warnings=0` at 46 scenarios, `run/selftest.py` exit 0
- [ ] Commits in both repos, no push without the go-ahead
- [ ] The operator's approval recorded in `goal.md` and `implementation-summary.md`
<!-- /ANCHOR:quality-gates -->

---

<!-- ANCHOR:architecture -->
## 3. ARCHITECTURE

### Pattern
Fix the rules, write in parallel against them, derive the root from the files, prove the tooling with planted faults, commit, then stop at the gate.

### Key Components
- **Root playbook**: `AI Systems/Product Owner/sk-product-owner/manual-testing-playbook/manual-testing-playbook.md`, the shared policy, the rubric, the wave table and the index
- **Scenario files**: 46 files in five `skill-*` and five `project-*` folders, per the manifest in `spec.md`
- **Writer brief**: `scratch/scenario-brief.md`, the authoring rules below plus the manifest, the phase 002 attachment list per ID and the phase 001 export names
- **Run tooling**: `AI Systems/Product Owner/benchmark/reports/2026-09-25--manual-testing-playbook--claude-opus-5-5-medium/run/`
- **Self-test**: `run/selftest.py`, no model calls, exit 0 or 1

### Scenario authoring rules
1. Frontmatter `title: "ID -- Name"`, a `description` and `version: 1.0.0.0`
2. Sections in order: `## 1. OVERVIEW`, `## 2. SCENARIO CONTRACT`, `## 3. TEST EXECUTION`, `## 4. SOURCE FILES`, `## 5. SOURCE METADATA`
3. Contract bullets in order: Objective, Real user request, Prompt, Attachments, Runtime profile, Precondition, Expected execution process, Expected signals, Desired user-visible outcome, Size band (advisory), Pass/fail, the SKIP line
4. `- Attachments:` holds comma-separated links such as `[roamstay-context.md](../../../benchmark/fixtures/companies/roamstay/roamstay-context.md)`, the company context file first, then the sources in the order Turn 1 names them
5. Every turn input is one line with no backtick, pipe or ISO date, UI strings in double quotes. Turn 1 names each attachment as `context/<basename>`. Twins share every turn word for word
6. The contract Prompt, the Turn 1 cell and the 9-column Exact prompt cell hold the same text, each wrapped in exactly two backticks
7. Pass clauses cite Blocking items only. The size band never appears in Pass/fail, and no Pass clause expects a discipline code in a Story or Epic H1
8. No `PARTIAL`, `READY`, `UNAUTOMATABLE` or `BLOCKED` in capitals, no `/Users/` or `/home/` path, no em dash, no semicolon
9. Source files: the root, the routed reference and template on the skill side, the kernel and the knowledge files by their post-001 names on the Project side, each attachment and the runtime's handover
10. Source metadata keeps `- Group:`, `- Playbook ID:`, `- Runtime:`, `- Canonical root source:` and `- Feature file path:`
11. Expected signals name exports in the post-001 words. `SST-004` and `PST-004` follow the expected behavior in `spec.md` section 3, which follows the phase 001 bundle design

### Run tooling changes
- **Runner**: `load_playbook` reads `- Attachments:` from section 2 and resolves each link against the scenario file. A missing file or a basename collision exits 2 before any scenario starts. `build()` copies each file to `<scratch>/context/<basename>` on both sides after the sandbox is built and before `snapshot()`. Each row, `manifest.json` and `meta.json` record basename, repository-relative source and sha256
- **Isolation**: `prove_isolation` takes the expected attachments and fails unless `context/` holds exactly those files with matching sha256 and no subfolder
- **Collector**: under `exports/`, a file in `export/<folder>/` lands at `<side>/<id> - <folder>/<file>`, and a reported Project path inside a folder does the same. `NUMBER_SLOT_RE` applies to the folder name. `context/` is skipped, and a modified attachment prints one warning line
- **check_run.py**: default `--model claude-opus-5-5`. A finding when `manifest.json` has an engine other than `claude`, a model other than the expected one or `thinking` other than `medium`

### Data Flow
Phase 001 names and the phase 002 manifest feed the brief. The brief feeds five writer groups. Their contract Prompt lines feed the root summaries. The validator and the selftest read the finished package, the commit pins it and the gate shows it to the operator.
<!-- /ANCHOR:architecture -->

---

<!-- ANCHOR:affected-surfaces -->
## FIX ADDENDUM: AFFECTED SURFACES

| Surface | Current Role | Action | Verification |
|---------|--------------|--------|--------------|
| Playbook root | Policy, rubric, waves, index | Rewritten | Validator, `load_waves`, citation read-back |
| 14 scenario files | Current set | 12 deleted, 2 rewritten, 44 created | Validator census 46, selftest parse |
| Runner, collector, check_run | Run tooling, Sonnet copies | Copied and extended in the new folder only | `run/selftest.py`, dry run |
| Sonnet report folder | Historical record | Unchanged | `git diff --stat` on it prints nothing |
| Sync Loop `check_criteria.sh` | Counts `- Playbook ID: (SID\|PID)-001` lines | Not a consumer of other changes | Both lines kept |
| Phase 005 graders | Read the root at the run commit | Consumer of the rubric | The rubric text is final before commit |

Required inventories:
- Every `file:line` citation in the root and the scenarios, read back on the post-001 commit
- Every existing advisory reading in root section 5, read back unchanged after the rubric lands
- Matrix axes: 23 IDs by 2 sides, 86 turns, 3 companies. Every row is asserted by the selftest
<!-- /ANCHOR:affected-surfaces -->

---

<!-- ANCHOR:phases -->
## 4. IMPLEMENTATION PHASES

Follow the ordered tasks in `tasks.md`. It owns the Setup, Implementation and Verification phase checkboxes and task state.

Commands, run from the repository root:

```bash
node .claude/skills/sk-doc/sk-create-manual-testing-playbook/scripts/validate-playbook-package.cjs --repo-root "$PWD" --skills-root "$PWD/AI Systems" --package "AI Systems/Product Owner/sk-product-owner/manual-testing-playbook"
python3 "AI Systems/Product Owner/benchmark/reports/2026-09-25--manual-testing-playbook--claude-opus-5-5-medium/run/selftest.py"
python3 "AI Systems/Product Owner/benchmark/reports/2026-09-25--manual-testing-playbook--claude-opus-5-5-medium/run/playbook_runner.py" --system "AI Systems/Product Owner" --out AI Systems/Product Owner/specs/013-po-realistic-playbook-opus-rerun/003-playbook-rewrite/scratch/dry-run --engine claude --model claude-opus-5-5 --effort medium --dry-run
git diff --stat -- "AI Systems/Product Owner/benchmark/reports/2026-09-25--manual-testing-playbook--claude-sonnet-5-medium"
grep -rn "PRD-" "AI Systems/Product Owner/sk-product-owner/manual-testing-playbook"
grep -rn $'\xe2\x80\x94' "AI Systems/Product Owner/sk-product-owner/manual-testing-playbook" "AI Systems/Product Owner/benchmark/reports/2026-09-25--manual-testing-playbook--claude-opus-5-5-medium"
```

The validator line must read `scenarios=46 categories=10 operator=46`, `violations=0 warnings=0` and `exit=0`. The three greps and the diff print nothing.
<!-- /ANCHOR:phases -->

---

<!-- ANCHOR:testing -->
## 5. TESTING STRATEGY

| Test Type | Scope | Tools |
|-----------|-------|-------|
| Package | Sections, links, IDs, prompt sync, census across 46 files | `validate-playbook-package.cjs` |
| Parse | 46 rows, manifest IDs, sides, slugs, turn counts, waves, twins, attachments against the phase 002 manifest, Turn 1 naming each attachment, the export word per file, every root link resolving | `run/selftest.py` importing `load_playbook` and `load_waves` |
| Isolation | Staged attachments pass, and an extra, a missing and an altered file each fail | `run/selftest.py` with `build`, staging and `prove_isolation` |
| Collector | A synthetic bundle on both sides, named as phase 001 sets it, lands in its subfolder, the Story-lane clarification outside it stays flat, `context/` is skipped, a dry run writes nothing. The same input through the Sonnet collector flattens, which proves the test sees the change | `run/selftest.py` |
| check_run | A synthetic manifest at effort `high` gives a finding, the default model is `claude-opus-5-5` | `run/selftest.py` |
| Manual | Twin pairs read side by side, citations read back, rubric read against the six existing readings | Operator and orchestrator |
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:dependencies -->
## 6. DEPENDENCIES

| Dependency | Type | Status | Impact if Blocked |
|------------|------|--------|-------------------|
| Phase 001 commit | Internal | Yellow, scaffolded | No export names, bundle paths or knowledge names to write against |
| Phase 002 commit and manifest | Internal | Yellow, scaffolded | No attachment names, and every scenario link fails |
| Sonnet `run/` folder | Internal | Green | No source for the copied scripts |
| Operator approval | External | Pending | Phase 004 cannot start |
<!-- /ANCHOR:dependencies -->

---

<!-- ANCHOR:rollback -->
## 7. ROLLBACK PLAN

- **Trigger**: The operator rejects the plan outright, or a check stays red after in-scope fixes
- **Procedure**: After commit, `git revert` the phase commit in each repo, which restores the 14 files and removes the new report folder. Before commit, restore the playbook paths only with the operator's approval. Never `reset --hard` in this shared tree
<!-- /ANCHOR:rollback -->

---


---

<!-- ANCHOR:phase-deps -->
## L2: PHASE DEPENDENCIES

```
Preflight ──► Rubric + brief ──► Five writer groups ──► Root from files ──► Validator ──┐
                    └──► Report folder + tooling ──► Selftest + dry run ────────────────┤
                                                                                        ├──► Commit ──► Approval gate
```

| Phase | Depends On | Blocks |
|-------|------------|--------|
| Preflight | Phases 001 and 002 committed | Everything |
| Rubric and brief | Preflight | Writers |
| Writers | Brief | Root summaries |
| Tooling | Preflight | Selftest |
| Commit | Validator and selftest green | Approval gate |
<!-- /ANCHOR:phase-deps -->

---

<!-- ANCHOR:effort -->
## L2: EFFORT ESTIMATION

| Phase | Complexity | Estimated Effort |
|-------|------------|------------------|
| Setup | Med | Preflight, citations, rubric and brief, about 1 hour |
| Core Implementation | High | Five writer groups in parallel plus the tooling, about 2 hours |
| Verification | Med | Validator, selftest, dry run, reviews, commits, about 1 hour |
| **Total** | | **About 4 hours before the operator's review** |
<!-- /ANCHOR:effort -->

---

<!-- ANCHOR:enhanced-rollback -->
## L2: ENHANCED ROLLBACK

### Pre-deployment Checklist
- [ ] Both repos' status and recent history inspected before staging
- [ ] Only the playbook package and the new report folder staged
- [ ] No push without the operator's go-ahead

### Rollback Procedure
1. `git revert` the phase commit in the Barter repo
2. `git revert` the matching commit in the Product Owner public repo
3. Rerun the validator and confirm the 14-scenario census returns
4. Tell the operator which commits were reverted and why

### Data Reversal
- **Has data migrations?** No
- **Reversal procedure**: N/A
<!-- /ANCHOR:enhanced-rollback -->

---
