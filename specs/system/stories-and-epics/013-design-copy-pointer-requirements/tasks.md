---
title: "Tasks: Design copy pointer requirements"
description: "Task Format: T### [P?] Description (file path). Verify: <command> prints <expected output>"
trigger_phrases:
  - "design copy pointer requirements tasks"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.4 -->
# Tasks: Design copy pointer requirements

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

`SM` is `sk-product-owner/references/story-mode.md`. `ST` is `sk-product-owner/assets/story-template.md`. Commands run from the Product Owner root.
<!-- /ANCHOR:notation -->

---

<!-- ANCHOR:phase-1 -->
## Phase 1: Setup

- [x] T001 Record the gate baseline before any edit (`benchmark/gates/run_gates.sh`). Verify: `bash benchmark/gates/run_gates.sh` prints `all 19 gates pass`.
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T002 Narrow the verbatim rule, add the design pointer rule and fix the item count (`sk-product-owner/references/story-mode.md`). Verify: `rg -c 'Never write one item per visible string' $SM` prints 1.
- [x] T003 Add the strike rule for quoted design strings and the design pointer note (`sk-product-owner/assets/story-template.md`). Verify: `rg -c 'Never write one item per visible string' $ST` prints 1.
- [x] T004 Carry the Story Mode sentences into the mirror (`claude project/knowledge/Product Owner - Templates - Story Mode.md`). Verify: `diff` of source lines 75 to 77 against mirror lines 52 to 54 prints nothing.
- [x] T005 Carry the template sentences into the mirror (`claude project/knowledge/Product Owner - Assets - Story Template.md`). Verify: `diff` of source lines 106 to 107 against mirror lines 87 to 88 prints nothing.
- [x] T006 Bump the hub to 1.0.34.0 and the skill to 1.2.19.0 and write both release notes (`README.md`). Verify: `rg -c '1.0.34.0|1.2.19.0' README.md` prints 3.
- [x] T007 Add the dated parity note (`SYNC.md`). Verify: `rg -c '2026-11-12 Claude Code' SYNC.md` prints 1.
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T008 Rerun every gate from the final state (`benchmark/gates/run_gates.sh`). Verify: `bash benchmark/gates/run_gates.sh` prints `all 19 gates pass`.
- [x] T009 Rerun the residency check (`benchmark/parity/run_residency.sh`). Verify: `bash benchmark/parity/run_residency.sh` prints `PASSED 1 system(s)`.
- [x] T010 Confirm the old sentences are gone (`sk-product-owner/references/story-mode.md`). Verify: `rg -c 'binds copy the source shows as much as copy it types' $SM` prints nothing and exits 1.
<!-- /ANCHOR:phase-3 -->

---

<!-- ANCHOR:completion -->
## Completion Criteria

- [x] All tasks marked `[x]`
- [x] No `[B]` blocked tasks remaining
- [x] Manual verification passed: the gate runner printed `all 19 gates pass` and the residency check printed `PASSED`
<!-- /ANCHOR:completion -->

---

<!-- ANCHOR:cross-refs -->
## Cross-References

- **Specification**: See `spec.md`
- **Plan**: See `plan.md`
<!-- /ANCHOR:cross-refs -->

---
