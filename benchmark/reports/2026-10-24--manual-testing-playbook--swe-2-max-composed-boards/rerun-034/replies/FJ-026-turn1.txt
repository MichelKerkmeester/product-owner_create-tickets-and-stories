Before I draw anything, this is how I read your request. I've drawn nothing and called no Figma tool yet.

**Question:** which statuses can a Roamstay booking have, and what moves it between them?
**Outcome:** support can read every booking status and spot the ones a booking ends in.
**Type:** a state diagram, because the question is about statuses and the events between them.

**Settled by your message** (all current behavior):
* Pending until the card is authorised, then Confirmed
* Confirmed holds Upcoming and In stay, and check-in moves Upcoming to In stay
* Check-out ends the booking as Completed
* A guest can cancel while Pending or Confirmed
* The hotel marks No-show after a missed check-in

**Colour:** a state diagram cannot take colour from the model. The composer already draws every state a booking ends from in light gray and names it "Final state" in the key. Completed, Cancelled and No-show will therefore stand out from the blue Pending and the white Confirmed states, but all three share one gray. A red for Cancelled and No-show would be a hand edit in FigJam after the write.

**Target:** a new board section in the existing file `<test-file-key>`, with no new file. It lands 400 pixels to the right of whatever the file holds. I take the Roamstay Product plan as you said it, because a file key doesn't tell me which plan owns the file.

**Three points to confirm:**
1. **Framing.** Reading: the diagram checker only lets a move leave a composite from the composite itself, never from Upcoming or In stay. Recommended: draw Confirmed as a composite, with check-out, cancel and missed check-in all leaving Confirmed. Why: it keeps your word "Confirmed" on the board. The cost is that the board can't show that check-out starts only from In stay and No-show only from Upcoming. The alternative is a flat machine with no Confirmed state, which is exact about those two moves but drops your grouping.
2. **Cancelling during a stay.** Reading: you wrote "while Pending or Confirmed", and Confirmed includes In stay. Recommended: draw it as written, so a guest can cancel from In stay too. Why: I have no source that limits it. If that is wrong, the flat framing in point 1 fixes it.
3. **Pending expiry.** Reading: the Roamstay company context says a booking left in `payment_pending` for 30 minutes expires and its room goes back on sale. Your lifecycle has no such state. Recommended: leave it out and name it under `Left out:` in the reply. Why: you listed the statuses, and adding an end state you didn't name would change what support sees.

**Assumed:** the end state is called Cancelled, since you only wrote "cancel". Detail is balanced, the audience is support and the reading distance is Laptop.

Is this the right reading of the board? Say yes to take my recommended answers on points 1 to 3, or correct any of them.