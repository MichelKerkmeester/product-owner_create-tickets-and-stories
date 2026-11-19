---
title: "Implementation Plan: ClickUp side-by-side screenshot columns"
description: "A Product Owner doc page push sets each DEV and FIGMA screenshot pair in a ClickUp columns block, built in the editor by the vendored mcp-click-up columns routine."
trigger_phrases:
  - "clickup side-by-side screenshot columns plan"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: plan-core | v2.4 -->
# Implementation Plan: ClickUp side-by-side screenshot columns

<!-- SPECKIT_LEVEL: 1 -->

---

<!-- ANCHOR:summary -->
## 1. SUMMARY

### Technical Context

| Aspect | Value |
|--------|-------|
| **Language/Stack** | Markdown skill docs, vendored skill packages |
| **Framework** | Product Owner hub |
| **Storage** | None |
| **Testing** | `run_gates.sh`, `vendor-sync.py status`, live ClickUp pages |

### Overview
The routine was proven on scratch pages before any doc changed. Upstream Skilled gained it as `mcp-click-up` 1.2.18.0, and Section 7 points to it for screenshot pairs.
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
Vendored owner, Product Owner pointer

### Key Components
- **`mcp-click-up/references/mcp-tools.md` Section 8**: owns the routine
- **`sk-product-owner/SKILL.md` Section 7**: decides when a push uses it

### Data Flow
The page write carries `[[COLS-n]]` lines, the gap pass runs, then the routine pastes each row and uploads each local screenshot.
<!-- /ANCHOR:architecture -->

---

<!-- ANCHOR:phases -->
## 4. IMPLEMENTATION PHASES

Follow the ordered tasks in `tasks.md`.
<!-- /ANCHOR:phases -->

---

<!-- ANCHOR:testing -->
## 5. TESTING STRATEGY

`bash benchmark/gates/run_gates.sh` and `python3 scripts/vendor-sync.py status` with `VENDOR_UPSTREAM_ROOT` set to the Skilled checkout.
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:dependencies -->
## 6. DEPENDENCIES

Skilled commit `4834f91ff3`.
<!-- /ANCHOR:dependencies -->

---

<!-- ANCHOR:rollback -->
## 7. ROLLBACK PLAN

Revert the Product Owner commit. A vendored copy returns with `vendor-sync.py pull` against an earlier upstream commit.
<!-- /ANCHOR:rollback -->

---
