---
title: "Goal: Phase 33: Composed FigJam boards"
description: "The durable directive this packet executes against and the criteria that decide when it is done."
trigger_phrases:
  - "composed boards goal"
importance_tier: "important"
contextType: "planning"
_memory:
  continuity:
    packet_pointer: "product-owner/017-figjam-flow-generation/033-composed-boards"
    last_updated_at: "2026-10-21T18:00:00Z"
    last_updated_by: "claude-code"
    recent_action: "Authored the durable directive"
    next_safe_action: "Start the phase"
    blockers: []
    key_files: []
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "1004bf13-7863-4447-a63e-6ad2f5fcfd86"
      parent_session_id: null
    completion_pct: 0
    open_questions: []
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: goal | v2.2 -->
# Goal: Phase 33: Composed FigJam boards

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->
<!-- GOAL_AUTHORING: .skilled/skills/sk-doc/sk-create-goal/SKILL.md -->

---

<!-- ANCHOR:directive -->
## 1. DURABLE DIRECTIVE

**Objective:** Compose every board with use_figma from the checked model: a framed board with a title block, tinted zones, palette shapes sized to their text, routed connectors and a key, laid out on a spacing grid, then read back and screenshot-checked.

### Decisions

Frozen choices. Changing one is an amendment.

| ID | Decision |
|----|----------|
| D1 | The operator judged the live boards of 2026-10-22 decent in content and poor in design, and asked on 2026-10-24 for boards that look a lot better |
| D2 | The operator chose on 2026-10-24 to compose boards with use_figma rather than polish generate_diagram output |
| D3 | The operator asked for the Flow scenarios to be rerun on SWE 2 MAX through cli-devin after the upgrade |
| D4 | No commit or push without the operator's go-ahead |

<!-- /ANCHOR:directive -->

---

<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

- [x] All gates pass
- [x] Format gate keeps its counts
- [x] validate.sh --strict on 033-composed-boards prints RESULT: PASSED
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
| Opened | Done | 2026-10-21 |
| Composer built | Done | 2026-10-24: self-test 116 of 116. Rendered on the test file with counts matching and no warnings: state 17:1141, architecture 17:1242 and 17:1365, Fernhouse user flow 17:1486, sequence with self and skip messages 16:897, gantt 14:892, ER 11:386 |
| Rules rewritten | In progress | get_figjam reports connector names (edge:, leg:), so read-back matches connectors by name. 2026-10-24: skill sources rewritten for the composed route, flow_check self-test 156 of 156, compose_board self-test 116 of 116. Live probes on 17:1486: setSharedPluginData tags and reads back, pins and sticky legend land inside a zoned board and roll back cleanly |
| Closed | Done | 2026-10-25: all 15 gates pass, composer self-test 468 of 468, rerun boards composed with counts matching, design rubric up on the three types with a before-board (ADR-001) |
<!-- /ANCHOR:log -->
