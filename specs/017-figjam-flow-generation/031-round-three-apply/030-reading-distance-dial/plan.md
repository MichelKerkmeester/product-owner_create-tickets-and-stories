---
title: "Implementation Plan: Phase 30: Add reading distance as the third dial"
description: "A DeepSeek worker proposes exact edits for this change, the orchestrator applies and checks them, and the gates run on the final tree."
trigger_phrases:
  - "reading distance dial plan"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: plan-core | v2.2 -->
# Implementation Plan: Phase 30: Add reading distance as the third dial

<!-- SPECKIT_LEVEL: 2 -->

---

<!-- ANCHOR:summary -->
## 1. SUMMARY

### Technical Context

| Aspect | Value |
|--------|-------|
| **Language/Stack** | Markdown, Python 3.9, JSON |
| **Framework** | The skilled parent-hub contract and the SYNC.md parity method |
| **Storage** | None |
| **Testing** | run_gates.sh, the format gates, the playbook validators, the Sync Loop gates |

### Overview
A read-only DeepSeek V4.1 Flash worker on cli-pi read the files and returned exact edits as JSON. The orchestrator applied them in order, regenerated the Flow mirrors, and ran every gate on the final tree.
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
Proposal by a read-only worker, application by the orchestrator

### Key Components
- **The worker brief**: the ranked change, its files and the writing rules
- **The applier**: refuses an edit whose old text is missing or not unique

### Data Flow
The brief goes to the worker, the worker returns edits, the applier writes them, and the gates read the result.
<!-- /ANCHOR:architecture -->

---

<!-- ANCHOR:affected-surfaces -->
## FIX ADDENDUM: AFFECTED SURFACES

| Surface | Current Role | Action | Verification |
|---------|--------------|--------|--------------|
| `sk-create-figjam/references/flow-mode.md` Section 4 and the budget sections of `sk-create-figjam/references/types/*.md` | The rule this change amends | Updated | The gates named in tasks.md |

Required inventories:
- Same-class producers: every copy of the changed sentence, found by grep in the sources, the Knowledge mirrors and the kernel
- Consumers of changed paths: playbook line citations and the Sync Loop declared statements
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
| Unit | The changed rule | flow_check.py self-test or the router fixtures where they apply |
| Integration | Mirrors and routing | run_gates.sh, the Sync Loop gates |
| Manual | The changed text | A read of the final diff |
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:dependencies -->
## 6. DEPENDENCIES

| Dependency | Type | Status | Impact if Blocked |
|------------|------|--------|-------------------|
| DeepSeek V4.1 Flash through llmgateway | External | Canary passed | The orchestrator writes the edit by hand |
<!-- /ANCHOR:dependencies -->

---

<!-- ANCHOR:rollback -->
## 7. ROLLBACK PLAN

- **Trigger**: A gate fails that cannot be repaired in scope
- **Procedure**: Restore the changed files from the pre-change snapshot in the session scratchpad
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
| Core Implementation | Low | 20 minutes |
| Verification | Med | 30 minutes |
| **Total** | | **1 hour** |
<!-- /ANCHOR:effort -->

---

<!-- ANCHOR:enhanced-rollback -->
## L2: ENHANCED ROLLBACK

### Pre-deployment Checklist
- [x] Backup created: the pre-change snapshot in the session scratchpad
- [x] Feature flag: not applicable
- [x] Monitoring: the gates

### Rollback Procedure
1. Stop before any commit
2. Restore the changed files from the snapshot
3. Rerun run_gates.sh
4. Tell the operator

### Data Reversal
- **Has data migrations?** No
- **Reversal procedure**: N/A
<!-- /ANCHOR:enhanced-rollback -->
