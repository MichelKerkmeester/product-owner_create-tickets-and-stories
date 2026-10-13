---
title: "Phase Specification: Route what people actually type"
description: "Extend the semantic tables so ordinary phrasing reaches the right mode, cutting the twenty-request fallback count from sixteen to at most four"
importance_tier: "high"
contextType: "specification"
_memory:
  continuity:
    packet_pointer: "008-router-and-skill-slimming/003-router-coverage"
    last_updated_at: "2026-09-03T00:00:00Z"
    last_updated_by: "claude"
    recent_action: "R1 implemented and verified against a held-out probe set"
    next_safe_action: "Run review-kernel to clear the sync check kernel gate"
    blockers: []
    completion_pct: 100
---
# Phase Specification: Route what people actually type

<!-- SPECKIT_LEVEL: 2 -->

---

## 1. METADATA

| Field | Value |
| --- | --- |
| Phase | 003-router-coverage |
| Parent | 008-router-and-skill-slimming |
| Requirement | R1 |
| Status | Complete |

---

## 2. SCOPE

Extend the semantic tables so ordinary phrasing reaches the right mode, cutting the twenty-request fallback count from sixteen to at most four

The parent packet holds the measured problem, the full requirement text and the risk table. This phase carries only what belongs to R1.

---

## 3. VERIFICATION

See `implementation.md` for what shipped and what it measured.

Inherited from the parent: router fixtures and the differential harness both green, the format validator and its fixtures passing, and every artifact under `export/z — Test Exports*/` still passing. Phase-specific checks live in the parent's requirement text.
