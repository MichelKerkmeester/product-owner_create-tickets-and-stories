Reading the retro board is done, so here is how I read your request before I draw anything.

The board has one section, "Sprint retro", with 6 gray stickies. Nothing on it shares a title with this diagram, so the lifecycle would land as a new section beside it and leave those stickies as they are.

**Question:** which statuses can a Roamstay booking have, and what moves it between them?
**Type:** a state diagram, because the question is about statuses and the moves between them.
**Outcome:** a reader can see every status, which ones end a booking and who or what triggers each move.

**Settled by your message**
- Pending is where a booking starts, and Pending moves to Confirmed when the card is authorised
- Confirmed is one group holding Upcoming and In stay
- Check-out ends the booking as Completed
- A guest can cancel from Pending or from Confirmed, which gives Cancelled
- The hotel marks No-show after a missed check-in

That is 7 states and 6 moves. Completed, Cancelled and No-show are the end states.

**Assumed, so correct any of these**
- The reader is the product team, at balanced detail with a mixed audience, read on a laptop. Recommended because nothing says otherwise.
- Upcoming moves to In stay on "check in". You never name this move, but "missed check-in" implies it.
- Check-out is taken from In stay, because a guest has to be in the stay to leave it.
- No-show is taken from Upcoming, because that is the state a missed check-in happens in.
- The board shows no timing rule for No-show, such as how long after the check-in date. You gave none, so I won't invent one.

**Left out:** payments and refunds, because the sources don't state them. Hotel-side screens are left out too, because this board is the lifecycle only.

**Still open:** "Confirmed" covers In stay, so a guest could cancel mid-stay as you wrote it. I'd draw it exactly as stated and not add a guard. Tell me if cancelling should stop at Upcoming.

Is this the right reading of the board?