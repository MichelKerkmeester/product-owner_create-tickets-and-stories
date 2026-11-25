---
title: "Product Owner Design Briefing Template"
description: "Copy/apply template for Product Owner design briefings that tell the Product Design team what to design and why, with audience facets a design review can tick."
contextType: general
importance_tier: important
trigger_phrases:
  - "design briefing template"
  - "briefing for design"
  - "design briefing scaffold"
  - "product design briefing"
  - "briefing requirements facets"
version: 0.17.0.1
---

# Product Owner Design Briefing Template

Copy/apply template for Product Owner design briefings.

- **Loading Condition:** CONDITIONAL, with `references/briefing-mode.md` whenever Briefing intent is selected
- **Purpose:** Provides the design briefing scaffold a new briefing is copied from
- **Scope:** The About, Briefing and Requirements core sections, the optional link blocks and closing sections, the audience headings and the facet grammar
- **Output Path:** `export/[###] - briefing-[description].md`

---

## 1. OVERVIEW

### Purpose

Provides a reusable markdown scaffold for briefing the Product Design team on what to design and why, before a dev task exists. A briefing names the problem, the design direction and the outcomes a design review can check. How devs build it stays out, apart from the logic the Dev Handover section passes on.

### Usage

Load this asset with Briefing Mode. Title the briefing by the rule in `AGENTS.md` Section 2, Artifact Titles. Copy the template, remove optional sections that do not apply and keep the section headings, audience headings and facet labels as written. Do not end a newly authored or rewritten bullet item with a full stop.

---

## 2. DESIGN BRIEFING TEMPLATE

Worked example: [`examples/briefing/briefing-example-full.md`](examples/briefing/briefing-example-full.md) shows two apps and a design system block with every optional section, every facet type and a Why facet.

Worked example: [`examples/briefing/briefing-example-single.md`](examples/briefing/briefing-example-single.md) shows one app with no audience labels, every optional section except the Flows block, with the References and Related tasks blocks.

Worked example: [`examples/briefing/briefing-example-minimal.md`](examples/briefing/briefing-example-minimal.md) shows the smallest valid briefing, with the core sections and two facets.

```markdown
# Briefing - {App or Apps} - {Area} - {Detail}

## About
* * *
{The problem, with its data and where the data comes from}

{The decision, in one or two sentences}

## Briefing
* * *
*   {Starting point, such as a concept or screen to reuse}
*   {What changes or is dropped from that starting point, and why}
*   {What is out of scope for design, and where it goes instead}

#### **References**
* * *
*   [{Current screen, flow or concept}](figma-url)
*   `{Named concept or notification with no link}`

#### **Flows**
* * *
*   [{Board or flow name}](figjam-url)

#### **Related tasks**
* * *
*   `{Task or briefing title}`


## Requirements
* * *
#### {AUDIENCE}
* * *
**Display**
- [] {What the screen shows, written so a design review can fail it}

**{Facet}**
- [] {Requirement}


#### {NEXT AUDIENCE}
* * *
**{Facet}**
- [] {Requirement}


## Deliverables
* * *
- [] {Frame or flow, with the states to hand over}


## Copy
* * *
*   {Who writes which copy, placeholder from design or final from Copywriter}


## Open Questions
* * *
*   {A decision that is still open, and who makes it}


## Success Signal
* * *
*   {The change we expect to see, and where we will see it}


## Dev Handover
* * *
*   {Logic the dev story must carry that the design does not show}
```

### Notes For Use

- The title is `Briefing - {App or Apps} - {Area} - {Detail}`. `Briefing` is the type lead and no team leads it. Join two apps with `&`, as in `Partner & Creator`. The apps are `Partner`, `Creator` and `Backoffice`. The area names the product area in full, such as `Barter Deals`, never `Deals`. A briefing that changes no app screen uses `Design System`. A design system block inside an app briefing does not enter the title
- About, Briefing and Requirements are required. Every other section is optional and is removed whole when it does not apply, never left with a placeholder
- About holds the problem and the decision. Give the data with its source and period, such as `Since July, about 3,000 deals`. Never write a number the source does not give
- Briefing holds the design direction: the starting point, what is reused and what is dropped with its reason. It also says what design leaves alone. It never restates the About decision or a requirement. A line a design review could tick belongs in Requirements
- When Briefing marks something out of scope, its bullet names where it goes, such as `and is listed under Dev Handover`, and the items themselves sit only in that section
- `#### **References**`, `#### **Flows**` and `#### **Related tasks**` hang under Briefing, in that order. Flows lists the FigJam boards or flows that go with the briefing, with the board name as link text. A name with no link is a backticked bullet, never a made-up URL
- Under Requirements, add an ALL-CAPS audience heading, `#### PARTNER`, `#### CREATOR`, `#### BACKOFFICE` or `#### DESIGN SYSTEM`, only when the briefing has two or more audiences. A single audience starts straight on its first facet
- Each facet is a bold lead line with `- []` items under it. No numbered groups, no prose under a facet and no User Story. Use the facet names below when one fits, in this order, and name a new facet for the thing it checks when none does
- `**Display**` is what the screen shows and how it reads, and every audience with a screen has one
- `**Validation**` is what blocks the user and how the error behaves, used when a field becomes required or gains limits
- `**Existing {Records}**`, such as `**Existing Deals**`, is how data saved before the change behaves when it is shown or edited
- `**{State}**`, such as `**Reach Paused**`, is one facet per named state the change adds, with when it starts, what it shows and when it clears
- `**Notification & Email**` covers messages the change sends, rewrites or retires. Name an existing notification by its catalog title in backticks
- `**Visibility**` is when an element shows or hides, with the condition as a value
- `**Contrast**` is readability over the backgrounds an element sits on, used for visual system changes
- Under `#### DESIGN SYSTEM`, a facet may name a component group, such as `**Partner Form Components**`, and `**Cleanup**` lists layers or components to remove. A `**Why**` facet with `*   ` bullets may follow when the team needs the reason for a component trade-off beside it. It is the one facet without checkboxes
- Deliverables lists the frames and states design hands over, such as empty, filled and error. Add it when the states are not plain from Requirements or when one change spans several screens. Never repeat a requirement there
- Copy says who writes which copy. Copy rules, such as `never a limit`, stay in Requirements
- Open Questions holds what is still undecided, and Briefing holds what is settled. Name who decides when it is not plain. Before adding a question, check that Requirements does not already answer it
- Success Signal names the change we expect to see after release and where it shows. Add it when About carries data to compare against. Leave it out of a pure visual or design system change
- Dev Handover lists the logic the dev story must carry that no frame shows, such as feed rules, thresholds and counts. It is for the PO writing that story, so it comes last
- Requirements and Deliverables use `- []`. Every other list uses `*   `
- Spacing: one blank line separates About, Briefing, the link blocks and the facets. Two blank lines go before Requirements, before every audience heading after the first and before every section that follows Requirements, so the sections read apart in ClickUp
- A `* * *` divider sits directly under every heading and nowhere else. A paragraph directly above `* * *` imports into ClickUp as a heading
- The section headings, the ALL-CAPS audience headings and the Title Case facet labels are this shape's own labels. The briefing keeps them as written, and a heading case rule in another shape does not rename them. Human Voice Rules sentence case covers every other heading and label in the briefing
- Write no markdown tables. A numbered title, if one is ever needed, is written `1\. **{Title}**`
- Wrap every file name and every component or layer name in backticks, such as `Form | Location`, so ClickUp does not auto-link a file name and the name reads as a literal
- Pushed to ClickUp, each `- []` is sent as `- [ ]` so it imports as a checkbox. The export keeps `- []`
- Do not end a bullet or checklist item with a full stop
