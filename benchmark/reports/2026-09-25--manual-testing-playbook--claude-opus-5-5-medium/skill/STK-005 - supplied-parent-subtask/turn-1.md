I wrote the Android subtask from the parent's shared rules. No clarification was needed because the parent already names this subtask and its title.

Path: `export/001 - task-android-recurring-todos-subtask.md`
Verified: read-back succeeded; 161 lines
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

**Quality summary:** Standard energy, checked from the user, business, technical and risk angles. It uses the subtask template with H3 sections, `---` dividers and `- [ ]` checklists. The parent and sibling tasks are listed as plain text in backticks because the parent gives no links. Every value comes from the parent, including the 1–99 custom interval, the 1–365 After limit, the 500-series limit with its exact wording, the flag name and both events.

**Summary:** The subtask covers what Android members see and do: the Repeat picker, custom interval, Ends options, check-off and Skip this one, the workspace limit, the Free plan badge, the flag, time zone display and the two tracking events. Working out next due dates is left to the recurrence engine subtask.

**Things I added that the parent doesn't state (remove any you don't want):**
- A check that "Weekdays" always means Monday through Friday, whatever day the app language starts its week on
- A check that the next reminder fires as a phone notification at the same local time. I based this on the board context, which says Android schedules reminders on the device
- A check that no next occurrence appears after an On date or After series has ended
- A check that with `recurring_todos` off, Android shows none of the feature
- The standard event properties and `user_id` hashing, taken from the board's analytics conventions

**Open points for Ines or Oskar:**
- The parent says Free workspaces open "the upgrade sheet", but the board context says plans can only be changed on Web. I kept the parent's wording and didn't guess what the Android sheet does.
- Neither source says whether Guests with edit access can set a repeat.
- Neither source mentions translations of the two new messages for the six app languages.

I can refine this or add a follow-up for any of those points.