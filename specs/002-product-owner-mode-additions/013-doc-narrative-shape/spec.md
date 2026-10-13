---
title: "013 - Doc Narrative Shape + Meta API Approval Field Test [002-product-owner-mode-additions/013-doc-narrative-shape/spec]"
description: 'The user finds Doc Mode output too much of a "logic glossary and overview": heavy label-bullet blocks, structure-first register. Doc Mode had four adaptive shapes (Guide, Catalo...'
importance_tier: "normal"
contextType: "general"
---
# 013 - Doc Narrative Shape + Meta API Approval Field Test

## Problem

The user finds Doc Mode output too much of a "logic glossary and overview": heavy label-bullet blocks, structure-first register. Doc Mode had four adaptive shapes (Guide, Catalog, Behavior reference, Proposal) and no prose-first shape for READMEs, statuses, investigation logs and handovers.

## Decision

1. Add a fifth adaptive shape, **Narrative overview**: README-style, prose-first, sections ordered by how the reader builds understanding, sparse earned structure, checklists only on open items.
2. Add a cross-shape rule, **Prose Is a First-Class Citizen**: label-bullet blocks serve genuinely enumerable content, never replace explanation.
3. Field-test with 8 fresh Sonnet 5 agents refining the real Meta API Approval working docs (`z — Context/Documentation/Content Gallery/Meta API Approval/00–07`) through Doc Mode refinement with explicitly authorized structural normalization. Sources untouched; artifacts land in `Product Owner/export/<original-basename>.md`.

## Version changes

- `skill/references/doc-mode.md` 0.100 → 0.101 (When to Use bullet, Step 4 shape bullet + prose rule, §7 Narrative Overview subsection)
- `skill/assets/doc-templates.md` 0.100 → 0.101 (five-shape Purpose list, Prose Is a First-Class Citizen section, §7 NARRATIVE OVERVIEW TEMPLATE, renumber 8–12)
- Surfaces updated: SKILL.md, kernel Custom Instructions.md, root README.md, SYNC.md, claude project README.md
- Mirrors renamed to v0.101; sync verified 28/28 byte-identical, 29/29 sha16; router fixtures 43/43

## Field test protocol

Each agent: bootstrap PO identity (AGENTS.md → SKILL.md → doc-mode.md → doc-templates.md), refine one source doc, choose the best-fitting shape (Narrative overview expected for 00, 01, 07), preserve every fact/identifier/URL/placeholder/status, never modify the source, no ClickUp, export with mechanical read-back receipt (`Verified: read-back succeeded; N lines`).
