---
title: "Implementation Plan: Phase 13: skilled-hub-alignment"
description: "Moves the Product Owner hub into product-owner/ on the skilled parent-hub contract and repoints every reader of the moved paths."
trigger_phrases:
  - "skilled hub alignment plan"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: plan-core | v2.2 -->
# Implementation Plan: Phase 13: skilled-hub-alignment

<!-- SPECKIT_LEVEL: 2 -->

---

<!-- ANCHOR:summary -->
## 1. SUMMARY

### Technical Context

| Aspect | Value |
|--------|-------|
| **Language/Stack** | Markdown, JSON, Python 3.9, Node, Bash |
| **Framework** | The skilled parent-hub contract in sk-create-skill |
| **Storage** | None |
| **Testing** | parent-skill-check.cjs, validate_skill_package.py, run_gates.sh, the Sync Loop gates |

### Overview
The hub files and the four packets move into `product-owner/`, the registry and hub router take the canonical schema, and the packet routers fold into each packet's `SKILL.md` Section 2. Every gate, script and doc that names a moved path is repointed and rerun.
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
Skilled parent hub with nested packets, two-stage routing

### Key Components
- **Stage one**: `mode-registry.json` and `hub-router.json` pick the mode
- **Stage two**: the hub `ROUTER.md` maps the intent to packet leaves, and the packet's `SKILL.md` Section 2 routes inside the packet

### Data Flow
`AGENTS.md` loads the hub `SKILL.md`, then `ROUTER.md`, then the selected packet's `SKILL.md` and the leaves its intent names.
<!-- /ANCHOR:architecture -->

---

<!-- ANCHOR:affected-surfaces -->
## FIX ADDENDUM: AFFECTED SURFACES

Use this section when `research_intent=fix_bug`, when planning from a deep-review FAIL/CONDITIONAL verdict, or when any finding touches security, path handling, env precedence, schema boundaries, persistence, public responses, or shared policy.

| Surface | Current Role | Action | Verification |
|---------|--------------|--------|--------------|
| Hub files and packets | The skill itself | Moved into product-owner/ | parent-skill-check 0 failures |
| Gates, scripts, validators, docs, Sync Loop declaration | Read the moved paths | Updated | run_gates.sh, format gates, Sync Loop gates, link check |
| Kernel and Knowledge files | Project mirror | Unchanged | run_parity.sh 39 of 39 |

Required inventories:
- Same-class producers: `rg -n '<field|string|helper|literal|error-pattern>' <module-or-files>`.
- Consumers of changed symbols: `rg -n '<changedSymbol>|<changedConstant>|<changedPublicField>' . --glob '*.ts' --glob '*.js' --glob '*.md'`.
- Matrix axes: list every independent input axis and the required rows before implementation.
- Algorithm invariant: for path/redaction/parser/resolver/security fixes, state the invariant and adversarial cases.
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
| Unit | Hub check, vendor sync, plugin build | Self-tests |
| Integration | Routing and parity | run_gates.sh, differential.py, Sync Loop gates |
| Manual | Routing scenarios | Playbook validator |
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:dependencies -->
## 6. DEPENDENCIES

| Dependency | Type | Status | Impact if Blocked |
|------------|------|--------|-------------------|
| .skilled sk-create-skill contract | External | Green | No skilled gates could run |
<!-- /ANCHOR:dependencies -->

---

<!-- ANCHOR:rollback -->
## 7. ROLLBACK PLAN

- **Trigger**: A gate fails that cannot be repaired in scope
- **Procedure**: Nothing is committed, so `git restore` and removing `product-owner/` return the tree, and the scratchpad backups restore `systems.py` and `systems.cjs`
<!-- /ANCHOR:rollback -->

---


---

<!-- ANCHOR:phase-deps -->
## L2: PHASE DEPENDENCIES

```
Phase 1 (Setup) ──────┐
                      ├──► Phase 2 (Core) ──► Phase 3 (Verify)
Phase 1.5 (Config) ───┘
```

| Phase | Depends On | Blocks |
|-------|------------|--------|
| Setup | None | Core, Config |
| Config | Setup | Core |
| Core | Setup, Config | Verify |
| Verify | Core | None |
<!-- /ANCHOR:phase-deps -->

---

<!-- ANCHOR:effort -->
## L2: EFFORT ESTIMATION

| Phase | Complexity | Estimated Effort |
|-------|------------|------------------|
| Setup | Low | 1 hour |
| Core Implementation | High | 5 hours |
| Verification | Med | 2 hours |
| **Total** | | **8 hours** |
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
2. Restore the tracked files and remove `product-owner/`
3. Rerun run_gates.sh
4. Tell the operator

### Data Reversal
- **Has data migrations?** No
- **Reversal procedure**: N/A
<!-- /ANCHOR:enhanced-rollback -->

---

