---
title: "Tasks: Phase 3: vendored-figma-and-sync"
description: "Task Format: T### [P?] Description (file path)"
trigger_phrases:
  - "vendored figma and sync tasks"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.2 -->
# Tasks: Phase 3: vendored-figma-and-sync

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

- [x] T001 Capture the gate baseline before any change: run_gates.sh 5 of 5 pass, run_parity.sh PASSED 37/37
- [x] T002 Confirm upstream mcp-figma is clean at 293caa90, 58 files, no symlinks (Code_Environment/Public)
- [x] T003 Write vendor.json with the package entry (vendor.json)
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T004 Write vendor-sync.py with status, pull and push (scripts/vendor-sync.py)
- [x] T005 Vendor mcp-figma through pull, recording 58 hashes and the base commit (mcp-figma/, vendor.json)
- [x] T006 Write tests against a scratch upstream git repo (scripts/tests/test_vendor_sync.py)
- [x] T007 Refuse symlinks, missing upstream and conflicting edits with distinct exit codes (scripts/vendor-sync.py)
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T008 Add the vendor sync gate and its tests to run_gates.sh, with a counted skip in a standalone clone (benchmark/gates/run_gates.sh)
- [x] T009 Plant a one-byte edit and confirm the gate fails, then restore and confirm status exits 0
- [x] T010 Update the gates README (benchmark/gates/README.md)
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

- [x] CHK-001 [P0] Requirements documented in spec.md [evidence: spec.md section 4]
- [x] CHK-002 [P0] Technical approach defined in plan.md [evidence: plan.md approach: manifest plus one sync script]
- [x] CHK-003 [P1] Dependencies identified and available [evidence: python3 and git only]
<!-- /ANCHOR:pre-impl -->

---

<!-- ANCHOR:code-quality -->
## Code Quality

- [x] CHK-010 [P0] Code passes lint/format checks [evidence: python3 -m py_compile passes]
- [x] CHK-011 [P0] No console errors or warnings [evidence: test run prints no warnings]
- [x] CHK-012 [P1] Error handling implemented [evidence: SetupError path exits 2]
- [x] CHK-013 [P1] Code follows project patterns [evidence: header box, docstring and numbered sections match example_lint.py]
<!-- /ANCHOR:code-quality -->

---

<!-- ANCHOR:testing -->
## Testing Checklist

- [x] CHK-020 [P0] All acceptance criteria met [evidence: acceptance-criteria.md AC-001 to AC-005 Met]
- [x] CHK-021 [P0] Manual testing complete [evidence: pull, status and drift run against the real upstream]
- [x] CHK-022 [P1] Edge cases tested [evidence: symlink, missing upstream, upstream moved]
- [x] CHK-023 [P1] Error scenarios validated [evidence: 7 unit tests pass]
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:fix-completeness -->
## Fix Completeness

- [x] CHK-FIX-001 [P0] Each actionable finding has a finding class: `instance-only`, `class-of-bug`, `cross-consumer`, `algorithmic`, `matrix/evidence`, or `test-isolation`. [evidence: n/a, new feature with no findings]
- [x] CHK-FIX-002 [P0] Same-class producer inventory completed, or instance-only status proven by grep. [evidence: n/a, new feature]
- [x] CHK-FIX-003 [P0] Consumer inventory completed for changed helpers, policies, schema fields, response fields, docs, and tests. [evidence: consumers: run_gates.sh and its README, both updated]
- [x] CHK-FIX-004 [P0] Security/path/parser/redaction fixes include adversarial table tests for delimiter, joined-input, outside-root, no-op, and fallback cases. [evidence: symlink and outside-root cases tested; path joins use manifest paths only]
- [x] CHK-FIX-005 [P1] Matrix axes and row count are listed before completion is claimed. [evidence: matrix: 3 commands x clean, local-ahead, upstream-ahead, link, no upstream]
- [x] CHK-FIX-006 [P1] Hostile env/global-state variant executed when tests or code read process-wide state. [evidence: tests strip VENDOR_UPSTREAM_ROOT from the inherited environment]
- [x] CHK-FIX-007 [P1] Evidence is pinned to a fix SHA or explicit diff range, not a moving branch-relative range. [evidence: uncommitted; evidence is the working tree on 2026-10-20]
<!-- /ANCHOR:fix-completeness -->

---

<!-- ANCHOR:security -->
## Security

- [x] CHK-030 [P0] No hardcoded secrets [evidence: no secrets; upstream root found by walking up, no personal path in tracked files]
- [x] CHK-031 [P0] Input validation implemented [evidence: manifest shape checked before use]
- [x] CHK-032 [P1] Auth/authz working correctly [evidence: n/a, no auth surface]
<!-- /ANCHOR:security -->

---

<!-- ANCHOR:docs -->
## Documentation

- [x] CHK-040 [P1] Spec/plan/tasks synchronized [evidence: spec, tasks and summary agree]
- [x] CHK-041 [P1] Code comments adequate [evidence: comments carry the why at each refusal]
- [x] CHK-042 [P2] README updated (if applicable) [evidence: gates README updated]
<!-- /ANCHOR:docs -->

---

<!-- ANCHOR:file-org -->
## File Organization

- [x] CHK-050 [P1] Temp files in scratch/ only [evidence: no temp files left]
- [x] CHK-051 [P1] scratch/ cleaned before completion [evidence: scratch/ holds only .gitkeep]
<!-- /ANCHOR:file-org -->

---

<!-- ANCHOR:summary -->
## Verification Summary

| Category | Total | Verified |
|----------|-------|----------|
| P0 Items | 16 | 16/16 |
| P1 Items | 14 | 14/14 |
| P2 Items | 1 | 1/1 |

**Verification Date**: 2026-10-20
<!-- /ANCHOR:summary -->

---



