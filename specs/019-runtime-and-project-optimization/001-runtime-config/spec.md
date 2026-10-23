---
title: "Feature Specification: Phase 1: Runtime config in the public repo"
description: "The Product Owner repository vendors mcp-click-up and mcp-figma, but it carries no .utcp_config.json, no .mcp.json and no opencode.json, and its Code Mode launcher lives only in the private .skilled tree, so a clone of the public repo cannot reach ClickUp or Figma through Code Mode. Make the public repo self-sufficient for its MCP tooling: vendor the forked Code Mode server, add the runtime configs and list every credential key in .env.example."
trigger_phrases:
  - "runtime config"
importance_tier: "normal"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "019-runtime-and-project-optimization/001-runtime-config"
    last_updated_at: "2026-10-21T18:00:00Z"
    last_updated_by: "claude-code"
    recent_action: "Opened the phase"
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
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.2 -->
# Feature Specification: Phase 1: Runtime config in the public repo

<!-- SPECKIT_LEVEL: 2 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 2 |
| **Priority** | P1 |
| **Status** | Complete |
| **Created** | 2026-10-21 |
| **Branch** | `main` |
| **Parent Spec** | ../spec.md |
| **Phase** | 1 of 16 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
The Product Owner repository vendors mcp-click-up and mcp-figma, but it carries no .utcp_config.json, no .mcp.json and no opencode.json, and its Code Mode launcher lives only in the private .skilled tree, so a clone of the public repo cannot reach ClickUp or Figma through Code Mode.

### Purpose
Make the public repo self-sufficient for its MCP tooling: vendor the forked Code Mode server, add the runtime configs and list every credential key in .env.example.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- Vendoring mcp-code-mode through vendor.json, with a per-package exclude so node_modules and dist stay out
- .utcp_config.json with the clickup_official and figma manuals
- .mcp.json and opencode.json that start the vendored server
- .env.example keys, .gitignore lines and the install steps in README.md

### Out of Scope
- Manuals Product Owner does not use, such as Notion, Webflow or GitHub
- Pinning the mcp-remote and figma-developer-mcp launch arguments
- Commits and pushes

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| vendor.json, scripts/vendor-sync.py, scripts/tests/test_vendor_sync.py | Modify | The third vendored packet and the exclude field |
| mcp-code-mode/ | Modify | Pulled from upstream |
| .utcp_config.json, .mcp.json, opencode.json | Modify | Runtime configs |
| .env.example, .gitignore | Modify | Credential keys and ignored build output |
| README.md, scripts/build-plugin.py | Modify | Install steps and the plugin's unshipped list |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | Vendor mcp-code-mode with node_modules and dist excluded |
| REQ-002 | Add .utcp_config.json with only the manuals Product Owner uses |
| REQ-003 | Add .mcp.json and opencode.json that start the vendored server with no .skilled path |
| REQ-004 | List every key the configs read in .env.example and document the one-time build |

> Acceptance criteria for these requirements live in `acceptance-criteria.md`,
> which is the document that decides whether this packet may close.
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: Every requirement in scope is met or recorded with the reason it was not.
- **SC-002**: The gates that own the changed files pass from the final state.
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Dependency | The upstream Code Mode server at its last commit | Order of work | Follow tasks.md |
| Risk | A change alters behaviour a gate or mirror relies on | Med | Rerun the owning gates after each batch |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:nfr -->
## L2: NON-FUNCTIONAL REQUIREMENTS

### Security
- **NFR-S01**: No secrets, board URLs or Barter flows in any changed file.

### Reliability
- **NFR-R01**: Each change is a working-tree edit to a tracked file, reverted with `git checkout -- <path>`.
<!-- /ANCHOR:nfr -->

---

<!-- ANCHOR:edge-cases -->
## L2: EDGE CASES

### Error Scenarios
- A requirement turns out not to fit when its site is opened: it is recorded as not met, with the reason.

### State Transitions
- Partial batch: tasks.md shows which tasks are done.
<!-- /ANCHOR:edge-cases -->

---

<!-- ANCHOR:complexity -->
## L2: COMPLEXITY ASSESSMENT

| Dimension | Score | Notes |
|-----------|-------|-------|
| Scope | 14/25 | Several files across one packet tree |
| Risk | 8/25 | Docs and scripts, reversible |
| Research | 4/20 | Measured before the phase opened |
| **Total** | **26/70** | **Level 2** |
<!-- /ANCHOR:complexity -->

---

<!-- ANCHOR:questions -->
## 10. OPEN QUESTIONS

- None.
<!-- /ANCHOR:questions -->
