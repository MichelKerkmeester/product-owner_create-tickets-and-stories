---
title: "Acceptance Criteria: Phase 4, run the realistic playbook on Opus 5.5 medium"
description: "The criteria phase 4 must satisfy before it may close, each one met, waived by a decision record, or superseded by one."
trigger_phrases:
  - "opus run acceptance"
  - "phase 4 closure"
  - "check_run exit 0"
  - "approval before run"
importance_tier: "important"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "013-po-realistic-playbook-opus-rerun/004-opus-run"
    last_updated_at: "2026-09-25T18:40:00Z"
    last_updated_by: "claude-opus-5-5"
    recent_action: "Wrote the acceptance criteria, all Unmet"
    next_safe_action: "Meet the criteria once the operator approves the scenario plan"
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
<!-- SPECKIT_TEMPLATE_SOURCE: acceptance-criteria | v2.2 -->
# Acceptance Criteria: Phase 4, run the realistic playbook on Opus 5.5 medium

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> This document decides whether the packet may close. A packet is closeable when
> every row below is `Met`, `Waived` or `Superseded`. A `Waived` or `Superseded`
> row MUST name an ADR that exists in `decision-record.md`.

---

<!-- ANCHOR:metadata -->
## 1. METADATA

**Packet:** 013-po-realistic-playbook-opus-rerun/004-opus-run
**Level:** 2
**Status:** Complete
**Date:** 2026-09-25
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:criteria -->
## 2. CRITERIA

One row per criterion. `AC-ID` is stable once written: supersede a criterion, never renumber it.

| AC-ID | REQ | Given / When / Then | Verification | Status | Waiver |
|-------|-----|---------------------|--------------|--------|--------|
| AC-001 | REQ-001 | Given phase 003's approval gate, When phase 004 starts, Then the operator's approval of the scenario plan is on record before `SID-001` or `PID-001` runs | The approval quoted with its date in the phase 003 record and the parent `goal.md` log, earlier than `scratch/smoke/manifest.json` | Met | - |
| AC-002 | REQ-002 | Given the sources the run reads, When the smoke run starts and the full run ends, Then Barter and Product Owner HEADs are recorded and `git status --porcelain` on the skill, kernel, knowledge, playbook and fixture paths prints nothing at both points | Both HEAD pairs and both empty status outputs in the run `README.md` | Met | - |
| AC-003 | REQ-003 | Given the smoke run of `SID-001` and `PID-001`, When `check_run.py --model claude-opus-5-5` reads it, Then both scenarios have every turn and no finding names either ID | `check_run.py` output piped to `grep -E '^[SP]ID-001:'` prints nothing, and the smoke `run-log.jsonl` shows four `ok` turns | Met | - |
| AC-004 | REQ-004 | Given the smoke event streams, When a second model name appears in a system event, an assistant message or `modelUsage`, Then the allowed set admits that name only and the run `README.md` names the stream, the field and the name, and when none appears `check_run.py` stays unchanged | `git diff` of `run/check_run.py` against its phase 003 commit, empty or matching the README entry | Met | - |
| AC-005 | REQ-005 | Given the approved playbook, When the full run command in `plan.md` runs, Then all 46 scenarios run on both sides and the runner never exits 2 | `run-progress.txt` ends in `runner exit 0` or `runner exit 1`, and `run-status.json` holds 46 rows | Met | - |
| AC-006 | REQ-006 | Given the finished run folder, When `python3 run/check_run.py . --model claude-opus-5-5` runs, Then it exits 0 | Its summary line: 46 scenarios, an event stream read for every declared turn, 0 findings | Met | - |
| AC-007 | REQ-007 | Given a turn that fails after the runner's three attempts, When the run is recorded, Then `run-status.json` marks its scenario failed and the run `README.md` lists it as a run defect with its cause, never as a pass | The README run defects list and `failed-attempts/`, or zero defects when all 46 rows read `ok` | Met | - |
| AC-008 | REQ-008 | Given the rewritten playbook, When the dry run parses it, Then it lists 46 scenarios, 23 per side, with the turns and attachments each scenario file declares | `scratch/dry-run.json` counts set beside the approved catalog | Met | - |
| AC-009 | REQ-009 | Given the empty `export/benchmark/`, When the collector's dry run and then the collection run, Then the dry run lists only new files of this run and the folder afterwards holds exactly those files, bundle subfolders kept | `find export/benchmark -type f` counts 0 before and the dry run's line count after | Met | - |
| AC-010 | REQ-010 | Given each Project extraction line the collector prints, When it is set beside its reply, Then the extracted block is the deliverable the reply reported | One review note per `project` line in the run `README.md` | Met | - |
| AC-011 | REQ-011 | Given the run folder, When `git status --porcelain --untracked-files=all` lists it, Then no event stream, stderr, transcript, failed attempt or `exports/` copy is offered, and every stream is still on disk for phase 005 | The status output, and `find . -name 'events-turn-*.jsonl'` counting one stream per declared turn | Met | - |
| AC-012 | REQ-012 | Given the checked run and collection, When they are committed, Then Barter and the Product Owner public repo carry them, the public commit has no attribution line and nothing is pushed before the operator's go-ahead | Commit hashes in both repos, and `git log -1 --format=%B` in the public repo without a `Co-Authored-By` line | Met | - |

### Status values

| Value | Meaning |
|-------|---------|
| `Met` | Verified. The Verification cell names evidence that was actually observed. |
| `Unmet` | Not yet satisfied. Blocks closure. |
| `Waived` | Deliberately not pursued. Requires an ADR in the Waiver cell. |
| `Superseded` | Replaced by a different criterion or decision. Requires an ADR in the Waiver cell. |

### Waiver cell

Write `-` when the row is `Met` or `Unmet`. Write `ADR-NNN` when the row is
`Waived` or `Superseded`, naming a decision record that exists in
`decision-record.md`. A waiver naming an ADR that is not there fails validation:
the point of a waiver is that someone recorded the reasoning, so an unbacked
waiver is treated as an unmet criterion rather than as a pass.
<!-- /ANCHOR:criteria -->

---

<!-- ANCHOR:closure -->
## 3. CLOSURE STATEMENT

**Closeable:** Yes

All 12 criteria are met. The operator approved the scenario plan at 19:31 UTC, the smoke and the full run followed on Product Owner 3023c5e and Barter c15c05e9, all 46 scenarios finished on their first attempt with `check_run.py` clean, and the 98 deliverables were collected and committed as Product Owner e9edb95 and Barter 7652158c. Nothing is pushed.
<!-- /ANCHOR:closure -->
