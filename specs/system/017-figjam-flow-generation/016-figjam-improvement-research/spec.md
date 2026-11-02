---
title: "Feature Specification: Phase 16: FigJam improvement research"
description: "sk-create-figjam was rebuilt for seven diagram types in phase 015 without a second look at the public FigJam work. This phase runs 10 deep-research iterations on the FigJam repos online and on the packet's integration with sk-product-owner and the hub, and ends in a ranked list of changes."
trigger_phrases:
  - "figjam improvement research"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.2 -->
# Feature Specification: Phase 16: FigJam improvement research

<!-- SPECKIT_LEVEL: 2 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 2 |
| **Priority** | P1 |
| **Status** | Complete |
| **Created** | 2026-10-20 |
| **Branch** | `main` |
| **Parent Spec** | ../spec.md |
| **Phase** | 16 of 16 |
| **Predecessor** | 015-figjam-rebuild |
| **Successor** | None. The ranked changes feed a later sk-create-figjam revision |
| **Handoff Criteria** | research/research.md exists with at least 10 ranked changes and the operator has chosen which to apply |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:phase-context -->
## Phase Context

This is **Phase 16** of the Product Owner FigJam flow generation upgrade specification.

**Scope Boundary**: Research and synthesis only. No Product Owner source file changes.

**Dependencies**:
- sk-create-figjam as rebuilt in phase 015, the hub files at the repository root and the sk-product-owner surfaces that hand off to it.
- Public FigJam repos pinned under `research/corpus/`, which git ignores: the 009 corpus plus the repos found on 2026-10-20.

**Deliverables**:
- 10 DeepSeek iteration files and a deep-research state log under `research/lineages/deepseek/`.
- `research/research.md`, the synthesis written by a fresh Opus 5.5 high agent.

**Changelog**:
- When this phase closes, refresh the matching file in ../changelog/ using the parent packet number plus this phase folder name.
<!-- /ANCHOR:phase-context -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
Phase 015 grew sk-create-figjam to seven diagram types from the 009 corpus and sk-design-diagram. New public FigJam work has appeared since, Figma's own guide among it, and nobody has checked how the packet hands work to and from sk-product-owner, the hub router, the kernel and the Claude Project.

### Purpose
Produce evidence-cited findings and a ranked list of changes for sk-create-figjam and its integration with sk-product-owner.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- What the new corpus does that sk-create-figjam does not: types, rules, checks, layout, colour, extensions, read-back, quality measurement, failure handling and delivery.
- The integration: hub stage one, the FLOW routes in the Product Owner router and the kernel, the hand-back rules, the Project mirror, the plugin, the benchmarks and the playbooks.
- Repos found during the run with `gh search`, pinned the same way.

### Out of Scope
- Editing the packet, its mirror or the kernel. This phase proposes, a later change applies.
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
| REQ-001 | Run 10 deep-research iterations on DeepSeek V4.1 Flash at max through cli-pi and llmgateway, with convergence stopping disabled. |
| REQ-002 | Each iteration widens the corpus or deepens an earlier finding and cites files as [SOURCE: path:line]. |
| REQ-003 | A fresh Opus 5.5 high agent writes `research/research.md` after checking each cited line it uses. |
| REQ-004 | The synthesis ranks at least 10 changes, each naming the file it changes and the source it comes from, with at least 3 on the integration with sk-product-owner. |

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

- **SC-001**: 10 iteration records exist and none ends the run early.
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
| Risk | Third-party code enters the public repo | Med | `research/.gitignore` ignores `corpus/` |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:nfr -->
## L2: NON-FUNCTIONAL REQUIREMENTS

### Security
- **NFR-S01**: No secrets or tokens in research files or logs.
- **NFR-S02**: No Barter screenshot, flow or board URL enters a prompt or an output.

### Reliability
- **NFR-R01**: A failed iteration is rerun, never skipped, so the count stays at 10.
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
| Research | 16/20 | 10 iterations across the corpus and the integration |
| **Total** | **30/70** | **Level 2** |
<!-- /ANCHOR:complexity -->

---

<!-- ANCHOR:questions -->
## 10. OPEN QUESTIONS

- Which of the ranked changes should the next sk-create-figjam revision apply? The operator decides.
<!-- /ANCHOR:questions -->
