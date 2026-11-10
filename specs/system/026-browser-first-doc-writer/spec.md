---
title: "Feature Specification: Browser-first ClickUp doc page writer"
description: "A new ClickUp doc page gets its body from one editor paste, so dividers stay tight, numbers and Mark-as-done lines turn gray and screenshot pairs sit side by side."
trigger_phrases:
  - "browser-first clickup doc page writer"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.4 -->
# Feature Specification: Browser-first ClickUp doc page writer

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
A doc page written as markdown through the ClickUp MCP showed an empty line under every divider and kept no colour. The team sets numbered titles with a gray, regular-weight number and a bold title, and Story criteria with a gray italic Mark-as-done line. Neither survives markdown. Every push needed a gap pass afterwards, and the gap pass picked the wrong editor on a short page.

### Purpose
`mcp-click-up` gains a browser-first page writer that pastes the whole body into the editor, and Product Owner uses it as the default doc page push, with the markdown write and gap pass as the fallback.
<!-- /ANCHOR:problem -->

<!-- ANCHOR:measured-behavior -->
### Measured Behavior
```text
Markdown write (before):
  every divider showed an empty line under it, colour lost
Browser-first write, scratch page 2kyq4d0p-123315 (after reload):
  dividers 11, gaps 0, columns [[1,1]], gray runs 5, checklist items 6, indented 2, leftovers none
  import diff: none once images are compared by position
Live Barter tasks DEV-4495, DEV-4496, DEV-4499, DEV-4501:
  numbered titles carry <span class="ql-text-color ql-color-grey">N. </span><strong>Title</strong>
```
<!-- /ANCHOR:measured-behavior -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- A markdown-to-editor-HTML page writer in `mcp-click-up/references/mcp-tools.md` section 8
- The body editor selector fix in the gap pass and columns programs
- Product Owner section 7 and `AGENTS.md` make the writer the default doc page push

### Out of Scope
- Task descriptions, which stay on `markdown_description`
- Rewriting a page that already exists

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| Skilled `mcp-click-up/references/mcp-tools.md`, `SKILL.md`, changelog | Modify and Create | Page writer, selector fix, release v1.2.19.0 |
| Skilled `mcp-tooling` hub version files and changelog | Modify and Create | Release v1.9.11.0 |
| `mcp-click-up/` vendored copy, `vendor.json` | Modify | Pulled from upstream |
| `sk-product-owner/SKILL.md`, `AGENTS.md` | Modify | Browser-first push wiring |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-001 | The writer leaves no divider gap | `verify.gaps` is 0 after a reload |
| REQ-002 | Numbered titles and Mark-as-done lines read gray | `verify.gray` counts each one |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-003 | The words survive the write | `importDiff` is empty |
| REQ-004 | The change adds no gate failure | `run_gates.sh` fails only vendor sync on `mcp-code-mode` |
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: A new doc page needs no gap pass
- **SC-002**: A Story or numbered task on a doc page reads like the team's own pages
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Risk | ClickUp changes its editor markup | Medium | The writer checks the saved page after a reload and the markdown fallback stays documented |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:questions -->
## 7. OPEN QUESTIONS

- Should task descriptions move to the browser writer too? Left on `markdown_description` until a task needs colour
<!-- /ANCHOR:questions -->

---
