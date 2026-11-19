---
title: "Feature Specification: Vendored browser packets for the ClickUp routines"
description: "The Aside and Chrome DevTools packets are vendored into Product Owner beside mcp-click-up, so the gap pass and columns routine carry their browser setup in this repository."
trigger_phrases:
  - "vendored browser packets for the clickup routines"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.4 -->
# Feature Specification: Vendored browser packets for the ClickUp routines

<!-- SPECKIT_LEVEL: 1 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 1 |
| **Priority** | P1 |
| **Status** | Complete |
| **Created** | 2026-11-10 |
| **Branch** | `main` |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
The ClickUp gap pass and columns routine drive the browser through the `aside` and `chrome_devtools_live` manuals, but their packets lived only in Skilled. A clone of Product Owner had the manuals in `.utcp_config.json` and none of the setup or troubleshooting behind them.

### Purpose
Product Owner carries both browser packets, kept in step by `vendor-sync.py`, and points to them where the ClickUp routines use the browser.
<!-- /ANCHOR:problem -->

<!-- ANCHOR:measured-behavior -->
### Measured Behavior
```text
Before the change:
  vendor.json held mcp-figma, mcp-click-up, mcp-code-mode, code-mode-launcher, mermaid-extract
After the pull:
  mcp-aside-devtools: in step at 6a619da8ed..., 74 files
  mcp-chrome-devtools: in step at a58f92208c..., 100 files
  check_hub.py first reported both as packet folders missing from mode-registry.json
```
<!-- /ANCHOR:measured-behavior -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- Add both packets to `vendor.json` and pull them
- List both as repository paths in the `repo-root-hub` extension, the same way `mcp-code-mode` is listed
- Name them in `AGENTS.md`, the hub `SKILL.md` and the README

### Out of Scope
- Registering them as routable hub modes
- Any edit inside the vendored copies

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| `vendor.json`, `mcp-aside-devtools/`, `mcp-chrome-devtools/` | Modify and Create | Vendored copies |
| `mode-registry.json` | Modify | Repository paths and the vendored-packets description |
| `AGENTS.md`, `SKILL.md`, `README.md` | Modify | Name the packets |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-001 | Both packets are in step with upstream | `vendor-sync.py status` prints `in step` for both |
| REQ-002 | The hub accepts them as repository paths | `python3 benchmark/gates/check_hub.py` prints `PASSED` |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-003 | The change adds no gate failure | `run_gates.sh` fails only vendor sync on `mcp-code-mode` |
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: A clone of Product Owner holds both browser packets
- **SC-002**: `AGENTS.md` names them where the ClickUp routines need the browser
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Risk | Upstream moves on | Low | `vendor-sync.py status` reports drift in the gate run |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:questions -->
## 7. OPEN QUESTIONS

- Should the two packets become routable hub modes? Left as repository paths until a request needs them routed
<!-- /ANCHOR:questions -->

---
