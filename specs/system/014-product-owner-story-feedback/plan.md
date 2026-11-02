---
title: "Implementation Plan: Product Owner Story and Epic template changes requested by the PM"
description: "Edit the Product Owner Story and Epic sources first, mirror each change into the Claude Project by hand, and teach both format validators the new Problem caps and the joined-outcome advice."
trigger_phrases:
  - "product owner story feedback plan"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: plan-core | v2.2 -->
# Implementation Plan: Product Owner Story and Epic template changes requested by the PM

<!-- SPECKIT_LEVEL: 1 -->

---

<!-- ANCHOR:summary -->
## 1. SUMMARY

### Technical Context

| Aspect | Value |
|--------|-------|
| **Language/Stack** | Markdown skill and Claude Project documents, one Node validator |
| **Framework** | sk-product-owner, manual parity method in `SYNC.md` |
| **Storage** | None |
| **Testing** | Router fixtures, format fixtures in four systems, reference parity, rule parity, project parity |

### Overview
The templates, Story Mode and examples change first, then each Project mirror gets the same wording. The two validators take one identical edit, because reference parity holds them byte-identical.
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
- [x] Tests passing (if applicable)
- [x] Docs updated (spec/plan/tasks)
<!-- /ANCHOR:quality-gates -->

---

<!-- ANCHOR:architecture -->
## 3. ARCHITECTURE

### Pattern
Source and hand-written mirror

### Key Components
- **Skill sources**: templates, Story Mode, examples and playbook
- **Claude Project**: kernel plus knowledge mirrors uploaded to claude.ai
- **Format validators**: Product Owner copy and the shared Sync Loop copy

### Data Flow
Skill source change, then the matching Project mirror, then gates, then the operator uploads the Project files.
<!-- /ANCHOR:architecture -->


---

<!-- ANCHOR:phases -->
## 4. IMPLEMENTATION PHASES

Follow the ordered tasks in `tasks.md`. It owns the Setup, Implementation and Verification phase checkboxes and task state.
<!-- /ANCHOR:phases -->

---

<!-- ANCHOR:testing -->
## 5. TESTING STRATEGY

Run every gate on the working tree and compare the format gate against a HEAD export in the scratchpad. The project parity gate reads committed history, so it runs after the commit.
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:dependencies -->
## 6. DEPENDENCIES

The validator and fixture twins live in the parent Barter repo, so that part of the change spans two repositories.
<!-- /ANCHOR:dependencies -->

---

<!-- ANCHOR:rollback -->
## 7. ROLLBACK PLAN

Revert the change in the Product Owner repo and the three Sync Loop files (`validate-output-format.cjs`, `run_fixtures.sh`, `systems.py`) plus the two delivery fixtures in the parent repo.
<!-- /ANCHOR:rollback -->

---

