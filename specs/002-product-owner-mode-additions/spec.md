---
title: "Spec: Product Owner Mode Additions (Parent)"
description: "Parent spec for the Product Owner capability wave: Doc Mode, Story Mode, ClickUp handoff, per-mode example libraries, and the package rewiring that ships them across both packagings."
trigger_phrases:
  - "product owner mode additions"
  - "product owner parent spec"
  - "per-mode examples"
importance_tier: "high"
contextType: "specification"
_memory:
  continuity:
    packet_pointer: "002-product-owner-mode-additions"
    last_updated_at: "2026-07-15T18:20:00Z"
    last_updated_by: "claude"
    recent_action: "Restructured the three shipped mode specs into phases 001-003 and opened phases 004-008 for the example libraries and rewiring"
    next_safe_action: "Author the per-mode example libraries (phases 004-007), then rewire the package (phase 008)"
---
<!-- SPECKIT_LEVEL: 3 -->
# Spec: Product Owner Mode Additions (Parent)

## 1. PURPOSE

One parent for the Product Owner capability wave. The Product Owner system started as Task and Bug modes; this initiative adds documentation, stories, safe ClickUp delivery, and worked example libraries so any fresh model session produces house-quality artifacts from cold bootstrap.

## 2. PHASES

| Phase | Scope |
|-------|-------|
| `001-product-owner-doc-mode` | COMPLETE. Doc Mode: DOC intent, source classification, conflict gate, four adaptive shapes, ClickUp grammar, plus amendments 002-004 from four review passes. |
| `002-product-owner-story-mode` | COMPLETE. Story Mode: story-format research, the three-tier template family, STORY intent with tier intelligence, cross-model end-to-end test. |
| `003-product-owner-clickup-handoff` | COMPLETE. ClickUp consent gate (offer, never push) and the markdown-preserving transport contract, live-verified. |
| `004-task-examples` | Task Mode example library: three to five worked task artifacts in `skill/assets/examples/task/`. |
| `005-bug-examples` | Bug Mode example library: three to five worked bug reports in `skill/assets/examples/bug/`. |
| `006-doc-examples` | Doc Mode example library: three to five worked documents in `skill/assets/examples/doc/`, one per adaptive shape at minimum. |
| `007-story-examples` | Story Mode example library: three worked stories in `skill/assets/examples/story/`, one per tier. |
| `008-package-rewiring` | Wire the example libraries into SKILL.md (ON_DEMAND example loading per routed mode), AGENTS.md, the user guide, SYNC.md, and the Claude project package (mirrors, checksum manifest, kernel knowledge table); full verification. |

## 3. REQUIREMENTS FOR PHASES 004-008

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-001 | One example folder per mode. | `skill/assets/examples/{task,bug,doc,story}/` exist, each holding three to five self-contained worked examples. |
| REQ-002 | Generic subject matter. | Every example uses generic Product Design / App & Web Development situations (fictional products); zero Barter product references, zero references to past Barter tasks or docs. |
| REQ-003 | Examples obey their mode's grammar. | Task and Bug examples use the H3-section, `-` bullet, `- [ ]` checklist, `---` separator grammar of their templates; Doc and Story examples use the ClickUp `* * *` / `*   ` contract; Story examples carry Connextra lines, Given/When/Then scenario bullets and DoR/DoD gates with one example per tier. |
| REQ-004 | Examples are exemplars, not instructions. | Each file is one filled artifact with a short frontmatter (title matching its mirror basename, description, version 0.100) and no template placeholders, meta-commentary or `{curly}` slots. |
| REQ-005 | Router wiring. | SKILL.md loads examples ON_DEMAND for the routed mode only (never bulk); AGENTS.md, the user guide and SYNC.md describe the example libraries; loading stays scoped. |
| REQ-006 | Claude project parity. | Every example ships as a byte-identical knowledge mirror with a checksum row; the kernel's knowledge table tells the Project when to consult each example set; the upload inventory and smoke matrix cover them. |
| REQ-007 | Verification. | Mirror parity and checksum manifest fully green; router fixture suite passes; a grammar scan over every example shows zero canon violations for its mode. |

## 4. EXECUTION MODEL

Phases 004-007 are authored by four parallel Sonnet 5 agents, one per mode, each briefed with the mode's reference and template files and the generic-subject constraint. Phase 008 is executed by the orchestrating session, which owns sync, checksums and verification.
