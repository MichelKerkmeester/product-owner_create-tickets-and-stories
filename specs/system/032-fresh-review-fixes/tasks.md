---
title: "Tasks: Fresh review fixes"
description: "Task Format: T### [P?] Description (file path). Verify: <command> prints <expected output>"
trigger_phrases:
  - "fresh review fixes tasks"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.4 -->
# Tasks: Fresh review fixes

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

- [x] T001 Verify the review findings against the tree and record Michel's four answers (`spec.md`). Verify: the spec lists the chosen findings and decisions.
- [x] T002 Count the identifiers per folder. Verify: the counts are in the implementation summary.
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T003 [P] Fix the scaffolds, the spacer rule, the feedback path and example, the stale counts and the restated rules, with the Project mirror (`sk-product-owner/`, `AGENTS.md`, `claude project/`). Verify: `example_lint.py` prints PASSED with 44 scaffold blocks.
- [x] T004 [P] Add the source format lint, the scaffold lint and the identifier scan to the gates (`benchmark/gates/`). Verify: each goes red on a scratch copy with a planted fault.
- [x] T005 [P] Exit 2 on a malformed manifest (`scripts/vendor-sync.py`). Verify: `test_vendor_sync.py` passes 36 tests.
- [x] T006 [P] Match hub keywords as whole tokens and read the grader word lists from the card (`check_leaf_map_parity.py`, `hvr_lint.py`). Verify: both self-tests pass.
- [x] T007 [P] Repair the upstream items in Skilled and replace the workspace id in two packets. Verify: each fix has a test that fails on the old code.
- [x] T008 Redact the identifiers in place (`specs/`, `benchmark/reports/`). Verify: a second run of the script reports 0 replacements.
- [x] T009 Correct the Flow reply sentence (`sk-create-figjam/references/flow-mode.md` and its mirror). Verify: the sentence names the `Finding:` line.
- [x] T010 Resync five declared residency statements (Sync Loop `systems.py`). Verify: `residency_check.py --all` prints PASSED.
- [x] T011 Release hub 1.0.30.0, `sk-product-owner` 1.2.17.0, `sk-create-figjam` 1.0.19.0 and kernel v1.2.20. Verify: `check_changelog_shape.py` prints PASS for each note.
- [x] T012 Pull the vendored packets from the published Skilled commit (`vendor.json`). Verify: `vendor-sync.py status` reports every entry in step.
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T013 Run the system gates. Verify: `run_gates.sh` prints `all 19 gates pass`.
- [x] T014 Run parity and residency in a scratch clone. Verify: both print PASSED.
- [x] T015 Validate this packet (`validate.sh --strict`). Verify: `RESULT: PASSED`.
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
