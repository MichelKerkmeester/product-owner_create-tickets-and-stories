---
title: "Implementation Summary"
description: "The type question now goes alone, one board stays one board, Quick reaches the playback and boards keep their meaning in greyscale. Released as sk-create-figjam v1.0.6.0 with kernel v1.2.8, with the rerun of the 31 scenarios that did not pass still to come."
trigger_phrases:
  - "figjam sonnet run findings implementation summary"
importance_tier: "normal"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "017-figjam-flow-generation/040-figjam-sonnet-run-findings"
    last_updated_at: "2026-10-26T20:00:00Z"
    last_updated_by: "claude-code"
    recent_action: "Fixed the run's findings, mirrored them and cut v1.0.6.0"
    next_safe_action: "Rerun the 31 scenarios at or after 22:00 UTC, then render, grade and refresh the gallery"
    blockers: []
    key_files:
      - "spec.md"
      - "acceptance-criteria.md"
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "348b59cb-58a2-4b49-8147-c40143312bc1"
      parent_session_id: null
    completion_pct: 60
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
| **Spec Folder** | 040-figjam-sonnet-run-findings |
| **Completed** | In progress |
| **Level** | 2 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:what-built -->
## What Was Built

Claude Sonnet 5.5 high passed 23 of 54 FigJam scenarios on v1.0.5.0, and its boards averaged 20.6 of 22, so most failures came from the skill and the playbook rather than the drawing. Every finding that held up after review is fixed in `sk-create-figjam` v1.0.6.0, `sk-product-owner` v1.2.3.0 and kernel v1.2.8.

### Phase 40: FigJam Sonnet run findings

A brief that fits two diagram types now gets one question, alone, before anything else. A request for one board that runs over budget loses its least-needed part instead of turning into two boards, and Quick energy reaches the playback on a thin brief. On the board, kinds that share a shape differ by outline as well as colour, a plain connector has a `Leads to` key entry, the focus can say why it is the focus and every arrow lands on its own point. A file you name is read once before the gate, so a section with the same title is named there and never found after your yes.

### Files Changed

| File | Action | Purpose |
|------|--------|---------|
| sk-create-figjam/SKILL.md, references/flow-mode.md | Modified | Type question alone, one-board cut, Quick threshold, accepted recommendation, scope narrowing, read before the gate |
| sk-create-figjam/references/ (rubric, style guide, hybrid workflow, seven types) | Modified | Accent on a revision, focus reason, outline weights, diamond pins, async messages, composite state section |
| sk-create-figjam/assets/ (composer, design, templates, examples) | Modified | Outlines, key entries, arrival points, gantt arrows, solid log edges |
| sk-create-figjam/scripts/ | Modified | Checks for every new drawing rule and the flow focus line |
| sk-create-figjam/manual-testing-playbook/ | Modified | Scenario corrections and the `driver:` key |
| sk-product-owner/references/interactive-mode.md | Modified | A board command conflict asks about the artifact first |
| claude project/, SYNC.md, README.md, USER-GUIDE.md | Modified | Mirror, kernel v1.2.8 and release notes |
| benchmark/reports/2026-10-25--manual-testing-playbook--figjam-model-comparison/ | Modified | Driver, aggregator, grades, renders and README section 8.5 |
| changelog/, sk-create-figjam/changelog/, sk-product-owner/changelog/, version files | Created, Modified | v1.0.6.0 and v1.2.3.0 |
<!-- /ANCHOR:what-built -->

---

<!-- ANCHOR:how-delivered -->
## How It Was Delivered

Five lanes each owned their own files, a sixth mirrored the changes into the Project and four reviewers read the whole diff. A repair lane fixed the 15 findings it confirmed, and a last pass applied the handoffs no lane owned. DeepSeek V4.1 Flash max made every edit from exact old and new text, and each target was byte-compared with an expected copy before it counted.
<!-- /ANCHOR:how-delivered -->

---

<!-- ANCHOR:decisions -->
## Key Decisions

| Decision | Why |
|----------|-----|
| Change the shared Human Voice Core card in every system | The operator said yes, and a byte copy in five systems means one change lands in all of them at once |
| Keep FJ-031 and FJ-032 runnable | Their operator setup steps are graded `harness`, and the rest of each scenario still measures the model |
| Fix a composite state section in planning, not in the composer | The zone tints sit within 4 luma of each other and a section has one fill |
| Record the composite exit's one crossing as open | A router rewrite is out of scope, and the self-test now fails on any new crossing |
<!-- /ANCHOR:decisions -->

---

<!-- ANCHOR:verification -->
## Verification

| Check | Result |
|-------|--------|
| `compose_board.py --self-test` | PASS, 1,240 of 1,240 |
| `compose_board.py --design-check` | PASS, 0 design warnings, room 9,341, 33,350 and 32,974 |
| `flow_check.py --self-test` | PASS, 163 of 163 |
| `pytest scripts/tests` | PASS, 18 tests |
| `benchmark/gates/run_gates.sh` | PASS, all 15 gates |
| Output format gate | PASS across 72 source files |
| Composer mirror | The Knowledge code block equals `--template`, 155 lines and 47,545 characters |
<!-- /ANCHOR:verification -->

---

<!-- ANCHOR:limitations -->
## Known Limitations

1. **The rerun has not run yet.** The 31 scenarios wait for 22:00 UTC under decision D1.
2. **Little room in the Project's composer call.** The whole composer leaves about 2,470 characters for the model, against about 2,400 for the largest shipped example model.
3. **One known crossing.** The composite state exit still crosses one edge, and the self-test records it as open.
<!-- /ANCHOR:limitations -->
