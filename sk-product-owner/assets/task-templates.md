---
title: "Product Owner Task Templates"
description: "Copy/apply templates for Product Owner standalone tasks, parent tasks, subtasks, quick tasks, feedback tickets and design briefings."
contextType: general
importance_tier: important
trigger_phrases:
  - "task templates"
  - "standalone task template"
  - "parent task template"
  - "subtask template"
  - "quick task template"
  - "feedback ticket template"
  - "design briefing template"
  - "briefing for design"
version: 0.17.0.9
---

# Product Owner Task Templates

Copy/apply templates for Product Owner task deliverables.

- **Loading Condition:** CONDITIONAL, with `references/task-mode.md` whenever Task intent is selected
- **Purpose:** Provides the canonical task, parent task, subtask, quick task, feedback ticket and design briefing scaffolds a new task artifact is copied from
- **Scope:** The six task shapes, the sections each one requires and the numbered requirement-group grammar
- **Output Path:** `export/[###] - task-[description].md`, or the existing task filename on a source sync

---

## 1. OVERVIEW

### Purpose

Provides reusable markdown scaffolds for standalone tasks, parent tasks, subtasks, quick tasks, feedback tickets and design briefings.

### Usage

Load this asset with Task Mode. Copy the matching template, remove optional sections that do not apply and preserve source structure when the user asks for sync or refinement.

---

## 2. CANONICAL TASK TEMPLATE

Worked example: [`examples/task/task-example-ui-refinement.md`](examples/task/task-example-ui-refinement.md) shows the full task shape applied to design-parity work, with functional scope protected and accessibility verification included.

```markdown
# {Team} - {App} - {Area} - {Detail}

## About

---

{1-3 short paragraphs describing the task, why it matters and what outcome it should create.}

**References**

---

Flows

- [{Flow name}](figma-url)

Page

- [{Page name}](figma-url)

Components

- [{Component name}](figma-url)

**Epic**

---

- `{Epic name}`

**Story**

---

- [{Story H1}](<[###] - Story-[description].md>)

**Parent task**

---

- [{Parent task title}](url)

**Related tasks**

---

- [{Related task title}](url)

**Related tickets**

---

- [{Related ticket}](url)

### Requirements

---

### **{Category Name}**

---

1\. **{Item Title}**

---

{1-2 short paragraphs describing the expected outcome and why it matters.}

**Checklist**

- [] {Actionable requirement}
- [] {Actionable requirement}

**User Story**

- **Given:** {context}
- **When:** {action}
- **Then:** {outcome}

---

2\. **{Item Title}**

---

{1-2 short paragraphs describing the expected outcome and why it matters.}

**Checklist**

- [] {Actionable requirement}
- [] {Actionable requirement}

---

### **{Next Category Name}**

---

3\. **{Item Title}**

---

{Short description.}

**Checklist**

- [] {Actionable requirement}
- [] {Actionable requirement}

```

### Notes For Use

- Title the task by the rule in `AGENTS.md` Section 2, Artifact Titles. A task or subtask leads with its team and a parent task with its app. A team the source does not name is asked for or left out
- Remove any optional section that does not apply
- If the user provides source content, preserve it and only normalize what the user asked to normalize
- When the task shares behavior with sibling tasks, add `Related tasks`
- A parent task, related task, ticket or epic that was named but not linked keeps its own bullet as backticked plain text, `` - `{Task title}` ``, the same shape `**Epic**` uses above. Never fabricate a URL to complete the link, and never move a named parent into About prose because no link was supplied
- A Task in a Story bundle follows the task path and Story-link contract in Story Mode Section 7. Omit `**Story**` for a task that belongs to no Story
- Do not end a newly authored or rewritten bullet item with a full stop

---

## 3. PARENT TASK TEMPLATE

Use this when one parent task coordinates several subtasks.

Worked example: [`examples/task/task-example-standard-feature.md`](examples/task/task-example-standard-feature.md) shows shared feature scope stated once while independent child tasks retain their own implementation detail. A design token release with one subtask per app lives in [`examples/task/task-example-ds-variables.md`](examples/task/task-example-ds-variables.md): the full change list stated once in the parent, in the ClickUp format the team ships.

```markdown
# {App} - {Initiative} - {Area}

## About

---

{Short overview of the initiative and why the subtasks exist.}

**References**

---

Flows

- [{Flow name}](figma-url)

### Requirements

---

1\. **{Subtask Name}**

---

[{Subtask Title}](url)

2\. **{Subtask Name}**

---

[{Subtask Title}](url)

3\. **{Subtask Name}**

---

[{Subtask Title}](url)

```

---

## 4. SUBTASK TEMPLATE

Use this when the work belongs to a larger parent task.

Worked example: [`examples/task/task-example-subtask.md`](examples/task/task-example-subtask.md) shows a bounded child task that separates zero-result recovery from request failure without leaking permission state. Subtasks split by platform live in [`examples/task/task-example-ds-variables.md`](examples/task/task-example-ds-variables.md): each carries only its own token file and the checks that file needs, under a parent that holds the shared change list.

```markdown
# {Team} - {App} - {Area} - {Detail}

## About

---

{1-2 short paragraphs describing this subtask's scope within the parent task.}

**References**

---

Components

- [{Component name}](figma-url)

### Requirements

---

### **{Area Name}**

---

1\. **{Item Title}**

---

{Short description.}

**Checklist**

- [] {Actionable requirement}
- [] {Actionable requirement}

```

---

## 5. QUICK TASK TEMPLATE

Use this for direct small updates when the request is explicit.

Worked example: [`examples/task/task-example-quick.md`](examples/task/task-example-quick.md) shows exact replacement copy, a zero-day edge and an explicit no-layout-change boundary in the compact shape.

```markdown
# {Team} - {App} - {Area} - {Detail}

## About

---

{Brief explanation of the change and why it matters.}

### Requirements

---

**{Item Title}**

---

{Short description.}

**Checklist**

- [] {Actionable requirement}
- [] {Actionable requirement}

```

Number requirement groups only when the task carries two or more. A single group keeps its bold title without a number, as above. The moment a second group appears, number them `1\. **{Title}**`, `2\. **{Title}**` in order. The backslash before the full stop keeps ClickUp from reading each title as a new numbered list, which restarts every group at 1 because the dividers between groups end the list.

---

## 6. FEEDBACK TICKET TEMPLATE

Use this for one round of product review feedback on a feature, such as a design QA pass or an acceptance round. One ticket holds one app and one kind of feedback: `Logic` for behavior and flow, `UI/UX` for visual and interaction detail. A round that covers two apps and both kinds becomes four tickets, and an app or kind with no items gets no ticket.

Worked example: [`examples/task/task-example-feedback.md`](examples/task/task-example-feedback.md) shows a UI/UX ticket with grouped items, a Code and Figma screenshot pair and a Code-only pair for an item with no Figma frame.

```markdown
# {Team} - {Feature} - Feedback #{Round} - {App}: {Logic | UI/UX}

## About

---

Feedback from Round #{Round} of product review on {Feature} ({App}).
{This feedback is release blocking. | This feedback is not release blocking.}

#### **References**

---

**Flows**

---

*   [{Flow name}](figma-url)

###   

## Feedback

---

### **{Screen or Area}**

---

1\. **{Item Title}**

---

{One or two sentences on what is wrong now, measured against Figma or the expected behavior.}

**Checklist**

- [] {Actionable fix}
- [] {Actionable fix}

Code
![]({built-screen screenshot url})

[Figma](figma-frame-url)
![]({figma frame screenshot url})

###   

### **{Next Screen or Area}**

---

2\. **{Item Title}**

---

**What happened?**

1. {Step}
2. {Step}
3. {What went wrong}

**Checklist**

- [] {Expected behavior, written as the fix}

Recording
[{recording url}]({recording url})
```

### Notes For Use

- The title names the team, the feature, the round, the app and the kind, in that order. The Barter Managed tickets read `BM - Chat Prompts MVP - Feedback #1 - Partner: UI/UX`
- About states the round and the feature in one line and whether the feedback blocks the release in a second line. Use the release line the requester gives, and ask when it is missing
- `#### **References**` is optional. Use it for the Figma flows the reviewer worked from, and close it with a `###   ` spacer heading
- `## Feedback` replaces `### Requirements`. Group items under `### **{Screen or Area}**` headings when the ticket covers more than one screen. A ticket with one area keeps its items flat
- Number items across the whole ticket, never per group, written `1\. **{Title}**` with the full stop escaped. A number the reviewer gave stays as given, gaps included
- A short description is optional. Write it when the checklist alone does not show what is wrong now
- Every item has a `**Checklist**`. Write each line as the fix or the expected result, never as the complaint. A reviewer's question stays a question when the decision is open, such as `Can the field validate the link format?`
- A Logic item may add `**What happened?**` with numbered steps, a `Note:` with bullets and a `Recording` link. A UI/UX item names the design token, component layer or value the fix needs, in backticks
- A screenshot pair is a `Code` line and a `Figma` line, each above its images, with the Figma frame link on the `Figma` label when the reviewer gave one. Keep the pair in that order. A doc page push sets the pair side by side in columns. Leave out a side with no screenshot, and never write a placeholder image
- Put `###   ` before each group heading after the first, so the groups read apart in ClickUp

---

## 7. DESIGN BRIEFING TEMPLATE

Use this to brief the Product Design team on what to design and why, before a dev task exists. A briefing names the problem, the design direction and the outcomes a design review can check. How devs build it stays out, apart from the logic the Dev Handover section passes on.

Worked examples: [`examples/task/task-example-design-briefing-full.md`](examples/task/task-example-design-briefing-full.md) shows two apps and a design system block with every optional section. [`examples/task/task-example-design-briefing-single.md`](examples/task/task-example-design-briefing-single.md) shows one app with no audience labels. [`examples/task/task-example-design-briefing-minimal.md`](examples/task/task-example-design-briefing-minimal.md) shows the core sections and one link block.

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

#### **Related tasks**
* * *
*   `{Task or briefing title}`

## Requirements
* * *
### {AUDIENCE}
* * *
**Display**
- [] {What the screen shows, written so a design review can fail it}

**{Facet}**
- [] {Requirement}

### {NEXT AUDIENCE}
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
- `#### **References**` and `#### **Related tasks**` hang under Briefing. A name with no link is a backticked bullet, never a made-up URL
- Under Requirements, add an ALL-CAPS audience heading, `### PARTNER`, `### CREATOR`, `### BACKOFFICE` or `### DESIGN SYSTEM`, only when the briefing has two or more audiences. A single audience starts straight on its first facet
- Each facet is a bold lead line with `- []` items under it. No numbered groups, no prose under a facet and no User Story. Use the facet names below when one fits, in this order, and name a new facet for the thing it checks when none does
- `**Display**` is what the screen shows and how it reads, and every audience with a screen has one
- `**Validation**` is what blocks the user and how the error behaves, used when a field becomes required or gains limits
- `**Existing {Records}**`, such as `**Existing Deals**`, is how data saved before the change behaves when it is shown or edited
- `**{State}**`, such as `**Reach Paused**`, is one facet per named state the change adds, with when it starts, what it shows and when it clears
- `**Notification & Email**` covers messages the change sends, rewrites or retires. Name an existing notification by its catalog title in backticks
- `**Visibility**` is when an element shows or hides, with the condition as a value
- `**Contrast**` is readability over the backgrounds an element sits on, used for visual system changes
- Under `### DESIGN SYSTEM`, a facet may name a component group, such as `**Partner Form Components**`, and `**Cleanup**` lists layers or components to remove. A `**Why**` facet with `*   ` bullets may follow when the team needs the reason for a component trade-off beside it. It is the one facet without checkboxes
- Deliverables lists the frames and states design hands over, such as empty, filled and error. Add it when the states are not plain from Requirements or when one change spans several screens. Never repeat a requirement there
- Copy says who writes which copy. Copy rules, such as `never a limit`, stay in Requirements
- Open Questions holds what is still undecided, and Briefing holds what is settled. Name who decides when it is not plain. Before adding a question, check that Requirements does not already answer it
- Success Signal names the change we expect to see after release and where it shows. Add it when About carries data to compare against. Leave it out of a pure visual or design system change
- Dev Handover lists the logic the dev story must carry that no frame shows, such as feed rules, thresholds and counts. It is for the PO writing that story, so it comes last
- Requirements and Deliverables use `- []`. Every other list uses `*   `
- A `* * *` divider sits directly under every heading and nowhere else. A paragraph directly above `* * *` imports into ClickUp as a heading
- The section headings, the ALL-CAPS audience headings and the Title Case facet labels are this shape's own labels. The briefing keeps them as written, and a heading case rule in another shape does not rename them. Human Voice Rules sentence case covers every other heading and label in the briefing
- Write no markdown tables. A numbered title, if one is ever needed, is written `1\. **{Title}**`
- Wrap every file name and every component or layer name in backticks, such as `Form | Location`, so ClickUp does not auto-link a file name and the name reads as a literal
- Pushed to ClickUp, each `- []` is sent as `- [ ]` so it imports as a checkbox. The export keeps `- []`
- Do not end a bullet or checklist item with a full stop
