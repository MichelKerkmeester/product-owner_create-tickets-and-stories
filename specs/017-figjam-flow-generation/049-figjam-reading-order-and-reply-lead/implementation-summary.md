---
title: "Implementation Summary"
description: "Phase 049 shipped v1.0.15.0 for the v1.0.14.0 rerun causes and ran the last FigJam rerun: both boards scored 22 of 22 and both scenarios failed one signal each."
trigger_phrases:
  - "figjam reading order and reply lead implementation summary"
importance_tier: "normal"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "017-figjam-flow-generation/049-figjam-reading-order-and-reply-lead"
    last_updated_at: "2026-10-28T06:03:22Z"
    last_updated_by: "generate-context"
    recent_action: "Closed phase 049"
    next_safe_action: "None, testing ended"
    blockers: []
    key_files:
      - "benchmark/reports/2026-10-25--manual-testing-playbook--figjam-model-comparison/grades/sonnet-high-049.md"
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
| **Spec Folder** | 049-figjam-reading-order-and-reply-lead |
| **Completed** | 2026-10-28 |
| **Level** | 2 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:what-built -->
## What Was Built

Every cause of README section 8.14 has a change, released as v1.0.15.0 with kernel v1.2.15, and FJ-022 and FJ-023 were rerun on it. This was the last test round.

### Phase 49: FigJam reading order and reply lead

`sk-create-figjam/scripts/figjam_checks/board_geometry.py` reads the accent first and then column by column again, and measures diamond labels by Inter Medium glyph widths. Every Flow delivery opens on the board URL with no sentence before it, and `run/adaptive_compare.py` flags a reply that does not. FJ-023 scripts its turn 1 intake round, a handoff queue between lanes is drawn as a line label, the dials no longer count as assumed rows and the process and user flow examples show an intake round. Each reader note ends on an `Order:` line that repeats the reader's own reading order, and `run/composition_check.py` turns the plan and those lines into the Composition score.

### Files Changed

| File | Action | Purpose |
|------|--------|---------|
| `sk-create-figjam/scripts/` | Modify | The plain reading order and the glyph-width diamond wrap with their self-tests |
| `sk-create-figjam/SKILL.md`, `references/`, `assets/` and `AGENTS.md` | Modify | The reply lead, the queue and dials rules and the examples |
| `sk-create-figjam/manual-testing-playbook/` | Modify | FJ-023's intake turn, the Composition sentence and the Section 5 rules |
| `claude project/`, `SYNC.md` and the release files | Modify, Create | The mirror, kernel v1.2.15 and the v1.0.15.0 release |
| The run folder and `sk-create-figjam/assets/screenshots/` | Create, Modify | The Composition script, the reader brief, the rerun records, README section 8.15 and the process gallery image |
<!-- /ANCHOR:what-built -->

---

<!-- ANCHOR:how-delivered -->
## How It Was Delivered

A fresh Claude Sonnet 5.5 high reviewer checked each 8.14 cause and recommended the fixes. One Sonnet implementer wrote them and one fresh Sonnet reviewer read the whole diff, one at a time as the operator asked. The review found two P1 and three P2 findings, each confirmed and repaired: the Composition script scored an accent read late by every reader 1 instead of 0, the reader brief claimed every type, and three wordings disagreed. The kernel sentence moved one residency row, resynced in the mirror commit, and the flow-mode review pin moved in its own commit. Both outer pushes needed the operator's one-push override because another session held uncommitted edits in a routing hub. The two scenarios ran one after the other in new draft files. The FJ-022 readers first wrote their `Order:` line in flow order against their own reading lists, so each rewrote that line and the reader brief now says what the line repeats.
<!-- /ANCHOR:how-delivered -->

---

<!-- ANCHOR:decisions -->
## Key Decisions

| Decision | Why |
|----------|-----|
| Drop the lifted decision | It fit the minority of FJ-023's six readers and cost more boards than the plain order |
| Keep the rubric's both-readers charge as it is | Charging only parts read early would fit the rubric to one run |
| Leave FJ-022's three-zone signal as written | Changing the scenario after the run would fit the score to it |
| Stop at this rerun | The operator ended testing here, so remaining failures stand as known limitations |
<!-- /ANCHOR:decisions -->

---

<!-- ANCHOR:verification -->
## Verification

| Check | Result |
|-------|--------|
| `python3 sk-create-figjam/scripts/flow_check.py --self-test` on the release tree | 201 of 201 |
| `python3 sk-create-figjam/scripts/compose_board.py --self-test` and `--design-check` | 1251 of 1251, design check exit 0 |
| pytest, the gates, the output format gate and `composition_check.py --self-test` | 18 passed, 15 of 15, format passed across 72 source files, 5 of 5 |
| Sync Loop checks after outer commit a20fc0e9f | parity PASSED 65 of 65, residency PASSED 7, divergence PASSED 208 pairs |
| Rerun, `grades/sonnet-high-049.jsonl` | FJ-022 FAIL at 22, FJ-023 FAIL at 22, Composition 2 on both by the script |
<!-- /ANCHOR:verification -->

---

<!-- ANCHOR:limitations -->
## Known Limitations

1. **SC-003 is not met.** Both boards score 22 of 22, but FJ-022 drew two zones where its scenario fixes three, and the skill makes zones a choice with no count. FJ-023 added a sentence about the write target after its intake round's closing question. The operator ended testing at this rerun, so neither is reopened
2. **The glyph-width label trace was not exercised live.** Neither rerun board printed a `Label:` line, so only the self-tests show it
3. **The `Row:` hint can move an exit away from its decision.** Both FJ-022 readers found Contact support's place odd, though it cost no point
<!-- /ANCHOR:limitations -->
