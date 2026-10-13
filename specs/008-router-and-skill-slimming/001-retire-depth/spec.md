---
title: "Phase Specification: Retire the DEPTH framework"
description: "Delete the 556-line always-loaded DEPTH reference and remove it from seventeen referencing files, rehoming anything still live rather than dropping it"
importance_tier: "high"
contextType: "specification"
_memory:
  continuity:
    packet_pointer: "008-router-and-skill-slimming/001-retire-depth"
    last_updated_at: "2026-09-03T00:00:00Z"
    last_updated_by: "claude"
    recent_action: "Phase carved out of the parent packet"
    next_safe_action: "Implement R3"
    blockers: []
    completion_pct: 0
---
# Phase Specification: Retire the DEPTH framework

<!-- SPECKIT_LEVEL: 2 -->

---

## 1. METADATA

| Field | Value |
| --- | --- |
| Phase | 001-retire-depth |
| Parent | 008-router-and-skill-slimming |
| Requirement | R3 |
| Status | Planned |

---

## 2. SCOPE

Delete the 556-line always-loaded DEPTH reference and remove it from seventeen referencing files, rehoming anything still live rather than dropping it

The parent packet holds the measured problem, the full requirement text and the risk table. This phase carries only what belongs to R3.

---

## 3. VERIFICATION

Inherited from the parent: router fixtures and the differential harness both green, the format validator and its fixtures passing, and every artifact under `export/z — Test Exports*/` still passing. Phase-specific checks live in the parent's requirement text.
