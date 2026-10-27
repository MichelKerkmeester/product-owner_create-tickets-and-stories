---
title: "Implementation Summary"
description: "The gaps of the v1.0.7.0 rerun shipped as sk-create-figjam v1.0.8.0 with kernel v1.2.10, and the rerun of the 14 failures ended at 7 PASS and 7 FAIL under the operator's two grading rulings."
trigger_phrases:
  - "figjam glance and left out implementation summary"
importance_tier: "normal"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "017-figjam-flow-generation/042-figjam-glance-and-left-out"
    last_updated_at: "2026-10-27T12:16:00Z"
    last_updated_by: "claude-code"
    recent_action: "Graded the v1.0.8.0 rerun at 7 PASS and 7 FAIL under the operator rulings and closed the phase"
    next_safe_action: "Open phase 043 for the gaps the rerun still shows, then rerun the 7 failures"
    blockers: []
    key_files:
      - "spec.md"
      - "acceptance-criteria.md"
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
| **Spec Folder** | 042-figjam-glance-and-left-out |
| **Completed** | 2026-10-27 |
| **Level** | 2 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:what-built -->
## What Was Built

The gaps of the v1.0.7.0 rerun shipped as `sk-create-figjam` v1.0.8.0, `sk-product-owner` v1.2.5.0 and kernel v1.2.10, with the Claude Project mirror in the same commit. Claude Sonnet 5.5 high then ran the 14 failures again and 7 pass, up from none of them.

### Phase 42: FigJam glance plans and Left out

- **Glance plans match the board.** A state board plans its first state first and reads its composite as frame. The rubric adds the light blue entry to the kinds that read right after the accent, and the process, architecture, user flow and state examples plan what the composer draws.
- **One Left out rule.** The reply and the gate name every cut, split, later board and point the sources left open, in the same words across the skill, the mirror, the kernel, `AGENTS.md`, `sk-product-owner` and the user guide. Six example gates show the line.
- **Sticky, revision and split title.** A single sticky goes past its node's end dot and never moves without a new yes. A same-title revision finds its old section by its earlier write time. The first split title reads `1. Sign up`.
- **Label warning.** `flow_check.py` prints a `Label:` line for a node label that would leave one word alone on its last line, measured at 0.5 of the node size against rendered boards. It never fails the check, and the composer is unchanged, so the Project keeps its room.
- **Playbook and records.** The Composition row counts a composite as frame and costs one point for an unplanned early part. FJ-009, FJ-029, FJ-038 and FJ-045 carry the new signals and FJ-045 asks three reader questions. FJ-017's v1.0.7.0 record carries no scorecard.
- **Rerun.** 7 PASS and 7 FAIL, graded with readers who had each scenario's persona and questions. The gallery's state image is now the FJ-026 board at 21.

### Files Changed

| File | Action | Purpose |
|------|--------|---------|
| `sk-create-figjam/references/`, `assets/`, `scripts/`, `manual-testing-playbook/` | Modified | The rules, examples, label warning and playbook rows |
| `claude project/` and `Custom Instructions.md` | Modified | The mirror and kernel v1.2.10 |
| `SKILL.md`, `AGENTS.md`, `USER-GUIDE.md`, `sk-product-owner/SKILL.md`, `README.md`, version files, changelogs, `SYNC.md` | Modified, Created | The release and the one Left out rule |
| `benchmark/.../grades/sonnet-high-041.*`, `grader-brief-042.md` | Modified, Created | The FJ-017 record and the grader brief |
| `benchmark/.../skill/sonnet-high-042/`, `replies/`, `stdout/`, `renders/`, `grades/sonnet-high-042*` | Created | The rerun, its renders and its grades |
| `benchmark/.../README.md` | Modified | Section 8.8 |
| `sk-create-figjam/assets/screenshots/state-board.png` and both gallery captions | Modified | The FJ-026 board replaces the v1.0.6.0 one |
<!-- /ANCHOR:what-built -->

---

<!-- ANCHOR:how-delivered -->
## How It Was Delivered

Sentence swaps ran from one script with counted matches. DeepSeek V4.1 Flash max wrote the label warning, and the operator chose a warning over wider boxes because the Project has no room for composer growth. A fresh Opus reviewer read the whole diff and six of its seven findings were confirmed and fixed. The reviewer's seventh finding, that the label check is noisy, was declined because the rendered boards wrap those labels. Each board scenario wrote into a fresh draft file in the operator's team plan. One Opus grader scored all 14 runs, skeptics and adjudicators settled the disputes and a completeness critic checked the records. The operator then ruled that lanes and zones read as frame and that the state rule applies as written. Board URLs, file keys and plan names are redacted from every committed file.
<!-- /ANCHOR:how-delivered -->

---

<!-- ANCHOR:decisions -->
## Key Decisions

| Decision | Why |
|----------|-----|
| The state rule follows the drawn board | Readers read the saturated first state before the composite, and changing the composer would restyle every state board |
| Warn about an orphan word, never widen the box | The Project sends the whole composer in every call and its largest example already uses nearly all the room |
| Lanes and zones read as frame on every type | The operator's ruling, so FJ-023, FJ-034 and FJ-045 are graded on one rule |
| The state rule applies as written in grading | The operator's ruling, so FJ-026 and FJ-032 are graded the same way |
<!-- /ANCHOR:decisions -->

---

<!-- ANCHOR:verification -->
## Verification

| Check | Result |
|-------|--------|
| `compose_board.py --self-test` | 1244 of 1244, exit 0 |
| `compose_board.py --design-check` | 0 design warnings, exit 0 |
| `flow_check.py --self-test` | 169 of 169, exit 0 |
| `pytest -q scripts/tests` | 18 passed, exit 0 |
| `benchmark/gates/run_gates.sh` | all 15 gates pass, exit 0 |
| `validate-output-format.cjs --system product-owner` | passed across 72 source files, exit 0 |
| `validate_parity.py product-owner` | PASSED 65/65 declared pairs |
| `residency_check.py --all` | PASSED 7 systems |
| Rerun grades | 14 lines in `grades/sonnet-high-042.jsonl`, every evidence path resolving in the run folder |
| Leak scan of the added lines and run output | 0 hits |
<!-- /ANCHOR:verification -->

---

<!-- ANCHOR:limitations -->
## Known Limitations

1. **SC-001 is met only under the operator's rulings.** Before them the rerun passed 6 of 14.
2. **Seven scenarios still fail.** FJ-009's gate keeps its Plan and Calls lines. FJ-017 shifts stickies on adjacent rows. FJ-026 and FJ-032 lose Composition to a composite's inner states. FJ-029 titles its second board `2. Setup` and names no split. FJ-031 keeps a numbered title on its revision. FJ-036 opens its reply on a status sentence. Phase 043 takes these.
3. **No run printed a `Label:` line.** The check falls silent without node, and its prediction differs from the drawn board on some labels.
4. **FJ-018 and FJ-035 stay operator-only.** They need Figma Desktop and the figma-ds-cli daemon.
<!-- /ANCHOR:limitations -->
