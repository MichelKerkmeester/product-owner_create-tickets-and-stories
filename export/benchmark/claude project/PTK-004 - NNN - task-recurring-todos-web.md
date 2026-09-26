# FE - Web - TODO - Recurring to-dos

### About

---

This subtask brings recurring to-dos to the web client, matching the iOS scope: the Repeat and Ends pickers, the Custom interval, Skip this one and the repeat icon on the to-do row. The parent task defines the options, the Ends and occurrence rules and the limit. BE creates every next occurrence, so Web sets the repeat and shows the result.

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
- [ ] With the app open, the next occurrence's reminder shows as a banner and badge on the To-dos view at the same local time as before
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
