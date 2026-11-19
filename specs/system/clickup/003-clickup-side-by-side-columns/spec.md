---
title: "Feature Specification: ClickUp side-by-side screenshot columns"
description: "A Product Owner doc page push sets each DEV and FIGMA screenshot pair in a ClickUp columns block, built in the editor by the vendored mcp-click-up columns routine."
trigger_phrases:
  - "clickup side-by-side screenshot columns"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.4 -->
# Feature Specification: ClickUp side-by-side screenshot columns

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
Design feedback compares a built screen with its Figma frame. ClickUp shows that best in a `/Columns` block, but a doc page takes only `text/md` and `text/plain`, and neither has a column. A pushed pair could only sit one above the other.

### Purpose
A doc page push shows each screenshot pair side by side, and a page that holds columns is never wiped by a later `replace`.
<!-- /ANCHOR:problem -->

<!-- ANCHOR:measured-behavior -->
### Measured Behavior
```text
Live on 2026-11-10:
  a columns block is .ql-layout-row-container with blocks carrying data-layout="<row>_<col>" and data-layout-width="0.50"
  the text/md read-back flattens it into stacked lines
  no Quill instance on window, so formatLine is unavailable
  pasted HTML in that shape over a [[COLS-1]] line builds a row that survives a reload
  a local PNG pasted as a file lands in its column as a clickup-attachments image
  the documented program: 2 pairs, 2 rows of 2 columns with 1 image each, 0 leftovers
```
<!-- /ANCHOR:measured-behavior -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- Add the columns routine and the `replace` caveat to the upstream `mcp-click-up` packet and pull it here
- Add two Section 7 Push Targets bullets to `sk-product-owner/SKILL.md`

### Out of Scope
- The claude.ai Project, which pushes through its own connector and has no browser
- Task descriptions, which have no columns

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| `sk-product-owner/SKILL.md` | Modify | Two Push Targets bullets, version 1.2.14.0 |
| `mcp-click-up/`, `vendor.json` | Modify | Vendored pull of upstream 1.2.18.0 |
| Hub version files, both READMEs, two changelogs, `SYNC.md` | Modify and Create | Hub 1.0.26.0 |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-001 | Section 7 names the columns routine and the `replace` caveat | `rg -n 'COLS-n|never rewritten with' sk-product-owner/SKILL.md` prints two lines |
| REQ-002 | The vendored copy carries the routine | `rg -n 'Side-by-side columns on a doc page' mcp-click-up/references/mcp-tools.md` prints one line |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-003 | The change adds no gate failure | `run_gates.sh` fails only vendor sync on `mcp-code-mode` |
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: A pushed pair shows as two columns after a reload
- **SC-002**: The routine reports no leftover placeholder or marker
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Risk | ClickUp changes its editor markup | Med | The routine verifies after a reload and reports leftovers, so a broken paste shows up |
| Dependency | Skilled commit `4834f91ff3` | The pull pins it | Pushed before the pull |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:questions -->
## 7. OPEN QUESTIONS

- Does a ClickUp task description support columns through any surface? Not measured
<!-- /ANCHOR:questions -->

---
