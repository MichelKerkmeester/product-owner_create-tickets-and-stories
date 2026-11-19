---
title: "Implementation Plan: Phase 6, concise writing"
description: "Add length caps to the Product Owner writing rules on both sides, report over-cap lines as a gate warning, and rewrite the 98 kept exports and the report to the caps by hand. A verify script proves each rewrite kept its facts. No scenario runs."
trigger_phrases:
  - "concise writing plan"
  - "length caps rollout"
  - "export rewrite verification"
  - "phase 6 plan"
importance_tier: "important"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: plan-core | v2.2 -->
# Implementation Plan: Phase 6, concise writing

<!-- SPECKIT_LEVEL: 2 -->

---

<!-- ANCHOR:summary -->
## 1. SUMMARY

### Technical Context

| Aspect | Value |
|--------|-------|
| **Language/Stack** | Markdown rules, Node (format gate), Python (collector, verify script) |
| **Framework** | Product Owner skill and Claude Project package |
| **Storage** | None |
| **Testing** | Format gate, Sync Loop fixtures, playbook validator, run selftest, parity, residency |

### Overview
Add length caps to the Product Owner writing rules on both sides, report over-cap lines as a gate warning, and rewrite the 98 kept exports and the report to the caps by hand. A verify script proves each rewrite kept its facts. No scenario runs.
<!-- /ANCHOR:summary -->

---

<!-- ANCHOR:quality-gates -->
## 2. QUALITY GATES

### Definition of Ready
- [ ] Problem statement clear and scope documented
- [ ] Success criteria measurable
- [ ] Dependencies identified

### Definition of Done
- [ ] All acceptance criteria met
- [ ] Tests passing (if applicable)
- [ ] Docs updated (spec/plan/tasks)
<!-- /ANCHOR:quality-gates -->

---

<!-- ANCHOR:architecture -->
## 3. ARCHITECTURE

### Pattern
Skill source first, Project mirror by hand, gate as a warning

### Key Components
- **Entry points**: `SKILL.md` and the kernel state the caps, since the Conciseness card is shared with three other systems
- **Format gate check**: reports over-cap artifact lines, never blocks
- **Verify script**: compares each rewritten export with its graded original

### Data Flow
Rule text to runtime. Graded export to rewrite to verify script to commit.
<!-- /ANCHOR:architecture -->

---

<!-- ANCHOR:affected-surfaces -->
## FIX ADDENDUM: AFFECTED SURFACES

Use this section when `research_intent=fix_bug`, when planning from a deep-review FAIL/CONDITIONAL verdict, or when any finding touches security, path handling, env precedence, schema boundaries, persistence, public responses, or shared policy.

| Surface | Current Role | Action | Verification |
|---------|--------------|--------|--------------|
| `validate-output-format.cjs` | Format gate for every system | Update, product-owner only | Fixtures and a full gate run |
| `run/collect_exports.py` | Copies deliverables into `export/benchmark` | Update | Selftest and a dry run |

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
| Unit | Length-cap check | Sync Loop fixtures |
| Integration | Rules and mirrors | Format gate, parity, residency, playbook validator |
| Manual | 98 rewritten exports | Verify script, sampled reads |
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:dependencies -->
## 6. DEPENDENCIES

| Dependency | Type | Status | Impact if Blocked |
|------------|------|--------|-------------------|
| Phase 005 report | Internal | Green | None, it is committed |
<!-- /ANCHOR:dependencies -->

---

<!-- ANCHOR:rollback -->
## 7. ROLLBACK PLAN

- **Trigger**: a verify or gate failure that cannot be fixed in scope
- **Procedure**: `git revert` the phase commits in both repos
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
| Setup | Low | 15 minutes |
| Core Implementation | Med | 2 hours, rewrites in parallel |
| Verification | Med | 30 minutes |
| **Total** | | **About 3 hours** |
<!-- /ANCHOR:effort -->

---

<!-- ANCHOR:enhanced-rollback -->
## L2: ENHANCED ROLLBACK

### Pre-deployment Checklist
- [ ] Graded originals reachable in git history

### Rollback Procedure
1. `git revert` the phase commits in both repos
2. Rerun the format gate, parity and residency

### Data Reversal
- **Has data migrations?** No
- **Reversal procedure**: N/A
<!-- /ANCHOR:enhanced-rollback -->

---

