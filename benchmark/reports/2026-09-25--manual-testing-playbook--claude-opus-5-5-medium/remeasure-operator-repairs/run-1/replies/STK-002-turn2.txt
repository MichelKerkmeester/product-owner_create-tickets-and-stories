I've written the task: `FE - Guest app - SRCH - Date picker stay limits`. It's one task for iOS, Android and web, with no parent, scheduled for the Search squad's 8.13.0 train. search-service stays as it is, and its own 30-night check remains the backstop.

Path: `export/002 - task-date-picker-stay-limits.md`
Verified: read-back succeeded; 178 lines
HVR self-scan: 1 hard blocker. Fixed: Oxford comma in the "Not in this task" line. Kept with reason: none.

**Quality:** it checks out against the task template's structure and dividers. Every limit, piece of copy and screen state comes from Ines's notes, and every button and helper-text string is quoted exactly as written there. QA sign-off covers all three platforms in en-GB and en-US.

The task has nine requirement groups. They cover the limits and where their values come from, the button states, what happens when a guest taps a greyed-out day, the six copy keys, and dates carried over from an earlier search. They also cover screen readers, the layout on each platform and QA sign-off.

**Two things you didn't answer:**
- **Property minimum stay:** the conflict is still open. The Roamstay context file says the property page already applies it, while Ines's notes say it's new. I didn't take a side: the task says what the picker must do, not what it does today. The About section now only states the part both sources agree on, that the picker allows ranges over 30 nights.
- **Figma link:** you didn't send one, so the `Date picker / Stay limits` frame is named in plain text with no URL. There's no epic either.

**My additions for you to check:**
- The user story's "35 nights later" example is mine.
- The final QA item, which says to check the week start, the greyed-out days past 30 nights and the highlight across a month break in both locales, is also mine.
- I assumed the apps already receive the 30-night limit, the 365-day window and the property minimum, since search-service isn't changing. If they don't, this task needs a back-end ticket first.
- **Missing from the design:** the notes don't say what helper text appears when a guest taps a greyed-out check-in day beyond 365 days. Ines needs to answer that before build.

Next step: send me the Figma link and the answer on the minimum stay, and I'll update the same file.