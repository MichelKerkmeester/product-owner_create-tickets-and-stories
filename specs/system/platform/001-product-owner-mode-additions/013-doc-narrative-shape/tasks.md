---
title: "Tasks: Doc Narrative Shape"
description: "Fifth adaptive Doc shape plus the Meta API Approval eight-doc field test."
importance_tier: "high"
contextType: "implementation"
---
<!-- SPECKIT_LEVEL: 2 -->
# Tasks: Doc Narrative Shape

- [x] T001 Add the Narrative overview template to `skill/assets/doc-templates.md`: five-shape Purpose list, "Prose Is a First-Class Citizen" cross-shape rule, full §7 NARRATIVE OVERVIEW TEMPLATE scaffold with adaptation notes, following sections renumbered 8-12.
- [x] T002 Wire the shape into `skill/references/doc-mode.md`: When to Use bullet, Step 4 shape bullet plus prose rule, §7 Narrative Overview subsection.
- [x] T003 Version bump both files 0.100 -> 0.101 and re-enumerate five shapes across SKILL.md, the kernel, root README (shape table + version table), SYNC.md and the claude project README.
- [x] T004 Re-sync: mirrors renamed to v0.101, kernel and Skill checksum rows rebuilt; verified 28/28 byte-identical, 29/29 sha16, 43/43 router fixtures.
- [x] T005 Dispatch eight fresh Sonnet 5 agents, one per Meta API Approval doc, as Doc Mode refinements with explicitly authorized structural normalization, free shape choice, fact and placeholder fidelity, no source writes, no ClickUp, mechanical read-back receipts.
- [x] T006 Validate the batch: 8/8 exports at `Product Owner/export/<original-basename>.md` with receipts matching line counts, ClickUp grammar present, zero `---` dividers, 06 checkbox states preserved (13 checked / 31 unchecked), 05 paste blocks diffed byte-identical, source mtimes prove agents read-only (working-tree changes on the folder are the user's other session).

## Field test outcomes

- Shapes chosen: Narrative overview for 00-README (55L), 01-diagnosis (169L), 02-research-findings (129L), 07-video-5-status-report (100L); Guide for 03-dashboard-setup (121L), 04-screencast-script (266L), 06-final-checklist (154L); Catalog for 05-reviewer-form-text (83L).
- Notable behaviors: 05 protected the four Meta form paste blocks verbatim and converted the working HTML comment into visible gating prose; 01 merged the redundant "At a glance" block into the ranked findings without losing its unique cross-reference; 07 restructured onto the template's four narrative beats.
- One orchestrator probe false alarm: `831870989726449` absent from the 01 export because it is absent from the 01 source.

## Readability pass (user feedback: "Structure and readability could be better")

- [x] T007 Diagnose the first-round output: spacer headings read as broken empty headings in file form, dividers flush against content, mega-paragraphs mixing topics, evidence links chained mid-sentence, checklist items grown into paragraphs. Root cause: the template scaffolds mandated maximum ClickUp grammar with no prose-density rules.
- [x] T008 Doc Mode and Doc Templates 0.101 -> 0.102: new Readability Floor (one idea per paragraph takeaway-first, links at the end of what they support, short bold-imperative checklist items, lists one level deep) and spacer headings reclassified as a ClickUp-bound affordance that file exports drop; quality checklists extended; mirrors and checksums re-verified 28/28 + 29/29, fixtures 43/43.
- [x] T009 Eight Sonnet 5 polish agents reworked the exports in place: 8/8 receipted, zero spacer headings remain, blank line after every divider (one residual in 01 fixed by the orchestrator), 06 checkboxes recounted 13/31, 05 paste blocks re-verified byte-identical, 04 kept script checklist wording verbatim over the reshape rule (correct fidelity-first judgment), sources untouched.
