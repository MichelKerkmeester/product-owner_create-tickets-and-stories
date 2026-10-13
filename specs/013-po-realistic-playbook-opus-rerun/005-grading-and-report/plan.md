---
title: "Implementation Plan: Phase 5, grade the Opus run and write the report"
description: "Five Opus 5.5 graders, one per folder group with both twins in it, grade every turn against the root at the run's commit. The orchestrator reviews every verdict, runs check_report.sh, writes the report from the files, takes the findings to the operator and closes the packet on fresh output."
trigger_phrases:
  - "opus grading plan"
  - "grader batches by folder group"
  - "check_report.sh"
  - "packet closure checks"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: plan-core | v2.2 -->
# Implementation Plan: Phase 5, grade the Opus run and write the report

<!-- SPECKIT_LEVEL: 2 -->

---

<!-- ANCHOR:summary -->
## 1. SUMMARY

### Technical Context

| Aspect | Value |
|--------|-------|
| **Language/Stack** | Markdown and CSV reports, Python and Bash graders |
| **Framework** | `AI Systems/Product Owner/benchmark/grader/`, Opus 5.5 grader agents |
| **Storage** | `<run folder>`, committed in both repos |
| **Testing** | `check_report.sh`, counts derived from `results.csv`, `validate.sh --recursive` |

### Overview
Grading follows the method of the 2026-09-25 Sonnet report: whole chains only, evidence for every verdict, a twin pair as the unit of comparison and three causes for a disagreement. Five graders on Opus 5.5 work in parallel, one per folder group, and return drafts. The orchestrator reviews every draft, settles each cross-batch reading once, runs `check_report.sh` and writes the report from the files, never from memory. The findings then go to the operator, and the packet closes on fresh output.
<!-- /ANCHOR:summary -->

---

<!-- ANCHOR:quality-gates -->
## 2. QUALITY GATES

### Definition of Ready
- [ ] Phase 004 closed, with its commits recorded
- [ ] Every event stream of the run still on disk
- [ ] Grading brief written from the sources at `<run commit>`

### Definition of Done
- [ ] All acceptance criteria met
- [ ] Every FAIL and every twin disagreement read twice
- [ ] Report committed and the parent goal criteria checked with fresh output
<!-- /ANCHOR:quality-gates -->

---

<!-- ANCHOR:architecture -->
## 3. ARCHITECTURE

### Pattern
Grade in parallel by folder group, review and adjudicate once, write one report.

### Key Components
- **Grading brief**: one file in this phase's `scratch/` that every grader gets. It holds the commits, the root sections at `<run commit>` (Scenario acceptance rules, Clarification turns, Rendering without a Canvas panel, Export names, Identity handover rule, Defect severity, Ticket realism), the verdict rule, the addition-naming rule, the evidence rule and the `results.csv` row contract
- **Graders**: five Opus 5.5 agents through the `opus-medium` definition, or the Agent tool's `model: opus` if that definition does not load. Batches are identity (2 scenarios), backlog (18), document (8), story (14) and interactive routing (4). Each reads its scenario files, replies, event streams, skill exports and the fixtures its scenarios attach, and returns a draft row and an evidence note per scenario plus a realism entry per export
- **Orchestrator review**: every draft checked against its evidence, cross-batch readings settled once, every FAIL and every disagreement read a second time
- **Report checker**: `benchmark/grader/check_report.sh <run folder>`, which runs the reply linter and the twin divergence check

### Data Flow
Run folder, streams and exports go to the graders. Drafts go to the orchestrator. Reviewed verdicts go into `results.csv` and `grading-notes.md`. The checker adds `hvr-lint.csv` and the twin findings. `results.md` and the README are written from `results.csv`.
<!-- /ANCHOR:architecture -->

---

<!-- ANCHOR:affected-surfaces -->
## FIX ADDENDUM: AFFECTED SURFACES

| Surface | Current Role | Action | Verification |
|---------|--------------|--------|--------------|
| `<run folder>` | Run output and the phase 004 run record | Grading and write-up added | `check_report.sh`, counts from `results.csv` |
| `export/benchmark/` | Deliverables | Read and reviewed, never edited | One realism entry per file |
| Skill, kernel, knowledge, playbook | Rules under test | Unchanged unless the operator decides a repair | `validate_parity.py product-owner` and the format gate after any repair |

Required inventories:
- The 23 twin pairs from the playbook's S and P IDs at `<run commit>`
- Every file in `export/benchmark/`, from `find` sorted
- Every FAIL with the rule and the file that states it at `<run commit>`
<!-- /ANCHOR:affected-surfaces -->

---

<!-- ANCHOR:phases -->
## 4. IMPLEMENTATION PHASES

Follow the ordered tasks in `tasks.md`. It owns the Setup, Implementation and Verification phase checkboxes and task state.

### Ordered steps and commands

Commands run from the workspace root unless they start with `cd`.

```bash
PO="AI Systems/Product Owner"
RUN="$PO/benchmark/reports/<run date>--manual-testing-playbook--claude-opus-5-5-medium"
P5="AI Systems/Product Owner/specs/013-po-realistic-playbook-opus-rerun/005-grading-and-report"
```

1. **Sources at the run's commit.** Take the Product Owner commit from the phase 004 run record, then:
   ```bash
   git -C "$PO" show <po commit>:sk-product-owner/manual-testing-playbook/manual-testing-playbook.md > "$P5/scratch/root-at-run.md"
   git -C "$PO" ls-tree -r --name-only <po commit> -- sk-product-owner/manual-testing-playbook benchmark/fixtures/companies > "$P5/scratch/sources-at-run.txt"
   ```
   Every other file a grader cites is read the same way, with `git show <po commit>:<path>`.
2. **Inventories.**
   ```bash
   find "$PO/export/benchmark" -type f | sort > "$P5/scratch/exports.txt" && wc -l < "$P5/scratch/exports.txt"
   find "$RUN" -name 'events-turn-*.jsonl' | wc -l
   ```
   The stream count must equal the declared turn count phase 004 recorded.
3. **Grading brief.** Write `$P5/scratch/grading-brief.md` from `root-at-run.md`. Settle nothing the root leaves open: an open reading becomes a finding for the operator.
4. **Grade.** Dispatch the five batches in one message. Each returns, per scenario, a draft `results.csv` row, an evidence note naming the reply line, stream event or file line that decides it, and, per export, a realism entry.
5. **Review.** Check every draft against its evidence. List each Blocking rule of Defect severity and Ticket realism with the rows it decided, and make each rule read the same in every batch. Read every FAIL a second time.
6. **Write `results.csv`**, then check it:
   ```bash
   cd "$RUN" && python3 -c "import csv;r=list(csv.DictReader(open('results.csv')));print(len(r),list(r[0].keys()),sorted({x['model'] for x in r}))"
   ```
   Expected `46`, the nine header columns in order, and `['claude-opus-5-5-medium']`.
7. **Report checker**, from the Product Owner folder:
   ```bash
   cd "AI Systems/Product Owner" && bash benchmark/grader/check_report.sh "benchmark/reports/<run date>--manual-testing-playbook--claude-opus-5-5-medium"
   ```
   The exit code counts checks with findings. Exit 64 or 66, or a check marked as unable to run, is a harness problem to fix before grading closes. Every finding goes into `grading-notes.md`.
8. **Twins.** Classify every pair `twin_divergence` lists as disagreeing: rule gap, parity gap or runtime fault, each confirmed in the rule files on both sides and tested from a second direction.
9. **Realism review.** One entry per line of `scratch/exports.txt`: artifact kind and template shape against the routed template's required sections, company facts set beside the fixture text, and the line count against the scenario's advisory band. The Blocking items of the rubric feed the verdicts, the size band stays advisory.
10. **Write the report.** `results.md` with the verdict table and a 23-row twin table. The README with any handover failure first, the counts and the command that derives them, then the findings and next steps above the phase 004 run record. The count command:
    ```bash
    cd "$RUN" && python3 -c "
    import csv,collections as c
    r=list(csv.DictReader(open('results.csv')))
    for k,v in sorted(c.Counter((x['runtime'],x['result']) for x in r).items()): print(k[0],k[1],v)
    print('facts_intact yes',sum(x['facts_intact']=='yes' for x in r),'of',len(r))
    print('after_failed_gate yes',sum(x['after_failed_gate']=='yes' for x in r))
    d={x['id']:x['result'] for x in r}
    print('twin pairs differing',sum(d[k]!=d['P'+k[1:]] for k in d if k[0]=='S'),'of',sum(k[0]=='S' for k in d))
    "
    ```
11. **Findings.** Put every finding to the operator through the ask tool, one question per decision. Record each answer in `implementation-summary.md`.
12. **Decided repairs.** For each, add its own tasks to `tasks.md`, edit the source first and then its mirrors, run `validate_parity.py product-owner` and the format gate, rerun the affected scenarios with `--out remeasure-<slug>/run-<n>` from `<run folder>`, and grade the round like the main run.
13. **Close.**
    ```bash
    bash .skilled/skills/system-spec-kit/runtime/cli/spec/validate.sh AI Systems/Product Owner/specs/013-po-realistic-playbook-opus-rerun --recursive
    grep -L '^\*\*Closeable:\*\* Yes' AI Systems/Product Owner/specs/013-po-realistic-playbook-opus-rerun/0*/acceptance-criteria.md
    ```
    The first must end in 0 errors and the `grep` must print nothing. Then check each of the seven parent goal criteria with fresh output and log it in the parent `goal.md`: the PRD grep of phase 001, then `python3 validate_parity.py product-owner` and `node validate-output-format.cjs --system product-owner` run from the Claude Project Sync Loop folder at the `AI Systems/` root, the playbook validator with the arguments phase 003 recorded, the approval evidence of phase 004, the counts above, the file count of `export/benchmark/` against the phase 004 collection count plus any remeasure rounds and the commits and push state below.
14. **Commit and push.** Stage explicit paths in the Product Owner repo and commit with no attribution line, then in Barter with the attribution lines. Push only on the operator's go-ahead, Barter through the michelkerkmeester-barter account. The kernel review stays pending in `AI Systems/Product Owner/SYNC.md` unless the operator confirms it.
<!-- /ANCHOR:phases -->

---

<!-- ANCHOR:testing -->
## 5. TESTING STRATEGY

| Test Type | Scope | Tools |
|-----------|-------|-------|
| Lint | Every captured reply | `lint_replies.py` through `check_report.sh` |
| Twin | 23 S and P pairs | `twin_divergence.py` through `check_report.sh` |
| Counts | Every total in the report | Commands over `results.csv`, named in the report |
| Realism | Every export | One entry per file, the count checked against `find` |
| Packet | All five phases | `validate.sh --recursive` and the `Closeable` grep |
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:dependencies -->
## 6. DEPENDENCIES

| Dependency | Type | Status | Impact if Blocked |
|------------|------|--------|-------------------|
| Phase 004 output and commits | Internal | Pending | Nothing to grade |
| `check_report.sh` | Internal | Green, present in `benchmark/grader/` | No lint or twin check |
| Operator decisions on findings | Human | Pending | Closing waits |
| Product Owner public repo | External | Green | Commit later |
<!-- /ANCHOR:dependencies -->

---

<!-- ANCHOR:rollback -->
## 7. ROLLBACK PLAN

- **Trigger**: A report found wrong after commit, or a decided repair that breaks the parity gate or a rerun
- **Procedure**: Correct the report and the CSV together in a follow-up commit that says what changed. `git revert` a repair commit in each repo it touched and rerun its scenarios
<!-- /ANCHOR:rollback -->

---


---

<!-- ANCHOR:phase-deps -->
## L2: PHASE DEPENDENCIES

```
Setup ──► Grade x5 in parallel ──► Review ──► check_report.sh ──► Write report ──► Operator findings ──► Decided repairs ──► Close and commit
```

| Phase | Depends On | Blocks |
|-------|------------|--------|
| Grade | Phase 004, grading brief | Review |
| Review and checker | Grade | Report |
| Report and findings | Review and checker | Repairs, closing |
| Close and commit | Report, operator decisions | None |
<!-- /ANCHOR:phase-deps -->

---

<!-- ANCHOR:effort -->
## L2: EFFORT ESTIMATION

| Phase | Complexity | Estimated Effort |
|-------|------------|------------------|
| Grading | High | One parallel pass of five batches |
| Review, checker and adjudication | Med | One pass across all batches |
| Report, findings and closing | Med | One pass, plus the operator's time on findings |
| **Total** | | **Three to five hours of wall time before any repair** |
<!-- /ANCHOR:effort -->

---

<!-- ANCHOR:enhanced-rollback -->
## L2: ENHANCED ROLLBACK

### Pre-deployment Checklist
- [ ] Counts recomputed from `results.csv` before commit
- [ ] `check_report.sh` output saved in `grading-notes.md`
- [ ] Both repos fetched and level

### Rollback Procedure
1. Identify the wrong statement
2. Correct the report and the CSV together
3. Recompute the counts
4. Commit the correction in each repo

### Data Reversal
- **Has data migrations?** No
- **Reversal procedure**: `git revert` in each repo. Never `reset --hard` in this shared tree
<!-- /ANCHOR:enhanced-rollback -->

---
