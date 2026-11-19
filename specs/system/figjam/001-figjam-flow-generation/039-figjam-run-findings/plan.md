---
title: "Implementation Plan: Phase 39: FigJam run findings"
description: "Fix the five skill findings in Flow Mode, the playbook and the composer and mirror what applies inside a Project by hand. Fix the three driver findings in the run folder."
trigger_phrases:
  - "figjam run findings plan"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: plan-core | v2.3 -->
# Implementation Plan: Phase 39: FigJam run findings

<!-- SPECKIT_LEVEL: 2 -->

---

<!-- ANCHOR:summary -->
## 1. SUMMARY

### Technical Context

| Aspect | Value |
|--------|-------|
| **Language/Stack** | Python for the composer wrapper and the driver, JavaScript for the composer |
| **Framework** | Figma's `use_figma` plugin API |
| **Storage** | None |
| **Testing** | The composer and check self-tests, pytest, the 15 repository gates and the output format gate |

### Overview
`compose_board.py` cuts the composer to the model's type on its numbered section heads before it fills the model, so a call carries one builder. Three Flow Mode rules and one playbook rule change in prose, the Project mirror takes the two that apply inside a Project and the driver reads two new facts from each scenario's script.
<!-- /ANCHOR:summary -->

---

<!-- ANCHOR:quality-gates -->
## 2. QUALITY GATES

### Definition of Ready
- [x] Problem statement clear and scope documented
- [x] Success criteria measurable
- [x] Dependencies identified

### Definition of Done
- [x] All acceptance criteria met
- [x] validate.sh --strict passes
- [x] Docs updated (spec, plan, tasks)
<!-- /ANCHOR:quality-gates -->

---

<!-- ANCHOR:architecture -->
## 3. ARCHITECTURE

### Pattern
One composer source, cut per call by the wrapper

### Key Components
- **`assets/compose-board.js`**: the composer, in numbered sections. Section 3 holds the primitives, Sections 4 and 5 the graph layout, 6 the sequence and 7 the gantt builder
- **`compose_board.py for_type`**: drops the sections of the other types and rewrites the builders line and the build call
- **`run/adaptive_compare.py`**: reads whether a scenario answers the write gate and whether it needs no hosted Figma server

### Data Flow
The model's `type` picks the sections to keep, the cut composer takes the model and the theme. The result is one `use_figma` call.
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
| Unit | The cut composer per type | `compose_board.py --self-test` |
| Integration | Skill sources and the Project mirror | `benchmark/gates/run_gates.sh`, the output format gate and the Sync Loop parity check |
| Static | The driver's scenario selection | A load of all 54 FigJam scenarios through `load_playbook` |
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:dependencies -->
## 6. DEPENDENCIES

| Dependency | Type | Status | Impact if Blocked |
|------------|------|--------|-------------------|
| Phase 038 run record | Internal | Complete | The findings would have no source |
<!-- /ANCHOR:dependencies -->

---

<!-- ANCHOR:rollback -->
## 7. ROLLBACK PLAN

- **Trigger**: A cut composer draws a board wrong
- **Procedure**: Make `fill_template` call `compact_template()` with no kind, which restores the whole composer, or revert the phase's commits
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
| Setup | Low | 15 minutes |
| Core Implementation | Med | 2 hours |
| Verification | Low | 1 hour |
| **Total** | | **3 hours** |
<!-- /ANCHOR:effort -->

---

<!-- ANCHOR:enhanced-rollback -->
## L2: ENHANCED ROLLBACK

### Pre-deployment Checklist
- [x] Backup created: the last commit holds the previous composer
- [x] Feature flag: not applicable
- [x] Monitoring: not applicable

### Rollback Procedure
1. Revert the composer commit
2. Run the composer self-test
3. Tell the operator

### Data Reversal
- **Has data migrations?** No
- **Reversal procedure**: N/A
<!-- /ANCHOR:enhanced-rollback -->
