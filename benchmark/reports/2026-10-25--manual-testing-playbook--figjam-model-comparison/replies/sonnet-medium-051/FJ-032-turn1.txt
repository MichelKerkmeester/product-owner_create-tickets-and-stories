I'm drawing this as a state diagram, since your text gives states and the events that move a booking between them. This is round 1 of 3. Nothing is written to the board yet. I'll read `<test-file-key>` once before the write gate. The new board will sit beside what's already there, and nothing existing will change.

**What I've read so far**
* States: Pending, Confirmed (containing Upcoming and In stay), Completed, Cancelled, No-show
* Source: your message only, so each row stays assumed until round 3

**1. Reader, question and outcome**
Reading: it's a retro board, so the readers are the team that ran the retro. Your text answers which states exist and what moves a booking between them.
Question: who reads this, and what should they be able to decide afterwards?
Recommended: the Roamstay product and engineering team, agreeing the status values and allowed moves before a story is written.
Why: you gave states and triggers, with no screens or steps.

**2. What the board must not do**
Reading: you named seven moves and no failure paths.
Question: what must this board not do?
Recommended: draw nothing you didn't state, so no authorisation failure, refund or booking change.
Why: a move the source doesn't state would read as agreed behaviour.

**3. Detail, audience and reading distance**
Reading: you stated none of the three.
Question: how detailed should it be, who is it written for, and where will it be read?
Recommended: Balanced detail, Mixed audience and Laptop distance.
Why: it's a status field read at a desk by product and engineering together.

Take the recommended answers, or correct any of them?