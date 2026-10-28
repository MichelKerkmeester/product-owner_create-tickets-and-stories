---
title: "Goal: Phase 47: FigJam glance and row fixes"
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
    packet_pointer: "017-figjam-flow-generation/047-figjam-glance-and-row-fixes"
    last_updated_at: "2026-10-27T23:30:00Z"
    last_updated_by: "claude-code"
    recent_action: "Scaffolded the phase"
    next_safe_action: "Write the Project mirror and the v1.0.13.0 release"
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
# Goal: Phase 47: FigJam glance and row fixes

<!-- SPECKIT_TEMPLATE_SOURCE: goal | v2.2 -->
<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->
<!-- GOAL_AUTHORING: .skilled/skills/sk-doc/sk-create-goal/SKILL.md -->

---

<!-- ANCHOR:directive -->
## 1. DURABLE DIRECTIVE

**Objective:** Fix every cause the v1.0.12.0 Claude Sonnet 5.5 high rerun found as hub and `sk-create-figjam` v1.0.13.0 with its Claude Project mirror and kernel v1.2.13 in the same commits, so the glance plan follows the drawn board, a bending main row is flagged, each sticky keeps its side and alignment within reach, the gate shows the checked model line for line and labels have a way past a wrap, then rerun FJ-017, FJ-022, FJ-023 and FJ-036 and refresh the gallery.

### Decisions

Frozen choices. Changing one is an amendment.

| ID | Decision |
|----|----------|
| D1 | `flow_check.py` prints a `Glance:` line on a user flow or a process, the rubric plans the glance lines from it with path order as the fallback and the playbook scores against it |
| D2 | A non-failing `Row:` line names a main-row line that bends, the node between and the zone move, with the composer unchanged |
| D3 | `Sides:` lines name the alignment, no square past one sticky width is offered and the notes call places each sticky on the named side and alignment |
| D4 | The gate shows the checked model verbatim, every `%%` and `style` line, with the `PASSED` line as printed |
| D5 | `may leave` marks a one-measure strand, step 5 allows a reworded or longer label or naming at the gate, the Legibility row covers several wraps and each example's Check block matches the check |
| D6 | Parts a reader names together in one reading step read as a set |
| D7 | Intake round One asks the three dials |
| D8 | An intake round beyond those a scenario names ends on its question |
| D9 | The harness redacts each scenario's own output and its run-log rows and reads a counted read-back or a `use_figma` call as a delivery |

<!-- /ANCHOR:directive -->

---

<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

- [x] `compose_board.py --self-test`, `--design-check`, `flow_check.py --self-test`, `pytest scripts/tests`, `run_gates.sh` (all 15 gates) and the output format gate each exit 0 on the committed tree
- [x] `validate_parity.py product-owner`, `residency_check.py --all` and `pair_divergence.py product-owner` each print PASSED after the last commit
- [x] The glance, row, sides, sketch, label, composition, dials and intake rules read the same in the skill and the Project
- [x] `sk-create-figjam` and the hub read 1.0.13.0 with a changelog, and the kernel H1 reads v1.2.13
- [x] FJ-017, FJ-022, FJ-023 and FJ-036 are rerun and graded on v1.0.13.0, recorded as README section 8.13, with the gallery refreshed
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
| Release v1.0.13.0 committed and pushed | Done | PO 99fbf956, b573d033 and f0c0ba95, outer 0f808e801 and 3fe1a442e, parity PASSED 65 of 65 |
| Rerun on v1.0.13.0 graded | Done | 1 of 4 pass, run README section 8.13, SC-003 not met and phase 048 takes the causes |

### Deviations and findings

| Item | Note |
|------|------|
<!-- /ANCHOR:log -->
