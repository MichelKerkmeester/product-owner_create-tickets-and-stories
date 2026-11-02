---
title: "Tasks: Product Owner Story and Epic template changes requested by the PM"
description: "Task Format: T### [P?] Description (file path)"
trigger_phrases:
  - "product owner story feedback tasks"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.2 -->
# Tasks: Product Owner Story and Epic template changes requested by the PM

<!-- SPECKIT_LEVEL: 1 -->

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

- [x] T001 Trace the four requests to templates, Story Mode, examples, kernel and playbook (grep over both packagings)
- [x] T002 Baseline the gates on the clean tree (router, format fixtures, rule parity, project parity)
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T003 Remove the Story intro lines and the Delivery helper sentences (templates, examples, mirrors, fixtures)
- [x] T004 Merge About and Problem into `## Problem` and move Solution to H2 (Story template, Story Mode, kernel, examples, both sides)
- [x] T005 One outcome per Then or And line (templates, Story Mode, kernel, examples, both sides)
- [x] T006 Problem caps and joined-outcome advice in both validators, with fixtures and runner cases
- [x] T007 Playbook pass lines and line citations, Sync Loop omitted-line declaration
- [x] T008 Skill v1.1.0.0, kernel v1.1.0, changelog, READMEs and a dated `SYNC.md` note
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T009 Format fixtures pass in Product Owner and the three shared-runner systems, reference parity identical
- [x] T010 Router and rule parity pass, format gate output equals the HEAD baseline
- [x] T011 Project parity 37/37 and pair divergence 37 pairs pass after commit (`a3367a5`, `1b615ce8`)
- [x] T012 Playbook signals for the new rules; full 46-scenario run on Haiku 5.5 high, every new Story and Epic follows the four rules (`benchmark/reports/2026-10-08--manual-testing-playbook--claude-haiku-5-5-high/`)
- [x] T014 Story and Epic criteria number as `1 ) **{Title}**`; four-scenario Haiku check writes 22 of 22 criteria in the new form
- [x] T013 Deliverables collected into `export/benchmark` with the collector's second-round clarification skip fixed
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



