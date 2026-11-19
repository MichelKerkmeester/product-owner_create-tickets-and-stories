---
title: "Implementation Plan: Mark-as-done line between two dividers"
description: "Each Story and Epic Mark-as-done line now sits between two dividers in every template, example, mirror and the format gate."
trigger_phrases:
  - "mark-as-done line between two dividers plan"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: plan-core | v2.4 -->
# Implementation Plan: Mark-as-done line between two dividers

<!-- SPECKIT_LEVEL: 1 -->

---

<!-- ANCHOR:summary -->
## 1. SUMMARY

### Technical Context

| Aspect | Value |
|--------|-------|
| **Language/Stack** | Markdown skill docs, JavaScript run in Code Mode |
| **Framework** | Product Owner hub |
| **Storage** | None |
| **Testing** | `run_fixtures.sh` in both corpora, `validate-output-format.cjs --system product-owner`, `rule_parity.py`, `run_gates.sh` and `validate.sh --strict` |

### Overview
The rule was reversed in the skill sources first, then mirrored by hand into the Project files, then the validator flipped and its fixtures moved.
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
Skill source first, hand mirror, gate last

### Key Components
- **Format validator**: `markAsDoneFindings` requires a divider above and below
- **Fixtures**: one shape per error, identical in both corpora

### Data Flow
Skill sources, Project mirrors, validator and fixtures, Sync Loop statements.
<!-- /ANCHOR:architecture -->

---

<!-- ANCHOR:phases -->
## 4. IMPLEMENTATION PHASES

Follow the ordered tasks in `tasks.md`.
<!-- /ANCHOR:phases -->

---

<!-- ANCHOR:testing -->
## 5. TESTING STRATEGY

`run_fixtures.sh` in both corpora, `validate-output-format.cjs --system product-owner`, `rule_parity.py`, `run_gates.sh` and `validate.sh --strict`.
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:dependencies -->
## 6. DEPENDENCIES

None beyond the Sync Loop folder beside this system.
<!-- /ANCHOR:dependencies -->

---

<!-- ANCHOR:rollback -->
## 7. ROLLBACK PLAN

Revert the Product Owner commit and the outer repository commit that carries the Sync Loop files.
<!-- /ANCHOR:rollback -->

---
