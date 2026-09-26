---
title: "Product Owner Task Templates - v0.103"
description: "Copy/apply templates for Product Owner standalone tasks, parent tasks, subtasks and quick tasks."
version: "0.103"
contextType: asset
importance_tier: high
trigger_phrases:
  - "task templates"
  - "standalone task template"
  - "parent task template"
  - "subtask template"
  - "quick task template"
---

# Product Owner Task Templates - v0.103

Copy/apply templates for Product Owner task deliverables.

**Loading Condition:** CONDITIONAL, with `references/task-mode.md` whenever Task intent is selected
**Purpose:** Provides the canonical task, parent task, subtask and quick task scaffolds a new task artifact is copied from
**Scope:** The four task shapes, the sections each one requires and the numbered requirement-group grammar
**Output Path:** `export/[###] - task-[description].md`, or the existing task filename on a source sync

---

## 1. OVERVIEW

### Purpose

Provides reusable markdown scaffolds for standalone tasks, parent tasks, subtasks and quick tasks.

### Usage

Load this asset with Task Mode. Copy the matching template, remove optional sections that do not apply and preserve source structure when the user asks for sync or refinement.

---

## 2. CANONICAL TASK TEMPLATE

Worked example: [`examples/task/task-example-ui-refinement.md`](examples/task/task-example-ui-refinement.md) shows the full task shape applied to design-parity work, with functional scope protected and accessibility verification included.

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

1.  **{Item Title}**

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

2.  **{Item Title}**

---

{1-2 short paragraphs describing the expected outcome and why it matters.}

**Checklist**

- [] {Actionable requirement}
- [] {Actionable requirement}

---

### **{Next Category Name}**

---

3.  **{Item Title}**

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
- `**Story**` names the Story a task delivers. In a Story with nested Tasks bundle the task saves as `[###].[n] - task-[description].md` in the Story's folder, links the sibling Story file in `**Story**` and carries no `**Parent task**` block for it, because a Story is not a task. Remove `**Story**` from a task that belongs to no Story
- Do not end a newly authored or rewritten bullet item with a full stop

---

## 3. PARENT TASK TEMPLATE

Use this when one parent task coordinates several subtasks.

Worked example: [`examples/task/task-example-standard-feature.md`](examples/task/task-example-standard-feature.md) shows shared feature scope stated once while independent child tasks retain their own implementation detail. A design token release with one subtask per app lives in [`examples/task/task-example-ds-variables.md`](examples/task/task-example-ds-variables.md): the full change list stated once in the parent, in the ClickUp format the team ships.

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

1.  **{Subtask Name}**

---

[{Subtask Title}](url)

2.  **{Subtask Name}**

---

[{Subtask Title}](url)

3.  **{Subtask Name}**

---

[{Subtask Title}](url)

```

---

## 4. SUBTASK TEMPLATE

Use this when the work belongs to a larger parent task.

Worked example: [`examples/task/task-example-subtask.md`](examples/task/task-example-subtask.md) shows a bounded child task that separates zero-result recovery from request failure without leaking permission state. Subtasks split by platform live in [`examples/task/task-example-ds-variables.md`](examples/task/task-example-ds-variables.md): each carries only its own token file and the checks that file needs, under a parent that holds the shared change list.

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

1.  **{Item Title}**

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

Number requirement groups only when the task carries two or more. A single group keeps its bold title without a number, as above. The moment a second group appears, number them `1.`, `2.` in order.
