---
title: "Implementation Plan: Phase 2: Input to model logic research"
description: "Stage the run outside Product Owner, run five DeepSeek iterations, merge, have a DeepSeek worker write a checked synthesis and copy it in."
trigger_phrases:
  - "input to model logic research plan"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: plan-core | v2.2 -->
# Implementation Plan: Phase 2: Input to model logic research

<!-- SPECKIT_LEVEL: 2 -->

---

<!-- ANCHOR:summary -->
## 1. SUMMARY

### Technical Context

| Aspect | Value |
|--------|-------|
| **Language/Stack** | Markdown, JSONL |
| **Framework** | The deep-research fan-out runner |
| **Storage** | The spec folder |
| **Testing** | State-log counts, SOURCE tag counts, orchestrator spot-checks |

### Overview
`fanout-run.cjs` runs one DeepSeek lineage of 5 iterations in a staging folder in the outer repository, with the stop policy at max-iterations and convergence off. `fanout-merge.cjs` merges it, a DeepSeek worker writes the synthesis, and the research folder is copied here.
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
- [x] Gates passing
- [x] Docs updated (spec, plan, tasks)
<!-- /ANCHOR:quality-gates -->

---

<!-- ANCHOR:architecture -->
## 3. ARCHITECTURE

### Pattern
Fan-out lineage, merge, checked synthesis

### Key Components
- **The topic**: the question, the sources and the writing rules
- **The synthesis worker**: a read-only DeepSeek worker that opens each cited line it keeps

### Data Flow
The topic goes to the runner, the iterations write to the lineage, the merge builds the registry and the synthesis reads all of it.
<!-- /ANCHOR:architecture -->

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
| Unit | The state log | A count of iteration records |
| Integration | The citations | A count of SOURCE tags per iteration |
| Manual | The synthesis | Orchestrator spot-checks of cited lines |
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:dependencies -->
## 6. DEPENDENCIES

| Dependency | Type | Status | Impact if Blocked |
|------------|------|--------|-------------------|
| DeepSeek V4.1 Flash through llmgateway | External | Used on 2026-10-21 | The run stalls |
<!-- /ANCHOR:dependencies -->

---

<!-- ANCHOR:rollback -->
## 7. ROLLBACK PLAN

- **Trigger**: A run that cannot finish
- **Procedure**: Delete the staging folder and this phase's research folder
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
| Setup | Low | 10 minutes |
| Core Implementation | Med | 20 minutes |
| Verification | Med | 30 minutes |
| **Total** | | **1 hour** |
<!-- /ANCHOR:effort -->

---

<!-- ANCHOR:enhanced-rollback -->
## L2: ENHANCED ROLLBACK

### Pre-deployment Checklist
- [x] Backup created: not needed, no source file changes
- [x] Feature flag: not applicable
- [x] Monitoring: the progress monitor

### Rollback Procedure
1. Stop the runner
2. Delete the staging folder
3. Delete research/ here
4. Tell the operator

### Data Reversal
- **Has data migrations?** No
- **Reversal procedure**: N/A
<!-- /ANCHOR:enhanced-rollback -->
