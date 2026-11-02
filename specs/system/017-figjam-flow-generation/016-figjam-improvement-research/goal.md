---
title: "Goal: Phase 16: FigJam improvement research"
description: "The durable directive this packet executes against and the criteria that decide when it is done."
trigger_phrases:
  - "figjam improvement research goal"
importance_tier: "important"
contextType: "planning"
_memory:
  continuity:
    packet_pointer: "product-owner/017-figjam-flow-generation/016-figjam-improvement-research"
    last_updated_at: "2026-10-20T21:00:00Z"
    last_updated_by: "claude-code"
    recent_action: "Wrote and verified the synthesis"
    next_safe_action: "The operator chooses which ranked changes to apply"
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
# Goal: Phase 16: FigJam improvement research

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->
<!-- GOAL_AUTHORING: .skilled/skills/sk-doc/sk-create-goal/SKILL.md -->

---

<!-- ANCHOR:directive -->
## 1. DURABLE DIRECTIVE

**Objective:** Produce 10 iterations of evidence-cited research on the public FigJam repos online and on how sk-create-figjam integrates with sk-product-owner and the hub, and end with a ranked list of changes to the packet and that integration.

### Decisions

Frozen choices. Changing one is an amendment.

| ID | Decision |
|----|----------|
| D1 | This phase produces findings only. No Product Owner source file changes, and every improvement is a proposal |
| D2 | Every iteration runs on DeepSeek V4.1 Flash at max reasoning through cli-pi on llmgateway, with no second lineage. A gateway failure reruns the same iteration and is logged, never skipped. The fallback model and the synthesis writer are the ones parent D4 names |
| D3 | All 10 iterations run. Convergence never stops the loop, because the stop policy is max-iterations and convergence mode is off |
| D4 | Each iteration either widens the corpus with a new repo, file or question, or deepens an earlier finding, and says which earlier iteration it builds on |
| D5 | The corpus is the 009 corpus plus the FigJam repos found by gh search on 2026-10-20, each pinned to a commit. A repo added later is pinned the same way |
| D6 | No Barter screenshot, Barter flow or board URL enters a prompt or an output. The packet is compared through its public source files only |

<!-- /ANCHOR:directive -->

---

<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

- [x] research/lineages/deepseek/deep-research-state.jsonl holds 10 iteration records
- [x] research/lineages/deepseek/iterations/ holds iteration-001.md to iteration-010.md, and each cites at least one file as [SOURCE: path:line]
- [x] research/research.md ranks at least 10 improvements, each naming the file it changes and the source it comes from
- [x] research/research.md ranks at least 3 improvements to the integration between sk-create-figjam, sk-product-owner and the hub
- [x] git status shows no changed file outside specs/017-figjam-flow-generation/ from this phase
- [x] validate.sh --strict on 016-figjam-improvement-research prints RESULT: PASSED
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
| Phase opened | Done | 2026-10-20, a child of 017 |
| Corpus pinned | Done | 15 new: figma/mcp-server-guide 056adaf7, figma/community-resources d868fb1f, figma/architecture-diagram-components c22de634, adobe/spectrum-design-data 900b522b, hferello/ai 181b6fd7, prasantloki/figjam-builder 2a271c94, rrichardsonv/parse-figjam 2722e737, ecestnrkl/figjam-mcp 8b484791, bluescaban/blueprints 2b987625, arinspunk/claude-talk-to-figma-mcp c7adf243, ulasbilgen/mcp-skills-plugins c61e27d4, tmcw/figjam-mermaid 57cf9174, lauragalera/figjam-erd-plugin 71bda9d7, lightspeedwp/.github 8f28eca8, openai/plugins 0722921d, amo-tech-ai/rocket-path-ai, atezer/FMCP, IamTheLime/dotfiles, memi-design/mermaid-jam, mkaralevich/pi-figma-labor, ompug/diagram-codebase, southleft/figma-console-mcp-skills. Seven 009 repos copied at their 009 pins |
| 10-iteration DeepSeek lineage | Done | 10 iteration records, stopReason maxIterationsReached, 22:11 to 22:27, fanout exit 0, every iteration cites 20 or more lines |
| Merge | Done | fanout-merge.cjs exit 0, 119 key findings |
| Opus 5.5 high synthesis | Done | research/research.md, 6,868 words, 12 ranked changes with 5 on the integration, 18 iteration claims dropped or corrected, every citation resolves |
| Orchestrator spot-check | Done | Router returns STORY with no question for a story plus FigJam request, mcp-wiring.md calls the hosted server unsupported, four templates carry Flows, kernel line 236 reads Outside Flow Mode, gh compare shows 1 commit |
| Scope check | Done | No Product Owner source file changed, the staging folder is deleted and the outer specs/ is clean |
| Extension run | Done | 2026-10-21, the operator asked for 5 more iterations. A Luna lineage was stopped in its first iteration when the operator switched to DeepSeek V4.1 Flash max. 5 iteration records, stopReason maxIterationsReached, fanout exit 0, 12 to 28 SOURCE tags per iteration, 43 merged key findings, lineage at research/lineages/deepseek-extension/ |
| Extension synthesis | Done | research.md Section 9: 8 implemented ranks found wanting, ranks 13 to 17, 20 claims corrected or dropped, 104 local citations resolved. The orchestrator reran four router probes and the repeated-label check, and each matched |
| Extension against D3 | Note | D3 bound the first run to 10 iterations. The 5 extra iterations are a separate lineage the operator asked for on 2026-10-21, so the first run's record is unchanged |
<!-- /ANCHOR:log -->
