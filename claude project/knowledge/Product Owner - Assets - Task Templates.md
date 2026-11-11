# Product Owner - Assets - Task Templates

The five task scaffolds a new task artifact is copied from, canonical task, parent task, subtask, quick task and feedback ticket, with the sections each one requires and the numbered requirement-group grammar.

---

## 1. OVERVIEW

### Purpose

Provides reusable markdown scaffolds for standalone tasks, parent tasks, subtasks, quick tasks and feedback tickets.

### Usage

Use these scaffolds with the Task Mode document, which holds the wider Task rules. Copy the matching template, remove optional sections that do not apply and preserve source structure when the user asks for sync or refinement.

---

## 2. CANONICAL TASK TEMPLATE

Worked example: **Examples - Task - UI Refinement** shows the full task shape applied to design-parity work, with functional scope protected and accessibility verification included.

```markdown
# {Task Title}

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

- Remove any optional section that does not apply
- If the user provides source content, preserve it and only normalize what the user asked to normalize
- When the task shares behavior with sibling tasks, add `Related tasks`
- A parent task, related task, ticket or epic that was named but not linked keeps its own bullet as backticked plain text, `` - `{Task title}` ``, the same shape `**Epic**` uses above. Never fabricate a URL to complete the link, and never move a named parent into About prose because no link was supplied
- A Task in a Story bundle follows the task path and Story-link contract in Templates - Story Mode Section 7. Omit `**Story**` for a task that belongs to no Story
- Do not end a newly authored or rewritten bullet item with a full stop

---

## 3. PARENT TASK TEMPLATE

Use this when one parent task coordinates several subtasks.

Worked example: **Examples - Task - Standard Feature** shows shared feature scope stated once while independent child tasks retain their own implementation detail. A design token release with one subtask per app lives in **Examples - Task - DS Variables**: the full change list stated once in the parent, in the ClickUp format the team ships.

```markdown
# {Parent Task Title}

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

Worked example: **Examples - Task - Subtask** shows a bounded child task that separates zero-result recovery from request failure without leaking permission state. Subtasks split by platform live in **Examples - Task - DS Variables**: each carries only its own token file and the checks that file needs, under a parent that holds the shared change list.

```markdown
# {Subtask Title}

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

Worked example: **Examples - Task - Quick Task** shows exact replacement copy, a zero-day edge and an explicit no-layout-change boundary in the compact shape.

```markdown
# {Task Title}

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

Worked example: **Examples - Task - Feedback Ticket** shows a UI/UX ticket with grouped items, a Code and Figma screenshot pair and a Code-only pair for an item with no Figma frame.

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
- A screenshot pair is a `Code` line and a `Figma` line, each above its images, with the Figma frame link on the `Figma` label when the reviewer gave one. Keep the pair in that order. Leave out a side with no screenshot, and never write a placeholder image
- Put `###   ` before each group heading after the first, so the groups read apart in ClickUp
