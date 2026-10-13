---
title: "Tasks: Phase 9, template forms and checklists"
description: "Task Format: T### [P?] Description (file path)"
trigger_phrases:
  - "template forms tasks"
  - "checklist bracket tasks"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.2 -->
# Tasks: Phase 9, template forms and checklists

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

- [x] T001 Scaffold this phase and bind it in the parent's goal and phase map (`../goal.md`, `../spec.md`) [EVIDENCE: D11 in the parent goal, slice 3991 of 4000 chars; phase map row 9]
- [x] T002 Snapshot the 78 exports and 21 examples before the conversion (`scratch/before/`) [EVIDENCE: 78 export files and 21 examples under task, story, doc and bug]
- [x] T003 Write and prove the transform script (`scratch/transform.py`) [EVIDENCE: `--check` passes a clean conversion; a heading left at `###` and an added word are each caught]
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T004 Move the five templates to the new forms (`sk-product-owner/assets/`) [EVIDENCE: Story v0.101, Epic v0.102, Task v0.103, Bug v0.102, Doc v0.109; each edit on its own line]
- [x] T005 Move the Story, Task, Bug, Doc and Interactive Mode references, Quality Scoring, `SKILL.md` and `AGENTS.md` to the new forms and wording (`sk-product-owner/references/`) [EVIDENCE: Story Mode v0.405, Task Mode v0.307, Bug Mode v0.205, Doc Mode v0.112, Interactive Mode v0.408, Quality Scoring v0.101; "build checklist" reads "build steps"]
- [x] T006 Update the kernel and every knowledge mirror, renaming each bumped mirror (`claude project/`) [EVIDENCE: kernel v0.20.0 lines 84, 138, 140, 193; 11 mirrors renamed with `git mv` and repointed; 17 example mirrors converted]
- [x] T007 Teach both validators `[]`, invert the Requirements rule and add the keyed `[ ]` rule (`validate-output-format.cjs` twice, `systems.cjs`) [EVIDENCE: identical logic in both copies; the `[ ]` rule keyed to Product Owner artifacts only]
- [x] T008 Update the fixtures in both folders and wire the new cases into both runners (`fixtures/`, `run_fixtures.sh`) [EVIDENCE: 9 fixtures changed, `checkbox-form-violation.md` added; `cmp` identical]
- [x] T009 Resync the residency declaration to the new kernel and Doc Mode text (`systems.py`) [EVIDENCE: 16 findings resolved; the resync repeated with a fresh bytecode cache until it reported 0]
- [x] T010 [P] Convert the 78 exports and 17 changed examples (`export/benchmark/`, `sk-product-owner/assets/examples/`) [EVIDENCE: `scratch/verify-exports.txt` checked 78 fails 0; `scratch/verify-examples.txt` checked 21 fails 0]
- [x] T011 [P] Update the playbook scenarios and root (`manual-testing-playbook/`) [EVIDENCE: 38 scenario files carry the new forms and 42 in all, the rest repointed mirror links only; `story-refinement` Pass rule names `- []` constraint items; root 2.5.0.0]
- [x] T012 Bump the versions and record the change (`SKILL.md`, READMEs, `description.json`, changelog v0.17.0.0, `SYNC.md`, run README) [EVIDENCE: skill 0.17.0, kernel v0.20.0, SYNC.md note with the review pending, run README Template forms section]
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T013 Gate, fixtures, parity, residency precheck, rule parity, playbook validator and selftest on the working tree [EVIDENCE: 40 sources and 78 exports exit 0; Copywriter, Deal and Sales 131 pass each, Product Owner 129 via the shared runner and PASSED on its own; reference parity identical; residency precheck PASSED 7 systems; rule parity PASSED; 46 scenarios 0 violations; selftest 7 of 7]
- [x] T014 Commit in both repos, then parity and residency on the commit [EVIDENCE: Product Owner 0d085cb (195 files), Barter b6ac9d86 (210 files), every hook passed with no bypass; `validate_parity.py product-owner` PASSED 38/38, `run_residency.sh product-owner` PASSED]
- [x] T015 Push on the operator's go-ahead [EVIDENCE: Product Owner bb9210f..0d085cb; Barter 0b08add1..b6ac9d86 through the Barter account, every pre-push hook passed with no bypass]
<!-- /ANCHOR:phase-3 -->

---

<!-- ANCHOR:completion -->
## Completion Criteria

- [x] All tasks marked `[x]`
- [x] No `[B]` blocked tasks remaining
- [x] Every converted file checked against its snapshot
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

- [x] CHK-001 [P0] Operator decisions recorded before any edit: Epic, exports, checkbox scope, requirement content [EVIDENCE: Epic too with Goal, convert all 78, `[]` everywhere, constraints with the new marker, answered 2026-09-26]
- [x] CHK-002 [P0] The exports and examples snapshotted before the conversion [EVIDENCE: scratch/before/, 78 exports and 21 examples]
- [x] CHK-003 [P1] The transform check proven to pass a clean file and catch planted faults [EVIDENCE: a heading left at `###` and an added word caught]
<!-- /ANCHOR:pre-impl -->

---

<!-- ANCHOR:code-quality -->
## Code Quality

- [x] CHK-010 [P0] The two validators give identical output on every fixture [EVIDENCE: `reference-parity.cjs` identical; fixture folders `cmp` identical, 16 files each]
- [x] CHK-011 [P0] No line a scenario cites moved [EVIDENCE: every template and reference edit stayed on its own line]
- [x] CHK-012 [P1] The `[ ]` rule touches no source and no other system [EVIDENCE: keyed `checkboxForm` sources off; `check_core` Copywriter case silent]
- [x] CHK-013 [P1] No ephemeral label in a code comment [EVIDENCE: the `systems.cjs` comment states the reason only]
<!-- /ANCHOR:code-quality -->

---

<!-- ANCHOR:testing -->
## Testing Checklist

- [x] CHK-020 [P0] Every converted file differs from its snapshot only by allowed transforms [EVIDENCE: verify-exports.txt 78 fails 0, verify-examples.txt 21 fails 0]
- [x] CHK-021 [P0] Format gate exit 0 on the sources and every export [EVIDENCE: 40 sources, 78 exports]
- [x] CHK-022 [P0] The new rules catch every old form on the snapshot [EVIDENCE: 815 `[ ]` lines and 290 plain Requirements bullets found, 75 files fail]
- [x] CHK-023 [P0] Playbook validator reports 0 violations [EVIDENCE: PASS scenarios=46 violations=0]
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:fix-completeness -->
## Fix Completeness

- [x] CHK-FIX-001 [P0] The `[]` gap is classed `class-of-bug`: every checkbox regex in the gate reads both forms [EVIDENCE: `CHECKBOX_ITEM`, the container strip, the length-caps strip and `MARK_AS_DONE`]
- [x] CHK-FIX-002 [P0] Both packagings carry the new forms [EVIDENCE: SKILL.md rules 9 to 11 and kernel lines 84, 138, 140]
- [x] CHK-FIX-003 [P1] Every consumer of the renamed mirrors repointed [EVIDENCE: `repoint_rename.py` per mirror; `carrier_query_evidence.py` and `residency/backlog.md` updated]
- [x] CHK-FIX-004 [P1] Evidence pinned to the commit that lands this phase [EVIDENCE: Product Owner 0d085cb, Barter b6ac9d86]
<!-- /ANCHOR:fix-completeness -->

---

<!-- ANCHOR:security -->
## Security

- [x] CHK-030 [P0] No credentials in any changed file, and the exports carry fixture data only [EVIDENCE: the transform changes markers and headings only]
- [x] CHK-031 [P1] Public repo commit carries no attribution line [EVIDENCE: 0d085cb message has no attribution line]
<!-- /ANCHOR:security -->

---

<!-- ANCHOR:docs -->
## Documentation

- [x] CHK-040 [P0] The changelog names the ClickUp rendering risk [EVIDENCE: v0.17.0.0 Known risk section]
- [x] CHK-041 [P0] No `SYNC.md` note marks the v0.20.0 review done [EVIDENCE: the note says the review of kernel v0.20.0 is pending]
- [x] CHK-042 [P1] Spec, plan and tasks synchronized [EVIDENCE: all three describe the five forms, the gate changes and the 78 exports]
- [x] CHK-043 [P2] Parent spec phase map updated to Complete [EVIDENCE: parent spec.md phase map row 9 Complete]
<!-- /ANCHOR:docs -->

---

<!-- ANCHOR:file-org -->
## File Organization

- [x] CHK-050 [P1] Snapshot, scripts and check output kept in scratch/ only [EVIDENCE: before/, transform.py, sync_mirror.py, build_resync.py, precheck_residency.py, edit.py, pair files, verify-*.txt]
- [x] CHK-051 [P1] scratch/ holds nothing temporary [EVIDENCE: every file there is a tool or evidence the criteria cite]
<!-- /ANCHOR:file-org -->

---

<!-- ANCHOR:summary -->
## Verification Summary

| Category | Total | Verified |
|----------|-------|----------|
| P0 Items | 13 | 13/13 |
| P1 Items | 9 | 9/9 |
| P2 Items | 1 | 1/1 |

**Verification Date**: 2026-09-26
<!-- /ANCHOR:summary -->

---
