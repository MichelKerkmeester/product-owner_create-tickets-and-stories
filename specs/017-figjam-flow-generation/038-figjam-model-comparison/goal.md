---
title: "Goal: Phase 38: FigJam model comparison"
description: "The durable directive this packet executes against and the criteria that decide when it is done."
trigger_phrases:
  - "figjam model comparison goal"
importance_tier: "important"
contextType: "planning"
_memory:
  continuity:
    packet_pointer: "017-figjam-flow-generation/038-figjam-model-comparison"
    last_updated_at: "2026-10-26T01:45:00Z"
    last_updated_by: "claude-code"
    recent_action: "Closed every completion criterion"
    next_safe_action: "Open a phase for the run README findings"
---
<!-- SPECKIT_TEMPLATE_SOURCE: goal | v2.2 -->
# Goal: Phase 38: FigJam model comparison

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->
<!-- GOAL_AUTHORING: .skilled/skills/sk-doc/sk-create-goal/SKILL.md -->

---

<!-- ANCHOR:directive -->
## 1. DURABLE DIRECTIVE

**Objective:** Run the seven board-quality scenarios on DeepSeek V4.1 Flash max, SWE 2 Max and GLM 5.3 Flash max against the composer phase 037 shipped, grade every board on the 22-point scorecard, say which model draws FigJam boards best and keep the best board of each type as the gallery.

### Decisions

Frozen choices. Changing one is an amendment.

| ID | Decision |
|----|----------|
| D1 | All three models run through the Devin CLI at their max variants |
| D2 | One adaptive operator drives every run and labels each extra turn |
| D3 | Graders and readers are fresh Sonnet 5.5 agents, never a model under test |
| D4 | The gallery board of each type is the highest total, then a pass, then fewer extra turns |
| D5 | Runs go one at a time on the one fictional test file. No Barter board, board URL, file key or plan name in any file |
| D6 | The operator authorised pushing to the public repository and Barter AI Systems without asking, by sk-git's commit standards |
<!-- /ANCHOR:directive -->

---

<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

- [x] All 21 runs are in the run folder with their replies, tool calls and `meta.json`
- [x] Every written board has three renders and a 22-point scorecard from a neutral grader
- [x] The run README names the best model per type and overall with the losses that decided it
- [x] The seven gallery images are the best board per type with honest captions
- [x] No board URL, file key, plan name or email is in any changed file
<!-- /ANCHOR:completion -->

---

<!-- ANCHOR:log -->
## 4. LOG

Everything below is VOLATILE. It is not part of the directive. It is not
copied into the objective and it is expected to grow. Progress, evidence, deviations
and findings belong here.

### Progress

| Item | State | Evidence |
|------|-------|----------|
| Phase opened | Done | 2026-10-25, a child of 017 after 037 |
| Batch run | Done | 21 of 21 runs completed, pushed per scenario through 315c8179 |
| Grading | Done | 21 scorecards by Sonnet 5.5 graders, three rotated readers, results in 23eb8293 |
| Best model | Done | GLM and SWE tie at 148, SWE 2 Max recommended for never writing early or changing others' boards |
| Gallery | Done | Seven best boards by ADR-004 in 33f93557 |
| Deviation | Recorded | Readers rotated across models, ADR-003 as-run note |
| Finding | Open | GLM deleted ten test boards on FJ-024 after a generic yes, a later phase should require a named yes |
<!-- /ANCHOR:log -->
