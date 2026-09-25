I've written the FE task for the date picker stay limits and saved it to the export folder.

Path: `export/001 - task-date-picker-stay-limits.md`
Verified: read-back succeeded; 165 lines
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

**Quality:** The task follows the standard task template and its title follows your naming format: `FE - Guest app - SRCH - Date picker stay limits`. All the numbers and exact copy from Ines's notes are in it, and nothing new was added. On the second check I fixed two claims the notes don't support. The notes only say iOS and Android use the design system calendar, not web. They also never name that component, so the task no longer gives it one.

**Summary:** The task explains the problem: search-service rejects stays over 30 nights, guests only find out after tapping Search, and Guest Support logged 23 chats about it in August. It then lists 8 groups of checks: the limits, the property minimum stay, the three picker states, the helper text, the six copy keys, the edge cases, screen readers and layout per platform. It covers iOS, Android and web, because your conventions say "Guest app" means all three. Flexible dates, prices per night in the calendar and tracking changes are listed as not in this task.

Two gaps worth closing before the task is picked up:
- **Where the limits come from:** the notes say the 30-night and 365-day limits come from search-service settings and the minimum stay comes with the property details. They don't say whether the apps and web can already read these values. If they can't, back-end work is needed first.
- **Disabled days:** the notes say what happens when a guest taps a grey day. They don't say what happens when a guest taps a disabled day (a past day, or more than 365 days out), so the task doesn't define that.

If you want this in ClickUp, I can push it once you say so.