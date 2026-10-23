---
title: "Goal: Phase 14: Hub to root"
description: "The durable directive this packet executes against and the criteria that decide when it is done."
trigger_phrases:
  - "hub to root goal"
importance_tier: "important"
contextType: "planning"
_memory:
  continuity:
    packet_pointer: "product-owner/017-figjam-flow-generation/014-hub-to-root"
    last_updated_at: "2026-10-20T18:30:00Z"
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
# Goal: Phase 14: Hub to root

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->
<!-- GOAL_AUTHORING: .skilled/skills/sk-doc/sk-create-goal/SKILL.md -->

---

<!-- ANCHOR:directive -->
## 1. DURABLE DIRECTIVE

**Objective:** Move the Product Owner hub back to the repository root, as Moneybird Accountant keeps it, so the skilled checker and validator pass it through the repo-root-hub extension and every gate still passes.

### Decisions

Frozen choices. Changing one is an amendment.

| ID | Decision |
|----|----------|
| D1 | The hub lives at the repository root, on the operator's choice of 2026-10-20 |
| D2 | The hub declares its repository entries in mode-registry.json, and no fixed allowlist exists in the checkers |
| D3 | Nothing inside mcp-figma/ or mcp-click-up/ is edited, and the Claude Project files do not change |

<!-- /ANCHOR:directive -->

---

<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

- [x] parent-skill-check.cjs on the repository root prints 0 failures
- [x] validate_skill_package.py --strict passes on the root and its four packets
- [x] run_gates.sh prints all gates pass, and the plugin build and the playbook validators pass
- [x] The Sync Loop parity and residency gates pass in a scratch clone
- [x] validate.sh --strict on 014-hub-to-root prints RESULT: PASSED
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
| Hub moved and checked | Done | 2026-10-20, parent-skill-check 0 failures 0 warnings, validate_skill_package --strict exit 0 on the root and four packets |
| Gates | Done | run_gates.sh all 12 pass, plugin validates, scratch clone run_parity.sh 39 of 39 and run_residency.sh pass |
<!-- /ANCHOR:log -->
