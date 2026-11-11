---
title: "Tasks: Doc alignment follow-up"
description: "Task Format: T### [P?] Description (file path). Verify: <command> prints <expected output>"
trigger_phrases:
  - "doc alignment follow-up tasks"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.4 -->
# Tasks: Doc alignment follow-up

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

- [x] T001 Run the alignment command on the system path. Verify: `resolve-scope.cjs` reports 0 files, so the checkers run by hand.
- [x] T002 Run the sk-doc checkers on the hub and the seven packets. Verify: each checker's exit code and tally are in the implementation summary.
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T003 Set the FigJam README version (`sk-create-figjam/README.md`). Verify: frontmatter reads 1.0.18.0.
- [x] T004 Bring three benchmark READMEs to the README heading shape (`benchmark/gates/README.md`, `benchmark/format/README.md`, `benchmark/router/README.md`). Verify: `validate_document.py` prints VALID for each.
- [x] T005 Update the one line citation into the renumbered router README (`benchmark/format/README.md`). Verify: the cited range ends at the Files section.
- [x] T006 Reword the pre-push lines in the packet 030 summary. Verify: `next_safe_action` names only the kernel paste.
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T007 Run the system gates. Verify: `run_gates.sh` prints every gate passing.
- [x] T008 Validate this packet and packet 030 (`validate.sh --strict`). Verify: `RESULT: PASSED`.
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
