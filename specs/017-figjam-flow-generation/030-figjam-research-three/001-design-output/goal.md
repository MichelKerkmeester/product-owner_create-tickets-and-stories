---
title: "Goal: Phase 1: Design output research"
description: "The durable directive this packet executes against and the criteria that decide when it is done."
trigger_phrases:
  - "design output research goal"
importance_tier: "important"
contextType: "planning"
_memory:
  continuity:
    packet_pointer: "product-owner/017-figjam-flow-generation/030-figjam-research-three/001-design-output"
    last_updated_at: "2026-10-21T10:00:00Z"
    last_updated_by: "claude-code"
    recent_action: "Ran the lineage and wrote the checked synthesis"
    next_safe_action: "The operator chooses which changes to apply"
    blockers: []
    key_files: []
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "1004bf13-7863-4447-a63e-6ad2f5fcfd86"
      parent_session_id: null
    completion_pct: 100
    open_questions: []
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: goal | v2.2 -->
# Goal: Phase 1: Design output research

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->
<!-- GOAL_AUTHORING: .skilled/skills/sk-doc/sk-create-goal/SKILL.md -->

---

<!-- ANCHOR:directive -->
## 1. DURABLE DIRECTIVE

**Objective:** Find how sk-create-figjam's FigJam diagrams can look and read better: layout, hierarchy, colour, density, labels, annotation and the board as a whole.

### Decisions

Frozen choices. Changing one is an amendment.

| ID | Decision |
|----|----------|
| D1 | Five iterations on DeepSeek V4.1 Flash at max through cli-pi on llmgateway, with convergence stopping off, as the operator asked on 2026-10-21 |
| D2 | A DeepSeek V4.1 Flash max worker writes the synthesis after opening each cited line it keeps |
| D3 | No Barter screenshot, Barter flow or board URL enters a prompt or an output. Examples use fictional companies |

<!-- /ANCHOR:directive -->

---

<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

- [x] research/lineages/deepseek/deep-research-state.jsonl holds 5 iteration records
- [x] research/lineages/deepseek/iterations/ holds iteration-001.md to iteration-005.md, and each cites at least one source
- [x] research/research.md ranks at least 8 changes to the design and output of FigJam diagrams, each naming the Product Owner file it changes and the source it comes from
- [x] validate.sh --strict on 001-design-output prints RESULT: PASSED
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
| Phase opened | Done | 2026-10-21, a child of 030-figjam-research-three |
| 5-iteration DeepSeek lineage | Done | research/lineages/deepseek/deep-research-state.jsonl holds 5 iteration records with stopReason maxIterationsReached, fanout exit 0, staged at specs/z-staging-po-030a in the outer repository and copied here |
| Merge | Done | fanout-merge.cjs, 61 key findings |
| DeepSeek synthesis | Done | A read-only DeepSeek V4.1 Flash max worker wrote research/research.md on its first attempt. Section 5 lists 10 dropped or corrected iteration claims. All 66 local citations resolve to an existing file and line, and the orchestrator read the top cited lines against their claims, plus 0 URL citations |
| Strict validation | Done | validate.sh --strict on this folder printed RESULT: PASSED |
<!-- /ANCHOR:log -->
