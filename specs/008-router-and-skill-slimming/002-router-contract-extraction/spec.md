---
title: "Phase Specification: Move the router pseudocode out of SKILL.md"
description: "Move the 608-line pseudocode fence to a dedicated reference and repoint the differential harness, taking SKILL.md under 600 lines"
importance_tier: "high"
contextType: "specification"
_memory:
  continuity:
    packet_pointer: "008-router-and-skill-slimming/002-router-contract-extraction"
    last_updated_at: "2026-09-03T00:00:00Z"
    last_updated_by: "claude"
    recent_action: "Phase carved out of the parent packet"
    next_safe_action: "Implement R2"
    blockers: []
    completion_pct: 0
---
# Phase Specification: Move the router pseudocode out of SKILL.md

<!-- SPECKIT_LEVEL: 2 -->

---

## 1. METADATA

| Field | Value |
| --- | --- |
| Phase | 002-router-contract-extraction |
| Parent | 008-router-and-skill-slimming |
| Requirement | R2 |
| Status | Planned |

---

## 2. SCOPE

Move the 608-line pseudocode fence to a dedicated reference and repoint the differential harness, taking SKILL.md under 600 lines

The parent packet holds the measured problem, the full requirement text and the risk table. This phase carries only what belongs to R2.

---

## 3. VERIFICATION

Inherited from the parent: router fixtures and the differential harness both green, the format validator and its fixtures passing, and every artifact under `export/z — Test Exports*/` still passing. Phase-specific checks live in the parent's requirement text.
