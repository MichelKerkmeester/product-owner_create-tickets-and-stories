---
title: "Implementation Plan: Phase 38: figjam-model-comparison"
description: "Builds one adaptive driver over the Devin runner, runs the seven board-quality scenarios on three models one at a time, renders and grades every board and keeps the best board of each type as the gallery."
trigger_phrases:
  - "figjam model comparison plan"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: plan-core | v2.2 -->
# Implementation Plan: Phase 38: figjam-model-comparison

<!-- SPECKIT_LEVEL: 2 -->

---

<!-- ANCHOR:summary -->
## 1. SUMMARY

### Technical Context

| Aspect | Value |
|--------|-------|
| **Language/Stack** | Python for the driver, the Devin CLI for the runs |
| **Framework** | Figma's hosted MCP server and the skill's composer |
| **Storage** | A run folder under `benchmark/reports/` |
| **Testing** | The 22-point board scorecard, a fresh reader and validate.sh --strict |

### Overview
The driver loads each scenario from the playbook, builds its sandbox with the Devin runner and sends the scripted turns. After an intake round it sends the recommended-answers turn, and after a stop that still has no board it sends "Yes, go ahead.", each labelled in `meta.json`. Boards are rendered through Code Mode's Figma manual, read by a fresh reader and graded per type, and the best board of each type replaces the gallery image.
<!-- /ANCHOR:summary -->

---

<!-- ANCHOR:quality-gates -->
## 2. QUALITY GATES

### Definition of Ready
- [x] Problem statement clear and scope documented
- [x] Success criteria measurable
- [x] Dependencies identified

### Definition of Done
- [ ] All acceptance criteria met
- [ ] validate.sh --strict passes
- [ ] Docs updated (spec, plan, tasks)
<!-- /ANCHOR:quality-gates -->

---

<!-- ANCHOR:architecture -->
## 3. ARCHITECTURE

### Pattern
One operator over one harness, with grading kept apart from the models under test

### Key Components
- **`run/adaptive_compare.py`**: one scenario on one model, through the Devin runner
- **`run/run_compare.sh`**: the 21 runs one at a time
- **The runner**: a copy of the 2026-10-24 Devin runner, unchanged but for the model
- **Grades**: one reader per model, one grader per type

### Data Flow
Each run writes its turns to `skill/<model>/<ID> - <slug>/`. The written board's node id is read from its compose call and rendered. The reader answers from the colour renders alone, the grader scores the renders, the transcript and the reader's answers, and `results.jsonl` holds one row per run.
<!-- /ANCHOR:architecture -->

---

<!-- ANCHOR:phases -->
## 4. IMPLEMENTATION PHASES

Follow the ordered tasks in `tasks.md`. It owns the Setup, Implementation and Verification phase checkboxes and task state.
<!-- /ANCHOR:phases -->

---

<!-- ANCHOR:testing -->
## 5. TESTING STRATEGY

| Test Type | Scope | Tools |
|-----------|-------|-------|
| Manual | Each board | The 22-point scorecard at two zooms, a greyscale copy and a fresh reader |
| Integration | The driver | A probe turn on each harness before the batch |
| Static | Redaction | A scan of the run folder for the file key, board URLs, plan names and emails |
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:dependencies -->
## 6. DEPENDENCIES

| Dependency | Type | Status | Impact if Blocked |
|------------|------|--------|-------------------|
| Phase 037 composer | Internal | Complete | None |
| Figma sign-in on Devin | External | Probed, whoami answers on all three models | The runs cannot write |
| Code Mode's Figma manual | External | Used in phase 035 | No renders to grade |
<!-- /ANCHOR:dependencies -->

---

<!-- ANCHOR:rollback -->
## 7. ROLLBACK PLAN

- **Trigger**: The operator rejects the new gallery
- **Procedure**: Restore the seven images and the captions from the last commit with `git checkout -- <path>` on the operator's approval
<!-- /ANCHOR:rollback -->

---

<!-- ANCHOR:phase-deps -->
## L2: PHASE DEPENDENCIES

| Phase | Depends On | Blocks |
|-------|------------|--------|
| Setup | None | Core |
| Core | Setup | Verify |
| Verify | Core | None |
<!-- /ANCHOR:phase-deps -->

---

<!-- ANCHOR:effort -->
## L2: EFFORT ESTIMATION

| Phase | Complexity | Estimated Effort |
|-------|------------|------------------|
| Setup | Low | 1 hour |
| Core Implementation | Med | 4 hours of runs |
| Verification | Med | 2 hours |
| **Total** | | **7 hours** |
<!-- /ANCHOR:effort -->

---

<!-- ANCHOR:enhanced-rollback -->
## L2: ENHANCED ROLLBACK

### Pre-deployment Checklist
- [ ] Backup created: the last commit holds the current gallery
- [ ] Feature flag: not applicable
- [ ] Monitoring: one status line per finished run

### Rollback Procedure
1. Stop the batch
2. Restore the gallery files on the operator's approval
3. Tell the operator

### Data Reversal
- **Has data migrations?** No
- **Reversal procedure**: N/A
<!-- /ANCHOR:enhanced-rollback -->
