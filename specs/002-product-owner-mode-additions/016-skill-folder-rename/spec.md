---
title: "016 - Skill Folder Rename + Skill README [002-product-owner-mode-additions/016-skill-folder-rename/spec]"
description: "The CLI packaging lived at Product Owner/skill/, a generic name, and the folder had no README for a developer browsing it. The user wants the folder renamed to sk-product-owner ..."
importance_tier: "normal"
contextType: "general"
---
# 016 - Skill Folder Rename + Skill README

## Problem

The CLI packaging lived at `Product Owner/skill/`, a generic name, and the folder had no README for a developer browsing it. The user wants the folder renamed to `sk-product-owner` (matching the repo's sk-* skill naming), every reference updated, and a skill README authored per sk-doc's create-skill conventions.

## Changes

- `Product Owner/skill/` renamed to `Product Owner/sk-product-owner/`. The `human-voice-rules.md` symlink survives unchanged (same depth, still resolves).
- 98 path references rewritten across AGENTS.md (33), SYNC.md (26), claude project/README.md (18), root README.md (14) and SKILL.md itself (7, including the router pseudocode). The replacement pattern excluded `skills/` so mcp-tooling packet paths stayed intact. Zero residual references verified.
- The skill's frontmatter `name: product-owner` was deliberately kept: the user asked for a folder rename, and the invocation name is a separate contract.
- Task Mode 0.301 -> 0.302 rode along (single-group numbering rule from the same session).
- Sync green after rename: 30/30 mirrors byte-identical, 31/31 sha16, 43/43 router fixtures (re-extracted from the renamed path).
- `sk-product-owner/README.md` authored per create-skill conventions (repo-side documentation, not a knowledge mirror).

## Alignment sweep (same turn, recorded here)

The single-group numbering rule and balanced heading ladder were propagated to the remaining canon surfaces: task-mode.md Requirement Item Standard, SKILL.md's ClickUp contract summary and quality gate line, and the root README's grammar description.
