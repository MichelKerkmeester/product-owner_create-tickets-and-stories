---
title: "Tasks: Phase 15: figjam-rebuild"
description: "Task Format: T### [P?] Description (file path)"
trigger_phrases:
  - "figjam rebuild tasks"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.2 -->
# Tasks: Phase 15: figjam-rebuild

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

- [x] T001 Read sk-design-diagram's intake, style guide, quality rubric and derivation record and the phase 009 research corpus
- [x] T002 Probe the vendored extractor on every type and record where it misreads one
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T003 Rewrite the check with a rule module per type and planted fixtures (sk-create-figjam/scripts/flow_check.py, scripts/figjam_checks/)
- [x] T004 Write the style guide, quality rubric and hybrid workflow (sk-create-figjam/references/)
- [x] T005 Write a reference per type and rewrite the workflow (sk-create-figjam/references/types/, flow-mode.md)
- [x] T006 Write a template per type past the user flow and a worked example per type (sk-create-figjam/assets/templates/, assets/examples/)
- [x] T007 Update the packet routing, README and changelog (sk-create-figjam/SKILL.md, README.md, changelog/v1.0.0.0.md)
- [x] T008 Update the hub wording, keywords, gold rows, manifest and a routing scenario (SKILL.md, ROUTER.md, AGENTS.md, README.md, description.json, graph-metadata.json, mode-registry.json, benchmark/hub-routing-cases.json, manual-testing-playbook/)
- [x] T009 Write the packet playbook (sk-create-figjam/manual-testing-playbook/)
- [x] T010 Widen the FLOW patterns with fixtures and corpus rows (claude project/Custom Instructions.md, sk-product-owner/references/router-contract.md, benchmark/router/)
- [x] T011 Mirror into the Project and record it (claude project/, systems.py, systems.cjs, validate_parity.py, rule_parity.py, SYNC.md)
- [x] T012 Remap shifted playbook citations (sk-product-owner/manual-testing-playbook/)
- [x] T016 Bring the packet playbook to the full sk-doc contract and extend it to every type, scored board quality and creation variants, the boundaries and routing gold (sk-create-figjam/manual-testing-playbook/, benchmark/hub-routing-cases.json)
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T013 Run the self-test, the skilled checkers and run_gates.sh
- [x] T014 Run the format gates, reference parity, the playbook validators and the plugin build
- [x] T015 Run the Sync Loop gates in the scratch clone
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

- [x] CHK-001 [P0] Requirements documented in spec.md [EVIDENCE: REQ-001 to REQ-006]
- [x] CHK-002 [P0] Technical approach defined in plan.md [EVIDENCE: plan.md Section 3]
- [x] CHK-003 [P1] Dependencies identified and available [EVIDENCE: the extractor probe named four misreads, handled by the check's own parsers]
<!-- /ANCHOR:pre-impl -->

---

<!-- ANCHOR:code-quality -->
## Code Quality

- [x] CHK-010 [P0] Scripts pass their self-tests [EVIDENCE: flow_check.py 148 of 148, 134 of 134 inside the plugin, example lint self-test 3 of 3]
- [x] CHK-011 [P0] No errors or warnings [EVIDENCE: parent-skill-check 0 failures 0 warnings]
- [x] CHK-012 [P1] Error handling kept [EVIDENCE: an unreadable file exits 2 and an undrawable block exits 1 with a pointer to the type table]
- [x] CHK-013 [P1] Code follows project patterns [EVIDENCE: the vendored extractor stays a byte copy, vendor-sync status clean in run_gates.sh]
<!-- /ANCHOR:code-quality -->

---

<!-- ANCHOR:testing -->
## Testing Checklist

- [x] CHK-020 [P0] All acceptance criteria met [EVIDENCE: acceptance-criteria.md]
- [x] CHK-021 [P0] Gates run from the final tree [EVIDENCE: run_gates.sh all 12 gates pass]
- [x] CHK-022 [P1] Edge cases tested [EVIDENCE: a pie block and an aliased sequence fail with exit 1, the playbook FJ-005 and FJ-006]
- [x] CHK-023 [P1] Parity gates run [EVIDENCE: scratch clone run_parity.sh 62 of 62, run_residency.sh pass]
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:security -->
## Security

- [x] CHK-030 [P0] No secrets, board URLs or Barter flows added [EVIDENCE: examples use Fernhouse, Loomlist and Roamstay and the placeholder board URL]
- [x] CHK-031 [P0] Plugin copies only declared files [EVIDENCE: build-plugin.py self-test passes]
<!-- /ANCHOR:security -->

---

<!-- ANCHOR:docs -->
## Documentation

- [x] CHK-040 [P1] Spec, plan and tasks synchronized [EVIDENCE: this phase]
- [x] CHK-041 [P1] SYNC.md records the mirror [EVIDENCE: the dated 2026-10-20 record on every FigJam diagram]
- [x] CHK-042 [P2] README counts updated [EVIDENCE: 62 Knowledge files, 125 fixtures, 204 differential inputs, 33 gold rows]
<!-- /ANCHOR:docs -->

---

<!-- ANCHOR:file-org -->
## File Organization

- [x] CHK-050 [P1] Temp files kept in the session scratchpad [EVIDENCE: the mirror transform, the playbook generator and probe models live there]
- [x] CHK-051 [P1] No temporary links left [EVIDENCE: no .skilled or .opencode link at the root]
<!-- /ANCHOR:file-org -->

---

<!-- ANCHOR:summary -->
## Verification Summary

| Category | Total | Verified |
|----------|-------|----------|
| P0 Items | 8 | 8/8 |
| P1 Items | 9 | 9/9 |
| P2 Items | 1 | 1/1 |

**Verification Date**: 2026-10-20
<!-- /ANCHOR:summary -->
