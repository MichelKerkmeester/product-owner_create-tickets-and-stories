---
title: "Feature Specification: Product Owner Scope-Aware Verbosity Scaling"
description: "Wire the Product Owner router's existing scope signal into an explicit output-verbosity contract so tasks and bugs are concise by default and add context only when scope or an explicit request warrants it."
trigger_phrases:
  - "product owner verbosity scaling"
  - "scope aware ticket length"
  - "concise by default tickets"
importance_tier: "high"
contextType: "general"
_memory:
  continuity:
    packet_pointer: "001-product-owner-scope-aware-verbosity"
    last_updated_at: "2026-06-15T00:00:00Z"
    last_updated_by: "claude-opus-4-8"
    recent_action: "Authored the Level 1 specification for Product Owner scope-aware verbosity scaling."
    next_safe_action: "On approval, implement the verbosity contract in skill/ then re-sync the claude project mirrors."
    blockers: []
    completion_pct: 5
    open_questions:
      - "Version bump policy for touched mirrors"
      - "Whether to add an explicit detailed-mode command"
---
# Feature Specification: Product Owner Scope-Aware Verbosity Scaling

<!-- SPECKIT_LEVEL: 1 -->
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.2 -->

---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 1 |
| **Priority** | P1 |
| **Status** | Planned |
| **Created** | 2026-06-15 |
| **Branch** | `001-product-owner-scope-aware-verbosity` |
| **System** | Product Owner (Barter) |

<!-- /ANCHOR:metadata -->
---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
The Product Owner system has no contract tying output verbosity to request scope. Every task gets the same treatment regardless of size: a multi-paragraph About, optional References/Epic/User Story blocks, category headings, and a descriptive paragraph per requirement. The router already computes a scope signal: `detect_shape_hint()` in `skill/SKILL.md` classifies a request small/medium/large and emits a `depth` field (light/standard/expanded) plus grouping guidance. Nothing consumes it. The depth value never reaches Task Mode delivery standards or the templates. Energy levels (Quick/Standard/Deep) scale thinking and perspective count, not artifact length, so a Standard one-line button tweak is still over-explained. The user has to manually ask for a trim, and there is no defined concise-by-default baseline.

### Purpose
Wire the existing scope signal into an explicit output-verbosity contract. The Product Owner writes right-sized artifacts: concise by default, expanding About length, optional context sections, category headings, per-requirement description and User Story only when scope or an explicit request signal ("detailed", "with context", "thorough") warrants it. WHAT/WHY framing, template compliance, the six quality floors and Human Voice Rules stay unchanged. The contract scales narrative and optional context only, never acceptance-criteria completeness.

<!-- /ANCHOR:problem -->
---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- `skill/SKILL.md`: add a Verbosity Scaling contract that consumes `detect_shape_hint` and an explicit-detail signal, mapping each scope tier to concrete output rules. Add one matching entry to Product Owner Principles.
- `skill/references/task_mode.md`: add a scope-to-verbosity delivery standard (which optional sections per tier, when category headings apply, minimal About by default, per-requirement description optional at small scope).
- `skill/assets/task_templates.md`: add template-selection-by-scope guidance (Quick template for small, Canonical for medium/large, drop unused optional sections).
- `skill/references/bug_mode.md`: add an explicit no-padding note (About stays 1-2 sentences, only provided evidence appears, no narrative inflation).
- `skill/references/depth_framework.md`: one-line cross-reference noting verbosity scales with scope independently of energy level.
- Re-sync the affected `claude project/knowledge/` mirrors, add the rule to `claude project/Custom Instructions.md`, and update the `claude project/README.md` paired-version and sha table.

### Out of Scope
- Routing decisions (which mode is selected), confidence thresholds, scoring-rubric floors, commands, energy levels and DEPTH phases.
- Human Voice Rules content.
- The fixed Bug report section order and the four-item QA checklist.
- A new dedicated detail command; verbosity stays automatic plus the existing `$quick`.
- Any other Barter system. This is Product Owner only.
- Source-sync behavior: refining an existing task still preserves source structure, so scaling applies to net-new artifacts only.

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| `Product Owner/skill/SKILL.md` | Modify | Verbosity Scaling contract + principle, consuming `detect_shape_hint` |
| `Product Owner/skill/references/task_mode.md` | Modify | Scope-to-verbosity delivery standard |
| `Product Owner/skill/assets/task_templates.md` | Modify | Template-selection-by-scope guidance |
| `Product Owner/skill/references/bug_mode.md` | Modify | No-padding verbosity note |
| `Product Owner/skill/references/depth_framework.md` | Modify | One-line scope-vs-energy cross-reference |
| `Product Owner/claude project/knowledge/*.md` | Modify | Re-synced byte-copy mirrors of changed sources |
| `Product Owner/claude project/Custom Instructions.md` | Modify | Add verbosity scaling rule (parity) |
| `Product Owner/claude project/README.md` | Modify | Update paired-version and sha table |

<!-- /ANCHOR:scope -->
---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-001 | Verbosity contract defined | `SKILL.md` maps small/medium/large scope to concrete output rules: About length, which optional sections appear, category headings, per-requirement description, User Story |
| REQ-002 | Concise default | Small scope yields a minimal artifact: short About, flat numbered checklist, no category headings, no References/Epic/User Story unless present in source or explicitly requested |
| REQ-003 | Scale-up on signal | Large scope or an explicit detail request expands context sections and per-requirement descriptions |
| REQ-004 | Shape hint consumed | The `detect_shape_hint` depth value is referenced by the contract and is no longer orphaned logic |
| REQ-005 | Bug no-padding | `bug_mode.md` keeps the fixed structure but states About is 1-2 sentences and only provided evidence appears |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-006 | Mirrors synced | Changed knowledge mirrors byte-match source, Custom Instructions carries the rule, README version/sha table updated |
| REQ-007 | House style + caps | No new em dashes or prose semicolons, SKILL.md stays within size caps, HVR and quality floors unaffected |
| REQ-008 | Source preservation safe | Scaling never overrides source-sync or refinement structure preservation |

<!-- /ANCHOR:requirements -->
---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: **Given** a small-scope request (one screen, one control), **When** a task is generated, **Then** the artifact has a short About, a flat checklist, and no optional context sections unless requested.
- **SC-002**: **Given** a large-scope or explicitly detailed request, **When** a task is generated, **Then** the artifact uses category headings and per-requirement descriptions.
- **SC-003**: **Given** the recent ticket 012 (Edit flow buttons) re-generated under the new contract, **Then** it lands at the concise shape with no follow-up trim request.
- **SC-004**: **Given** the drift checks, **Then** every changed mirror byte-matches source and HVR plus the six quality floors still pass.

<!-- /ANCHOR:success-criteria -->
---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Risk | Over-trimming drops needed acceptance detail | High | Contract scales narrative and optional context only, checklist completeness stays independent of verbosity |
| Risk | Conflict with source preservation | Medium | Explicit rule: sync and refinement preserve source, scaling applies to net-new artifacts |
| Risk | Scope detection feels subjective | Medium | Reuse the deterministic `detect_shape_hint`, default to medium when ambiguous, honor explicit signal override |
| Risk | Mirror drift after edits | Medium | Re-sync every changed mirror, verify byte-match, update README sha table |
| Dependency | `detect_shape_hint` in `SKILL.md` | High | The contract reads its existing small/medium/large depth output |
| Dependency | sk-doc reference/asset templates and PO sync rules | High | Edits follow the OVERVIEW shape and the README sync protocol |

<!-- /ANCHOR:risks -->
---

<!-- ANCHOR:questions -->
## 7. OPEN QUESTIONS

- Version bump policy: bump touched docs' versions and rename their mirrors, or keep versions stable and update sha only. Default assumed: bump SKILL minor (0.2.0 to 0.3.0) and the touched reference/asset versions, then update the README table.
- Whether to add an explicit detail command as the inverse of `$quick`, or rely on the natural-language signal only. Default assumed: natural-language signal only, no new command.
- Whether the contract is mirrored as a short table in Custom Instructions or as prose. Default assumed: a short table for parity with the skill.

<!-- /ANCHOR:questions -->

---

<!--
CORE TEMPLATE (~80 lines)
- Essential what/why/how only
- No boilerplate sections
- Add L2/L3 addendums for complexity
-->
