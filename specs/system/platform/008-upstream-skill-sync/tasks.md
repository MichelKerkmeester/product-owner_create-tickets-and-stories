---
title: "Tasks: Upstream skill sync"
description: "Task Format: T### [P?] Description (file path). Verify: <command> prints <expected output>"
trigger_phrases:
  - "upstream skill sync tasks"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.4 -->
# Tasks: Upstream skill sync

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

- [x] T001 Baseline the vendor-sync tests. Verify: `test_vendor_sync.py` prints `Ran 36 tests` and `OK`.
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T002 Add the `--remote` and `--ref` source (`scripts/vendor-sync.py`). Verify: `status --remote` names no entry out of step.
- [x] T003 Add the `add` command (`scripts/vendor-sync.py`). Verify: the add tests pass.
- [x] T004 Print a rebuild line on a source change (`scripts/vendor-sync.py`). Verify: the rebuild test passes.
- [x] T005 Add the one-command update and its agent command (`scripts/update-vendored.sh`, `.claude/commands/vendor-update.md`). Verify: `bash -n scripts/update-vendored.sh` exits 0.
- [x] T006 Document the commands (`scripts/README.md`, `README.md`, `changelog/v1.0.38.0.md`). Verify: `rg -n update-vendored scripts/README.md README.md` prints a line per file.
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T007 Run the tests. Verify: `Ran 41 tests` and `OK`.
- [x] T008 Run the update end to end. Verify: `update-vendored.sh --remote` prints `2 of 19 gates failed`, the two that failed before.
- [x] T010 Refresh the code READMEs under `scripts/` and add the four missing under `sk-create-figjam/`. Verify: `validate_document.py` prints `VALID` for each.
- [x] T011 Check out every entry on a one-package remote run, and exit 1 for any sync or gate failure (`scripts/vendor-sync.py`, `scripts/update-vendored.sh`, `scripts/README.md`). Verify: `update-vendored.sh --package mermaid-extract` in a clone with no Skilled checkout prints `vendor sync ok`, and `Ran 42 tests` and `OK`.
- [x] T012 Delete the 20 tracked skill-format JSONs no code, gate, CI or advisor reads, and fix the doc lines naming them (Copywriter README, Prompt Improver README, Moneybird `SKILL.md`). Verify: each system's checks give the same result before and after. HolyArrs' 4 untracked files were deleted on the operator's answer, with no backup, and its README tree updated.
- [x] T013 Remove the hub's `description.json` and `graph-metadata.json`, drop the skilled hub contract gate, add `sk-create-figjam/assets/README.md` to the Sync Loop `systems.cjs` list, and replace the home path in 32 review receipts. Verify: `run_gates.sh` prints `all 18 gates pass`.
- [x] T009 Validate this packet (`validate.sh --strict`). Verify: `RESULT: PASSED`.
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
