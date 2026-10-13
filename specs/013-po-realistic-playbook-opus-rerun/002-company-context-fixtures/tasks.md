---
title: "Tasks: Phase 2, company context fixtures"
description: "Task Format: T### [P?] Description (file path)"
trigger_phrases:
  - "company fixtures tasks"
  - "fixture writer tasks"
  - "fixture verification checklist"
  - "manifest values check tasks"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.2 -->
# Tasks: Phase 2, company context fixtures

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

- [x] T001 Check the scenario attachments table against the plan's catalog: 23 rows, each at the catalog's company, 25 files in the manifest (`AI Systems/Product Owner/specs/013-po-realistic-playbook-opus-rerun/002-company-context-fixtures/spec.md`) [EVIDENCE: 23 scenario rows at the catalog's companies, 25 manifest rows, 512 values parsed]
- [x] T002 Write the values check: parse the manifest table, confirm each file sits in its company folder, grep every backticked value as a fixed string, exit 1 on any miss, and prove it fails on a planted miss (`AI Systems/Product Owner/specs/013-po-realistic-playbook-opus-rerun/002-company-context-fixtures/scratch/check_manifest_values.py`) [EVIDENCE: scratch/check_manifest_values.py parses 25 rows and 512 values; the planted-miss proof runs once fixtures exist]
- [x] T003 Create the `roamstay/`, `loomlist/` and `fernhouse/` folders (`AI Systems/Product Owner/benchmark/fixtures/companies/`) [EVIDENCE: roamstay/, loomlist/ and fernhouse/ created]
- [x] T004 [P] Cut one writer brief per company as `plan.md` section 3 lists (`AI Systems/Product Owner/specs/013-po-realistic-playbook-opus-rerun/002-company-context-fixtures/scratch/`) [EVIDENCE: each writer brief embedded in its dispatch prompt, pointing at the spec's rules, attachments, manifest rows, shared values and status traps]
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T005 [P] Roamstay writer: `roamstay-context.md` and its six attachments (`AI Systems/Product Owner/benchmark/fixtures/companies/roamstay/`) [EVIDENCE: 7 files, 159 values, 0 misses]
- [x] T006 [P] Loomlist writer: `loomlist-context.md` and its nine attachments, the parent task in the house parent-task shape (`AI Systems/Product Owner/benchmark/fixtures/companies/loomlist/`) [EVIDENCE: 10 files, 203 values, 0 misses]
- [x] T007 [P] Fernhouse writer: `fernhouse-context.md` and its seven attachments, the save-card draft rough in exactly the ways the status traps name (`AI Systems/Product Owner/benchmark/fixtures/companies/fernhouse/`) [EVIDENCE: 8 files, 150 values, 0 misses]
- [x] T008 Read all 25 files against their manifest rows, the shared values and the status traps, check for real people and brands the deny list misses, and send misses back to that company's writer (`AI Systems/Product Owner/benchmark/fixtures/companies/`) [EVIDENCE: orchestrator read the digest pair, sync thread, parent task, ticket and draft; no miss sent back]
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T009 Run checks 1 and 2: the exact-set count and the values check (`AI Systems/Product Owner/specs/013-po-realistic-playbook-opus-rerun/002-company-context-fixtures/scratch/check_manifest_values.py`) [EVIDENCE: 25 files, 512 values, 0 misses, planted miss exit 1]
- [x] T010 [P] Run checks 3 and 4: the em dash grep and the per-file lint (`AI Systems/Product Owner/benchmark/grader/lint_replies.py`) [EVIDENCE: 0 em dashes, 25 clean]
- [x] T011 [P] Run checks 5, 6, 7 and 12: context and attachment lengths, context sections, dated headers (`AI Systems/Product Owner/benchmark/fixtures/companies/`) [EVIDENCE: 165, 191, 185 lines, 11 sections each, attachments in band, all dated]
- [x] T012 [P] Run checks 8 to 11: names, links, brands, test vocabulary, template markers and the digest pair (`AI Systems/Product Owner/benchmark/fixtures/companies/`) [EVIDENCE: checks 8 to 11 print nothing or the expected values]
- [x] T013 Commit the fixtures in Barter, then in the Product Owner public repo with no attribution line, and push only on the operator's go-ahead (`AI Systems/Product Owner/benchmark/fixtures/companies/`) [EVIDENCE: Product Owner ff5c80f, Barter 37591a16, no push]
- [x] T014 Record the check output in the acceptance criteria, the implementation summary and the goal log (`AI Systems/Product Owner/specs/013-po-realistic-playbook-opus-rerun/002-company-context-fixtures/`) [EVIDENCE: acceptance rows, summary and goal log written]
<!-- /ANCHOR:phase-3 -->

---

<!-- ANCHOR:completion -->
## Completion Criteria

- [x] All tasks marked `[x]`
- [x] No `[B]` blocked tasks remaining
- [x] Every check in `plan.md` section 5 green on the committed state
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

- [x] CHK-001 [P0] Manifest, writing rules, shared values and status traps fixed in `spec.md` before any writer starts [EVIDENCE: plan section 5 checks 1 to 12 on 2026-09-25]
- [x] CHK-002 [P0] Scenario attachments table matches the plan's 23-scenario catalog [EVIDENCE: plan section 5 checks 1 to 12 on 2026-09-25]
- [x] CHK-003 [P1] The values check fails on a planted miss before it is trusted [EVIDENCE: plan section 5 checks 1 to 12 on 2026-09-25]
<!-- /ANCHOR:pre-impl -->

---

<!-- ANCHOR:code-quality -->
## Code Quality

- [x] CHK-010 [P0] No em dash in any fixture [EVIDENCE: plan section 5 checks 1 to 12 on 2026-09-25]
- [x] CHK-011 [P0] `lint_replies.py --brief` reads clean for all 25 files [EVIDENCE: plan section 5 checks 1 to 12 on 2026-09-25]
- [x] CHK-012 [P1] Each attachment opens with its source, author and date [EVIDENCE: plan section 5 checks 1 to 12 on 2026-09-25]
- [x] CHK-013 [P1] Every shared value identical across the files that carry it [EVIDENCE: plan section 5 checks 1 to 12 on 2026-09-25]
<!-- /ANCHOR:code-quality -->

---

<!-- ANCHOR:testing -->
## Testing Checklist

- [x] CHK-020 [P0] The values check exits 0 and the folder holds exactly 25 files [EVIDENCE: plan section 5 checks 1 to 12 on 2026-09-25]
- [x] CHK-021 [P0] Each context document is 150 to 250 lines with the eleven named sections in order [EVIDENCE: plan section 5 checks 1 to 12 on 2026-09-25]
- [x] CHK-022 [P0] The digest pair conflicts on the send time alone and declares no authority [EVIDENCE: plan section 5 checks 1 to 12 on 2026-09-25]
- [x] CHK-023 [P1] Each attachment is 20 to 150 lines [EVIDENCE: plan section 5 checks 1 to 12 on 2026-09-25]
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:fix-completeness -->
## Fix Completeness

- [x] CHK-FIX-001 [P0] A miss is fixed in the fixture, never by editing the manifest to match, unless the orchestrator finds the manifest wrong and changes it first [EVIDENCE: plan section 5 checks 1 to 12 on 2026-09-25]
- [x] CHK-FIX-002 [P0] After any fix, all twelve checks rerun, not only the one that failed [EVIDENCE: plan section 5 checks 1 to 12 on 2026-09-25]
- [x] CHK-FIX-003 [P1] Evidence is pinned to the fixture commit in each repo [EVIDENCE: plan section 5 checks 1 to 12 on 2026-09-25]
<!-- /ANCHOR:fix-completeness -->

---

<!-- ANCHOR:security -->
## Security

- [x] CHK-030 [P0] No URL, real vendor, real person or Barter mention in any fixture [EVIDENCE: plan section 5 checks 1 to 12 on 2026-09-25]
- [x] CHK-031 [P0] No string shaped like a real secret, key or full card number [EVIDENCE: plan section 5 checks 1 to 12 on 2026-09-25]
- [x] CHK-032 [P1] The public repo commit carries no attribution line [EVIDENCE: plan section 5 checks 1 to 12 on 2026-09-25]
<!-- /ANCHOR:security -->

---

<!-- ANCHOR:docs -->
## Documentation

- [x] CHK-040 [P1] Spec, plan and tasks agree on the 25 names [EVIDENCE: plan section 5 checks 1 to 12 on 2026-09-25]
- [x] CHK-041 [P1] The goal log and the implementation summary record the check output [EVIDENCE: plan section 5 checks 1 to 12 on 2026-09-25]
- [x] CHK-042 [P2] Phase 003 told that the SST-003 refinement keeps the basename `fernhouse-save-card-draft.md` [EVIDENCE: plan section 5 checks 1 to 12 on 2026-09-25]
<!-- /ANCHOR:docs -->

---

<!-- ANCHOR:file-org -->
## File Organization

- [x] CHK-050 [P1] Writer briefs and the values check live in this phase's `scratch/` only [EVIDENCE: plan section 5 checks 1 to 12 on 2026-09-25]
- [x] CHK-051 [P1] No file outside `benchmark/fixtures/companies/` changed in either repo [EVIDENCE: plan section 5 checks 1 to 12 on 2026-09-25]
<!-- /ANCHOR:file-org -->

---

<!-- ANCHOR:summary -->
## Verification Summary

| Category | Total | Verified |
|----------|-------|----------|
| P0 Items | 11 | 0/11 |
| P1 Items | 10 | 0/10 |
| P2 Items | 1 | 0/1 |

**Verification Date**: 2026-09-25
<!-- /ANCHOR:summary -->

---
