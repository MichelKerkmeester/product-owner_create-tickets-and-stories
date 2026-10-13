---
title: "Feature Specification: Phase 5, grade the Opus run and write the report"
description: "Grade every turn of the 46-scenario claude-opus-5-5 medium run against the rewritten playbook root at the run's commit, review the realism of every collected export, write the report, bring the findings to the operator and close the packet."
trigger_phrases:
  - "opus run grading"
  - "ticket realism review"
  - "twin agreement adjudication"
  - "packet 076 closure"
importance_tier: "important"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.2 -->
# Feature Specification: Phase 5, grade the Opus run and write the report

<!-- SPECKIT_LEVEL: 2 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 2 |
| **Priority** | P0 |
| **Status** | Complete |
| **Created** | 2026-09-25 |
| **Branch** | `main` |
| **Parent Spec** | ../spec.md |
| **Phase** | 5 of 5 |
| **Predecessor** | 004-opus-run |
| **Successor** | None |
| **Handoff Criteria** | A committed report with 46 graded rows and every export reviewed, every phase closeable and the parent goal criteria met with fresh output |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:phase-context -->
## Phase Context

This is **Phase 5** of the packet that rewrites the Product Owner manual testing playbook around realistic tickets for three fictional companies and reruns both packagings on claude-opus-5-5 medium.

In every document of this phase, `<run folder>` means `AI Systems/Product Owner/benchmark/reports/<run date>--manual-testing-playbook--claude-opus-5-5-medium/`, and `<run commit>` means the Product Owner and Barter commits phase 004 recorded before the run.

**Scope Boundary**: grading and reporting inside `<run folder>`, then closing the packet. Findings about the skill, kernel, knowledge files or playbook go to the operator. A repair happens only on the operator's decision, as its own tasks with a rerun of the affected scenarios.

**Dependencies**:
- Phase 004 closed: 46 whole scenarios in `<run folder>`, their event streams still on disk and the collection in `AI Systems/Product Owner/export/benchmark/`
- The commits phase 004 recorded, so every rule is read with `git show <run commit>:<path>`
- `AI Systems/Product Owner/benchmark/grader/check_report.sh`, which runs `lint_replies.py` and `twin_divergence.py`
- The company fixtures in `AI Systems/Product Owner/benchmark/fixtures/companies/` at the run's commit

**Deliverables**:
- In `<run folder>`: `results.csv`, `results.md`, the README with its counts, `grading-notes.md` with the realism review and `hvr-lint.csv`
- The findings put to the operator through the ask tool, each with the operator's decision recorded
- A closed packet: every phase closeable, the parent goal checked with fresh output, commits in both repos and a push on the operator's go-ahead

**Changelog**:
- When this phase closes, refresh the matching file in ../changelog/ using the parent packet number plus this phase folder name
<!-- /ANCHOR:phase-context -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
Run output is not a result until each scenario is graded whole against the rules the runtime saw. This run adds a rubric that has never graded anything, Ticket realism, and 46 scenarios with about 86 turns is too much for one grader to read the same way from start to end. The grading needs batches that read one rubric at one commit, an orchestrator who reviews every verdict and counts derived from the files. The packet closes only on fresh output.

### Purpose
One committed report that says, for each of the 46 scenarios, what passed and what failed and why, how each twin pair compares and how real each export reads.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- One verdict per scenario, PASS, FAIL or SKIP, from all its turns, against the root's Scenario acceptance rules, Clarification turns, Rendering without a Canvas panel, Export names (`Story-` and the bundle subfolder), Identity handover rule, Defect severity and Ticket realism sections, read at `<run commit>`
- Five grader batches on Opus 5.5 run in parallel, one per folder group with both twins in it, and the orchestrator's review of every verdict before any file is written
- `results.csv`, `results.md`, the README counts, `grading-notes.md` and `hvr-lint.csv`
- `check_report.sh` on `<run folder>`, its findings folded into the grading
- Twin agreement for all 23 S and P pairs, each disagreement classified as a rule gap, a parity gap or a runtime fault
- A realism review of every file in `export/benchmark/`: artifact kind and template shape, company facts used verbatim from the fixtures and size against the scenario's advisory band
- Findings to the operator through the ask tool, and each decided repair as its own tasks with a rerun of the affected scenarios
- Packet closure: recursive validation, closeable phases, fresh checks of the parent goal criteria, commits and a push on the operator's go-ahead

### Out of Scope
- A repair the operator has not decided - parent decision D7
- Recording the kernel review - it stays pending unless the operator confirms it (D7)
- A verdict comparison with the 2026-09-25 Sonnet run - every scenario is new, so the report names none as comparable and describes behavior only
- Prompt Improver and Deal Templates - parent decision D5

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| `<run folder>/results.csv` | Create | 46 rows, one per scenario |
| `<run folder>/results.md` | Create | Verdict table and twin table |
| `<run folder>/README.md` | Modify | Handover status first, counts with the command that derives them, findings and next steps, above the phase 004 run record |
| `<run folder>/grading-notes.md` | Create | Evidence per verdict, the realism review, twin adjudications and the `check_report.sh` output |
| `<run folder>/hvr-lint.csv` | Create | Written by `check_report.sh` |
| `<run folder>/remeasure-<slug>/run-<n>/` | Create, only on a decided repair | Rerun of the affected scenarios, graded |
| Skill, kernel, knowledge or playbook files | Modify, only on the operator's decision | Named per decided repair, with their mirrors |
| `AI Systems/Product Owner/specs/013-po-realistic-playbook-opus-rerun/goal.md` log and `spec.md` phase map | Modify | Closure evidence and phase status |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | Every scenario has exactly one verdict, graded on all its turns and citing the reply, stream or file that decides it. A turn that misses any Pass clause fails the scenario |
| REQ-002 | Graders read the root, the scenario files, the rule sources and the fixtures with `git show <run commit>:<path>`, never from the working tree |
| REQ-003 | `results.csv` has the header `id,runtime,model,result,turns_run,turns_declared,after_failed_gate,facts_intact,note` and exactly 46 rows, one per scenario ID |
| REQ-004 | Every count in the README and `results.md` is derived from `results.csv` by a command the report names, and matches it |
| REQ-005 | The orchestrator reviews every verdict from every batch before any report file is written, and reads every FAIL and every twin disagreement a second time |
| REQ-006 | `check_report.sh` runs on `<run folder>` with both checks executing and writes `hvr-lint.csv`. Every finding it reports appears in `grading-notes.md` |
| REQ-007 | Every file in `export/benchmark/` has a realism entry: artifact kind and template shape, company facts checked verbatim against the fixtures and size against the scenario's advisory band |
| REQ-008 | Findings go to the operator through the ask tool, and no repair lands without the operator's recorded decision (D7) |
| REQ-009 | At closing, `validate.sh --recursive` on the packet reports 0 errors, every phase's `acceptance-criteria.md` reads `Closeable: Yes` and each parent goal completion criterion is checked with fresh output |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement |
|----|-------------|
| REQ-010 | Each of the 23 twin pairs has an agreement entry, and each disagreement carries one cause, rule gap, parity gap or runtime fault, confirmed in the rule files on both sides |
| REQ-011 | A failed handover opens the README before any other result and names the runtime whose other verdicts it puts in question |
| REQ-012 | Each decided repair becomes its own tasks with its source files and mirrors, and the affected scenarios rerun into a `remeasure-<slug>/run-<n>/` round of `<run folder>` that is graded like the main run |
| REQ-013 | The report is committed in Barter and the Product Owner public repo, with no attribution lines in the public commit, and pushed on the operator's go-ahead. No `SYNC.md` marks a kernel review done without the operator's confirmation |

> Acceptance criteria for these requirements live in `acceptance-criteria.md`,
> which is the document that decides whether this packet may close.
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: 46 graded scenarios in one committed report, every count derived from `results.csv`
- **SC-002**: Every export reviewed for realism, every twin disagreement given a cause and a findings list the operator has ruled on
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Risk | Grader drift between batches: five graders read one rubric five ways | High | One grading brief for all five, holding the rubric text at `<run commit>`, the verdict rule and the CSV row contract. The orchestrator reviews every verdict and checks that each Blocking rule decided the same way in every batch |
| Risk | Twin disagreement that comes from the grading rather than the runtimes | Med | Both twins of a pair sit in one batch. Every disagreement is read a second time and confirmed in both sides' rule files |
| Risk | The Ticket realism rubric meets its first real exports | Med | Its Blocking and Advisory split, as phase 003 settled it, decides. A case the rubric does not settle goes to the operator as a finding and is never graded by a guess |
| Risk | Cost and time: about 86 turns, their streams and every export read by five Opus graders | Med | Graders read the captured files and rerun nothing. Batches run in parallel |
| Risk | A rule read from the working tree instead of the run's commit | High | `git show <run commit>:<path>` only, with the commits named at the top of `grading-notes.md` |
| Risk | Event streams cleaned before grading, which loses the read-back evidence | Med | Phase 004 keeps them on disk until this phase closes |
| Dependency | Operator decisions on findings | Med | Closing waits for them. An undecided repair stays a finding |
| Dependency | Product Owner public repo | Low | Fetch and check status before committing, no attribution line |
<!-- /ANCHOR:risks -->

---


---

<!-- ANCHOR:nfr -->
## L2: NON-FUNCTIONAL REQUIREMENTS

### Performance
- **NFR-P01**: Five grader batches run in parallel, and the orchestrator adjudicates once over all of them
- **NFR-P02**: `check_report.sh` runs after grading, not in place of it

### Security
- **NFR-S01**: No raw event stream or credential enters a committed file
- **NFR-S02**: Quoted replies carry fixture data only, never real customer data

### Reliability
- **NFR-R01**: Every verdict cites the reply, stream or file that decides it
- **NFR-R02**: Report prose follows the repository voice rules, no em dashes
<!-- /ANCHOR:nfr -->

---

<!-- ANCHOR:edge-cases -->
## L2: EDGE CASES

### Data Boundaries
- A scenario phase 004 recorded as a run defect: SKIP only when a named blocker kept it from running, never PASS
- A single-turn scenario: graded on its one turn
- The bundle `SST-004` and its twin: the Story and every Task in the subfolder graded and reviewed, with the parent link checked in both directions
- A clarification export: reviewed as a clarification, not measured against a ticket template

### Error Scenarios
- `check_report.sh` exits non-zero: its exit code counts checks with findings, so the output is read, not treated as a crash. Exit 64 or 66, or a check that could not run, is a harness problem fixed before grading closes
- A grader returns a verdict without evidence: the orchestrator sends it back rather than writing it
- Two batches read the same rule differently: the orchestrator settles the reading once and regrades the affected rows

### State Transitions
- The operator decides a repair: its tasks are added to `tasks.md`, the repair lands in its source and mirrors and the affected scenarios rerun into a remeasure round
- A peer commit lands on the report folder: re-read before committing
<!-- /ANCHOR:edge-cases -->

---

<!-- ANCHOR:complexity -->
## L2: COMPLEXITY ASSESSMENT

| Dimension | Score | Notes |
|-----------|-------|-------|
| Scope | 16/25 | 46 scenarios, about 86 turns, every export, packet closure |
| Risk | 10/25 | Reporting, and repairs only on decision |
| Research | 14/20 | A new rubric, and twin adjudication read on both sides |
| **Total** | **40/70** | **Level 2** |
<!-- /ANCHOR:complexity -->

---

<!-- ANCHOR:questions -->
## 10. OPEN QUESTIONS

- Does "`check_report.sh` run clean" mean exit 0, or both checks run to completion with their findings folded in? Exit 0 needs every reply lint-clean and every twin in agreement, which grading does not control, so this spec reads it as the second
<!-- /ANCHOR:questions -->

---
