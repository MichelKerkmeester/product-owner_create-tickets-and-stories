# FE - Android - TODO - Recurring to-dos

## About

---

Members on Android phones and tablets can set a to-do to repeat, choose when the series ends, and skip or check off an occurrence. Android shows each next due date that the recurrence engine returns and never works one out on the device. The shared rules sit in the parent task, `FS - TODO - Recurring to-dos`, and the engine is built in parallel as `BE - TODO - Recurrence engine`.

This subtask ships in Android 5.4.0, which Oskar's Mobile Platform team takes into release. Every requirement below must hold on phones and on tablets.

**References**

---

Flows

- `Recurring to-dos / Repeat picker`
- `Recurring to-dos / Custom interval`
- `Recurring to-dos / Occurrence menu`

**Parent task**

---

- `FS - TODO - Recurring to-dos`

### Requirements

---

### **Repeat on the to-do**

---

1.  **Repeat entry point**

---

Repeat sits on the to-do's detail sheet. Without a due date it shows greyed out, so the member sees what to add first.

**Checklist**

- [] Repeat sits on the to-do's detail sheet
- [] A to-do without a due date shows Repeat greyed out with the hint `Add a due date to repeat`

2.  **Repeat picker**

---

The picker sets how often the to-do repeats.

**Checklist**

- [] The picker offers `Daily`, `Weekdays`, `Weekly`, `Monthly` and `Custom`
- [] `Custom` takes an interval of days, weeks or months, with N from 1 to 99

3.  **Ends**

---

The member picks when the series stops. The default is no end.

**Checklist**

- [] The Ends choice offers `Never`, `On date` and `After`, with `Never` as the default
- [] `After` takes a count from 1 to 365

---

### **Occurrences**

---

4.  **Check off and skip**

---

Checking off or skipping an occurrence moves the to-do on to its next occurrence. Skipping does not mark the to-do done.

**Checklist**

- [] Checking off an occurrence shows the new occurrence with its next due date
- [] The to-do's menu offers `Skip this one`
- [] `Skip this one` moves the to-do to its next due date without marking it done

---

### **Due dates**

---

5.  **Next due date from the engine**

---

The app shows the due date the recurrence engine returns for each occurrence. It does not derive a due date from the repeat rule.

**Checklist**

- [] Each occurrence shows the next due date that the recurrence engine returns
- [] The app never computes a next due date on the device, for any repeat option
- [] A member viewing a to-do owned by someone in another time zone sees the owner's date, with the zone shown when it differs from their own

---

### **Limit and plan**

---

6.  **Repeat limit**

---

A workspace holds at most 500 repeating to-dos that have not ended.

**Checklist**

- [] At the limit, Repeat stays visible and opens a sheet with the text `This workspace has 500 repeating to-dos. End one to add another.`

7.  **Plan access**

---

Repeat is for Plus and Team workspaces.

**Checklist**

- [] On Plus and Team workspaces, Repeat opens the repeat picker
- [] On a Free workspace, Repeat shows a Plus badge and opens the upgrade sheet

8.  **Workspace flag**

---

The repeat rules ship dark behind one workspace flag.

**Checklist**

- [] Repeat stays hidden while the workspace flag `recurring_todos` is off
