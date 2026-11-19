---
title: "Implementation Plan: Deal Templates upgrades for Product Owner"
description: "Describe the reply once in an always-loaded asset section, point every surface at it, fix the Doc examples, add an example lint and one gate runner, and widen the em-dash grant to Catalog entry headings in both validator twins."
trigger_phrases:
  - "deal templates upgrades plan"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: plan-core | v2.2 -->
# Implementation Plan: Deal Templates upgrades for Product Owner

<!-- SPECKIT_LEVEL: 2 -->

---

<!-- ANCHOR:summary -->
## 1. SUMMARY

### Technical Context

| Aspect | Value |
|--------|-------|
| **Language/Stack** | Markdown, Python 3, Node.js, Bash |
| **Framework** | Product Owner skill and Claude Project packaging |
| **Storage** | None |
| **Testing** | Router and format fixtures, rule parity, example lint and its self-test, reference parity, playbook validator, residency |

### Overview
The reply shape lands once, in Interactive Response Templates Section 3, which every mode already loads. Every other surface swaps its own reply description for a pointer, each edit kept on its own line so no cited line moves. The Doc examples are fixed, then a lint runs every example through the validator and reads every worked reply, and one runner calls every gate.
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
- **Reply shape**: Interactive Response Templates Section 3, always loaded
- **Validator twins**: the system validator and the shared Sync Loop validator, held equal by reference parity
- **Example lint**: validator over every example and mirror, plus a line reader for worked replies
- **Gate runner**: one command over every system gate

### Data Flow
A surface describes nothing about the reply and points at Section 3. The lint reads Section 3's worked replies and every example, and the runner reports every gate with a failure count as its exit code.
<!-- /ANCHOR:architecture -->

---

<!-- ANCHOR:affected-surfaces -->
## FIX ADDENDUM: AFFECTED SURFACES

| Surface | Current Role | Action | Verification |
|---------|--------------|--------|--------------|
| Reply description in four files | Each described the reply its own way | Point at Section 3 | grep, example lint |
| Doc examples | Model the house format | Remove em dashes and semicolons | Example lint 42 files |
| Validator twins | Shared format gate | Catalog grant | Fixtures, reference parity, four systems' fixtures |
| Kernel statements | Declared in `systems.py` | Resync pairs handed over | Simulation resolves every pair |
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
| Unit | Validator grant, router | `benchmark/format/run_fixtures.sh`, `benchmark/router/run_fixtures.sh` |
| Integration | All gates, twins, playbook | `run_gates.sh`, `reference-parity.cjs`, playbook validator, `residency_check.py` |
| Manual | Cited line numbers, residual wording | Line-count asserts, grep sweep |
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:dependencies -->
## 6. DEPENDENCIES

| Dependency | Type | Status | Impact if Blocked |
|------------|------|--------|-------------------|
| `systems.py` resync | Internal | Yellow | Residency stays red until the handed-over pairs land |
| Shared Human Voice card | Internal | Yellow | Card and Doc Mode disagree on the Catalog grant until the owner edits it |
<!-- /ANCHOR:dependencies -->

---

<!-- ANCHOR:rollback -->
## 7. ROLLBACK PLAN

- **Trigger**: A gate regression the change cannot fix
- **Procedure**: Restore the changed paths from HEAD in both repos and delete the new files; nothing is committed
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
| Core Implementation | Med | 3 hours |
| Verification | Med | 1 hour |
| **Total** | | **About 4.5 hours** |
<!-- /ANCHOR:effort -->

---

<!-- ANCHOR:enhanced-rollback -->
## L2: ENHANCED ROLLBACK

### Pre-deployment Checklist
- [x] Backup created (if data changes): N/A, git holds every original
- [x] Feature flag configured: N/A
- [x] Monitoring alerts set: N/A

### Rollback Procedure
1. Restore the changed paths from HEAD in the nested and the Barter repo
2. Delete the lint, runner, fixtures and changelog this packet created
3. Rerun the format fixtures and reference parity

### Data Reversal
- **Has data migrations?** No
- **Reversal procedure**: N/A
<!-- /ANCHOR:enhanced-rollback -->

---
