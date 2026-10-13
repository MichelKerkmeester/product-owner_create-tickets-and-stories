---
title: "Tasks: Requirements bloat in Story Mode"
description: "Task Format: T### [P?] Description (file path)"
trigger_phrases:
  - "requirements bloat tasks"
  - "story requirements classification"
  - "narration check fixture pair"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.2 -->
# Tasks: Requirements bloat in Story Mode

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

- [x] T001 Read the five rule sources and the four commits the brief names (`findings.md` corpus note)
- [x] T002 Assemble the corpus and count 221 Requirements bullets across the fifteen stories that carry the section (`findings.md` section 2)
- [x] T003 Run the format gate and its fixtures at baseline (`run.log`)
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T004 Quote the carry-through and hard-constraint rules and attribute each bloated bullet to the rule it obeyed (`findings.md` section 1)
- [x] T005 Classify every bullet and tabulate description and rider rates per story and per source shape (`findings.md` section 2)
- [x] T006 Write the build-can-fail test and run the nine cases, including the borderline presentation shape (`findings.md` section 3)
- [x] T007 Write edits A to P with the current text and the replacement, file by file (`findings.md` section 4)
- [x] T008 [P] Scan the five worked examples and the mirrors for a modelling line (`findings.md` section 5)
- [x] T009 [P] Build the narration check and its fixture pair and run both against the corpus (`findings.md` section 6)
- [x] T010 Answer what a story does with the screen description it drops (`findings.md` section 7)
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T011 The narration check measured 3 true positives and 0 false positives on the corpus, and fired zero times on 93 example, export and mirror bullets (`findings.md` section 6.2)
- [x] T012 The violation fixture produced exactly two findings and the exempt fixture produced none (`findings.md` section 6.3)
- [x] T013 No file outside this folder changed, no sync compiler ran and nothing was committed (`run.log`)
<!-- /ANCHOR:phase-3 -->

---

<!-- ANCHOR:completion -->
## Completion Criteria

- [x] All tasks marked `[x]`
- [x] No `[B]` blocked tasks remaining
- [ ] Proposed edits applied (a follow-up pass, since the brief scoped proposals only)
<!-- /ANCHOR:completion -->

---

<!-- ANCHOR:cross-refs -->
## Cross-References

- **Specification**: See `spec.md`
- **Plan**: See `plan.md`
- **Findings**: See `findings.md`
<!-- /ANCHOR:cross-refs -->

---
