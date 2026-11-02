---
title: "Feature Specification: Phase 9: FigJam skill research"
description: "Flow Mode was built without comparing it to the public FigJam diagram skills, Figma's own among them. This phase runs 20 deep-research iterations on those skills and ends in a ranked list of changes for Flow Mode."
trigger_phrases:
  - "figjam skill research"
  - "phase 9 figjam skill research"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.2 -->
# Feature Specification: Phase 9: FigJam skill research

<!-- SPECKIT_LEVEL: 2 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 2 |
| **Priority** | P1 |
| **Status** | In Progress |
| **Created** | 2026-10-20 |
| **Branch** | `main` |
| **Parent Spec** | ../spec.md |
| **Phase** | 9 of 9 |
| **Predecessor** | 005-flow-mode |
| **Successor** | None. The ranked changes feed a later Flow Mode revision |
| **Handoff Criteria** | research/research.md exists with at least 10 ranked changes and the operator has chosen which to apply |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:phase-context -->
## Phase Context

This is **Phase 9** of the Product Owner FigJam flow generation upgrade specification.

**Scope Boundary**: Research and synthesis only. No Product Owner source file changes.

**Dependencies**:
- Flow Mode as built in phase 005: `sk-product-owner/references/flow-mode.md`, `sk-product-owner/assets/flow-templates.md` and `sk-product-owner/scripts/flow_check.py`.
- Eight public repos pinned to a commit under `research/corpus/`, which git ignores.

**Deliverables**:
- 20 DeepSeek iteration files and a deep-research state log under `research/lineages/deepseek/`.
- `research/research.md`, the synthesis written by a fresh Opus 5.5 high agent.

**Changelog**:
- When this phase closes, refresh the matching file in ../changelog/ using the parent packet number plus this phase folder name.
<!-- /ANCHOR:phase-context -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
Flow Mode was built without comparing it to the public FigJam diagram skills, Figma's own among them. A first look found one rule that cannot work: FigJam files have one page, and Flow Mode writes into a new page.

### Purpose
Produce evidence-cited findings and a ranked list of changes for Flow Mode, its check script and its Project mirror.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- Rules, checks, write routes, read-back, failure handling, file and page handling, layout, colour, shapes, density and labels in each corpus skill.
- Verdicts on four known gaps and on Flow Mode's five deliberate limits.
- Repos found during the run with `gh search`, pinned the same way.

### Out of Scope
- Editing Flow Mode, its mirror or the kernel. This phase proposes, a later change applies.
- Any Barter screenshot, Barter flow or board URL.

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
| REQ-001 | Run 20 deep-research iterations on DeepSeek V4.1 Flash at max through cli-pi and llmgateway, with convergence stopping disabled. |
| REQ-002 | Each iteration widens the corpus or deepens an earlier finding and cites corpus files as [SOURCE: path:line]. |
| REQ-003 | A fresh Opus 5.5 high agent writes `research/research.md` after checking each cited line it uses. |
| REQ-004 | The synthesis ranks at least 10 changes, each naming the Flow Mode file it changes and the corpus file it comes from, and gives a verdict on the four known gaps. |

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
- **SC-002**: The operator can choose which changes to apply from `research/research.md` alone.
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Dependency | DeepSeek through llmgateway | Run stalls | Rerun the iteration, then the fallback parent D4 names |
| Risk | DeepSeek claims drift from the cited lines | High | The Opus synthesis opens every cited line it uses |
| Risk | The runner's snapshot copies private files | Med | `specs/**/containment/` is git-ignored |
| Risk | Third-party code enters the public repo | Med | `specs/**/research/corpus/` is git-ignored |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:nfr -->
## L2: NON-FUNCTIONAL REQUIREMENTS

### Security
- **NFR-S01**: No secrets or tokens in research files or logs.
- **NFR-S02**: No Barter screenshot, flow or board URL enters a prompt or an output.

### Reliability
- **NFR-R01**: A failed iteration is rerun, never skipped, so the count stays at 20.
<!-- /ANCHOR:nfr -->

---

<!-- ANCHOR:edge-cases -->
## L2: EDGE CASES

### Error Scenarios
- Empty model output at exit 0: treat as a miss and rerun the iteration.
- A cited line that does not say what the iteration claims: the synthesis drops or corrects the claim and lists it.

### State Transitions
- Partial completion: resume from the last iteration record in the state log.
<!-- /ANCHOR:edge-cases -->

---

<!-- ANCHOR:complexity -->
## L2: COMPLEXITY ASSESSMENT

| Dimension | Score | Notes |
|-----------|-------|-------|
| Scope | 8/25 | Research files only |
| Risk | 6/25 | External models, no source edits |
| Research | 18/20 | 20 iterations across eight repos |
| **Total** | **32/70** | **Level 2** |
<!-- /ANCHOR:complexity -->

---

<!-- ANCHOR:questions -->
## 10. OPEN QUESTIONS

- Which of the ranked changes should a Flow Mode revision apply? The operator decides.
<!-- /ANCHOR:questions -->
