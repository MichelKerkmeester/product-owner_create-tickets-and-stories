---
title: "Product Owner - Templates - Task Mode - v0.307"
description: "Product Owner task-mode workflow, delivery standards and structure rules for task artifacts."
version: "0.307"
contextType: reference
importance_tier: high
trigger_phrases:
  - "task mode"
  - "$task acceptance criteria"
  - "subtask parent task"
  - "source task sync"
  - "requirements checklist"
---

# Product Owner - Templates - Task Mode - v0.307

Task-mode guidance aligned to the current Product Owner task corpus. This version prioritizes a flexible context block, numbered requirement groups, an H2 About and H3 section headings under it.

**Loading Condition:** ON-DEMAND
**Purpose:** Provides task-mode workflow, standards and structure rules for `$task` and `$t` requests
**Scope:** Task mode overview, delivery standards, structure rules, error recovery and task template usage pointer
**Output Path:** `export/[existing-task-name].md` or `export/[###] - task-[description].md`
**Loads With:** `assets/task-templates.md` as the paired scaffold, beside the always-loaded `references/hvr-core.md` and `references/conciseness.md`
**Routed By:** `$task`, `$t`, `$task --subtask`, task framing, the feature, acceptance, user_need, technical_task and integration semantic topics, and the ui_refinement topic on its 0.80 override
**Hands Off To:** `references/interactive-mode.md` when scope, user value or testable acceptance criteria cannot be inferred, which returns here once the user answers

---

## 1. OVERVIEW

### Purpose

Provides the task-mode workflow, delivery standards and structure rules for `$task` and `$t` requests. Task Mode creates or refines Product Owner tasks that define WHAT and WHY, delivered as a markdown task artifact with checklist items inside Requirements for QA and handoff.

### When to Use

Use Task Mode for:
- Standalone tasks with About and Requirements
- Synced tasks updated to match pasted source material or corpus style
- Parent tasks that link or track child subtasks
- Subtasks covering one area within a parent task
- Feature work, enhancements, acceptance criteria and refinement of existing task content

### Command: `$task`

- **Short Alias:** `$t`
- **Purpose:** Create or refine Product Owner tasks that define WHAT and WHY
- **Output:** Markdown task artifact
- **Thinking:** Rigor scales with the selected energy automatically
- **Interactive Mode:** Ask one comprehensive question unless the request already contains enough direction. An explicit command routes the request and does not stand in for the direction, so `$task` and `$bug` still ask their context-specific question and wait. Only `$quick` may skip routine intake
- **Key Feature:** Uses checklist items inside Requirements for QA and handoff

### Core Rules

- Ask one comprehensive question before drafting unless the request already contains enough direction or uses `$quick`. An explicit command routes the request and does not supply that direction
- Deliver only the requested task, subtask or refinement
- Do not force a fixed metadata block order when the source task already exists
- When syncing or refining an existing task, preserve the source section names, section order and reference labels unless the user asks to standardize them. A value, name or status a supplied source gives travels into the task as the source writes it, inside backticks: a value a requirement builds or checks, such as an algorithm, header, endpoint, status code, count, range, timeout, schedule or threshold, an event, property or service name, and a status word such as `deprecated` or `proposed`. A supplied value is a constraint rather than HOW, so staying in WHAT and WHY never removes it. Say what a status means beside its word, never in place of it, and never write a generic stand-in such as the server where the source names the service
- Use the same filename when updating an existing task

### Task Types Supported

- **Standalone task:** Full task with About and Requirements
- **Synced task:** Existing task updated to match pasted source material or corpus style
- **Parent task:** Coordination task that links or tracks child subtasks
- **Subtask:** Narrow task covering one area within a parent task

---

## 2. DELIVERY STANDARDS

### Required Core Sections

Every task must include:

1. Title
2. `## About`
3. `### Requirements`

### Optional Context Sections

Use only when they add value or already exist in the source task:

- `**References**`
- `**Epic**`
- `**Parent task**`
- `**Related tasks**`
- `**Related tickets**`
- `**Ticket:** TBD`
- `Flows`
- `Page`
- `Components` or `Component`
- `**User Story**`

### Flexibility Rules

- The task corpus contains both newer clean tasks and older legacy tasks
- The template must support either a minimal context block or a richer context block
- Category headings inside Requirements are optional but recommended for larger tasks
- Category headings may be bold or plain when matching existing source material

### Requirement Item Standard

Each numbered requirement group should follow this pattern unless the source task must be mirrored more literally:

1. Numbered item title
2. One or more short paragraphs that explain the outcome and context
3. `**Checklist**`
4. `- []` checklist items for literal, actionable requirements
5. Checklist and bullet items must not end with `.`

Number requirement groups only when the task carries two or more. A single group keeps its bold title without a number. The moment a second group appears, number them `1.`, `2.` in order.

### Assumptions

- Never add `[Assumes: ...]` in task exports
- If dependency uncertainty matters, rewrite it as plain task language without bracketed assumption tags
- A short blockquoted note after a requirement block is acceptable when it clarifies terminology, behavior distinctions or intentionally deferred logic that affects QA

---

## 3. STRUCTURE RULES

### Section Hierarchy

- **Core sections:** `## About` at H2, `### Requirements` at H3
- **Requirement category headings:** `### **{Group Name}**` or `### {Group Name}` when matching an existing task
- **Bold sub-label:** `**Checklist**`
- **Optional bold labels:** `**References**`, `**Epic**`, `**Parent task**`, `**Related tickets**`

### Naming a parent or related work with no link

A parent task, related task, ticket or epic is often named before it exists as a link. Give it its own bullet as backticked plain text, `` - `{Task title}` ``, which is the shape `**Epic**` already uses. Never fabricate a ClickUp or Figma URL to complete the link, never drop the named parent because no link was supplied, and never push it into About as prose where a reader looking for the relationship will not find it. When the link arrives later, the bullet becomes an ordinary markdown link in place.

### Divider Rules

- Use `---` after `## About`
- Use `---` after `### Requirements`
- Use `---` after each category heading
- Use `---` after each numbered item title

### References Block

The references block is flexible. Use only the subsections that matter.

Allowed reference labels include:

- `Flows`
- `Page`
- `Components`
- `Component`
- `Changed`
- `Impacted`

These labels may be bold or plain when syncing an existing task. Do not auto-normalize them unless the user asks.

### Requirement Group Variants

The active template supports three valid patterns:

#### Pattern A: Flat numbered groups

Use when the task is small.

```markdown
1.  **{Item Title}**

---

{Short description.}

**Checklist**

- [] {Requirement}
- [] {Requirement}
```

#### Pattern B: Category heading plus numbered groups

Use when the task spans multiple areas.

```markdown
### **{Category Name}**

---

1.  **{Item Title}**

---

{Short description.}

**Checklist**

- [] {Requirement}
- [] {Requirement}
```

#### Pattern C: Nested sub-blocks inside a numbered group

Use when one numbered requirement needs several sub-areas.

```markdown
1.  **{Item Title}**

---

{Short description.}

**Sub-area A**

- [] {Requirement}
- [] {Requirement}

**Sub-area B**

- [] {Requirement}
```

### User Story Usage

- User Story is optional
- Include it only when it clarifies the user flow or business value
- Place it inside the relevant numbered requirement block
- Use Given / When / Then format
- Use this exact structure only

```markdown
**User Story**

- **Given:** {context}
- **When:** {action}
- **Then:** {outcome}
```

The labels carry a colon and the block takes no `---` divider under `**User Story**`, which is what the task corpus writes and what [task-templates.md](../assets/task-templates.md) shows. The divider rules above cover `## About`, `### Requirements`, category headings and numbered item titles, and the bold sub-labels inside a requirement (`**Checklist**`, `**User Story**`) are not among them. A refinement keeps whatever the source task already uses.

### Tables

Use a table when every row shares the same fields, such as token or property values that change per size.

- A table carries at most 4 columns. When the columns would pass that, split them across more tables that each repeat the first column
- A table of values that vary by size puts Size in the leftmost column with one row per size. Each token or property gets its own column, though tokens that share every value may share one

[`examples/task/task-example-ds-variables.md`](../assets/examples/task/task-example-ds-variables.md) shows both rules on a design token release.

---

## 4. QUALITY CHECKLIST

### Pre-Creation Validation

- [ ] User request understood clearly?
- [ ] Task type identified correctly?
- [ ] Scope limited to the requested change?
- [ ] Source material preserved when task is a sync or refinement?
- [ ] Latest template version used?
- [ ] Supplied links in References, Epic, Related tasks and Related tickets resolve, with unresolvable ones flagged in prose rather than kept as dead links?

### Structure Validation

- [ ] Title present as H1?
- [ ] About uses `## About`?
- [ ] Requirements uses `### Requirements`?
- [ ] Numbered requirement groups use clear titles?
- [ ] Actionable requirement items use `- []`, with no space between the brackets?
- [ ] `---` dividers used consistently?
- [ ] Every table at most 4 columns, with Size leftmost when values vary by size?

### Content Validation

- [ ] About explains the task outcome and value?
- [ ] Requirements describe WHAT and WHY, not HOW, and carry every supplied value, name and status word as the source writes it?
- [ ] Requirement wording is concrete and testable?
- [ ] No unrequested scope added?
- [ ] Optional sections included only when useful?
- [ ] User Story included only when it adds value?

### Source Sync Validation

- [ ] Existing headings preserved when user asked for a sync?
- [ ] Existing section order preserved when user asked for a sync?
- [ ] Existing reference labels preserved when user asked for a sync?
- [ ] Legacy `[ ]` boxes or plain bullets converted to `- []` checklists only when the user asked to normalize them?

---

## 5. ERROR RECOVERY

### Common Errors

#### Forced metadata block

**Fix:** Remove unneeded `Epic`, `Related tickets` or `Ticket` sections. Keep only what the task needs.

#### Plain bullets used for actionable requirements

**Fix:** Convert requirement bullets to `- []` checklists.

#### Source task was standardized when it should have been synced

**Fix:** Restore the source section names, order and wording, then update only the checklist or requested parts.

#### User Story added by default

**Fix:** Remove it unless it adds clear value or the user requested it.

#### Assumption tags appear in export

**Fix:** Remove `[Assumes: ...]` and rewrite the point in plain task language or remove it if it is not required.

### Prevention Rules

1. Start from the source task when one exists
2. Keep the core sections fixed and the context block flexible
3. Group the checklist at the level that best supports verification
4. Use `- []` for actionable items
5. Add only the sections the task actually needs

---

Templates: see [task-templates.md](../assets/task-templates.md).

---

## 6. FINAL REMINDERS

1. Keep the core structure fixed and the context block flexible
2. Preserve source structure when syncing an existing task
3. Use category headings when they make the task easier to scan
4. Use `- []` for actionable requirement items
5. Stay in WHAT and WHY, not HOW
6. Deliver only the requested task scope
---

The kernel points here for the When To Use list:

- Development tasks, subtasks, parent tasks, acceptance criteria, QA-ready requirements, and copy-consistency or casing standardisation work
- Bug reports, defect writeups, reproduction steps, expected behavior, capture
- Refinement of pasted task, bug, PRD or document content into backlog-ready or ClickUp-ready markdown
- Product requirements documents (PRDs) with Connextra-adjacent house-format sections, numbered Given/When/Then acceptance criteria and a Mark-as-done checkbox per criterion
- Product or engineering guides, catalogs, behavior references, runbooks, API or schema references, architecture documents, technical proposals and decision records

The kernel points here for the backlog artefact rule:

5. Keep backlog artifacts outcome-focused. Keep documentation facts, analysis, recommendations and proposals in their correct authority state.

The kernel points here for the dependency and edge case rule:

9. Identify dependencies, edge cases, error states, empty states, loading states and permission boundaries when relevant.

The kernel points here for the acceptance criteria rule:

10. Write acceptance criteria as outcomes the user can rely on, few in number and open on the mechanism, growing only with the surfaces a story touches. In a Story, Requirements holds hard constraints only, carries every hard value the source supplied with its value, units and notation intact, mirrors the source's own screen or surface grouping where it has one, names each shared screen's reuse map as a constraint, and is omitted only where the source supplies none. Every Requirements item is a `- []` checkbox holding a sentence a build can fail, so an item that reports what a screen says, shows or contains, naming no value, limit, condition, effect or named flow a build could get wrong, is description and is struck rather than reworded, and copy a screenshot supplies is quoted verbatim in backticks or dropped. A supplied value never travels into an acceptance criterion instead. Keep the Task QA checklist inside a Task's Requirements.
