---
title: "Implementation Plan: Phase 49: FigJam reading order and reply lead"
description: "Return the glance order to the plain majority read, put the board URL first in every delivery, align FJ-023 and the examples with the turn 1 rule, measure diamond labels by glyph width, score Composition mechanically, check them with the gates and a fresh review, release v1.0.15.0 and rerun FJ-022 and FJ-023."
trigger_phrases:
  - "figjam reading order and reply lead plan"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: plan-core | v2.3 -->
# Implementation Plan: Phase 49: FigJam reading order and reply lead

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
The check's reading order returns to the accent first and then column by column, and the diamond label check wraps by Inter Medium glyph widths, each with self-tests and the process example's shown output regenerated. The prose rules put the board URL first in every delivery, make FJ-023 and the examples model the turn 1 intake round, draw a handoff queue as a label and keep the dials out of the row count. The harness gains an `Order:` line in the reader brief and a script that scores Composition. One Claude Sonnet 5.5 high agent implements, a fresh one reviews the whole diff, the Project mirror lands in the same commit as kernel v1.2.15 and FJ-022 and FJ-023 rerun one after the other on v1.0.15.0.
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
- **`scripts/figjam_checks/board_geometry.py`, `scripts/flow_check.py`**: the plain reading order and the glyph-width diamond wrap
- **`references/flow-mode.md`, `references/quality-rubric.md`, `references/types/process.md`, `SKILL.md`**: the reply lead, the majority read, the queue rule and the dials rule
- **`assets/flow-templates.md` and `assets/examples/`**: the wrong and right first line, the named readers and the intake rounds
- **`manual-testing-playbook/`**: the Section 5 dials sentence and FJ-023's turns
- **`benchmark/reports/.../run/`**: the delivery check and the Composition script

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
| Review | The whole diff against the causes | A fresh Claude Sonnet 5.5 high reviewer |
| Live | FJ-022 and FJ-023 on v1.0.15.0 | The run harness, renders, two readers per board and one Opus grader |
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:dependencies -->
## 6. DEPENDENCIES

| Dependency | Type | Status | Impact if Blocked |
|------------|------|--------|-------------------|
| The graded v1.0.14.0 rerun and its causes | Internal | Complete | The fixes would have no source |
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
- [x] Backup created: the last pushed commit holds v1.0.14.0
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
