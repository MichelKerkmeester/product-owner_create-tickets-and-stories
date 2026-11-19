---
title: "Implementation Plan: Phase 9, template forms and checklists"
description: "The templates, rules and kernel move to H4 openings, a bold Expected outcomes label, About at H2 and `[]` checkboxes. Both format validators learn the new forms, and a script converts the 78 exports and 17 examples, proving each changed line is an allowed transform."
trigger_phrases:
  - "template forms plan"
  - "checklist bracket rollout"
importance_tier: "important"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: plan-core | v2.2 -->
# Implementation Plan: Phase 9, template forms and checklists

<!-- SPECKIT_LEVEL: 2 -->

---

<!-- ANCHOR:summary -->
## 1. SUMMARY

### Technical Context

| Aspect | Value |
|--------|-------|
| **Language/Stack** | Markdown rules and artifacts, JavaScript (format gate), Python (residency, transform) |
| **Framework** | Product Owner skill, Claude Project package, shared Sync Loop gates |
| **Storage** | None |
| **Testing** | Transform check, format gate fixtures, reference parity, residency, rule parity, playbook validator |

### Overview
The rules move first, then the gate learns to read `[]` and to block the retired forms. A scratch script converts the exports and examples against a snapshot and checks that every changed line is an allowed transform. Mirrors, the residency declaration and the playbook follow the rules. No scenario runs.
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
Rule first, gate second, then a mechanical conversion proved line by line

### Key Components
- **Transform script** (`scratch/transform.py`): converts a file and, with `--check`, compares the converted snapshot to the live file
- **Format gate**: one validator shared by four systems, and Product Owner's own copy, which must give identical output
- **Checkbox key** (`systems.cjs`): the `[ ]` rule blocks Product Owner artifacts only, never sources or other systems

### Data Flow
Snapshot to transform to check to gate. Skill source to mirror to residency declaration.
<!-- /ANCHOR:architecture -->

---

<!-- ANCHOR:affected-surfaces -->
## FIX ADDENDUM: AFFECTED SURFACES

Use this section when `research_intent=fix_bug`, when planning from a deep-review FAIL/CONDITIONAL verdict, or when any finding touches security, path handling, env precedence, schema boundaries, persistence, public responses, or shared policy.

| Surface | Current Role | Action | Verification |
|---------|--------------|--------|--------------|
| Shared `validate-output-format.cjs` | Gate for four systems | `[]` read everywhere, Requirements rule inverted, keyed `[ ]` rule | All four fixture suites |
| Product Owner `validate-output-format.cjs` | Twin of the shared gate | The same logic | `reference-parity.cjs`, `cmp` on fixtures |
| `systems.py` declared statements | Residency | Resynced to the new kernel and Doc Mode text | Residency on the commit |
| `carrier_query_evidence.py`, `residency/backlog.md` | Mirror file names | Repointed to the renamed mirrors | Repointer, residency |

Required inventories:
- Same-class producers: `rg -n '\[ \]' sk-product-owner/assets sk-product-owner/references` for every checkbox the rules write.
- Consumers of changed symbols: `rg -n 'markAsDone|CHECKBOX_ITEM|Checklist' validate-output-format.cjs run_fixtures.sh`.
- Matrix axes: checkbox form (`[]`, `[ ]`), marker (`- `, `*   `), section (inside or outside Requirements), system (Product Owner or another), target (artifact or source).
- Algorithm invariant: a converted line differs from its snapshot only by a heading level, a label form, a checkbox marker or the bracket space.
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
| Unit | Transform script, gate rules | `--check` with planted faults, fixture cases per rule |
| Integration | Gate, mirrors, residency, playbook | Four fixture suites, reference parity, residency, rule parity, playbook validator |
| Manual | Templates and examples | Read by hand after conversion |
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:dependencies -->
## 6. DEPENDENCIES

| Dependency | Type | Status | Impact if Blocked |
|------------|------|--------|-------------------|
| Phase 008 commits | Internal | Green | None, they are pushed |
| ClickUp rendering of `- []` | External | Unverified | The operator accepted the risk |
<!-- /ANCHOR:dependencies -->

---

<!-- ANCHOR:rollback -->
## 7. ROLLBACK PLAN

- **Trigger**: ClickUp renders `- []` as text, or a gate failure that cannot be repaired in scope
- **Procedure**: `git revert` the phase commits in both repos, or restore an export from `scratch/before/`
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
| Core Implementation | High | 3 to 4 hours |
| Verification | Med | 1 hour |
| **Total** | | **About 5 hours** |
<!-- /ANCHOR:effort -->

---

<!-- ANCHOR:enhanced-rollback -->
## L2: ENHANCED ROLLBACK

### Pre-deployment Checklist
- [x] Snapshot of the 78 exports and 21 examples in `scratch/before/`

### Rollback Procedure
1. `git revert` the phase commits in both repos
2. Rerun the format gate fixtures, parity and residency

### Data Reversal
- **Has data migrations?** No
- **Reversal procedure**: N/A
<!-- /ANCHOR:enhanced-rollback -->

---
