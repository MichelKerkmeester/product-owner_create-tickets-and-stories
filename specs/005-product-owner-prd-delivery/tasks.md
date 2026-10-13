---
title: "Tasks: Product Owner Story and Epic Templates"
description: "Source-first task breakdown for aligning Story output, adding Epic output and validating Product Owner routing and cross-runtime parity."
trigger_phrases:
  - "product owner story epic tasks"
importance_tier: "high"
contextType: "reference"
_memory:
  continuity:
    packet_pointer: "005-product-owner-prd-delivery"
    last_updated_at: "2026-08-13T16:00:00Z"
    last_updated_by: "codex"
    recent_action: "Sequenced Story and Epic template implementation tasks"
    next_safe_action: "Begin Phase 1 baseline checks"
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
# Tasks: Product Owner Story and Epic Templates

<!-- SPECKIT_LEVEL: 2 -->
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.2 -->

---

<!-- ANCHOR:notation -->
## Task Notation

- `[ ]` pending
- `[x]` verified complete
- P0 blocks completion
- P1 requires completion or explicit user-approved deferral
<!-- /ANCHOR:notation -->

---

<!-- ANCHOR:phase-1 -->
## Phase 1: Baseline and Contract

- [x] P0 Read the four approved Story sources and the approved Epic source in full
- [x] P0 Record Story and Epic section orders and their key differences in `spec.md`
- [ ] P0 Record failing assertions for missing Epic routing and obsolete Story checklist behavior
- [ ] P0 Inspect Git status and preserve unrelated changes in both repositories
- [ ] P0 Run the Product Owner compiler plan and confirm registered paths exist
- [ ] P1 Record the current Product Owner router fixture total
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Authoritative Implementation

- [ ] P0 Replace tier-selected PRD scaffolds with canonical Story and Epic shapes in `assets/prd-templates.md`
- [ ] P0 Add Story or Epic artifact-kind selection to `references/prd-mode.md`
- [ ] P0 Add exact `$epic` and `$e` routing, natural Epic framing and conflict handling to `SKILL.md`
- [ ] P0 Align the command registry and PRD contract in `AGENTS.md`
- [ ] P0 Change Story requirements to bold names with natural bullets and no Checklist subheading
- [ ] P0 Add Goal and Scope to Epic output and omit Requirements by default
- [ ] P0 Keep Delivery as the shared closing section with `TBD...` fallbacks
- [ ] P1 Replace or retire obsolete tier examples and add canonical Story and Epic examples
- [ ] P0 Add Epic command, framing, precedence, conflict and false-positive router fixtures
- [ ] P1 Align the Product Owner README
- [ ] P0 Hand-synthesize the same contract in `claude project/Custom Instructions.md`
- [ ] P1 Add the next valid changelog entry with observed verification results
- [ ] P0 Run Product Owner sync with `--write`
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [ ] P0 Assert canonical Story order and bullet-only requirement grammar
- [ ] P0 Assert canonical Epic order, Goal, Scope and no default Requirements section
- [ ] P0 Assert both artifact kinds end with the same Delivery block
- [ ] P0 Run all Product Owner router fixtures and record the exact result
- [ ] P0 Run `check --system product-owner --run-validators`
- [ ] P1 Complete the required human kernel review and rerun the compiler check
- [ ] P0 Confirm the five approved Product Context sources and Product Owner exports are unchanged
- [ ] P1 Run `git diff --check` and no-stray-file sweeps in both repositories
- [ ] P1 Update the packet checklist and implementation summary with current evidence
<!-- /ANCHOR:phase-3 -->

---

<!-- ANCHOR:completion -->
## Completion Criteria

- [ ] Every P0 task is complete with current command evidence
- [ ] Every P1 task is complete or explicitly deferred by the user
- [ ] Product Owner compiler and router gates pass
- [ ] Human kernel review is recorded if the contract-input gate requires it
- [ ] No approved Product Context source, export or unrelated system file changed
<!-- /ANCHOR:completion -->

---

<!-- ANCHOR:cross-refs -->
## Cross-References

- `spec.md` owns the Story and Epic contracts and routing decisions
- `plan.md` owns sequencing, parity surfaces and rollback
- `checklist.md` owns verification state
- `implementation-summary.md` owns delivered evidence after implementation
- Related packet: `../004-product-owner-prd-opening-restructure/spec.md`
<!-- /ANCHOR:cross-refs -->
