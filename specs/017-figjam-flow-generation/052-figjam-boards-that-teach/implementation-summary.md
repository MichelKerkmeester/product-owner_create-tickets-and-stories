---
title: "Implementation Summary"
description: "Phase 052 lets FigJam boards carry what their source says and scores it, then reruns the gallery on Sonnet 5.5 medium."
trigger_phrases:
  - "figjam boards that teach implementation summary"
importance_tier: "normal"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "017-figjam-flow-generation/052-figjam-boards-that-teach"
    last_updated_at: "2026-10-30T11:00:00Z"
    last_updated_by: "claude-code"
    recent_action: "Gallery rerun graded and published; phase closed"
    next_safe_action: "Take up the glance-order gap in a later phase"
    blockers: []
    key_files: []
    completion_pct: 100
    open_questions: []
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: impl-summary-core | v2.3 -->
# Implementation Summary

<!-- SPECKIT_LEVEL: 2 -->
<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

---

<!-- ANCHOR:metadata -->
## Metadata

| Field | Value |
|-------|-------|
| **Spec Folder** | 052-figjam-boards-that-teach |
| **Completed** | 2026-10-30 |
| **Level** | 2 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:what-built -->
## What Was Built

- **Zone and lane notes.** `%% about:` lines, read and checked in `sk-create-figjam/scripts/compose_board.py` and drawn under the zone title by `sk-create-figjam/assets/compose-board.js`
- **Detail cards at Balanced on four types.** `detail_problems` in `sk-create-figjam/scripts/figjam_checks/flowchart.py`, used by the architecture and state checks too
- **Focus reasons.** `flow_focus_problems` in `sk-create-figjam/scripts/flow_check.py` and `focus_line_problems` in `sk-create-figjam/scripts/figjam_checks/common.py`
- **A compact key.** One band in `sk-create-figjam/assets/compose-board.js`
- **Substance.** `sk-create-figjam/manual-testing-playbook/manual-testing-playbook.md` Section 3 and the ten scenarios
- **Composer fixes from the rerun.** A 16 pixel corner on body cards, small key samples for the shapes FigJam holds at 80 pixels, and room for database and queue card bodies, in `sk-create-figjam/assets/compose-board.js`
- **Gallery rerun.** Ten graded runs in `benchmark/reports/2026-10-25--manual-testing-playbook--figjam-model-comparison/grades/sonnet-medium-052.jsonl`, nine new gallery images and report section 8.17
- **Release.** `sk-create-figjam/changelog/v1.0.17.0.md`, `changelog/v1.0.18.0.md` and the Project mirror, recorded in `SYNC.md`
<!-- /ANCHOR:what-built -->

---

<!-- ANCHOR:how-delivered -->
## How It Was Delivered

The rules went into the checker first, with a passing and a refused fixture each, then the composer, the docs and the shipped models, and the Project copies by hand. The Project composer file was split into two code blocks once the measure showed a graph model would have too little room in one call.
<!-- /ANCHOR:how-delivered -->

---

<!-- ANCHOR:decisions -->
## Key Decisions

| Decision | Why |
|----------|-----|
| Keep each request and add a source excerpt | The counts and Q1 to Q3 still hold, so Substance is the one new measure |
| Substance only where source questions are named | The other scored scenarios test other things and keep their 22 points |
| Rerun the seven card boards after the composer fixes | Michel chose it, so the gallery shows the current design |
| Keep the status lane image from v1.0.16.0 | The graded FJ-049 run drew no lane, and Michel chose to keep the old image |
| Waive the one-row key on narrow boards | ADR-001: FJ-025's three-participant board wraps its key to 144 pixels |
<!-- /ANCHOR:decisions -->

---

<!-- ANCHOR:verification -->
## Verification

| Check | Result |
|-------|--------|
| flow_check self-test | 237 of 237 |
| compose_board self-test | 1305 of 1305 |
| run_gates.sh | 15 of 15 |
| Residency and divergence | Pass |
| Parity | 66 of 66 on commit 4b9c0e665 |
| Gallery rerun | 3 PASS of 10; Substance 2 on nine boards, 1 on FJ-027; Composition fails six |
| validate.sh --strict | RESULT: PASSED for 052, 051 and the parent |
<!-- /ANCHOR:verification -->

---

<!-- ANCHOR:limitations -->
## Known Limitations

1. Six boards still lose Composition: readers take the filled goal, an exit or a second decision before the white steps the `Glance:` line prints first. This is the gap phase 051 found and stays out of this phase's scope
2. FJ-027's column comment, which carried the payment statuses, is dropped by the composer
3. FJ-049's graded run drew no status lane, because the lane stays optional
<!-- /ANCHOR:limitations -->
