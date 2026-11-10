---
title: "Tasks: ClickUp doc push editor and numbering fixes"
description: "Task Format: T### [P?] Description (file path). Verify: <command> prints <expected output>"
trigger_phrases:
  - "clickup doc push editor and numbering tasks"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.4 -->
# Tasks: ClickUp doc push editor and numbering fixes

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

- [x] T001 Probe the live page editor (ClickUp page `2kyq4d0p-122975`). Verify: two `.ql-editor` elements, the body one holds `HR.ql-divider` then an empty `DIV.ql-block`.
- [x] T002 Compare three title spellings on the live page. Verify: all three render as `DIV.ql-block`, and only `2\. **X**` reads back as sent.
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T003 Escape numbered task titles in six sources and five mirrors (`sk-product-owner/`, `claude project/knowledge/`). Verify: the REQ-001 `rg` prints nothing.
- [x] T004 Fix the gap pass selector and name both spellings upstream (Skilled `mcp-click-up` 1.2.17.0, hub 1.9.9.0). Verify: Skilled commit `16db86bc96` pushed and level with origin.
- [x] T005 Pull the vendored copy (`mcp-click-up/`, `vendor.json`). Verify: `vendor-sync.py status` prints `mcp-click-up: in step at 16db86bc96...`.
- [x] T006 Release hub 1.0.25.0 and `sk-product-owner` 1.2.13.0 (`SKILL.md`, three hub JSON files, two READMEs, two changelogs, `SYNC.md`). Verify: `rg -n '1\.0\.25\.0|1\.2\.13\.0'` prints a line per file.
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T007 Run the system gates (`benchmark/gates/run_gates.sh`). Verify: 1 of 15 fails, vendor sync on `mcp-code-mode` only.
- [x] T008 Republish the live page and run the gap pass. Verify: 25 titles numbered 1 to 25, import diff 0, 60 gaps removed, text unchanged.
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
- **Related packet**: `specs/system/021-clickup-doc-divider-spacing`, which added the gap pass
<!-- /ANCHOR:cross-refs -->

---
