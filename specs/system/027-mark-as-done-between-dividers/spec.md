---
title: "Feature Specification: Mark-as-done line between two dividers"
description: "Each Story and Epic Mark-as-done line now sits between two dividers in every template, example, mirror and the format gate."
trigger_phrases:
  - "mark-as-done line between two dividers"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.4 -->
# Feature Specification: Mark-as-done line between two dividers

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
Story and Epic criteria closed with a Mark-as-done checkbox that no divider separated from the next criterion, and the format gate blocked a divider there. In ClickUp the team works the checklist as its own band between two rules, so the house shape and the team's pages disagreed.

### Purpose
The Mark-as-done line sits between two dividers everywhere, and the format gate requires both.
<!-- /ANCHOR:problem -->

<!-- ANCHOR:measured-behavior -->
### Measured Behavior
```text
Before: validate-output-format.cjs blocked a divider under a Mark-as-done line
After: run_fixtures.sh 62 PASS (was 59), Sync Loop fixtures 157 PASS (was 154)
Real export Media, Reel Player: old validator passes, new one reports 15 missing dividers
```
<!-- /ANCHOR:measured-behavior -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- Rule text in `AGENTS.md`, `SKILL.md`, Story, Doc and Task Mode references, templates, five Story examples and 14 playbook scenarios
- Claude Project kernel and knowledge mirrors
- Both copies of the format validator, their fixtures, `rule_parity.py` and the Sync Loop statements

### Out of Scope
- Old exports, which keep their shape
- Gray colour, which the ClickUp page writer sets

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| `AGENTS.md`, `sk-product-owner/` rule, template, example and playbook files | Modify | New divider rule |
| `claude project/Custom Instructions.md` and knowledge mirrors | Modify | Same rule in the Project |
| `benchmark/format/`, `../z — Claude Project Sync Loop/` validator, fixtures, statements | Modify and Create | Gate requires both dividers |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-001 | The gate requires both dividers | `run_fixtures.sh` passes with the new violation fixtures |
| REQ-002 | Every source file follows the rule | `validate-output-format.cjs --system product-owner` exits 0 on 73 files |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-003 | The change adds no gate failure | `run_gates.sh` fails only vendor sync on `mcp-code-mode` |
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: Every Story and Epic shape puts Mark-as-done between two dividers
- **SC-002**: The kernel and knowledge files say the same
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Risk | Older exports now fail the lint | Low | They keep their shape until refined |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:questions -->
## 7. OPEN QUESTIONS

- Should the gate enforce only the lower divider? Both are enforced for now
<!-- /ANCHOR:questions -->

---
