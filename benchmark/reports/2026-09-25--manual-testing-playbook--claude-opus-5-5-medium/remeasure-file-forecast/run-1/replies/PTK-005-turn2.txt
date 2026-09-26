```markdown
# FE - Android - TODO - Recurring to-dos

### About

---

This subtask covers recurring to-dos in the Android app on phones and tablets. It is part of the parent task `FS - TODO - Recurring to-dos`, which sets the shared rules once for every client. A member can make a to-do with a due date repeat on a schedule they pick. When they check off or skip one occurrence, the next one appears with the next due date.

The engine is built in parallel in `BE - TODO - Recurrence engine`. Android shows the next due date the engine returns and never works one out on the device, so every client shows the same date for the same occurrence. Oskar's team takes this into Android 5.4.0. It ships dark behind the workspace flag `recurring_todos`, and Data turns the flag on once iOS, Android and Web are out.

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

### **Repeat on the detail sheet**

---

1.  **Repeat options**

---

A member sets Repeat from the to-do's detail sheet. Only a to-do with a due date can repeat, because the engine counts every next due date from the current one.

**Checklist**

- [ ] Repeat shows on the to-do's detail sheet
- [ ] A to-do without a due date shows Repeat greyed out with the hint `Add a due date to repeat`
- [ ] The picker offers Daily, Weekdays, Weekly, Monthly and Custom
- [ ] Custom sets an interval of every N days, weeks or months, with N from 1 to 99
- [ ] Every next due date on screen is the one the engine returns, and the app never works one out on the device

2.  **Ends**

---

A member decides when a series stops. The engine applies the end rule, and Android offers the three choices and sends the one the member picks.

**Checklist**

- [ ] Ends offers Never, On date and After
- [ ] Never is selected by default
- [ ] On date lets the member pick the date after which no new occurrence is created
- [ ] After accepts a number of occurrences from 1 to 365

---

### **Occurrences**

---

3.  **Check off and Skip this one**

---

Only one occurrence of a series exists at a time. The member moves the series forward by checking off the current occurrence or by skipping it.

**Checklist**

- [ ] Checking off an occurrence shows the next one on the same page with the next due date the engine returns
- [ ] The next occurrence keeps the assignee and the reminder of the one before it
- [ ] The reminder for the next occurrence fires at the same local time as the one before it
- [ ] Skip this one sits in the to-do's menu
- [ ] Skip this one moves the to-do to its next due date without marking it done
- [ ] A monthly series that starts on the 31st shows the 30th in April and the 31st again in May, as returned by the engine

4.  **Time zone**

---

Next due dates follow the to-do owner's time zone, so a teammate in another zone sees the same date the owner sees.

**Checklist**

- [ ] A teammate in a different time zone from the owner sees the owner's date with the owner's zone shown
- [ ] After the to-do is reassigned, the next occurrence shows the date the engine returns for the new owner's zone

---

### **Limit, plans and rollout**

---

5.  **Workspace limit**

---

A workspace can hold at most 500 repeating to-dos that have not ended. Checked-off and ended series do not count toward the limit.

**Checklist**

- [ ] At the limit, Repeat stays visible
- [ ] At the limit, tapping Repeat opens a sheet that says `This workspace has 500 repeating to-dos. End one to add another.`

6.  **Plans**

---

Repeat is available on Plus and Team workspaces.

**Checklist**

- [ ] On Plus and Team workspaces, Repeat works as described in this subtask
- [ ] On Free workspaces, Repeat shows with a Plus badge and opens the upgrade sheet

7.  **Flag and devices**

---

This subtask ships in Android 5.4.0 behind `recurring_todos`, so no member sees Repeat before Data turns the flag on.

**Checklist**

- [ ] With `recurring_todos` off, the app shows no Repeat control and no Skip this one
- [ ] With `recurring_todos` on, every flow in this subtask works on phones and tablets
- [ ] Every flow works from Android 9, the app's minimum OS

---

### **Tracking**

---

8.  **Events**

---

Both events are in the tracking plan Yara reviewed on 2026-09-16.

**Checklist**

- [ ] `todo_repeat_set` fires when a member sets Repeat, with `repeat` set to `daily`, `weekdays`, `weekly`, `monthly` or `custom`
- [ ] `todo_occurrence_skipped` fires on Skip this one
- [ ] Both events carry `workspace_id`, `user_id`, `platform`, `app_version` and `plan`, with `user_id` hashed before it leaves the device
```

Export-equivalent path: `export/002 - task-android-recurring-todos.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

**Quality:** Passes. Each checklist item is something QA can test on Android. Every value comes from the parent, the board context or your answer. The subtask covers what Android shows and does, and leaves how the engine calculates dates to `BE - TODO - Recurrence engine`.

**What I added that you didn't ask for (remove any you don't want):**
- **Android 9:** every flow must work from Android 9, the app's minimum OS on the board context page.
- **Flag off:** with `recurring_todos` off, the app shows no Repeat control and no Skip this one. The parent only says the feature ships behind the flag.
- **Event properties:** both events carry the standard properties, and `user_id` is hashed. This follows the board's analytics conventions.
- **The 31st check:** a monthly series starting on the 31st shows the 30th in April. This is the parent's example, used here to check that Android shows the engine's date.

**Still open, so they're not in the subtask:**
- **Upgrade sheet:** billing changes can only be made on Web. The subtask only says the Plus badge opens the upgrade sheet, without saying what that sheet does on Android.
- **Offline check-off:** there's no offline mode. It's still unclear whether the next occurrence appears right after a check-off or only once the engine confirms it.
- **Guests with edit access:** it's unclear whether they can set Repeat.
- **Figma links:** there are none yet, so the three flows are listed as plain names.
- **Translations:** there's no translated copy for the hint or the limit sheet. Without it, those strings fall back to en-US.

The ClickUp connector isn't available in this session, so I can't publish this to ClickUp from here.