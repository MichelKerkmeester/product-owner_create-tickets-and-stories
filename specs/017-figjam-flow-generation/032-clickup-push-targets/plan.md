---
title: "Implementation Plan: Phase 32: Local ClickUp push targets with a private doc option"
description: "The orchestrator writes the edits directly and the gates run on the final tree."
trigger_phrases:
  - "clickup push targets plan"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: plan-core | v2.2 -->
# Implementation Plan: Phase 32: Local ClickUp push targets with a private doc option

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
The orchestrator writes the edits directly, mirrors the reply templates and the kernel by the SYNC.md parity method, resyncs any declared statement the kernel edit moves and runs every gate on the final tree.
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
A local destination lookup in front of the existing ClickUp approval

### Key Components
- **The lookup**: shell `CLICKUP_*` variables first, then the gitignored `.env` at the repository root
- **The offer**: names the target for the artifact kind and adds a private doc, or asks where with a private doc recommended

### Data Flow
The artifact is saved and read back, the lookup finds the link for its kind, the closing line offers that target or asks where, and only an explicit yes pushes.
<!-- /ANCHOR:architecture -->

---

<!-- ANCHOR:affected-surfaces -->
## FIX ADDENDUM: AFFECTED SURFACES

| Surface | Current Role | Action | Verification |
|---------|--------------|--------|--------------|
| `.gitignore`, a new `.env.example`, `AGENTS.md` ClickUp Handoff, `sk-product-owner/SKILL.md`, `sk-product-owner/assets/interactive-response-templates.md` and its Knowledge mirror, the kernel's ClickUp offer and the sk-product-owner playbook | The rule this change amends | Updated | The gates named in tasks.md |

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
| The ClickUp MCP `clickup_create_document` visibility field | External | Documented | The private doc option is dropped |
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
