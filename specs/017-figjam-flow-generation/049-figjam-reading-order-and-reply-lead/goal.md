---
title: "Goal: Phase 49: FigJam reading order and reply lead"
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
    packet_pointer: "017-figjam-flow-generation/049-figjam-reading-order-and-reply-lead"
    last_updated_at: "2026-10-28T00:53:24Z"
    last_updated_by: "claude-code"
    recent_action: "Scaffolded the phase"
    next_safe_action: "Implement D1 to D8 with one Sonnet agent"
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
# Goal: Phase 49: FigJam reading order and reply lead

<!-- SPECKIT_TEMPLATE_SOURCE: goal | v2.2 -->
<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->
<!-- GOAL_AUTHORING: .skilled/skills/sk-doc/sk-create-goal/SKILL.md -->

---

<!-- ANCHOR:directive -->
## 1. DURABLE DIRECTIVE

**Objective:** Fix every cause the v1.0.14.0 Claude Sonnet 5.5 high rerun found as hub and `sk-create-figjam` v1.0.15.0 with its Claude Project mirror and kernel v1.2.15 in the same commits, so the glance order is the majority read, every delivery opens on the board URL, FJ-023 and the examples follow the turn 1 rule, diamond labels are measured by glyph width and Composition is scored by a script, then rerun FJ-022 and FJ-023 one after the other and refresh the gallery.

### Decisions

Frozen choices. Changing one is an amendment.

| ID | Decision |
|----|----------|
| D1 | Plain reading order: `reading_order` drops the lift that put a decision beside the accent second: the accent comes first, then column by column along the flow. Across all 18 reader orders of the 046 to 048 runs the lift fit the minority on FJ-023 and cost more boards than the plain order. `references/quality-rubric.md` Section 3 drops the exception and says the printed order is the majority read, the process example's `Glance:` line and second glance follow and phase 048's D1 is superseded. |
| D2 | Reply lead: Everything written after the last tool call is the reply and its first characters are the board URL, with no sentence before it, not a status line or a sentence announcing the reply. `references/flow-mode.md` Section 8 and step 11, `SKILL.md`, the rubric, `assets/flow-templates.md` with a wrong and a right first line, the kernel and the mirrors state it, and the harness flags a delivery whose first line is not the URL. |
| D3 | FJ-023 turns and the queue: FJ-023 scripts the turn 1 intake round its prompt calls for, as FJ-022 does, and keeps 8 of 8 nodes. `references/types/process.md` draws a queue that only carries work between two lanes as the crossing connector's label, and a queue is a store only when steps read and write it on their own. |
| D4 | Examples model the intake: The gantt, ER and sequence example requests name their reader, and the process and user flow examples show an intake round before the playback, in the skill and the Project. |
| D5 | Diamond wrap by glyph width: The label check wraps a diamond's label by Inter Medium advance widths at half its width less 4 px and reports a stranded last word as `leaves`, with a self-test on the labels FigJam stranded. |
| D6 | Dials are not rows: The detail level, the audience and the reading distance are dials, never Brief rows, so an unstated dial takes its default and never counts toward the two assumed rows, while a reader no source names stays unsettled. Flow-mode Section 2, playbook Section 5 and the mirror state it. |
| D7 | Mechanical Composition: Each reader's notes end on an `Order:` line and `run/composition_check.py` scores Composition from the plan's `Glance:` line and the two readers' orders, so the grader no longer reads the order by eye. |
| D8 | Release: Every change lands in the skill and its hand-written Project mirror in the same commit as hub and `sk-create-figjam` v1.0.15.0, with kernel v1.2.15 for the reply lead. |

<!-- /ANCHOR:directive -->

---

<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

- [ ] `compose_board.py --self-test`, `--design-check`, `flow_check.py --self-test`, `pytest scripts/tests`, `run_gates.sh` (all 15 gates) and the output format gate each exit 0 on the committed tree
- [ ] `validate_parity.py product-owner`, `residency_check.py --all` and `pair_divergence.py product-owner` each print PASSED after the last commit
- [ ] The reading order, reply lead, queue, examples, dials and Composition rules read the same in the skill and the Project
- [ ] `sk-create-figjam` and the hub read 1.0.15.0 with a changelog, and the kernel H1 reads v1.2.15
- [ ] FJ-022 and FJ-023 are rerun and graded on v1.0.15.0, recorded as README section 8.15, with the gallery refreshed
- [ ] `validate.sh --strict` on this phase prints RESULT: PASSED, and both repositories are pushed
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

### Deviations and findings

| Item | Note |
|------|------|
<!-- /ANCHOR:log -->
