---
title: "Feature Specification: Runtime config and Project optimization"
description: "Make the public Product Owner repo self-sufficient for its MCP tooling, then cut the Claude Project package for kernel size and retrieval and check the result against the playbook."
trigger_phrases:
  - "runtime and project optimization phase parent spec"
importance_tier: "important"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "019-runtime-and-project-optimization"
    last_updated_at: "2026-10-21T18:00:00Z"
    last_updated_by: "claude-code"
    recent_action: "Opened the packet"
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
<!-- SPECKIT_TEMPLATE_SOURCE: phase-parent-spec | v2.2 -->

<!-- SPECKIT_LEVEL: 2 -->

# Feature Specification: Runtime config and Project optimization

---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 2 |
| **Priority** | P1 |
| **Status** | In Progress |
| **Created** | 2026-10-21 |
| **Branch** | `main` |
| **Parent Spec** | None |
| **Parent Packet** | product-owner |
| **Predecessor** | 018-product-owner-deep-review |
| **Successor** | None |
| **Handoff Criteria** | Each child meets its acceptance criteria and the gates pass from the final tree |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
The public Product Owner repository vendors mcp-click-up and mcp-figma but carries no runtime config for them, and its Code Mode launcher exists only in the private .skilled tree, so a clone cannot reach ClickUp or Figma. Its Claude Project package costs 75 KB of kernel on every turn, 27 KB of it Router Code a Project never runs, beside 62 knowledge files that total 700 KB.

### Purpose
Make the public repo self-sufficient for its MCP tooling, then shrink the Project package where it costs the most and confirm against the playbook that its behavior holds.

> **Phase-parent note:** This spec.md and goal.md are the only authored documents at this level. Plans, tasks, checklists and decisions live in the child phase folders listed below.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- Runtime configs, the vendored Code Mode server and the credential key list
- The kernel, the knowledge set and a Project playbook run

### Out of Scope
- Commits and pushes without the operator's go-ahead

### Files to Change

| File Path | Change Type | Phase | Description |
|-----------|-------------|-------|-------------|
| .utcp_config.json, .mcp.json, opencode.json, .env.example, mcp-code-mode/, vendor.json | Create, Modify | 001 | Runtime config |
| claude project/Custom Instructions.md | Modify | 002 | Kernel size |
| claude project/knowledge/ | Modify | 003 | Retrieval |
| benchmark/reports/ | Create | 004 | The behavior run |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:phase-map -->
## PHASE DOCUMENTATION MAP

> Each phase is an independently executable child spec folder.

| Phase | Folder | Focus | Status |
|-------|--------|-------|--------|
| 1 | 001-runtime-config/ | Vendor the forked Code Mode server and add the runtime configs and credential keys | Complete |
| 2 | 002-kernel-size/ | Cut the kernel's per-turn cost without losing a rule | Complete |
| 3 | 003-knowledge-retrieval/ | Remove duplicated text across the knowledge files | Complete |
| 4 | 004-behavior-check/ | Run the Project playbook against the optimized package and fix what fails | Complete |
| 5 | 005-claude-project-review/ | Review the Claude Project packaging and its connector setup in three DeepSeek iterations | Complete |
| 6 | 006-claude-project-fixes/ | Write the Claude Desktop user guide and fix every 005 finding | Complete |
| 7 | 007-project-ux-and-mode-fixes/ | Fix the Opus UX and mode review findings | Complete |
| 8 | 008-routing-research/ | Ten DeepSeek iterations on routing, mode links, README currency, dead files and sk-code-skilled alignment | Complete |
| 9 | 009-routing-research-fixes/ | Fix every P1 and P2 finding of the 008 research | Complete |
| 10 | 010-routing-p0-fixes/ | Make hub-router.json the stage-one authority and fix every P0 finding | Complete |
| 11 | 011-project-push-targets/ | Read ClickUp push targets from a private Knowledge file in the Project | Complete |
| 12 | 012-scripts-alignment/ | Align scripts/ with sk-code-skilled and add code READMEs | Complete |
| 13 | 013-push-target-catalog/ | Named push-target catalog for the Project and the skill | Complete |
| 14 | 014-user-guide-rewrite/ | USER-GUIDE rewritten to the sk-doc install guide contract | Complete |
| 15 | 015-live-figma-test/ | Live Figma playbook run on DeepSeek V4.1 Flash max | In Progress |
| 16 | 016-figma-desktop-setup/ | Figma Desktop route setup help | Complete |

### Phase Transition Rules

- Each phase MUST pass `validate.sh` independently
- The phases run in order, since each later one measures the state the one before leaves

### Phase Handoff Criteria

| From | To | Criteria | Verification |
|------|-----|----------|--------------|
| 018-product-owner-deep-review | 001 | The operator asked for the runtime configs and the optimization on 2026-10-21 | This spec |
<!-- /ANCHOR:phase-map -->

---

<!-- ANCHOR:questions -->
## 4. OPEN QUESTIONS

- None.
<!-- /ANCHOR:questions -->

---

## RELATED DOCUMENTS

- **Phase children**: See sub-folders `[0-9][0-9][0-9]-*/`
