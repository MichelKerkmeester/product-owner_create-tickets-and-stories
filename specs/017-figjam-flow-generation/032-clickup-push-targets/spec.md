---
title: "Feature Specification: Phase 32: Local ClickUp push targets with a private doc option"
description: "A ClickUp push has no destination rule, so every push asks from scratch and a public repo cannot carry a team's ClickUp links. This phase, an operator request, makes sure a ClickUp push goes to the link the operator set locally for that artifact kind, or asks where when none is set, and always offers a private doc."
trigger_phrases:
  - "clickup push targets"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.2 -->
# Feature Specification: Phase 32: Local ClickUp push targets with a private doc option

<!-- SPECKIT_LEVEL: 2 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 2 |
| **Priority** | P1 |
| **Status** | Complete |
| **Created** | 2026-10-21 |
| **Branch** | `main` |
| **Parent Spec** | ../spec.md |
| **Phase** | 32 of 32 |
| **Predecessor** | ../031-round-three-apply |
| **Successor** | None |
| **Handoff Criteria** | The change is applied, mirrored and every gate passes |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:phase-context -->
## Phase Context

This is **Phase 32** of the Product Owner FigJam flow generation upgrade, added at the operator's request to set ClickUp push targets locally.

**Scope Boundary**: `.gitignore`, a new `.env.example`, `AGENTS.md` ClickUp Handoff, `sk-product-owner/SKILL.md`, `sk-product-owner/assets/interactive-response-templates.md` and its Knowledge mirror, the kernel's ClickUp offer and the sk-product-owner playbook.

**Dependencies**:
- The operator's answers of 2026-10-21: a gitignored `.env` with a tracked `.env.example`, one link per artifact kind, and the claude.ai Project always asks.

**Deliverables**:
- The edited sources, their Project mirrors where they have one, and passing gates.

**Changelog**:
- When this phase closes, refresh the matching file in ../changelog/ using the parent packet number plus this phase folder name.
<!-- /ANCHOR:phase-context -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
A ClickUp push has no destination rule, so every push asks from scratch and a public repo cannot carry a team's ClickUp links.

### Purpose
A ClickUp push goes to the link the operator set locally for that artifact kind, or asks where when none is set, and always offers a private doc.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- `.gitignore`, a new `.env.example`, `AGENTS.md` ClickUp Handoff, `sk-product-owner/SKILL.md`, `sk-product-owner/assets/interactive-response-templates.md` and its Knowledge mirror, the kernel's ClickUp offer and the sk-product-owner playbook

### Out of Scope
- Any other ranked change, which has its own phase
- Any Barter screenshot, Barter flow or board URL

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| `.gitignore`, a new `.env.example`, `AGENTS.md` ClickUp Handoff, `sk-product-owner/SKILL.md`, `sk-product-owner/assets/interactive-response-templates.md` and its Knowledge mirror, the kernel's ClickUp offer and the sk-product-owner playbook | Modify | A ClickUp push goes to the link the operator set locally for that artifact kind, or asks where when none is set, and always offers a private doc |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | A ClickUp push goes to the link the operator set locally for that artifact kind, or asks where when none is set, and always offers a private doc. |
| REQ-002 | Every gate passes after the change: run_gates.sh, the format gates, the playbook validators and the Sync Loop gates where a mirror changed. |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement |
|----|-------------|
| REQ-003 | No ClickUp link enters a tracked file, and the vendored `mcp-click-up/` packet stays a byte copy. |

> Acceptance criteria for these requirements live in `acceptance-criteria.md`,
> which is the document that decides whether this packet may close.
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: The push targets live in a gitignored `.env` or the shell, with a tracked `.env.example`, one link per artifact kind. With a link set the offer names it and adds a private doc option, and with none set it asks where and recommends a private doc. The claude.ai kernel always asks.
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Risk | Parallel edits collide in a shared file | Med | Edits apply in order and a failed match is redone by hand |
| Risk | A mirror drifts from its source | Med | Mirrors are regenerated or edited with the source and the parity gates run |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:nfr -->
## L2: NON-FUNCTIONAL REQUIREMENTS

### Security
- **NFR-S01**: No secrets, board URLs or Barter flows in any edit.

### Reliability
- **NFR-R01**: The pre-change tree is snapshotted, so the change reverts file by file.
<!-- /ANCHOR:nfr -->

---

<!-- ANCHOR:edge-cases -->
## L2: EDGE CASES

### Error Scenarios
- A proposed edit whose old text no longer matches: redone by hand against the current file.

### State Transitions
- Partial completion: the snapshot restores any file.
<!-- /ANCHOR:edge-cases -->

---

<!-- ANCHOR:complexity -->
## L2: COMPLEXITY ASSESSMENT

| Dimension | Score | Notes |
|-----------|-------|-------|
| Scope | 8/25 | A few files |
| Risk | 6/25 | Reversible text edits |
| Research | 2/20 | The ClickUp document API is documented in `mcp-click-up/` |
| **Total** | **18/70** | **Level 2** |
<!-- /ANCHOR:complexity -->

---

<!-- ANCHOR:questions -->
## 10. OPEN QUESTIONS

- None.
<!-- /ANCHOR:questions -->
