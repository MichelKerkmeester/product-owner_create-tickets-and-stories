---
title: "Implementation Plan: Product Owner Story and Epic Templates"
description: "Replace tier-driven PRD output with approved Story and Epic shapes, update routing and examples, then regenerate Product Owner mirrors and verify parity."
trigger_phrases:
  - "product owner story epic plan"
  - "implement product owner epic template"
importance_tier: "high"
contextType: "plan"
_memory:
  continuity:
    packet_pointer: "005-product-owner-prd-delivery"
    last_updated_at: "2026-08-13T16:00:00Z"
    last_updated_by: "codex"
    recent_action: "Planned the source-first Story and Epic contract update"
    next_safe_action: "Capture baselines and patch authoritative Product Owner sources"
    blockers: []
    key_files:
      - "AI Systems/Product Owner/sk-product-owner/assets/prd-templates.md"
      - "AI Systems/Product Owner/sk-product-owner/references/prd-mode.md"
      - "AI Systems/Product Owner/sk-product-owner/SKILL.md"
      - "AI Systems/Product Owner/benchmark/router/"
    completion_pct: 20
    open_questions: []
    answered_questions: []
---
# Implementation Plan: Product Owner Story and Epic Templates

<!-- SPECKIT_LEVEL: 2 -->
<!-- SPECKIT_TEMPLATE_SOURCE: plan-core | v2.2 -->

---

<!-- ANCHOR:summary -->
## 1. SUMMARY

### Technical Context

| Aspect | Value |
|---|---|
| **Language/Stack** | Markdown, JSON, shell fixtures and Node.js sync tooling |
| **Framework** | Product Owner skill package and local sync compiler |
| **Storage** | Authoritative skill files plus generated Claude knowledge mirrors |
| **Testing** | Static shape assertions, router fixtures, strict spec validation and compiler checks |

### Overview

Change the authoritative Product Owner PRD contract first. Replace Simple, Medium and Complex template selection with explicit Story or Epic artifact-kind selection. Align Story output with the four approved Onboarding stories, add the Epic shape based on the approved Onboarding epic, then update examples, routing, bootstrap guidance and the Claude kernel before regenerating mirrors.
<!-- /ANCHOR:summary -->

---

<!-- ANCHOR:quality-gates -->
## 2. QUALITY GATES

### Definition of Ready

- [x] Four approved Story sources and one approved Epic source have been read in full
- [x] Story and Epic structures are documented separately
- [x] Source, derived surfaces, routing impact and rollback are identified
- [x] Delivery placement and labels remain approved

### Definition of Done

- [ ] Authoritative sources select Story or Epic before rendering
- [ ] Story output uses concise bullet requirements without Checklist subheadings
- [ ] Epic output includes Goal and Scope and omits Requirements by default
- [ ] Story and Epic examples demonstrate the approved shapes and shared Delivery close
- [ ] Epic routing fixtures, full Product Owner router fixtures and compiler checks pass
- [ ] Human kernel review is recorded when required by `SYNC.md`
<!-- /ANCHOR:quality-gates -->

---

<!-- ANCHOR:architecture -->
## 3. ARCHITECTURE

### Pattern

One PRD Mode with an explicit artifact-kind discriminator and two canonical templates.

### Key Components

- **Router and bootstrap**: resolve `artifact_kind=STORY` or `artifact_kind=EPIC`
- **PRD mode reference**: owns creation, refinement and validation behavior for both kinds
- **Template asset**: owns the literal Story and Epic scaffolds and shared Delivery block
- **Examples**: demonstrate one canonical Story and one canonical Epic without obsolete tier behavior
- **Claude kernel**: hand-synthesized runtime parity surface
- **Sync compiler**: regenerates declared mirrors, checksums and package state

### Data Flow

An explicit command or natural-language frame selects PRD Mode and its artifact kind. The selected kind chooses one canonical scaffold. User sources populate the scaffold, the Product Owner quality gate checks the correct contract and export remains unchanged.
<!-- /ANCHOR:architecture -->

---

<!-- ANCHOR:affected-surfaces -->
## FIX ADDENDUM: AFFECTED SURFACES

| Surface | Current Role | Action | Verification |
|---|---|---|---|
| `assets/prd-templates.md` | Tiered PRD scaffolds | Replace with Story and Epic scaffolds plus shared Delivery | Exact section-order assertions |
| `references/prd-mode.md` | PRD workflow and tier selection | Add artifact-kind selection and kind-specific gates | Static assertions and mirror parity |
| `SKILL.md` | Runtime router and summary | Add `$epic` and `$e`, framing and kind metadata | Router fixtures |
| `AGENTS.md` | Project bootstrap | Add Epic commands and current shape description | Static parity check |
| PRD examples | Tiered worked examples | Retire or replace obsolete examples with Story and Epic examples | No checklist or tier residue |
| `benchmark/router/` | Routing oracle and fixtures | Add Epic positives, negatives and conflicts | Full fixture pass |
| `README.md` | Package guide | Document both artifact kinds | Static content check |
| `Custom Instructions.md` | Claude runtime kernel | Hand-synthesize equivalent behavior | Kernel review and compiler check |
| Knowledge mirrors | Derived package | Regenerate, never hand-edit | Compiler byte-parity check |
| Product Context sources | Approved examples | Read-only | Scoped Git diff |
<!-- /ANCHOR:affected-surfaces -->

---

<!-- ANCHOR:phases -->
## 4. IMPLEMENTATION PHASES

### Phase 1: Baseline and Contract

- [ ] Record failing assertions for missing Epic routing and obsolete Story checklist behavior
- [ ] Capture current router fixture total and Product Owner compiler state
- [ ] Confirm unrelated worktree changes before editing
- [ ] Confirm the five approved source documents remain read-only

### Phase 2: Authoritative Implementation

- [ ] Update `prd-templates.md` with Story, Epic and shared Delivery scaffolds
- [ ] Update `prd-mode.md` with artifact-kind behavior and refinement rules
- [ ] Update `SKILL.md` and `AGENTS.md` with Epic commands, framing and routing precedence
- [ ] Replace obsolete tier examples with canonical Story and Epic examples
- [ ] Update router oracle and fixtures
- [ ] Align README and hand-synthesize the Claude kernel
- [ ] Add the next valid changelog entry after verification values are known
- [ ] Run Product Owner sync with `--write`

### Phase 3: Verification

- [ ] Assert exact Story and Epic orders, requirement grammar and shared Delivery
- [ ] Assert `$epic` and `$e` positives, false positives and conflicts
- [ ] Run all Product Owner router fixtures
- [ ] Run Product Owner compiler check with validators
- [ ] Complete required kernel review and rerun checks
- [ ] Confirm no approved Product Context source or export changed
<!-- /ANCHOR:phases -->

---

<!-- ANCHOR:testing -->
## 5. TESTING STRATEGY

| Test Type | Scope | Tools |
|---|---|---|
| Story shape | Title, preamble, opening, bullet requirements, acceptance criteria and Delivery | `rg`, ordered assertions and diff inspection |
| Epic shape | Goal, Scope, no default Requirements, release criteria and Delivery | `rg`, ordered assertions and diff inspection |
| Routing | Commands, framing, conflicts, precedence and false positives | Product Owner router fixtures |
| Example migration | No Simple, Medium, Complex or Checklist contract remains | Repository scan |
| Mirror parity | Declared knowledge sources and generated state | `ai-system-sync.cjs check --system product-owner --run-validators` |
| Source preservation | Approved stories, epic and exports remain unchanged | Scoped `git diff` |
| Repository hygiene | Intended files only and no temporary artifacts | `git status --short`, `git diff --check` |
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:dependencies -->
## 6. DEPENDENCIES

| Dependency | Type | Status | Impact if Blocked |
|---|---|---|---|
| Approved Onboarding sources | Product evidence | Green | Template shape lacks authority |
| Product Owner authoritative package | Internal | Green | No safe source for the change |
| Product Owner router benchmark | Internal | Green | Epic command behavior cannot be proven |
| Product Owner sync registry | Internal | Green | Mirrors cannot be regenerated safely |
| Sync compiler runtime | Internal | To verify | Mechanical parity cannot close |
| Human kernel reviewer | Human | Required after final bytes | Contract-input review remains incomplete |
<!-- /ANCHOR:dependencies -->

---

<!-- ANCHOR:rollback -->
## 7. ROLLBACK PLAN

- **Trigger**: Shape assertions, router fixtures, compiler checks or kernel review reject the new contract
- **Procedure**: Revert only the Story and Epic contract edits and changelog, restore the prior PRD mode and examples, run Product Owner sync and verify the previous router state without touching Product Context sources or exports
<!-- /ANCHOR:rollback -->

---

<!-- ANCHOR:phase-deps -->
## L2: PHASE DEPENDENCIES

| Phase | Depends On | Blocks |
|---|---|---|
| Baseline and Contract | Approved packet and source audit | Authoritative edits |
| Authoritative Implementation | Baseline evidence | Sync and verification |
| Verification | Final authoritative and kernel bytes | Completion claim |
<!-- /ANCHOR:phase-deps -->

---

<!-- ANCHOR:effort -->
## L2: EFFORT ESTIMATION

| Workstream | Expected Size | Notes |
|---|---|---|
| Template and mode contract | Medium | Two artifact kinds replace tier selection |
| Router and fixtures | Medium | New commands, framing and negative cases |
| Examples and README | Medium | Obsolete tier examples must stop teaching old behavior |
| Kernel and sync | Medium | Hand synthesis plus generated state |
| Verification | Medium | Static, router, compiler and human review gates |
<!-- /ANCHOR:effort -->

---

<!-- ANCHOR:enhanced-rollback -->
## L2: ENHANCED ROLLBACK

1. Preserve unrelated worktree changes and the five approved source documents.
2. Restore the previous PRD router, tier language, template asset and examples.
3. Remove only the Epic command and artifact-kind additions introduced by this packet.
4. Restore README and kernel wording to the pre-change state.
5. Run sync with `--write`, then rerun compiler and router checks.
<!-- /ANCHOR:enhanced-rollback -->
