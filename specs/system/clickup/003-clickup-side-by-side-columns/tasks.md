---
title: "Tasks: ClickUp side-by-side screenshot columns"
description: "Task Format: T### [P?] Description (file path). Verify: <command> prints <expected output>"
trigger_phrases:
  - "clickup side-by-side screenshot columns tasks"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.4 -->
# Tasks: ClickUp side-by-side screenshot columns

<!-- SPECKIT_LEVEL: 1 -->

---

<!-- ANCHOR:notation -->
## Task Notation

| Prefix | Meaning |
|--------|---------|
| `[ ]` | Pending |
| `[x]` | Completed |
| `[P]` | Parallelizable |
| `[B]` | Blocked |

**Task Format**: `T### [P?] Description (file path). Verify: <command> prints <expected output>`
<!-- /ANCHOR:notation -->

---

<!-- ANCHOR:phase-1 -->
## Phase 1: Setup

- [x] T001 Probe a live columns block (BM page). Verify: blocks carry `data-layout` and `data-layout-width`.
- [x] T002 Prove the paste on scratch pages (doc `2kyq4d0p-147775`). Verify: a row survives a reload.
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T003 Add the routine upstream (Skilled `mcp-click-up` 1.2.18.0). Verify: commit `4834f91ff3` pushed.
- [x] T004 Pull the copy (`mcp-click-up/`, `vendor.json`). Verify: `vendor-sync.py status` prints `in step at 4834f91ff3...`.
- [x] T005 Add the Section 7 bullets and release (`sk-product-owner/SKILL.md`, hub files). Verify: REQ-001 prints two lines.
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T006 Run the documented program on a fresh page (page `2kyq4d0p-123195`). Verify: 2 rows, 1 image per column, 0 leftovers.
- [x] T007 Run the system gates. Verify: 1 of 15 fails, vendor sync on `mcp-code-mode`.
- [x] T008 Validate this packet (`validate.sh --strict`). Verify: `RESULT: PASSED`.
<!-- /ANCHOR:phase-3 -->

---

<!-- ANCHOR:completion -->
## Completion Criteria

- [x] All tasks marked `[x]`
- [x] No `[B]` blocked tasks remaining
- [x] Manual verification passed
<!-- /ANCHOR:completion -->

---

<!-- ANCHOR:cross-refs -->
## Cross-References

- **Specification**: See `spec.md`
- **Plan**: See `plan.md`
<!-- /ANCHOR:cross-refs -->

---
