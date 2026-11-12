---
title: "Feature Specification: Design copy pointer requirements"
description: "A Story for a new screen listed every badge, heading and button label as its own requirement, because the rules counted copy a design shows as a supplied value. The rules now point at the design instead."
trigger_phrases:
  - "design copy pointer requirements"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.4 -->
# Feature Specification: Design copy pointer requirements

<!-- SPECKIT_LEVEL: 1 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 1 |
| **Priority** | P1 |
| **Status** | Complete |
| **Created** | 2026-11-12 |
| **Branch** | `main` |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
A Story for the new App Select screen wrote nine Requirements items, seven of them one quoted string each: the badge, the heading, the subheading, both option titles and their lines. Michel confirmed the copy came from a design. Story Mode asked for this: it said the verbatim rule binds copy the source shows as much as copy it types, and that a screen's group holds as many items as the screen has supplied values. The list duplicates the design and goes stale when the design changes.

### Purpose
A new screen or component supplied as a design gets one Requirements item pointing at that design plus the rules a design cannot show, in the skill and in the Claude Project.
<!-- /ANCHOR:problem -->

<!-- ANCHOR:measured-behavior -->
### Measured Behavior
```text
$ for f in sk-product-owner/references/story-mode.md sk-product-owner/assets/story-template.md; do echo "HEAD $f: $(git show HEAD:$f | rg -c 'binds copy the source shows as much as copy it types|shows only in a screenshot, supplies its copy')"; done
HEAD sk-product-owner/references/story-mode.md: 1
HEAD sk-product-owner/assets/story-template.md: 1
```
<!-- /ANCHOR:measured-behavior -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- Narrow Story Mode's verbatim rule to strings the source types and shown strings that are themselves the change
- Add the design pointer rule for a new screen or component supplied as a Figma frame, a design link or a screenshot
- Stop the per-screen item count from counting a designed screen's visible strings
- Strike, in the Story template, an item that only quotes a string a design already shows
- Carry the same sentences into the two Claude Project knowledge mirrors and release the change as patch steps

### Out of Scope
- The Project kernel - it says an item carries its supplied value verbatim and leaves what counts as supplied to Story Mode, so it stays at v1.2.21
- The quality-scoring line on supplied hard values and the moved statement in `task-mode.md` on screenshot copy - both are declared residency statements, and a rewrite needs a resync of the shared Sync Loop declaration in the parent repository
- A playbook scenario for a designed screen - the fixtures hold text only, so it needs an image fixture first
- Task Mode - its verbatim rule covers typed values only

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| `sk-product-owner/references/story-mode.md` | Modify | Narrowed verbatim rule, new design pointer rule, item count |
| `sk-product-owner/assets/story-template.md` | Modify | Strike rule for quoted design strings, design pointer note |
| `claude project/knowledge/Product Owner - Templates - Story Mode.md` | Modify | Mirror of the Story Mode sentences |
| `claude project/knowledge/Product Owner - Assets - Story Template.md` | Modify | Mirror of the template sentences |
| `SKILL.md`, `hub-router.json`, `mode-registry.json`, `description.json`, `README.md`, `claude project/README.md`, `sk-product-owner/SKILL.md`, `sk-product-owner/README.md` | Modify | Hub v1.0.34.0 and `sk-product-owner` v1.2.19.0 |
| `changelog/v1.0.34.0.md`, `sk-product-owner/changelog/v1.2.19.0.md` | Create | Release notes |
| `SYNC.md` | Modify | Dated parity note |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-001 | Story Mode and the Story template no longer tell the writer to quote every string a design shows | `rg -c 'binds copy the source shows as much as copy it types\|shows only in a screenshot, supplies its copy'` prints no count for either source file |
| REQ-002 | Both sources state the design pointer rule | `rg -c 'Never write one item per visible string'` prints 1 for each source file |
| REQ-003 | Typed values still travel verbatim | `rg -c 'Supplied hard values travel into Requirements verbatim' sk-product-owner/references/story-mode.md` prints 1 |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-004 | The two Project mirrors carry the same sentences as their sources | `diff` of the changed lines between each source and its mirror prints nothing |
| REQ-005 | The gates hold | `bash benchmark/gates/run_gates.sh` prints `all 19 gates pass` and `bash benchmark/parity/run_residency.sh` prints `PASSED` |
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: The old sentence count is 0 and the new rule count is 1 in each of the two source files and the two mirrors
- **SC-002**: `bash benchmark/gates/run_gates.sh` prints `all 19 gates pass`, as it did before the change
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Dependency | The shared Sync Loop declaration in the parent repository pins some kernel and knowledge statements by hash | An edit inside a pinned statement fails the residency check | Keep every edit outside the pinned statements and rerun `run_residency.sh` |
| Risk | The writer now drops a string that was the change, such as replaced copy shown only in a screenshot | Medium | The rule keeps a shown string that is itself the change verbatim, with a worked example |
| Risk | No playbook scenario covers a designed screen, so a regression shows only in real use | Medium | Named in Known Limitations with the image fixture it needs |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:questions -->
## 7. OPEN QUESTIONS

- Should the two pinned statements be reworded too, with a resync of the shared declaration in the parent repository? Decision: left to Michel, not part of this packet.
<!-- /ANCHOR:questions -->

---
