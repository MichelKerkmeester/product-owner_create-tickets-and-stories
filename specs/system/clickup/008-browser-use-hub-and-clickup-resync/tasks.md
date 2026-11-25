---
title: "Tasks: Browser Use hub and ClickUp resync"
description: "Task Format: T### [P?] Description (file path). Verify: <command> prints <expected output>"
trigger_phrases:
  - "browser use hub and clickup resync tasks"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.4 -->
# Tasks: Browser Use hub and ClickUp resync

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

- [x] T001 Size the upstream hub and capture the gate baseline. Verify: 322 files, no symlinks, and `run_gates.sh` prints `3 of 19 gates failed`.
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T002 Replace the two browser entries with the hub entry and delete both folders (`vendor.json`). Verify: `vendor-sync.py status --package mcp-browser-use` prints `in step`.
- [x] T003 Pull `mcp-click-up`, `mcp-figma` and `mcp-code-mode` (`vendor.json`). Verify: `vendor-sync.py status` names no entry out of step.
- [x] T004 List the hub as a repository path (`mode-registry.json`). Verify: `check_hub.py` prints `PASSED`.
- [x] T005 Name the hub (`SKILL.md`, `README.md`, `scripts/README.md`). Verify: `rg -n mcp-browser-use SKILL.md README.md scripts/README.md` prints a line per file.
- [x] T006 Bump the hub to v1.0.38.0 with its changelog (`changelog/v1.0.38.0.md`). Verify: the four version files read `1.0.38.0`.
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T007 Run the system gates. Verify: no gate fails that passed in the baseline.
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
