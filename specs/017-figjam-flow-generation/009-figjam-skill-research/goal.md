---
title: "Goal: Phase 9: FigJam skill research"
description: "The durable directive this packet executes against and the criteria that decide when it is done."
trigger_phrases:
  - "figjam skill research goal"
importance_tier: "important"
contextType: "planning"
_memory:
  continuity:
    packet_pointer: "product-owner/017-figjam-flow-generation/009-figjam-skill-research"
    last_updated_at: "2026-10-20T07:37:46Z"
    last_updated_by: "scaffold"
    recent_action: "Authored the durable directive"
    next_safe_action: "Execute against the completion criteria"
    blockers: []
    key_files: []
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "1004bf13-7863-4447-a63e-6ad2f5fcfd86"
      parent_session_id: null
    completion_pct: 0
    open_questions: []
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: goal | v2.2 -->
# Goal: Phase 9: FigJam skill research

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->
<!-- GOAL_AUTHORING: .skilled/skills/sk-doc/sk-create-goal/SKILL.md -->

---

<!-- ANCHOR:directive -->
## 1. DURABLE DIRECTIVE

**Objective:** Produce 20 iterations of evidence-cited research on the strongest public FigJam diagram skills on GitHub, each compared with Product Owner's Flow Mode, and end with a ranked list of changes Flow Mode, its check script and its Project mirror should adopt.

### Decisions

Frozen choices. Changing one is an amendment.

| ID | Decision |
|----|----------|
| D1 | This phase produces findings only. No Product Owner source file changes, and every improvement is a proposal |
| D2 | Every iteration runs on DeepSeek V4.1 Flash at max reasoning through cli-pi on llmgateway, with no second lineage. A gateway failure reruns the same iteration and is logged, never skipped. The fallback model and the synthesis writer are the ones parent D4 names |
| D3 | All 20 iterations run. Convergence never stops the loop, because the stop policy is max-iterations and convergence mode is off |
| D4 | Each iteration either widens the corpus with a new repo, file or question, or deepens an earlier finding, and says which earlier iteration it builds on |
| D5 | The corpus starts as eight repos pinned to a commit: figma/mcp-server-guide, IamTheLime/dotfiles, southleft/figma-console-mcp-skills, mkaralevich/pi-figma-labor, amo-tech-ai/rocket-path-ai, atezer/FMCP, ompug/diagram-codebase and memi-design/mermaid-jam. A repo added later is pinned the same way |
| D6 | No Barter screenshot, Barter flow or board URL enters a prompt or an output. Flow Mode is compared through its public source files only |

<!-- /ANCHOR:directive -->

---


<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

- [x] research/lineages/deepseek/deep-research-state.jsonl holds 20 iteration records
- [x] research/lineages/deepseek/iterations/ holds iteration-001.md to iteration-020.md, and each cites at least one corpus file as [SOURCE: path:line]
- [x] research/research.md ranks at least 10 improvements, each naming the Flow Mode file it changes and the corpus file it comes from
- [x] research/research.md gives an adopt or reject verdict on FigJam's single page, emojis in Mermaid, reserved node IDs and underscores in node IDs
- [x] git status shows no changed file outside specs/017-figjam-flow-generation/ from this phase
- [x] validate.sh --strict on 009-figjam-skill-research prints RESULT: PASSED
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
| Phase opened | Done | 2026-10-20, scaffolded as a child of 017 |
| Corpus pinned | Done | figma/mcp-server-guide 7047cb45, IamTheLime/dotfiles 77976c17, southleft/figma-console-mcp-skills 807fcc1c, mkaralevich/pi-figma-labor 97e4c6d8, amo-tech-ai/rocket-path-ai a616047d, atezer/FMCP 364c0ce6, ompug/diagram-codebase b1e20f57, memi-design/mermaid-jam 568c1e8c |
| 20-iteration DeepSeek lineage | Done | 20 iteration records, synthesis_complete with stopReason maxIterationsReached, 09:40 to 10:07 |
| Merge | Done | fanout-merge.cjs exit 0, 235 key findings |
| Opus 5.5 high synthesis | Done | research/research.md, 5,574 words, 15 ranked changes, all four gaps adopted, 14 iteration claims corrected |
| Orchestrator spot-check | Done | A subgraph model fails flow_check.py, an emoji, underscore and end-ID model passes, flow-mode.md:142 already names missing items |
| Scope check | Done | Product Owner shows no changed file outside specs/017 from this phase. The outer repo's other changes date from 2026-10-19. The staging folder is deleted |
| Strict validation | Done | validate.sh --recursive --strict on 017: 10 of 10 RESULT: PASSED, exit 0 |

### Deviations and findings

| Item | Note |
|------|------|
| Run staged at specs/z-staging-po-009-research | Same reason as 001: the runner refuses symlinked spec paths, and running inside Product Owner loads its persona. research/ is copied here and the staging folder deleted after the run |
| No route-proof fields in the state records | The CLI lineage runs the whole loop in one detached prompt. 001's DeepSeek records have the same shape |
| DeepSeek state timestamps run past the real end time | The runner flagged 14 of 22 rows. The synthesis was told not to trust them |
| Corpus ignore rule lives in research/.gitignore | Keeps the third-party clones out of the public repo without touching a file outside the packet |
| Containment quarantined 009 goal.md | The runner snapshot caught the orchestrator's own log edit made during the run. Nothing was reverted |
<!-- /ANCHOR:log -->
