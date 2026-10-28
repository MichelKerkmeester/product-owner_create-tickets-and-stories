---
title: "Implementation Plan: Phase 48: FigJam neighbour and closing fixes"
description: "Read a decision beside the accent where readers meet it, end each intake round on one closing question, align FJ-017 with the skill, trace diamonds at FigJam's size, check them with the gates and a fresh Opus review, release v1.0.14.0 and rerun the four scenarios."
trigger_phrases:
  - "figjam neighbour and closing fixes plan"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: plan-core | v2.3 -->
# Implementation Plan: Phase 48: FigJam neighbour and closing fixes

<!-- SPECKIT_LEVEL: 2 -->

---

<!-- ANCHOR:summary -->
## 1. SUMMARY

### Technical Context

| Aspect | Value |
|--------|-------|
| **Language/Stack** | Python for the check and the harness, Bash for the run driver, Markdown for the skill, the playbook and the mirror |
| **Framework** | Figma's `use_figma` plugin API |
| **Storage** | None |
| **Testing** | The composer and check self-tests, pytest, the 15 repository gates, the output format gate and the Sync Loop parity and residency checks |

### Overview
The check's reading order lifts a decision joined to the accent on its own row, and the trace measures whole-pixel lines and a wider diamond text box, each with self-tests and the two flow examples' shown output regenerated. The prose rules end each intake round on one closing question, keep the dials at the playback, align FJ-017's Finding with the skill, rewrite the Composition levels and score a turn 1 that models before its intake. A fresh Opus reviewer then reads the whole diff, the Project mirror lands in the same commit and the four scenarios rerun on v1.0.14.0, graded as phase 047 graded its rerun.
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
- **`scripts/figjam_checks/board_geometry.py`, `scripts/flow_check.py`**: the accent neighbour in `reading_order` and the diamond text box
- **`scripts/compose-trace.mjs`**: whole-pixel line heights in the trace
- **`references/flow-mode.md`, `references/quality-rubric.md`, `references/hybrid-workflow.md`**: the closing question, the playback dials, the glance exception and the Finding rule
- **`assets/flow-templates.md` and `assets/examples/`**: the closing question and the regenerated models
- **`manual-testing-playbook/`**: the Composition levels, the Section 5 rules and FJ-017

### Data Flow
A cause names a rule and its file. The owning lane edits the source, the mirror lane carries it to its Project file and the gates prove both agree.
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
| Unit | Composer and checks | `compose_board.py --self-test`, `flow_check.py --self-test`, pytest |
| Integration | Skill sources and the Project mirror | `benchmark/gates/run_gates.sh`, the output format gate, `validate_parity.py` and `residency_check.py` |
| Review | The whole diff against the causes | A fresh Opus reviewer |
| Live | FJ-017, FJ-022, FJ-023 and FJ-036 on v1.0.14.0 | The run harness, renders, two readers per board and one Opus grader |
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:dependencies -->
## 6. DEPENDENCIES

| Dependency | Type | Status | Impact if Blocked |
|------------|------|--------|-------------------|
| The graded v1.0.13.0 rerun and its causes | Internal | Complete | The fixes would have no source |
| The hosted Figma MCP and a draft file in the operator's team | External | Available | The rerun waits |
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
| Verification | Med | 3 hours |
| **Total** | | **5.5 hours** |
<!-- /ANCHOR:effort -->

---

<!-- ANCHOR:enhanced-rollback -->
## L2: ENHANCED ROLLBACK

### Pre-deployment Checklist
- [x] Backup created: the last pushed commit holds v1.0.13.0
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
