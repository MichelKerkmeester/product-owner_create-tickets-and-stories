---
title: "Goal: Phase 1: research"
description: "The durable directive this packet executes against and the criteria that decide when it is done."
trigger_phrases:
  - "research goal"
importance_tier: "important"
contextType: "planning"
_memory:
  continuity:
    packet_pointer: "product-owner/017-figjam-flow-generation/001-research"
    last_updated_at: "2026-10-19T21:00:00Z"
    last_updated_by: "scaffold"
    recent_action: "Authored the durable directive"
    next_safe_action: "Execute against the completion criteria"
    blockers: []
    key_files: []
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "unset"
      parent_session_id: null
    completion_pct: 0
    open_questions: []
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: goal | v2.2 -->
# Goal: Phase 1: research

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->
<!-- GOAL_AUTHORING: .skilled/skills/sk-doc/sk-create-goal/SKILL.md -->

---

<!-- ANCHOR:directive -->
## 1. DURABLE DIRECTIVE

**Objective:** Produce twenty iterations of evidence-cited research on turning screenshots, Figma flows and product docs into FigJam flows from Product Owner, on the Media Editor plugin and Moneybird Accountant hub precedents, and on syncing an embedded figma skill back to .skilled, ending in an Opus 5.5 synthesis that fixes the later phases.

### Decisions

Frozen choices. Changing one is an amendment.

| ID | Decision |
|----|----------|
| D1 | DeepSeek V4.1 Flash max through cli-pi and llmgateway runs the 20 iterations with convergence off. GLM 5.3 Flash max runs only when DeepSeek fails. SWE 2 max through cli-devin runs only when DeepSeek, GLM and Luna usage all run out. |
| D2 | Luna max, fast tier, through cli-codex runs its own 8-iteration lineage on the same topic. |
| D3 | Each iteration opens a new question or deepens an earlier finding. |
| D4 | A fresh Opus 5.5 high agent writes the synthesis from the research files. |
| D5 | This phase produces findings only. No file outside 001-research/ changes. |

<!-- /ANCHOR:directive -->

---


<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

- [ ] research/lineages/deepseek/deep-research-state.jsonl holds 20 iteration records and no converged stop
- [ ] research/lineages/deepseek/iterations/iteration-001.md through iteration-020.md exist
- [ ] research/lineages/luna/iterations/iteration-001.md through iteration-008.md exist
- [ ] research/research.md tags every claim confirmed or inferred and lists the later phases with order, scope and verification
- [ ] research/research.md has a copy-and-avoid section each for Media Editor and Moneybird Accountant
- [ ] git status in Product Owner shows no modified path outside 001-research/ and the parent packet docs
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
| DeepSeek lineage | Done | 20 iteration records, no converged stop, exit 0 |
| Luna lineage | Done | 8 iterations, service_tier=fast, exit 0 |
| Synthesis | Done | research/research.md by a fresh Opus 5.5 high agent, 164 citations opened, 3 failed and fixed |

### Deviations and findings

| Item | Note |
|------|------|
| Run staged at specs/z-staging-po-017-research | The research runner refuses symlinked spec paths, and running inside Product Owner loads its persona AGENTS.md. research/ was copied here and the staging folder deleted |
| SOURCE_TAGS warns on 455 of 588 citations | The validator resolves paths from the Product Owner root, while the iterations cite paths from the AI Systems root |

<!-- /ANCHOR:log -->
