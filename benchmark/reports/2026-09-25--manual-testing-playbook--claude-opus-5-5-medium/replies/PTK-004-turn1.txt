```markdown
# FS - TODO - Recurring to-dos

### About

---

Members want to-dos that come back on a schedule. Repeating to-dos are the most requested to-do feature we have: 212 requests on the feedback board since January, and 38 Plus workspaces named it in the renewal survey as the reason they keep a second app for chores and routines. Today people copy a to-do by hand every week, or set a reminder far ahead and keep moving it.

This parent task holds the behavior every platform builds to, plus the rollout and the tracking. iOS, Android, Web and BE each deliver their part in a subtask. Desktop gets the feature through the web client, so it has no subtask of its own.

The work counts as a success when 10% of weekly active Plus and Team workspaces have at least one repeating to-do 8 weeks after the flag is on for everyone.

**References**

---

Brief

- `Recurring to-dos, PM brief` (Ines, 2026-09-08, with the answers from planning on 2026-09-10)

Flows

- `Recurring to-dos / Repeat picker`
- `Recurring to-dos / Custom interval`
- `Recurring to-dos / Occurrence menu`

Anouk has these frames ready for review.

### Requirements

---

### **Subtasks**

---

1.  **iOS**

---

- `FE - iOS - TODO - Recurring to-dos`

2.  **Android**

---

- `FE - Android - TODO - Recurring to-dos`

3.  **Web**

---

- `FE - Web - TODO - Recurring to-dos`

4.  **BE**

---

- `BE - TODO - Recurring to-dos`

---

### **Shared behavior**

---

5.  **Setting a repeat**

---

Any to-do with a due date can repeat. The member opens the to-do's detail sheet and taps Repeat. On a to-do without a due date, Repeat is greyed out with the hint `Add a due date to repeat`.

| Option | Next due date |
| --- | --- |
| Daily | The next day |
| Weekdays | The next weekday, Monday through Friday |
| Weekly | Same weekday next week |
| Monthly | Same day next month |
| Custom | Every N days, weeks or months, with N from 1 to 99 |

Monthly keeps to the day of the first due date. A series that starts on the 31st lands on the 30th in April and on the 31st again in May.

---

6.  **Ends**

---

Ends sits under Repeat and has three choices:

- Never, the default
- On date, which stops the series after the last occurrence on or before that date
- After, which stops the series after a set number of occurrences, from 1 to 365

---

7.  **Occurrences and Skip this one**

---

Only one occurrence exists at a time. When the member checks it off, the next one appears on the same page with the next due date. The assignee and the reminder carry over, and the reminder keeps the same local time.

Skip this one sits in the to-do's menu. It moves the to-do to its next due date without marking it done. A skipped occurrence still counts toward an After limit, so a series set to end after 5 occurrences ends after 5 whether each one was checked off or skipped.

---

8.  **Workspace limit**

---

A workspace can hold 500 repeating to-dos that have not ended. Checked-off and ended series do not count. When a workspace reaches the limit, Repeat stays visible but opens a sheet that says `This workspace has 500 repeating to-dos. End one to add another.`

---

9.  **Time zones**

---

Next due dates are worked out in the to-do owner's time zone. The Overdue chip and reminders follow the same rule, so all three agree for the owner. When the to-do is reassigned, the next occurrence uses the new owner's zone. A teammate in another zone sees the owner's date with the zone shown.

> The to-do owner is the assignee, or the creator when the to-do has no assignee. It is not the workspace Owner role.

---

10. **Plans**

---

Repeat is for Plus and Team workspaces. On Free it shows with a Plus badge and opens the upgrade sheet.

---

### **Rollout and tracking**

---

11. **Flag and rollout**

---

Everything ships behind the workspace flag `recurring_todos`, and iOS, Android, Web and BE all ship dark first. Data turns the flag on for a sample of Plus and Team workspaces once all three clients are out, then widens it from there.

**Checklist**

- [ ] iOS, Android, Web and BE have all shipped with `recurring_todos` off
- [ ] Data turns `recurring_todos` on for a sample of Plus and Team workspaces only after iOS, Android and Web are all out
- [ ] The 10% success target is read 8 weeks after the flag is on for everyone

---

12. **Tracking**

---

Data wants two events. Yara reviews the tracking plan before client work starts, so the plan is the first thing to close.

| Event | Fires on | Event-specific property |
| --- | --- | --- |
| `todo_repeat_set` | Setting a repeat | `repeat` set to `daily`, `weekdays`, `weekly`, `monthly` or `custom` |
| `todo_occurrence_skipped` | Skip this one | None |

Both events carry the standard properties `workspace_id`, `user_id`, `platform`, `app_version` and `plan`.

**Checklist**

- [ ] Yara has reviewed the tracking plan with both events before iOS, Android or Web work starts
- [ ] `todo_repeat_set` sends `repeat` as one of `daily`, `weekdays`, `weekly`, `monthly` or `custom`
- [ ] `todo_occurrence_skipped` fires once for each Skip this one

---

### **Out of scope**

---

- Repeating a whole page or a database row
- Repeating from the date the to-do was checked off, as in every 3 days after I finish
- A different time for each weekday
- Any Support console change

> Whether a series shows its past occurrences in the to-do's activity is still open. It is not needed for the first release, and Ines decides after the flag reaches everyone.
```

Export-equivalent path: `export/NNN - task-recurring-todos.md`

```markdown
# FE - iOS - TODO - Recurring to-dos

### About

---

This subtask brings recurring to-dos to the iOS app: the Repeat and Ends pickers, the Custom interval, Skip this one and the repeat icon on the to-do row. The parent task defines the options, the Ends rules, the occurrence rules and the limit. BE creates every next occurrence, so iOS sets the repeat and shows the result.

Most iOS members read and check off to-dos on the move. That makes the check-off, and the next occurrence that replaces it, the moment this subtask has to get right.

**References**

---

Flows

- `Recurring to-dos / Repeat picker`
- `Recurring to-dos / Custom interval`
- `Recurring to-dos / Occurrence menu`

**Parent task**

---

- `FS - TODO - Recurring to-dos`

**Related tasks**

---

- `BE - TODO - Recurring to-dos`

### Requirements

---

1.  **Repeat and Ends pickers**

---

The member sets a repeat from the to-do's detail sheet. A repeat only works from a due date, so a to-do without one shows Repeat but does not let the member use it.

**Checklist**

- [ ] The detail sheet shows Repeat with Daily, Weekdays, Weekly, Monthly and Custom
- [ ] On a to-do without a due date, Repeat is greyed out with the hint `Add a due date to repeat`
- [ ] Custom sets every N days, weeks or months and accepts N from 1 to 99 only
- [ ] Ends sits under Repeat with Never, On date and After, and Never is selected by default
- [ ] After accepts 1 to 365 occurrences only

---

2.  **Occurrences on the to-do row**

---

Only one occurrence exists at a time, so the row the member checks off is followed by the next one on the same page.

**Checklist**

- [ ] A repeating to-do shows the repeat icon on its row
- [ ] Checking off an occurrence shows the next one on the same page with its next due date, assignee and reminder
- [ ] The next occurrence's reminder arrives as a local notification at the same local time as before
- [ ] Checking off the last occurrence of an On date or After series shows no next occurrence
- [ ] A teammate in another time zone sees the owner's due date with the zone shown

---

3.  **Skip this one**

---

Skip this one lets a member pass on one occurrence without marking it done. Today they get the same result by moving a reminder forward by hand.

**Checklist**

- [ ] The menu on a repeating to-do shows Skip this one
- [ ] Skip this one moves the to-do to its next due date without marking it done

---

4.  **Limit, plan and flag states**

---

**Checklist**

- [ ] When the workspace has 500 repeating to-dos that have not ended, Repeat stays visible and opens the sheet `This workspace has 500 repeating to-dos. End one to add another.`
- [ ] On a Free workspace, Repeat shows a Plus badge and opens the upgrade sheet
- [ ] With `recurring_todos` off for the workspace, Repeat, Ends, Skip this one and the repeat icon do not show
```

Export-equivalent path: `export/NNN - task-recurring-todos-ios.md`

```markdown
# FE - Android - TODO - Recurring to-dos

### About

---

This subtask brings recurring to-dos to the Android app: the Repeat and Ends pickers, the Custom interval, Skip this one and the repeat icon on the to-do row. The scope matches iOS. The parent task defines the options, the Ends rules, the occurrence rules and the limit. BE creates every next occurrence, so Android sets the repeat and shows the result.

Most Android members read and check off to-dos on the move. That makes the check-off, and the next occurrence that replaces it, the moment this subtask has to get right.

**References**

---

Flows

- `Recurring to-dos / Repeat picker`
- `Recurring to-dos / Custom interval`
- `Recurring to-dos / Occurrence menu`

**Parent task**

---

- `FS - TODO - Recurring to-dos`

**Related tasks**

---

- `FE - iOS - TODO - Recurring to-dos`
- `BE - TODO - Recurring to-dos`

### Requirements

---

1.  **Repeat and Ends pickers**

---

The member sets a repeat from the to-do's detail sheet. A repeat only works from a due date, so a to-do without one shows Repeat but does not let the member use it.

**Checklist**

- [ ] The detail sheet shows Repeat with Daily, Weekdays, Weekly, Monthly and Custom
- [ ] On a to-do without a due date, Repeat is greyed out with the hint `Add a due date to repeat`
- [ ] Custom sets every N days, weeks or months and accepts N from 1 to 99 only
- [ ] Ends sits under Repeat with Never, On date and After, and Never is selected by default
- [ ] After accepts 1 to 365 occurrences only

---

2.  **Occurrences on the to-do row**

---

Only one occurrence exists at a time, so the row the member checks off is followed by the next one on the same page.

**Checklist**

- [ ] A repeating to-do shows the repeat icon on its row
- [ ] Checking off an occurrence shows the next one on the same page with its next due date, assignee and reminder
- [ ] The next occurrence's reminder arrives as a local notification at the same local time as before
- [ ] Checking off the last occurrence of an On date or After series shows no next occurrence
- [ ] A teammate in another time zone sees the owner's due date with the zone shown

---

3.  **Skip this one**

---

Skip this one lets a member pass on one occurrence without marking it done. Today they get the same result by moving a reminder forward by hand.

**Checklist**

- [ ] The menu on a repeating to-do shows Skip this one
- [ ] Skip this one moves the to-do to its next due date without marking it done

---

4.  **Limit, plan and flag states**

---

**Checklist**

- [ ] When the workspace has 500 repeating to-dos that have not ended, Repeat stays visible and opens the sheet `This workspace has 500 repeating to-dos. End one to add another.`
- [ ] On a Free workspace, Repeat shows a Plus badge and opens the upgrade sheet
- [ ] With `recurring_todos` off for the workspace, Repeat, Ends, Skip this one and the repeat icon do not show
```

Export-equivalent path: `export/NNN - task-recurring-todos-android.md`

```markdown
# FE - Web - TODO - Recurring to-dos

### About

---

This subtask brings recurring to-dos to the web client: the Repeat and Ends pickers, the Custom interval, Skip this one and the repeat icon on the to-do row. The scope matches iOS. The parent task defines the options, the Ends rules, the occurrence rules and the limit. BE creates every next occurrence, so Web sets the repeat and shows the result.

Desktop wraps the web client, so this subtask also delivers the feature to Desktop members the next time Desktop loads, with no Desktop release. On Web and Desktop, reminders show only inside the app while it is open, and the next occurrence's reminder works the same way.

**References**

---

Flows

- `Recurring to-dos / Repeat picker`
- `Recurring to-dos / Custom interval`
- `Recurring to-dos / Occurrence menu`

**Parent task**

---

- `FS - TODO - Recurring to-dos`

**Related tasks**

---

- `FE - iOS - TODO - Recurring to-dos`
- `BE - TODO - Recurring to-dos`

### Requirements

---

1.  **Repeat and Ends pickers**

---

The member sets a repeat from the to-do's detail sheet. A repeat only works from a due date, so a to-do without one shows Repeat but does not let the member use it.

**Checklist**

- [ ] The detail sheet shows Repeat with Daily, Weekdays, Weekly, Monthly and Custom
- [ ] On a to-do without a due date, Repeat is greyed out with the hint `Add a due date to repeat`
- [ ] Custom sets every N days, weeks or months and accepts N from 1 to 99 only
- [ ] Ends sits under Repeat with Never, On date and After, and Never is selected by default
- [ ] After accepts 1 to 365 occurrences only

---

2.  **Occurrences on the to-do row**

---

Only one occurrence exists at a time, so the row the member checks off is followed by the next one on the same page.

**Checklist**

- [ ] A repeating to-do shows the repeat icon on its row
- [ ] Checking off an occurrence shows the next one on the same page with its next due date, assignee and reminder
- [ ] While the app is open, the next occurrence's reminder shows as a banner and a badge on the To-dos view at the same local time as before
- [ ] Checking off the last occurrence of an On date or After series shows no next occurrence
- [ ] A teammate in another time zone sees the owner's due date with the zone shown
- [ ] Desktop shows the same pickers, icon and menu through the web client with no Desktop release

---

3.  **Skip this one**

---

Skip this one lets a member pass on one occurrence without marking it done. Today they get the same result by moving a reminder forward by hand.

**Checklist**

- [ ] The menu on a repeating to-do shows Skip this one
- [ ] Skip this one moves the to-do to its next due date without marking it done

---

4.  **Limit, plan and flag states**

---

**Checklist**

- [ ] When the workspace has 500 repeating to-dos that have not ended, Repeat stays visible and opens the sheet `This workspace has 500 repeating to-dos. End one to add another.`
- [ ] On a Free workspace, Repeat shows a Plus badge and opens the upgrade sheet
- [ ] With `recurring_todos` off for the workspace, Repeat, Ends, Skip this one and the repeat icon do not show
```

Export-equivalent path: `export/NNN - task-recurring-todos-web.md`

```markdown
# BE - TODO - Recurring to-dos

### About

---

This subtask covers the back end of recurring to-dos: the next occurrence on check-off and on skip, Ends, the workspace limit of 500 and handing the next reminder to reminders-service. The parent task defines each rule. The clients set the repeat and show the result, so every next due date a member sees comes from this subtask.

**Parent task**

---

- `FS - TODO - Recurring to-dos`

**Related tasks**

---

- `FE - iOS - TODO - Recurring to-dos`
- `FE - Android - TODO - Recurring to-dos`
- `FE - Web - TODO - Recurring to-dos`

### Requirements

---

1.  **Next occurrence**

---

Only one occurrence of a series exists at a time. The next due date is worked out in the to-do owner's time zone, the same rule the Overdue chip and reminders follow, so the date the owner sees matches their Overdue chip.

**Checklist**

- [ ] Checking off an occurrence creates the next one on the same page, with the next due date from the option table in the parent task
- [ ] Only one occurrence of a series exists at any time
- [ ] Weekdays moves a Friday occurrence to the following Monday
- [ ] A Monthly series that starts on the 31st lands on the 30th in April and on the 31st again in May
- [ ] Custom moves the due date by N days, weeks or months, with N from 1 to 99
- [ ] The next due date is worked out in the to-do owner's time zone
- [ ] After a reassignment, the next occurrence uses the new owner's time zone
- [ ] The next occurrence keeps the assignee and the reminder, and the reminder keeps the same local time
- [ ] On check-off and on skip, the next occurrence's reminder is handed to reminders-service

---

2.  **Skip this one**

---

A skip moves the series forward without counting as done, but it still uses up one occurrence of an After limit.

**Checklist**

- [ ] Skip this one moves the to-do to its next due date without marking it done
- [ ] A skipped occurrence counts toward an After limit

---

3.  **Ends**

---

**Checklist**

- [ ] Never keeps the series going with no end
- [ ] On date creates no occurrence after the last one on or before that date
- [ ] After creates no occurrence past the set count, from 1 to 365

---

4.  **Workspace limit**

---

The limit counts live series only, so ending a series frees room for a new one.

**Checklist**

- [ ] A workspace holds at most 500 repeating to-dos that have not ended
- [ ] Setting a repeat that would take the workspace past 500 is refused, so the clients can show the limit sheet
- [ ] Checked-off and ended series do not count toward the 500

---

5.  **Flag**

---

**Checklist**

- [ ] With `recurring_todos` off for a workspace, the back end accepts no repeat on its to-dos
```

Export-equivalent path: `export/NNN - task-recurring-todos-be.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

**Quality:** All six floors pass (Completeness, Clarity, Actionability, Accuracy, Relevance, Mechanism Depth). For a task set, Actionability matters most: every checklist item names something a tester can see.

**What you're getting:** one parent task (`FS - TODO`) and four subtasks titled with the board convention. The parent covers the shared behavior, rollout, tracking and out-of-scope items. Each subtask covers only its own part. There's no Desktop subtask because Desktop gets the feature through the web client. Nothing links yet, so the parent and sibling tasks appear as plain backticked titles. You can swap in ClickUp links once the tasks exist.

**Things I added that aren't in the brief (delete any you don't want):**
- The Weekdays example (Friday moves to Monday) comes from "Monday through Friday."
- The last occurrence of an On date or After series shows no next occurrence.
- "Ship dark" means nothing about the feature shows while `recurring_todos` is off.
- The back end refuses a repeat that would go past 500.
- The Desktop check sits in the Web subtask.
- The iOS and Android local-notification checks and the Web banner check come from how reminders work in the context page.

**Gaps in the brief I didn't fill:**
- **Who sends the two tracking events?** The brief doesn't say whether the clients or BE send them, so tracking stays in the parent.
- **Does BE enforce the Plus or Team plan?** Or is the plan gate only in the clients?
- **Removing a due date:** the brief doesn't say what happens when someone removes the due date from a to-do that already repeats.

Let me know how to settle those and I'll put them into the right subtask.