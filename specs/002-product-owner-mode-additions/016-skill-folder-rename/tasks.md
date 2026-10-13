---
title: "Tasks: Skill Folder Rename + Skill README"
description: "sk-product-owner rename, reference sweep and create-skill README."
importance_tier: "high"
contextType: "implementation"
---
<!-- SPECKIT_LEVEL: 2 -->
# Tasks: Skill Folder Rename + Skill README

- [x] T001 Alignment sweep from the same turn: single-group numbering rule into task-mode.md (0.301 -> 0.302), balanced heading ladder into SKILL.md's ClickUp contract summary and quality gate, and into the root README grammar description. Kernel, DEPTH, bug and interactive surfaces checked clean.
- [x] T002 Folder renamed `skill/` -> `sk-product-owner/`; the human-voice-rules symlink survives (same relative depth). Frontmatter `name: product-owner` deliberately kept as a separate contract.
- [x] T003 98 path references rewritten across AGENTS.md, SYNC.md, both READMEs and SKILL.md's router pseudocode, with a pattern that excluded `skills/` so mcp-tooling paths stayed intact. Zero residual references verified.
- [x] T004 Sync green post-rename: 30/30 mirrors byte-identical, 31/31 sha16 (two stale rows caught and fixed), 43/43 router fixtures re-extracted from the new path.
- [x] T005 `sk-product-owner/README.md` authored per create-skill's standalone skill README template (agent chose the correct template over the thinner hub-packet style). Orchestrator fixes on validation: the wrong symlink-skipped claim corrected to mirrored-dereferenced, the 3-column troubleshooting table reshaped to 2 columns, semicolons removed from the DEPTH sentence and table cells.
- [x] T006 README rewritten far more descriptive at the user's request, modeled on the Public repo root README's mechanisms: value table plus reasons-to-trust opener, problem-story overview, ASCII routing pipeline diagram, one descriptive section per mode, a safety-model section (source classes, fidelity, receipts, ClickUp consent), output-format and examples-library sections, an objection-handling FAQ and an expanded troubleshooting table. Ten sections, ~280 lines, 2-column tables and HVR held throughout.
- [x] T007 Second revision on user feedback ("section 1 doesn't make sense, wrong diagram styling, more detail on modes, output format, ClickUp"): the abstract problem-story overview replaced with a concrete what-this-is (folder anatomy, bootstrap path), the diagram redrawn in the repo's box-drawing style (┌─┐ │ ▼ arrows), and the weight shifted from marketing narrative to reference detail: per-mode sections now carry template/tier/shape tables and structure rules, the output-format section shows a live grammar snippet plus heading-ladder and readability-floor detail, and ClickUp got its own section with the transport parameter table, push shape and failure symptom. Eleven sections.
