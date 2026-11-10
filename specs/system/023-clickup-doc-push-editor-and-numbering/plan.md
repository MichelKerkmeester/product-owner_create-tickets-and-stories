---
title: "Implementation Plan: ClickUp doc push editor and numbering fixes"
description: "Escape the full stop in numbered task titles across the task sources and their Knowledge mirrors, fix the gap pass selector upstream and pull it here, then release."
trigger_phrases:
  - "clickup doc push editor and numbering plan"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: plan-core | v2.4 -->
# Implementation Plan: ClickUp doc push editor and numbering fixes

<!-- SPECKIT_LEVEL: 1 -->

---

<!-- ANCHOR:summary -->
## 1. SUMMARY

### Technical Context

| Aspect | Value |
|--------|-------|
| **Language/Stack** | Markdown skill docs, vendored skill package |
| **Framework** | Product Owner hub with `sk-product-owner` and the vendored `mcp-click-up` packet |
| **Storage** | None |
| **Testing** | Live ClickUp page read-backs, `run_gates.sh`, `validate_parity.py` |

### Overview
The title form was chosen on a live page: three spellings rendered as plain blocks, and only `2\. **X**` read back as sent. The task sources and their mirrors take that form with one substitution. The gap pass fix and the push shape rules land upstream in Skilled first, then reach this repository through `vendor-sync.py pull`.
<!-- /ANCHOR:summary -->

---

<!-- ANCHOR:quality-gates -->
## 2. QUALITY GATES

### Definition of Ready
- [x] Problem statement clear and scope documented
- [x] Success criteria measurable
- [x] Dependencies identified

### Definition of Done
- [x] All acceptance criteria met
- [x] `run_gates.sh` fails only the vendor sync gate that predates this change
- [x] Docs updated (spec/plan/tasks)
<!-- /ANCHOR:quality-gates -->

---

<!-- ANCHOR:architecture -->
## 3. ARCHITECTURE

### Pattern
Fix at the template, with the transport naming the same spelling

### Key Components
- **`sk-product-owner/assets/task-templates.md`**: the scaffold every new task copies
- **`mcp-click-up/references/mcp-tools.md` Section 8**: the vendored gap pass

### Data Flow
A task drafted from the template carries `1\. **{Title}**`, the push sends it unchanged, and the gap pass edits the body editor after the write.
<!-- /ANCHOR:architecture -->

---

<!-- ANCHOR:phases -->
## 4. IMPLEMENTATION PHASES

Follow the ordered tasks in `tasks.md`. Setup measures the page, Implementation edits the sources and pulls the vendored copy, and Verification runs the gates and the live page.
<!-- /ANCHOR:phases -->

---

<!-- ANCHOR:testing -->
## 5. TESTING STRATEGY

A live page read-back confirms the title form and the gap pass. `run_gates.sh`, the format gate and `validate_parity.py product-owner` cover the repository.
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:dependencies -->
## 6. DEPENDENCIES

Skilled commit `16db86bc96`, pushed to origin before the pull.
<!-- /ANCHOR:dependencies -->

---

<!-- ANCHOR:rollback -->
## 7. ROLLBACK PLAN

Revert the commit in this repository and the Skilled commit `16db86bc96`. The vendored copy returns with `vendor-sync.py pull` against an earlier upstream commit.
<!-- /ANCHOR:rollback -->

---
