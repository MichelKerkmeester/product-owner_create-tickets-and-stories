I've written the epic. It has one child story for each of Oskar's four areas, and each story covers iOS, Android and Desktop together.

Path: `export/002 - Epic-offline-mode.md`
Verified: read-back succeeded; 106 lines
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

**What's in it:** The Problem and Goal use the figures from Oskar's brief (23% of sessions, 31% of Plus cancellation reasons, `lost-edit` tickets). The Goal also carries his two success measures. The About section says it's for every plan, Free included, with a Q1 2027 target. The Scope section splits the four stories into two groups:
- **Starts now:** Offline reading, and Offline indicator and storage settings.
- **Waits on Joana's decision on 2026-10-09:** Offline editing and creation, and Sync on reconnect.

There are three release-level acceptance criteria and no delivery section, because you didn't ask for one.

**Choices I made where your reply was silent:**
- **Conflict handling:** I wrote the epic now instead of waiting. It names Joana's decision as still open, and no acceptance criterion depends on how conflicts get resolved.
- **Web and the sync protocol:** If Joana's decision changes sync protocol v3, the Web client would also need an update. The Scope section says it's undecided whether that belongs to this epic.
- **Guests:** The title reads `Member` because the brief says "a member". Guest access to offline pages isn't covered, so tell me if Guests should be included.

**Left for the child stories:** The brief's exact limits (500 pages, 1 GB, 30 seconds) belong in the child stories. I left them out of the epic's acceptance criteria so the criteria don't have to change if a limit does. The child story names are plain text, since the stories don't exist yet.

Next, I can write any of the four child stories. Offline reading is a good first one because it doesn't wait on Joana's decision.