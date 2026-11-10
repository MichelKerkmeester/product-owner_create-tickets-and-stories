---
title: "Tasks: Feedback ticket template"
description: "Task Format: T### [P?] Description (file path). Verify: <command> prints <expected output>"
trigger_phrases:
  - "feedback ticket template tasks"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.4 -->
# Tasks: Feedback ticket template

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

- [x] T001 Read the four live feedback tasks in ClickUp. Verify: titles, fields, gray numbers and columns recorded in spec.md.
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T002 Write the template (`task-templates.md` Section 6). Verify: `rg -n FEEDBACK assets/task-templates.md` prints the heading.
- [x] T003 Write the Task Mode rules and routing (`task-mode.md`, `routing.md`). Verify: `rg -n "Feedback Tickets" references` prints both.
- [x] T004 Add the worked example and its mirrors. Verify: `validate-output-format.cjs` exits 0.
- [x] T005 Push each ticket as a private doc (`SKILL.md` Section 7). Verify: live push reports gaps 0 and import diff empty.
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T006 Run the system gates. Verify: 1 of 15 fails, vendor sync on `mcp-code-mode`.
- [x] T007 Validate this packet (`validate.sh --strict`). Verify: `RESULT: PASSED`.
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
