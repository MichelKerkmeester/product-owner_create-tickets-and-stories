---
title: "Tasks: Phase 13: skilled-hub-alignment"
description: "Task Format: T### [P?] Description (file path)"
trigger_phrases:
  - "skilled hub alignment tasks"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.2 -->
# Tasks: Phase 13: skilled-hub-alignment

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

- [x] T001 Run parent-skill-check.cjs and validate_skill_package.py --strict against the hub for a baseline: 39 failures, FAIL on both workflow packets
- [x] T002 Read the skilled parent-hub contract and the `mcp-tooling` hub it models, and ask the operator where the hub lives (answer: `product-owner/`)
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T003 Move `SKILL.md`, `mode-registry.json`, `hub-router.json` and the four packets into `product-owner/`
- [x] T004 Rewrite the registry and the hub router in the canonical schema, with the stage one rules as `routerPolicy.stageOneOrder` and the vendored packets as a declared extension (product-owner/mode-registry.json, hub-router.json)
- [x] T005 Write the thin hub and the stage two router (product-owner/SKILL.md, ROUTER.md)
- [x] T006 Add the hub metadata and companions (product-owner/description.json, graph-metadata.json, leaf-manifest.json, changelog/, manual-testing-playbook/, benchmark/)
- [x] T007 Move packet routing into each workflow packet's Section 2 and retire the packet router and identity files (sk-product-owner/SKILL.md, references/routing.md, sk-create-figjam/SKILL.md)
- [x] T008 Point every reader at the moved paths (benchmark/, scripts/, vendor.json, AGENTS.md, README.md, SYNC.md, claude project/README.md, the outer Sync Loop declaration and format validator, Commands/agent-router.md)
- [x] T009 Remap the playbook's links and line citations to the new files
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T010 Run the skilled checker and validator, run_gates.sh, the format gates, reference parity, the playbook validators, the plugin build, vendor-sync status and the Sync Loop gates in a scratch clone
- [x] T011 Run run_gates.sh in a standalone copy with no shared folders beside it, and grep for retired paths
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

- [x] CHK-001 [P0] Requirements documented in spec.md [EVIDENCE: spec.md REQ-001 to REQ-005]
- [x] CHK-002 [P0] Technical approach defined in plan.md [EVIDENCE: plan.md Sections 1 and 3]
- [x] CHK-003 [P1] Dependencies identified and available [EVIDENCE: the skilled checker and validator ran from the outer repo]
<!-- /ANCHOR:pre-impl -->

---

<!-- ANCHOR:code-quality -->
## Code Quality

- [x] CHK-010 [P0] Code passes lint/format checks [EVIDENCE: format gate exit 0 on four systems, PO validator passed across 47 source files]
- [x] CHK-011 [P0] No console errors or warnings [EVIDENCE: parent-skill-check 0 failures and 0 warnings. The sk-product-owner word-count advisory remains, see implementation-summary.md]
- [x] CHK-012 [P1] Error handling implemented [EVIDENCE: the two skilled gates skip with a reason when no shared skill folder is above the repository]
- [x] CHK-013 [P1] Code follows project patterns [EVIDENCE: hub shape follows mcp-tooling, validate_skill_package --strict PASS on all five packages]
<!-- /ANCHOR:code-quality -->

---

<!-- ANCHOR:testing -->
## Testing Checklist

- [x] CHK-020 [P0] All acceptance criteria met [EVIDENCE: acceptance-criteria.md AC-001 to AC-006 Met]
- [x] CHK-021 [P0] Manual testing complete [EVIDENCE: playbook validator 48 scenarios 0 violations, hub playbook 6 routing gold 0 violations]
- [x] CHK-022 [P1] Edge cases tested [EVIDENCE: standalone copy run_gates.sh 8 of 12 pass, 4 skipped, exit 0]
- [x] CHK-023 [P1] Error scenarios validated [EVIDENCE: check_hub.py --self-test 11 of 11 planted defects caught]
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:fix-completeness -->
## Fix Completeness

- [x] CHK-FIX-001 [P0] Each actionable finding has a finding class: `instance-only`, `class-of-bug`, `cross-consumer`, `algorithmic`, `matrix/evidence`, or `test-isolation`. [EVIDENCE: the 39 checker failures are one cross-consumer class, the hub location]
- [x] CHK-FIX-002 [P0] Same-class producer inventory completed, or instance-only status proven by grep. [EVIDENCE: grep for packet ROUTER.md and identity files outside specs returns only dated SYNC.md history]
- [x] CHK-FIX-003 [P0] Consumer inventory completed for changed helpers, policies, schema fields, response fields, docs, and tests. [EVIDENCE: T008 list, link check over the repository shows no broken link outside vendored and example files]
- [x] CHK-FIX-004 [P0] Security/path/parser/redaction fixes include adversarial table tests for delimiter, joined-input, outside-root, no-op, and fallback cases. [EVIDENCE: no path-handling code changed. build-plugin.py self-test 7 of 7 and vendor-sync tests still pass]
- [x] CHK-FIX-005 [P1] Matrix axes and row count are listed before completion is claimed. [EVIDENCE: 24 hub gold rows, 201 differential inputs, 6 hub playbook rows]
- [x] CHK-FIX-006 [P1] Hostile env/global-state variant executed when tests or code read process-wide state. [EVIDENCE: Sync Loop gates ran with a fresh PYTHONPYCACHEPREFIX in a scratch clone]
- [x] CHK-FIX-007 [P1] Evidence is pinned to a fix SHA or explicit diff range, not a moving branch-relative range. [EVIDENCE: uncommitted working tree on 2026-10-20, scratch clone commit amended from it]
<!-- /ANCHOR:fix-completeness -->

---

<!-- ANCHOR:security -->
## Security

- [x] CHK-030 [P0] No hardcoded secrets [EVIDENCE: no credential or board URL added, example URLs stay placeholders]
- [x] CHK-031 [P0] Input validation implemented [EVIDENCE: check_hub.py validates the registry, router and packets before replaying gold rows]
- [x] CHK-032 [P1] Auth/authz working correctly [EVIDENCE: not applicable, no auth surface changed]
<!-- /ANCHOR:security -->

---

<!-- ANCHOR:docs -->
## Documentation

- [x] CHK-040 [P1] Spec/plan/tasks synchronized [EVIDENCE: this file, plan.md and spec.md name the same files]
- [x] CHK-041 [P1] Code comments adequate [EVIDENCE: check_hub.py module docstring names the hub layout]
- [x] CHK-042 [P2] README updated (if applicable) [EVIDENCE: root README tree, routing and checks table updated]
<!-- /ANCHOR:docs -->

---

<!-- ANCHOR:file-org -->
## File Organization

- [x] CHK-050 [P1] Temp files in scratch/ only [EVIDENCE: backups and the scratch clone live in the session scratchpad]
- [x] CHK-051 [P1] scratch/ cleaned before completion [EVIDENCE: standalone copy removed, no .skilled or .opencode link left in the repository]
<!-- /ANCHOR:file-org -->

---

<!-- ANCHOR:summary -->
## Verification Summary

| Category | Total | Verified |
|----------|-------|----------|
| P0 Items | 12 | 12/12 |
| P1 Items | 13 | 13/13 |
| P2 Items | 1 | 1/1 |

**Verification Date**: 2026-10-20
<!-- /ANCHOR:summary -->

---



