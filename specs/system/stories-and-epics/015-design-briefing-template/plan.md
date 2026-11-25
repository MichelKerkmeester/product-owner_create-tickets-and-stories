---
title: "Implementation Plan: Design briefing template"
description: "Changes both format validators against a red example first, then the briefing template and mode, the router and title rules, the Project mirrors and the shared declaration, and releases the change as patch steps, the second of which moves the briefing out of Task Mode."
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
Run the format gate on the refined briefing examples as the red case, then change both validators in step and add three fixtures. Write the template, the examples, the mode reference and the title rules, mirror them into the Project by hand, resync the declaration and release as a patch step. A second pass moves the briefing out of Task Mode into its own intent, command, mode reference and template, rewires the router copies, the leaf map and the Project, and releases as the next patch step.
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
- **`sk-product-owner/assets/design-briefing-template.md`**: the scaffold, with `references/briefing-mode.md` as its rule source
- **`sk-product-owner/references/router-contract.md`**: the router as Python, which `benchmark/router/route_contract.py` and the kernel's Router Code must equal
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

The baseline for the move is 17 of 19 gates with the identifier scan and the format fixtures parity count failing, 190 route fixtures, 283 differential inputs, parity 71 of 71 and residency passing. The final state must match it, with five more route fixtures and differential inputs, two more declared pairs and nothing new failing.
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
