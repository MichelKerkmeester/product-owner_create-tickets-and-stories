---
title: "Tasks: Deal Templates upgrades for Product Owner"
description: "Task Format: T### [P?] Description (file path)"
trigger_phrases:
  - "deal templates upgrades tasks"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.2 -->
# Tasks: Deal Templates upgrades for Product Owner

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

- [x] T001 Map every surface that describes the reply (`AGENTS.md`, `SKILL.md`, Doc, Story and Interactive Mode, Quality Scoring, kernel)
- [x] T002 Record which lines the playbook cites, so edits stay in place
- [x] T003 Baseline every gate at HEAD
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T004 Fix the six failing Doc examples and their mirrors (`assets/examples/doc/`, `claude project/knowledge/`)
- [x] T005 Delivery Reply Shape, Section 3, both packagings (`assets/interactive-response-templates.md`)
- [x] T006 Point `AGENTS.md`, `SKILL.md`, the four references and the kernel at the shape; one question round; Open items
- [x] T007 Catalog grant in both validator twins, three fixtures, eight fixture cases (`validate-output-format.cjs`, `run_fixtures.sh`)
- [x] T008 Catalog grant prose (`references/doc-mode.md`, `assets/doc-templates.md`, mirrors)
- [x] T009 Example lint with self-test and gate runner (`benchmark/gates/example_lint.py`, `run_gates.sh`)
- [x] T010 Versions, READMEs, playbook expectations, `changelog/v1.2.1.0.md`, dated `SYNC.md` record
- [x] T011 Resync pairs written for the coordinator (`systems.py` not touched)
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T012 `run_gates.sh`, reference parity, Deal Templates, Copywriter and Sales Direct format fixtures
- [x] T013 Playbook validator, `validate_document.py` against HEAD, residency with a fresh `PYTHONPYCACHEPREFIX`
- [x] T014 Kernel size and `SKILL.md` word cap
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

- [x] CHK-010 [P0] Code passes lint/format checks. Evidence: `run_gates.sh` "all 5 gates pass"
- [x] CHK-011 [P0] No console errors or warnings. Evidence: router "PASSED 117/117", differential "189/189", format fixtures 59 cases pass
- [x] CHK-012 [P1] Error handling implemented. Evidence: the lint fails when it finds no file or fewer than three worked replies; the runner counts a missing gate as a failure
- [x] CHK-013 [P1] Code follows project patterns. Evidence: the runner and lint follow `rule_parity.py` and the existing fixture scripts
<!-- /ANCHOR:code-quality -->

---

<!-- ANCHOR:testing -->
## Testing Checklist

- [x] CHK-020 [P0] All acceptance criteria met. Evidence: acceptance-criteria.md, six rows Met
- [x] CHK-021 [P0] Manual testing complete. Evidence: grep sweep for the old reply wording and em dashes
- [x] CHK-022 [P1] Edge cases tested. Evidence: catalog violation and no-Index fixtures fail on the expected lines
- [x] CHK-023 [P1] Error scenarios validated. Evidence: `example_lint.py --self-test` passes 3 cases, a broken example and a broken reply both fail
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:fix-completeness -->
## Fix Completeness

- [x] CHK-FIX-001 [P0] Each actionable finding has a finding class. Evidence: `class-of-bug`, examples that fail the gate they model; reply described in four places
- [x] CHK-FIX-002 [P0] Same-class producer inventory completed. Evidence: every example and Project mirror runs through the lint, 42 files
- [x] CHK-FIX-003 [P0] Consumer inventory completed. Evidence: four systems' format fixtures, reference parity, playbook citations, residency rows
- [x] CHK-FIX-004 [P0] Adversarial cases. Evidence: heading with no ID, double dash, H2, missing Index all blocked by fixtures
- [x] CHK-FIX-005 [P1] Matrix axes listed. Evidence: heading and link, with and without Index, skill and Project packaging
- [x] CHK-FIX-006 [P1] Hostile global state. Evidence: residency run with a fresh `PYTHONPYCACHEPREFIX`
- [x] CHK-FIX-007 [P1] Evidence pinned. Evidence: uncommitted tree over HEAD `1c9befee8`
<!-- /ANCHOR:fix-completeness -->

---

<!-- ANCHOR:security -->
## Security

- [x] CHK-030 [P0] No hardcoded secrets. Evidence: text and gate scripts only
- [x] CHK-031 [P0] Input validation implemented. Evidence: N/A, no input surface added
- [x] CHK-032 [P1] Auth/authz working correctly. Evidence: N/A
<!-- /ANCHOR:security -->

---

<!-- ANCHOR:docs -->
## Documentation

- [x] CHK-040 [P1] Spec/plan/tasks synchronized. Evidence: this packet
- [x] CHK-041 [P1] Code comments adequate. Evidence: the validator, lint and runner comments carry the reason, with no packet ids
- [x] CHK-042 [P2] README updated (if applicable). Evidence: root, skill, Project and both benchmark READMEs
<!-- /ANCHOR:docs -->

---

<!-- ANCHOR:file-org -->
## File Organization

- [x] CHK-050 [P1] Temp files in scratch/ only. Evidence: self-test copies go to a temp dir it removes
- [x] CHK-051 [P1] scratch/ cleaned before completion. Evidence: temporary `.skilled` and `.opencode` links removed
<!-- /ANCHOR:file-org -->

---

<!-- ANCHOR:summary -->
## Verification Summary

| Category | Total | Verified |
|----------|-------|----------|
| P0 Items | 12 | 12/12 |
| P1 Items | 13 | 13/13 |
| P2 Items | 1 | 1/1 |

**Verification Date**: 2026-10-18
<!-- /ANCHOR:summary -->

---
