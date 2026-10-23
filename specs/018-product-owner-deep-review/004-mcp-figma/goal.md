---
title: "Goal: Phase 4: mcp-figma deep review"
description: "The durable directive this packet executes against and the criteria that decide when it is done."
trigger_phrases:
  - "mcp figma deep review goal"
importance_tier: "important"
contextType: "planning"
_memory:
  continuity:
    packet_pointer: "product-owner/018-product-owner-deep-review/004-mcp-figma"
    last_updated_at: "2026-10-21T12:00:00Z"
    last_updated_by: "claude-code"
    recent_action: "Closed the review phase"
    next_safe_action: "The operator chooses which findings to fix"
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
# Goal: Phase 4: mcp-figma deep review

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->
<!-- GOAL_AUTHORING: .skilled/skills/sk-doc/sk-create-goal/SKILL.md -->

---

<!-- ANCHOR:directive -->
## 1. DURABLE DIRECTIVE

**Objective:** Review the vendored mcp-figma packet for correctness, contract drift and stale references, and how the hub uses it, in five DeepSeek iterations, with every P0 and P1 finding checked against its cited line.

### Decisions

Frozen choices. Changing one is an amendment.

| ID | Decision |
|----|----------|
| D1 | Five iterations on DeepSeek V4.1 Flash at max through cli-pi on llmgateway, with convergence stopping off, as the operator asked on 2026-10-21 |
| D2 | The lineage reads only and writes only inside its own directory |
| D3 | No Barter screenshot, Barter flow or board URL enters a prompt or an output |

<!-- /ANCHOR:directive -->

---

<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

- [x] review/lineages/deepseek/deep-review-state.jsonl holds 5 iteration records
- [x] Every P0 and P1 finding has a verdict in implementation-summary.md
- [x] Findings name the upstream skill file to change, since the packet is vendored and never edited here
- [x] validate.sh --strict on 004-mcp-figma prints RESULT: PASSED
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
| Phase opened | Done | 2026-10-21, a child of 018-product-owner-deep-review |
| Review run | Done | 5 iterations, 0 P0, 6 P1, 11 P2, 6 of 6 P1 holding on the cited line |
<!-- /ANCHOR:log -->
