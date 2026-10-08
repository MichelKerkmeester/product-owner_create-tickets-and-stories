---
title: "Product Owner - Assets - Story Template"
description: "The Barter house-format Story scaffold: a Problem section of three to five sentences, a Solution with Expected outcomes and References, an optional Requirements section holding only hard constraints, a few outcome-led acceptance criteria, and an opt-in Delivery close written only on request or where the artifact forces one. Shared grammar, artifact-kind selection and the optional enrichments live in story-mode.md."
contextType: general
importance_tier: important
trigger_phrases:
  - "story template"
  - "story scaffold"
  - "PRD house format"
  - "write a user story"
  - "story requirements section"
version: 0.17.0.11
---

# Product Owner - Assets - Story Template

The default shape for a Story. Detail scales with scope. The order does not change.

**Loading Condition:** CONDITIONAL, with `references/story-mode.md` when the resolved shape is Story
**Purpose:** Provides the Barter house-format Story scaffold a new Story is copied from
**Scope:** The Problem and Solution opening, Requirements as hard constraints only and omitted when there are none, a few outcome-led acceptance criteria and an opt-in Delivery close written only on request or where the artifact forces one
**Output Path:** `export/[###] - Story-[description].md`, or `export/[original-source-filename].md` for a refinement

---

## 1. OVERVIEW

### Purpose

Provides the Barter house-format Story scaffold: a Problem section of three to five sentences, a Solution with Expected outcomes and References, Requirements holding only the hard constraints the delivery must satisfy, a few outcome-led acceptance criteria that leave the how to the developer, and an opt-in Delivery close written only on request or where the artifact forces one.

### Usage

Load this asset with Story Mode. The shared house grammar, the artifact-kind selection and the optional enrichments live in [story-mode.md](../references/story-mode.md).

---

## 2. STORY TEMPLATE

```markdown
# {Persona or platform} - {Area or initiative} - {Feature}

* * *
## Problem
* * *
{Three to five sentences, one paragraph, on the business problem: what breaks or is missing today, who it costs and why it matters to the business.}
* * *
##   

## Solution
* * *
{Two or three sentences on the approach: what changes for the user, and why this shape of change answers the Problem. Written as a decision, not a list. Bullets only when the story bundles several distinct changes that a reader needs to tell apart, and then one line each.}

**Expected outcomes**
* * *
*   {Result for users or the business}
*   {Result for users or the business}

#### **References**
* * *
{Supplied links only, grouped under plain labels. Omit the whole section when none are supplied.}
Components
*   [Page | {name}]({url})
Flows
*   [{Flow}]({url})
Lifecycle
*   [{link}]({url})
##   

## Requirements
* * *
**{Constraint group, such as Video format or Data retention}**
* * *
- [] {A hard requirement: a format, limit, platform, integration or rule the delivery must satisfy}
- [] {Another hard requirement in the same group}

**{Next constraint group}**
* * *
- [] {Hard requirement}
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

#### {Optional surface group}
* * *
1 ) **{What the user can now rely on, as a short title}**
* * *
*   **Given** {the situation the user is in}
*   **When** {what they do, or what happens}
*   **Then** {one outcome they experience and the quality it has to have, with the how left open}
*   **And** {a second outcome, on its own line rather than joined to the Then line with "and"}
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   
```

### Notes For Use

- The `#### **References**` block uses plain sub-labels (`Components`, `Flows`, `Lifecycle`), not bold. Omit any group with no supplied links. Images are embedded in ClickUp after export, so the artifact never carries an image, a screenshot reference or a file path to one
- Solution is the product decision in prose: what changes for the user and why that shape answers the Problem. It never restates the constraints that sit in Requirements or the outcomes that sit in Acceptance criteria, and it names no mechanism. If a Solution bullet could be pasted into Requirements or a criterion unchanged, it belongs there instead. `**Expected outcomes**` closes Solution as a bold label with a `* * *` divider under it, never as a heading, because the outcomes belong to Solution rather than standing as a section of their own
- Problem opens the Story with no intro lines above it. It states the business problem in three to five sentences, one paragraph: what breaks or is missing today, who it costs and why it matters to the business. It names no solution and links no parent epic in place of the prose. This paragraph is the one exception to the three-sentence paragraph cap
- Requirements hold hard requirements only: the formats, limits, platforms, integrations, compliance rules and performance floors the delivery has to satisfy whatever approach the developer takes. Each group is a bold name, a divider and short `- []` checklist items, one constraint per item, stated as a fact or an instruction rather than as a user outcome or a build step. Every item is a sentence a build can fail, so an item that reports what a screen says, shows or contains, naming no value, limit, condition, effect or named flow a build could get wrong, is description and is struck rather than reworded. Never a `**Checklist**` label, and never `[ ]` with a space
- Supplied hard values travel verbatim. Copy each number, size, spacing, heading level, limit, exact string and button order into a constraint item with its value intact, in the source's own units and notation, inside backticks. Where the source is organised per screen or surface, mirror that organisation with one bold-lead group per screen under the source's own name, and carry each screen's reuse map as a Shared with: constraint in that group. Where the source names a change without giving its content, point the constraint at the design that settles it rather than inventing the text or dropping the line. A screen the source describes in prose, or shows only in a screenshot, supplies its copy, its labels and its values, and not its layout, its composition or a paraphrase of what it communicates. Carry the strings verbatim in backticks and let the design link carry the rest
- A source line above the first heading, or for a surface no heading names, is a group of its own under that surface's name, and source hedges are rewritten as facts or open constraints rather than carried into the artifact's prose
- Requirements is optional only where there is nothing hard to hold. Omit the whole section, spacer included, when the source names no hard constraint and the acceptance criteria say everything. One supplied hard value makes the section mandatory: optionality is permission to omit an empty section, never permission to drop a value the source supplied. Never pad it with outcomes or with screen description to make it look complete. A group named for a screen the source mentioned once holds one item, and a group that grew past its source grew by description
- `## Delivery` is opt-in and lives in section 3 rather than in the scaffold above, because a delivery view nobody asked for reads as three `TBD...` slots pretending to be a plan. When it is absent, Acceptance criteria is the last section and keeps the close it already writes
- Acceptance criteria describe what the user can rely on once the work ships and the quality it has to have, from the product's point of view. They leave the mechanism to the developer. A criterion says playback starts at once and adapts to the connection, not which player or bitrate ladder does it
- Keep acceptance criteria few. One criterion per outcome the story exists to guarantee, plus the edges that matter. The count grows only with the number of surfaces and considerations the story touches, never with its size or the number of requirements
- One outcome per Then or And line. When a Then line would join two outcomes with "and", the second outcome moves to its own `*   **And**` line, and so does each outcome after it: "the list sorts by rating ascending, and the sort control shows Rating as active" becomes a Then line and an And line. An "and" inside one outcome stays, as in "name and email" or "Terms and Conditions"
- Surface groups (`#### {Group}`) are optional: add them only when the story spans two or more surfaces and each carries its own criteria (for example `#### Upload`, `#### Playback`). A short story keeps a flat numbered list
- The Mark-as-done checkbox is the final line of each criterion block. Start the next criterion after one blank line and no divider. The last criterion in the section is the exception: a `* * *` closes Acceptance criteria on the line above the `##   ` spacer, which is what the house Story does

---

## 3. OPTIONAL DELIVERY CLOSE

Append this block only when the requester asked for a delivery view, or when a requirement carries an `**Open:**` line or an undated external constraint forces one. Otherwise the scaffold above is the whole artifact and its trailing `##   ` spacer is the last line of the file.

```markdown
## Delivery
* * *
#### Estimation
* * *
*   TBD...

#### Rabbit holes
* * *
*   TBD...

#### No-gos
* * *
*   TBD...
* * *
```
