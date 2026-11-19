---
title: "Implementation Plan: Phase 14: hub-to-root"
description: "Moves the Product Owner hub from product-owner/ back to the repository root, declares the repository entries through repo-root-hub and repoints every reader."
trigger_phrases:
  - "hub to root plan"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: plan-core | v2.2 -->
# Implementation Plan: Phase 14: hub-to-root

<!-- SPECKIT_LEVEL: 2 -->

---

<!-- ANCHOR:summary -->
## 1. SUMMARY

### Technical Context

| Aspect | Value |
|--------|-------|
| **Language/Stack** | Markdown, JSON, Python 3.9, Node, Bash |
| **Framework** | The skilled parent-hub contract with the repo-root-hub extension |
| **Storage** | None |
| **Testing** | parent-skill-check.cjs, validate_skill_package.py, run_gates.sh, the Sync Loop gates |

### Overview
A script recomputes every markdown link from its old and new location and strips the `product-owner/` prefix from lines this work added, then moves the files. The registry declares the repository entries, and each gate, script and doc is pointed at the root by hand.
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
- [x] Tests passing
- [x] Docs updated (spec, plan, tasks)
<!-- /ANCHOR:quality-gates -->

---

<!-- ANCHOR:architecture -->
## 3. ARCHITECTURE

### Pattern
Skilled parent hub at a repository root

### Key Components
- **`repo-root-hub` in `mode-registry.json`**: the repository's own entries, which the checkers skip
- **`scripts/build-plugin.py`**: copies the hub files, `AGENTS.md` and the registry's packets into `skills/product-owner/`

### Data Flow
`AGENTS.md` loads the root `SKILL.md`, then `ROUTER.md`, then the selected packet's `SKILL.md` and the leaves its intent names.
<!-- /ANCHOR:architecture -->

---

<!-- ANCHOR:affected-surfaces -->
## FIX ADDENDUM: AFFECTED SURFACES

| Surface | Current Role | Action | Verification |
|---------|--------------|--------|--------------|
| Hub files and packets | The skill itself | Moved to the root | parent-skill-check 0 failures |
| Gates, scripts, validators, docs, Sync Loop declaration | Read the hub paths | Updated | run_gates.sh, format gates, Sync Loop gates, link check |
| Kernel and Knowledge files | Project mirror | Unchanged | run_parity.sh 39 of 39 |

Required inventories:
- Same-class producers: a grep for `product-owner/` over the repository outside `specs/`
- Consumers of changed paths: every gate in `run_gates.sh`, the plugin build and the outer `systems.py` and `systems.cjs`
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
| Unit | Hub check, plugin build | Self-tests |
| Integration | Routing and parity | run_gates.sh, differential.py, Sync Loop gates |
| Manual | Routing scenarios | Playbook validator |
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:dependencies -->
## 6. DEPENDENCIES

| Dependency | Type | Status | Impact if Blocked |
|------------|------|--------|-------------------|
| repo-root-hub in the skilled checkers | External | Green | The root hub would fail 2a and 6a |
<!-- /ANCHOR:dependencies -->

---

<!-- ANCHOR:rollback -->
## 7. ROLLBACK PLAN

- **Trigger**: A gate fails that cannot be repaired in scope
- **Procedure**: Nothing is committed, so the move can be reversed with the same script run the other way, and the scratchpad backups restore `systems.py` and `systems.cjs`
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
| Core Implementation | Med | 2 hours |
| Verification | Med | 1 hour |
| **Total** | | **3.5 hours** |
<!-- /ANCHOR:effort -->

---

<!-- ANCHOR:enhanced-rollback -->
## L2: ENHANCED ROLLBACK

### Pre-deployment Checklist
- [x] Backup created: systems.py and systems.cjs copies in the session scratchpad
- [x] Feature flag: not applicable, a file move has no flag
- [x] Monitoring: not applicable, the gates are the check

### Rollback Procedure
1. Stop before any commit
2. Move the hub files back into `product-owner/` and drop the extension
3. Rerun run_gates.sh
4. Tell the operator

### Data Reversal
- **Has data migrations?** No
- **Reversal procedure**: N/A
<!-- /ANCHOR:enhanced-rollback -->
