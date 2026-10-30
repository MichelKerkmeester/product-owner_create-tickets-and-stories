---
title: "Goal: Phase 52: FigJam boards that teach the reader something"
description: "The durable directive this packet executes against and the criteria that decide when it is done."
trigger_phrases:
  - "packet goal"
  - "durable directive"
  - "completion criteria"
  - "goal binding"
importance_tier: "important"
contextType: "planning"
_memory:
  continuity:
    packet_pointer: "017-figjam-flow-generation/052-figjam-boards-that-teach"
    last_updated_at: "2026-10-30T09:00:00Z"
    last_updated_by: "claude-code"
    recent_action: "Scaffolded the phase"
    next_safe_action: "Change the checker for section notes, detail levels and the focus reason"
    blockers: []
    key_files: []
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "cb7f5c8f-ad61-46e0-8985-4b3286150879"
      parent_session_id: null
    completion_pct: 0
    open_questions: []
    answered_questions: []
---
# Goal: Phase 52: FigJam boards that teach the reader something

<!-- SPECKIT_TEMPLATE_SOURCE: goal | v2.2 -->
<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->
<!-- GOAL_AUTHORING: .skilled/skills/sk-doc/sk-create-goal/SKILL.md -->

---

<!-- ANCHOR:directive -->
## 1. DURABLE DIRECTIVE

**Objective:** Make `sk-create-figjam` boards carry what their source says, with section notes, detail cards on four types, a compact key and a reason for every accent, score that as Substance, give the ten gallery scenarios spec-sized sources, release it with the Claude Project mirror, rerun the gallery on GLM 5.3 Flash max through Devin and draw every gallery image from that run, with no board URL, file key, plan name or email in any committed file.

### Decisions

Frozen choices. Changing one is an amendment.

| ID | Decision |
|----|----------|
| D1 | Board maker: `glm-5-3-flash-max` on Devin. |
| D2 | `%% about:` notes, up to three lines of 56 characters, required on a Balanced or Faithful zoned flow. |
| D3 | Detail cards at Balanced (4 lines) and Faithful (10) on user flow, process, architecture and state. |
| D4 | A compact key, and every accent names its reason. |
| D5 | Substance in the reading zoom, 24 points, pass at 20. |
| D6 | Ten scenarios with spec-sized fictional sources and two source questions each. |
| D7 | Every gallery image from this run, a failing board rerun once. |

<!-- /ANCHOR:directive -->

---

<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

- [ ] The checker and composer changes pass their fixtures and a scratch board shows notes and the compact key
- [ ] The scorecard defines Substance and the ten scenarios carry sources and source questions
- [ ] Release 1.0.17.0 with the Claude Project mirror, and parity passes
- [ ] Ten runs on `glm-5-3-flash-max` are graded and the gallery comes from them
- [ ] The scan prints nothing, the gates pass and `validate.sh --strict` prints RESULT: PASSED
<!-- /ANCHOR:completion -->

---

<!-- ANCHOR:log -->
## 4. LOG

Everything below is VOLATILE. It is not part of the directive, it is not copied
into the objective, and it is expected to grow. Progress, evidence, deviations
and findings belong here.

### Progress

| Item | State | Evidence |
|------|-------|----------|
| Phase scaffolded | Done | spec, plan, tasks, acceptance criteria and this goal |
| Skill change and release | Done | checker, composer, docs, playbook, 1.0.17.0 and the Project mirror; gates 15 of 15 |

### Deviations

| Item | Note |
|------|------|
| Board maker route | GLM on Pi has no Figma write route, so Michel chose GLM on Devin |
| Project composer split | The new drawing code left one whole block 1,367 characters of model room, so the Project file carries a graph block and a sequence and gantt block |
| Source excerpts | Each scenario keeps its request and adds an excerpt, so the counts and Q1 to Q3 still hold and Q4 and Q5 measure Substance; Substance scores only where a scenario names source questions |
| Live composer check | The scratch Figma board was skipped; the first rerun board, FJ-022, is the live check before the other nine run |
<!-- /ANCHOR:log -->
