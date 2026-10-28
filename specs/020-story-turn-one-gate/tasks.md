---
title: "Tasks: Story turn-one gate and reply linter fixes"
description: "Task Format: T### [P?] Description (file path). Verify: <command> prints <expected output>"
trigger_phrases:
  - "story turn one gate tasks"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.4 -->
# Tasks: Story turn-one gate and reply linter fixes

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

**Task Format**: `T### [P?] Description (file path). Verify: <command> prints <expected output>`
<!-- /ANCHOR:notation -->

---

<!-- ANCHOR:phase-1 -->
## Phase 1: Setup

- [x] T001 Create the packet (`specs/020-story-turn-one-gate`). Verify: `ls specs/020-story-turn-one-gate` lists spec.md, plan.md and tasks.md. [EVIDENCE: the scaffold wrote all four docs]
- [x] T002 Trace the turn 1 drafting to its source (`events-turn-1.jsonl` of the Pi PST-004 run). Verify: the reasoning quotes the template's "Populate only unresolved fields". [EVIDENCE: spec.md Measured Behavior]
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T003 State the rule in the kernel, `AGENTS.md` and `SKILL.md`. Verify: `rg -c "Validation field"` prints 1 for each. [EVIDENCE: 1 line in each of the three files]
- [x] T004 Keep the Validation field in the Story and Doc question templates and close Story Mode's Interactive behavior line and Step 1, in the skill and its mirror. Verify: `rg -c "Validation\*\* field|settle every field|all four are established"` prints 2 for each of the four files. [EVIDENCE: 2 lines in each]
- [x] T005 Bound the Product Owner linter's phrases and exempt `TBD...` (`benchmark/grader/hvr_lint.py`). Verify: a one-off check passes. [EVIDENCE: "contacts as" no copula hit, three `TBD...` no ellipsis hit, "Wait... then..." still 2 hits]
- [x] T006 [P] Bound the phrase matches in the Copywriter, Deal Templates, Sales HubSpot and Sales Direct Communication linters and the Sales export gate. Verify: a phrase gives 1 hit and the same phrase inside a word gives 0. [EVIDENCE: 1 and 0 in each, "bij dezelfde" 0 in Sales Direct Communication]
- [x] T007 Release hub v1.0.16.0, `sk-product-owner` v1.2.6.0 and kernel v1.2.16 (version files, `changelog/`, `SYNC.md`, `README.md`, `claude project/README.md`). Verify: `rg -n "1\.0\.16\.0"` hits the version files. [EVIDENCE: SKILL.md, description.json, hub-router.json, mode-registry.json and README.md]
- [x] T008 Pull the drifted vendored packets the vendor sync gate reported (`mcp-figma/`, `mcp-click-up/`, `vendor.json`). Verify: `python3 scripts/vendor-sync.py status` prints in step for all five. [EVIDENCE: all five in step]
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T009 Run the gates. Verify: `bash benchmark/gates/run_gates.sh` prints `all 15 gates pass` and the format gate prints `validation passed`. [EVIDENCE: all 15 gates pass, format gate passed across 72 source files, residency and pair divergence PASSED]
- [x] T010 [P] Run the sibling gates. Verify: each suite passes. [EVIDENCE: Copywriter all 4, Deal Templates all 7, Sales HubSpot exit 0, Sales Direct Communication gates and export blocker check passed]
- [x] T011 Rerun PST-003 and PST-004 twice on Pi. Verify: turn 1 asks one question and renders no draft in all four runs. [EVIDENCE: 4 of 4 turn 1 replies carry a Validation line and no `## Problem`, 4 of 4 turn 2 replies draft Problem and Acceptance criteria, 8 of 8 lint clean]
- [x] T012 Run the parity check after the commit. Verify: `validate_parity.py product-owner` prints PASSED. [EVIDENCE: PASSED 65/65 declared pairs after outer commits 0001128 and 0001129]
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
