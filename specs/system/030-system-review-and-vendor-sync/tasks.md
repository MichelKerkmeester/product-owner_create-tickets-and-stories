---
title: "Tasks: Whole-system review and vendor sync"
description: "Task Format: T### [P?] Description (file path). Verify: <command> prints <expected output>"
trigger_phrases:
  - "system review and vendor sync tasks"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.4 -->
# Tasks: Whole-system review and vendor sync

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

- [x] T001 Gray every Mark-as-done line in the page writer, upstream then pulled (`mcp-click-up/`). Verify: the match accepts `_Mark as done_` and rejects `Mark as doneness`.
- [x] T002 Run the ten-iteration review, seven iterations in parallel. Verify: `review-report.md` exists and the run status is complete.
- [x] T003 Run the sk-doc and sk-code checks and read the overlay engine. Verify: `package_skill.py --check --strict` prints valid for three roots.
- [x] T004 Pull the pending `mcp-code-mode` entry (`mcp-code-mode/`, `vendor.json`). Verify: `vendor-sync.py status` exits 0.
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T005 [P] Fix the hub doc drift (`SKILL.md`, `ROUTER.md`, `AGENTS.md`). Verify: `check_hub.py` passes.
- [x] T006 [P] Add the browser capture rules upstream and pull them (Skilled `mcp-chrome-devtools/`, `mcp-aside-devtools/`). Verify: `vendor-sync.py status` exits 0 after the pull.
- [x] T007 [P] Fix gate wiring, run reference parity from the format harness, add ignore patterns (`benchmark/`, `.gitignore`, `.utcp_config.json`). Verify: `run_fixtures.sh` passes and a broken reference copy fails it.
- [x] T008 [P] Fix the kernel count, add the feedback ticket label, fix the upload guide (`claude project/`). Verify: `validate_parity.py product-owner` passes.
- [x] T009 [P] Add `sync`, `status --local` and `diff`, check the override root, write the recipe (`scripts/`). Verify: `test_vendor_sync.py` passes.
- [x] T010 Run `status --local` from the release gate where it skipped (`benchmark/gates/run_gates.sh`). Verify: the standalone branch calls it.
- [x] T011 Release the hub and the kernel with changelogs and a SYNC note. Verify: `check_changelog_shape.py` passes.
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T012 Run the system gates, every fixture harness, the format gate, parity and residency. Verify: every gate passes.
- [x] T013 Validate this packet (`validate.sh --strict`). Verify: `RESULT: PASSED`.
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
