---
title: "Feature Specification: Phase 3: Interactive intake research"
description: "Both packets ask one bounded round of questions and then draw, so a thin brief yields a board that answers the wrong question. This phase researches it in five DeepSeek iterations and ranks changes."
trigger_phrases:
  - "interactive intake research"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.2 -->
# Feature Specification: Phase 3: Interactive intake research

<!-- SPECKIT_LEVEL: 2 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 2 |
| **Priority** | P1 |
| **Status** | Complete |
| **Created** | 2026-10-21 |
| **Branch** | `main` |
| **Parent Spec** | ../spec.md |
| **Phase** | 3 of 3 |
| **Predecessor** | None |
| **Successor** | None. The ranked changes feed a later change the operator chooses |
| **Handoff Criteria** | research/research.md exists and the operator has chosen which changes to apply |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:phase-context -->
## Phase Context

This is **Phase 3** of the third FigJam research round under the Product Owner FigJam flow generation upgrade.

**Scope Boundary**: Research and synthesis only. No Product Owner source file changes.

**Dependencies**:
- sk-create-figjam and sk-product-owner as phase 029 left them, and the earlier syntheses in `../../009-figjam-skill-research/research/research.md` and `../../016-figjam-improvement-research/research/research.md`.
- The 22 public repos pinned for phase 016, copied under `research/corpus/`, which git ignores.

**Deliverables**:
- 5 DeepSeek iteration files and a deep-research state log under `research/lineages/deepseek/`.
- `research/research.md`, a synthesis written and checked on DeepSeek.

**Changelog**:
- When this phase closes, refresh the matching file in ../changelog/ using the parent packet number plus this phase folder name.
<!-- /ANCHOR:phase-context -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
Both packets ask one bounded round of questions and then draw, so a thin brief yields a board that answers the wrong question.

### Purpose
Design an intake for sk-product-owner and sk-create-figjam that keeps asking until it is confident it understands the feature, and spars with the user on what the board conveys and how it looks.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- Design an intake for sk-product-owner and sk-create-figjam that keeps asking until it is confident it understands the feature, and spars with the user on what the board conveys and how it looks
- Repos and pages found during the run, cited by path or URL

### Out of Scope
- Editing the packets, their mirrors or the kernel. This phase proposes, a later change applies
- Any Barter screenshot, Barter flow or board URL

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| research/ | Create | Iterations, state log, corpus and the synthesis |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | Run 5 deep-research iterations on DeepSeek V4.1 Flash at max through cli-pi and llmgateway, with convergence stopping disabled. |
| REQ-002 | Each iteration widens the sources or deepens an earlier finding and cites them as [SOURCE: path:line] or [SOURCE: URL]. |
| REQ-003 | A DeepSeek V4.1 Flash max worker writes `research/research.md` after opening each cited line it keeps. |
| REQ-004 | Research/research.md proposes an intake loop with a confidence rule, a stop rule, the questions it asks and the sparring step, each naming the Product Owner file it changes and the source it comes from. |

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

- **SC-001**: 5 iteration records exist and none ends the run early.
- **SC-002**: The operator can choose which changes to apply from `research/research.md` alone.
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Dependency | DeepSeek through llmgateway | Run stalls | Rerun the iteration |
| Risk | DeepSeek claims drift from the cited lines | High | The synthesis worker opens every cited line it keeps, and the orchestrator spot-checks |
| Risk | Third-party code enters the public repo | Med | `research/.gitignore` ignores `corpus/` |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:nfr -->
## L2: NON-FUNCTIONAL REQUIREMENTS

### Security
- **NFR-S01**: No secrets, board URLs or Barter flows in any prompt or output.

### Reliability
- **NFR-R01**: The run is staged outside Product Owner and copied in, so a failed run leaves the packet as it was.
<!-- /ANCHOR:nfr -->

---

<!-- ANCHOR:edge-cases -->
## L2: EDGE CASES

### Error Scenarios
- A gateway failure: the iteration is rerun and logged.

### State Transitions
- Partial run: the state log shows where it stopped, and the run resumes.
<!-- /ANCHOR:edge-cases -->

---

<!-- ANCHOR:complexity -->
## L2: COMPLEXITY ASSESSMENT

| Dimension | Score | Notes |
|-----------|-------|-------|
| Scope | 6/25 | One synthesis |
| Risk | 4/25 | No source change |
| Research | 14/20 | Five iterations |
| **Total** | **24/70** | **Level 2** |
<!-- /ANCHOR:complexity -->

---

<!-- ANCHOR:questions -->
## 10. OPEN QUESTIONS

- None.
<!-- /ANCHOR:questions -->
