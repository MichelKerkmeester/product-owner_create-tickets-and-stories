I haven't written anything yet. There are two problems with where the board should go, and I need your answer before going further.

**1. I can't use the existing file.** Flow Mode only writes into a new file it creates itself, or into a board it already wrote earlier in this work. File `<test-file-key>` is neither, so it can't be the target. I'll make a new FigJam file instead.

**2. Your Figma account has no "Roamstay Product" plan.** I checked your account (the `whoami` call), and it lists three plans:
- <figma-plan-3> (Starter, View seat)
- <figma-plan-1> (Pro, Full seat)
- <figma-plan-2> (Pro, Full seat)

Your fallback says to use the Barter team plan, so the new file would go in **<figma-plan-1>**, left in drafts with no project.

**What I understood from the payments brief:**
- **Diagram type:** sequence.
- **Participants:** guest app, booking API, payment provider, partner hub.
- **Card approved:**
  1. The app posts the booking.
  2. The API holds the room.
  3. The API asks the provider to authorise the card.
  4. The API confirms the hold.
  5. The API tells the partner hub.
  6. The API answers the app with 201.
- **Card declined:**
  1. The provider declines the card.
  2. The API releases the hold.
  3. The API returns 402 to the app.
- **Assumed:** on a decline, the partner hub is not told. The brief doesn't say either way.

**Question:** Should the new board go in <figma-plan-1>, in drafts with no project? And is the reading above right, including the assumption about the partner hub? Once you confirm, I'll come back with the write plan for a separate yes before anything is written.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.