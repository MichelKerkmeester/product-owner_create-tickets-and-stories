---
title: "Implementation Summary"
description: "v1.0.13.0 fixed every v1.0.12.0 rerun cause: the check prints the drawn reading order and a bending row, stickies keep their side and alignment within reach, the gate shows the checked model line for line and labels have a way past a wrap. The rerun passed 1 of 4."
trigger_phrases:
  - "figjam glance and row fixes implementation summary"
importance_tier: "normal"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "017-figjam-flow-generation/047-figjam-glance-and-row-fixes"
    last_updated_at: "2026-10-28T00:53:23Z"
    last_updated_by: "generate-context"
    recent_action: "Closed phase after rerun"
    next_safe_action: "Continue in phase 048"
    blockers: []
    key_files:
      - "sk-create-figjam/scripts/flow_check.py"
      - "sk-create-figjam/scripts/figjam_checks/board_geometry.py"
    session_dedup:
      fingerprint: "sha256:e1446d858bf5e8974d9de21b09b911685bb36d54775e6f1d81cfadf396f41fcd"
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
| **Spec Folder** | 047-figjam-glance-and-row-fixes |
| **Completed** | 2026-10-28 |
| **Level** | 2 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:what-built -->
## What Was Built

Every script, skill, playbook and harness cause of README section 8.12 has a change, released as v1.0.13.0 with kernel v1.2.13, and the four failed scenarios were rerun on it.

### Phase 47: FigJam glance and row fixes

On a user flow or a process `flow_check.py` now prints a `Glance:` line, the order a reader meets the nodes on the board it composes in memory: the accent first, then column by column along the flow and down each column, with the goal marked. The rubric plans the second glance as the nodes up to and including the goal in that order and the last glance as the rest, or the key and the source line when the goal comes last, and the playbook scores Composition against it. A non-failing `Row:` line names a main-row line that bends off the row round a node and, on a zoned flow, the move into the next step's zone, with the composer's layout unchanged. Each `Sides:` line names its alignment and no square past one sticky width is offered. The gate shows the checked model verbatim, every `%%` and `style` line, in every source, example and the kernel. A word only one measure strands prints `may leave`, step 5 allows a reworded or longer label or naming at the gate, the Legibility row covers several wraps, the user flow and process examples were relabelled and a self-test holds each example's Check block to the real check output. Intake round One asks the three dials, an extra intake round ends on its question and parts read in one step read as a set. The harness redacts only each scenario's own output and its run-log rows and reads a counted read-back or a `use_figma` call as a delivery.

Causes with no skill change: FJ-017's hard-coded Cancelled sticky and the three gate sketches that dropped lines were model slips against rules D3 and D4 now make explicit, and FJ-023's labels that cleared the check in the runbook's words were a model slip.

### Files Changed

| File | Action | Purpose |
|------|--------|---------|
| `sk-create-figjam/scripts/flow_check.py`, `scripts/figjam_checks/board_geometry.py` | Modify | The glance, row, sides and label lines and the Check block self-test |
| `sk-create-figjam/references/` (flow-mode, quality-rubric, hybrid-workflow) | Modify | The rules |
| `sk-create-figjam/assets/flow-templates.md` and the seven `assets/examples/` | Modify | Round One dials, the Sketch line and the relabelled models |
| `sk-create-figjam/manual-testing-playbook/manual-testing-playbook.md` | Modify | The Composition and Legibility rows and the Section 5 stop rules |
| `claude project/Custom Instructions.md` | Modify | The verbatim sketch in the Flow write bullet |
| `benchmark/reports/.../run/` (`run_full.sh`, `adaptive_compare.py`, three `redact_run.py` copies) | Modify | The harness, and key discovery for a file a run creates for itself |
| `claude project/` (twelve Knowledge files, the composer mirror), `SYNC.md`, the release files | Modify, Create | The mirror and the v1.0.13.0 release |
| The run folder and `sk-create-figjam/assets/screenshots/` | Create, Modify | The 047 rerun records, README section 8.13 and the user flow gallery image |
<!-- /ANCHOR:what-built -->

---

<!-- ANCHOR:how-delivered -->
## How It Was Delivered

The check reads both new lines off the board it already composes in memory for the label trace, so nothing in the composer moved. Each check change came with self-test cases: a zoned flow whose off-row exit sits in its own column and the same flow with that exit moved into the next zone, a sticky case with an end dot inside and past one sticky width and a lone word only the narrow measure strands. The two flow examples were relabelled until their checks printed no `Label:` line, and a new self-test row compares every example's Check block with the real output. A fresh Opus reviewer read the whole diff and found 1 P1 and 11 P2, each confirmed and repaired: the P1 read a skip edge as a bent row, mended by skipping a line that passes a node on the row or reaches the edge's target. The kernel edit moved a residency row, resynced and committed before the Sync Loop checks ran, and the flow-mode review pin moved in its own commit. The rerun used four parallel lanes, and a file FJ-017 created for itself leaked its key until `redact_run.py` learned to find keys in the output.
<!-- /ANCHOR:how-delivered -->

---

<!-- ANCHOR:decisions -->
## Key Decisions

| Decision | Why |
|----------|-----|
| Plan the glance from the drawn order | Readers met off-row nodes where the composer drew them, early, while the plan put them last |
| Advise on a bending row, never fail | The board still reads, and the model is where a bend is mended |
| Show the checked model verbatim | Three gates showed a sketch that was not the model the check read |
| Keep FJ-022's PASS | It ran the check before the playback under Standard energy, but the scenario's signals and PASS line held when it was graded, so the breach is a finding and the playbook rule comes in phase 048 |
<!-- /ANCHOR:decisions -->

---

<!-- ANCHOR:verification -->
## Verification

| Check | Result |
|-------|--------|
| `python3 sk-create-figjam/scripts/flow_check.py --self-test` on the committed tree | 194 of 194, exit 0 |
| `python3 sk-create-figjam/scripts/compose_board.py --self-test` and `--design-check` on the committed tree | 1250 of 1250, exit 0 |
| `flow_check.py` on the relabelled user flow and process examples | PASSED with a `Glance:` line and no `Label:` line |
| The three `redact_run.py` copies | One hash |
| pytest, the gates and the output format gate | 18 passed, 15 of 15 on the release tree, format passed across 72 source files |
| Sync Loop checks after outer commit 3fe1a442e | parity PASSED 65 of 65, residency PASSED 7, divergence PASSED 208 pairs, every `check_criteria.sh` row ok |
| Rerun, `grades/sonnet-high-047.jsonl` | FJ-022 PASS at 21, FJ-023 FAIL at 21, FJ-036 FAIL at 22, FJ-017 FAIL with no scorecard |
<!-- /ANCHOR:verification -->

---

<!-- ANCHOR:limitations -->
## Known Limitations

1. **SC-003 is not met.** The rerun passed 1 of 4. FJ-017 named no sticky on a `Finding:` line where its scenario asked for one the skill does not, FJ-036's intake round ended on a `Why:` line after its question, FJ-023's readers met the accent's lane neighbour before the entry the `Glance:` line put second and the label trace passed a diamond label FigJam wrapped. Run README section 8.13 records each cause and phase 048 takes them all
<!-- /ANCHOR:limitations -->
