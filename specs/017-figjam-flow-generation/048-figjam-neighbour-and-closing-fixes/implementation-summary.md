---
title: "Implementation Summary"
description: "v1.0.14.0 fixed the v1.0.13.0 rerun causes: the accent row decision in the glance order, one closing question per intake round, the FJ-017 Finding, the diamond trace, the dials at the playback, the Composition levels and the turn 1 intake. The rerun passed 2 of 4."
trigger_phrases:
  - "figjam neighbour and closing fixes implementation summary"
importance_tier: "normal"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "017-figjam-flow-generation/048-figjam-neighbour-and-closing-fixes"
    last_updated_at: "2026-10-28T05:06:07Z"
    last_updated_by: "generate-context"
    recent_action: "Closed phase 048"
    next_safe_action: "Continue in phase 049"
    blockers: []
    key_files:
      - "benchmark/reports/2026-10-25--manual-testing-playbook--figjam-model-comparison/grades/sonnet-high-048.md"
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
| **Spec Folder** | 048-figjam-neighbour-and-closing-fixes |
| **Completed** | 2026-10-28 |
| **Level** | 2 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:what-built -->
## What Was Built

Every script, skill, playbook and mirror cause of README section 8.13 has a change, released as v1.0.14.0 with kernel v1.2.14, and the four scenarios were rerun on it.

### Phase 48: FigJam neighbour and closing fixes

The `Glance:` line in `sk-create-figjam/scripts/figjam_checks/board_geometry.py` puts a decision joined to the accent on its own row, with no node between, right after the accent, and names a second accent-fill node once. Every intake round ends on one closing question, the playback names the three dials and FJ-017 asks for a `Finding:` line only for a sticky that left its named side. `scripts/compose-trace.mjs` measures whole-pixel lines and the check reads a diamond's text box at half its width less 8 px, so the user flow example's labels were reworded in the returns doc's words. The composer keeps edge labels 4 px clear of a zone title. The playbook's Composition levels charge only the part read early in a swapped pair, and turn 1 is an intake round when the reader is unsettled.

### Files Changed

| File | Action | Purpose |
|------|--------|---------|
| `sk-create-figjam/scripts/` and `assets/compose-board.js` | Modify | The reading order, the diamond trace and the label clearance with their self-tests |
| `sk-create-figjam/references/` (flow-mode, quality-rubric, hybrid-workflow) and `assets/` (flow templates, the user flow and process examples) | Modify | The rules and the regenerated models |
| `sk-create-figjam/manual-testing-playbook/` | Modify | The Composition levels, the Section 5 rules, FJ-017 and FJ-022 |
| `claude project/` (the kernel, seven Knowledge files and the README), `SYNC.md`, the release files | Modify, Create | The mirror and the v1.0.14.0 release |
| The run folder and `sk-create-figjam/assets/screenshots/` | Create, Modify | The 048 rerun records, README section 8.14 and the process gallery image |
<!-- /ANCHOR:what-built -->

---

<!-- ANCHOR:how-delivered -->
## How It Was Delivered

A fresh Opus reviewer checked each 8.13 cause against the files, the run streams and the renders and recommended the fixes, and an Opus implementer wrote them with self-tests. A second fresh Opus reviewer read the whole diff and found 1 P1 and 9 P2, each confirmed and repaired: a second accent-fill node named twice, the top-down reading of the accent's row, FJ-022's missing intake turn, the playback sentence without the dials, the Composition level against the revision exception and four figures and wordings. The kernel sentence moved one residency row, resynced in the mirror commit, and the flow-mode review pin moved in its own commit. The first rerun launch stopped on the account's weekly limit and was relaunched after the reset. A completeness check corrected three grade scores against the reader notes and the style guide before the records were committed.
<!-- /ANCHOR:how-delivered -->

---

<!-- ANCHOR:decisions -->
## Key Decisions

| Decision | Why |
|----------|-----|
| Lift only a decision on the accent's row with no node between | Of four rules tested against the 047 boards, only this one predicted every reader order then, though the 048 readers did not follow it |
| Add a closing question rather than reorder the template | A question after its own recommendation reads backwards |
| Keep the composer's 4 px label clearance | The whole-pixel line height left one planted label 1 px into a zone title, and the composer self-test must pass |
| Replace the process gallery image at a tied 21 | The new board keeps every route in its lane and accents a step rather than the goal |
<!-- /ANCHOR:decisions -->

---

<!-- ANCHOR:verification -->
## Verification

| Check | Result |
|-------|--------|
| `python3 sk-create-figjam/scripts/flow_check.py --self-test` on the release tree | 199 of 199, exit 0 |
| `python3 sk-create-figjam/scripts/compose_board.py --self-test` and `--design-check` | 1251 of 1251, exit 0 |
| pytest, the gates and the output format gate | 18 passed, 15 of 15, format passed across 72 source files |
| Sync Loop checks after outer commit 8bc6d1014 | parity PASSED 65 of 65, residency PASSED 7, divergence PASSED 208 pairs, every `check_criteria.sh` row ok |
| Rerun, `grades/sonnet-high-048.jsonl` | FJ-017 PASS, FJ-036 PASS at 21, FJ-022 FAIL at 20, FJ-023 FAIL at 21 |
<!-- /ANCHOR:verification -->

---

<!-- ANCHOR:limitations -->
## Known Limitations

1. **SC-003 is not met.** The rerun passed 2 of 4. FJ-022 opened its delivery reply on a sentence above the URL and both its readers read the exit last, FJ-023 skipped its turn 1 intake round, drew a queue store its scenario does not count and lost Composition to its entry read before the lifted decision, and the label trace passed an accented diamond label FigJam wrapped. Run README section 8.14 records each cause and phase 049 takes them all
<!-- /ANCHOR:limitations -->
