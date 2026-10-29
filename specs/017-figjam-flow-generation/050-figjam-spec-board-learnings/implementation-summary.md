---
title: "Implementation Summary"
description: "Phase 050 built five sk-create-figjam changes from a hand-built spec board, released as v1.0.16.0 with the Project in step."
trigger_phrases:
  - "figjam spec board learnings implementation summary"
importance_tier: "normal"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "017-figjam-flow-generation/050-figjam-spec-board-learnings"
    last_updated_at: "2026-10-29T19:30:00Z"
    last_updated_by: "claude-code"
    recent_action: "Committed the release and moved the flow-mode review record; every check passes"
    next_safe_action: "Push both repositories on the operator's go-ahead"
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
| **Spec Folder** | 050-figjam-spec-board-learnings |
| **Completed** | 2026-10-29 |
| **Level** | 2 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:what-built -->
## What Was Built

- **Status lane.** `%% status: <lane id>` names one lane of a laned process as a record's statuses. The check holds it to one `-->` chain declared first and to dotted `-.->` moves from steps, and reads the path, the ways out and the goal on the work alone. The composer draws each status as a white chevron and each move as a dotted gray line the key names `Moves the status`
- **Detail cards.** `%% level: faithful` and `%% detail:` lines give a step a body of at most 10 lines of 44 characters. The label stays one Bold line, a 10 pixel spacer follows and the body uses the new `body` token, 16 at 145% line height. A laned process with detail cards reads at 18 nodes and 24 connectors
- **Fresh read-back.** A view after any later write is taken with `node.screenshot()` inside `use_figma`, and a stale view is named and retaken
- **Subtitle rule.** Every subtitle names where the flow starts and ends, and the shipped examples follow it
- **Worked example.** `assets/examples/process-fernhouse-commission.md`, a fictional client and maker moving a planter commission through five statuses, plus a status lane pattern in `assets/templates/process.md`
- **Playbook.** FJ-046, FJ-047 and FJ-048
- **Gallery image.** `assets/screenshots/process-status-lane-board.png` shows the worked example's board, captioned as a release check rather than a graded run
- **Release.** Hub 1.0.17.0, `sk-create-figjam` 1.0.16.0, 13 Project knowledge files rewritten by hand, one new Project file and a SYNC note
<!-- /ANCHOR:what-built -->

---

<!-- ANCHOR:how-delivered -->
## How It Was Delivered

Each check landed with planted self-test cases that failed first. The composer changes were then drawn on a scratch FigJam board from the worked example in one call, read back from a fresh view, and the clipped card height found there went back into the composer. The Project mirror was written by hand from the changed sources and checked in a scratch clone of the outer repository, because the Sync Loop refuses a dirty declaration file.
<!-- /ANCHOR:how-delivered -->

---

<!-- ANCHOR:decisions -->
## Key Decisions

| Decision | Why |
|----------|-----|
| D1 to D6 in spec.md Section 2 | Taken from the operator's answers of 2026-10-29 |
| A chevron for a status | A step is already a rounded rectangle, so the proposed shape would not tell them apart. The operator chose the chevron |
| A work view without the status lane | A status move is not a way out of a step, so an end may move the last status and stay an end, and the path limit reads the work alone |
| A shorter compact code | The new drawing code first left the Project 1,346 characters for a model. Merging the detail card into the entity card, encoding the status line as a dash level and dropping redundant brackets and separators in the compactor brought the room to 2,628 |
| A 32 pixel card allowance | The live board clipped a three-line body at 160 pixels and a probe measured 176 as the fit |
| Wrap advice skips cards | It read a card's lines as one label and advised on words that were never stranded |
| Review repairs | A fresh reviewer showed an architecture accepted a status lane and bodies, a status could take the accent and a status could go unmoved. Each is now refused. The Project mirrors also name the model room as the real ceiling for detail cards |
<!-- /ANCHOR:decisions -->

---

<!-- ANCHOR:verification -->
## Verification

| Check | Result |
|-------|--------|
| `flow_check.py --self-test` | 227 of 227, with four cases planted from the review |
| `compose_board.py --self-test` and `--design-check` | 1302 of 1302, 0 warnings |
| `pytest -q scripts/tests sk-create-figjam` | 18 passed |
| `benchmark/gates/run_gates.sh` | 15 of 15 |
| Scratch board read-back | 15 of 15 nodes, 20 of 20 connectors, 0 warnings, fresh view after the card resize |
| Sync Loop after the commits | Parity PASSED 66 of 66, residency PASSED 7 systems, divergence PASSED 66 pairs |
| Output format gate | Fails only on `sk-product-owner/SKILL.md:46`, a semicolon from before this phase |
| `validate.sh --strict` on this phase and the parent | RESULT: PASSED |
<!-- /ANCHOR:verification -->

---

<!-- ANCHOR:limitations -->
## Known Limitations

1. The Project can draw the commission model with 18 characters to spare, so a longer example of the same shape needs a shorter body or a second call.
2. The scratch board's three cards were resized in place after the allowance change, not recomposed from scratch.
3. The output format gate fails on a line outside this phase's scope.
4. Crossings among the status moves are not measured, because the crossing count reads the work view only.
<!-- /ANCHOR:limitations -->
