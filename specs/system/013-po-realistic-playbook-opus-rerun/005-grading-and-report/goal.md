---
title: "Goal: Phase 5, grade the Opus run and write the report"
description: "The durable directive this phase executes against and the criteria that decide when it is done."
trigger_phrases:
  - "phase 5 goal"
  - "grading goal"
  - "completion criteria"
  - "goal binding"
importance_tier: "important"
contextType: "planning"
_memory:
  continuity:
    packet_pointer: "013-po-realistic-playbook-opus-rerun/005-grading-and-report"
    last_updated_at: "2026-09-25T18:40:00Z"
    last_updated_by: "claude-opus-5-5"
    recent_action: "Authored the phase directive"
    next_safe_action: "Wait for phase 004 to close, then run T001"
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
# Goal: Phase 5, grade the Opus run and write the report

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

> Everything between the frontmatter and the log is the DURABLE SLICE. This is
> a phase child: it binds through the parent goal's binding table and is never
> set as the session objective on its own.

---

<!-- ANCHOR:directive -->
## 1. DURABLE DIRECTIVE

**Objective:** Grade every turn of the 46-scenario claude-opus-5-5 medium run against the rewritten playbook at the run's commit, review every collected export for realism, report both and close the packet once the operator has ruled on the findings.

### Decisions

Parent decisions this phase honors. Changing one is an amendment to the parent.

| ID | Decision |
|----|----------|
| D1 | Story exports use `Story-`, graded as the Story artifact word |
| D2 | A Story with its task breakdown is one subfolder holding the Story and its linked Tasks, graded as one bundle |
| D3 | Company facts come from the attached context files, so a deliverable that alters or ignores them fails realism |
| D4 | `export/benchmark/` holds only this run's deliverables |
| D7 | Repairs happen only on the operator's decision, and a kernel review is recorded only after the operator confirms it |

### Operator copy

The operator holds the parent directive as the session objective, not this
file. A change here that alters a parent decision or criterion is applied to
the parent `goal.md` first, and the parent's chat slice is resent.
<!-- /ANCHOR:directive -->

---


<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

- [ ] `results.csv` in the run folder has the header `id,runtime,model,result,turns_run,turns_declared,after_failed_gate,facts_intact,note` and 46 rows, and the README counts match it
- [ ] `check_report.sh` ran on the run folder with both checks executing, and its findings are in `grading-notes.md`
- [ ] `grading-notes.md` has one realism entry per file in `export/benchmark/`
- [ ] Every finding went to the operator through the ask tool, and every repair made has a recorded decision and a graded rerun of its scenarios
- [ ] `validate.sh --recursive` on the packet reports 0 errors and every phase's `acceptance-criteria.md` reads `Closeable: Yes`
- [ ] The report is committed in Barter and the Product Owner public repo and pushed on the operator's go-ahead, and the kernel review is still pending unless the operator confirmed it
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
| Phase 005 grading | Pending | Waits for phase 004 to close with its commits recorded |

### Deviations and findings

| Item | Note |
|------|------|
| None yet | |
<!-- /ANCHOR:log -->
