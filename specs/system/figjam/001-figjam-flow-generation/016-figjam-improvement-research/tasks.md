---
title: "Tasks: Phase 16: figjam-improvement-research"
description: "Task Format: T### [P?] Description (file path)"
trigger_phrases:
  - "figjam improvement research tasks"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.2 -->
# Tasks: Phase 16: figjam-improvement-research

<!-- SPECKIT_LEVEL: 2 -->

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

- [x] T001 Find new FigJam repos with gh search and pin each to a commit (research/corpus/)
- [x] T002 Copy the 009 corpus beside them (research/corpus/)
- [x] T003 Write the topic, the config and the fan-out matrix in the staging folder
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T004 Run the 10-iteration DeepSeek lineage with fanout-run.cjs (research/lineages/deepseek/)
- [x] T005 Merge the lineage with fanout-merge.cjs (research/findings-registry.json)
- [x] T006 Have a fresh Opus 5.5 high agent write the synthesis (research/research.md)
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T007 Count the iteration records and the SOURCE tags per iteration
- [x] T008 Spot-check three cited claims against their lines
- [x] T009 Copy research/ back, repoint staging paths, delete the staging folder and run validate.sh --strict
- [x] T010 Run 5 extra DeepSeek iterations on 2026-10-21 and copy the lineage to research/lineages/deepseek-extension/
- [x] T011 Have a fresh Opus 5.5 high agent write research/research.md Section 9
- [x] T012 Rerun the router probes and the repeated-label check that Section 9 rests on
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

## Verification Checklist

<!-- ANCHOR:protocol -->
## Verification Protocol

| Priority | Handling | Completion Impact |
|----------|----------|-------------------|
| **[P0]** | HARD BLOCKER | Cannot claim done until complete |
| **[P1]** | Required | Must complete OR get user approval |
| **[P2]** | Optional | Can defer with documented reason |
<!-- /ANCHOR:protocol -->

---

<!-- ANCHOR:pre-impl -->
## Pre-Implementation

- [x] CHK-001 [P0] Requirements documented in spec.md
- [x] CHK-002 [P0] Technical approach defined in plan.md
- [x] CHK-003 [P1] Dependencies identified and available
<!-- /ANCHOR:pre-impl -->

---

<!-- ANCHOR:code-quality -->
## Code Quality

- [x] CHK-010 [P0] No Product Owner source file changed
- [x] CHK-011 [P1] Every iteration cites at least one file
<!-- /ANCHOR:code-quality -->

---

<!-- ANCHOR:testing -->
## Testing Checklist

- [x] CHK-020 [P0] All acceptance criteria met
- [x] CHK-021 [P1] Three cited claims spot-checked
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:security -->
## Security

- [x] CHK-030 [P0] No secrets, board URLs or Barter flows in prompts or outputs
- [x] CHK-031 [P0] The corpus stays git-ignored
<!-- /ANCHOR:security -->

---

<!-- ANCHOR:docs -->
## Documentation

- [x] CHK-040 [P1] Spec, plan and tasks synchronized
<!-- /ANCHOR:docs -->

---

<!-- ANCHOR:file-org -->
## File Organization

- [x] CHK-050 [P1] Staging folder deleted after the copy
<!-- /ANCHOR:file-org -->

---

<!-- ANCHOR:summary -->
## Verification Summary

| Category | Total | Verified |
|----------|-------|----------|
| P0 Items | 6 | 6/6 |
| P1 Items | 5 | 5/5 |
| P2 Items | 0 | 0/0 |

**Verification Date**: 2026-10-20
<!-- /ANCHOR:summary -->
