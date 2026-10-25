---
title: "Implementation Plan: Phase 36: figjam-design-system"
description: "Runs a three-lineage deep-research fan-out on sk-create-figjam design quality and a user-editable design spec file, merges the lineages and writes the synthesis."
trigger_phrases:
  - "figjam design system plan"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: plan-core | v2.2 -->
# Implementation Plan: Phase 36: figjam-design-system

<!-- SPECKIT_LEVEL: 2 -->

---

<!-- ANCHOR:summary -->
## 1. SUMMARY

### Technical Context

| Aspect | Value |
|--------|-------|
| **Language/Stack** | Markdown, JSONL, Node, Bash |
| **Framework** | The system-deep-loop research workflow, `fanout-run.cjs` and `fanout-merge.cjs` |
| **Storage** | research/, made by the workflow |
| **Testing** | Iteration counts in each state log, SOURCE tag counts, screenshot names, the synthesis checks, validate.sh --strict |

### Overview
The deep-research workflow runs a fan-out with one lineage per executor and convergence stopping off, so every iteration runs. claude-opus-5-5 at medium effort through cli-claude-code runs 3 iterations, swe-2-max through cli-devin runs 2 and gpt-6-luna at max effort on the fast service tier through cli-codex runs 2. The merge consolidates the lineages and a fresh Opus 5.5 medium agent writes `research/research.md`. The run is staged at `specs/z-staging-po-036-research` in the outer repository, as 016 was, then the research folder is copied here, staging paths in the markdown are repointed and the staging folder is deleted.
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
Three detached CLI lineages, a merge and the workflow's synthesis

### Key Components
- **`fanout-run.cjs`**: runs each lineage under `research/lineages/`
- **`fanout-merge.cjs`**: merges the lineage registries into one findings registry
- **The synthesis step**: opens every cited line it uses and writes `research/research.md`

### Data Flow
The topic names the sk-create-figjam inputs, the nine screenshots and the design spec question. Each iteration writes an iteration file and a state record, the merge reads them, and the synthesis reads the iterations, the registry and the cited lines.
<!-- /ANCHOR:architecture -->

---

<!-- ANCHOR:affected-surfaces -->
## FIX ADDENDUM: AFFECTED SURFACES

| Surface | Current Role | Action | Verification |
|---------|--------------|--------|--------------|
| sk-create-figjam packet | Composes FigJam boards | Read only | git status |
| Project mirror and kernel | Carry the packet to claude.ai | Not read or changed | git status |

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
| Unit | Each iteration record | The state logs and a SOURCE tag count per iteration file |
| Integration | The merge and the synthesis | fanout-merge.cjs exit status, the synthesis corrections list |
| Manual | Three cited claims | The orchestrator opens the cited lines and screenshots |
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:dependencies -->
## 6. DEPENDENCIES

| Dependency | Type | Status | Impact if Blocked |
|------------|------|--------|-------------------|
| cli-claude-code with claude-opus-5-5 | External | Available | The lineage is rerun |
| cli-devin with swe-2-max | External | Available | The lineage is rerun |
| cli-codex with gpt-6-luna | External | Available | The lineage is rerun |
<!-- /ANCHOR:dependencies -->

---

<!-- ANCHOR:rollback -->
## 7. ROLLBACK PLAN

- **Trigger**: The run produces nothing usable
- **Procedure**: Delete `research/`, nothing outside it is written
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
| Setup | Low | 20 minutes |
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
- [x] Monitoring: the state logs and the fan-out output

### Rollback Procedure
1. Stop the lineages
2. Delete this phase's `research/`
3. Tell the operator

### Data Reversal
- **Has data migrations?** No
- **Reversal procedure**: N/A
<!-- /ANCHOR:enhanced-rollback -->
