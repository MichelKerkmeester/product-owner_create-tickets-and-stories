---
title: "Implementation Plan: Story criteria and checklist layout"
description: "Changes both format validators first against a red fixture, then the Story rule sources, their Project mirrors and the shared declaration, and releases the change as patch steps."
trigger_phrases:
  - "story criteria and checklist layout plan"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: plan-core | v2.4 -->
# Implementation Plan: Story criteria and checklist layout

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
| **Testing** | `run_gates.sh`, `run_residency.sh`, both `run_fixtures.sh` runners, `reference-parity.cjs` and strict packet validation |

### Overview
Write a Story in the new layout and run the current gate on it as the red case. Change both validators in step so the parity check stays byte-identical, and flip the Mark-as-done fixtures. Then rewrite the Story rule sources, templates, examples and playbook scenarios, mirror them into the Claude Project by hand, resync the shared declaration and bump the hub and skill one patch step each.
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
- [x] Gate, fixture, parity and residency results match the baseline apart from the intended changes
- [x] Docs updated (spec/plan/tasks)
<!-- /ANCHOR:quality-gates -->

---

<!-- ANCHOR:architecture -->
## 3. ARCHITECTURE

### Pattern
Gate first, then source, then mirror

### Key Components
- **`benchmark/format/validate-output-format.cjs`**: the reference validator the shared core must reproduce
- **`../z — Claude Project Sync Loop/validate-output-format.cjs`**: the shared core, checked against the reference by `reference-parity.cjs`
- **`sk-product-owner/references/story-mode.md`**: the single authority for the Story and Epic shapes
- **`../z — Claude Project Sync Loop/systems.py`**: declares kernel and knowledge statements by hash

### Data Flow
The validators change first, so the old layout fails and the new one passes. The rule sources change next, the mirrors follow by hand, and `resync_statement.py` rewrites any declared statement the edit touched.
<!-- /ANCHOR:architecture -->

---

<!-- ANCHOR:phases -->
## 4. IMPLEMENTATION PHASES

Follow the ordered tasks in `tasks.md`. Setup records the baseline. Implementation changes the gates, then the sources, mirrors and release files. Verification reruns every baseline check and the export.
<!-- /ANCHOR:phases -->

---

<!-- ANCHOR:testing -->
## 5. TESTING STRATEGY

The baseline is 18 of 19 gates, with vendor sync failing before the change, a passing residency check, passing fixtures in both runners and a byte-identical parity check. The final state must match it, with the flipped Mark-as-done fixtures and a Story in the new layout passing.
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:dependencies -->
## 6. DEPENDENCIES

`python3`, `node`, `rg` and the shared Sync Loop folder one level above this repository. No new package.
<!-- /ANCHOR:dependencies -->

---

<!-- ANCHOR:rollback -->
## 7. ROLLBACK PLAN

Trigger: the team wants the two-divider layout back. Revert the commit carrying this packet in this repository and the matching commit in the Barter repository.
<!-- /ANCHOR:rollback -->

---
