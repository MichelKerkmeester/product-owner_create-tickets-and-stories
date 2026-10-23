---
title: "Implementation Plan: Phase 16: figjam-improvement-research"
description: "Pins the 009 corpus and the FigJam repos found on 2026-10-20, runs one 10-iteration DeepSeek lineage through fanout-run.cjs and has a fresh Opus 5.5 high agent write the synthesis."
trigger_phrases:
  - "figjam improvement research plan"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: plan-core | v2.2 -->
# Implementation Plan: Phase 16: figjam-improvement-research

<!-- SPECKIT_LEVEL: 2 -->

---

<!-- ANCHOR:summary -->
## 1. SUMMARY

### Technical Context

| Aspect | Value |
|--------|-------|
| **Language/Stack** | Markdown, JSONL, Node, Bash |
| **Framework** | The system-deep-loop research workflow, `fanout-run.cjs` and `fanout-merge.cjs` |
| **Storage** | research/, with the corpus git-ignored |
| **Testing** | Iteration counts in the state log, SOURCE tag counts, the synthesis writer's line checks, validate.sh --strict |

### Overview
The run is staged at `specs/z-staging-po-016-research` in the outer repository, as 009 was, because the runner refuses symlinked spec paths and running inside Product Owner loads its persona. One cli-pi lineage runs 10 iterations with the stop policy at max-iterations and convergence off, the merge consolidates its findings, and a fresh Opus 5.5 high agent writes `research/research.md`. The research folder is then copied here and the staging folder deleted.
<!-- /ANCHOR:summary -->

---

<!-- ANCHOR:quality-gates -->
## 2. QUALITY GATES

### Definition of Ready
- [x] Problem statement clear and scope documented
- [x] Success criteria measurable
- [x] Dependencies identified

### Definition of Done
- [x] All acceptance criteria met
- [x] validate.sh --strict passes
- [x] Docs updated (spec, plan, tasks)
<!-- /ANCHOR:quality-gates -->

---

<!-- ANCHOR:architecture -->
## 3. ARCHITECTURE

### Pattern
One detached CLI lineage, a merge and a separate synthesis writer

### Key Components
- **`fanout-run.cjs`**: runs the DeepSeek lineage under `research/lineages/deepseek/`
- **`fanout-merge.cjs`**: merges the lineage registry into `research/findings-registry.json`
- **The synthesis agent**: opens every cited line it uses and writes `research/research.md`

### Data Flow
The topic names the packet sources, the integration surfaces and the corpus. Each iteration writes an iteration file and a state record, the merge reads them, and the synthesis reads the iterations, the registry and the cited lines.
<!-- /ANCHOR:architecture -->

---

<!-- ANCHOR:affected-surfaces -->
## FIX ADDENDUM: AFFECTED SURFACES

| Surface | Current Role | Action | Verification |
|---------|--------------|--------|--------------|
| sk-create-figjam packet | Draws FigJam diagrams | Read only | git status |
| Hub, sk-product-owner, kernel, Project mirror | Route and hand off Flow work | Read only | git status |

Required inventories:
- Same-class producers: not applicable, nothing is changed
- Consumers of changed paths: not applicable, nothing is changed
<!-- /ANCHOR:affected-surfaces -->

---

<!-- ANCHOR:phases -->
## 4. IMPLEMENTATION PHASES

Follow the ordered tasks in `tasks.md`. It owns the Setup, Implementation and Verification phase checkboxes and task state.
<!-- /ANCHOR:phases -->

---

<!-- ANCHOR:testing -->
## 5. TESTING STRATEGY

| Test Type | Scope | Tools |
|-----------|-------|-------|
| Unit | Each iteration record | The state log and a SOURCE tag count per iteration file |
| Integration | The merge and the synthesis | fanout-merge.cjs exit status, the writer's corrections list |
| Manual | Three cited claims | The orchestrator opens the cited lines |
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:dependencies -->
## 6. DEPENDENCIES

| Dependency | Type | Status | Impact if Blocked |
|------------|------|--------|-------------------|
| DeepSeek V4.1 Flash through llmgateway | External | Used in 009 | Fallback per parent D4 |
| gh CLI | External | Signed in | No new repos found |
<!-- /ANCHOR:dependencies -->

---

<!-- ANCHOR:rollback -->
## 7. ROLLBACK PLAN

- **Trigger**: The run produces nothing usable
- **Procedure**: Delete the staging folder and `research/`, nothing outside them is written
<!-- /ANCHOR:rollback -->

---

<!-- ANCHOR:phase-deps -->
## L2: PHASE DEPENDENCIES

| Phase | Depends On | Blocks |
|-------|------------|--------|
| Setup | None | Core |
| Core | Setup | Verify |
| Verify | Core | None |
<!-- /ANCHOR:phase-deps -->

---

<!-- ANCHOR:effort -->
## L2: EFFORT ESTIMATION

| Phase | Complexity | Estimated Effort |
|-------|------------|------------------|
| Setup | Low | 30 minutes |
| Core Implementation | Med | 1 hour of run time |
| Verification | Med | 1 hour |
| **Total** | | **2.5 hours** |
<!-- /ANCHOR:effort -->

---

<!-- ANCHOR:enhanced-rollback -->
## L2: ENHANCED ROLLBACK

### Pre-deployment Checklist
- [x] Backup created: not needed, no existing file is changed
- [x] Feature flag: not applicable
- [x] Monitoring: the state log and the fan-out output

### Rollback Procedure
1. Stop the lineage
2. Delete the staging folder and this phase's `research/`
3. Tell the operator

### Data Reversal
- **Has data migrations?** No
- **Reversal procedure**: N/A
<!-- /ANCHOR:enhanced-rollback -->
