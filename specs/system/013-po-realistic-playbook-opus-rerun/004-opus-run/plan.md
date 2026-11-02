---
title: "Implementation Plan: Phase 4, run the realistic playbook on Opus 5.5 medium"
description: "A dry run, a two-scenario smoke run that settles the model set, then the full 46-scenario run through the Claude engine of the phase 003 runner at effort medium, followed by check_run.py, the collector's dry run and the collection into export/benchmark."
trigger_phrases:
  - "opus run plan"
  - "playbook runner claude engine"
  - "smoke run model check"
  - "collect_exports dry run"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: plan-core | v2.2 -->
# Implementation Plan: Phase 4, run the realistic playbook on Opus 5.5 medium

<!-- SPECKIT_LEVEL: 2 -->

---

<!-- ANCHOR:summary -->
## 1. SUMMARY

### Technical Context

| Aspect | Value |
|--------|-------|
| **Language/Stack** | Python 3 runner, Claude CLI |
| **Framework** | `<run folder>/run/playbook_runner.py`, Claude engine, with the phase 003 attachment extension |
| **Storage** | `<run folder>` and `AI Systems/Product Owner/export/benchmark/` |
| **Testing** | The runner's isolation proof, `run/check_run.py`, the collector's dry run |

### Overview
The run folder phase 003 created runs its own runner copy against the system three levels up, exactly as the Sonnet run did with `--system ../../..`. A dry run confirms the parse and a smoke run of the two identity handovers settles which model names the streams carry. The full run then captures every turn. `check_run.py` then reads completeness and models from the files, and the collector copies the deliverables into the emptied `export/benchmark/`.
<!-- /ANCHOR:summary -->

---

<!-- ANCHOR:quality-gates -->
## 2. QUALITY GATES

### Definition of Ready
- [ ] The operator's approval of the scenario plan is on record
- [ ] Phases 001 to 003 committed, and Barter and Product Owner HEADs recorded
- [ ] Claude CLI authenticated and its version recorded

### Definition of Done
- [ ] All acceptance criteria met
- [ ] `check_run.py --model claude-opus-5-5` exits 0 on `<run folder>`
- [ ] Run output and collection committed in both repos
<!-- /ANCHOR:quality-gates -->

---

<!-- ANCHOR:architecture -->
## 3. ARCHITECTURE

### Pattern
One runner process at a time for Product Owner, fanning out to scenario workers, each worker holding one sandbox and one Claude session per scenario chain.

### Key Components
- **Runner**: `run/playbook_runner.py`, engine `claude`, model `claude-opus-5-5`, effort `medium`. It runs `SID-001` and `PID-001` first and alone, then the rest in skill wave order with each Project twin beside its skill twin. Three attempts per scenario (`ATTEMPTS`, line 55 of the Sonnet copy) and 900 seconds per turn
- **Attachments**: the phase 003 extension copies each fixture a scenario names into `<scratch>/context/` before the baseline snapshot, so an attachment never shows in the ledger unless a turn changes it
- **Isolation**: a fresh scratch tree per scenario under `$TMPDIR/pi-playbook-bench/product-owner/<side>/<ID>`, `--setting-sources ""`, an empty MCP config and a sandbox profile opening only that scenario's folders. A failed proof stops the runner with exit 2
- **Run check**: `run/check_run.py`, which exits 0 only when every manifest scenario has a completed `meta.json`, a non-empty reply per declared turn and an event stream whose system event, assistant messages and `modelUsage` name only the expected model
- **Collector**: `run/collect_exports.py`, which copies skill files and Project blocks into `export/benchmark/`, keeps bundle subfolders and never deletes

### Data Flow
Scenario file and its attachments, then a scratch tree, then one Claude session per scenario chain, then replies, `meta.json` and event streams per scenario, then `run-status.json` and `manifest.json`, then `check_run.py`, then the collection.
<!-- /ANCHOR:architecture -->

---

<!-- ANCHOR:affected-surfaces -->
## FIX ADDENDUM: AFFECTED SURFACES

| Surface | Current Role | Action | Verification |
|---------|--------------|--------|--------------|
| Runner and collector | Drive the run, collect its deliverables | Unchanged, as phase 003 committed them | `shasum -a 256 run/*.py` matches the phase 003 record |
| `run/check_run.py` | Completeness and model check | Widened only on smoke evidence | Its diff and the evidence in the run `README.md` |
| Playbook, fixtures, skill, kernel, knowledge | What the run measures | Read only | HEADs and `git status` unchanged before and after |
| `export/benchmark/` | Deliverables | Created from the collection | The collector's dry run lists only new files |

Required inventories:
- Every scenario ID from the dry run, compared with `run-status.json` after the run: 46 rows
- Every model name in every event stream, compared with the allowed set
<!-- /ANCHOR:affected-surfaces -->

---

<!-- ANCHOR:phases -->
## 4. IMPLEMENTATION PHASES

Follow the ordered tasks in `tasks.md`. It owns the Setup, Implementation and Verification phase checkboxes and task state.

### Ordered steps and commands

Commands run from the workspace root unless they start with `cd`. Shell state does not persist between tool calls, so each block sets what it needs.

```bash
PO="AI Systems/Product Owner"
RUN="$PO/benchmark/reports/<run date>--manual-testing-playbook--claude-opus-5-5-medium"
P4="AI Systems/Product Owner/specs/013-po-realistic-playbook-opus-rerun/004-opus-run"
```

From inside `<run folder>`, the workspace root is `../../../../..`, so this phase's scratch folder is `../../../../../$P4/scratch`.

1. **Approval.** Read the operator's approval of the scenario plan in the phase 003 record and the parent `goal.md` log. Without it, stop here (D6).
2. **Sources and harness.** Record the output of each:
   ```bash
   git -C "$PO" rev-parse HEAD && git rev-parse HEAD
   git -C "$PO" status --porcelain -- sk-product-owner "claude project" AGENTS.md benchmark/fixtures
   shasum -a 256 "$RUN"/run/*.py
   claude --version
   pgrep -fl playbook_runner.py
   ```
   The `status` and `pgrep` lines must print nothing.
3. **Ignore rules.** `test -f "$RUN/.gitignore" || cp "$PO/benchmark/reports/2026-09-25--manual-testing-playbook--claude-sonnet-5-medium/.gitignore" "$RUN/"`
4. **Dry run.**
   ```bash
   cd "$RUN" && python3 run/playbook_runner.py --system ../../.. --out . --engine claude --model claude-opus-5-5 --effort medium --dry-run > ../../../../../AI Systems/Product Owner/specs/013-po-realistic-playbook-opus-rerun/004-opus-run/scratch/dry-run.json
   python3 -c "import json,sys;d=json.load(open(sys.argv[1]));print(len(d),'scenarios',sum(len(x['turns']) for x in d),'turns',sum(x['side']=='skill' for x in d),'skill')" AI Systems/Product Owner/specs/013-po-realistic-playbook-opus-rerun/004-opus-run/scratch/dry-run.json
   ```
   Expected `46 scenarios 86 turns 23 skill` by the approved catalog. Compare each row's attachments with its scenario's `- Attachments:` bullet.
5. **Smoke run**, into this phase's scratch so the full run stays one clean pass:
   ```bash
   cd "$RUN" && python3 run/playbook_runner.py --system ../../.. --out ../../../../../AI Systems/Product Owner/specs/013-po-realistic-playbook-opus-rerun/004-opus-run/scratch/smoke --engine claude --model claude-opus-5-5 --effort medium --jobs 2 --ids SID-001,PID-001
   cd "$RUN" && python3 run/check_run.py ../../../../../AI Systems/Product Owner/specs/013-po-realistic-playbook-opus-rerun/004-opus-run/scratch/smoke --model claude-opus-5-5 | grep -E '^[SP]ID-001:'
   python3 -c "import json,sys;[print(r['id'],r['turn'],r['status'],r['response_models'],round(r['cost_usd'],2),r['wall_s']) for r in map(json.loads,open(sys.argv[1]))]" AI Systems/Product Owner/specs/013-po-realistic-playbook-opus-rerun/004-opus-run/scratch/smoke/run-log.jsonl
   ```
   The `grep` must print nothing. The runner writes the full manifest even under `--ids`, so the `check_run.py` summary line also counts 44 scenarios the smoke never ran, and those findings are expected. The last command must print four `ok` turns, each naming claude-opus-5-5 alone.
6. **Model set.** When the streams name one dated ID and nothing else, pass that exact ID to `check_run.py --model` from here on, and keep `claude-opus-5-5` as the runner's `--model`. When they name a second model, add an `--allow <name>` option to `<run folder>/run/check_run.py` that admits that one name beside the expected model, which must still appear in every turn. Write the stream, the event field and the name into the run `README.md`, then rerun step 5's check with the option. When they name claude-opus-5-5 alone, change nothing.
7. **Estimate.** Multiply the smoke's mean cost and wall time per turn by the dry run's turn count and record both in `implementation-summary.md` before step 8.
8. **Full run**, in the background:
   ```bash
   cd "$RUN" && { python3 run/playbook_runner.py --system ../../.. --out . --engine claude --model claude-opus-5-5 --effort medium --jobs 4; echo "runner exit $?"; } > run-progress.txt 2>&1
   ```
   `runner exit 0` means every scenario ran, `1` means at least one failed after three attempts and `2` means an isolation proof failed and nothing from the round is used.
9. **Resume**, only for a harness or account cause such as an auth lapse, a rate limit or a timeout. Move the earlier attempts aside first, because a retry reuses their folder names:
   ```bash
   cd "$RUN" && for d in failed-attempts/*/<ID>-attempt-*; do mv "$d" "$d-round-1"; done
   cd "$RUN" && { python3 run/playbook_runner.py --system ../../.. --out . --engine claude --model claude-opus-5-5 --effort medium --jobs 4 --ids <ID>,<ID>; echo "runner exit $?"; } >> run-progress.txt 2>&1
   ```
   A scenario that still fails is a run defect, recorded with its cause.
10. **Run check.**
    ```bash
    cd "$RUN" && python3 run/check_run.py . --model claude-opus-5-5
    cd "$RUN" && python3 -c "import json;r=json.load(open('run-status.json'));print(len(r),'rows',sum(x['status']=='ok' for x in r),'ok',sum(x['attempts']>1 for x in r),'retried')"
    ```
    Expected exit 0 with `46 scenarios, 86 declared turns, 86 event streams read, 0 finding(s), expected model claude-opus-5-5`, and `46 rows 46 ok`.
11. **Sources unchanged.** Rerun the `rev-parse` and `status` lines of step 2 and compare.
12. **Collector dry run.**
    ```bash
    cd "$RUN" && find ../../../export/benchmark -type f 2>/dev/null | wc -l
    cd "$RUN" && python3 run/collect_exports.py . ../../../export/benchmark --dry-run > ../../../../../AI Systems/Product Owner/specs/013-po-realistic-playbook-opus-rerun/004-opus-run/scratch/collect-dry-run.txt
    ```
    The count must be 0. Every listed line must name one of the 46 IDs and a deliverable: a skill file the runtime wrote under `export/`, or a Project block. A line naming anything else is recorded for phase 005 before the real collection.
13. **Collect.**
    ```bash
    cd "$RUN" && python3 run/collect_exports.py . ../../../export/benchmark
    cd "$RUN" && find ../../../export/benchmark -type f | wc -l
    ```
    The count must equal the dry run's line count. Set every `project` line beside its reply and note the result.
14. **Run record.** Write `<run folder>/README.md`: commits, harness hashes, CLI version, model, effort, jobs, the smoke result and model set, wall time, cost, retries, run defects and the collection count.
15. **Commit.** Check that `git -C "$PO" status --porcelain --untracked-files=all -- benchmark/reports export/benchmark` offers no event stream, stderr, transcript, failed attempt or `exports/` copy. Stage explicit paths in the Product Owner repo and commit with no attribution line, then stage the same paths in Barter and commit with the attribution lines. Push only on the operator's go-ahead, Barter through the michelkerkmeester-barter account.
<!-- /ANCHOR:phases -->

---

<!-- ANCHOR:testing -->
## 5. TESTING STRATEGY

| Test Type | Scope | Tools |
|-----------|-------|-------|
| Isolation | Each scenario's scratch tree | The runner's own proof, exit 2 on failure |
| Model | Every event stream | `check_run.py --model claude-opus-5-5`, smoke first |
| Completeness | Every declared turn | `check_run.py` and `run-status.json` |
| Collection | Every deliverable | The collector's dry run, then a file count after the collection |
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:dependencies -->
## 6. DEPENDENCIES

| Dependency | Type | Status | Impact if Blocked |
|------------|------|--------|-------------------|
| Operator approval of the scenario plan | Human | Pending | No run |
| Phase 003 run folder and harness | Internal | Pending | No run |
| Claude CLI | External | Green when `claude --version` answers | No run |
| Account limits | External | Unknown until the smoke run | Slower run, resume by ID |
<!-- /ANCHOR:dependencies -->

---

<!-- ANCHOR:rollback -->
## 7. ROLLBACK PLAN

- **Trigger**: An isolation failure, a model name the smoke did not justify, a runner defect or a source change during the run
- **Procedure**: Stop the runner and move that round's untracked output aside, keeping `failed-attempts/` for the record. Then rerun the affected scenarios by `--ids`. After a commit, `git revert` the run commit in each repo
<!-- /ANCHOR:rollback -->

---


---

<!-- ANCHOR:phase-deps -->
## L2: PHASE DEPENDENCIES

```
Approval ──► Dry run ──► Smoke run and model set ──► Full run ──► check_run ──► Collect ──► Commit
```

| Phase | Depends On | Blocks |
|-------|------------|--------|
| Dry run | Approval, phase 003 | Smoke run |
| Smoke run | Dry run | Full run |
| Full run | Smoke run and model set | Run check |
| Run check and collection | Full run | Commit, phase 005 |
<!-- /ANCHOR:phase-deps -->

---

<!-- ANCHOR:effort -->
## L2: EFFORT ESTIMATION

| Phase | Complexity | Estimated Effort |
|-------|------------|------------------|
| Setup, dry run and smoke | Low | Under 30 minutes |
| Full run | High | About one hour of wall time, unattended, up to three with retries or a lower `--jobs` |
| Checks, collection and commit | Low | Under an hour |
| **Total** | | **Two to four hours, refined by the smoke run's estimate** |
<!-- /ANCHOR:effort -->

---

<!-- ANCHOR:enhanced-rollback -->
## L2: ENHANCED ROLLBACK

### Pre-deployment Checklist
- [ ] HEADs and harness hashes recorded
- [ ] `.gitignore` in place before the first stream is written
- [ ] `export/benchmark/` holds no file before the collection

### Rollback Procedure
1. Stop the runner
2. Move the round's untracked output aside, keeping `failed-attempts/`
3. Fix the cause outside this phase or report it to the operator
4. Rerun the affected scenarios by `--ids`

### Data Reversal
- **Has data migrations?** No
- **Reversal procedure**: `git revert` the run commit in each repo. Never `reset --hard` in this shared tree
<!-- /ANCHOR:enhanced-rollback -->

---
