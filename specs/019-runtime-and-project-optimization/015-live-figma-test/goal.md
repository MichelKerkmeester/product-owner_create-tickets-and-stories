---
title: "Goal: Phase 15: live Figma playbook run on DeepSeek V4.1 Flash max"
description: "The durable directive this packet executes against and the criteria that decide when it is done."
trigger_phrases:
  - "live figma test goal"
importance_tier: "important"
contextType: "planning"
_memory:
  continuity:
    packet_pointer: "product-owner/019-runtime-and-project-optimization/015-live-figma-test"
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
# Goal: Phase 15: live Figma playbook run on DeepSeek V4.1 Flash max

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->
<!-- GOAL_AUTHORING: .skilled/skills/sk-doc/sk-create-goal/SKILL.md -->

---

<!-- ANCHOR:directive -->
## 1. DURABLE DIRECTIVE

**Objective:** Run the skill-side Flow and FigJam scenarios live on fresh DeepSeek V4.1 Flash sessions at max thinking, with fj writes into a throwaway FigJam board, and grade each reply.

### Decisions

Frozen choices. Changing one is an amendment.

| ID | Decision |
|----|----------|
| D1 | The operator asked on 2026-10-21 for a live Figma playbook run on DeepSeek V4.1 Flash max |
| D2 | The operator asked for live Figma testing with a fresh DeepSeek on 2026-10-22, and chose to try the hosted route first |
| D3 | No commit or push without the operator's go-ahead |

<!-- /ANCHOR:directive -->

---

<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

- [ ] Every selected scenario has a verdict or a named SKIP
- [ ] The README states the hosted-route refusal
- [ ] validate.sh --strict on 015-live-figma-test prints RESULT: PASSED
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
