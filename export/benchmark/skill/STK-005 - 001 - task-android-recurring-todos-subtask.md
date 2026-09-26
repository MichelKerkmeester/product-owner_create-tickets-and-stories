# FE - Android - TODO - Recurring to-dos

### About

---

This subtask brings recurring to-dos to Android phones and tablets and covers what Android members see and do, under the parent task's shared rules. Oskar's team takes it into the 5.4.0 release, and it ships dark behind the workspace flag `recurring_todos`, which Data turns on once iOS, Android and Web are out.

BE builds the recurrence engine in parallel, and the engine works out every next due date. The app shows the next due date BE returns and never works one out on the device, so one series always shows the same dates on every surface. End-to-end checks on occurrences wait until the engine is available to test against.

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
- `FE - Web - TODO - Recurring to-dos`
- `BE - TODO - Recurrence engine`

### Requirements

---

### **Setting a repeat**

---

1.  **Repeat picker**

---

Repeat sits on the to-do's detail sheet. It only works on a to-do with a due date, because every next occurrence is counted from the due date.

**Checklist**

- [ ] Repeat shows on the to-do's detail sheet
- [ ] On a to-do without a due date, Repeat is greyed out with the hint `Add a due date to repeat`
- [ ] The picker offers Daily, Weekdays, Weekly, Monthly and Custom
- [ ] The Repeat picker, the custom interval and the Ends options work on phones and on tablets

2.  **Custom interval**

---

Custom lets the member repeat every N days, weeks or months.

**Checklist**

- [ ] The member picks days, weeks or months and a value of N
- [ ] N accepts 1 to 99 and nothing outside that range

3.  **Ends**

---

A series runs until the member ends it, unless they pick an end when they set the repeat.

**Checklist**

- [ ] Never is selected by default
- [ ] On date stops the series after the last occurrence on or before the chosen date
- [ ] After stops the series after a set number of occurrences, from 1 to 365

### **Occurrences**

---

4.  **Check off and the next occurrence**

---

Only one occurrence exists at a time. Checking it off brings the next one onto the same page, so the member never has to recreate the to-do.

**Checklist**

- [ ] Checking off an occurrence shows the next one on the same page with the next due date BE returns
- [ ] The app never works out a next due date on the device
- [ ] The next occurrence keeps the assignee
- [ ] The next occurrence keeps the reminder, and its local notification fires at the same local time as before
- [ ] A Monthly series that starts on 31 March shows 30 April, then 31 May, as BE returns them
- [ ] No next occurrence appears once an On date or After series has ended

5.  **Skip this one**

---

Skip moves a repeating to-do to its next due date without marking it done. It still uses up one occurrence of an After limit, so a skipped occurrence is never a free extra.

**Checklist**

- [ ] Skip this one sits in the menu of a repeating to-do
- [ ] Skipping moves the to-do to the next due date BE returns and does not mark it done
- [ ] A skip counts toward an After limit

### **Limits and access**

---

6.  **Workspace limit**

---

A workspace holds at most 500 repeating to-dos that have not ended. Checked-off and ended series do not count toward the 500.

**Checklist**

- [ ] At the limit, Repeat stays visible
- [ ] At the limit, Repeat opens a sheet that says `This workspace has 500 repeating to-dos. End one to add another.`

7.  **Plans and flag**

---

Repeat is for Plus and Team workspaces. A Free workspace still sees it, so the member learns the feature exists.

**Checklist**

- [ ] On Free, Repeat shows with a Plus badge and opens the upgrade sheet
- [ ] On Plus and Team, Repeat opens the picker
- [ ] With `recurring_todos` off for the workspace, Android shows no Repeat, no Skip this one and no recurring behavior

### **Time zone and tracking**

---

8.  **Owner's time zone**

---

Next due dates follow the to-do owner's time zone, so a to-do reassigned across zones moves to the new owner's zone from its next occurrence.

**Checklist**

- [ ] A teammate in another zone sees the owner's due date with the zone shown
- [ ] After a reassignment, the next occurrence shows the due date BE returns in the new owner's zone

9.  **Tracking**

---

Both events are in the tracking plan Yara reviewed on 2026-09-16.

**Checklist**

- [ ] `todo_repeat_set` fires when a repeat is set, with `repeat` set to `daily`, `weekdays`, `weekly`, `monthly` or `custom`
- [ ] `todo_occurrence_skipped` fires on Skip this one
- [ ] Both events carry `workspace_id`, `user_id`, `platform`, `app_version` and `plan`, with `user_id` hashed before it leaves the device
