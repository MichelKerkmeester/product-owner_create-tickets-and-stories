---
title: "Feature Specification: Phase 40: FigJam Sonnet run findings"
description: "The graded Claude Sonnet 5.5 high run of all 54 FigJam scenarios closed at 23 PASS, 29 FAIL and 2 SKIP, and most failures traced to rules that contradicted each other, boards that lost meaning in greyscale and playbook lines that asked for the wrong thing. This phase fixes them as v1.0.6.0, mirrors them to the Project and reruns the 31 scenarios that did not pass."
trigger_phrases:
  - "figjam sonnet run findings"
  - "phase 40 figjam sonnet run findings"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.3 -->
# Feature Specification: Phase 40: FigJam Sonnet run findings

<!-- SPECKIT_LEVEL: 2 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 2 |
| **Priority** | P1 |
| **Status** | In Progress |
| **Created** | 2026-10-26 |
| **Branch** | `main` |
| **Parent Spec** | ../spec.md |
| **Phase** | 40 of 40 |
| **Predecessor** | 039-figjam-run-findings |
| **Successor** | None |
| **Handoff Criteria** | Every row in acceptance-criteria.md is Met |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:phase-context -->
## Phase Context

This is **Phase 40** of the Product Owner FigJam flow generation upgrade specification.

**Scope Boundary**: the findings of the graded Claude Sonnet 5.5 high run in `sk-create-figjam`, the Interactive Mode reference, the playbook, the Claude Project mirror and the run folder's driver and records, then a rerun of the 29 failed and 2 skipped scenarios. No Barter board is read or written.

**Dependencies**:
- The 54-scenario run in `benchmark/reports/2026-10-25--manual-testing-playbook--figjam-model-comparison/skill/sonnet-high/` and its grades.
- `sk-create-figjam` v1.0.5.0 as phase 039 left it.

**Deliverables**:
- The skill, design, playbook and driver fixes, released as hub and `sk-create-figjam` v1.0.6.0 and `sk-product-owner` v1.2.3.0.
- The hand-written Project mirror and kernel v1.2.7.
- The graded rerun, its renders and the refreshed screenshot gallery.

**Changelog**:
- When this phase closes, refresh the matching file in ../changelog/ using the parent packet number plus this phase folder name.
<!-- /ANCHOR:phase-context -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
Claude Sonnet 5.5 high ran all 54 FigJam scenarios on v1.0.5.0 and passed 23 once skeptics and an adjudicator had checked one grader's verdicts. Its 20 scored boards averaged 20.6 of 22, so most failures were not drawing faults: Flow Mode told the model to ask one question and to run rounds, to split an oversized board and to keep one board, and Quick energy could not reach the draw-ready threshold on a thin brief. Kinds that share a shape lost their meaning on a greyscale copy, and several playbook lines graded a signal the skill never sets.

### Purpose
Remove every contradiction and gap the run recorded, then prove the fixes by rerunning the 31 scenarios that did not pass on the same model.

### Decisions
- **D1**: No rerun starts before 23:00 Amsterdam time (22:00 UTC) on 2026-10-26, on the operator's word.
- **D2**: DeepSeek V4.1 Flash max on cli-pi through llmgateway makes the edits, Opus agents plan and verify them and GPT 6 Luna max fast on cli-codex is the only fallback.
- **D3**: One Opus grader scores every rerun board on one scale, then skeptics and adjudicators check each verdict.
- **D4**: Every skill change reaches its Project file in the same commit. The shared Human Voice card in `z — Knowledge` changes only on the operator's yes, because five systems hold a byte copy of it.
- **D5**: Reruns run in parallel lanes, each writing into its own FigJam file in drafts of the operator's team plan, and no board URL, file key, plan name or email reaches a committed file.
- **D6**: FJ-031 and FJ-032 stay runnable by the driver. Their operator setup steps are graded `harness` rather than skipped, because the rest of each scenario still measures the model.
- **D7**: A composite state section that outweighs the focus is fixed in planning, not in the composer, because the zone tints sit within 4 luma of each other and a section has one fill.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- Make the type question go alone, one board mean one board, Quick reach the playback and an accepted recommendation stay assumed.
- Give kinds that share a shape distinct outlines, a `Leads to` key entry, a focus reason and an arrival point of their own.
- Read a file the user named once before the gate and name any same-titled section there.
- Correct the playbook lines the run showed were wrong and add a `driver:` key for scenarios the driver cannot set up.
- Rerun the 31 scenarios that did not pass, render and grade every board and refresh the screenshot gallery.

### Out of Scope
- The Human Voice Core count wording - it lives in a card five systems share, so it waits for the operator's yes under D4.
- A router change for the composite state exit that crosses one edge - recorded as an open failure in the self-test instead.

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| sk-create-figjam/SKILL.md, references/, assets/ | Modify | Flow Mode, rubric, style guide, design, templates, examples and the seven type references |
| sk-create-figjam/assets/compose-board.js, scripts/ | Modify | Outlines, key entries, arrival points, gantt arrows, focus reason and their checks |
| sk-create-figjam/manual-testing-playbook/ | Modify | Scenario corrections and the `driver:` key |
| sk-product-owner/references/interactive-mode.md | Modify | A board command conflict asks about the artifact first |
| claude project/, SYNC.md, README.md, USER-GUIDE.md | Modify | Mirror, kernel v1.2.7 and release notes |
| benchmark/reports/2026-10-25--manual-testing-playbook--figjam-model-comparison/ | Modify, Create | Driver, grades, renders and README |
| changelog/, sk-create-figjam/changelog/, sk-product-owner/changelog/, version files | Create, Modify | v1.0.6.0 and v1.2.3.0 |
| sk-create-figjam/assets/screenshots/ | Modify | The best v1.0.6.0 board of each type |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | The composer self-test, the design check, the flow check self-test, pytest, the 15 repository gates and the output format gate all exit 0 on the committed tree. |
| REQ-002 | The Sync Loop parity and residency checks print PASSED after the last commit, and the Flow Board Composer Knowledge code block equals `compose_board.py --template`. |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement |
|----|-------------|
| REQ-003 | Flow Mode in the skill and the Project asks the type question alone, cuts one board rather than splitting it, reaches the playback under Quick and keeps an accepted recommendation assumed. |
| REQ-004 | The composer draws kinds that share a shape with distinct outlines, a `Leads to` key entry, a focus reason in the key and one arrival point per edge outside a join. |
| REQ-005 | Flow Mode reads a file the user named before the gate and names any same-titled section at the gate. |
| REQ-006 | The playbook grades only signals the skill sets, and the driver skips an `operator-only` scenario and runs a `new-file` scenario with no file pin. |
| REQ-007 | The 31 scenarios that did not pass run again on Claude Sonnet 5.5 high no earlier than 22:00 UTC, every board they write has a 100% render and each has one graded line. |
| REQ-008 | `sk-create-figjam` and the hub read 1.0.6.0 with changelogs, and the screenshot gallery holds the best v1.0.6.0 board of each of the seven types with a caption. |

> Acceptance criteria for these requirements live in `acceptance-criteria.md`,
> which is the document that decides whether this packet may close.
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: The rerun passes more of the 31 scenarios than the 0 of 31 they passed on v1.0.5.0, and every remaining failure is named with its cause in the run README.
- **SC-002**: `compose_board.py --self-test` and `flow_check.py --self-test` each run more checks than their v1.0.5.0 counts of 1,032 and 158, and all pass.
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Dependency | The operator's team plan drafts for the rerun files | High | Each lane writes into its own draft file, and lane 1 keeps the fictional test file the operator allowed |
| Risk | The whole composer the Project sends leaves about 2,470 characters for the model | Med | The largest shipped example model runs about 2,400 characters, and the Composer Knowledge file names the room |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:nfr -->
## L2: NON-FUNCTIONAL REQUIREMENTS

### Security
- **NFR-S01**: No board URL, Figma file key, plan name or email in any committed file. PO is a public repository.
<!-- /ANCHOR:nfr -->

---

<!-- ANCHOR:edge-cases -->
## L2: EDGE CASES

### Data Boundaries
- A gantt bar shorter than its arrows: the landing points space out to fit the bar.

### Error Scenarios
- An `operator-only` scenario: the driver prints a skipped row with its reason and exits 0.
<!-- /ANCHOR:edge-cases -->

---

<!-- ANCHOR:complexity -->
## L2: COMPLEXITY ASSESSMENT

| Dimension | Score | Notes |
|-----------|-------|-------|
| Scope | 18/25 | About 90 files across skill, mirror, playbook, driver and records |
| Risk | 10/25 | The composer every board write sends, and a live rerun |
| Research | 6/20 | The findings were graded and adjudicated before this phase |
| **Total** | **34/70** | **Level 2** |
<!-- /ANCHOR:complexity -->

---

<!-- ANCHOR:questions -->
## 10. OPEN QUESTIONS

- Should the shared Human Voice card name how a term kept with a reason counts on the self-scan line? It waits for the operator's yes under D4.
<!-- /ANCHOR:questions -->
