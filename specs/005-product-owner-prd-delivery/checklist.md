---
title: "Verification Checklist: Product Owner Story and Epic Templates"
description: "Planning and implementation checks for the Product Owner Story and Epic contracts."
trigger_phrases:
  - "verify product owner story epic templates"
importance_tier: "high"
contextType: "reference"
_memory:
  continuity:
    packet_pointer: "005-product-owner-prd-delivery"
    last_updated_at: "2026-08-13T16:00:00Z"
    last_updated_by: "codex"
    recent_action: "Updated verification coverage for Story and Epic artifact kinds"
    next_safe_action: "Implement authoritative sources and collect evidence"
    blockers: []
    key_files:
      - "spec.md"
      - "plan.md"
      - "tasks.md"
    completion_pct: 20
    open_questions: []
    answered_questions: []
---
# Verification Checklist: Product Owner Story and Epic Templates

<!-- SPECKIT_LEVEL: 2 -->
<!-- SPECKIT_TEMPLATE_SOURCE: checklist | v2.2 -->

---

<!-- ANCHOR:protocol -->
## Verification Protocol

| Priority | Handling | Completion Impact |
|---|---|---|
| **P0** | Hard blocker | Cannot claim implementation complete |
| **P1** | Required | Complete or obtain explicit deferral |
| **P2** | Optional | May defer with a reason |
<!-- /ANCHOR:protocol -->

---

<!-- ANCHOR:pre-impl -->
## Pre-Implementation

- [x] [P0] Four approved Story sources read in full
  - Evidence: `spec.md` lists each dated Onboarding Story and the repeated Story contract.
- [x] [P0] Approved Epic source read in full
  - Evidence: `spec.md` records the Epic's Goal, Scope, release-level criteria and missing default Requirements section.
- [x] [P0] Story and Epic requirements documented
  - Evidence: `spec.md` contains separate canonical scaffolds and artifact-kind routing rules.
- [x] [P1] Dependencies, parity surfaces and rollback identified
  - Evidence: `plan.md` inventories authoritative sources, router fixtures, kernel, mirrors and checks.
- [x] [P1] Delivery placement and labels retained
  - Evidence: both canonical shapes close with Estimation, Rabbit holes and No-gos.
<!-- /ANCHOR:pre-impl -->

---

<!-- ANCHOR:code-quality -->
## Code Quality

- [ ] [P0] Authoritative sources change before generated mirrors
- [ ] [P0] No generated mirror is hand-edited
- [ ] [P1] Markdown structure follows the approved Story and Epic contracts
- [ ] [P1] Changelog records only observed verification results
<!-- /ANCHOR:code-quality -->

---

<!-- ANCHOR:testing -->
## Testing

- [ ] [P0] Story output uses the approved title, preamble and section order
- [ ] [P0] Story requirements use natural bullets without Checklist subheadings or checkboxes
- [ ] [P0] Epic output contains Goal and Scope and omits Requirements by default
- [ ] [P0] Story acceptance criteria can use optional H4 groups
- [ ] [P0] Epic acceptance criteria remain release-level
- [ ] [P0] Story and Epic output end with the shared Delivery block
- [ ] [P0] `$epic`, `$e` and natural Epic framing route correctly
- [ ] [P0] Embedded and filename-like Epic aliases do not route
- [ ] [P0] Compiler check passes with validators
- [ ] [P0] Router fixtures retain a full passing result
- [ ] [P1] Refinement-fidelity wording prevents unrelated normalization
- [ ] [P1] Unknown Delivery values remain `TBD...`
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:fix-completeness -->
## Fix Completeness

- [ ] [P0] Producer inventory includes template, mode, skill router and bootstrap
- [ ] [P0] Consumer inventory includes examples, README, kernel and mirrors
- [ ] [P1] Obsolete tier and Checklist guidance has no active producer
- [ ] [P1] The scoped diff proves approved Product Context sources and exports are untouched
<!-- /ANCHOR:fix-completeness -->

---

<!-- ANCHOR:security -->
## Security

- [x] [P0] No secrets or environment values belong in this documentation change
  - Evidence: the packet contains format, routing and verification requirements only.
- [ ] [P1] Sync and review commands expose no secret output
- [ ] [P1] ClickUp consent and markdown transport remain unchanged
<!-- /ANCHOR:security -->

---

<!-- ANCHOR:docs -->
## Documentation

- [x] [P0] `spec.md`, `plan.md`, `tasks.md` and checklist describe the same Story and Epic scope
- [ ] [P0] Product Owner README and changelog reflect the implemented contract
- [ ] [P1] Implementation summary records real checks after implementation
- [ ] [P1] Human kernel review status is explicit
<!-- /ANCHOR:docs -->

---

<!-- ANCHOR:file-org -->
## File Organization

- [x] [P1] Packet remains in the AI Systems spec group
  - Evidence: `specs/005-product-owner-prd-delivery/` retains its existing packet identity.
- [ ] [P1] Scratch contains no temporary implementation artifacts at completion
- [ ] [P1] No stray backup or temporary files remain
<!-- /ANCHOR:file-org -->

---

<!-- ANCHOR:summary -->
## Verification Summary

| Category | Total | Verified |
|---|---:|---:|
| P0 Items | 20 | 5 |
| P1 Items | 15 | 3 |
| P2 Items | 0 | 0 |

**Verification Date**: Planning packet updated on 2026-08-13. Implementation remains pending.
<!-- /ANCHOR:summary -->
