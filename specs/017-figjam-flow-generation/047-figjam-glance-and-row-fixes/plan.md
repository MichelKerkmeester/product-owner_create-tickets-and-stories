---
title: "Implementation Plan: Phase 47: FigJam glance and row fixes"
description: "Add the glance and row lines and the sticky alignment and reach to the check, turn the v1.0.12.0 rerun causes into rule changes in the skill and the mirror, fix the harness, check them with the gates and a fresh Opus review, release v1.0.13.0 and rerun the four scenarios."
trigger_phrases:
  - "figjam glance and row fixes plan"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: plan-core | v2.3 -->
# Implementation Plan: Phase 47: FigJam glance and row fixes

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
The check composes each user flow and process in memory, as it already does for the label trace, and reads two new lines off that board: a `Glance:` line in the order a reader meets the nodes and a `Row:` advisory for a main-row line that bends. The sides search names each sticky's alignment and stops offering squares past one sticky width. The prose rules change to follow those lines, to require the checked model verbatim at the gate and to give labels a way past a wrap, and the user flow and process examples are relabelled so their Check blocks match the check, which a new self-test holds. The harness keeps redaction to each scenario's own output. A fresh Opus reviewer then reads the whole diff, the Project mirror lands in the same commit as kernel v1.2.13 and the four scenarios rerun on v1.0.13.0, graded as phase 046 graded its rerun.
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
- **`scripts/flow_check.py`, `scripts/figjam_checks/board_geometry.py`**: the glance and row lines, the sides alignment and reach and the two-measure label trace
- **`references/flow-mode.md`**: step 5 label branches, step 7 verbatim sketch and the Section 4 dials round
- **`references/quality-rubric.md`**: the glance plan from the drawn order and the Section 5 gate checklist
- **`references/hybrid-workflow.md`**: the sticky's named side and alignment
- **`assets/flow-templates.md` and `assets/examples/`**: round One dials, the Sketch line and the relabelled models
- **`manual-testing-playbook/`**: the Composition and Legibility rows and the Section 5 stop rules
- **`benchmark/reports/.../run/`**: the per-scenario redaction and the delivery reading

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
| Live | FJ-017, FJ-022, FJ-023 and FJ-036 on v1.0.13.0 | The run harness, renders, two readers per board and one Opus grader |
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:dependencies -->
## 6. DEPENDENCIES

| Dependency | Type | Status | Impact if Blocked |
|------------|------|--------|-------------------|
| The graded v1.0.12.0 rerun and its causes | Internal | Complete | The fixes would have no source |
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
| Core Implementation | Med | 3 hours |
| Verification | Med | 3 hours |
| **Total** | | **6.5 hours** |
<!-- /ANCHOR:effort -->

---

<!-- ANCHOR:enhanced-rollback -->
## L2: ENHANCED ROLLBACK

### Pre-deployment Checklist
- [x] Backup created: the last pushed commit holds v1.0.12.0
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
