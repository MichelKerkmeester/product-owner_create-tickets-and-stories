---
title: "Goal: Phase 15: FigJam rebuild"
description: "The durable directive this packet executes against and the criteria that decide when it is done."
trigger_phrases:
  - "figjam rebuild goal"
importance_tier: "important"
contextType: "planning"
_memory:
  continuity:
    packet_pointer: "product-owner/017-figjam-flow-generation/015-figjam-rebuild"
    last_updated_at: "2026-10-20T20:00:00Z"
    last_updated_by: "claude-code"
    recent_action: "Met every completion criterion"
    next_safe_action: "Commit on the operator's go-ahead"
    blockers: []
    key_files: []
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "1004bf13-7863-4447-a63e-6ad2f5fcfd86"
      parent_session_id: null
    completion_pct: 100
    open_questions: []
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: goal | v2.2 -->
# Goal: Phase 15: FigJam rebuild

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->
<!-- GOAL_AUTHORING: .skilled/skills/sk-doc/sk-create-goal/SKILL.md -->

---

<!-- ANCHOR:directive -->
## 1. DURABLE DIRECTIVE

**Objective:** Rebuild sk-create-figjam so it draws every diagram type Figma's generate_diagram supports, with sk-design-diagram's intake, style, quality and derivation rules and the researched FigJam skills translated to FigJam, and mirror it into the Claude Project.

### Decisions

Frozen choices. Changing one is an amendment.

| ID | Decision |
|----|----------|
| D1 | Seven types: user flow, process, architecture, sequence, state, ER and gantt, on the operator's choice of 2026-10-20 |
| D2 | Examples use fictional companies only, and no Barter flow, screenshot or board URL enters the public repository |
| D3 | The Project is mirrored by the SYNC.md parity method, with the kernel staying at the unreleased v1.2.2 |

<!-- /ANCHOR:directive -->

---

<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

- [x] Every type has a reference, a template past the user flow and a worked example that passes flow_check.py
- [x] flow_check.py --self-test passes every planted defect, template, example and Project mirror
- [x] parent-skill-check.cjs and validate_skill_package.py --strict pass on the root and its four packets
- [x] run_gates.sh, the format gates, reference parity, the playbook validators and the plugin build pass
- [x] The Sync Loop parity and residency gates pass in a scratch clone
- [x] validate.sh --strict on 015-figjam-rebuild prints RESULT: PASSED
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
| Packet rebuilt and checked | Done | 2026-10-20, self-test 148 of 148, parent-skill-check 0 failures 0 warnings |
| Gates | Done | run_gates.sh all 12 pass, plugin validates, scratch clone run_parity.sh 62 of 62 and run_residency.sh pass |
<!-- /ANCHOR:log -->
