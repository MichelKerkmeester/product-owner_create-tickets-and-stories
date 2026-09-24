# Product Owner - Assets - Task Templates - v0.101

The four task scaffolds a new task artifact is copied from, canonical task, parent task, subtask and quick task, with the sections each one requires and the numbered requirement-group grammar.

---

## 1. OVERVIEW

### Purpose

Provides reusable markdown scaffolds for standalone tasks, parent tasks, subtasks and quick tasks.

### Usage

Use these scaffolds with the Task Mode document, which holds the wider Task rules. Copy the matching template, remove optional sections that do not apply and preserve source structure when the user asks for sync or refinement.

---

## 2. CANONICAL TASK TEMPLATE

Worked example: **Examples - Task - UI Refinement** shows the full task shape applied to design-parity work, with functional scope protected and accessibility verification included.

```markdown
# {Task Title}

### About

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

- [ ] {Actionable requirement}
- [ ] {Actionable requirement}

**User Story**

- **Given:** {context}
- **When:** {action}
- **Then:** {outcome}

---

2.  **{Item Title}**

---

{1-2 short paragraphs describing the expected outcome and why it matters.}

**Checklist**

- [ ] {Actionable requirement}
- [ ] {Actionable requirement}

---

### **{Next Category Name}**

---

3.  **{Item Title}**

---

{Short description.}

**Checklist**

- [ ] {Actionable requirement}
- [ ] {Actionable requirement}

```

### Notes For Use

- Remove any optional section that does not apply
- If the user provides source content, preserve it and only normalize what the user asked to normalize
- When the task shares behavior with sibling tasks, add `Related tasks`
- A parent task, related task, ticket or epic that was named but not linked keeps its own bullet as backticked plain text, `` - `{Task title}` ``, the same shape `**Epic**` uses above. Never fabricate a URL to complete the link, and never move a named parent into About prose because no link was supplied
- Do not end a newly authored or rewritten bullet item with a full stop

---

## 3. PARENT TASK TEMPLATE

Use this when one parent task coordinates several subtasks.

Worked example: **Examples - Task - Standard Feature** shows shared feature scope stated once while independent child tasks retain their own implementation detail. A design token release with one subtask per app lives in **Examples - Task - DS Variables**: the full change list stated once in the parent, in the ClickUp format the team ships.

```markdown
# {Parent Task Title}

### About

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

Worked example: **Examples - Task - Subtask** shows a bounded child task that separates zero-result recovery from request failure without leaking permission state. Subtasks split by platform live in **Examples - Task - DS Variables**: each carries only its own token file and the checks that file needs, under a parent that holds the shared change list.

```markdown
# {Subtask Title}

### About

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

- [ ] {Actionable requirement}
- [ ] {Actionable requirement}

```

---

## 5. QUICK TASK TEMPLATE

Use this for direct small updates when the request is explicit.

Worked example: **Examples - Task - Quick Task** shows exact replacement copy, a zero-day edge and an explicit no-layout-change boundary in the compact shape.

```markdown
# {Task Title}

### About

---

{Brief explanation of the change and why it matters.}

### Requirements

---

**{Item Title}**

---

{Short description.}

**Checklist**

- [ ] {Actionable requirement}
- [ ] {Actionable requirement}

```

Number requirement groups only when the task carries two or more. A single group keeps its bold title without a number, as above. The moment a second group appears, number them `1.`, `2.` in order.
