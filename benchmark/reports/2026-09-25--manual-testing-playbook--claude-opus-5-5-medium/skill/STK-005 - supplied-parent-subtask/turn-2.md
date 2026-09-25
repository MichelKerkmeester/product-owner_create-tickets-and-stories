I've updated the subtask with your details. It's still saved under the same filename.

Path: `export/001 - task-android-recurring-todos-subtask.md`
Verified: read-back succeeded; 164 lines
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

**What changed:**
- **Scope:** The About now covers phones and tablets. The Repeat picker section has a new check that the picker, custom interval and Ends options work on both.
- **Release:** Oskar's team takes it into 5.4.0. It still ships hidden behind `recurring_todos`, and Data turns that on once all three apps are out.
- **Due dates:** The About says BE builds the recurrence engine in parallel. The checks for checking off, skipping and reassigning now say the app shows the next due date BE returns. A new check says the app never works one out on the device. The 31 March → 30 April → 31 May example now checks what BE returns.
- **Removed:** I dropped my earlier check that "Weekdays" means Monday to Friday in every language. That was about how dates are worked out, which is now BE's job, so it belongs in the engine subtask.

**One addition to confirm:** The About now says end-to-end tests of occurrences have to wait until the engine can be tested against. That follows from the parallel build, but you didn't state it, so remove it if the team has a mock or another way to test.

**Still open from last time:**
- What the upgrade sheet does on Android, since plans can only be changed on Web.
- Whether Guests with edit access can set a repeat.
- Translations of the two new messages.