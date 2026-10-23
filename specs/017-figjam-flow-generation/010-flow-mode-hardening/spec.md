---
title: "Feature Specification: Phase 10: Flow Mode hardening"
description: "Flow Mode targeted a new FigJam page, which a FigJam file cannot have, and its check let through models the board generator rejects. This phase applies the 15 changes the phase 9 research ranked."
trigger_phrases:
  - "flow mode hardening"
  - "phase 10 flow mode hardening"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.2 -->
# Feature Specification: Phase 10: Flow Mode hardening

<!-- SPECKIT_LEVEL: 2 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 2 |
| **Priority** | P0 |
| **Status** | Complete |
| **Created** | 2026-10-20 |
| **Branch** | `main` |
| **Parent Spec** | ../spec.md |
| **Phase** | 10 of 10 |
| **Predecessor** | 009-figjam-skill-research |
| **Successor** | 008-upstream-roundtrip-and-release |
| **Handoff Criteria** | The check self-test, run_gates.sh, the format gate and the Sync Loop parity and residency gates pass |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:phase-context -->
## Phase Context

This is **Phase 10** of the Product Owner FigJam flow generation upgrade specification.

**Scope Boundary**: Flow Mode's reference, templates and check script, their two Project mirrors, the kernel's Flow Mode Delivery bullet, SYNC.md and the one declared statement the kernel edit moves.

**Dependencies**:
- `../009-figjam-skill-research/research/research.md` section 4, the 15 ranked changes.
- The operator chose all 15 on 2026-10-20.

**Deliverables**:
- `sk-product-owner/references/flow-mode.md`, `sk-product-owner/assets/flow-templates.md` and `sk-product-owner/scripts/flow_check.py` changed.
- The two Flow Knowledge files and the kernel changed to match.

**Changelog**:
- When this phase closes, refresh the matching file in ../changelog/ using the parent packet number plus this phase folder name.
<!-- /ANCHOR:phase-context -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
Flow Mode wrote each board into a new FigJam page, but a FigJam file has one page and no write can add another. Its check also passed models with an emoji, an underscore in a node id or a node named `end`, which the board generator rejects or mis-routes.

### Purpose
Apply the 15 ranked changes so Flow Mode targets a file, refuses what the generator cannot take, and proves which nodes each connector joins.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- The file target, one file per flow, the scoped rollback and the retry rules.
- New check rules: emoji, reserved ids, underscores, solid connectors, markup on the raw block, orphan nodes, label length and a named subgraph refusal.
- The structural read-back, the hosted preflight, the `fj` board check and the split's left-out list.
- Left to right as a second direction, the paired-stroke accent and a parity rule for the new model rules, chosen by the operator after the first pass.
- The 21 findings of a fresh review, all chosen by the operator: check bypasses and false failures, the conditional read-back, the `Left out:` reply line, the export exemption in SKILL.md, AGENTS.md and Interactive Mode, stale counts and a Flow playbook pair.

### Out of Scope
- A live board write, which needs the hosted Figma MCP.

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| sk-product-owner/references/flow-mode.md | Modify | Gate, read-back, rules, routes, recovery |
| sk-product-owner/assets/flow-templates.md | Modify | Usage notes, split note, left-out list, reply note |
| sk-product-owner/scripts/flow_check.py | Modify | Eight new conditions and nine planted models |
| claude project/knowledge/Product Owner - Templates - Flow Mode.md | Modify | The same changes for a Project |
| claude project/knowledge/Product Owner - Assets - Flow Templates.md | Modify | The same template changes |
| claude project/Custom Instructions.md | Modify | Flow Mode Delivery bullet |
| SYNC.md | Modify | Maintenance record |
| AGENTS.md, sk-product-owner/SKILL.md, references/interactive-mode.md and its Knowledge mirror | Modify | Flow Mode named as the export exemption |
| README.md, sk-product-owner/README.md, benchmark/gates/README.md, benchmark/gates/rule_parity.py | Modify | Counts, the Flow Mode section and whole-sentence parity phrases |
| sk-product-owner/manual-testing-playbook/ | Modify | SFL-001 and PFL-001 and the index counts |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | No live Flow Mode source, mirror or kernel line targets a page or clears one. |
| REQ-002 | The check refuses each new rule, and its self-test proves each one on a planted model. |
| REQ-003 | The shipped patterns and the Change Location model still pass the check. |
| REQ-004 | run_gates.sh, the format gate and the Sync Loop parity and residency gates pass. |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement |
|----|-------------|
| REQ-005 | SYNC.md records the change as maintenance, not a review. |

> Acceptance criteria for these requirements live in `acceptance-criteria.md`,
> which is the document that decides whether this packet may close.
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: A model the board generator would reject fails the check before the write gate.
- **SC-002**: A Flow Mode write can no longer clear a board that holds other work.
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Risk | The new rules refuse a real flow | Med | The shipped patterns and the Change Location model pass |
| Risk | The kernel edit moves a declared statement | Med | resync_statement.py, then residency in a scratch clone |
| Dependency | get_figjam connector fields | Low | Unobserved until a live board, and the read-back says when it was visual |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:nfr -->
## L2: NON-FUNCTIONAL REQUIREMENTS

### Reliability
- **NFR-R01**: Every new check rule has a planted model that fails on it.

### Maintainability
- **NFR-M01**: The skill and its mirror state the same rules in the same order.
<!-- /ANCHOR:nfr -->

---

<!-- ANCHOR:edge-cases -->
## L2: EDGE CASES

### Error Scenarios
- A quoted label with a parenthesis passes, and the good model in the self-test proves it.
- An arrow such as `<-->` is never read as an HTML tag.

### State Transitions
- A failed hosted call is read before any retry.
<!-- /ANCHOR:edge-cases -->

---

<!-- ANCHOR:complexity -->
## L2: COMPLEXITY ASSESSMENT

| Dimension | Score | Notes |
|-----------|-------|-------|
| Scope | 12/25 | Seven files plus the declaration |
| Risk | 10/25 | A shared kernel and a parity-gated mirror |
| Research | 4/20 | Done in phase 9 |
| **Total** | **26/70** | **Level 2** |
<!-- /ANCHOR:complexity -->

---

<!-- ANCHOR:questions -->
## 10. OPEN QUESTIONS

- Does the claude.ai Figma connector offer `get_figjam`? Unverified until a Project run.
<!-- /ANCHOR:questions -->
