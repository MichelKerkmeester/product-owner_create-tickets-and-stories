---
title: "Tasks: Vendored browser packets for the ClickUp routines"
description: "Task Format: T### [P?] Description (file path). Verify: <command> prints <expected output>"
trigger_phrases:
  - "vendored browser packets for the clickup routines tasks"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.4 -->
# Tasks: Vendored browser packets for the ClickUp routines

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

- [x] T001 Size both upstream packets. Verify: 74 and 100 files, no `node_modules`.
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T002 Add and pull both packets (`vendor.json`). Verify: `vendor-sync.py status` prints `in step` for both.
- [x] T003 List both as repository paths (`mode-registry.json`). Verify: `check_hub.py` prints `PASSED`.
- [x] T004 Name both packets (`AGENTS.md`, `SKILL.md`, `README.md`). Verify: `rg -n mcp-aside-devtools AGENTS.md SKILL.md README.md` prints a line per file.
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T005 Run the system gates. Verify: 1 of 15 fails, vendor sync on `mcp-code-mode`.
- [x] T006 Validate this packet (`validate.sh --strict`). Verify: `RESULT: PASSED`.
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
