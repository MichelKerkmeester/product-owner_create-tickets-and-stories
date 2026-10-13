---
title: "015 - ClickUp Heading Depth [002-product-owner-mode-additions/015-clickup-heading-depth/spec]"
description: "Product Owner artifacts use H2 for every section, and ClickUp renders H2 very large. The user wants H2 used sparingly, with H3, H4 and bold text carrying normal structure."
importance_tier: "normal"
contextType: "general"
---
# 015 - ClickUp Heading Depth

## Problem

Product Owner artifacts use H2 for every section, and ClickUp renders H2 very large. The user wants H2 used sparingly, with H3, H4 and bold text carrying normal structure.

## Decision

New artifact heading ladder, canon in the Doc and Story ClickUp contracts: H1 is the title only, section headings default to H3, subsections to H4, and bold paragraph leads replace anything deeper. H2 is reserved for the few genuinely major parts of a long document and is nothing in a story. Spacer headings follow the demoted levels (`###   `, `####   `). Task, Bug and Interactive artifacts already used H3-only structure and needed no change.

## Changes

- `skill/assets/doc-templates.md` 0.103 -> 0.104: heading-depth rule in the ClickUp Markdown Contract, spacer rule reworded, all five shape scaffolds demoted (H2 -> H3, H3 -> H4, H4 numbered rule headings -> bold paragraph leads), Quick and conflict-hold scaffolds included.
- `skill/references/doc-mode.md` 0.103 -> 0.104: contract bullet, spacer bullet reworded, layout checklist item.
- `skill/assets/story-templates.md` 0.100 -> 0.101: grammar bullet updated to `###   ` spacers plus a heading-depth bullet, all three tier scaffolds demoted (shared-concept H4 headings -> bold leads).
- `skill/references/story-mode.md` 0.100 -> 0.101: grammar validation bullet updated, heading-depth validation bullet added.
- Seven examples demoted in place (4 doc, 3 story), titles unchanged, mirrors resynced.
- Verification: 28/28 mirrors byte-identical, 29/29 sha16, 43/43 router fixtures, plus a two-agent generation test (one doc, one story) confirming emitted artifacts use the new ladder.
