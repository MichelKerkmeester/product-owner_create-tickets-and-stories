---
title: "Goal: Phase 4, run the realistic playbook on Opus 5.5 medium"
description: "The durable directive this phase executes against and the criteria that decide when it is done."
trigger_phrases:
  - "phase 4 goal"
  - "opus run goal"
  - "completion criteria"
  - "goal binding"
importance_tier: "important"
contextType: "planning"
_memory:
  continuity:
    packet_pointer: "013-po-realistic-playbook-opus-rerun/004-opus-run"
    last_updated_at: "2026-09-25T18:40:00Z"
    last_updated_by: "claude-opus-5-5"
    recent_action: "Authored the phase directive"
    next_safe_action: "Wait for the operator's approval of the scenario plan, then run T001"
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
<!-- SPECKIT_TEMPLATE_SOURCE: goal | v2.2 -->
# Goal: Phase 4, run the realistic playbook on Opus 5.5 medium

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> Everything between the frontmatter and the log is the DURABLE SLICE. This is
> a phase child: it binds through the parent goal's binding table and is never
> set as the session objective on its own.

---

<!-- ANCHOR:directive -->
## 1. DURABLE DIRECTIVE

**Objective:** Run all 46 scenarios of the approved Product Owner playbook on claude-opus-5-5 at effort medium, both packagings, and leave checked run output and its collected deliverables committed for grading.

### Decisions

Parent decisions this phase honors. Changing one is an amendment to the parent.

| ID | Decision |
|----|----------|
| D3 | Company context documents are attached files the runner copies into both sandboxes at `context/` |
| D4 | `export/benchmark/` was emptied first, so after the collection it holds only this run |
| D5 | Product Owner only, both packagings |
| D6 | No scenario runs, the smoke run included, before the operator approves the scenario plan |
| D7 | Nothing measured is repaired here. A source or harness defect is reported, and any repair waits for the operator's decision |

### Operator copy

The operator holds the parent directive as the session objective, not this
file. A change here that alters a parent decision or criterion is applied to
the parent `goal.md` first, and the parent's chat slice is resent.
<!-- /ANCHOR:directive -->

---


<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

- [ ] The operator's approval of the scenario plan is on record before the first smoke turn ran
- [ ] The smoke run's `check_run.py --model claude-opus-5-5` output names neither `SID-001` nor `PID-001`, and any widened model set is recorded with its evidence in the run `README.md`
- [ ] `python3 run/check_run.py . --model claude-opus-5-5` exits 0 in the run folder with 46 scenarios read
- [ ] `run-status.json` holds 46 rows, and every row not `ok` is listed as a run defect in the run `README.md`
- [ ] The collector's dry run listed only new files, and `export/benchmark/` holds exactly that many files
- [ ] The run folder and `export/benchmark/` are committed in Barter and in the Product Owner public repo
<!-- /ANCHOR:completion -->

---

<!-- ANCHOR:log -->
## 4. LOG

Everything below is VOLATILE. It is not part of the directive, it is not copied
into the objective, and it is expected to grow. Progress, evidence, deviations
and findings belong here.

### Progress

| Item | State | Evidence |
|------|-------|----------|
| Phase 004 run | Pending | Waits for the operator's approval of the scenario plan at the end of phase 003 |
| Phase 004 | Done | Smoke ok on claude-opus-5-5 alone; full run 46/46 ok first attempt, check_run 0 findings, USD 71.36, 30 min; 98 files collected; Product Owner e9edb95, Barter 7652158c; 12/12 AC met; not pushed |

### Deviations and findings

| Item | Note |
|------|------|
| None yet | |
<!-- /ANCHOR:log -->
