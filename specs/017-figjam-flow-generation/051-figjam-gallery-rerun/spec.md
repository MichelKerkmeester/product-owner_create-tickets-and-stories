---
title: "Feature Specification: Phase 51: FigJam gallery rerun on v1.0.16.0"
description: "The sk-create-figjam gallery images were drawn on older composers, from v1.0.6.0 to v1.0.15.0. This phase reruns the nine gallery scenarios and one new status lane scenario with Claude Sonnet 5.5 medium as the board maker on v1.0.16.0, grades every board and replaces an image only when the new board scores at least as high."
trigger_phrases:
  - "figjam gallery rerun"
  - "phase 51 figjam"
  - "sonnet medium figjam boards"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.3 -->
# Feature Specification: Phase 51: FigJam gallery rerun on v1.0.16.0

<!-- SPECKIT_LEVEL: 2 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 2 |
| **Priority** | P2 |
| **Status** | Complete |
| **Created** | 2026-10-29 |
| **Branch** | `main` |
| **Parent Spec** | ../spec.md |
| **Phase** | 51 of 52 |
| **Predecessor** | 050-figjam-spec-board-learnings |
| **Successor** | 052-figjam-boards-that-teach |
| **Handoff Criteria** | Every row in acceptance-criteria.md is Met |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:phase-context -->
## Phase Context

This is **Phase 51** of the Product Owner FigJam flow generation upgrade specification.

**Scope Boundary**: the FigJam model comparison run folder, the `sk-create-figjam` gallery and its two READMEs, and one new board-quality playbook scenario. The skill's behavior does not change.

**Dependencies**:
- `sk-create-figjam` v1.0.16.0 as phase 050 left it.
- The hosted Figma MCP, a draft file per run in the operator's team plan and the Claude Code backend of the run driver.

**Deliverables**:
- Ten graded runs with Claude Sonnet 5.5 medium as the board maker.
- A gallery where each image is the higher-scoring of its old and new board.
- One new scenario, FJ-049, for a laned process with a status lane and detail cards.

**Changelog**:
- When this phase closes, refresh the matching file in ../changelog/ using the parent packet number plus this phase folder name.
<!-- /ANCHOR:phase-context -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement

Each gallery image shows the composer of the run it came from, from v1.0.6.0 to v1.0.15.0. Since then the design changed: body text sizes, the line-height of cards, the reading-order rules and, in v1.0.16.0, the status lane and detail cards. The status lane image comes from a release check, not a graded run.

### Purpose

Show what the current skill draws, from graded runs, on one model the operator chose.

### Decisions

- **D1**: Claude Sonnet 5.5 medium makes every board, through the driver's `claude:claude-sonnet-5-5:medium` backend. The operator chose it on 2026-10-29.
- **D2**: The nine gallery scenarios run, FJ-022 to FJ-028, FJ-032 and FJ-036, plus a new FJ-049 for the status lane board.
- **D3**: Grading is the last reruns' method: two fresh readers per board, `run/composition_check.py` and one Claude Sonnet 5.5 high grader on the 22-point scorecard.
- **D4**: A new board replaces its image only when it scores at least as high as the image's own board. A tie goes to the new board, because it shows the current design.
- **D5**: One push of both repositories after the gallery lands, which also carries the two unpushed phase 050 gallery commits.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- Ten runs, one at a time, each in a new draft file, FJ-032 on a prepared board that already holds content.
- The new FJ-049 scenario and its root playbook entry.
- Grades, renders, reader notes and a new report section in the run folder.
- Gallery images and captions that the grades support.

### Out of Scope
- Fixing the skill from what the runs find. Findings are recorded for a later phase.
- The Claude Project, which carries no images.

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| benchmark/reports/2026-10-25--manual-testing-playbook--figjam-model-comparison/ | Modify | Run records, renders, grades and report section 8.16 |
| sk-create-figjam/manual-testing-playbook/board-quality/status-lane-board-quality.md | Create | FJ-049 |
| sk-create-figjam/manual-testing-playbook/manual-testing-playbook.md | Modify | Lists FJ-049 |
| sk-create-figjam/assets/screenshots/ | Modify | Images the grades support |
| sk-create-figjam/README.md, sk-create-figjam/assets/screenshots/README.md | Modify | Captions |
| leaf-manifest.json | Modify | The new scenario and images |
| mcp-figma/, mcp-click-up/, mcp-code-mode/, vendor.json | Modify | Pulled from upstream to clear the vendor gate another session's commits had turned red |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-001 | Every run's board maker is Claude Sonnet 5.5 medium | Each run's meta.json names `claude:claude-sonnet-5-5:medium` |
| REQ-002 | No board URL, file key, plan name or email in a committed file | The redaction pass and a scan print nothing |
| REQ-003 | The gates pass on the committed tree | `run_gates.sh` passes 15 of 15 |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-004 | Every board is graded | Each run has two reader notes and a scorecard row |
| REQ-005 | Each image is the higher-scoring board | Every caption names its run, model, version and score |
| REQ-006 | FJ-049 is a scenario a grader can score | It has a prompt, expected signals and pass criteria, and the playbook root lists it |
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: The gallery shows ten boards, each from a graded run on the current or a higher-scoring earlier composer.
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Risk | Medium effort draws worse boards than high | Med | D4 keeps the old image when the new board scores lower |
| Risk | A reply carries a board URL or file key | High | Each scenario's output is redacted as it finishes |
| Dependency | The Figma MCP and the operator's plan | High | The batch resumes where it stopped |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:nfr -->
## L2: NON-FUNCTIONAL REQUIREMENTS

### Security
- **NFR-S01**: Product Owner is a public repository, so no board URL, Figma file key, plan name or email is committed.
<!-- /ANCHOR:nfr -->

---

<!-- ANCHOR:edge-cases -->
## L2: EDGE CASES

### Data Boundaries
- A scenario whose run fails on its reply but draws a higher-scoring board: the board may still take the image, and the caption says why the run failed.

### Error Scenarios
- A run that writes no board: it is recorded and rerun once.
<!-- /ANCHOR:edge-cases -->

---

<!-- ANCHOR:complexity -->
## L2: COMPLEXITY ASSESSMENT

| Dimension | Score | Notes |
|-----------|-------|-------|
| Scope | 12/25 | Ten runs, one new scenario and the gallery |
| Risk | 6/25 | No skill code changes |
| Research | 6/20 | Grading and the judge rule |
| **Total** | **24/70** | **Level 2** |
<!-- /ANCHOR:complexity -->

---

<!-- ANCHOR:questions -->
## 10. OPEN QUESTIONS

- None.
<!-- /ANCHOR:questions -->
