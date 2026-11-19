---
title: "Feature Specification: Feedback ticket template"
description: "Product Owner writes a round of product review feedback as feedback tickets, one per app and kind, in the shape the team's ClickUp feedback tasks use."
trigger_phrases:
  - "feedback ticket template"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.4 -->
# Feature Specification: Feedback ticket template

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
Review rounds produce feedback tickets that Michel writes by hand in ClickUp, such as the four Chat Prompts MVP Feedback #1 tasks. Product Owner had no shape for them, so a request to turn review notes into tickets came out as an ordinary task with Requirements and none of the team's conventions: one ticket per app and kind, `## Feedback` with screen groups, Code and Figma screenshot pairs, and Logic items with steps.

### Purpose
Task Mode gains a feedback ticket shape with a template, rules, routing and a worked example, and the ClickUp push writes each ticket as its own private doc through the browser-first page writer.
<!-- /ANCHOR:problem -->

<!-- ANCHOR:measured-behavior -->
### Measured Behavior
```text
Live tasks read on 2026-11-10 (DEV-4495, DEV-4496, DEV-4499, DEV-4501):
  list Side Quests, priority high, App / Filter: Feature / Scope fields
  title "BM - Chat Prompts MVP - Feedback #1 - {App}: {Logic | UI/UX}"
  items "<gray>N. </gray><strong>Title</strong>", divider, Checklist, Code | Figma 50/50 columns
Template push on scratch page 2kyq4d0p-123435 (Partner Logic round):
  blocks 33, dividers 5, gaps 0, columns [[1,1]], gray 3, import diff none
```
<!-- /ANCHOR:measured-behavior -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- Task Templates Section 6, the feedback ticket template and its notes
- Task Mode rules for the signal, split, intake, title, items, screenshots and delivery
- Routing rule 6 sends review-round feedback to feedback tickets
- A worked example and its Claude Project mirror
- Section 7 pushes each ticket as its own private doc

### Out of Scope
- Setting ClickUp custom fields or moving tickets to a list, which the user does by hand
- A separate mode or command

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| `sk-product-owner/assets/task-templates.md`, `references/task-mode.md`, `references/routing.md`, `SKILL.md` | Modify | Template, rules, routing, push |
| `sk-product-owner/assets/examples/task/task-example-feedback.md` | Create | Worked example |
| `claude project/knowledge/` Task Templates, Task Mode and the new example mirror | Modify and Create | Project mirrors |
| `leaf-manifest.json`, `README.md` files, Sync Loop `systems.py` | Modify | Inventories and pair declaration |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-001 | The example passes the format gate | `validate-output-format.cjs --system product-owner` exits 0 |
| REQ-002 | A ticket pushes cleanly | Page writer reports gaps 0, columns built, import diff empty |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-003 | Mirrors match their sources | `validate_parity.py product-owner` passes on every declared pair. `rule_parity.py` counts shared phrases and cannot show a mirror is equal |
| REQ-004 | The change adds no gate failure | `run_gates.sh` fails only vendor sync on `mcp-code-mode` |
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: Review notes for two apps and both kinds come out as up to four tickets in the team's shape
- **SC-002**: A pushed ticket reads like DEV-4495 in ClickUp, gray numbers and columns included
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Dependency | Browser-first page writer | Medium | Markdown fallback with the gap pass and columns routine |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:questions -->
## 7. OPEN QUESTIONS

- Should a feedback ticket push as a task in a named list with its custom fields set? Private docs for now, on Michel's choice
<!-- /ANCHOR:questions -->

---
