---
title: "Feature Specification: Phase 1: research"
description: "Twenty-iteration deep research on turning screenshots, Figma flows and product docs into FigJam flows from Product Owner, ending in an Opus 5.5 synthesis that fixes the later phases."
trigger_phrases:
  - "phase 1 research"
  - "figjam research"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.2 -->
# Feature Specification: Phase 1: research

<!-- SPECKIT_LEVEL: 2 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 2 |
| **Priority** | P0 |
| **Status** | Draft |
| **Created** | 2026-10-19 |
| **Branch** | `main` |
| **Parent Spec** | ../spec.md |
| **Phase** | 1 of 1 |
| **Predecessor** | None |
| **Successor** | Later phases, named by the synthesis |
| **Handoff Criteria** | research/research.md exists and the operator has approved its child-spec list |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:phase-context -->
## Phase Context

This is **Phase 1** of the Product Owner FigJam flow generation upgrade specification.

**Scope Boundary**: Research and synthesis only. No file outside this phase folder changes.

**Dependencies**:
- `.skilled/skills/mcp-tooling/mcp-figma`, the Figma MCP skill to be duplicated.
- `.skilled/skills/sk-design/sk-design-diagram`, the flow-chart rules to translate to FigJam.
- Media Editor (`runtime/claude-plugin`) as the Claude Code plugin precedent.
- Moneybird Accountant (`hub-router.json`, `mode-registry.json`) as the parent-hub precedent.

**Deliverables**:
- 20 DeepSeek iteration files and a deep-research state log under `research/lineages/deepseek/`.
- 8 Luna iteration files under `research/lineages/luna/iterations/`.
- `research/research.md`, the synthesis written by a fresh Opus 5.5 high agent.

**Changelog**:
- When this phase closes, refresh the matching file in ../changelog/ using the parent packet number plus this phase folder name.
<!-- /ANCHOR:phase-context -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
Product Owner cannot turn screenshots, Figma flows or product docs into diagrams. Four parts of the fix are unproven: what the Figma MCP can build in FigJam, how a duplicate of the figma skill lives inside Product Owner, how a Claude Code plugin sits beside the Claude Project, and how changes sync back to the shared skill repo across two git repos.

### Purpose
Produce evidence-cited findings and a ranked plan that fixes the names, order, scope and verification of the later phases.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- FigJam capability and limits through the Figma MCP, and how each input type becomes a flow model.
- Which sk-design-diagram rules carry over to FigJam, and which need a FigJam-native replacement.
- Embedding a duplicate of mcp-figma in Product Owner, the plugin form, the sync path back to `.skilled` and the parent-hub conversion.
- Lessons from the Media Editor plugin and the Moneybird Accountant hub.
- Risks: public-repo privacy, Figma auth and rate limits, parity gates and the format gate.

### Out of Scope
- Editing the Product Owner system, `.skilled` or any skill - this phase finds, later phases build.
- Commits, pushes and branches - none are part of research.

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| research/ | Create | Iterations, state log, cross-checks and the synthesis |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | Run 20 deep-research iterations on DeepSeek V4.1 Flash at max through cli-pi and llmgateway, with convergence stopping disabled. GLM 5.3 Flash at max is used only when DeepSeek fails. |
| REQ-002 | Run an 8-iteration Luna lineage at max, fast tier, through cli-codex. |
| REQ-003 | A fresh Opus 5.5 high agent writes `research/research.md` from the research files, with every claim tagged confirmed or inferred. |
| REQ-004 | The synthesis names the final later phases with order, scope and verification, and carries a copy and avoid list from Media Editor and from Moneybird Accountant. |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement |
|----|-------------|
| REQ-005 | The orchestrator posts a one-line status about every 3 minutes while agents run. |

> Acceptance criteria for these requirements live in `acceptance-criteria.md`,
> which is the document that decides whether this packet may close.
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: 20 iteration records exist and none ends the run early.
- **SC-002**: The operator can approve or amend the later phases from `research/research.md` alone.
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Dependency | DeepSeek through llmgateway | Run stalls | Fall back to GLM 5.3 Flash at max |
| Risk | DeepSeek answers vanish at the output cap | High | Small batches, a canary per batch, split on a miss, read `--mode json` |
| Risk | Billing errors exit 0 | Med | Read `--mode json` output, dispatch pi from the repo root |
| Risk | Synthesis built from a summary | Med | The Opus agent reads the research files directly |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:nfr -->
## L2: NON-FUNCTIONAL REQUIREMENTS

### Security
- **NFR-S01**: No secrets or tokens in research files or logs.
- **NFR-S02**: Nothing from the public Product Owner repo's private context leaves it through an external model prompt unreviewed.

### Reliability
- **NFR-R01**: A failed iteration is rerun, never skipped, so the count stays at 20.
<!-- /ANCHOR:nfr -->

---

<!-- ANCHOR:edge-cases -->
## L2: EDGE CASES

### Error Scenarios
- External service failure: switch the lineage to the GLM fallback and record the switch in the state log.
- Empty model output at exit 0: treat as a miss, split the batch and rerun.

### State Transitions
- Partial completion: resume from the last iteration record in the state log.
<!-- /ANCHOR:edge-cases -->

---

<!-- ANCHOR:complexity -->
## L2: COMPLEXITY ASSESSMENT

| Dimension | Score | Notes |
|-----------|-------|-------|
| Scope | 10/25 | Research files only |
| Risk | 8/25 | External models, no source edits |
| Research | 18/20 | 20 iterations across four precedents |
| **Total** | **36/70** | **Level 2** |
<!-- /ANCHOR:complexity -->

---

<!-- ANCHOR:questions -->
## 10. OPEN QUESTIONS

- Which Figma MCP route (hosted, desktop, or both) can write to FigJam? The research decides.
- Should the plugin carry the figma skill or call the embedded copy? The research decides.
<!-- /ANCHOR:questions -->
