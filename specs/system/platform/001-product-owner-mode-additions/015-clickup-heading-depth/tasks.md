---
title: "Tasks: ClickUp Heading Depth"
description: "H2-sparing heading ladder across Doc and Story artifacts."
importance_tier: "high"
contextType: "implementation"
---
<!-- SPECKIT_LEVEL: 2 -->
# Tasks: ClickUp Heading Depth

- [x] T001 Survey heading depths across all five artifact templates, fifteen examples and recent exports. Finding: Doc scaffolds carried 68 fence H2s and Story scaffolds 19, while Task, Bug and Interactive artifacts were already H3-only and needed no change.
- [x] T002 Canonize the ladder in doc-templates (ClickUp Markdown Contract) and doc-mode (ClickUp Output Contract plus layout checklist): H1 title only, H3 sections, H4 subsections, bold paragraph leads below, H2 reserved for rare major parts of long documents; spacer headings demoted to `###   `/`####   `.
- [x] T003 Same rule in story-templates (grammar bullets) and story-mode (validation bullets), with H2 banned outright in story artifacts.
- [x] T004 Mechanically demote all scaffolds fence-aware (H2 to H3, H3 to H4, H4 numbered rule headings to bold leads, deepest spacers removed) and all seven Doc and Story examples in place. Zero H2 remains in any scaffold or example body.
- [x] T005 Version bumps and sync: Doc Mode and Doc Templates 0.103 to 0.104, Story Mode and Story Templates 0.100 to 0.101, four mirrors renamed, seven example mirrors resynced, version tables and SYNC rows updated; verified 28/28 byte-identical, 29/29 sha16, 43/43 router fixtures.
- [x] T006 Generation verification: two fresh Sonnet agents produced export 069 (Behavior reference: H1=1, H2=0, H3=5, H4=3, bold leads deeper, zero spacers in the file export) and export 070 (Simple story: H1=1, H2=0, H3=3, 2 scenarios). Both receipted and mechanically confirmed.

## Amendment: balanced ladder (user correction)

The user rejected the flat no-H2 outcome mid-regeneration: H2 is allowed and normal for major anchors (Overview included), it just stays a minority, roughly 3-4 H2s when a document has around ten headings.

- [x] T007 Canon reworded in all four files (Doc Mode + Doc Templates 0.104 -> 0.105, Story Mode + Story Templates 0.101 -> 0.102): H2 anchors major sections and stays a minority, H3 carries the rest and the subsections under an H2 anchor, H4 deeper, bold leads below; H2-level spacers valid again.
- [x] T008 Scaffolds re-balanced by script (doc fences 14 H2 / 29 H3 / 2 H4 across five shapes, story fences 8 H2 / 4 H3 across three tiers, spacers levelled); all seven Doc and Story examples re-balanced by two agents, heading depths only.
- [x] T009 Sync green after re-balance: 28/28 mirrors, 29/29 sha16, 43/43 fixtures.
- [x] T010 Full regeneration of the nine-artifact test set under balanced canon, exports 060-068 receipted and validated: Guide 2 H2 / 9 headings, Catalog 3/13, Behavior reference 3/19, Proposal 4/15, Narrative overview 3/7, Simple story 1 H2, Medium story 3 H2 with 9 scenarios at 3 per requirement, task and bug on their own H3 canon. All fabrication traps held again; one title em dash in 062 fixed by the orchestrator.
