---
title: "Receipt: Motivation stories aligned to the PRD opening restructure"
description: "Six export/Motivation stories rewritten to the 034 house opening (About narrative, Problem, Solution, References, Expected Outcomes) with product outcomes added; all requirements, checklists, acceptance criteria and Definition of Done blocks preserved verbatim."
contextType: "reference"
---

# Receipt: Motivation stories aligned to the PRD opening restructure

Applied 2026-08-10. Scope: the six `AI Systems/Product Owner/export/Motivation/` stories. These files are untracked in git (export deliverables), so this receipt is the change record.

## Stories aligned

- `FE - Creator - Barter deal - Application - Flow & Voice Messages.md`
- `FE - Creator - Barter deal - Improved Presentation.md`
- `FE - Creator - My Barters - Motivation - Voice Messages.md`
- `FE - Partner - Barter deal - Motivation - Settings.md`
- `FE - Partner - Barter deal - Target Platform & Form Updates.md`
- `FE - Partner - Side Panel - Motivation - Voice Messages.md`

## What changed

- Opening rebuilt to the 034 house shape: `## About` narrative (the User Story promise folded into prose, block removed), `### Problem`, `### Solution`, `### References` (Spec/Figma/Screenshots link groups), and a new `### Expected Outcomes` section per story (product outcomes)
- Major sections promoted to H2 (`## Requirements`, `## Acceptance criteria`), opening groups at H3, requirement names to H4-bold (`#### **Name**`), Definition of Done to H4-bold
- Acceptance criteria retitled from escaped `**1\. Name**` to the house numbered form `1. **Name**`; `* * *` dividers, `*   ` bullets and `##   ` spacers normalized
- The Target Platform story's open design question blockquote preserved verbatim

## Preserved verbatim

All requirement prose leads, build checklists (110 `- [ ]` items), Given/When/Then acceptance criteria (32 across the six stories, each with its Mark-as-done checkbox), Definition of Done items, links, identifiers (`5:7`, `Optional`/`Required`, `Input | Select`, `send_window`-style tokens) and status labels.

Follow-up refinements after the initial alignment (owner-directed, same session):

- Improved Presentation: Solution made concise and purpose-led (judge the opportunity at a glance); deal-presentation distinction updated — Local deals show a map, Online deals show the company logo in the header (if present); map tap opens Google Maps or the iOS location modal; the two detail requirements merged into a single `#### Deal details` requirement covering location, availability, platforms and conditions (target audience, motivation, creator limit) — everything between the application status and the About section; acceptance criteria consolidated from 8 to 4, one per requirement (Hero lightbox, Header and status, Deal details, Lower sections)
- Application - Flow & Voice Messages: ticket now leads with the motivation step redesign and the three-format toolbar (About, Solution and Requirements reordered)
- Motivation - Settings: cross-references the deal page, the application flow and the partner preview form as display surfaces; gained acceptance criterion 3 (every surface reads the stored setting) and a `#### Dependencies` block naming the three surfaces and their non-blocking status

## Verification

- Structure grep: each story has exactly one Problem / Solution / References / Expected Outcomes, one `## Requirements`, one `## Acceptance criteria`
- Zero old-shape markers (`**Problem**`, `**Solution**`, `**User Story**`, `**Documentation**`, `### Requirements`, `### Acceptance criteria`, escaped `1\.` AC numbers)
- Zero stray `- ` bullets (110 hyphen lines, all `- [ ]` checklists)
- AC count per story: 12 / 8 / 4 / 2 / 4 / 2, matching the pre-change reads; read-back verified non-empty for all six files
