---
title: "Implementation Plan: Phase 15: figjam-rebuild"
description: "Grows sk-create-figjam to every FigJam diagram type with references, templates, examples, a per-type check, a playbook and the Claude Project mirror."
trigger_phrases:
  - "figjam rebuild plan"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: plan-core | v2.2 -->
# Implementation Plan: Phase 15: figjam-rebuild

<!-- SPECKIT_LEVEL: 2 -->

---

<!-- ANCHOR:summary -->
## 1. SUMMARY

### Technical Context

| Aspect | Value |
|--------|-------|
| **Language/Stack** | Markdown, Mermaid, Python 3.9, Node, Bash |
| **Framework** | The skilled parent-hub contract and the SYNC.md parity method |
| **Storage** | None |
| **Testing** | flow_check.py self-test, run_gates.sh, the skilled checkers, the playbook validators, the Sync Loop gates |

### Overview
The check came first, so every reference, template and example was written against rules a script enforces. Then the packet's routing, the hub and the playbook followed, and a transform script wrote the Project mirrors from the sources.
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
One workflow, a type choice inside it, and one rule module per type

### Key Components
- **`references/flow-mode.md`**: the workflow, the type choice, intake, shared rules, write routes, read-back and delivery
- **`references/types/`**: one reference per type
- **`scripts/flow_check.py` with `scripts/figjam_checks/`**: dispatch by header and `%% type:` line, one module per type, planted fixtures

### Data Flow
`SKILL.md` Section 2 loads the Flow pair, then the type's reference and template, the quality rubric before the gate, the style guide when colour is set and the hybrid workflow when the gate names an extension.
<!-- /ANCHOR:architecture -->

---

<!-- ANCHOR:affected-surfaces -->
## FIX ADDENDUM: AFFECTED SURFACES

| Surface | Current Role | Action | Verification |
|---------|--------------|--------|--------------|
| sk-create-figjam packet | Draws FigJam diagrams | Rebuilt | Self-test, skilled checkers |
| Hub routing | Picks the packet | Keywords, gold rows, a scenario | check_hub.py, topology gate |
| PO router, kernel router | Route Flow requests | FLOW patterns widened | 125 fixtures, 204 differential inputs |
| Project mirror | Flow Mode in a Project | 23 new files, 2 rewritten, kernel rows | Sync Loop parity and residency |

Required inventories:
- Same-class producers: every copy of the FLOW pattern, found by grep in the kernel, `router-contract.md` and `route_contract.py`
- Consumers of changed paths: rule_parity.py phrases, playbook line citations, the two format gate perimeters and the example lint self-test tree
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
| Unit | Every rule of every type | flow_check.py --self-test |
| Integration | Routing, parity and the format perimeter | run_gates.sh, differential.py, the Sync Loop gates |
| Manual | Type choice, refusals and board writes | The packet playbook |
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:dependencies -->
## 6. DEPENDENCIES

| Dependency | Type | Status | Impact if Blocked |
|------------|------|--------|-------------------|
| Hosted Figma MCP | External | Not connected | Board-write scenarios record SKIP |
<!-- /ANCHOR:dependencies -->

---

<!-- ANCHOR:rollback -->
## 7. ROLLBACK PLAN

- **Trigger**: A gate fails that cannot be repaired in scope
- **Procedure**: Nothing is committed, so the working tree changes can be reverted file by file, and the scratchpad holds the pre-resync `systems.py` and the pre-edit kernel
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
| Setup | Med | 2 hours |
| Core Implementation | High | 8 hours |
| Verification | Med | 2 hours |
| **Total** | | **12 hours** |
<!-- /ANCHOR:effort -->

---

<!-- ANCHOR:enhanced-rollback -->
## L2: ENHANCED ROLLBACK

### Pre-deployment Checklist
- [x] Backup created: the pre-resync systems.py and the pre-edit kernel in the session scratchpad
- [x] Feature flag: not applicable, a skill packet has no flag
- [x] Monitoring: not applicable, the gates are the check

### Rollback Procedure
1. Stop before any commit
2. Restore the edited files and delete the new ones
3. Rerun run_gates.sh
4. Tell the operator

### Data Reversal
- **Has data migrations?** No
- **Reversal procedure**: N/A
<!-- /ANCHOR:enhanced-rollback -->
