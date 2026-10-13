---
title: "Tasks: Phase 8, cut the exports and set a word budget"
description: "Task Format: T### [P?] Description (file path)"
trigger_phrases:
  - "cut exports tasks"
  - "word budget tasks"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.2 -->
# Tasks: Phase 8, cut the exports and set a word budget

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

- [x] T001 Scaffold this phase and bind it in the parent's goal and phase map (`../goal.md`, `../spec.md`) [EVIDENCE: D9 and D10 in the parent goal, slice 3979 of 4000 chars; phase map row 8]
- [x] T002 Snapshot the 78 exports before the cut (`scratch/before-cut/`) [EVIDENCE: 78 files copied from export/benchmark after phase 007]
- [x] T003 Write and prove the verify script (`scratch/verify_cut.py`) [EVIDENCE: identity run 78 of 78 pass at 0% cut; a dropped Given/When/Then line, a dropped number and a changed heading each caught]
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T004 [P] Cut the 78 exports in seven balanced groups, round one (`export/benchmark/`) [EVIDENCE: scratch/verify-round1.txt, 78 of 78 pass, words 73942 to 62906, 14.9%]
- [x] T005 [P] Second round at the depth one group reached, with table body rows opened to tightening [EVIDENCE: operator chose it; scratch/verify-round2.txt, 78 of 78 pass, 23.2%]
- [x] T006 [P] Fact review of every file against its snapshot, and repair of each finding (`scratch/fact-review-g1.md` to `-g7.md`) [EVIDENCE: 81 findings, 75 restored by the writers, 6 left as color or a subtask restating its parent]
- [x] T007 Match the Doc template's dashes in the two PDK-003 Docs [EVIDENCE: 32 label dashes and 7 Status-line dashes restored, operator chose "Match the template"]
- [x] T008 Set the word budget from the cut counts on `SKILL.md` line 276, kernel line 90 and the playbook Size band row [EVIDENCE: bundle task 500, subtask 750, task 900, bug 800, Epic 1,000, Story and Doc 1,400; 68 of 78 fit; each edit stayed on its line]
- [x] T009 Bump the versions and record the change (`SKILL.md`, kernel, READMEs, `description.json`, changelog v0.16.0.0, `SYNC.md`) [EVIDENCE: skill 0.16.0, kernel v0.19.0, playbook 2.4.0.0, SYNC.md note with the review pending]
- [x] T010 Record the second edit in the run README [EVIDENCE: Second edit section and updated Next steps, every paragraph within the caps]
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T011 Verify, format gate, parity, residency, playbook validator, selftest and collector dry run on the working tree [EVIDENCE: 78 of 78, 22.7%; 40 sources and 78 exports pass the gate; parity 38/38; residency PASSED; 46 scenarios 0 violations; selftest 7 of 7; dry run keeps all 78]
- [x] T012 Commit in both repos, then parity and residency on the commit [EVIDENCE: Product Owner bb9210f, Barter 0b08add1 (89 files each); the Barter commit skipped mirror-parity once on the operator's approval, since a parallel session's uncommitted markdown-agent edit in Code_Environment left its Codex mirror stale; parity 38/38 and residency PASSED on the commit]
- [x] T013 Push on the operator's go-ahead [EVIDENCE: Product Owner e042272..bb9210f; Barter c6493c1b..0b08add1, every pre-push hook passed with no bypass]
<!-- /ANCHOR:phase-3 -->

---

<!-- ANCHOR:completion -->
## Completion Criteria

- [x] All tasks marked `[x]`
- [x] No `[B]` blocked tasks remaining
- [x] Every cut export verified, fact-reviewed and repaired
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

- [x] CHK-001 [P0] Operator decisions recorded before any edit: local copies, strength, files, rules [EVIDENCE: all 46 local copies, about 30%, all 78 files, a word budget, answered 2026-09-26]
- [x] CHK-002 [P0] The 78 exports snapshotted before the cut [EVIDENCE: scratch/before-cut/, 78 files]
- [x] CHK-003 [P1] The verify script proven to pass a clean file and catch planted faults [EVIDENCE: identity 78 of 78 at 0%, three planted faults caught]
<!-- /ANCHOR:pre-impl -->

---

<!-- ANCHOR:code-quality -->
## Code Quality

- [x] CHK-010 [P0] The budget reads the same in `SKILL.md`, the kernel and the playbook root, and the shared card is unchanged [EVIDENCE: "a subtask 750" found once in each of SKILL.md, the kernel, the root, SYNC.md and the changelog; z — Knowledge card untouched, parity 38/38]
- [x] CHK-011 [P0] No line a scenario cites moved [EVIDENCE: git diff -U0 hunks @@ -276 +276, @@ -90 +90, @@ -209 +209]
- [x] CHK-012 [P1] The budget never fails a scenario [EVIDENCE: it sits in the root's Advisory Size band row, which reads "Never a failure"]
- [x] CHK-013 [P1] The collector keeps the cut files [EVIDENCE: dry run prints a keep warning for all 78]
<!-- /ANCHOR:code-quality -->

---

<!-- ANCHOR:testing -->
## Testing Checklist

- [x] CHK-020 [P0] Every cut export keeps its fixed lines, values, numbers and links [EVIDENCE: scratch/verify-final.txt, 78 of 78]
- [x] CHK-021 [P0] Format gate exit 0 on the sources and every export [EVIDENCE: 40 sources, 78 exports, 0 failures]
- [x] CHK-022 [P0] Playbook validator reports 0 violations [EVIDENCE: PASS scenarios=46 violations=0]
- [x] CHK-023 [P1] Words before and after reported [EVIDENCE: 73942 to 57138, 22.7%, in the README Second edit section]
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:fix-completeness -->
## Fix Completeness

- [x] CHK-FIX-001 [P0] The length gap is classed `class-of-bug`: no rule bounded a whole artifact, so every kind gets a budget [EVIDENCE: task, subtask, bundle task, bug, Epic, Story and Doc each named]
- [x] CHK-FIX-002 [P0] Both packagings carry the budget [EVIDENCE: SKILL.md line 276 and kernel line 90 carry the same sentence]
- [x] CHK-FIX-003 [P1] Every consumer of the export files checked: README, collector, grading citations [EVIDENCE: README Second edit, collector keeps edited files, verdicts still cite the graded originals]
- [x] CHK-FIX-004 [P1] Evidence pinned to the commit that lands this phase [EVIDENCE: Product Owner bb9210f, Barter 0b08add1]
<!-- /ANCHOR:fix-completeness -->

---

<!-- ANCHOR:security -->
## Security

- [x] CHK-030 [P0] No credentials committed, and the exports carry fixture data only [EVIDENCE: Roamstay, Loomlist and Fernhouse fixture data only]
- [x] CHK-031 [P1] Public repo commit carries no attribution line [EVIDENCE: bb9210f message has no attribution line]
<!-- /ANCHOR:security -->

---

<!-- ANCHOR:docs -->
## Documentation

- [x] CHK-040 [P0] The report says the exports were cut after grading and that verdicts cite the graded originals [EVIDENCE: README Second edit, third paragraph]
- [x] CHK-041 [P0] No `SYNC.md` note marks the v0.19.0 review done [EVIDENCE: the note says the review of kernel v0.19.0 is pending]
- [x] CHK-042 [P1] Spec, plan and tasks synchronized [EVIDENCE: spec, plan, tasks and criteria describe two rounds, the fact review and the split subtask budget]
- [x] CHK-043 [P2] Parent spec phase map updated to Complete [EVIDENCE: parent spec.md phase map row 8 Complete]
<!-- /ANCHOR:docs -->

---

<!-- ANCHOR:file-org -->
## File Organization

- [x] CHK-050 [P1] Snapshot, briefs, verify script and reviews kept in scratch/ only [EVIDENCE: before-cut/, groups/, cut-brief.md, fact-review-brief.md, verify_cut.py, verify-*.txt, fact-review-g*.md]
- [x] CHK-051 [P1] scratch/ holds nothing temporary [EVIDENCE: every file there is evidence the criteria cite]
<!-- /ANCHOR:file-org -->

---

<!-- ANCHOR:summary -->
## Verification Summary

| Category | Total | Verified |
|----------|-------|----------|
| P0 Items | 12 | 12/12 |
| P1 Items | 11 | 11/11 |
| P2 Items | 1 | 1/1 |

**Verification Date**: 2026-09-26
<!-- /ANCHOR:summary -->

---
