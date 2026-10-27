---
title: "Implementation Plan: Phase 45: FigJam findings fixes"
description: "Turn the v1.0.10.0 rerun findings into scripted sentence swaps in the skill and the mirror, check them with the gates and a fresh Opus review, and release v1.0.11.0 with no rerun."
trigger_phrases:
  - "figjam findings fixes plan"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: plan-core | v2.3 -->
# Implementation Plan: Phase 45: FigJam findings fixes

<!-- SPECKIT_LEVEL: 2 -->

---

<!-- ANCHOR:summary -->
## 1. SUMMARY

### Technical Context

| Aspect | Value |
|--------|-------|
| **Language/Stack** | Markdown for the skill, the playbook and the mirror |
| **Framework** | Figma's `use_figma` plugin API |
| **Storage** | None |
| **Testing** | The composer and check self-tests, pytest, the 15 repository gates, the output format gate and the Sync Loop parity and residency checks |

### Overview
Every fix is a sentence swap whose wording this phase sets, applied by one script that refuses to run when a target sentence is missing or appears twice, and byte-checked in the skill and its Project file alike. The playbook scenarios take one uniform swap each. A fresh Opus reviewer then reads the whole diff against the findings, and the confirmed findings are repaired the same way. The Project mirror lands in the same commit.
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
- **`references/flow-mode.md`**: the intake, the revision, the read-back and the reply
- **`references/quality-rubric.md`, `references/types/state.md` and `assets/examples/`**: the glance rules and the plans models copy
- **`references/hybrid-workflow.md`**: the single sticky and its gate
- **`manual-testing-playbook/`**: the scorecard rows, the turn rule and the board scenarios

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
| Unit | Composer and checks, unchanged | `compose_board.py --self-test`, `flow_check.py --self-test`, pytest |
| Integration | Skill sources and the Project mirror | `benchmark/gates/run_gates.sh`, the output format gate, `validate_parity.py` and `residency_check.py` |
| Review | The whole diff against the findings | A fresh Opus reviewer |
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:dependencies -->
## 6. DEPENDENCIES

| Dependency | Type | Status | Impact if Blocked |
|------------|------|--------|-------------------|
| The graded v1.0.10.0 rerun and its findings | Internal | Complete | The fixes would have no source |
<!-- /ANCHOR:dependencies -->

---

<!-- ANCHOR:rollback -->
## 7. ROLLBACK PLAN

- **Trigger**: A gate fails on the committed tree or a later rerun shows a rule reads worse
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
| Core Implementation | Med | 2 hours |
| Verification | Low | 1 hour |
| **Total** | | **3.5 hours** |
<!-- /ANCHOR:effort -->

---

<!-- ANCHOR:enhanced-rollback -->
## L2: ENHANCED ROLLBACK

### Pre-deployment Checklist
- [x] Backup created: the last pushed commit holds v1.0.10.0
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
