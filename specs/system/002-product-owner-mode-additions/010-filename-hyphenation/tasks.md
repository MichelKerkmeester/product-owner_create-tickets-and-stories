---
title: "Tasks: Filename Hyphenation"
description: "Rename every underscore filename in the Product Owner package to hyphens and rewrite all path references."
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_LEVEL: 1 -->
# Tasks: Filename Hyphenation

- [x] T001 Rename all underscore names under `Product Owner/`: twelve skill files (seven references including the `human-voice-rules.md` symlink, whose external target is untouched, plus five assets) and two directories (`z-legacy`, `export/z-archive`). Example files and mirror names were already hyphen/space based. External check confirmed no other AI system references Product Owner's files (the underscore hits elsewhere are those systems' own packages). (`Product Owner/`)
- [x] T002 Rewrite every path reference: sixteen live files updated (SKILL.md including its router resource maps and pseudocode paths, AGENTS.md, both READMEs, SYNC.md, the five mode references' cross-links, and six knowledge mirrors). The pinned Task Mode, Bug Mode and DEPTH sources changed bytes only by these reference rewrites, per the operator's package-wide directive; their mirrors and checksum rows were rebuilt accordingly. Post-scan: zero underscore paths remain (excluding `.DS_Store`), zero stale references outside the untouched archives. (`Product Owner/`)
- [x] T003 Re-sync and verify: all thirteen core mirrors re-copied from the hyphenated sources (symlink dereferenced), fifteen example mirrors refreshed, every checksum row rebuilt from final bytes. Verified: 28/28 mirrors byte-identical, 29/29 checksums match, knowledge directory holds exactly twenty-eight files, and the router fixture suite passes with the hyphenated resource paths resolving through the live filesystem glob. (`Product Owner/`)
