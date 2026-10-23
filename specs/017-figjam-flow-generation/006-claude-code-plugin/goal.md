---
title: "Goal: Phase 6: Claude Code plugin"
description: "The durable directive this packet executes against and the criteria that decide when it is done."
trigger_phrases:
  - "claude code plugin goal"
importance_tier: "important"
contextType: "planning"
_memory:
  continuity:
    packet_pointer: "product-owner/017-figjam-flow-generation/006-claude-code-plugin"
    last_updated_at: "2026-10-20T00:00:00Z"
    last_updated_by: "scaffold"
    recent_action: "Authored the durable directive"
    next_safe_action: "Execute against the completion criteria"
    blockers: []
    key_files: []
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "unset"
      parent_session_id: null
    completion_pct: 0
    open_questions: []
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: goal | v2.2 -->
# Goal: Phase 6: Claude Code plugin

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->
<!-- GOAL_AUTHORING: .skilled/skills/sk-doc/sk-create-goal/SKILL.md -->

---

<!-- ANCHOR:directive -->
## 1. DURABLE DIRECTIVE

**Objective:** Package the Product Owner hub as a skills-only Claude Code plugin on the Media Editor build pattern, with no bin folder and no MCP server entry.

### Decisions

Frozen choices. Changing one is an amendment.

| ID | Decision |
|----|----------|
| D1 | Skills only: no bin/ folder and no MCP server entry. A bin shim is added later only if 002 shows fj needs one (operator, 2026-10-20). |

<!-- /ANCHOR:directive -->

---


<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

- [ ] claude plugin validate exits 0 on the built plugin
- [ ] Two consecutive builds produce identical hash trees
- [ ] A planted divergence and a planted symlink each make the build fail
- [ ] A claude --plugin-dir session lists the Product Owner skill and routes the Flow command to Flow Mode
- [ ] The built plugin has no bin/ folder and no mcpServers entry
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
| Phase opened | Pending | |

### Deviations and findings

| Item | Note |
|------|------|
| None yet | |
<!-- /ANCHOR:log -->
