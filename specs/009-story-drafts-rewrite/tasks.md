---
title: "Tasks: Story Drafts two-pass rewrite"
description: "Task Format: T### [P?] Description (file path)"
trigger_phrases:
  - "story drafts rewrite tasks"
  - "first pass lane timings"
  - "criteria cleanup rerun"
  - "story benchmark model rows"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.2 -->
# Tasks: Story Drafts two-pass rewrite

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

- [x] T001 Write `run.sh` to read `files.txt` and split its draft paths three ways round-robin across lanes 1, 2 and 3 (run.sh)
- [x] T002 Write the router prompt that rewrites each draft in place as a full Story, with no numbered export and no screenshot references (run.sh)
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T003 Fire one router call per draft with DeepSeek V4 Flash at max thinking, three lanes at once (results.tsv)
- [x] T004 Record lane, seconds, exit and path for all sixteen first-pass runs (results.tsv)
- [x] T005 Write `rerun3.sh` for the three stories whose criteria described UI mechanics (rerun3.sh)
- [x] T006 Rewrite those three from the same source with one extra sentence of steer, same model and router (rerun3.tsv)
- [x] T007 Record seconds, exit and path for the three second-pass runs (rerun3.tsv)
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T008 Read the first pass against the format gate and the criteria counts (README.md)
- [x] T009 Read the second pass, run again from the original drafts and context files only, against the gate (README.md)
- [x] T010 Run the separate one-request benchmark across three models and record validity per row (story-benchmark-results.tsv)
<!-- /ANCHOR:phase-3 -->

---

<!-- ANCHOR:completion -->
## Completion Criteria

- [x] All tasks marked `[x]`
- [x] No `[B]` blocked tasks remaining
- [x] Second pass passes the gate 16 of 16 with no hand fixes
- [ ] The per-surface acceptance-criteria ceiling is not built, so Content Gallery - Highlights - Edit Reel UX stays open at 13 criteria on a four-surface draft
<!-- /ANCHOR:completion -->

---

<!-- ANCHOR:cross-refs -->
## Cross-References

- **Specification**: See `spec.md`
- **Plan**: See `plan.md`
- **Implementation summary**: See `implementation-summary.md`
- **Reading guide**: See `README.md` for the tsv column meanings and the two-pass result
<!-- /ANCHOR:cross-refs -->

---
