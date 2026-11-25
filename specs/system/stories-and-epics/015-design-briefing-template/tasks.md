---
title: "Tasks: Design briefing template"
description: "Task Format: T### [P?] Description (file path). Verify: <command> prints <expected output>"
trigger_phrases:
  - "design briefing template tasks"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.4 -->
# Tasks: Design briefing template

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

`V` is `benchmark/format/validate-output-format.cjs`. `SL` is `../z — Claude Project Sync Loop`. Commands run from the Product Owner root.
<!-- /ANCHOR:notation -->

---

<!-- ANCHOR:phase-1 -->
## Phase 1: Setup

- [x] T001 Record the baseline with no stray `.skilled/` folder (`benchmark/gates/run_gates.sh`). Verify: `run_gates.sh` prints `1 of 19 gates failed`, the identifier scan, and the fixture runners print 84 and 229 passes
- [x] T002 Run the gate on the refined full example as the red case (`SL/validate-output-format.cjs`). Verify: `--system product-owner <example-full>` reports three plain bullet errors
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T003 Add the Why exemption to both validators and three fixtures per folder with four runner cases each (`V`, `SL/validate-output-format.cjs`). Verify: both runners pass, with 88 and 233 passes
- [x] T004 Write Task Templates Section 7 and the three examples (`sk-product-owner/assets/task-templates.md`). Verify: `node $SL/validate-output-format.cjs --system product-owner <file>` exits 0 on each example and on the extracted scaffold
- [x] T005 Add the Task Mode entry, the title and file naming rules and the shape lists (`sk-product-owner/references/task-mode.md`, `AGENTS.md`). Verify: `rg -c 'Design Briefings' sk-product-owner/references/task-mode.md` prints 1
- [x] T006 Mirror the kernel, five knowledge files and the Project README by hand, then resync the declaration (`claude project/Custom Instructions.md`, `SL/systems.py`). Verify: `run_residency.sh` in a scratch clone prints `PASSED 1 system(s)`
- [x] T007 Regenerate the leaf manifest (`leaf-manifest.json`). Verify: `generate-leaf-manifest.cjs --check` exits 0
- [x] T008 Bump the skill to 1.2.22.0 and the kernel to v1.2.24, write the release note and the dated parity note (`sk-product-owner/changelog/v1.2.22.0.md`, `SYNC.md`). Verify: `rg -c '1.2.22.0' sk-product-owner/SKILL.md` prints 1
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T009 Gate a scratch copy of Michel's real briefing converted to the new layout. Verify: `--system product-owner <copy>` exits 0
- [x] T010 Rerun every gate and runner from the final state. Verify: results in `implementation-summary.md`
- [x] T011 Run parity and residency in a scratch clone with a throwaway commit. Verify: `PASSED 71/71 declared pairs, seven checks` and `PASSED 1 system(s)`
<!-- /ANCHOR:phase-3 -->

---

<!-- ANCHOR:completion -->
## Completion Criteria

- [x] All tasks marked `[x]`
- [x] No `[B]` blocked tasks remaining
- [x] Manual verification passed apart from the peer-file gap named in the summary
<!-- /ANCHOR:completion -->

---

<!-- ANCHOR:cross-refs -->
## Cross-References

- **Specification**: See `spec.md`
- **Plan**: See `plan.md`
<!-- /ANCHOR:cross-refs -->

---
