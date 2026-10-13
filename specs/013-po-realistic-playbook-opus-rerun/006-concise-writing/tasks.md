---
title: "Tasks: Phase 6, concise writing"
description: "Task Format: T### [P?] Description (file path)"
trigger_phrases:
  - "concise writing tasks"
  - "export rewrite tasks"
  - "length cap verification"
  - "phase 6 tasks"
importance_tier: "important"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.2 -->
# Tasks: Phase 6, concise writing

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

- [x] T001 Scaffold this phase and bind it in the parent's goal and phase map (`../goal.md`, `../spec.md`) [EVIDENCE: phase docs written, parent binding and phase map carry 006, chat slice resent at 3733 chars]
- [x] T002 Snapshot the 98 graded exports and the over-cap counts (`scratch/before/`, `scratch/caps-before.txt`) [EVIDENCE: scratch/before/ holds 98 files, byte-identical to Product Owner e9edb95 and Barter 7652158c; scratch/caps-before.txt]
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T003 Add the caps to `SKILL.md` line 276 and kernel line 90, then skill 0.15.0, kernel v0.18.0, changelog and `SYNC.md` note [EVIDENCE: SKILL.md line 276 and kernel line 90 changed in place; skill 0.15.0, kernel v0.18.0, changelog v0.15.0.0, SYNC.md note with the review pending]
- [x] T004 Add the length-cap warning to the format gate for product-owner artifacts, with two fixtures (`z — Claude Project Sync Loop/`) [EVIDENCE: lengthCapFindings in both validators, lengthCaps key in systems.cjs, two fixtures, four suites PASSED, reference parity identical]
- [x] T005 Append the caps to the root's Advisory Size band row, root 2.3.0.0 (`manual-testing-playbook.md`) [EVIDENCE: root line 209 changed in place, version 2.3.0.0, validator 46 scenarios 0 violations]
- [x] T006 [P] Rewrite the 98 exports to the caps in five Opus batches (`export/benchmark/`) [EVIDENCE: five Opus agents edited 80 files and left 18 unchanged; over-cap lines 623 in 78 files to 7 in 7]
- [x] T007 Verify each rewrite against its snapshot: headings, backticked spans, numbers, caps, gate, em dashes (`scratch/verify_rewrite.py`) [EVIDENCE: verify_rewrite.py --all: 98 of 98 passed, 7 KEPT About openings; scratch/verify-after.txt]
- [x] T014 Review every changed hunk for a dropped, changed or added fact the script cannot see, and repair each (`scratch/fact-review-*.md`) [EVIDENCE: fact-review-a.md, -b.md and -c.md: seven findings across 98 files, all repaired and reverified]
- [x] T008 Rewrite the report prose and label the edited exports (`README.md`, `results.md`, grading-notes review sections) [EVIDENCE: README sections 1 to 5, the four review sections and Edited after grading meet the caps, 0 em dashes]
- [x] T009 Make the collector skip edited targets and collect rounds only with `--rounds` (`run/collect_exports.py`) [EVIDENCE: --rounds and the edit guard; selftest 7 of 7, collector 19 checks, both new checks fail on the old collector; dry run keeps 80 edited files and lists no round]
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T010 Format gate, fixtures, playbook validator and selftest pass on the working tree [EVIDENCE: source gate exit 0, 98 exports 0 gate failures, fixtures PASSED in four systems, playbook validator PASS, selftest 7 of 7]
- [x] T011 Commit in both repos with the 102 deletions, then parity and residency on the commit [EVIDENCE: Product Owner fdc8a28 (203 files), Barter 48ca7a3f (209 files); validate_parity.py 38/38 PASSED, run_residency.sh PASSED on the commit]
- [x] T012 `validate.sh --recursive` passes and every phase reads `Closeable: Yes` [EVIDENCE: validate.sh --recursive --strict RESULT: PASSED in every folder]
- [x] T013 Push on the operator's go-ahead [EVIDENCE: operator chose Push both, then authorized the mass-deletion gate for 102 round exports; Product Owner 3fdce37..fdc8a28, Barter d214c160..48ca7a3f]
<!-- /ANCHOR:phase-3 -->

---

<!-- ANCHOR:completion -->
## Completion Criteria

- [x] All tasks marked `[x]`
- [x] No `[B]` blocked tasks remaining
- [x] Every rewritten export verified and every gate green
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

- [x] CHK-001 [P0] Operator decisions recorded before any source edit: scope, caps strength, deletion, spec folder [EVIDENCE: scope, strength, deletion and spec folder answered 2026-09-26 in plan mode; caps home answered before any rule edit]
- [x] CHK-002 [P0] The 98 graded exports snapshotted before the rewrite [EVIDENCE: scratch/before/, 98 files, cmp against e9edb95 and 7652158c 0 differ]
- [x] CHK-003 [P1] Over-cap counts measured before the rewrite [EVIDENCE: scratch/caps-before.txt, 623 over-cap lines in 78 files under the final rule]
<!-- /ANCHOR:pre-impl -->

---

<!-- ANCHOR:code-quality -->
## Code Quality

- [x] CHK-010 [P0] The caps read the same in `SKILL.md`, the kernel and the root, and the shared card is unchanged [EVIDENCE: the same four caps in SKILL.md line 276, kernel line 90 and root line 209; z — Knowledge card unchanged, parity 38/38]
- [x] CHK-011 [P0] No line a scenario cites moved: every source edit stays on its existing line [EVIDENCE: git diff -U0 hunks @@ -276 +276, @@ -90 +90, @@ -209 +209]
- [x] CHK-012 [P1] The length-cap check warns only, never blocks, and is off for sources [EVIDENCE: product-owner lengthCaps artifacts advisory, sources off; fixture violation exits 0; source gate 40 files passed]
- [x] CHK-013 [P1] Collector change keeps the selftest green [EVIDENCE: selftest 7 of 7 after the change]
<!-- /ANCHOR:code-quality -->

---

<!-- ANCHOR:testing -->
## Testing Checklist

- [x] CHK-020 [P0] Every rewritten export keeps its headings, backticked spans and numbers [EVIDENCE: verify_rewrite.py 98 of 98, structural lines, backticked spans, numbers, links and comments unchanged]
- [x] CHK-021 [P0] Format gate exit 0 on the sources and every export; fixtures pass [EVIDENCE: source gate exit 0, 98 exports 0 gate failures, four fixture suites PASSED]
- [x] CHK-022 [P0] Playbook validator reports 0 violations [EVIDENCE: PASS scenarios=46 violations=0]
- [x] CHK-023 [P1] Over-cap counts after the rewrite reported beside the counts before [EVIDENCE: 623 in 78 files before, 7 in 7 files after, in README Edited after grading]
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:fix-completeness -->
## Fix Completeness

- [x] CHK-FIX-001 [P0] The cap gap is classed `class-of-bug`: no rule defined short, so every artifact kind is in scope [EVIDENCE: no rule defined short, so the caps sit on the entry-point line every artifact loads, both sides]
- [x] CHK-FIX-002 [P0] Both packagings carry the caps: skill and Project [EVIDENCE: SKILL.md line 276 and kernel line 90 carry the same sentence]
- [x] CHK-FIX-003 [P1] Every consumer of the export files checked: README, realism entries, collector [EVIDENCE: README collection table and extraction review relabelled, grading-notes pointers added, collector guard keeps edited exports]
- [x] CHK-FIX-004 [P1] Evidence pinned to the commit that lands this phase [EVIDENCE: Product Owner fdc8a28, Barter 48ca7a3f]
<!-- /ANCHOR:fix-completeness -->

---

<!-- ANCHOR:security -->
## Security

- [x] CHK-030 [P0] No credentials committed, and the exports carry fixture data only [EVIDENCE: exports carry Roamstay, Loomlist and Fernhouse fixture data only; no credential in the diff]
- [x] CHK-031 [P1] Public repo commit carries no attribution line [EVIDENCE: fdc8a28 message has no attribution line]
<!-- /ANCHOR:security -->

---

<!-- ANCHOR:docs -->
## Documentation

- [x] CHK-040 [P0] The report says the exports were edited by hand after grading and names the graded originals [EVIDENCE: README Edited after grading names e9edb95, 7652158c and replies/]
- [x] CHK-041 [P0] No `SYNC.md` note marks the kernel review done [EVIDENCE: SYNC.md note says the review of kernel v0.18.0 is still pending]
- [x] CHK-042 [P1] Spec, plan and tasks synchronized [EVIDENCE: spec, plan, tasks and criteria updated for the caps home, the gate fixes and the fact review]
- [x] CHK-043 [P2] Parent spec phase map updated [EVIDENCE: parent spec.md phase map row 6 Complete]
<!-- /ANCHOR:docs -->

---

<!-- ANCHOR:file-org -->
## File Organization

- [x] CHK-050 [P1] Snapshots and verify script kept in scratch/ only [EVIDENCE: before/, groups/, briefs, verify script, fact reviews and caps counts in scratch/]
- [x] CHK-051 [P1] scratch/ cleaned before completion [EVIDENCE: nothing temporary left; the snapshot, briefs, verify script and reviews stay as the evidence the criteria cite]
<!-- /ANCHOR:file-org -->

---

<!-- ANCHOR:summary -->
## Verification Summary

| Category | Total | Verified |
|----------|-------|----------|
| P0 Items | 12 | 12/12 |
| P1 Items | 10 | 10/10 |
| P2 Items | 1 | 1/1 |

**Verification Date**: 2026-09-26
<!-- /ANCHOR:summary -->

---



