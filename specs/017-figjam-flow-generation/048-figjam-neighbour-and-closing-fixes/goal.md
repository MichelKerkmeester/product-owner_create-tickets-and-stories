---
title: "Goal: Phase 48: FigJam neighbour and closing fixes"
description: "The durable directive this packet executes against and the criteria that decide when it is done."
trigger_phrases:
  - "packet goal"
  - "durable directive"
  - "completion criteria"
  - "goal binding"
importance_tier: "important"
contextType: "planning"
_memory:
  continuity:
    packet_pointer: "017-figjam-flow-generation/048-figjam-neighbour-and-closing-fixes"
    last_updated_at: "2026-10-28T00:53:24Z"
    last_updated_by: "claude-code"
    recent_action: "Scaffolded the phase"
    next_safe_action: "Verify the implementer diff and run the gates"
    blockers: []
    key_files: []
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "348b59cb-58a2-4b49-8147-c40143312bc1"
      parent_session_id: null
    completion_pct: 0
    open_questions: []
    answered_questions: []
---
# Goal: Phase 48: FigJam neighbour and closing fixes

<!-- SPECKIT_TEMPLATE_SOURCE: goal | v2.2 -->
<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->
<!-- GOAL_AUTHORING: .skilled/skills/sk-doc/sk-create-goal/SKILL.md -->

---

<!-- ANCHOR:directive -->
## 1. DURABLE DIRECTIVE

**Objective:** Fix every cause the v1.0.13.0 Claude Sonnet 5.5 high rerun found as hub and `sk-create-figjam` v1.0.14.0 with its Claude Project mirror in the same commits, so a decision beside the accent reads where readers meet it, each intake round ends on one closing question, FJ-017 asks for the Finding the skill gives and the trace draws diamonds as FigJam does, then rerun FJ-017, FJ-022, FJ-023 and FJ-036 and refresh the gallery.

### Decisions

Frozen choices. Changing one is an amendment.

| ID | Decision |
|----|----------|
| D1 | Accent neighbour: `reading_order` puts a decision joined to the accent by one line, set on the accent's own row with no node between them on that row, right after the accent. `references/quality-rubric.md` Section 3 states the same exception, the process example's `Glance:` line and second glance are regenerated and a self-test holds the FJ-036 shape, where a node stands between, to the plain order. |
| D2 | Closing question: Every intake round ends on one closing question after its last block, such as `Take the recommended answers, or correct any of them?`, so each `Why:` line stays inside its block: `assets/flow-templates.md` Section 5, `references/flow-mode.md` Section 8 and playbook Section 5, where a round whose last line is anything else misses its signal. The template's block order stays. |
| D3 | Finding on a moved sticky: FJ-017 and the root playbook ask for a `Finding:` line only for a sticky that left the side its `Sides:` line named, and none for a sticky placed where its line said. `references/hybrid-workflow.md` Section 3 says the check gives the second sticky the side below or to the left and names it on its `Sides:` line, so the gate shows it. The Project hybrid mirror, which has no check, says the notes call chooses the side from the returned boxes and a reply names every sticky placed below or left of its node on a `Finding:` line. |
| D4 | Diamond label trace: `compose-trace.mjs` measures whole-pixel line heights, so the trace draws diamonds at the size FigJam draws them, and `board_geometry._text_width` reads a diamond's text box as half its width less 8 px. A self-test holds a 26-character decision to a 336 px diamond, and the user flow example's `Drop-off point or pickup?` is reworded in the skill and the Project. |
| D5 | Dials at the playback: The playback names the three dials by their words and the gate need not repeat them, in flow-mode and its mirror, and playbook Section 5 fails a playback that leaves one out. |
| D6 | Composition levels: The playbook Composition row scores 2 when the planned order holds with the requested element first, 1 when one part reads out of its planned place or one unplanned part reads at or before the second glance, and 0 for two or more or a requested element not first. When two parts swap, only the part read earlier than its place costs the point. |
| D7 | Turn 1 intake: Playbook Section 5: under Standard energy, when the sources leave the reader unsettled or more than two rows assumed, turn 1 is an intake round, and no model is written and no check runs before the playback's answer, read from the tool stream. |
| D8 | Release: Every change lands in the skill and its hand-written Project mirror in the same commit as hub and `sk-create-figjam` v1.0.14.0, with a kernel bump only if a kernel sentence changes. |

<!-- /ANCHOR:directive -->

---

<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

- [x] `compose_board.py --self-test`, `--design-check`, `flow_check.py --self-test`, `pytest scripts/tests`, `run_gates.sh` (all 15 gates) and the output format gate each exit 0 on the committed tree
- [x] `validate_parity.py product-owner`, `residency_check.py --all` and `pair_divergence.py product-owner` each print PASSED after the last commit
- [x] The glance, closing question, Finding, label, dials, composition and turn 1 rules read the same in the skill and the Project
- [x] `sk-create-figjam` and the hub read 1.0.14.0 with a changelog
- [x] FJ-017, FJ-022, FJ-023 and FJ-036 are rerun and graded on v1.0.14.0, recorded as README section 8.14, with the gallery refreshed
- [x] `validate.sh --strict` on this phase prints RESULT: PASSED, and both repositories are pushed
<!-- /ANCHOR:completion -->

---

<!-- ANCHOR:log -->
## 4. LOG

Everything below is VOLATILE. It is not part of the directive, it is not copied
into the objective, and it is expected to grow. Progress, evidence, deviations
and findings belong here.

### Progress

| Item | State | Evidence |
|------|-------|----------|
| Phase scaffolded | Done | spec, plan, tasks, acceptance criteria, implementation summary and this goal |
| Release v1.0.14.0 committed and pushed | Done | PO e0a082d5 and 3a3a356a, outer 2ea776e8e and 8bc6d1014, parity PASSED 65 of 65 |
| Rerun on v1.0.14.0 graded | Done | 2 of 4 pass, run README section 8.14, SC-003 not met and phase 049 takes the causes |

### Deviations and findings

| Item | Note |
|------|------|
<!-- /ANCHOR:log -->
