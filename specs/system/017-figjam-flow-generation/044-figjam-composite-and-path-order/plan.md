---
title: "Implementation Plan: Phase 44: FigJam composite placement and path order"
description: "Turn the v1.0.9.0 rerun causes into one composer brief, sentence swaps for the glance rules and a pinned node in the launcher, mirror them to the Project in the same commit, then rerun the 6 failures in fresh files with two readers per board and one grader."
trigger_phrases:
  - "figjam composite and path order plan"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: plan-core | v2.3 -->
# Implementation Plan: Phase 44: FigJam composite placement and path order

<!-- SPECKIT_LEVEL: 2 -->

---

<!-- ANCHOR:summary -->
## 1. SUMMARY

### Technical Context

| Aspect | Value |
|--------|-------|
| **Language/Stack** | Markdown for the skill and the mirror, JavaScript for the composer, Python for the checks and the driver |
| **Framework** | Figma's `use_figma` plugin API |
| **Storage** | None |
| **Testing** | The composer and check self-tests, pytest, the 15 repository gates, the output format gate and the Sync Loop parity and residency checks |

### Overview
The composer change comes first, from its own DeepSeek brief: a composite sits after the state that enters it, proved by a self-test case and the recomposed state example, with the composer's room measured. Sentence swaps whose wording this phase sets, the path-order glance rule and the wider revision exemption, are applied by script and byte-checked in the skill and the mirror alike. A fresh Opus reviewer then reads the whole diff against the decisions. The Project mirror, including the composer code block, lands in the same commit. The launcher pins the working node and a fixture proves the label trace before fresh draft files are made and the lanes start.
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
One source per rule, mirrored by hand into the Project and checked by the Sync Loop

### Key Components
- **`references/flow-mode.md`**: the intake, the gate and the read-back the model follows
- **`assets/compose-board.js` and `scripts/compose_board.py`**: the composer and the wrapper that fills and checks it
- **`scripts/flow_check.py`**: the pre-write check, whose label trace needs a working node
- **`references/quality-rubric.md`, `references/types/state.md` and `assets/examples/`**: the glance rules and the plans models copy
- **`run/`**: the driver, its backends and the run's temp folder

### Data Flow
A finding names a rule and its file. The owning lane edits the source, the mirror lane carries it to its Project file and the gates prove both agree.
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
| Unit | Composer layout, outlines, key and checks | `compose_board.py --self-test`, `flow_check.py --self-test`, pytest |
| Integration | Skill sources and the Project mirror | `benchmark/gates/run_gates.sh`, the output format gate, `validate_parity.py` and `residency_check.py` |
| Live | The 6 failures of the v1.0.9.0 rerun | The driver on Claude Sonnet 5.5 high, renders, two readers per board and one grader |
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:dependencies -->
## 6. DEPENDENCIES

| Dependency | Type | Status | Impact if Blocked |
|------------|------|--------|-------------------|
| The graded v1.0.9.0 rerun and its findings | Internal | Complete | The findings would have no source |
| Figma access to draft files on the team plan | External | Available | The rerun could not write boards |
<!-- /ANCHOR:dependencies -->

---

<!-- ANCHOR:rollback -->
## 7. ROLLBACK PLAN

- **Trigger**: A gate fails on the committed tree or a rerun board shows a composer regression
- **Procedure**: Revert this phase's commits in Product Owner and the outer repository, then rerun the gates
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
| Setup | Low | 30 minutes |
| Core Implementation | High | 3 hours |
| Verification and rerun | Med | 3 hours |
| **Total** | | **6.5 hours** |
<!-- /ANCHOR:effort -->

---

<!-- ANCHOR:enhanced-rollback -->
## L2: ENHANCED ROLLBACK

### Pre-deployment Checklist
- [x] Backup created: the last pushed commit holds v1.0.9.0
- [x] Feature flag: not applicable
- [x] Monitoring: not applicable

### Rollback Procedure
1. Revert the phase's commits
2. Run the gates
3. Tell the operator

### Data Reversal
- **Has data migrations?** No
- **Reversal procedure**: N/A
<!-- /ANCHOR:enhanced-rollback -->
