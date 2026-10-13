---
title: "Tasks: Held-out review of Creator - Deals - Saved Deals Shelf"
description: "Task Format: T### [P?] Description (file path)"
trigger_phrases:
  - "holdout review tasks"
  - "trap-by-trap verdict"
  - "ranked changes p0 to p3"
  - "report printed to findings"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.2 -->
# Tasks: Held-out review of Creator - Deals - Saved Deals Shelf

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

- [x] T001 Write the brief with the reading list, the eight trap families and the six advisory questions (`brief.md`)
- [x] T002 Write the runner that dispatches the reviewer and captures its output (`run.sh`)
- [x] T003 Baseline the format gate and its fixture suite, fixtures pass 18/18 (`benchmark/format/run_fixtures.sh`)
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T004 Read the source, the artifact, the rules and the two commits that set the Requirements rule (`export/Story Drafts/Creator - Deals - Saved Deals Shelf/`, `sk-product-owner/references/story-mode.md`, `ba2bec3`, `095479a`)
- [x] T005 Give a verdict per trap family, seven held and one failed (`findings.md` section 1)
- [x] T006 Measure the proposed phrase list over 328 Requirements bullets (`findings.md` section 2.2)
- [x] T007 Answer the six advisory questions on the paraphrase, the scope line, the remaining sections, the output path, the stale rules and the fixture (`findings.md` sections 2 to 7)
- [x] T008 Rank every recommended change P0 to P3 with file, line, current text and replacement (`findings.md` section 8)
- [x] T009 Write the report to `findings.md` and print it into `run.log` (`findings.md`, `run.log`)
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T010 Run the format gate over the artifact and all seventeen stories, one fails and sixteen pass (`benchmark/format/validate-output-format.cjs`)
- [x] T011 Confirm the reviewer run exits clean, `exit=0 seconds=842` (`run.log`)
- [x] T012 Confirm nothing outside this folder changed and nothing was committed, `git status` against `AI Systems/Product Owner/` (`run.log`)
<!-- /ANCHOR:phase-3 -->

---

<!-- ANCHOR:completion -->
## Completion Criteria

- [x] All tasks marked `[x]`
- [x] No `[B]` blocked tasks remaining
- [ ] The ranked repairs are applied (outside this run, which the brief bound to read-only)
<!-- /ANCHOR:completion -->

---

<!-- ANCHOR:cross-refs -->
## Cross-References

- **Specification**: See `spec.md`
- **Plan**: See `plan.md`
<!-- /ANCHOR:cross-refs -->

---
