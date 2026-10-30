Playback of what your request settles so far:

- **Type:** state diagram, because you ask which statuses a booking passes through and what moves it between them
- **Entry:** Pending
- **Exit:** Completed, Cancelled and No-show
- **States:** Pending, Confirmed (a section holding Upcoming and In stay), Completed, Cancelled and No-show
- **Moves:** card authorised, check-out, guest cancel from Pending or Confirmed, and the hotel marking No-show after a missed check-in
- **Guards from the booking doc:** 15 minutes at most in Pending, a cancel within 48 hours of check-in keeps the first night's price, and No-show from 6 hours after the check-in time
- **Target:** retro board `<test-file-key>`, added as a new section beside what it holds, with nothing already there changed
- **Source:** your message and the three doc lines you quoted. The doc itself is not attached, so I treat those lines as current behavior (assumed)

Two gaps will come up in round two, so you can think about them now. The sources do not say what happens when the 15 minutes pass without an authorised card. They also do not name the trigger from Upcoming to In stay. I will not invent an Expired state or a trigger without your say.

**1. Reader and outcome**
Reading: the board goes on a retro board, but nothing names who reads it.
Question: Who reads it, and what should they decide or do afterwards?
Recommended: the retro team, agreeing what each status means and what moves a booking between them.
Why: it is a status field, and a shared reading of it should come before any story is written.

**2. What the board must not do**
Reading: your lines cover seven statuses and three guards, and say nothing about refund amounts, payment retries or a failed card check.
Question: What must this board not do?
Recommended: leave out refund amounts, payment retries and the failed-card path, and list them under `Left out:`.
Why: the board then draws only what the sources state.

**3. Dials**
Reading: a retro board is usually shared on a call.
Question: Which detail level, audience and reading distance?
Recommended: Balanced, Mixed and Meeting screen. The guards sit in short state notes, and labels stay under 32 characters.
Why: Balanced keeps the 15 minute, 48 hour and 6 hour rules on the board without crowding the transitions.

Take the recommended answers, or correct any of them?