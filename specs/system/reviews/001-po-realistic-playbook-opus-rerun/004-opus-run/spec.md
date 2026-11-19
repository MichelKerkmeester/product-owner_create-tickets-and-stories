---
title: "Feature Specification: Phase 4, run the realistic playbook on Opus 5.5 medium"
description: "Once the operator approves the scenario plan, run all 46 scenarios of the rewritten Product Owner playbook on claude-opus-5-5 at effort medium, both packagings, check the run from its files and collect its deliverables into the emptied export/benchmark."
trigger_phrases:
  - "opus 5.5 medium playbook run"
  - "smoke run sid-001 pid-001"
  - "check_run model set"
  - "collect exports bundle subfolder"
importance_tier: "important"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.2 -->
# Feature Specification: Phase 4, run the realistic playbook on Opus 5.5 medium

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
| **Phase** | 4 of 5 |
| **Predecessor** | 003-playbook-rewrite |
| **Successor** | 005-grading-and-report |
| **Handoff Criteria** | `check_run.py --model claude-opus-5-5` exits 0 on 46 scenarios, the deliverables sit in `export/benchmark/` and both repos carry the run in a commit |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:phase-context -->
## Phase Context

This is **Phase 4** of the packet that rewrites the Product Owner manual testing playbook around realistic tickets for three fictional companies and reruns both packagings on claude-opus-5-5 medium.

In every document of this phase, `<run folder>` means `AI Systems/Product Owner/benchmark/reports/<run date>--manual-testing-playbook--claude-opus-5-5-medium/`, the folder phase 003 creates. Phase 003 fixes its date.

**Scope Boundary**: producing run output in `<run folder>` and collecting its deliverables. No grading and no edits to the playbook, fixtures, skill, kernel or knowledge files. The one code change allowed is widening the model set in the run folder's own `run/check_run.py`, and only on smoke evidence.

**Dependencies**:
- The operator's approval of the scenario plan at the end of phase 003 (parent decision D6)
- Phase 003 closed: the rewritten root, 46 scenario files and `<run folder>/run/` holding the runner extended for attachments and the collector that keeps bundle subfolders
- Phases 001 to 003 committed, so the run reads committed skill, kernel, knowledge, playbook and fixture files
- The Claude CLI authenticated for claude-opus-5-5

**Deliverables**:
- In `<run folder>`: `skill/` and `claude project/` scenario folders with replies and `meta.json`, `replies/`, `manifest.json`, `run-status.json`, `run-log.jsonl` and a `README.md` that records how the run was made
- The deliverables in `AI Systems/Product Owner/export/benchmark/`, collected by `<run folder>/run/collect_exports.py`
- A commit of both in the Barter repo and in the Product Owner public repo

**Changelog**:
- When this phase closes, refresh the matching file in ../changelog/ using the parent packet number plus this phase folder name
<!-- /ANCHOR:phase-context -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
The rewritten playbook proves nothing until it has run whole on the model it names. Opus 5.5 has never run this system through the playbook runner, and attachments in `context/` and bundle subfolders are new to the harness. `check_run.py` also compares the model names in each event stream with one exact name (its default, `claude-sonnet-5`, sits at line 54). A helper model or a dated model ID in `modelUsage` would flag every turn, so the model set has to be read from a smoke run before the full run is trusted.

### Purpose
Complete, isolated and attributable run output for all 46 scenarios, read from committed sources on claude-opus-5-5 medium, with the deliverables collected and ready for phase 005 to grade.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- A check that the operator's approval of the scenario plan is on record before anything runs
- Barter and Product Owner HEADs, harness hashes and the CLI version recorded before the smoke run, and the source paths confirmed unchanged after the full run
- A dry run that lists 46 scenarios with their turns and attachments
- A smoke run of `SID-001` and `PID-001` into this phase's `scratch/smoke/`, checked with `check_run.py --model claude-opus-5-5`
- Widening the allowed model set in `<run folder>/run/check_run.py` only when a smoke stream names a second model, with the evidence written into the run `README.md`
- The full run of all 46 scenarios in waves 1 to 6, both sides, at `--jobs 4`, with the exact command in `plan.md`
- `check_run.py` on the full run, then the collector's dry run, then the collection into `export/benchmark/`
- The run record in the run `README.md`: commits, hashes, CLI version, smoke result, model set, cost, wall time, retries and run defects
- Commits in the Barter repo and the Product Owner public repo, and a push on the operator's go-ahead

### Out of Scope
- Grading, verdicts, twin agreement and the realism review - phase 005 owns them
- Edits to the playbook, fixtures, skill, kernel or knowledge files - a run that edits what it measures measures nothing, so a defect found there stops the phase and is reported
- Changes to the runner or collector beyond the phase 003 copies - a harness defect stops the phase and goes back to phase 003
- Prompt Improver and Deal Templates - parent decision D5

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| `<run folder>/**` | Create | Run output, the `README.md` run record and a `.gitignore` if phase 003 left none |
| `<run folder>/run/check_run.py` | Modify, only on smoke evidence | Allowed model set widened for the one name the smoke streams show |
| `AI Systems/Product Owner/export/benchmark/**` | Create | Collected deliverables, skill and Project, bundle subfolders kept |
| `AI Systems/Product Owner/specs/013-po-realistic-playbook-opus-rerun/004-opus-run/scratch/` | Create, local only | Dry run output, smoke run output and the collector's dry-run listing |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | No scenario runs, the smoke run included, before the operator's approval of the scenario plan is on record (parent D6) |
| REQ-002 | The run reads committed sources: Barter and Product Owner HEADs are recorded before the smoke run, and `git status --porcelain` on the skill, kernel, knowledge, playbook and fixture paths prints nothing before the smoke run and after the full run |
| REQ-003 | The smoke run captures both turns of `SID-001` and `PID-001`, and `check_run.py --model claude-opus-5-5` reports no finding that names either ID |
| REQ-004 | The allowed model set changes only when a smoke event stream names a second model, and the run `README.md` names the stream, the event field and the model name that justified it |
| REQ-005 | The full run covers all 46 scenarios on both sides with the command in `plan.md`, and no isolation proof fails, so the runner never exits 2 |
| REQ-006 | `python3 run/check_run.py . --model claude-opus-5-5` exits 0 on `<run folder>`: every scenario whole, every declared turn with a non-empty reply and an event stream naming only the allowed models |
| REQ-007 | A turn that still fails after the runner's three attempts is recorded in `run-status.json` and in the run `README.md` as a run defect with its cause, never as a pass |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement |
|----|-------------|
| REQ-008 | The dry run lists 46 scenarios, 23 per side, with the turn count and the attachments each scenario file declares |
| REQ-009 | The collector's dry run lists only new files, each one a deliverable of this run, and after the collection `export/benchmark/` holds exactly those files with bundle subfolders kept |
| REQ-010 | Every Project extraction line the collector prints is set beside its reply, and the extracted block is the deliverable the reply reported |
| REQ-011 | Event streams, stderr, transcripts, failed attempts and per-scenario `exports/` copies stay out of git through the run folder's `.gitignore`, and stay on disk until phase 005 closes |
| REQ-012 | The run output and `export/benchmark/` are committed in the Barter repo and the Product Owner public repo, with no attribution lines in the public commit. Nothing is pushed before the operator's go-ahead |

> Acceptance criteria for these requirements live in `acceptance-criteria.md`,
> which is the document that decides whether this packet may close.
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: 46 scenarios and every declared turn captured on claude-opus-5-5 medium, both packagings, from committed sources
- **SC-002**: A model check, a completeness check and a collection that a reader can rerun from the commands in `plan.md`
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Risk | Cost and time: 46 scenarios and about 86 turns on Opus, three times the Sonnet run's 28 turns, with attachments adding input | High | The Sonnet run cost $6.05 over 28 turns (its `run-log.jsonl`). The smoke run's cost and wall time per turn, times the dry run's turn count, is recorded before the full run starts |
| Risk | A helper or dated model name in a stream flags every turn, since `check_run.py` wants the exact set | Med | Smoke first and read the names. A dated ID alone is passed as `--model`. A second model widens the set only with the evidence recorded |
| Risk | Flaky turns: the 900 second timeout, rate limits, empty replies | Med | The runner's three attempts with failed attempts kept in `failed-attempts/`. A resume by `--ids` only for a harness or account cause, recorded in the README |
| Risk | Scratch collision: the harness tree is keyed by system and ID under `$TMPDIR/pi-playbook-bench` | Med | Rounds run in sequence, and `pgrep -fl playbook_runner.py` prints nothing before each round starts |
| Risk | A peer session edits the sources in the shared tree during the run | Med | HEADs and `git status` checked before the smoke run and after the full run |
| Dependency | Operator approval (D6) | High | Nothing runs without it |
| Dependency | Claude CLI and account limits | High | Lower `--jobs`, resume the remaining IDs |
| Dependency | Phase 003 runner and collector | High | A harness defect stops the phase and returns to phase 003 |
<!-- /ANCHOR:risks -->

---


---

<!-- ANCHOR:nfr -->
## L2: NON-FUNCTIONAL REQUIREMENTS

### Performance
- **NFR-P01**: At most four Claude sessions at once, and one runner process on Product Owner at a time
- **NFR-P02**: Each round is resumable by scenario ID

### Security
- **NFR-S01**: The CLI runs with no setting sources and no MCP servers, inside the runner's sandbox profile
- **NFR-S02**: No credential or environment value lands in a tracked file

### Reliability
- **NFR-R01**: A scenario is complete only when its last declared turn is captured
- **NFR-R02**: A scenario that failed after its attempts stays in the record as failed to run, never as a verdict
<!-- /ANCHOR:nfr -->

---

<!-- ANCHOR:edge-cases -->
## L2: EDGE CASES

### Data Boundaries
- A single-turn scenario by design, such as `STK-001`, `SBG-001` and `SEP-003` and their twins: complete after one turn
- The bundle scenario `SST-004` and its twin: the skill writes one subfolder of several files, and the collection keeps that subfolder whole
- A scenario whose first turn misses its gate: still run whole, since the playbook states the turns

### Error Scenarios
- CLI authentication lapses mid-run: stop, report, resume by `--ids` once restored
- Isolation proof fails: the runner exits 2 and nothing from that round is used
- Account rate limit: lower `--jobs` and resume the remaining IDs

### State Transitions
- A round interrupted part way: `run-status.json` shows what finished, and the rest resumes by ID after earlier `failed-attempts/` folders are moved aside, because a retry reuses their names
- A peer commit lands on the sources during the run: the affected scenarios rerun once the tree is stable, and the new HEADs replace the recorded ones
<!-- /ANCHOR:edge-cases -->

---

<!-- ANCHOR:complexity -->
## L2: COMPLEXITY ASSESSMENT

| Dimension | Score | Notes |
|-----------|-------|-------|
| Scope | 12/25 | 46 scenarios, one system, two repos |
| Risk | 14/25 | A long unattended run on an external service, with new harness features |
| Research | 5/20 | The harness is known, the model set is not until the smoke run |
| **Total** | **31/70** | **Level 2** |
<!-- /ANCHOR:complexity -->

---

<!-- ANCHOR:questions -->
## 10. OPEN QUESTIONS

- Do the Opus event streams name a helper or dated model? The smoke run answers it before the full run starts
<!-- /ANCHOR:questions -->

---
