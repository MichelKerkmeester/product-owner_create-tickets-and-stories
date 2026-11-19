---
title: "Feature Specification: Phase 6, concise writing"
description: "Length caps for Product Owner artifacts, the benchmark exports and report rewritten to them by hand, and no rerun."
trigger_phrases:
  - "concise writing caps"
  - "hand-edited benchmark exports"
  - "length cap gate warning"
  - "phase 6 concise writing"
importance_tier: "important"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.2 -->
# Feature Specification: Phase 6, concise writing

<!-- SPECKIT_LEVEL: 2 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 2 |
| **Priority** | P1 |
| **Status** | Complete |
| **Created** | 2026-09-26 |
| **Branch** | `scaffold/006-concise-writing` |
| **Parent Spec** | ../spec.md |
| **Phase** | 6 of 6 |
| **Predecessor** | 005-grading-and-report |
| **Successor** | None |
| **Handoff Criteria** | Rules, gate, playbook, exports and report committed, gates green |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:phase-context -->
## Phase Context

This is **Phase 6** of packet 076. It follows the graded Opus 5.5 run and its three remeasure rounds.

**Scope Boundary**: writing rules, one gate warning, one playbook row, the 98 kept exports and the report prose. No scenario runs.

**Dependencies**:
- Phase 005 closed, its report committed

**Deliverables**:
- Caps in both packagings, a gate warning, an Advisory playbook row
- 98 exports and the report rewritten to the caps
- The 102 deleted round exports committed as removed

**Changelog**:
- When this phase closes, refresh the matching file in ../changelog/ using the parent packet number plus this phase folder name.
<!-- /ANCHOR:phase-context -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
The benchmark exports read bloated: 109 bullets run over 30 words and 81 paragraphs over 60. The rules never define "short", so no runtime has a cap to meet.

### Purpose
Every artifact meets one set of length caps, and the kept benchmark shows it.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- Caps: a bullet is one sentence of 25 words or fewer, a paragraph at most 3 sentences and 60 words, an opening at most 2 paragraphs
- The caps in `SKILL.md` and the kernel, a gate warning and an Advisory playbook row
- The 98 exports and the report rewritten by hand, labelled as edited after grading
- The collector made safe for edited exports, and the round deletion committed

### Out of Scope
- A playbook rerun - the operator chose none
- History purge - the operator chose to commit the deletion only
- Verdict changes - the graded originals stand

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| `sk-product-owner/references/conciseness.md`, `SKILL.md` | Modify | The caps |
| `claude project/Custom Instructions.md` | Modify | The caps, kernel v0.18.0 |
| `z — Claude Project Sync Loop/validate-output-format.cjs`, `systems.cjs`, fixtures | Modify | Length-cap warning |
| Playbook root | Modify | Advisory row |
| `export/benchmark/**` | Modify, Delete | Rewrite 98, remove 102 |
| Run folder `README.md`, `results.md`, grading-notes review sections, `run/collect_exports.py` | Modify | Report prose, collector guard |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | The caps appear in `SKILL.md` and the kernel, and the shared Conciseness card stays unchanged |
| REQ-002 | Every rewritten export keeps its headings, backticked values and numbers, adds no fact and meets the caps |
| REQ-003 | The README says the exports were edited after grading and where the graded originals are |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement |
|----|-------------|
| REQ-004 | The format gate reports over-cap lines in artifacts without blocking |
| REQ-005 | The collector never overwrites an edited export and collects rounds only on request |
| REQ-006 | The report prose meets the caps with every count unchanged |

> Acceptance criteria for these requirements live in `acceptance-criteria.md`,
> which is the document that decides whether this packet may close.
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: Over-cap bullets and paragraphs in the 98 exports drop from 109 and 81 to 0
- **SC-002**: Format gate, fixtures, validator, selftest, parity, residency and `validate.sh` pass
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Risk | A rewrite drops or changes a fact | High | Verify script compares headings, backticked spans and numbers per file |
| Risk | Exports no longer match the graded text | Med | README label, originals in git history and `replies/` |
| Risk | A later collector run undoes the edits | Med | Skip differing targets unless `--force` |
<!-- /ANCHOR:risks -->

---


---

<!-- ANCHOR:nfr -->
## L2: NON-FUNCTIONAL REQUIREMENTS

### Performance
- **NFR-P01**: The gate warning adds no noticeable time to a system run

### Security
- **NFR-S01**: No credentials or raw streams committed

### Reliability
- **NFR-R01**: The warning never blocks an artifact
<!-- /ANCHOR:nfr -->

---

<!-- ANCHOR:edge-cases -->
## L2: EDGE CASES

### Data Boundaries
- Code, tables, quoted source copy and Given/When/Then lines are exempt from the caps
- A cap that cannot be met without losing a fact keeps the fact and splits the line

### Error Scenarios
- A rewrite that fails verification goes back once, then to the orchestrator

### State Transitions
- Partial rewrite: unverified files stay at their graded text
<!-- /ANCHOR:edge-cases -->

---

<!-- ANCHOR:complexity -->
## L2: COMPLEXITY ASSESSMENT

| Dimension | Score | Notes |
|-----------|-------|-------|
| Scope | 16/25 | About 110 files, two repos |
| Risk | 10/25 | Fact loss in rewrites |
| Research | 4/20 | Measured already |
| **Total** | **30/70** | **Level 2** |
<!-- /ANCHOR:complexity -->

---

<!-- ANCHOR:questions -->
## 10. OPEN QUESTIONS

- None. The operator settled scope, strength, deletion and spec folder on 2026-09-26
<!-- /ANCHOR:questions -->

---


