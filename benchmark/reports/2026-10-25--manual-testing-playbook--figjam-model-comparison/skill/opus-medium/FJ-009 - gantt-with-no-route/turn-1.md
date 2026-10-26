I haven't written anything to the board yet. Flow Mode first plays your plan back to you, then asks a separate yes before it writes.

**What I checked in Figma**
- `<test-file-key>` is a FigJam file I can open. It already holds 9 offline mode launch boards, titled "Offline mode launch", "Loomlist offline mode launch schedule" and "Loomlist offline mode launch plan". The newest is dated 26 Oct 2026 and uses the same six bars you listed.
- I'll add a new board to the right of everything on the page and delete nothing. Changing any of the existing boards would need you to name them.

**Playback: how I read your plan as a gantt chart**

| Row | Reading | Status |
|---|---|---|
| Question | Which work runs when before the offline mode release, and what sets the release date? | assumed |
| Reader | The Sync and Mobile Platform teams and Oskar (PM, Mobile), who own the offline mode epic | assumed |
| Outcome | The reader can see that design, then conflict screen build, integration and beta set the release date, and that the sync engine has one week of slack | assumed |
| Tasks | Design, 2 Nov, 2w · Sync engine, 2 Nov, 3w · Conflict screen build, after Design, 2w · Integration, after Sync engine and Conflict screen build, 1w · Beta, after Integration, 2w · Release, milestone after Beta | captured |
| Dates | Calendar weeks give: Design 2 to 15 Nov, Sync engine 2 to 22 Nov, Conflict screen 16 to 29 Nov, Integration 30 Nov to 6 Dec, Beta 7 to 20 Dec, **Release 21 Dec 2026** | assumed |
| Sections | Design · Build (Sync engine, Conflict screen build, Integration) · Launch (Beta, Release) | assumed |
| Critical path | Design, Conflict screen build, Integration and Beta are marked critical. Sync engine isn't, because it has a week of slack | assumed |
| First glance | The Release milestone | assumed |
| Sources | Your plan in chat, current direction. `context/loomlist-offline-mode-brief.md` for names only | captured |

**Questions.** If you don't answer, I'll go with the recommendation.

1. **Weeks**
   - Reading: you gave durations in weeks with no working-day rule.
   - Recommended: calendar weeks, so Release falls on Monday 21 Dec 2026.
   - Why: the plan states no holidays or weekend exclusions, and the chart can't draw them anyway.
2. **What the board leaves out**
   - Reading: your plan names no owners, platforms or beta audience. The older boards in the file show "Desktop and iOS integration" and "Beta for 5 percent of workspaces".
   - Recommended: use your words only, with no owners, platforms or beta size, and don't copy them from the older boards.
   - Why: I can't tell which of those boards, if any, is still current.
3. **Target conflict**
   - Reading: the brief from 23 Sep targets Q1 2027, but your plan releases on 21 Dec 2026.
   - Recommended: your plan sets the dates, and the board's source line says it came from your plan of 26 Oct 2026.
   - Why: your plan is newer and more specific. The brief's target stays on record in the brief.

Does this reading hold, or what should change? Once it's settled, I'll show you the checked chart, the target file and the rollback for a separate yes before anything is written.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.