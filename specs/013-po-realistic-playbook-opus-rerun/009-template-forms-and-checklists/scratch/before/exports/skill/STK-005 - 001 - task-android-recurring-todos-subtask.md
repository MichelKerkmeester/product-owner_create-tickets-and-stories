# FE - Android - TODO - Recurring to-dos

### About

---

Recurring to-dos come to Android phones and tablets under the parent task's shared rules. Oskar's team ships it in 5.4.0, dark behind the workspace flag `recurring_todos`, which Data turns on once iOS, Android and Web are out.

BE's parallel recurrence engine works out every next due date, so a series shows the same dates everywhere. End-to-end occurrence checks wait for the engine.

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

Repeat needs a due date, because occurrences count from it.

**Checklist**

- [ ] Repeat is on the to-do's detail sheet
- [ ] Without a due date, Repeat is greyed out with the hint `Add a due date to repeat`
- [ ] It offers Daily, Weekdays, Weekly, Monthly and Custom
- [ ] The picker, custom interval and Ends options work on phones and tablets

2.  **Custom interval**

---

**Checklist**

- [ ] The member picks days, weeks or months and N
- [ ] N accepts only 1 to 99

3.  **Ends**

---

**Checklist**

- [ ] Never is the default, so a series runs until the member ends it
- [ ] On date stops after the last occurrence on or before the chosen date
- [ ] After stops after 1 to 365 occurrences

### **Occurrences**

---

4.  **Check off and the next occurrence**

---

Only one occurrence exists at a time. Checking it off brings the next one onto the same page, so the member never recreates the to-do.

**Checklist**

- [ ] Checking one off shows the next on the same page, with the due date BE returns
- [ ] The app never works out a due date on the device
- [ ] The next occurrence keeps the assignee
- [ ] It keeps the reminder, whose local notification fires at the same local time
- [ ] A Monthly series from 31 March shows 30 April, then 31 May, as BE returns them
- [ ] No next occurrence appears after an On date or After series ends

5.  **Skip this one**

---

**Checklist**

- [ ] Skip this one is in a repeating to-do's menu
- [ ] Skipping moves to the next due date BE returns without marking it done
- [ ] A skip counts toward an After limit, so it is never a free extra

### **Limits and access**

---

6.  **Workspace limit**

---

A workspace holds at most 500 unended repeating to-dos, not counting checked-off and ended series.

**Checklist**

- [ ] At the limit, Repeat stays visible and opens a sheet that says `This workspace has 500 repeating to-dos. End one to add another.`

7.  **Plans and flag**

---

Repeat is for Plus and Team, and Free sees it so members learn it exists.

**Checklist**

- [ ] On Free, Repeat shows with a Plus badge and opens the upgrade sheet
- [ ] On Plus and Team, Repeat opens the picker
- [ ] With `recurring_todos` off, Android shows no Repeat, Skip this one or recurring behavior

### **Time zone and tracking**

---

8.  **Owner's time zone**

---

Due dates follow the to-do owner's time zone.

**Checklist**

- [ ] A teammate in another zone sees the owner's due date and zone
- [ ] After reassignment, the next occurrence shows the BE due date in the new owner's zone

9.  **Tracking**

---

Both events are in the tracking plan Yara reviewed on 2026-09-16.

**Checklist**

- [ ] `todo_repeat_set` fires on setting a repeat, with `repeat` as `daily`, `weekdays`, `weekly`, `monthly` or `custom`
- [ ] `todo_occurrence_skipped` fires on Skip this one
- [ ] Both carry `workspace_id`, `user_id`, `platform`, `app_version` and `plan`, with `user_id` hashed on the device
