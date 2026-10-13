---
title: "017 - SKILL.md Alignment + Advisor Metadata [002-product-owner-mode-additions/017-skill-md-alignment/spec]"
description: "sk-product-owner/SKILL.md had grown to ~1190 lines by accretion: four separate Python fences with decorative dicts nothing executed, routing rules stated three ways in prose, an..."
importance_tier: "normal"
contextType: "general"
---
# 017 - SKILL.md Alignment + Advisor Metadata

## Problem

`sk-product-owner/SKILL.md` had grown to ~1190 lines by accretion: four separate Python fences with decorative dicts nothing executed, routing rules stated three ways in prose, and long duplication of content the mode references already own. The user wants it aligned with sk-doc's create-skill standard, shorter, with an improved router, plus the companion JSONs the system-skill-advisor expects. The same batch of requests covered a README symlink at the package root and a SYNC.md restructure to sk-doc standards.

## Changes

- `SKILL.md` rewritten by a fresh Sonnet agent against the create-skill section standard: keywords comment, seven numbered ALL-CAPS sections, 1188 -> 741 lines. The router consolidated into one executable Python fence (dropping the never-referenced `INTENT_MODEL`, `ENERGY_MODEL`, `FALLBACK_CHAINS` and `DOCUMENT_MAP` decoration) and one nine-step detection sequence in prose. The 741 floor is honest: the executable router the regression suite exercises is ~450 lines and cannot leave SKILL.md.
- Behavior parity proven twice: the agent ran the 43-check suite to zero failures and the orchestrator re-ran it independently after handoff.
- `description.json` and `graph-metadata.json` created in the leaf-skill shape observed in siblings, modeling the five intents, commands, ClickUp handoff and DEPTH/HVR vocabulary.
- Version cascade to v0.5.0: SKILL frontmatter, mirror renamed to `Product Owner - System - Skill - v0.5.0.md`, kernel alignment line, SYNC pins, claude project manifest rows and the skill README frontmatter. Verified 30/30 mirrors byte-identical, 31/31 sha16.
- Package root: `README.md` replaced (user pre-deleted the old package guide, user-confirmed) by a relative symlink to `sk-product-owner/README.md`, and the skill README's self-referential related-documents row removed.
- `SYNC.md` restructured to sk-doc standards: frontmatter, tagline, eight numbered sections with dividers, a When to Sync section, a Related Documents table, the stale four-shapes drift check corrected to five and the balanced heading ladder added to parity and fixture checks.
