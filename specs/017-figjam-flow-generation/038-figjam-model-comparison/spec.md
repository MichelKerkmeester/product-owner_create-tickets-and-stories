---
title: "Feature Specification: Phase 38: FigJam model comparison"
description: "The seven board-quality scenarios run on DeepSeek V4.1 Flash max, SWE 2 Max and GLM 5.3 Flash max against the composer phase 037 shipped, each board graded on the 22-point scorecard, so the best board per diagram type becomes the gallery and the run says which model draws FigJam boards best."
trigger_phrases:
  - "figjam model comparison"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.2 -->
# Feature Specification: Phase 38: FigJam model comparison

<!-- SPECKIT_LEVEL: 2 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 2 |
| **Priority** | P1 |
| **Status** | In Progress |
| **Created** | 2026-10-25 |
| **Branch** | `main` |
| **Parent Spec** | ../spec.md |
| **Phase** | 38 of 38 |
| **Predecessor** | 037-figjam-design-spec |
| **Successor** | None |
| **Handoff Criteria** | Every row in acceptance-criteria.md is Met, waived or superseded by a decision record |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:phase-context -->
## Phase Context

This is **Phase 38** of the Product Owner FigJam flow generation upgrade specification.

**Scope Boundary**: a benchmark run folder under `benchmark/reports/`, the gallery in `sk-create-figjam/assets/screenshots/` and the captions that describe it. No skill behaviour changes. No Barter board.

**Dependencies**:
- The composer and design file phase 037 shipped.
- The board-quality scenarios FJ-022 to FJ-028 and the 22-point scorecard in the root playbook Section 3.
- Figma's hosted MCP server, signed in on the Devin CLI, and the one fictional test FigJam file the operator cleared.

**Deliverables**:
- A run folder with every reply, tool call, render and grade of 21 scenario runs.
- A per-type and per-model result table that says which model draws boards best.
- The gallery's seven type images replaced by the best board of each type, with honest captions.

**Changelog**:
- When this phase closes, refresh the matching file in ../changelog/ using the parent packet number plus this phase folder name.
<!-- /ANCHOR:phase-context -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
The gallery shows boards the composer drew before phase 037, so it no longer shows what the skill draws. The operator also wants to know whether DeepSeek V4.1 Flash max, SWE 2 Max or GLM 5.3 Flash max drives the skill to the best FigJam boards.

### Purpose
Run every diagram type on all three models under one operator script, grade each board the same way and keep the best board of each type as the gallery.

### Decisions
The full records are in `decision-record.md`.

- **D1 (ADR-001)**: All three models run through the Devin CLI at their max variants. The operator asked for Devin first, and llmgateway refuses `max` for GLM 5.3 Flash.
- **D2 (ADR-002)**: One adaptive operator drives every run: the scripted turns in order, the recommended-answers turn after an intake round and "Yes, go ahead." after a stop that still has no board, each extra turn recorded as supplementary.
- **D3 (ADR-003)**: Fresh Sonnet 5.5 graders score the boards, never one of the three models under test, and a fresh reader answers each board's questions from its colour screenshots alone.
- **D4 (ADR-004)**: The best board per type is the highest scorecard total, then a pass over a fail, then fewer supplementary turns.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- One adaptive driver over the Devin runner, with the intake classifier the 035 run used.
- FJ-022 user flow, FJ-023 process, FJ-024 architecture, FJ-025 sequence, FJ-026 state, FJ-027 ER and FJ-028 gantt, each on all three models, one run at a time on the fictional test file.
- Overview, 100% and greyscale renders of every written board.
- A fresh reader per model and one grader per type on the 22-point scorecard.
- The gallery's seven type images, its README and the root README captions.
- Redaction of every board URL, the file key, plan names and emails before any commit.

### Out of Scope
- Any change to the skill's behaviour, references or Project mirror. A finding that needs one is recorded for a later phase.
- The two harder gallery boards, `state-on-existing-board.png` and `dense-flow-board.png`, which come from scenarios this run does not repeat.
- Any Barter board, board URL or Figma file key in a tracked file.

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| benchmark/reports/2026-10-25--manual-testing-playbook--figjam-model-comparison/ | Create | The run folder: driver, evidence, renders list, grades and README |
| sk-create-figjam/assets/screenshots/ | Modify | The seven type images and the gallery README |
| README.md, sk-create-figjam/README.md | Modify | Gallery captions where they name a score or a source |
| benchmark/reports/README.md | Modify | The new run's row |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | All 21 runs, seven scenarios on each of three models, run one at a time on the fictional test file under one driver, and each run's replies, tool calls and `meta.json` land in the run folder. |
| REQ-002 | Every written board is rendered at overview, 100% and greyscale and graded on the 22-point scorecard by a grader that is none of the three models, with Clarity from a fresh reader. |
| REQ-003 | No board URL, Figma file key, plan name or email reaches a tracked file. |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement |
|----|-------------|
| REQ-004 | The gallery's seven type images are the best board of each type under D4, and every caption names the scenario, the model and the score it came from. |
| REQ-005 | The run's README states which model draws boards best, per type and overall, with the losses that decided it. |

> Acceptance criteria for these requirements live in `acceptance-criteria.md`,
> which is the document that decides whether this packet may close.
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: A reader of the run's README can tell which model to use for FigJam boards and why.
- **SC-002**: Every image in the gallery is a board the current composer drew, with the score it earned.
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Dependency | Figma sign-in on Devin | High | A whoami probe on each model before the batch |
| Risk | SWE 2 Max rate limits | Med | The Devin runner waits out the reset time Devin names |
| Risk | A model stops before it writes | Med | The driver's follow-up turns, recorded as supplementary |
| Risk | Boards land beside each other and move | Low | One run at a time |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:nfr -->
## L2: NON-FUNCTIONAL REQUIREMENTS

### Security
- **NFR-S01**: No secrets, board URLs, Figma file keys, plan names or Barter flows in any changed file. PO is a public repository.

### Reliability
- **NFR-R01**: Each scenario runs in a fresh sandbox that cannot read the repository, the playbooks or another scenario's files.
<!-- /ANCHOR:nfr -->

---

<!-- ANCHOR:edge-cases -->
## L2: EDGE CASES

### Error Scenarios
- A run fails on transport: it reruns once and the result names the retry.
- A model never writes a board: it scores 0 for that type and the README says where it stopped.

### State Transitions
- Partial completion: resume from the first scenario with no `meta.json` in the run folder.
<!-- /ANCHOR:edge-cases -->

---

<!-- ANCHOR:complexity -->
## L2: COMPLEXITY ASSESSMENT

| Dimension | Score | Notes |
|-----------|-------|-------|
| Scope | 10/25 | A run folder and the gallery |
| Risk | 8/25 | Live Figma writes on one fictional file |
| Research | 10/20 | Grading 21 boards |
| **Total** | **28/70** | **Level 2** |
<!-- /ANCHOR:complexity -->

---

<!-- ANCHOR:questions -->
## 10. OPEN QUESTIONS

- None. The operator chose seven types on each model and a new phase on 2026-10-25.
<!-- /ANCHOR:questions -->
