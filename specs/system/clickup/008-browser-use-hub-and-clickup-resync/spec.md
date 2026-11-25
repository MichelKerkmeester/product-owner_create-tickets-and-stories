---
title: "Feature Specification: Browser Use hub and ClickUp resync"
description: "Product Owner vendors the Skilled mcp-browser-use hub in place of the two browser packets and resyncs mcp-click-up, so the ClickUp page routines name browser packets that exist in this repository."
trigger_phrases:
  - "browser use hub and clickup resync"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.4 -->
# Feature Specification: Browser Use hub and ClickUp resync

<!-- SPECKIT_LEVEL: 1 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 1 |
| **Priority** | P1 |
| **Status** | Complete |
| **Created** | 2026-11-24 |
| **Branch** | `main` |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
Skilled moved the Aside and Chrome DevTools packets out of `mcp-tooling` into a dedicated `mcp-browser-use` hub, which also adds Bladebro. The two `vendor.json` entries for the browser packets now point at upstream paths that no longer exist, and the latest `mcp-click-up` names the browsers as `mcp-browser-use/mcp-aside-devtools` and `mcp-browser-use/mcp-chrome-devtools`, folders this repository does not have.

### Purpose
Product Owner vendors the whole `mcp-browser-use` hub at its root in place of the two browser packets, resyncs `mcp-click-up`, `mcp-figma` and `mcp-code-mode` to the latest Skilled versions and names the hub wherever the repository describes its vendored packets.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- Replace the `mcp-aside-devtools` and `mcp-chrome-devtools` entries in `vendor.json` with one `mcp-browser-use` entry that excludes `graph-metadata.json`, and delete both old folders
- Pull `mcp-browser-use` and sync `mcp-click-up`, `mcp-figma` and `mcp-code-mode`
- List `mcp-browser-use` as a repository path in the `repo-root-hub` extension, and update the hub `SKILL.md`, `README.md`, `scripts/README.md` and `AGENTS.md` where they name the browser packets
- A patch version bump and changelog entry for the hub

### Out of Scope
- Registering `mcp-browser-use` as a routable hub mode
- Any edit inside a vendored copy
- Registering a Bladebro manual in `.utcp_config.json`
- Changelogs, earlier specs, benchmark reports and `SYNC.md` history that name the old packets
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-001 | Every vendored copy is in step with upstream | `vendor-sync.py status` names no entry out of step |
| REQ-002 | The hub accepts `mcp-browser-use` as a repository path | `python3 benchmark/gates/check_hub.py` prints `PASSED` |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-003 | The change adds no gate failure | `run_gates.sh` fails no gate that passed in the baseline |
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: Every browser packet name in the vendored `mcp-click-up` resolves to a folder in this repository
- **SC-002**: No live Product Owner file names the removed `mcp-aside-devtools/` or `mcp-chrome-devtools/` root folders
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Risk | Another session holds uncommitted edits to `SYNC.md`, the format validator and two voice cards | Medium | Leave those files untouched and compare gates against a baseline |
| Risk | The deletion removes about 176 tracked files | Low | The files return as the same content under `mcp-browser-use/` |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:questions -->
## 7. OPEN QUESTIONS

- None. `mcp-code-mode` synced here, because it was the last entry out of step
<!-- /ANCHOR:questions -->
