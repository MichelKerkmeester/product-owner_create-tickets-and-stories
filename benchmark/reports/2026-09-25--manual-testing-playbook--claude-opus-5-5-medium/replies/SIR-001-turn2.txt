I've written the Epic (the parent item that the four child stories will sit under). The point value and who pays for points appear only as undecided, with no number on either.

Path: `export/002 - Epic-guest-loyalty-points.md`
Verified: read-back succeeded; 103 lines
HVR self-scan: 0 hard blockers. Fixed: two three-item lists bunched together in the opening paragraph. Kept with reason: none.

**Quality summary:** your 19% → 25% by end of 2027 goal, the four child stories and the Pay now-only rule are carried over exactly, with platforms stated as iOS, Android and web. The check that should run on the file before it ships isn't in this folder (the `z — Claude Project Sync Loop` directory is missing), so the format was checked by hand only.

The Epic sets out the problem, the goal, how you'll get there and the four child stories, named as plain text because none exist yet. It ends with four acceptance criteria (the outcomes the finished work must deliver), one per child story. I left out a Delivery section (estimates, risks, exclusions) because you didn't ask for one. I didn't add links either, since you didn't supply any.

**Things I added that you didn't give me.** Strike any that are wrong:
- Only signed-in guests can join, since joining happens from Account.
- A stay cancelled before it's completed earns no points.
- Membership shows the same on iOS, Android and web.
- The history lists spent points as well as earned ones.

**Gaps you may want as more child stories or decisions:**
- **Email-only guests:** people who book with just an email address, without signing in, have no route to join.
- **Cancelled bookings paid with points:** nothing says what happens to the points.
- **Measuring the goal:** no story sets up the tracking to measure the 19% → 25% goal.