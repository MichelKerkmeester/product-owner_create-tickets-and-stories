---
title: "Implementation Summary"
description: "The 35 findings of the v1.0.6.0 rerun shipped as sk-create-figjam v1.0.7.0 with kernel v1.2.9, and the rerun of every scenario that did not pass ended at 2 PASS, 14 FAIL and 2 NOT RUN."
trigger_phrases:
  - "figjam rerun findings implementation summary"
importance_tier: "normal"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "017-figjam-flow-generation/041-figjam-rerun-findings"
    last_updated_at: "2026-10-27T08:10:00Z"
    last_updated_by: "claude-code"
    recent_action: "Graded the v1.0.7.0 rerun, folded the critic's record corrections, swapped the process gallery image and wrote README section 8.7"
    next_safe_action: "Open phase 042 for the glance-plan, Left out and sticky gaps the rerun still shows, then rerun the 14 failures"
    blockers: []
    key_files:
      - "spec.md"
      - "acceptance-criteria.md"
      - "../../../benchmark/reports/2026-10-25--manual-testing-playbook--figjam-model-comparison/grades/sonnet-high-041.md"
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "348b59cb-58a2-4b49-8147-c40143312bc1"
      parent_session_id: null
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
| **Spec Folder** | 041-figjam-rerun-findings |
| **Completed** | 2026-10-27 |
| **Level** | 2 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:what-built -->
## What Was Built

The 35 findings of the v1.0.6.0 rerun shipped as `sk-create-figjam` v1.0.7.0, `sk-product-owner` v1.2.4.0 and kernel v1.2.9, with the Claude Project mirror in the same commit. The driver now gives every pinned run one destination and every board scenario a fresh file, and the 040 records carry the critic's corrections. Claude Sonnet 5.5 high then ran every scenario that had not passed. The rerun passes 2 of the 16 it ran, short of what the phase set out to prove.

### Phase 41: FigJam rerun findings

Each finding and what closed it:

- **F1.** `flow-mode.md` and Templates - Flow Mode define a request for one board by its words, so a destination no longer cuts a board.
- **F2.** No change. Under that definition FJ-029's two boards stand.
- **F3.** The playbook root gained the Composition and Signal carve-outs for a named group and a revision's second glance.
- **F4.** `types/state.md` plans the composite first and the focus state by its group, mirrored.
- **F5.** The type question carries one recommended scope.
- **F6.** A missing route runs the playback and the gate first, in `flow-mode.md` and the kernel.
- **F7.** `hybrid-workflow.md` sets the single sticky order.
- **F8.** `quality-rubric.md` plans the outlined kinds right after the accent.
- **F9.** Leadership maps to the Executive and Simplified dials and the gate names all three.
- **F10.** `types/process.md` names the log writer.
- **F11.** The driver pins `NEW_FILE_PLAN` and sends the plan line only when a run creates a file.
- **F12.** Fidelity is scored against the run's own model.
- **F13.** Every board scenario gets a fresh file and `file_start_sections`.
- **F14.** A named file that already holds content gets one more read before the gate.
- **F15.** `flow_check.py` and the type references refuse a self-loop. The split-message half needed no change after F1.
- **F16.** Gantt arrows arrive 24 px apart within 72 px of a bar's left end, with checks.
- **F17.** `state.py` warns on a guard named by id and `state.md` says so.
- **F18.** Interactive-mode Open items carry no board fact.
- **F19.** FJ-020 gained its second turn and Hygiene allows the paired re-save.
- **F20.** The mirror shipped in the release commit.
- **F21.** The driver scripts the operator steps. FJ-044 and FJ-045 ran, FJ-018 and FJ-035 did not.
- **F22.** No change. Checker files and reader notes carry keys while in scratch, and the graded lines cite the run's own files.
- **F23 and F24.** No change. Both were model slips.
- **C1.** FJ-029 and FJ-032 score Reply 1 in the 040 records.
- **C2.** Eight board records gained the scorecard signal.
- **C3.** The operator-only scenarios read NOT RUN and the readers saw greyscale renders.
- **C4.** One destination per pinned run.
- **C5.** The FJ-019 cite is fixed.
- **C6.** No change. The finding rests on FJ-031 alone and the F14 read stays.
- **C7.** Graph arrivals sit 24 px apart through `shared_arrivals`.
- **C8.** The FJ-017 turn-shift ruling is corrected.
- **C9.** No change. The citation errors sat only in the synthesized findings.
- **C10.** FJ-035 is split into its nine signals.
- **C11.** The mirror carries the No route paragraph and the read-visually rule.

The record corrections were applied by script. A review of the diff also repaired a stray blank line, the composer's missing-after case and the devin runner pin.

### Files Changed

| File | Action | Purpose |
|------|--------|---------|
| `sk-create-figjam/references/`, `assets/`, `scripts/`, `manual-testing-playbook/` | Modified | The skill, composer, checks and playbook rows for F1 to F19 and C7 |
| `sk-product-owner/references/interactive-mode.md` | Modified | F18 |
| `claude project/` and `Custom Instructions.md` | Modified | The mirror and kernel v1.2.9 |
| `SKILL.md`, `README.md`, version files, changelogs, `SYNC.md` | Modified | The v1.0.7.0 and v1.2.4.0 release and the SYNC notes |
| `benchmark/.../run/adaptive_compare.py` | Modified | F11, F13 and F21 |
| `benchmark/.../grades/sonnet-high-rerun.*`, `sonnet-high-gallery.jsonl` | Modified | The 040 record corrections |
| `benchmark/.../skill/sonnet-high-041/`, `renders/`, `grades/sonnet-high-041*` | Created | The rerun, its renders and its grades |
| `benchmark/.../README.md` | Modified | Section 8.7 |
| `sk-create-figjam/assets/screenshots/process-board.png` and both gallery captions | Modified | The FJ-023 board replaces the FJ-034 one |
<!-- /ANCHOR:what-built -->

---

<!-- ANCHOR:how-delivered -->
## How It Was Delivered

DeepSeek V4.1 Flash max made the prose edits, Opus agents planned and verified each one, and the release landed as one commit with its mirror. Each board scenario ran in its own fresh file in drafts of the operator's team plan. One Opus grader scored all 18 scenarios. Skeptics and adjudicators then ruled on the disputes, and a completeness critic checked the folded records. Its record corrections are applied: the evidence files now sit in the run folder, FJ-033 drops to 21 and two loss causes are restated. Board URLs, file keys and plan names are redacted from every committed file.
<!-- /ANCHOR:how-delivered -->

---

<!-- ANCHOR:decisions -->
## Key Decisions

| Decision | Why |
|----------|-----|
| Define a request for one board by its words | A destination such as on a new board appears in every playbook prompt, so treating it as a request cut boards no one asked to cut |
| Record the low pass count rather than regrade it | The grades follow the playbook as written. The gaps they expose go to phase 042 |
| Keep the best model-run board per type in the gallery | The operator's choice. Only the process image changed, because FJ-023 shows more of the type at the same score |
<!-- /ANCHOR:decisions -->

---

<!-- ANCHOR:verification -->
## Verification

| Check | Result |
|-------|--------|
| `compose_board.py --self-test` | 1244 of 1244, exit 0 |
| `compose_board.py --design-check` | 0 design warnings, exit 0 |
| `flow_check.py --self-test` | 167 of 167, exit 0 |
| `pytest -q scripts/tests` | 18 passed, exit 0 |
| `benchmark/gates/run_gates.sh` | all 15 gates pass, exit 0 |
| `validate-output-format.cjs --system product-owner` | passed across 72 source files, exit 0 |
| `validate_parity.py product-owner` | PASSED 65/65 declared pairs |
| `residency_check.py --all` | PASSED 7 systems |
| Rerun grades | 18 lines in `grades/sonnet-high-041.jsonl`, every evidence path resolving in the run folder |
| Leak scan of the added lines | 0 hits |
<!-- /ANCHOR:verification -->

---

<!-- ANCHOR:limitations -->
## Known Limitations

1. **SC-001 is unmet.** The rerun passes 2 of the 16 scenarios it ran, against the 14 of 27 the v1.0.6.0 rerun passed. Of the 14 run on both versions, only FJ-020 moved to PASS. Counted over every scenario run on either version, 16 of 29 pass.
2. **Composition still fails most boards.** It is below full marks on 9 of the 14 failures. The plans copy shipped examples that leave the goal, gateway or entry out of their glance lines, and the state rule plans the composite first where readers read the saturated first state first.
3. **Gaps left for phase 042.** No `Left out:` line on a split or a gate. The single sticky has no free side next to an end-dot connector. The router lets two runs lie 24 px apart. The rubric lets FJ-045's accent sit on a decision. FJ-017 is scored on a scorecard its scenario does not hold.
4. **FJ-018 and FJ-035 were not run.** They need Figma Desktop and the figma-ds-cli daemon.
<!-- /ANCHOR:limitations -->
