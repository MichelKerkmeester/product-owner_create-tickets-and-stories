---
title: "Goal: Runtime config and Project optimization"
description: "The durable directive this packet executes against and the criteria that decide when it is done."
trigger_phrases:
  - "runtime and project optimization goal"
importance_tier: "important"
contextType: "planning"
_memory:
  continuity:
    packet_pointer: "product-owner/019-runtime-and-project-optimization"
    last_updated_at: "2026-10-21T18:00:00Z"
    last_updated_by: "claude-code"
    recent_action: "Authored the durable directive"
    next_safe_action: "Start phase 001"
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
# Goal: Runtime config and Project optimization

<!-- SPECKIT_TEMPLATE_SOURCE: goal | v2.2 -->
<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->
<!-- GOAL_AUTHORING: .skilled/skills/sk-doc/sk-create-goal/SKILL.md -->

---

<!-- ANCHOR:directive -->
## 1. DURABLE DIRECTIVE

**Objective:** Make the public Product Owner repo self-sufficient for its MCP tooling, then cut the Claude Project package for kernel size and retrieval without losing a rule, and confirm its behavior against the playbook.

### Decisions

Frozen choices. Changing one is an amendment.

| ID | Decision |
|----|----------|
| D1 | The forked Code Mode server is vendored like mcp-click-up and mcp-figma, with node_modules and dist excluded, as the operator chose on 2026-10-21 |
| D2 | The optimization covers kernel size, then retrieval, then a measured playbook run, as the operator chose on 2026-10-21 |
| D3 | Every rule survives a cut, counted before and after |

<!-- /ANCHOR:directive -->

---

<!-- ANCHOR:binding -->
## 2. BINDING

**Read the child goal before working a phase.** Each is authoritative for its
phase and binds as if written here.

| Phase | Goal document |
|-------|---------------|
| 001 | `001-runtime-config/goal.md` |
| 002 | `002-kernel-size/goal.md` |
| 003 | `003-knowledge-retrieval/goal.md` |
| 004 | `004-behavior-check/goal.md` |
| 005 | `005-claude-project-review/goal.md` |
| 006 | `006-claude-project-fixes/goal.md` |
| 007 | `007-project-ux-and-mode-fixes/goal.md` |
| 008 | `008-routing-research/goal.md` |
| 009 | `009-routing-research-fixes/goal.md` |
| 010 | `010-routing-p0-fixes/goal.md` |
| 011 | `011-project-push-targets/goal.md` |
| 012 | `012-scripts-alignment/goal.md` |
| 013 | `013-push-target-catalog/goal.md` |
| 014 | `014-user-guide-rewrite/goal.md` |
| 015 | `015-live-figma-test/goal.md` |
| 016 | `016-figma-desktop-setup/goal.md` |
| 017 | `017-remove-claude-plugin/goal.md` |

**Precedence.** Decisions above outrank child detail. Child detail outranks any
summary of it. Name a conflict rather than resolving it silently.

**Stop.** Only the criteria below decide done. An evaluator sees the objective
string, not these files.
<!-- /ANCHOR:binding -->

---

<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

- [x] Every child phase folder has a Phase Documentation Map row and a binding row above
- [ ] A clone of the public repo reaches ClickUp and Figma through its own Code Mode config
- [ ] The kernel and the knowledge set are smaller by a recorded amount with every rule kept
- [x] The Project playbook run shows no unexplained regression
- [x] validate.sh --recursive --strict on this folder prints RESULT: PASSED
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
| Packet opened | Done | 2026-10-21 |

### Deviations and findings

| Item | Note |
|------|------|
| None yet | - |
<!-- /ANCHOR:log -->
