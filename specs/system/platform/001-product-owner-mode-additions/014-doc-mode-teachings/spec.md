---
title: "014 - Doc Mode Teachings [002-product-owner-mode-additions/014-doc-mode-teachings/spec]"
description: "The user wants Doc Mode (and the other modes a tiny bit) to learn from three strong documentation sources in the Public repo: the root README (tone and structure exemplar), the ..."
importance_tier: "normal"
contextType: "general"
---
# 014 - Doc Mode Teachings

## Problem

The user wants Doc Mode (and the other modes a tiny bit) to learn from three strong documentation sources in the Public repo: the root README (tone and structure exemplar), the sk-doc create-readme packet (authoring contract) and the sk-doc shared backbone (quality control).

## Approach

Three-model independent review panel, identical brief, read-only:

- GPT 5.6 Sol (high, fast) via cli-opencode → `report-sol.md`
- GLM 5.2 (max) via cli-opencode → `report-glm.md`
- Fable 5 (high) via the claude2 second-account Claude CLI in plan mode, per explicit user instruction to dispatch rather than answer natively → `report-fable-5.md`

The brief pinned the invariants (ClickUp grammar, source-safety classes, HVR, dual-packaging sync cost, 2-column tables, v0.102 Readability Floor) and demanded mechanisms with file locations, honest gap analysis in both directions, implementation-ready recommendations and an explicit do-not-import list.

## Outcome

`synthesis.md` holds the convergence map, the unanimous do-not-import list, the one genuine conflict (example table widths vs the phase-001 fixture exemption) and a three-wave implementation order. Two stale-enumeration defects found by the panel were verified and fixed immediately; the recommendations themselves await the owner's selection.
