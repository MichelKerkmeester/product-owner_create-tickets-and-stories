---
title: "Goal: Phase 6: Claude Project review fixes and user guide"
description: "The durable directive this packet executes against and the criteria that decide when it is done."
trigger_phrases:
  - "claude project fixes goal"
importance_tier: "important"
contextType: "planning"
_memory:
  continuity:
    packet_pointer: "product-owner/019-runtime-and-project-optimization/006-claude-project-fixes"
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
# Goal: Phase 6: Claude Project review fixes and user guide

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->
<!-- GOAL_AUTHORING: .skilled/skills/sk-doc/sk-create-goal/SKILL.md -->

---

<!-- ANCHOR:directive -->
## 1. DURABLE DIRECTIVE

**Objective:** Write a user guide for Claude Desktop in Media Editor's shape and fix every finding at its source.

### Decisions

Frozen choices. Changing one is an amendment.

| ID | Decision |
|----|----------|
| D1 | The operator chose on 2026-10-21 to fix every finding of the 005 review and to add a Claude Desktop user guide |
| D2 | Vendored packets are never edited here, so a finding inside one is fixed upstream or recorded |
| D3 | No commit or push without the operator's go-ahead |

<!-- /ANCHOR:directive -->

---

<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

- [ ] USER-GUIDE.md exists and README.md links it
- [ ] Every 005 finding is fixed or recorded
- [ ] validate.sh --strict on 006-claude-project-fixes prints RESULT: PASSED
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
<!-- /ANCHOR:log -->
