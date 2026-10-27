---
title: "Implementation Plan: Phase 42: FigJam glance plans and Left out"
description: "Turn the v1.0.7.0 rerun findings into one-change briefs, apply them with DeepSeek and the Project mirror in the same commit, prove the composer changes by self-test, then rerun the 14 failures in fresh files and grade them with one grader."
trigger_phrases:
  - "figjam glance and left out plan"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: plan-core | v2.3 -->
# Implementation Plan: Phase 42: FigJam glance plans and Left out

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
Each finding becomes one change with its file and the check that proves it. Sentence swaps whose wording this phase sets are applied by script and byte-checked in the skill and the mirror alike. DeepSeek V4.1 Flash max makes each code change from its own brief, and the diff is read before the next one goes out. The composer changes are proven by new self-test cases first. A fresh Opus reviewer then reads the whole diff against the decisions. The Project mirror and kernel land in the same commit, and a fresh draft file is made for each board scenario before the rerun starts.
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
- **`scripts/flow_check.py`**: the pre-write check that now warns about a label left with one word on its last line
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
| Live | The 14 failures of the v1.0.7.0 rerun | The driver on Claude Sonnet 5.5 high, renders and one grader |
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:dependencies -->
## 6. DEPENDENCIES

| Dependency | Type | Status | Impact if Blocked |
|------------|------|--------|-------------------|
| The graded v1.0.7.0 rerun and its findings | Internal | Complete | The findings would have no source |
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
| Core Implementation | High | 2.5 hours |
| Verification and rerun | Med | 3 hours |
| **Total** | | **6.5 hours** |
<!-- /ANCHOR:effort -->

---

<!-- ANCHOR:enhanced-rollback -->
## L2: ENHANCED ROLLBACK

### Pre-deployment Checklist
- [x] Backup created: the last pushed commit holds v1.0.7.0
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
