---
title: "Product Owner - Assets - Story Template - v0.100"
description: "The Barter house-format Story scaffold: a story preamble, an About umbrella with Problem, Solution, Expected outcomes and References, an optional Requirements section holding only hard constraints, a few outcome-led acceptance criteria, and an opt-in Delivery close written only on request or where the artifact forces one. Shared grammar, artifact-kind selection and the optional enrichments live in story-mode.md."
version: "0.100"
contextType: asset
importance_tier: high
trigger_phrases:
  - "story template"
  - "story scaffold"
  - "PRD house format"
  - "write a user story"
  - "story requirements section"
---

# Product Owner - Assets - Story Template - v0.100

The default shape for a Story. Detail scales with scope. The order does not change.

**Loading Condition:** CONDITIONAL, with `references/story-mode.md` when the resolved shape is Story
**Purpose:** Provides the Barter house-format Story scaffold a new Story is copied from
**Scope:** The story preamble, the About umbrella, Requirements as hard constraints only and omitted when there are none, a few outcome-led acceptance criteria and an opt-in Delivery close written only on request or where the artifact forces one
**Output Path:** `export/[###] - Story-[description].md`, or `export/[original-source-filename].md` for a refinement

---

## 1. OVERVIEW

### Purpose

Provides the Barter house-format Story scaffold: a story preamble, an About umbrella with Problem, Solution, Expected outcomes and References, Requirements holding only the hard constraints the delivery must satisfy, a few outcome-led acceptance criteria that leave the how to the developer, and an opt-in Delivery close written only on request or where the artifact forces one.

### Usage

Load this asset with Story Mode. The shared house grammar, the artifact-kind selection and the optional enrichments live in [story-mode.md](../references/story-mode.md).

---

## 2. STORY TEMPLATE

```markdown
# {Persona or platform} - {Area or initiative} - {Feature}

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
{One to three short sentences: what this story covers. Add a second paragraph only when the flow needs framing.}

### Problem
* * *
{What breaks or is missing today, or a link to the parent epic where the high-level problem is defined.}

### Solution
* * *
{Two or three sentences on the approach: what changes for the user, and why this shape of change answers the Problem. Written as a decision, not a list. Bullets only when the story bundles several distinct changes that a reader needs to tell apart, and then one line each.}

#### **Expected outcomes**
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
*   {A hard requirement: a format, limit, platform, integration or rule the delivery must satisfy}
*   {Another hard requirement in the same group}

**{Next constraint group}**
* * *
*   {Hard requirement}
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

#### {Optional surface group}
* * *
1\. **{What the user can now rely on, as a short title}**
* * *
*   **Given** {the situation the user is in}
*   **When** {what they do, or what happens}
*   **Then** {the outcome they experience and the quality it has to have, with the how left open}
*   **And** {a second outcome, only when the criterion needs it}
* * *
- [ ] _Mark as done, if the criteria are met_
* * *
##   
```

### Notes For Use

- The `#### **References**` block uses plain sub-labels (`Components`, `Flows`, `Lifecycle`), not bold. Omit any group with no supplied links. Images are embedded in ClickUp after export, so the artifact never carries an image, a screenshot reference or a file path to one
- Solution is the product decision in prose: what changes for the user and why that shape answers the Problem. It never restates the constraints that sit in Requirements or the outcomes that sit in Acceptance criteria, and it names no mechanism. If a Solution bullet could be pasted into Requirements or a criterion unchanged, it belongs there instead
- Requirements hold hard requirements only: the formats, limits, platforms, integrations, compliance rules and performance floors the delivery has to satisfy whatever approach the developer takes. Each group is a bold name, a divider and short `*   ` bullets, one constraint per bullet, stated as a fact or an instruction rather than as a user outcome. Every bullet is a sentence a build can fail, so a bullet that reports what a screen says, shows or contains, naming no value, limit, condition, effect or named flow a build could get wrong, is description and is struck rather than reworded. Never a `**Checklist**`
- Supplied hard values travel verbatim. Copy each number, size, spacing, heading level, limit, exact string and button order into a constraint bullet with its value intact, in the source's own units and notation, inside backticks. Where the source is organised per screen or surface, mirror that organisation with one bold-lead group per screen under the source's own name, and carry each screen's reuse map as a Shared with: constraint in that group. Where the source names a change without giving its content, point the constraint at the design that settles it rather than inventing the text or dropping the line. A screen the source describes in prose, or shows only in a screenshot, supplies its copy, its labels and its values, and not its layout, its composition or a paraphrase of what it communicates. Carry the strings verbatim in backticks and let the design link carry the rest
- A source line above the first heading, or for a surface no heading names, is a group of its own under that surface's name, and source hedges are rewritten as facts or open constraints rather than carried into the artifact's prose
- Requirements is optional only where there is nothing hard to hold. Omit the whole section, spacer included, when the source names no hard constraint and the acceptance criteria say everything. One supplied hard value makes the section mandatory: optionality is permission to omit an empty section, never permission to drop a value the source supplied. Never pad it with outcomes or with screen description to make it look complete. A group named for a screen the source mentioned once holds one bullet, and a group that grew past its source grew by description
- `## Delivery` is opt-in and lives in section 3 rather than in the scaffold above, because a delivery view nobody asked for reads as three `TBD...` slots pretending to be a plan. When it is absent, Acceptance criteria is the last section and keeps the close it already writes
- Acceptance criteria describe what the user can rely on once the work ships and the quality it has to have, from the product's point of view. They leave the mechanism to the developer. A criterion says playback starts at once and adapts to the connection, not which player or bitrate ladder does it
- Keep acceptance criteria few. One criterion per outcome the story exists to guarantee, plus the edges that matter. The count grows only with the number of surfaces and considerations the story touches, never with its size or the number of requirements
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
The delivery budget or expected size for the approved scope.

*   TBD...

#### Rabbit holes
* * *
Areas that could waste effort, create ambiguity or distract from the intended outcome.

*   TBD...

#### No-gos
* * *
Explicit scope exclusions and behaviors the delivery team must not introduce.

*   TBD...
* * *
```
