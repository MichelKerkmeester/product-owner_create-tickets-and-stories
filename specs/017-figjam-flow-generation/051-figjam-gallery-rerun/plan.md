---
title: "Implementation Plan: Phase 51: FigJam gallery rerun on v1.0.16.0"
description: "Write FJ-049, prepare the FJ-032 board, run the ten scenarios one at a time with Claude Sonnet 5.5 medium, grade each board with two readers and one Sonnet high grader, then swap only the images the grades support."
trigger_phrases:
  - "figjam gallery rerun plan"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: plan-core | v2.3 -->
# Implementation Plan: Phase 51: FigJam gallery rerun on v1.0.16.0

<!-- SPECKIT_LEVEL: 2 -->

---

<!-- ANCHOR:summary -->
## 1. SUMMARY

The run driver in the model comparison run folder already runs one scenario on one model through Claude Code, records every turn and redacts each scenario's output as it finishes. This phase runs it with the label `sonnet-medium-051` and the model `claude:claude-sonnet-5-5:medium` on ten scenarios, each in a new draft file, and grades the boards the same way sections 8.13 to 8.15 did.
<!-- /ANCHOR:summary -->

---

<!-- ANCHOR:quality-gates -->
## 2. QUALITY GATES

| Gate | Command | Expected |
|------|---------|----------|
| Repository gates | `bash benchmark/gates/run_gates.sh` | 15 of 15 |
| Redaction | `run/redact_run.py` per scenario, then a scan for figma.com, file keys, plan names and emails | Nothing found |
| Spec | `validate.sh --strict` | RESULT: PASSED |
<!-- /ANCHOR:quality-gates -->

---

<!-- ANCHOR:architecture -->
## 3. ARCHITECTURE

`run/run_full.sh` loops over scenario ids and calls `run/adaptive_compare.py` for each. A file key is passed per run, so each scenario gets its own new draft file. FJ-032 runs with `OPERATOR_DONE=FJ-032` on a board prepared with existing content. Readers read the colour renders, `run/composition_check.py` scores Composition and the grader scores the 22-point scorecard.
<!-- /ANCHOR:architecture -->

---

<!-- ANCHOR:phases -->
## 4. IMPLEMENTATION PHASES

1. Write FJ-049 and list it in the playbook root.
2. Create the draft files and prepare the FJ-032 board.
3. Run the ten scenarios one at a time.
4. Render each board, then read and grade it.
5. Judge each image, update the gallery, record report section 8.16.
6. Gates, commit, push.
<!-- /ANCHOR:phases -->

---

<!-- ANCHOR:testing -->
## 5. TESTING STRATEGY

The runs are the test. Each board is read by two fresh readers who did not see the model, and graded on the shipped scorecard.
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:dependencies -->
## 6. DEPENDENCIES

| Dependency | Type | Status | Impact if Blocked |
|------------|------|--------|-------------------|
| The hosted Figma MCP and the operator's team plan | External | Available | The runs wait |
| Claude Code with Sonnet 5.5 | External | Available | The runs wait |
<!-- /ANCHOR:dependencies -->

---

<!-- ANCHOR:rollback -->
## 7. ROLLBACK PLAN

Each image swap is one file in git, so `git revert` of the gallery commit restores the old images. Draft files in Figma are left for the operator to delete.
<!-- /ANCHOR:rollback -->

---

<!-- ANCHOR:phase-deps -->
## L2: PHASE DEPENDENCIES

| Phase | Depends On | Blocks |
|-------|------------|--------|
| Runs | FJ-049, draft files | Grading |
| Grading | Runs, renders | Gallery |
| Gallery | Grading | Push |
<!-- /ANCHOR:phase-deps -->

---

<!-- ANCHOR:effort -->
## L2: EFFORT ESTIMATION

| Phase | Complexity | Estimated Effort |
|-------|------------|------------------|
| Runs | Low | About 50 minutes of turn time |
| Grading | Medium | Twenty reader notes and ten scorecards |
| Gallery and report | Low | One pass |
<!-- /ANCHOR:effort -->

---

<!-- ANCHOR:enhanced-rollback -->
## L2: ENHANCED ROLLBACK

### Pre-deployment Checklist
- [ ] Redaction scan clean before each commit

### Rollback Procedure
1. Revert the gallery commit in both repositories.

### Data Reversal
- **Has data migrations?** No
- **Reversal procedure**: None needed
<!-- /ANCHOR:enhanced-rollback -->
