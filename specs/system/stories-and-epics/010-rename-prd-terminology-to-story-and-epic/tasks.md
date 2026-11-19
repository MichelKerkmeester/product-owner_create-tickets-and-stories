---
title: "Tasks: Rename leftover PRD terminology to Story and Epic across the Product Owner skill, Claude Project, router benchmark and Sync Loop declaration"
description: "Task Format: T### [P?] Description (file path)"
trigger_phrases:
  - "rename prd terminology to story and epic tasks"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.2 -->
# Tasks: Rename leftover PRD terminology to Story and Epic across the Product Owner skill, Claude Project, router benchmark and Sync Loop declaration

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

- [x] T001 Classify every PRD mention as artifact name, input wording or history (grep over `claude project/`, `sk-product-owner/`, `AGENTS.md`, `README.md`)
- [x] T002 Map dependents outside the packagings (`benchmark/router/`, `systems.py`, episode walk-state)
- [x] T003 Back up `systems.py` to the scratchpad
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T004 `**PRD:**` value line to `**Story:**` (`references/story-mode.md`, `story-example-complete.md` and both mirrors)
- [x] T005 Rename the five examples to `story-example-*.md` and repoint `leaf-manifest.json`, `leaf-aliases.json`, both READMEs, `story-mode.md` and `systems.py`
- [x] T006 Router topic `prd` to `story` (`router-contract.md`, `Custom Instructions.md`, `route_contract.py`, `SKILL.md` topic table, corpus labels)
- [x] T007 Artifact-name prose through 47 exact phrase pairs, each skill line with its mirror, plus five README lines and one playbook citation
- [x] T008 Kernel v1.2.0, Skill v1.2.0.0, README version claims, `changelog/v1.2.0.0.md`, dated `SYNC.md` record
- [x] T009 Resync declared statements in `systems.py` until a pass reports 0
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T010 Router and format fixtures, reference parity
- [x] T011 Leaf metadata and sk-doc validation against HEAD baseline
- [x] T012 Residency and parity in a scratch clone against a HEAD baseline; red leg reports an edit made after a rename
- [x] T013 Rename-aware drift check (`validate_parity.py` `path_at_revision`), `prove_rename_drift.py`, Sync Loop README and feature catalog
- [x] T015 Fix pass: Story Mode Knowledge copy names examples by title (walk 0 findings), stale twenty-example sentence in the Router Contract, five missing `---` separators, five other systems' padding-only residency statements resynced and one HubSpot key recomputed
- [x] T014 Follow-up review: NUL-separated rename listing for non-ASCII paths, two README wording fixes, four v1.1.0-era declared statements resynced so Product Owner residency passes
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

- [x] CHK-001 [P0] Requirements documented in spec.md. Evidence: spec.md §4
- [x] CHK-002 [P0] Technical approach defined in plan.md. Evidence: plan.md §1
- [x] CHK-003 [P1] Dependencies identified and available. Evidence: plan.md §6
<!-- /ANCHOR:pre-impl -->

---

<!-- ANCHOR:code-quality -->
## Code Quality

- [x] CHK-010 [P0] Code passes lint/format checks. Evidence: `benchmark/format/run_fixtures.sh` exit 0, "PASSED all format-validator fixtures"
- [x] CHK-011 [P0] No console errors or warnings. Evidence: router run "PASSED 117/117 fixtures", "PASSED 189/189 differential inputs"
- [x] CHK-012 [P1] Error handling implemented. Evidence: N/A, no new control flow; the rename touches a dict key, a constant name and comments
- [x] CHK-013 [P1] Code follows project patterns. Evidence: `story-example-` matches the `doc-example-` and `task-example-` siblings
<!-- /ANCHOR:code-quality -->

---

<!-- ANCHOR:testing -->
## Testing Checklist

- [x] CHK-020 [P0] All acceptance criteria met. Evidence: acceptance-criteria.md, five rows Met
- [x] CHK-021 [P0] Manual testing complete. Evidence: residual grep shows only aliases, input wording, the `PRD -` ban and history
- [x] CHK-022 [P1] Edge cases tested. Evidence: fixtures for `$prd`, `$p`, `$prds` and "write a proper prd" pass
- [x] CHK-023 [P1] Error scenarios validated. Evidence: residency 5 findings, identical to the HEAD baseline
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:fix-completeness -->
## Fix Completeness

- [x] CHK-FIX-001 [P0] Each actionable finding has a finding class. Evidence: `class-of-bug`, stale artifact naming across mirrored files
- [x] CHK-FIX-002 [P0] Same-class producer inventory completed. Evidence: grep for `PRD` and `product requirements doc` over both packagings, `AGENTS.md` and READMEs
- [x] CHK-FIX-003 [P0] Consumer inventory completed. Evidence: `systems.py`, router benchmark, leaf manifests, walk-state checked
- [x] CHK-FIX-004 [P0] Adversarial cases. Evidence: N/A, no path, parser or security change
- [x] CHK-FIX-005 [P1] Matrix axes listed. Evidence: 47 phrase pairs with per-file hit counts
- [x] CHK-FIX-006 [P1] Hostile global state. Evidence: resync run with a fresh `PYTHONPYCACHEPREFIX`
- [x] CHK-FIX-007 [P1] Evidence pinned. Evidence: scratch-clone commit over HEAD `d10706fec`
<!-- /ANCHOR:fix-completeness -->

---

<!-- ANCHOR:security -->
## Security

- [x] CHK-030 [P0] No hardcoded secrets. Evidence: text-only edits
- [x] CHK-031 [P0] Input validation implemented. Evidence: N/A, no input surface added
- [x] CHK-032 [P1] Auth/authz working correctly. Evidence: N/A
<!-- /ANCHOR:security -->

---

<!-- ANCHOR:docs -->
## Documentation

- [x] CHK-040 [P1] Spec/plan/tasks synchronized. Evidence: this packet
- [x] CHK-041 [P1] Code comments adequate. Evidence: router comments say Story framing and Story request
- [x] CHK-042 [P2] README updated (if applicable). Evidence: both READMEs and the Project README carry v1.2.0
<!-- /ANCHOR:docs -->

---

<!-- ANCHOR:file-org -->
## File Organization

- [x] CHK-050 [P1] Temp files in scratch/ only. Evidence: backups and clones in the session scratchpad
- [x] CHK-051 [P1] scratch/ cleaned before completion. Evidence: scratch clones and backup removed
<!-- /ANCHOR:file-org -->

---

<!-- ANCHOR:summary -->
## Verification Summary

| Category | Total | Verified |
|----------|-------|----------|
| P0 Items | 12 | 12/12 |
| P1 Items | 13 | 13/13 |
| P2 Items | 1 | 1/1 |

**Verification Date**: 2026-10-17
<!-- /ANCHOR:summary -->

---
