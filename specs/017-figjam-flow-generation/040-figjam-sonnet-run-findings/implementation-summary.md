---
title: "Implementation Summary"
description: "The type question now goes alone, one board stays one board, Quick reaches the playback and boards keep their meaning in greyscale. Released as sk-create-figjam v1.0.6.0 with kernel v1.2.8, and the 31 scenarios that did not pass rerun at 14 PASS, 13 FAIL and 4 SKIP."
trigger_phrases:
  - "figjam sonnet run findings implementation summary"
importance_tier: "normal"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "017-figjam-flow-generation/040-figjam-sonnet-run-findings"
    last_updated_at: "2026-10-26T23:26:00Z"
    last_updated_by: "claude-code"
    recent_action: "Reran the 31 scenarios, refreshed the gallery, audited the skill docs and pushed both repositories"
    next_safe_action: "None in this phase. The 35 rerun findings wait for the operator to open a next phase"
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
| **Spec Folder** | 040-figjam-sonnet-run-findings |
| **Completed** | 2026-10-26 |
| **Level** | 2 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:what-built -->
## What Was Built

Claude Sonnet 5.5 high passed 23 of 54 FigJam scenarios on v1.0.5.0, and its boards averaged 20.6 of 22, so most failures came from the skill and the playbook rather than the drawing. Every finding that held up after review is fixed in `sk-create-figjam` v1.0.6.0, `sk-product-owner` v1.2.3.0 and kernel v1.2.8.

### Phase 40: FigJam Sonnet run findings

A brief that fits two diagram types now gets one question, alone, before anything else. A request for one board that runs over budget loses its least-needed part instead of turning into two boards, and Quick energy reaches the playback on a thin brief. On the board, kinds that share a shape differ by outline as well as colour, a plain connector has a `Leads to` key entry, the focus can say why it is the focus and every arrow lands on its own point. A file you name is read once before the gate, so a section with the same title is named there and never found after your yes.

### The rerun and the gallery

Claude Sonnet 5.5 high ran the 31 scenarios again from 22:00:39 UTC. One Opus grader scored all 34 runs, with skeptics and adjudicators on every grade, and the rerun reads 14 PASS, 13 FAIL and 4 SKIP, 13 of the passes new. The 13 graded rerun boards score 274 of 286, and none lost a Signal point in greyscale. The skill's gallery now shows the best v1.0.6.0 board of each type. A findings pass and a critic named 35 findings for a next phase, listed in the run README section 8.6.

### Files Checked Against v1.0.6.0

An Opus reviewer read every `sk-create-figjam` doc against the v1.0.6.0 changelog and the composer's own output, and opened every gallery image beside its caption. Five files held stale lines, fixed with their Project copies.

- `SKILL.md`: the Quick line, fixed
- `README.md`: OK, every caption matches its image
- `assets/figjam-design.md` and `assets/flow-templates.md`: OK
- `assets/screenshots/README.md`: OK once one caption measurement was removed
- `assets/templates/` for architecture, ER, gantt, process, sequence and state: OK
- `assets/examples/` for architecture, ER, gantt, process, sequence and user flow: OK
- `assets/examples/state-roamstay-booking.md`: the glance order, fixed
- `references/flow-mode.md`, `references/hybrid-workflow.md` and `references/style-guide.md`: OK
- `references/quality-rubric.md`: the greyscale line, fixed
- `references/types/` for architecture, ER, process, sequence, state and user flow: OK
- `references/types/gantt.md`: the arrow sentence, fixed
- `manual-testing-playbook/manual-testing-playbook.md`: the zone tint rule and the fallback count, fixed

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
| benchmark/reports/2026-10-25--manual-testing-playbook--figjam-model-comparison/ | Modified | Driver, aggregator, rerun records, grades, renders and README sections 8.5 and 8.6 |
| sk-create-figjam/assets/screenshots/, sk-create-figjam/README.md, README.md | Modified | The gallery's v1.0.6.0 boards and captions |
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
| `validate_parity.py product-owner` | PASSED, 65 of 65 pairs, after the last commit |
| `residency_check.py --all` | PASSED, 7 systems |
| Rerun | 14 PASS, 13 FAIL and 4 SKIP, 31 graded lines, first stream timestamp 22:00:50 UTC |
<!-- /ANCHOR:verification -->

---

<!-- ANCHOR:limitations -->
## Known Limitations

1. **13 reruns still fail.** Six are model slips alone. The rest trace to gaps the run README section 8.6 names, such as an undefined request for one board and a state board's first glance, and wait for the operator's call on a next phase.
2. **Little room in the Project's composer call.** The whole composer leaves about 2,470 characters for the model, against about 2,400 for the largest shipped example model.
3. **One known crossing.** The composite state exit still crosses one edge, and the self-test records it as open.
4. **One board has no render.** FJ-031's first board was deleted by its own scripted turns before it could be rendered.
<!-- /ANCHOR:limitations -->
