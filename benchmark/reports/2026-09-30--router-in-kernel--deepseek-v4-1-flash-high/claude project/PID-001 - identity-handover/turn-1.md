```
I'll create your task. Open points below:

**1. Platform**
- Which client carries the change: Web, Desktop, iOS, Android, or more than one
- If Web, whether Desktop counts as covered through the web client it wraps

**2. Why now**
- The problem this chip solves and which persona hits it, whether Dana on Free, Theo's agency or Mireille's team
- What members do today instead, such as reading the whole list or scrolling to a date

**3. What the chip matches**
- To-dos due today in the owner's time zone only, or today and anything earlier
- Whether checked-off to-dos stay out, as they do for Overdue
- Whether a to-do with no due date stays out, and what a repeating to-do shows on its next due date

**4. How it sits with the current chips**
- A fourth chip in the existing row, or a replacement for one of the chips shipping today
- Whether one chip stays active at a time with All as the default, and whether Due today can combine with Assigned to me
- The chip label, its position in the row, and whether it shows a count

**5. List and empty state**
- Whether the due-date sort and the no-due-date items at the bottom stay unchanged
- The copy shown when nothing is due today

**6. Design and copy**
- Design references for the chip row and for its default, active, hover and empty states
- Whether the label needs new strings in the six shipped locales

**7. Analytics**
- The `filter` value for the new chip, following the existing lowercase snake_case pattern
- Whether Data reviews a tracking plan update before client work starts, and who raises it

**8. Dependencies and boundaries**
- Whether anything behind the `recurring_todos` flag changes what today means for this filter
- Whether the To-dos view query needs a back-end change or an existing query already answers it
- A parent task, Story or related ticket this attaches to
- What sits out of scope, beyond the other chips keeping their current behavior

**9. Validation**
- What I am likely to assume wrongly about the filter or the member who uses it
- Which constraint above should I question before writing it into the task
```

Export-equivalent path: `export/NNN - task-due-today-filter-chip-clarification.md`

Quality: question covers the task fields, challenges the filter definition and the platform assumption, and waits rather than drafting.

HVR self-scan: 0 hard blockers. Fixed: opening triad rewritten as a two-part sentence. Kept with reason: the three supplied personas as content, and the backticked identifiers `recurring_todos` and `filter` written as the sources name them.

Summary: `$task` routes to Task Mode, which asks its context question before drafting, so this delivery is the intake question in the task lane and the task follows once you answer. From the Loomlist context page I already hold the three existing chips and their one-at-a-time rule, the Overdue rule and the owner time-zone rule, the due-date sort with undated to-dos at the bottom, the `filter_selected` convention, and the `Filter the To-dos view` flow. Two mentions I would apply unless you correct them: the title follows the house convention as `FE - {platform} - TODO - Due today filter chip on the To-dos view`, and this runs at Standard energy, so say the word if you would rather have a lean `$quick` pass.