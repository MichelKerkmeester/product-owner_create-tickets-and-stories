---
title: "Implementation Plan: Phase 8, cut the exports and set a word budget"
description: "Seven writers cut the 78 exports about 30% against a snapshot, a script and fact reviewers check what survived, and the cut counts set a per-artifact word budget on both entry-point lines and the playbook's Size band row. No scenario runs."
trigger_phrases:
  - "cut exports plan"
  - "word budget rollout"
importance_tier: "important"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: plan-core | v2.2 -->
# Implementation Plan: Phase 8, cut the exports and set a word budget

<!-- SPECKIT_LEVEL: 2 -->

---

<!-- ANCHOR:summary -->
## 1. SUMMARY

### Technical Context

| Aspect | Value |
|--------|-------|
| **Language/Stack** | Markdown rules and exports, Python (verify script) |
| **Framework** | Product Owner skill and Claude Project package |
| **Storage** | None |
| **Testing** | Verify script, fact reviews, format gate, playbook validator, parity, residency |

### Overview
Seven writers cut the 78 exports about 30% against a snapshot. A script and fact reviewers check what survived. The cut counts then set a per-artifact word budget on both entry-point lines and the playbook's Size band row. No scenario runs.
<!-- /ANCHOR:summary -->

---

<!-- ANCHOR:quality-gates -->
## 2. QUALITY GATES

### Definition of Ready
- [x] Problem statement clear and scope documented
- [x] Success criteria measurable
- [x] Dependencies identified

### Definition of Done
- [ ] All acceptance criteria met
- [ ] Tests passing (if applicable)
- [ ] Docs updated (spec/plan/tasks)
<!-- /ANCHOR:quality-gates -->

---

<!-- ANCHOR:architecture -->
## 3. ARCHITECTURE

### Pattern
Measured edit first, then a rule set from the measurement

### Key Components
- **Verify script** (`scratch/verify_cut.py`): holds structure, values and caps, and reports the cut per file
- **Fact reviewers**: read each file against `scratch/before-cut/` for losses no script can see
- **Entry points**: `SKILL.md` line 276 and kernel line 90 carry the budget, as they carry the caps

### Data Flow
Snapshot to cut to script to fact review to repair. Cut counts per artifact kind to budget to rules.
<!-- /ANCHOR:architecture -->

---

<!-- ANCHOR:affected-surfaces -->
## FIX ADDENDUM: AFFECTED SURFACES

Use this section when `research_intent=fix_bug`, when planning from a deep-review FAIL/CONDITIONAL verdict, or when any finding touches security, path handling, env precedence, schema boundaries, persistence, public responses, or shared policy.

| Surface | Current Role | Action | Verification |
|---------|--------------|--------|--------------|
| `SKILL.md` line 276, kernel line 90 | State the caps | Update, same sentence both sides | Format gate, parity |
| Playbook Size band row | Advisory grading | Update, never a failure | Playbook validator |
| `run/collect_exports.py` | Edit guard | Unchanged, keeps the cut files | Dry run |

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
| Unit | The verify script | Identity run, three planted faults |
| Integration | Rules and mirrors | Format gate, parity, residency, playbook validator |
| Manual | 78 cut exports | Fact reviewers, sampled reads |
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:dependencies -->
## 6. DEPENDENCIES

| Dependency | Type | Status | Impact if Blocked |
|------------|------|--------|-------------------|
| Phase 007 commits | Internal | Green | None, they are pushed |
<!-- /ANCHOR:dependencies -->

---

<!-- ANCHOR:rollback -->
## 7. ROLLBACK PLAN

- **Trigger**: a lost fact or a gate failure that cannot be repaired in scope
- **Procedure**: `git revert` the phase commits in both repos, or restore a file from `scratch/before-cut/`
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
| Setup | Low | 20 minutes |
| Core Implementation | Med | 1 to 2 hours, writers in parallel |
| Verification | Med | 1 hour, fact reviews in parallel |
| **Total** | | **About 3 hours** |
<!-- /ANCHOR:effort -->

---

<!-- ANCHOR:enhanced-rollback -->
## L2: ENHANCED ROLLBACK

### Pre-deployment Checklist
- [x] Snapshot of all 78 files in `scratch/before-cut/`

### Rollback Procedure
1. `git revert` the phase commits in both repos
2. Rerun the format gate, parity and residency

### Data Reversal
- **Has data migrations?** No
- **Reversal procedure**: N/A
<!-- /ANCHOR:enhanced-rollback -->

---
