---
title: "Feature Specification: ClickUp doc divider spacing in the Product Owner push"
description: "Every Doc artifact uses `* * *` dividers, and the ClickUp MCP writes each one with an empty line under it on a new page. The Product Owner push said nothing about it, and its vendored mcp-click-up copy predates the upstream fix."
trigger_phrases:
  - "clickup doc divider spacing"
  - "clickup doc divider spacing in the product owner push"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.4 -->
# Feature Specification: ClickUp doc divider spacing in the Product Owner push

<!-- SPECKIT_LEVEL: 1 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 1 |
| **Priority** | P1 |
| **Status** | Complete |
| **Created** | 2026-11-05 |
| **Branch** | `main` |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
Every new Doc artifact uses `* * *` dividers, and a doc push lands as a new page through `clickup_create_document_page`. The ClickUp MCP writes every divider on such a page with an empty line under it, so each pushed Doc shows a double gap under each divider while its markdown read-back looks clean. The Section 7 handoff did not mention the gap, and the vendored `mcp-click-up/` copy sits at 1.2.8.0, two releases behind the upstream packet that now documents the fix.

### Purpose
A Product Owner doc push tells the user about the divider gap and offers the editor pass, and the vendored `mcp-click-up/` copy carries the upstream steps that pass follows.
<!-- /ANCHOR:problem -->

<!-- ANCHOR:measured-behavior -->
### Measured Behavior
```text
Measured on the clickup_official Code Mode manual on 2026-11-05, recorded in full in the Skilled packet
specs/mcp-tooling/026-clickup-doc-divider-spacing/spec.md:
  create_document_page with "#### Basics\n* * *\n*   ..." reads back in "text/plain" as "Basics\n \nWho: X"
  a page built in the ClickUp editor reads back as "Basics\n Who gets it"
  both read back the same in "text/md"

python3 scripts/vendor-sync.py status --package mcp-click-up
  mcp-click-up: upstream-ahead, 8 change(s)
  upstream added changelog/v1.2.10.0.md
  upstream added changelog/v1.2.9.0.md
  upstream changed references/mcp-tools.md
  ...
python3 scripts/vendor-sync.py pull --package mcp-click-up
  mcp-click-up: pull refused, upstream has uncommitted changes; commit them first
```
<!-- /ANCHOR:measured-behavior -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- Add two Push Targets bullets to `sk-product-owner/SKILL.md` Section 7 that name the gap and offer the editor pass
- Bump `sk-product-owner` to 1.2.7.0 with a changelog entry, and record the change in `SYNC.md`
- Pull the vendored `mcp-click-up/` copy to upstream 1.2.10.0 once the Skilled packet is committed
- Move the hub to 1.0.19.0 with a release note and the README version row, after the pull

### Out of Scope
- The claude.ai Project kernel - the gap was not measured on the connector a Project pushes through, and a Project has no browser for the editor pass
- `AGENTS.md` - its ClickUp Handoff already defers the mechanics to `mcp-click-up/SKILL.md`, which now carries the warning
- The upstream `mcp-click-up` text - the Skilled packet owns it

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| `sk-product-owner/SKILL.md` | Modify | Two Section 7 bullets, version 1.2.7.0 |
| `sk-product-owner/changelog/v1.2.7.0.md` | Create | Release note |
| `SYNC.md` | Modify | Dated maintenance note, no Project change |
| `mcp-click-up/` and `vendor.json` | Modify | Vendored pull to upstream 1.2.10.0 |
| `SKILL.md`, `hub-router.json`, `mode-registry.json`, `description.json`, `README.md`, `changelog/v1.0.19.0.md` | Modify and Create | Hub release 1.0.19.0 |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-001 | Section 7 names the gap and offers the editor pass behind its own yes | `rg -n 'empty line under every' sk-product-owner/SKILL.md` prints one line and `rg -n 'waits for its own yes' sk-product-owner/SKILL.md` prints one line |
| REQ-002 | The vendored copy matches upstream | `python3 scripts/vendor-sync.py status --package mcp-click-up` exits 0 |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-003 | The change adds no gate failure | `bash benchmark/gates/run_gates.sh` fails no gate beyond the four that fail without this change |
| REQ-004 | The release numbers agree | Hub 1.0.19.0 in `SKILL.md`, the three hub JSON files and the README row, and `sk-product-owner` 1.2.7.0 in its `SKILL.md` and the README row |
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: A doc push reply names the divider gap and offers the editor pass
- **SC-002**: `vendor-sync.py status --package mcp-click-up` reports the copy in sync with upstream 1.2.10.0
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Dependency | The Skilled packet `specs/mcp-tooling/026-clickup-doc-divider-spacing` must be committed | The vendored pull stays refused | The pull and the hub release wait for that commit, and nothing claims them before it |
| Risk | The claude.ai connector shows the same gap | Med | `SYNC.md` records that the connector was not checked, so a later measurement can add the kernel line |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:questions -->
## 7. OPEN QUESTIONS

- Does the claude.ai ClickUp connector write dividers with the same gap? Not measured, and the kernel stays unchanged until it is
<!-- /ANCHOR:questions -->

---
