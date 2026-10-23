---
title: "Goal: Phase 13: named push-target catalog for the Project and the skill"
description: "The durable directive this packet executes against and the criteria that decide when it is done."
trigger_phrases:
  - "push target catalog goal"
importance_tier: "important"
contextType: "planning"
_memory:
  continuity:
    packet_pointer: "product-owner/019-runtime-and-project-optimization/013-push-target-catalog"
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
# Goal: Phase 13: named push-target catalog for the Project and the skill

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->
<!-- GOAL_AUTHORING: .skilled/skills/sk-doc/sk-create-goal/SKILL.md -->

---

<!-- ANCHOR:directive -->
## 1. DURABLE DIRECTIVE

**Objective:** Replace the four per-kind slots with one local named catalog of lists and docs, read by the skill from claude project/local/ and uploaded to the Project, where the offer names the list or doc that fits and documents become a new page in the named doc.

### Decisions

Frozen choices. Changing one is an amendment.

| ID | Decision |
|----|----------|
| D1 | The operator asked on 2026-10-21 for a named push-target catalog shared by the Project and the skill |
| D2 | The operator chose a named catalog over one default per kind, and new pages in a named doc over separate private docs, on 2026-10-22 |
| D3 | No commit or push without the operator's go-ahead |

<!-- /ANCHOR:directive -->

---

<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

- [ ] Gates, differential, format gate and residency pass
- [ ] git grep finds no operator ClickUp id
- [ ] validate.sh --strict on 013-push-target-catalog prints RESULT: PASSED
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
