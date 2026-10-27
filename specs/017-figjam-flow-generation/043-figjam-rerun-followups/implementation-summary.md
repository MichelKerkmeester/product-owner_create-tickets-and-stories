---
title: "Implementation Summary"
description: "v1.0.9.0 fixed the gaps of the v1.0.8.0 rerun and the 7 failures ran again: 1 passes, SC-001 is unmet and phase 044 takes the composer placement and the path-order glance rule."
trigger_phrases:
  - "figjam rerun follow-ups implementation summary"
importance_tier: "normal"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "017-figjam-flow-generation/043-figjam-rerun-followups"
    last_updated_at: "2026-10-27T14:00:00Z"
    last_updated_by: "claude-code"
    recent_action: "Closed the phase after the graded rerun"
    next_safe_action: "Open phase 044"
    blockers: []
    key_files: []
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
| **Spec Folder** | 043-figjam-rerun-followups |
| **Completed** | 2026-10-27 |
| **Level** | 2 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:what-built -->
## What Was Built

`sk-create-figjam` and the hub shipped as v1.0.9.0 with kernel v1.2.11, and Claude Sonnet 5.5 high ran the 7 failures of v1.0.8.0 again. 1 passes. SC-001 asked for 5, so it is unmet, and the operator chose to close this phase and open 044 for the two causes the grading found.

### Phase 43: FigJam rerun follow-ups

- **State plan.** A state board with no state named plans the first state first, the states inside a composite second with their section and the end states last. The state example, whose request names the end states, focuses Cancelled (D1, D10)
- **Split, revision and reply.** The second split board is `2. Workspace setup` and is named under `Left out:`. A revision's changed end is the second glance alone and a revision that deletes keeps the old title. Every Flow reply and the reply after a delete open on the board URL with nothing before it, in the skill, `AGENTS.md`, the Project and the kernel
- **Stickies and the missing route.** A second sticky on an adjacent row goes below or left with a `Finding:` line, and the gantt example shows the missing-route gate, the Project copy in connector words
- **Label check.** `flow_check.py` prints `Label: skipped` with the reason when node is missing or the trace fails, and the Project's Flow Mode carries a hand rule for labels
- **Playbook.** The Composition row reads lanes and zones as frame, counts a composite's states as parts, needs both of two readers and exempts the entry and decisions on a revision (D3, D5, D9). The style guide reads the 56 pixel rule on the composer's path estimate (D2)
- **Rerun.** 7 lanes in fresh draft files, 29 turns, every turn exit 0. One grader, two readers per scored board, skeptics, adjudicators and a critic, with the operator's FJ-017 ruling. Records in `grades/sonnet-high-043.*` and README section 8.9

### Files Changed

| File | Action | Purpose |
|------|--------|---------|
| `sk-create-figjam/references/`, `assets/`, `SKILL.md`, `README.md` | Modify | The state, split, revision, reply, sticky, style and label rules and the state and gantt examples |
| `sk-create-figjam/scripts/flow_check.py` | Modify | The skipped `Label:` line and its two self-test cases |
| `sk-create-figjam/manual-testing-playbook/` | Modify | The Composition row, two readers and FJ-017's reply signal |
| `claude project/`, `AGENTS.md`, `SYNC.md`, `README.md`, version files, changelogs | Modify, Create | Mirror, kernel v1.2.11 and the v1.0.9.0 release |
| `benchmark/reports/2026-10-25--manual-testing-playbook--figjam-model-comparison/` | Create, Modify | The rerun, its renders, the grader brief, the grades, the reader notes and README section 8.9 |
<!-- /ANCHOR:what-built -->

---

<!-- ANCHOR:how-delivered -->
## How It Was Delivered

The sentence swaps ran by script, each matched once in the skill and the mirror. DeepSeek V4.1 Flash max on cli-pi made the `flow_check.py` change. A fresh Opus medium reviewer found no P0 and three P1 findings. The operator settled two of them (D9, D10) and the confirmed fixes went in by a second script. Three small polish edits to `flow_check.py` from that review were made by hand rather than through DeepSeek, because each was a line or two: the skipped line keeps to the first line of an error, the module docstring names it and `unittest.mock` loads only in the self-test. The rerun ran after the commit, and the grading ran as one workflow.
<!-- /ANCHOR:how-delivered -->

---

<!-- ANCHOR:decisions -->
## Key Decisions

| Decision | Why |
|----------|-----|
| Plan a composite's inner states second | Readers took them early, so the plan was moved toward what the board shows |
| Two readers per scored board | One reader's read decided several verdicts on its own |
| Exempt the entry and decisions on a revision (D9) | The rubric itself says the entry reads right after the accent |
| A request to colour the end states names a group (D10) | The playbook already read it that way, so the example had to agree |
| FJ-017 fails on the 042 reading of beside | The operator kept one reading across runs |
| Close with SC-001 unmet and open 044 | Every remaining failure has one of two causes the rules alone cannot fix |
<!-- /ANCHOR:decisions -->

---

<!-- ANCHOR:verification -->
## Verification

| Check | Result |
|-------|--------|
| Composer self-test and design check | 1244 of 1244, exit 0 |
| Flow check self-test | 171 of 171 with node, 168 of 168 without it |
| pytest, repository gates and output format gate | 18 passed, 15 of 15, passed across 72 source files |
| Sync Loop | parity PASSED 65/65, residency PASSED 7 |
| Rerun | 1 PASS and 6 FAIL, 97 of 110 points on the 5 scored boards, every Composition at 0 |
| Leak scan | 108 rerun files and the 12 grade files, 0 hits |
<!-- /ANCHOR:verification -->

---

<!-- ANCHOR:limitations -->
## Known Limitations

1. **SC-001 is unmet.** 1 of 7 passes. The composer draws a composite across the top row, so its inner states read before any planned first glance, and readers take a flow's main row in path order while the plans order nodes by fill. Phase 044 takes both.
2. **No label trace ran.** Homebrew's node on the run machine cannot load its `simdutf` library, so every check printed the skipped line. Phase 044 pins a working node in the launcher.
3. **FJ-018 and FJ-035 stay operator-only.** They need Figma Desktop and the figma-ds-cli daemon.
<!-- /ANCHOR:limitations -->
