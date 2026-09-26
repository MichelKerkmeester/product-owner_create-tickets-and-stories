# FE - Android - TODO - Recurring to-dos

## About

---

This brings recurring to-dos to the Android app, matching the iOS scope. The parent task defines the rules, and BE creates every next occurrence, so Android sets the repeat and shows the result.

Most Android members check off to-dos on the move, so the check-off and the next occurrence matter most.

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

**Checklist**

- [] The detail sheet shows Repeat with Daily, Weekdays, Weekly, Monthly and Custom
- [] Without a due date, Repeat is greyed out with the hint `Add a due date to repeat`
- [] Custom sets every N days, weeks or months, N from 1 to 99 only
- [] Ends sits under Repeat with Never, the default, On date and After, which accepts 1 to 365 occurrences only

---

2.  **Occurrences on the to-do row**

---

**Checklist**

- [] A repeating to-do shows the repeat icon on its row
- [] Checking off an occurrence shows the next on the same page, with its due date, assignee and reminder
- [] The next occurrence's reminder arrives as a local notification at the same local time
- [] The last occurrence of an On date or After series has no next one
- [] A teammate in another time zone sees the owner's due date and zone

---

3.  **Skip this one**

---

**Checklist**

- [] A repeating to-do's menu shows Skip this one, which moves it to its next due date without marking it done

---

4.  **Limit, plan and flag states**

---

**Checklist**

- [] At 500 unended repeating to-dos, Repeat stays visible and opens the sheet `This workspace has 500 repeating to-dos. End one to add another.`
- [] On a Free workspace, Repeat shows a Plus badge and opens the upgrade sheet
- [] With `recurring_todos` off, Repeat, Ends, Skip this one and the repeat icon do not show
