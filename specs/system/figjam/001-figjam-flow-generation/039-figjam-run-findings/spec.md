---
title: "Feature Specification: Phase 39: FigJam run findings"
description: "The stopped Claude Opus 5.5 medium run of 24 FigJam scenarios found five skill gaps and three driver gaps. This phase fixes them: a named file as a target, a scratch clean-up step, stops that end their turn, a hygiene exemption for a widened section, a composer cut to the model's type and three driver fixes."
trigger_phrases:
  - "figjam run findings"
  - "phase 39 figjam run findings"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.3 -->
# Feature Specification: Phase 39: FigJam run findings

<!-- SPECKIT_LEVEL: 2 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 2 |
| **Priority** | P1 |
| **Status** | Complete |
| **Created** | 2026-10-26 |
| **Branch** | `main` |
| **Parent Spec** | ../spec.md |
| **Phase** | 39 of 39 |
| **Predecessor** | 038-figjam-model-comparison |
| **Successor** | None |
| **Handoff Criteria** | Every row in acceptance-criteria.md is Met |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:phase-context -->
## Phase Context

This is **Phase 39** of the Product Owner FigJam flow generation upgrade specification.

**Scope Boundary**: the five skill findings and the three driver findings of the stopped full run phase 038 recorded, in `sk-create-figjam`, its playbook, the Claude Project mirror and the run folder's driver. No new run and no Barter board.

**Dependencies**:
- The stopped full run in `benchmark/reports/2026-10-25--manual-testing-playbook--figjam-model-comparison/`, README section 8.3.
- The composer and its self-test as phase 038 left them.

**Deliverables**:
- The five skill fixes in `references/flow-mode.md`, the playbook, `assets/compose-board.js` and `scripts/compose_board.py`.
- The hand-written Project mirror of the fixes that apply inside a Project.
- The three driver fixes in `run/adaptive_compare.py`, `run/runtimes.py` and FJ-004.
- `sk-create-figjam` and the hub at v1.0.5.0.

**Changelog**:
- When this phase closes, refresh the matching file in ../changelog/ using the parent packet number plus this phase folder name.
<!-- /ANCHOR:phase-context -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
Claude Opus 5.5 medium drew 20 sound boards in 24 scenarios, but the skill got in its way five times. Flow Mode listed no existing file the user named as a target, left the scratch model and code behind, let a stop sit mid-turn, failed a board on a section its own extension widened and sent a composer so large that a graph model had about 2,850 characters of room. The driver also pushed six scenarios past the stop they grade, ran FJ-009 with the Figma server it must not have and FJ-004 printed a SKIP the run read as a gap.

### Purpose
Close every finding the run recorded, so the next run measures the model and not the skill's or the driver's gaps.

### Decisions
- **D1**: The hygiene finding is fixed in the playbook rule, not with a composer reserve. The composer cannot know how many notes an extension adds or how large they are, while `references/hybrid-workflow.md` already grows the section and returns its old size for the rollback.
- **D2**: The FJ-004 SKIP is fixed with a note, not by putting the Project mirror into the sandbox. The runner removes `claude project/` on purpose and its isolation proof fails a skill sandbox that holds it, and `benchmark/gates/run_gates.sh` already runs the same self-test with the mirror present.
- **D3**: The Project keeps the whole composer. It fills the code by hand and cannot cut it per type, so only the skill's `compose_board.py` sends a type-cut composer.
- **D4**: The clean-up step is not mirrored, because a Project writes no file.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- List an existing FigJam file the user named as a valid write target.
- Add a clean-up step that deletes the scratch folder before the reply.
- Make the playback and the gate each the last message of their turn.
- Exempt a section a gated extension widens from the hygiene rule.
- Cut the composer to the model's type before the model is filled.
- Stop the driver's follow-up yes on a scenario that grades an earlier stop, run FJ-009 without the hosted Figma server and explain the FJ-004 SKIP.

### Out of Scope
- A new run of any scenario - the operator stopped the full run and the remaining 30 scenarios wait for a separate decision.
- A Codex run of FJ-009 - Codex reaches Figma through the account's app, and no way to switch that off for one run has been tried.

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| sk-create-figjam/references/flow-mode.md | Modify | Target file rule, clean-up step, stops that end their turn |
| sk-create-figjam/assets/compose-board.js | Modify | Arrow primitives moved to Section 3 |
| sk-create-figjam/scripts/compose_board.py | Modify | `for_type`, per-type room in the design check and a self-test check |
| sk-create-figjam/manual-testing-playbook/ | Modify | Hygiene exemption and the FJ-004 sandbox note |
| claude project/knowledge/, SYNC.md | Modify | Flow Mode and composer mirror, maintenance note |
| benchmark/reports/2026-10-25--manual-testing-playbook--figjam-model-comparison/run/ | Modify | `adaptive_compare.py` and `runtimes.py` |
| changelog/, sk-create-figjam/changelog/, version files | Create, Modify | v1.0.5.0 |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | `compose_board.py` fills a model into a composer that holds its own type's builder and no other, and `--template` with no model still prints the whole composer. |
| REQ-002 | The composer self-test, the design check, the flow check self-test, pytest, the 15 repository gates and the output format gate all pass. |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement |
|----|-------------|
| REQ-003 | Flow Mode lists an existing FigJam file the user named as a target, in the skill and the Project mirror. |
| REQ-004 | Flow Mode deletes its scratch folder before the reply. |
| REQ-005 | The playback and the gate are each the last message of their turn, in the skill and the Project mirror. |
| REQ-006 | The playbook's hygiene rule exempts the section a gated extension widens. |
| REQ-007 | The driver sends a follow-up yes only to a scenario whose script answers the write gate, and runs a scenario that needs no hosted Figma server without it. |
| REQ-008 | FJ-004 says why a sandbox prints a SKIP line for each Project mirror. |

> Acceptance criteria for these requirements live in `acceptance-criteria.md`,
> which is the document that decides whether this packet may close.
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: `compose_board.py --design-check` reports more room for every type than the 2,850 characters of v1.0.4.0.
- **SC-002**: None of the eight findings in the Problem Statement is open, and the run README section 8.4 names where each was fixed.
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Dependency | The section heads in `assets/compose-board.js` | High | `for_type` cuts on `// N. TITLE` heads, and a self-test check fails when a cut call holds another type's builder or is not shorter |
| Risk | A primitive a cut type needs sits in a dropped section | High | The arrow primitives moved to Section 3, and the self-test composes every fixture through the cut composer |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:nfr -->
## L2: NON-FUNCTIONAL REQUIREMENTS

### Security
- **NFR-S01**: No board URL, Figma file key, plan name or email in any changed file. PO is a public repository.
<!-- /ANCHOR:nfr -->

---

<!-- ANCHOR:edge-cases -->
## L2: EDGE CASES

### Data Boundaries
- A model with no type: `compact_template` returns the whole composer.

### Error Scenarios
- A scenario that needs no hosted Figma server on a Codex runtime: the driver prints a skipped status and exits 0.
<!-- /ANCHOR:edge-cases -->

---

<!-- ANCHOR:complexity -->
## L2: COMPLEXITY ASSESSMENT

| Dimension | Score | Notes |
|-----------|-------|-------|
| Scope | 10/25 | About 15 files across skill, mirror and driver |
| Risk | 8/25 | The composer every board write sends |
| Research | 4/20 | The findings were already recorded |
| **Total** | **22/70** | **Level 2** |
<!-- /ANCHOR:complexity -->

---

<!-- ANCHOR:questions -->
## 10. OPEN QUESTIONS

- None. The operator chose all three groups of fixes and a new phase on 2026-10-26.
<!-- /ANCHOR:questions -->
