---
title: "Tasks: Phase 4: parent-hub-conversion"
description: "Task Format: T### [P?] Description (file path)"
trigger_phrases:
  - "parent hub conversion tasks"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.2 -->
# Tasks: Phase 4: parent-hub-conversion

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

- [x] T001 Capture the baseline before any change: router 117/117 and 189/189, format 59 fixtures, 26,358 o200k tokens for the default Task read set (scratch/base-*.txt)
- [x] T002 Capture the live baseline of the other three systems' format fixtures (155 each), reference parity (identical) and run_parity.sh (37/37)
- [x] T003 Build a scratch systems tree with Product Owner, the three format-gated systems and the Sync Loop folder, rsynced with `--exclude /export`
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T004 Run convert.py: hub SKILL.md, mode-registry.json, hub-router.json, ROUTER.md with the pointer left behind, AGENTS.md read order, differential.py, README tree, 23 playbook files remapped with 0 unresolved (scratch/convert.py)
- [x] T005 Write the hub check with the vendored exemption, five gold rows and a three-defect self-test, and add both to the gate runner (benchmark/gates/check_hub.py, benchmark/gates/run_gates.sh)
- [x] T006 Add the hub SKILL.md and ROUTER.md to both format validators' perimeter and HVR set (z — Claude Project Sync Loop/systems.cjs, validate-output-format.cjs, benchmark/format/validate-output-format.cjs)
- [x] T007 Trim the hub overhead from 432 to 286 tokens, then record the operator's criterion amendment (goal.md D4)
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T008 Apply the scratch build to the live trees as two patches and rerun every gate from the final state (scratch/hub.patch, scratch/sync-loop.patch)
- [x] T009 Plant an em dash in each new hub file and confirm both validators fail on it
- [x] T010 Document the hub check in the gates README and get a fresh review of the diff (benchmark/gates/README.md)
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
- [x] CHK-002 [P0] Technical approach defined in plan.md [evidence: scratch/convert.py and scratch/fixes.py, applied as one patch]
- [x] CHK-003 [P1] Dependencies identified and available [evidence: python3, node and tiktoken, all present]
<!-- /ANCHOR:pre-impl -->

---

<!-- ANCHOR:code-quality -->
## Code Quality

- [x] CHK-010 [P0] Code passes lint/format checks [evidence: python3 -m py_compile check_hub.py passes, both format validators pass on 42 sources]
- [x] CHK-011 [P0] No console errors or warnings [evidence: gate runs print no warnings]
- [x] CHK-012 [P1] Error handling implemented [evidence: check_hub.py reports unreadable JSON and missing keys as problems, never a traceback]
- [x] CHK-013 [P1] Code follows project patterns [evidence: check_hub.py follows example_lint.py: header box, docstring, PO_ROOT, --self-test]
<!-- /ANCHOR:code-quality -->

---

<!-- ANCHOR:testing -->
## Testing Checklist

- [x] CHK-020 [P0] All acceptance criteria met [evidence: acceptance-criteria.md AC-001 to AC-005 Met]
- [x] CHK-021 [P0] Manual testing complete [evidence: live run of every gate after the patch, implementation-summary.md:97-105]
- [x] CHK-022 [P1] Edge cases tested [evidence: 11 gold rows including negation, curly apostrophe and $ command cases]
- [x] CHK-023 [P1] Error scenarios validated [evidence: 5 planted defects each fail with their own message]
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:fix-completeness -->
## Fix Completeness

- [x] CHK-FIX-001 [P0] Each actionable finding has a finding class: `instance-only`, `class-of-bug`, `cross-consumer`, `algorithmic`, `matrix/evidence`, or `test-isolation`. [evidence: review findings classed in goal.md log: stage one rules algorithmic, stale mentions class-of-bug]
- [x] CHK-FIX-002 [P0] Same-class producer inventory completed, or instance-only status proven by grep. [evidence: grep for SKILL.md routing claims across the repo, every hit repointed or kept with a reason]
- [x] CHK-FIX-003 [P0] Consumer inventory completed for changed helpers, policies, schema fields, response fields, docs, and tests. [evidence: consumers of the router: differential.py, playbook citations, READMEs, both validators, AGENTS.md]
- [x] CHK-FIX-004 [P0] Security/path/parser/redaction fixes include adversarial table tests for delimiter, joined-input, outside-root, no-op, and fallback cases. [evidence: n/a, no path or parser security surface; stage one parsing has adversarial gold rows]
- [x] CHK-FIX-005 [P1] Matrix axes and row count are listed before completion is claimed. [evidence: matrix: signal x artifact word x $ command x negation position, 11 rows]
- [x] CHK-FIX-006 [P1] Hostile env/global-state variant executed when tests or code read process-wide state. [evidence: self-test runs against a temp copy through PO_ROOT, never the live tree]
- [x] CHK-FIX-007 [P1] Evidence is pinned to a fix SHA or explicit diff range, not a moving branch-relative range. [evidence: uncommitted; evidence pinned to scratch/hub.patch and scratch/sync-loop.patch]
<!-- /ANCHOR:fix-completeness -->

---

<!-- ANCHOR:security -->
## Security

- [x] CHK-030 [P0] No hardcoded secrets [evidence: no secrets or file keys in any changed file]
- [x] CHK-031 [P0] Input validation implemented [evidence: registry and router JSON shapes checked before use]
- [x] CHK-032 [P1] Auth/authz working correctly [evidence: n/a, no auth surface]
<!-- /ANCHOR:security -->

---

<!-- ANCHOR:docs -->
## Documentation

- [x] CHK-040 [P1] Spec/plan/tasks synchronized [evidence: spec, tasks, summary and acceptance criteria agree]
- [x] CHK-041 [P1] Code comments adequate [evidence: comments carry the why at each rule]
- [x] CHK-042 [P2] README updated (if applicable) [evidence: root, skill, router and gates READMEs updated]
<!-- /ANCHOR:docs -->

---

<!-- ANCHOR:file-org -->
## File Organization

- [x] CHK-050 [P1] Temp files in scratch/ only [evidence: temp builds lived in the session scratchpad; scratch/ holds only the build scripts, baselines and patches]
- [ ] CHK-051 [P1] scratch/ cleaned before completion [deferred: scratch/ keeps the two patches for rollback until the operator commits, then it is emptied as in 003]
<!-- /ANCHOR:file-org -->

---

<!-- ANCHOR:summary -->
## Verification Summary

| Category | Total | Verified |
|----------|-------|----------|
| P0 Items | 13 | 13/13 |
| P1 Items | 14 | 13/14 |
| P2 Items | 1 | 1/1 |

**Verification Date**: 2026-10-20
<!-- /ANCHOR:summary -->

---



