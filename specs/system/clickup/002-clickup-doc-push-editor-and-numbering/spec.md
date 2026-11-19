---
title: "Feature Specification: ClickUp doc push editor and numbering fixes"
description: "A Product Owner task pushed to a ClickUp doc showed every requirement title as 1., literal checkbox brackets and divider gaps the gap pass reported as removed."
trigger_phrases:
  - "clickup doc push editor and numbering"
  - "numbered task title clickup"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.4 -->
# Feature Specification: ClickUp doc push editor and numbering fixes

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
A task pushed to a private ClickUp doc on 2026-11-10 showed three defects. The divider gap pass reported no gaps while the plain-text read-back still counted 60, because a doc page now has a second `.ql-editor` for its title and the program took the first one. Every `- []` checkbox arrived as literal `\[\]` text. Every requirement title read `1.`, because ClickUp reads `1.  **{Title}**` as a one-item numbered list and the divider after it ends that list.

### Purpose
A numbered task title keeps its number in ClickUp, and the vendored `mcp-click-up/` copy carries a gap pass that edits the page body and a push shape that names both spellings.
<!-- /ANCHOR:problem -->

<!-- ANCHOR:measured-behavior -->
### Measured Behavior
```text
Live on page 2kyq4d0p-122975 on 2026-11-10:
  gap pass with querySelector(".ql-editor"): presses 0, left 0, plain-text hits 60
  body editor probe: H2.ql-heading, HR.ql-divider, DIV.ql-block with one BR
  "**1. X**", "2\. **X**" and "3.<nbsp>**X**" all render as DIV.ql-block, no list
  "2\. **X**" reads back as "2\. **X**", the other two read back changed
  gap pass with the largest .ql-editor: presses 60, plain-text hits 0, text unchanged
```
<!-- /ANCHOR:measured-behavior -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- Write numbered task titles as `1\. **{Title}**` in the task templates, Task Mode, three task examples and the README, and in their five Knowledge mirrors
- Fix the gap pass selector and name the two spellings in the upstream `mcp-click-up` packet, then pull it here
- Release the hub at 1.0.25.0 and `sk-product-owner` at 1.2.13.0, and record the change in `SYNC.md`

### Out of Scope
- The claude.ai Project kernel, which names no task title shape
- The Story acceptance criteria, which already use `1 ) **{Title}**`
- The `mcp-code-mode` vendor drift, which predates this change

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| `sk-product-owner/assets/task-templates.md`, `references/task-mode.md`, `README.md` and three task examples | Modify | Escaped title form and the rule |
| Five `claude project/knowledge/` task files | Modify | Same edit, mirrored by hand |
| `mcp-click-up/`, `vendor.json` | Modify | Vendored pull of upstream 1.2.17.0 |
| `SKILL.md`, three hub JSON files, `README.md`, `claude project/README.md`, two changelogs, `SYNC.md` | Modify and Create | Hub 1.0.25.0 and `sk-product-owner` 1.2.13.0 |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-001 | No task source or mirror writes the list-forming title | `rg -n '^ *([0-9]+|\{[a-z]+\})\.  \*\*' sk-product-owner "claude project"` prints nothing |
| REQ-002 | The vendored copy matches upstream | `vendor-sync.py status` reports `mcp-click-up` in step at the upstream commit |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-003 | The change adds no gate failure | `run_gates.sh` fails only the vendor sync gate that already failed on `mcp-code-mode` |
| REQ-004 | The release numbers agree | Hub 1.0.25.0 in `SKILL.md`, the three hub JSON files and the README, and `sk-product-owner` 1.2.13.0 in its `SKILL.md` and both READMEs |
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: A pushed task page shows its requirement titles numbered in order
- **SC-002**: The gap pass removes every divider gap on a doc page and leaves the text unchanged
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Dependency | The Skilled commit `16db86bc96` | The vendored pull pins it | Pushed to origin before the pull |
| Risk | Another markdown viewer shows the backslash | Low | CommonMark renders `1\.` as `1.`, and ClickUp reads it back exactly |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:questions -->
## 7. OPEN QUESTIONS

- Does a ClickUp task description, not a doc page, form the same one-item list? Not measured, and the template change covers both
<!-- /ANCHOR:questions -->

---
