---
title: "Tasks: Phase 7, drop clarification exports"
description: "Task Format: T### [P?] Description (file path)"
trigger_phrases:
  - "drop clarification exports tasks"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.2 -->
# Tasks: Phase 7, drop clarification exports

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

**Task Format**: `T### [P?] Description (file path)`
<!-- /ANCHOR:notation -->

---

<!-- ANCHOR:phase-1 -->
## Phase 1: Setup

- [x] T001 Confirm the 20 clarification files and their counts per side (`export/benchmark/`). Evidence: 10 skill and 10 Project `*-clarification.md`, 98 files in all
- [x] T002 Record the old collector and selftest hashes as the negative control (`run/`). Evidence: collector `1611…0e5f` and selftest `f657…fbd8c` matched the README, old collector copied to the scratchpad
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T003 Skip clarifications on both sides with a skip line (`run/collect_exports.py`). Evidence: `CLARIFICATION_SUFFIX` checked before the copy and before the Project write
- [x] T004 Expect no clarification and two skip lines in the collector check (`run/selftest.py`). Evidence: two planted clarifications left out of the expected set, a new check asks for both skip lines
- [x] T005 Remove the 20 files with `git rm` in the Product Owner repo (`export/benchmark/`). Evidence: `git rm` of 20 paths, 78 files remain
- [x] T006 Update counts, the Project table, the hashes and the kernel review line (`README.md`). Evidence: Clarifications removed section, rounds paragraph, 10 table rows out, hashes and the kernel review line
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T007 Selftest fails with the old collector and passes with the new one. Evidence: old collector exit 1 on both new checks, new collector 7 of 7
- [x] T008 Dry run over the real run folder: no clarification write, 20 skip lines. Evidence: 20 skip lines, 0 clarification writes
- [x] T009 Format gate, parity and residency on the committed state. Evidence: 78 exports 0 failures, parity 38/38 with reviews, residency PASSED
- [x] T010 Commit in both repos, push on the operator's go-ahead. Evidence: pushed Product Owner `1fc3657..e042272`, Barter `e324ecdf..c6493c1b` on the second attempt
- [x] T011 Delete the git-ignored local copies the operator added to scope (`benchmark/reports/*/**/exports/`). Evidence: 46 removed, Opus 25, GLM 16, Sonnet 2026-09-25 5, each with a same-named file in git history, backup in the session scratchpad; README and collector docstring now point to the transcript
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
