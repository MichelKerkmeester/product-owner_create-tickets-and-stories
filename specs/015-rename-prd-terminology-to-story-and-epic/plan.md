---
title: "Implementation Plan: Rename leftover PRD terminology to Story and Epic across the Product Owner skill, Claude Project, router benchmark and Sync Loop declaration"
description: "Classify every PRD mention as artifact name, input wording or history, then rename the artifact names with exact phrase pairs applied to the skill source and its Project mirror together, rename the examples and router key, and resync the Sync Loop declaration."
trigger_phrases:
  - "rename prd terminology to story and epic plan"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: plan-core | v2.2 -->
# Implementation Plan: Rename leftover PRD terminology to Story and Epic across the Product Owner skill, Claude Project, router benchmark and Sync Loop declaration

<!-- SPECKIT_LEVEL: 2 -->

---

<!-- ANCHOR:summary -->
## 1. SUMMARY

### Technical Context

| Aspect | Value |
|--------|-------|
| **Language/Stack** | Markdown, JSON, Python 3 |
| **Framework** | Product Owner skill and Claude Project packaging |
| **Storage** | None |
| **Testing** | Router fixtures and differential, format fixtures, reference parity, Sync Loop residency and parity |

### Overview
Each PRD mention is sorted into artifact name, input wording or history. Artifact names change through exact phrase pairs applied to the skill source and its Project mirror in one pass, with a hit count per pair, so a mirror cannot drift from its source. The router key, the example files and the declaration follow, then every gate runs against a HEAD baseline.
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
- [x] Tests passing (if applicable)
- [x] Docs updated (spec/plan/tasks)
<!-- /ANCHOR:quality-gates -->

---

<!-- ANCHOR:architecture -->
## 3. ARCHITECTURE

### Pattern
Source first, mirror by hand, per the manual parity method in `SYNC.md`.

### Key Components
- **Skill source**: `sk-product-owner/`, the behavioural source of truth
- **Project mirror**: `claude project/`, the kernel and knowledge written from the source
- **Router copies**: the fenced contract, the kernel JSON copy and `route_contract.py`, held equal by the differential
- **Declaration**: `systems.py`, pair paths and verbatim kernel statements

### Data Flow
A skill edit lands, its mirror takes the same phrase, the router differential compares the three router copies, and residency compares declared statements with the kernel.
<!-- /ANCHOR:architecture -->

---

<!-- ANCHOR:affected-surfaces -->
## FIX ADDENDUM: AFFECTED SURFACES

| Surface | Current Role | Action | Verification |
|---------|--------------|--------|--------------|
| Story Mode template and complete example | Produce the value line | Update label | grep for `**PRD:**` outside history returns nothing |
| Router topic key | Names the Story topic | Rename in all copies | Router differential 189/189 |
| `systems.py` statements | Quote kernel text | Resync | Residency equals baseline |
| Parity drift check | Dates each pair | Follows renames | `prove_rename_drift.py` 4/4, fails 3/4 without the fix |
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
| Unit | Router routing and copy parity | `benchmark/router/run_fixtures.sh` |
| Integration | Format validators and Sync Loop gates | `run_fixtures.sh`, `reference-parity.cjs`, `residency_check.py`, `validate_parity.py` |
| Manual | Residual PRD mentions | grep with per-line classification |
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:dependencies -->
## 6. DEPENDENCIES

| Dependency | Type | Status | Impact if Blocked |
|------------|------|--------|-------------------|
| Sync Loop gate tooling | Internal | Green | Declaration could not be verified |
| Operator decision on rename drift | Internal | Green | Resolved: rename-aware gate |
<!-- /ANCHOR:dependencies -->

---

<!-- ANCHOR:rollback -->
## 7. ROLLBACK PLAN

- **Trigger**: A gate regression the rename cannot fix
- **Procedure**: `git checkout` the changed paths in both repos and `git mv` the five examples back, nothing is committed yet
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
| Setup | Low | 15 minutes |
| Core Implementation | Med | 1 hour |
| Verification | Med | 30 minutes |
| **Total** | | **About 2 hours** |
<!-- /ANCHOR:effort -->

---

<!-- ANCHOR:enhanced-rollback -->
## L2: ENHANCED ROLLBACK

### Pre-deployment Checklist
- [x] Backup created (if data changes): `systems.py` copied to the scratchpad before the resync
- [x] Feature flag configured: N/A
- [x] Monitoring alerts set: N/A

### Rollback Procedure
1. Restore the changed paths from HEAD in the nested and the Barter repo
2. Move the five examples back to their `prd-example-` names
3. Rerun the router and format fixtures

### Data Reversal
- **Has data migrations?** No
- **Reversal procedure**: N/A
<!-- /ANCHOR:enhanced-rollback -->

---
