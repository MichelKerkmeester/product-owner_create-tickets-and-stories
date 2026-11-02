# PID-001 turn 2 transcript

**User:** Front end, Web only for now, Desktop gets it through the web client and the apps follow later. The chip goes right after Overdue and shows to-dos not checked off that are due today in the owner's time zone, sorted by due date like the other chips, and only one chip is active at a time. Picking it sends filter_selected with filter set to due_today, which Yara has already added to the tracking plan. No Figma, reuse the existing chip, and nothing else depends on it.

**Tool call:** `Read` `{"file_path": "/private/var/folders/3c/zfqcqsts0kn19cgblj82gqhm0000gn/T/pi-playbook-bench/product-owner/project/PID-001/knowledge/Product Owner - Assets - Task Templates - v0.102.md"}`

**Tool result:** `Read`

```text
1	# Product Owner - Assets - Task Templates - v0.102
2	
3	The four task scaffolds a new task artifact is copied from, canonical task, parent task, subtask and quick task, with the sections each one requires and the numbered requirement-group grammar.
4	
5	---
6	
7	## 1. OVERVIEW
8	
9	### Purpose
10	
11	Provides reusable markdown scaffolds for standalone tasks, parent tasks, subtasks and quick tasks.
12	
13	### Usage
14	
15	Use these scaffolds with the Task Mode document, which holds the wider Task rules. Copy the matching template, remove optional sections that do not apply and preserve source structure when the user asks for sync or refinement.
16	
17	---
18	
19	## 2. CANONICAL TASK TEMPLATE
20	
21	Worked example: **Examples - Task - UI Refinement** shows the full task shape applied to design-parity work, with functional scope protected and accessibility verification included.
22	
23	```markdown
24	# {Task Title}
25	
26	### About
27	
28	---
29	
30	{1-3 short paragraphs describing the task, why it matters and what outcome it should create.}
31	
32	**References**
33	
34	---
35	
36	Flows
37	
38	- [{Flow name}](figma-url)
39	
40	Page
41	
42	- [{Page name}](figma-url)
43	
44	Components
45	
46	- [{Component name}](figma-url)
47	
48	**Epic**
49	
50	---
51	
52	- `{Epic name}`
53	
54	**Story**
55	
56	---
57	
58	- [{Story H1}](<[###] - Story-[description].md>)
59	
60	**Parent task**
61	
62	---
63	
64	- [{Parent task title}](url)
65	
66	**Related tasks**
67	
68	---
69	
70	- [{Related t
```

**Tool call:** `Read` `{"file_path": "/private/var/folders/3c/zfqcqsts0kn19cgblj82gqhm0000gn/T/pi-playbook-bench/product-owner/project/PID-001/knowledge/Product Owner - Examples - Task - UI Refinement - v0.100.md"}`

**Tool result:** `Read`

```text
1	# Product Owner - Examples - Task - UI Refinement - v0.100
2	
3	Instantiates Task Templates section 2, Canonical Task. Shows design-parity work scoped with no functional change and cross-device accessibility verification.
4	
5	---
6	
7	# Align the Meridian settings screen with the current design reference
8	
9	### About
10	
11	---
12	
13	A design audit of the Meridian mobile app found that the shipped settings screen has drifted from design reference v3. The screen still uses the earlier 12pt section gap, full-width dividers and 20x20 leading icons while newer settings surfaces use the current tokens.
14	
15	Match design reference v3 on iOS and Android. Keep every label, row, navigation target, toggle, permission rule and analytics event unchanged.
16	
17	**References**
18	
19	---
20	
21	Page
22	
23	- [Settings screen, design reference v3](figma-url)
24	
25	Components
26	
27	- [Settings row component](figma-url)
28	- [Settings section header component](figma-url)
29	
30	### Requirements
31	
32	---
33	
34	### **Spacing**
35	
36	---
37	
38	1.  **Match section and row spacing to the design tokens**
39	
40	---
41	
42	Replace the earlier spacing values with the exact measurements in design reference v3. Rows may grow for wrapped labels but must never shrink below the specified height.
43	
44	**Checklist**
45	
46	- [ ] Set spacing between section headers and their first row to `space-16` (16pt)
47	- [ ] Set spacing between grouped sections to `space-24` (24pt)
48	- [ ] Set minimu
```

**Tool call:** `Grep` `{"pattern": "(?i)compact summary|chat reply|pre-reply|floor", "path": "/private/var/folders/3c/zfqcqsts0kn19cgblj82gqhm0000gn/T/pi-playbook-bench/product-owner/project/PID-001/knowledge/Product Owner - Rules - Quality Scoring - v0.100.md", "output_mode": "content", "-C": 2}`

**Tool result:** `Grep`

```text
1-# Product Owner - Rules - Quality Scoring - v0.100
2-
3:The rubric behind the six blocking floors. Each dimension states what it measures, the one test that separates a clear pass from a near miss, and how it reads against each artifact shape the system produces.
4-
5----
--
9-### Purpose
10-
11:Six dimensions on a ten-point scale, scored against every deliverable before export. Five carry a floor of 8. Accuracy carries 9.
12-
13:A floor is blocking, not advisory. A dimension under its floor stops the export and names the work, which is why every dimension below carries a test a scorer can actually run rather than an adjective to agree with.
14-
15-### What a score is not
--
23-## 2. THE SIX DIMENSIONS
24-
25:Each entry names its floor, what it measures, and the test that separates a floor-clearing score from a near miss. The near miss is written at 6, one band below, because that is the score a competent draft lands on when a dimension is nearly right. Accuracy is written at 7, since its bands sit one point higher.
26-
27:**Completeness, floor 8.** Measures whether every section the resolved shape requires is present and populated from supplied material, with dependencies, edge cases, error states, empty states, loading states and permission boundaries named wherever they bear on acceptance.
28-
29-At 6 every required section exists and at least one carries a placeholder, a restated heading, or a single generic line where the shape expects substance. At 8 an implementer co
```

**Assistant:**

```markdown
# FE - Web - TODO - Due today filter chip

### About

---

The To-dos view has three filter chips: All, Assigned to me and Overdue. Overdue only shows to-dos due before today. To see what has to be finished today, a member has to scan All, where today's to-dos sit between older and later ones.

Add a Due today chip that lists the to-dos not checked off whose due date is today in the to-do owner's time zone. It uses the same day boundary as Overdue, so a to-do never appears under both chips. Together, the two chips cover everything not checked off that is due up to the end of today.

This task covers Web only. Desktop gets the chip through the web client the next time it loads, with no Desktop release. iOS and Android follow in later tasks.

### Requirements

---

1.  **Add the chip after Overdue**

---

Due today uses the existing filter chip, so it looks and behaves like the other three chips.

**Checklist**

- [ ] Show a chip labelled "Due today" directly after Overdue, so the row reads All, Assigned to me, Overdue, Due today
- [ ] Use the existing filter chip component with no new styles or states
- [ ] Keep one chip active at a time, so selecting Due today deactivates the chip that was active
- [ ] Keep All as the default chip when the To-dos view opens
- [ ] Confirm the chip appears in Desktop after it loads the web build that ships this task

---

2.  **List the to-dos due today**

---

"Today" means the to-do owner's today, the same rule that Overdue and due dates already follow. Say a teammate's to-do is due today in the teammate's time zone. A member viewing it sees it under Due today, even when the member's own date is different.

**Checklist**

- [ ] Show only to-dos not checked off whose due date is today in the to-do owner's profile time zone
- [ ] Leave out to-dos due before today, which stay under Overdue
- [ ] Leave out to-dos due after today and to-dos with no due date
- [ ] Show only to-dos the member can open, the same set the other chips draw from
- [ ] Sort the list by due date, the same way the other chips sort

---

3.  **Send the chip selection event**

---

Yara has added `due_today` to the tracking plan. That means this task can send the value without waiting for another Data review.

**Checklist**

- [ ] Send `filter_selected` with `filter` set to `due_today` when a member selects Due today
- [ ] Include `workspace_id`, `user_id`, `platform`, `app_version` and `plan` on the event, with the web build number in `app_version`
- [ ] Keep the events for `all`, `assigned_to_me` and `overdue` unchanged
```

Export-equivalent path: `export/002 - task-todos-due-today-filter-chip.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

I've written the Web task for the Due today chip. All six quality checks passed. Everything in it comes from your answer or from `loomlist-context.md`.

**Things I added that you didn't state (delete any you don't want):**
- **Other time zones:** a teammate's to-do appears under Due today when it's due today in the teammate's time zone. This follows from the owner time zone rule in the context file.
- **Which to-dos show:** only to-dos the member can open, which matches how the context file defines the To-dos view.
- **Leaving out overdue to-dos:** these stay under Overdue, so the two chips never overlap.
- **Existing events:** the `all`, `assigned_to_me` and `overdue` events stay unchanged.
- **Web build number:** it goes in `app_version`, as the context file says Web does.
- **Desktop check:** confirm the chip shows up once Desktop loads the new web build.

**Still open, so I left them out of the task:**
- **Empty state:** what the list shows when nothing is due today.
- **Translations:** the "Due today" label needs strings for de-DE, fr-FR, es-ES, ja-JP and pt-BR. Without them, those locales will show the en-US label.

Tell me what you want for either one and I'll add it to the task.
