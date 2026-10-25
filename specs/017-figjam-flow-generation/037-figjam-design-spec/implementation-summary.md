---
title: "Implementation Summary"
description: "The FigJam design file, the eighteen ranked fixes and the claude.ai Project mirror are built, hardened by a fresh Opus high review and pass every gate. The gallery recompose moved to phase 038."
trigger_phrases:
  - "figjam design spec implementation summary"
importance_tier: "normal"
contextType: "general"
_memory:
  continuity:
    packet_pointer: "017-figjam-flow-generation/037-figjam-design-spec"
    last_updated_at: "2026-10-25T21:00:00Z"
    last_updated_by: "claude-code"
    recent_action: "Wrote the spec folder"
    next_safe_action: "Record the baseline and start task T002"
    blockers: []
    key_files:
      - "spec.md"
      - "decision-record.md"
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "348b59cb-58a2-4b49-8147-c40143312bc1"
      parent_session_id: null
    completion_pct: 3
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
| **Spec Folder** | 037-figjam-design-spec |
| **Status** | Complete |
| **Completed** | 2026-10-25 |
| **Level** | 2 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:what-built -->
## What Was Built

Every composed FigJam board is now drawn in one design file a team can edit. `sk-create-figjam/assets/figjam-design.md` holds the tokens as one json block, `scripts/figjam_checks/design.py` reads it over the composer's built-in design and holds every token to its floor, and `compose_board.py` sends the composer only the tokens that differ as `THEME`. A token that misses a floor falls back to its shipped value with a named `DESIGN` line, and a block that does not parse falls back whole, so a bad edit never stops a board. The eighteen ranked fixes from phase 036 are the composer's only behaviour. The rubric, the playbook, the style guide, the seven type references, the READMEs and the user guide follow, and the claude.ai Project carries the design as a new Knowledge file under kernel v1.2.4.

### Files Changed

| File | Action | Purpose |
|------|--------|---------|
| sk-create-figjam/assets/compose-board.js | Modified | Built-in design, `__THEME__` merge and the ranked fixes |
| sk-create-figjam/assets/figjam-design.md | Created | The design file |
| sk-create-figjam/scripts/figjam_checks/design.py | Created | Reads, checks and diffs the design |
| sk-create-figjam/scripts/compose_board.py | Modified | Fills `__THEME__`, prints `DESIGN` lines, `--design-check` and the self-test checks |
| sk-create-figjam/scripts/figjam_checks/board_geometry.py | Modified | Takes the design's sizes and accent, and measures each stage zone from its own top, never above the shared one |
| sk-create-figjam/scripts/compose-trace.mjs | Modified | Records each text's font and plants two families that fail to load, so the font fallbacks are proved |
| sk-create-figjam/scripts/flow_check.py | Modified | Skips the design file as a model |
| sk-create-figjam/references/ (style guide, rubric, flow mode, hybrid workflow, seven types) | Modified | Point at the design file and record the shipped design |
| sk-create-figjam/manual-testing-playbook/ | Modified and created | Signal and tint rules, FJ-044 and FJ-045 |
| sk-create-figjam/SKILL.md, README.md, changelog/v1.0.3.0.md | Modified and created | File map, routing and release notes |
| SKILL.md, README.md, USER-GUIDE.md, mode-registry.json, description.json, hub-router.json, changelog/v1.0.3.0.md, leaf-manifest.json | Modified and created | Hub release v1.0.3.0 and the manifest |
| claude project/ (kernel, README, 12 Knowledge files, 1 new) | Modified and created | The Project mirror and kernel v1.2.4 |
| SYNC.md | Modified | Dated maintenance note |
| ../z — Claude Project Sync Loop/systems.py and systems.cjs | Modified | New pair and source, four resynced residency statements, the stale composer review record dropped and the user guide's review recorded |
<!-- /ANCHOR:what-built -->

---

<!-- ANCHOR:how-delivered -->
## How It Was Delivered

The composer's constants moved into one built-in design object first, so the theme merge and the design reader share one source. The fixes then landed one rank at a time against the self-test. One fix broke five architecture fixtures: aligning zone tops in a row stretched the External zone over the corridor an edge needed. Isolating it showed the cause, and the rule now aligns a row only when no edge skips a zone in it, with the same rule in the Python stage-zone check. The mirror's code block was regenerated from `compose_board.py --template`, and the Sync Loop gates ran in a scratch clone because they refuse an uncommitted declaration.

A fresh Opus high review then raised 15 findings, three P1 and twelve P2, and each was checked against the code before it was fixed. A nested list in the tint cycle crashed the design read, so the reader now refuses any item that is not a name and a guard draws the built-in design on any failure it did not foresee. The floor loop stopped after twelve passes, so it now reverts one token at a time until every floor holds. Flow Mode still said 16 pixel edge labels. The rest closed gaps the review measured: lines and dots that could vanish on white, a key on the accent's hue, sizes with no ceiling, a name long enough to break the size limit, Windows line endings, a Semi Bold style most families name SemiBold, zone tints that only looked at the zone declared before them, a loose stage-zone check and a Project mirror nothing checked. A second fresh review closed all 15 and found four more gaps in the new code: zone names had no working ceiling, a zone the cycle could not fit took the key's gray, an early revert could drop a token that would have stood and a lone surrogate in a key word crashed the compose. The stage-zone check also accepted a top that was neither legal edge. Each is fixed and replayed on the reviewer's own probes, and the self-test now composes the planted models at the largest and smallest sizes the floors allow.
<!-- /ANCHOR:how-delivered -->

---

<!-- ANCHOR:decisions -->
## Key Decisions

| Decision | Why |
|----------|-----|
| One design file inside the skill (ADR-001) | The operator chose it |
| Fall back with a warning (ADR-003) | The operator chose it |
| White sequence participants (ADR-007) | The operator chose it |
| The Project gets the design now (ADR-008) | The operator chose it |

The other five records are in `decision-record.md`. The operator left the remaining calls to judgement, to be checked at the end:

| Judgement call | Why |
|----------|-----|
| No per-run `--design` flag | One design per repository was the operator's choice, and a flag would add a second source |
| Plain JSON with swatch names, never a hex outside the palette | A custom colour drops out of FigJam's picker |
| No layout switches, spacing and rhythm stay the composer's | The router measures every clearance against the spacing |
| Rank 8 grows the diagram's box to hold its routes | The router's corridors stay as tested, and the title gap check holds every board |
| Rank 11 pins sit beside the sender's lifeline, where the research said the first lifeline | The pin then reads with the message it numbers on every row |
| Rank 6 aligns a row only when no edge skips a zone in it | Aligning across a skipped zone closed the corridor an edge needed |
| Rank 12 outlines planned bars in the connector gray through an outline rule, not a new pair | Planned bars read hollow at overview zoom, and the white pair's light stroke still serves every other white node |
| A fork maps to `pseudo`, a final state to `done` and a queue gets its own role | Each keeps the colour it drew before |
| The key orders kinds as the `kind` group lists them, the focus last | One order per type, set in one place |
| The scorecard stays at 22 points | Its Signal reads the design file instead of growing a dimension |
| A family FigJam cannot load falls back to Inter with a warning | A bad family should not stop a board |
| The board's tag records the design's name and hash | A later revision can tell which design drew a board |
| No self-test pin that the shipped file equals the built-in design | A team's restyle would then fail the gates |
| Async messages and lifelines hold 2:1 on white, every connector 3:1 | The shipped async blue measures 2.44:1 and the lifeline gray 2.1:1, and an open head also marks an async message, so 3:1 would have failed the shipped design |
| A missed floor reverts one changed token at a time | A token that only missed a floor beside another edit stands once that edit is back |
| The key keeps the composer's kind order, and the design file now says so | A reorderable key would be a new token for no request that asked for one |
| Zone tints avoid any zone drawn within two zone gaps, not only the zone declared before | Architecture, state and ER zones sit wherever the layout puts them |
| Semi Bold is tried as `Semi Bold`, then `SemiBold` | Inter uses the first name and most other families the second |
| Zone names stop at 24 pixels, so node labels do too | At 28 the router pushed an edge through a zone on five planted architectures, and the break depends on a name's length, so the ceiling is the size the router was tuned for rather than the largest that passed today's fixtures |
| A zone the tint cycle cannot fit keeps the neighbour rule and repeats a member's hue, with a warning | Two zones reading as one hurts a board more than a zone sharing a step's hue, and the key's gray stays the key's |
| The gallery moves to phase 038 (ADR-010) | The operator asked for a three-model comparison that composes every type anyway |
<!-- /ANCHOR:decisions -->

---

<!-- ANCHOR:verification -->
## Verification

| Check | Result |
|-------|--------|
| Composer self-test | 1,015 of 1,015, from a baseline of 815 of 815 |
| Flow check self-test | 158 of 158, unchanged |
| Unit tests | 18 passed, unchanged |
| Packet gates | 15 of 15 with the upstream root set, as at the base commit |
| Sync Loop gates in a scratch clone | Residency passed, parity 65 of 65 with the user guide review recorded, output format passed across 72 files, reference parity identical |
| Design check | Exit 0 on the shipped file with `THEME {}`, 0 design warnings and 3,447 characters left for the model, exit 1 on a broken copy with three named warnings |
| Fallbacks | One bad token and a broken block each still compose an ER board at 48,229 characters |
| Gallery | Moved to phase 038 by ADR-010 |
| Opus high review | 15 findings, all fixed. A second fresh review closed all 15 and raised four new P2s and an F11 residual, all fixed and replayed on its own probes |
| Spec validation | validate.sh --strict passed on this folder, the parent and phase 036 after the metadata repair |
<!-- /ANCHOR:verification -->

---

<!-- ANCHOR:limitations -->
## Known Limitations

1. **The gallery shows the earlier composer.** The screenshots in `sk-create-figjam/assets/screenshots/` predate this phase until phase 038 recomposes them.
2. **The user guide review record needs the commit hash.** Parity holds a recorded review to the commit that changed the source, so `systems.py` records it in a second outer commit.
3. **The model has less room.** The compact composer grew to 46,569 characters, so the model JSON and the `THEME` line share 3,449 characters in one `use_figma` call. The largest shipped example model runs 2,261.
<!-- /ANCHOR:limitations -->
