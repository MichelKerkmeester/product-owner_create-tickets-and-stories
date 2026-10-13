# SID-001 turn 2 transcript

**User:** Front end, Web only for now, Desktop gets it through the web client and the apps follow later. The chip goes right after Overdue and shows to-dos not checked off that are due today in the owner's time zone, sorted by due date like the other chips, and only one chip is active at a time. Picking it sends filter_selected with filter set to due_today, which Yara has already added to the tracking plan. No Figma, reuse the existing chip, and nothing else depends on it.

**Tool call:** `Bash` `{"command": "cd /private/var/folders/3c/zfqcqsts0kn19cgblj82gqhm0000gn/T/pi-playbook-bench/product-owner/skill/SID-001; cat sk-product-owner/assets/task-templates.md; ls sk-product-owner/assets/examples/task/", "description": "Read task templates and list task examples"}`

**Tool result:** `Bash`

```text
zsh:1: operation not permitted: /dev/null
zsh:1: operation not permitted: /dev/null
zsh:1: operation not permitted: /dev/null
---
title: "Product Owner Task Templates - v0.102"
description: "Copy/apply templates for Product Owner standalone tasks, parent tasks, subtasks and quick tasks."
version: "0.102"
contextType: asset
importance_tier: high
trigger_phrases:
  - "task templates"
  - "standalone task template"
  - "parent task template"
  - "subtask template"
  - "quick task template"
---

# Product Owner Task Templates - v0.102

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

Worked example: [`examples/task/task-example-ui-refinement.md`](examples/task/task-example-ui-refinement.md) s
```

**Tool call:** `Write` `{"file_path": "/private/var/folders/3c/zfqcqsts0kn19cgblj82gqhm0000gn/T/pi-playbook-bench/product-owner/skill/SID-001/export/002 - task-due-today-filter-chip.md", "content": "# FE - Web - TODO - Due today filter chip\n\n### About\n\n---\n\nMembers can filter the To-dos view by All, Assigned to me and Overdue, but they have no quick way to see what is due today. This task adds a fourth chip, \"Due today\", so a member can see today's open work without scanning the full list or checking Overdue.\n\nThe chip ships on Web first. Desktop gets it through the web client the next time it loads, with n`

**Tool result:** `Write`

```text
File created successfully at: /private/var/folders/3c/zfqcqsts0kn19cgblj82gqhm0000gn/T/pi-playbook-bench/product-owner/skill/SID-001/export/002 - task-due-today-filter-chip.md (file state is current in your context — no need to Read it back)
```

**Tool call:** `Read` `{"file_path": "/private/var/folders/3c/zfqcqsts0kn19cgblj82gqhm0000gn/T/pi-playbook-bench/product-owner/skill/SID-001/export/002 - task-due-today-filter-chip.md"}`

**Tool result:** `Read`

```text
1	# FE - Web - TODO - Due today filter chip
2	
3	### About
4	
5	---
6	
7	Members can filter the To-dos view by All, Assigned to me and Overdue, but they have no quick way to see what is due today. This task adds a fourth chip, "Due today", so a member can see today's open work without scanning the full list or checking Overdue.
8	
9	The chip ships on Web first. Desktop gets it through the web client the next time it loads, with no Desktop release. iOS and Android follow in later tasks.
10	
11	### Requirements
12	
13	---
14	
15	1.  **Due today chip**
16	
17	---
18	
19	The chip reuses the existing filter chip component and follows the same selection rules as the other chips, so it looks and works like them. No new design is needed.
20	
21	**Checklist**
22	
23	- [ ] "Due today" sits directly after Overdue, making the order All, Assigned to me, Overdue, Due today
24	- [ ] The chip uses the existing filter chip component with no visual changes
25	- [ ] Only one chip is active at a time, so selecting Due today clears the chip that was active before
26	- [ ] All stays the default chip when the To-dos view opens
27	
28	---
29	
30	2.  **Due today list**
31	
32	---
33	
34	Due today shows the open to-dos a member still needs to finish today. "Today" is based on the to-do owner's time zone, which is also how Overdue works, so the two chips never show the same to-do.
35	
36	**Checklist**
37	
38	- [ ] The list shows only to-dos that are not checked off and whose due date is today in the to
```

**Assistant:**

I've written the Web task for the "Due today" chip on the To-dos view.

Path: `export/002 - task-due-today-filter-chip.md`
Verified: read-back succeeded; 56 lines
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

**Quality summary:** Everything in it comes from your answers or `context/loomlist-context.md`. The task has an About section and three checklist groups: the chip, the list it shows and the tracking event. The title follows the naming rule in the context file: `FE - Web - TODO - Due today filter chip`. There are no Figma or Epic references, since you said there's no Figma and nothing depends on it. The earlier question file (001) is unchanged.

The chip uses the existing chip component and sits right after Overdue. Only one chip can be active at a time, and All stays the default. It shows to-dos not checked off that are due today in the owner's time zone, sorted by due date. Selecting it sends `filter_selected` with `filter` set to `due_today`, which Yara has already added to the tracking plan.

**Things I added that you didn't state (remove any you don't want):**
- A to-do owned by someone in another time zone counts when it's due today in the owner's time zone, even if the viewer's date is different
- The list only shows to-dos the member can open, the same as the rest of the To-dos view
- The other three `filter` values are still sent as before
- The event includes the standard properties listed in the context file

**Not in the task, because you didn't answer or mention them:**
- Whether todos-service already supports a "due today" query
- What the view shows when nothing is due today
- Translations of the "Due today" label for the other five languages the app ships in

Tell me if any of these should go in.
