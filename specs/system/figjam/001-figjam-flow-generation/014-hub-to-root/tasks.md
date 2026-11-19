---
title: "Tasks: Phase 14: hub-to-root"
description: "Task Format: T### [P?] Description (file path)"
trigger_phrases:
  - "hub to root tasks"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.2 -->
# Tasks: Phase 14: hub-to-root

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

- [x] T001 Probe a copy of the repository with the hub at the root against both checkers to name every blocker
- [x] T002 Land the `repo-root-hub` extension in the shared checkers (Code_Environment `specs/sk-doc/068-hub-repo-folder-exemption`)
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T003 Recompute links in 68 files and move `product-owner/` to the root, with the hub benchmark files into `benchmark/`
- [x] T004 Declare `repo-root-hub` with the repository entries (mode-registry.json)
- [x] T005 Fix the hub layout, the `../` depths and the hub changelog (SKILL.md, ROUTER.md, changelog/v1.0.0.0.md, packet READMEs and SKILL.md files)
- [x] T006 Point the gates and scripts at the root (benchmark/gates/check_hub.py, run_gates.sh, rule_parity.py, benchmark/router/differential.py, route_contract.py, benchmark/format/validate-output-format.cjs, scripts/build-plugin.py)
- [x] T007 Update the docs and the outer Sync Loop declaration (README.md, benchmark/README.md, benchmark/gates/README.md, SYNC.md, systems.py, systems.cjs), and restore Commands/agent-router.md
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T008 Regenerate the leaf manifest and run the skilled checker and validator on the root and the packets
- [x] T009 Run run_gates.sh, the format gates, reference parity, the playbook validators, the plugin build and vendor-sync status
- [x] T010 Run the Sync Loop gates in the scratch clone and a link check
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

- [x] CHK-001 [P0] Requirements documented in spec.md [EVIDENCE: REQ-001 to REQ-004]
- [x] CHK-002 [P0] Technical approach defined in plan.md [EVIDENCE: plan.md Section 1]
- [x] CHK-003 [P1] Dependencies identified and available [EVIDENCE: the 068 checker change passes its suites]
<!-- /ANCHOR:pre-impl -->

---

<!-- ANCHOR:code-quality -->
## Code Quality

- [x] CHK-010 [P0] Scripts pass their self-tests [EVIDENCE: build-plugin.py self-test 8 of 8, check_hub.py self-test in run_gates.sh]
- [x] CHK-011 [P0] No errors or warnings [EVIDENCE: parent-skill-check 0 fail 0 warn]
- [x] CHK-012 [P1] Error handling kept [EVIDENCE: build-plugin.py still refuses symlinks]
- [x] CHK-013 [P1] Code follows project patterns [EVIDENCE: gates take paths from $PWD as before]
<!-- /ANCHOR:code-quality -->

---

<!-- ANCHOR:testing -->
## Testing Checklist

- [x] CHK-020 [P0] All acceptance criteria met [EVIDENCE: acceptance-criteria.md]
- [x] CHK-021 [P0] Gates run from the final tree [EVIDENCE: run_gates.sh all 12 gates pass]
- [x] CHK-022 [P1] Edge cases tested [EVIDENCE: plugin self-test proves a repository folder never ships]
- [x] CHK-023 [P1] Parity gates run [EVIDENCE: scratch clone run_parity.sh 39 of 39, run_residency.sh pass]
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:security -->
## Security

- [x] CHK-030 [P0] No secrets or board URLs added [EVIDENCE: the diff adds paths only]
- [x] CHK-031 [P0] Plugin copies only declared files [EVIDENCE: build from the registry's packets plus named hub files]
<!-- /ANCHOR:security -->

---

<!-- ANCHOR:docs -->
## Documentation

- [x] CHK-040 [P1] Spec, plan and tasks synchronized [EVIDENCE: this phase]
- [x] CHK-041 [P1] SYNC.md records the move [EVIDENCE: the 013 record describes the root hub and the product-owner/ detour]
- [x] CHK-042 [P2] README tree updated [EVIDENCE: README.md layout tree and checks table]
<!-- /ANCHOR:docs -->

---

<!-- ANCHOR:file-org -->
## File Organization

- [x] CHK-050 [P1] Temp files kept in the session scratchpad [EVIDENCE: hub_to_root.py and the probe live there]
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
