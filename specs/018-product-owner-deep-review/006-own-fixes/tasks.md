---
title: "Tasks: Phase 6: Product Owner own fixes"
description: "Task Format: T### [P?] Description (file path)"
trigger_phrases:
  - "own fixes tasks"
importance_tier: "normal"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "018-product-owner-deep-review/006-own-fixes"
    last_updated_at: "2026-10-21T14:00:00Z"
    last_updated_by: "claude-code"
    recent_action: "Opened the fix phase"
    next_safe_action: "Apply the fixes"
    blockers: []
    key_files: []
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "1004bf13-7863-4447-a63e-6ad2f5fcfd86"
      parent_session_id: null
    completion_pct: 0
    open_questions: []
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.2 -->
# Tasks: Phase 6: Product Owner own fixes

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

- [x] T001 Reopen each finding's cited line before editing (review/ in phases 001 to 005)
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T002 Fix the sk-product-owner findings (sk-product-owner/)
- [x] T003 Fix the sk-create-figjam findings (sk-create-figjam/), R4-P2-003 recorded as not fixed
- [x] T004 Fix the hub, tooling and gate findings (AGENTS.md, ROUTER.md, SYNC.md, README.md, scripts/, benchmark/)
- [x] T005 Bring the Claude Project mirrors and kernel in step (claude project/)
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T006 Rerun every owning gate and validate this phase. All 12 run_gates.sh gates pass after the 007 pull
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
<!-- /ANCHOR:pre-impl -->

---

<!-- ANCHOR:code-quality -->
## Code Quality

- [x] CHK-010 [P0] Every changed script passes its own test or direct run [EVIDENCE: flow_check --self-test 156 of 156, test_vendor_sync 15 of 15, build-plugin --self-test exit 0]
<!-- /ANCHOR:code-quality -->

---

<!-- ANCHOR:testing -->
## Testing Checklist

- [x] CHK-020 [P0] All acceptance criteria met [EVIDENCE: acceptance-criteria.md, four rows Met]
- [x] CHK-021 [P1] Owning gates rerun from the final state [EVIDENCE: implementation-summary.md Verification]
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:security -->
## Security

- [x] CHK-030 [P0] No secrets, board URLs or Barter flows in changed files [EVIDENCE: the new scenarios use the fictional Loomlist fixtures only]
<!-- /ANCHOR:security -->

---

<!-- ANCHOR:docs -->
## Documentation

- [x] CHK-040 [P1] Spec, plan and tasks synchronized
<!-- /ANCHOR:docs -->

---

<!-- ANCHOR:file-org -->
## File Organization

- [x] CHK-050 [P1] Only the files named in spec.md changed [EVIDENCE: implementation-summary.md Files Changed]
<!-- /ANCHOR:file-org -->

---

<!-- ANCHOR:summary -->
## Verification Summary

| Category | Total | Verified |
|----------|-------|----------|
| P0 Items | 5 | 5/5 |
| P1 Items | 3 | 3/3 |
| P2 Items | 0 | 0/0 |

**Verification Date**: 2026-10-21
<!-- /ANCHOR:summary -->
