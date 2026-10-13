---
title: "Implementation Summary: Phase 4, run the realistic playbook on Opus 5.5 medium"
description: "All 46 approved scenarios ran on claude-opus-5-5 medium on the first attempt, check_run clean, 98 deliverables collected. Committed as Product Owner e9edb95 and Barter 7652158c."
trigger_phrases:
  - "implementation summary"
  - "opus run status"
  - "phase 4 complete"
  - "continuation notes"
importance_tier: "normal"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "013-po-realistic-playbook-opus-rerun/004-opus-run"
    last_updated_at: "2026-09-25T20:20:00Z"
    last_updated_by: "claude-opus-5-5"
    recent_action: "Ran, checked, collected and committed the Opus run"
    next_safe_action: "Grade the run in phase 005"
    blockers: []
    key_files:
      - "AI Systems/Product Owner/benchmark/reports/2026-09-25--manual-testing-playbook--claude-opus-5-5-medium/README.md"
      - "AI Systems/Product Owner/export/benchmark/"
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "12f293fe-5421-46a0-b1ea-9fdc15ce0f8e"
      parent_session_id: null
    completion_pct: 100
    open_questions: []
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: impl-summary-core | v2.2 -->
# Implementation Summary

<!-- SPECKIT_LEVEL: 2 -->
<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

---

<!-- ANCHOR:metadata -->
## Metadata

| Field | Value |
|-------|-------|
| **Spec Folder** | 004-opus-run |
| **Status** | Complete |
| **Completed** | 2026-09-25 |
| **Level** | 2 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:what-built -->
## What Was Built

The rewritten playbook has now run for real. All 46 scenarios, 23 skill and 23 Project, ran on claude-opus-5-5 at effort medium against the committed sources the operator approved, and every one finished on its first attempt. The 98 deliverables they wrote sit in `export/benchmark/`, ready for grading.

### Phase 4: opus-run

| Result | Value |
|--------|-------|
| Scenarios | 46 of 46 `ok`, 0 retried, 86 of 86 turns |
| Models | `claude-opus-5-5` alone in all 86 streams |
| `check_run.py` | exit 0, 0 findings |
| Time and cost | About 30 minutes, USD 71.36 |
| Collection | 98 files, 41 skill and 57 Project, bundles kept as folders |

### Files Changed

| File | Action | Purpose |
|------|--------|---------|
| `AI Systems/Product Owner/benchmark/reports/2026-09-25--manual-testing-playbook--claude-opus-5-5-medium/` | Run output added | `manifest.json`, `run-status.json`, `replies/`, per-scenario `meta.json` and `turn-<n>.md`, the run record `README.md` |
| `AI Systems/Product Owner/export/benchmark/` | Created | The 98 collected deliverables |
<!-- /ANCHOR:what-built -->

---

<!-- ANCHOR:how-delivered -->
## How It Was Delivered

The operator approved the scenario plan on 2026-09-25 at 19:31 UTC. The smoke run came first, then the full run, the check, the collection and one commit in each repository.

### Smoke run, 2026-09-25

`SID-001` and `PID-001` ran into `scratch/smoke/` with `--jobs 2`, runner exit 0, both scenarios `ok` on their first attempt with 2 of 2 turns. `check_run.py --model claude-opus-5-5` named neither ID, and its other 44 findings are the scenarios the smoke never ran, as the plan expects.

| Scenario | Turn | Status | Models in the stream | Cost (USD) | Wall (s) |
|----------|------|--------|----------------------|-----------:|---------:|
| PID-001 | 1 | ok | claude-opus-5-5 | 0.38 | 33.69 |
| SID-001 | 1 | ok | claude-opus-5-5 | 0.59 | 36.09 |
| SID-001 | 2 | ok | claude-opus-5-5 | 0.74 | 28.98 |
| PID-001 | 2 | ok | claude-opus-5-5 | 0.56 | 46.52 |

Every stream names `claude-opus-5-5` alone, so the allowed model set stays as it is and `check_run.py` keeps `--model claude-opus-5-5`.

### Estimate for the full run

Mean per smoke turn: USD 0.57 and 36.3 s. Times 86 turns: about USD 49 and 52 minutes of turn time, about 13 minutes of wall time at `--jobs 4`. The handover is one of the smallest scenarios, so both figures are a floor: turns that read three attachments and write a bundle or a long task will run longer and cost more.

### Full run

Started in the background with `--jobs 4`. Events ran from 19:35:44 to 20:06:05 UTC, and the runner exited 0. The run cost USD 71.36, 46% above the estimate, and took about 30 minutes rather than 13: the bundle, parent task and long task turns ran up to 352 s each.

### Collection and commit

The collector's dry run listed 98 new files into an empty `export/benchmark/`, and the collection wrote exactly those. Every skill file is byte-identical to the runtime's own export, and every Project file's text is found verbatim in its reply, one row each in the run README. Committed as Product Owner e9edb95 and Barter 7652158c, 319 paths each, with no attribution line. Nothing is pushed.
<!-- /ANCHOR:how-delivered -->

---

<!-- ANCHOR:decisions -->
## Key Decisions

| Decision | Why |
|----------|-----|
| The smoke run writes to this phase's `scratch/smoke/`, not the run folder | The full run then holds one clean pass of all 46 scenarios, and the smoke's extra turns stay out of `run-log.jsonl` and `run-status.json` |
| A dated model ID alone changes only the `--model` value `check_run.py` gets | The exact-set check stays as strict as before, and no code changes without a second model to justify it |
<!-- /ANCHOR:decisions -->

---

<!-- ANCHOR:verification -->
## Verification

Acceptance: 12 of 12 criteria met, see `acceptance-criteria.md`. Checklist: every item in `tasks.md` checked with evidence.

| Check | Result |
|-------|--------|
| `python3 run/check_run.py . --model claude-opus-5-5` in the run folder | exit 0, `46 scenarios, 86 declared turns, 86 event streams read, 0 finding(s)` |
| `run-status.json` | 46 rows, 46 ok, 0 retried |
| `python3 run/collect_exports.py . ../../../export/benchmark --dry-run` | 98 lines, every one a deliverable of one of the 46 IDs |
| Collection | 98 files, 41 byte-identical skill files, 57 Project blocks found verbatim in their replies |
| Sources | Product Owner 3023c5e and Barter c15c05e9 before the smoke and after the run, status empty |
| Staged files | No stream, stderr, transcript, failed attempt, `exports/` copy or progress file |
<!-- /ANCHOR:verification -->

---

<!-- ANCHOR:limitations -->
## Known Limitations

1. **Not graded yet.** A clean run says every scenario finished, not that it passed. Phase 005 grades each turn against the root.
2. **Both `PST-004` turns share one folder.** Each turn rendered a bundle under the same folder name, so the collected Project folder holds both turns' blocks, the later ones marked `(turn 2)` where a name repeats.
3. **Not pushed.** Both commits wait for the operator's go-ahead.
<!-- /ANCHOR:limitations -->

---
