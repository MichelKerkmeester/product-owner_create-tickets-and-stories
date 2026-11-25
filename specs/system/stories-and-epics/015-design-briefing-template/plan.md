---
title: "Implementation Plan: Design briefing template"
description: "Changes both format validators against a red example first, then the template, Task Mode and title rules, the Project mirrors and the shared declaration, and releases the change as one patch step."
trigger_phrases:
  - "design briefing template plan"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: plan-core | v2.4 -->
# Implementation Plan: Design briefing template

<!-- SPECKIT_LEVEL: 1 -->

---

<!-- ANCHOR:summary -->
## 1. SUMMARY

### Technical Context

| Aspect | Value |
|--------|-------|
| **Language/Stack** | Markdown, JSON, Node.js, Python |
| **Framework** | Product Owner hub, `sk-product-owner`, its Claude Project package and the shared Sync Loop |
| **Storage** | None |
| **Testing** | `run_gates.sh`, both `run_fixtures.sh` runners, `reference-parity.cjs`, parity and residency in a scratch clone |

### Overview
Run the format gate on the refined briefing examples as the red case, then change both validators in step and add three fixtures. Write Section 7, the examples, the Task Mode entry and the title rules, mirror them into the Project by hand, resync the declaration and release as one patch step.
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
- [x] Gate results match the baseline apart from the intended changes and the named peer-file gap
- [x] Docs updated (spec/plan/tasks)
<!-- /ANCHOR:quality-gates -->

---

<!-- ANCHOR:architecture -->
## 3. ARCHITECTURE

### Pattern
Gate first, then source, then mirror

### Key Components
- **`benchmark/format/validate-output-format.cjs`**: the reference validator the shared core must reproduce
- **`../z — Claude Project Sync Loop/validate-output-format.cjs`**: the shared core
- **`sk-product-owner/assets/task-templates.md`**: the scaffold, with Task Mode as its rule source
- **`../z — Claude Project Sync Loop/systems.py`**: declares mirror pairs and kernel statements by hash

### Data Flow
Both validators change first. The sources follow, the mirrors after them by hand, and `resync_statement.py` rewrites each declared statement the kernel edit touched.
<!-- /ANCHOR:architecture -->

---

<!-- ANCHOR:phases -->
## 4. IMPLEMENTATION PHASES

Follow the ordered tasks in `tasks.md`.
<!-- /ANCHOR:phases -->

---

<!-- ANCHOR:testing -->
## 5. TESTING STRATEGY

The baseline is 18 of 19 gates with the identifier scan failing, 84 and 229 fixture passes and a byte-identical reference parity. The final state must match it, plus four new cases per runner.
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:dependencies -->
## 6. DEPENDENCIES

`python3`, `node`, `rsync` and the shared Sync Loop folder one level above this repository. No new package.
<!-- /ANCHOR:dependencies -->

---

<!-- ANCHOR:rollback -->
## 7. ROLLBACK PLAN

Trigger: the team drops the briefing shape. Revert the commit carrying this packet in this repository and the matching commit in the Barter repository.
<!-- /ANCHOR:rollback -->

---
