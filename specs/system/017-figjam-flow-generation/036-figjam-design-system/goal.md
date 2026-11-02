---
title: "Goal: Phase 36: FigJam design system research"
description: "The durable directive this packet executes against and the criteria that decide when it is done."
trigger_phrases:
  - "figjam design system goal"
importance_tier: "important"
contextType: "planning"
_memory:
  continuity:
    packet_pointer: "product-owner/017-figjam-flow-generation/036-figjam-design-system"
    last_updated_at: "2026-10-25T19:45:00Z"
    last_updated_by: "claude-code"
    recent_action: "Closed the phase on the verified synthesis"
    next_safe_action: "Choose which ranked changes and which design spec questions to apply in a new phase"
    blockers: []
    key_files: []
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "348b59cb-58a2-4b49-8147-c40143312bc1"
      parent_session_id: null
    completion_pct: 100
    open_questions: []
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: goal | v2.2 -->
# Goal: Phase 36: FigJam design system research

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->
<!-- GOAL_AUTHORING: .skilled/skills/sk-doc/sk-create-goal/SKILL.md -->

---

<!-- ANCHOR:directive -->
## 1. DURABLE DIRECTIVE

**Objective:** Produce 7 iterations of evidence-cited research on sk-create-figjam that rank changes to the UI design quality and consistency of composed FigJam boards, and recommend a user-editable design spec file that agents read before composing so a repo user can restyle boards to their own taste.

### Decisions

Frozen choices. Changing one is an amendment.

| ID | Decision |
|----|----------|
| D1 | This phase produces findings only. No Product Owner source file, Project mirror or kernel changes, and every improvement is a proposal |
| D2 | The run is a fan-out with one lineage per executor: claude-opus-5-5 at medium effort through cli-claude-code for 3 iterations, swe-2-max through cli-devin for 2 and gpt-6-luna at max effort on the fast service tier through cli-codex for 2. A failed iteration is rerun on the same executor and logged, never skipped |
| D3 | All 7 iterations run. Convergence never stops a lineage, because the stop policy is max-iterations and convergence mode is off |
| D4 | The inputs are compose-board.js, flow-templates.md, the templates, the examples, the nine rendered screenshots, the style guide, the quality rubric, the type references and compose_board.py |
| D5 | The design spec file is modelled on a DESIGN.md Style Reference as the sk-design-md-generator mode of sk-design produces it |
| D6 | No Barter screenshot, Barter flow, board URL or Figma file key enters a prompt or an output |

<!-- /ANCHOR:directive -->

---

<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

- [x] The three lineages hold 3, 2 and 2 iteration files
- [x] Each iteration cites files as [SOURCE: path:line] and names the image file for any screenshot it uses
- [x] research/research.md ranks at least 10 design changes, each naming the file it changes and the evidence
- [x] research/research.md ranks at least 3 changes on consistency across diagram types
- [x] research/research.md recommends the design spec file's location, schema, readers, safe defaults and rubric check
- [x] git status shows no changed file outside specs/017-figjam-flow-generation/ from this phase
- [x] validate.sh --strict on 036-figjam-design-system prints RESULT: PASSED
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
| Phase opened | Done | 2026-10-25, a child of 017 |
| Three-lineage fan-out | Done | Staged at specs/z-staging-po-036-research in the outer repository, stop policy max-iterations, convergence off. opus 3, swe 2 and luna 2 iteration files. A monitor posted counts every 3 minutes from 20:08 to 20:32 |
| Sonnet slot | Note | The planned Sonnet 5.5 lineage on cli-pi was dropped because pi has no Claude route through llmgateway, and the operator moved that slot to a third Opus iteration |
| Merge | Done | fanout-merge.cjs merged 2 lineages and 45 key findings. The opus lineage was skipped because it wrote no state log |
| Opus 5.5 medium synthesis | Done | research/research.md: 75 iteration findings checked, 58 held, 15 corrected, 2 dropped, 8 added. 18 ranked changes with 8 on consistency, a design spec recommendation in Section 6 and six open questions in Section 9 |
| Scope check | Done | compose_board.py --self-test 815/815 passed during synthesis. No packet source file changed and the staging folder is deleted |
<!-- /ANCHOR:log -->
