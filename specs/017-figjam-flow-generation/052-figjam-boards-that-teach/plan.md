---
title: "Implementation Plan: Phase 52: FigJam boards that teach the reader something"
description: "Add section notes, wider detail cards, a compact key and a required focus reason to the checker and composer, score Substance, rewrite the ten gallery scenarios with spec-sized sources, release, mirror, then rerun the gallery on GLM 5.3 Flash max through Devin."
trigger_phrases:
  - "figjam boards that teach plan"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: plan-core | v2.3 -->
# Implementation Plan: Phase 52: FigJam boards that teach the reader something

<!-- SPECKIT_LEVEL: 2 -->

---

<!-- ANCHOR:summary -->
## 1. SUMMARY

`compose_board.py` already passes a `%% detail:` body to the composer for any flowchart step, and `compose-board.js` already draws a body card and a focus reason. The work is mostly in the rules: the checker opens detail cards to Balanced and to two more types, refuses an accent without a reason and reads the new `%% about:` line. The composer draws the notes under a zone or lane title and a compact key. The playbook gains Substance, and the run driver reruns the ten scenarios on `glm-5-3-flash-max`.
<!-- /ANCHOR:summary -->

---

<!-- ANCHOR:quality-gates -->
## 2. QUALITY GATES

| Gate | Command | Expected |
|------|---------|----------|
| Skill checks | `python3 scripts/flow_check.py --self-test` and the fixture suites | Pass |
| Repository gates | `bash benchmark/gates/run_gates.sh` | All pass |
| Sync Loop | `validate_parity.py product-owner`, the format gate | Parity passes, format as before |
| Redaction | `run/redact_run.py` per scenario and a scan | Nothing found |
| Spec | `validate.sh --strict` | RESULT: PASSED |
<!-- /ANCHOR:quality-gates -->

---

<!-- ANCHOR:architecture -->
## 3. ARCHITECTURE

The checker (`scripts/figjam_checks/flowchart.py`, `state.py`) owns the rules. `scripts/compose_board.py` turns a checked model into the MODEL JSON, with `about` notes on each zone and `body` on each step. `assets/compose-board.js` draws them inside `use_figma`. The run driver `run/adaptive_compare.py` sends a model id with no runtime prefix to Devin.
<!-- /ANCHOR:architecture -->

---

<!-- ANCHOR:phases -->
## 4. IMPLEMENTATION PHASES

1. Checker and composer changes with fixtures.
2. Docs, templates, examples, the scorecard and the ten scenarios.
3. Release, the Claude Project mirror and the gates.
4. The rerun, grading and the gallery.
5. Commit and, on Michel's yes, push.
<!-- /ANCHOR:phases -->

---

<!-- ANCHOR:testing -->
## 5. TESTING STRATEGY

Fixtures cover each new rule on its happy path and one refusal. A composed scratch board checks the notes and the key in Figma before the rerun. The rerun is the end-to-end test.
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:dependencies -->
## 6. DEPENDENCIES

| Dependency | Type | Status | Impact if Blocked |
|------------|------|--------|-------------------|
| Devin with `glm-5-3-flash-max` | External | To confirm | The rerun waits |
| The hosted Figma MCP and the team plan | External | Available | The rerun waits |
<!-- /ANCHOR:dependencies -->

---

<!-- ANCHOR:rollback -->
## 7. ROLLBACK PLAN

Revert the phase's commits in both repositories. Draft files in Figma are left for Michel to delete.
<!-- /ANCHOR:rollback -->

---

<!-- ANCHOR:phase-deps -->
## L2: PHASE DEPENDENCIES

| Phase | Depends On | Blocks |
|-------|------------|--------|
| Skill changes | None | Scenarios, release |
| Release and mirror | Skill changes | Rerun |
| Rerun and grading | Release | Gallery |
<!-- /ANCHOR:phase-deps -->

---

<!-- ANCHOR:effort -->
## L2: EFFORT ESTIMATION

| Phase | Complexity | Estimated Effort |
|-------|------------|------------------|
| Skill changes | High | Checker, composer, fixtures |
| Docs and scenarios | Medium | Ten sources and the scorecard |
| Rerun and grading | Medium | About an hour of runs, twenty notes, ten scorecards |
<!-- /ANCHOR:effort -->

---

<!-- ANCHOR:enhanced-rollback -->
## L2: ENHANCED ROLLBACK

### Pre-deployment Checklist
- [ ] Redaction scan clean before each commit

### Rollback Procedure
1. Revert the phase's commits in both repositories.

### Data Reversal
- **Has data migrations?** No
- **Reversal procedure**: None needed
<!-- /ANCHOR:enhanced-rollback -->
