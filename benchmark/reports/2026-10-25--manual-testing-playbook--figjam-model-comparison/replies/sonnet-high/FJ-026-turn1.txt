Before I draw anything, this is how I read the request.

**Question:** which statuses does a Roamstay booking have, and what moves it between them?

**Outcome:** support can read every booking status and spot the three a booking ends in.

**Settled by your request:**
* Pending until the card is authorised, then Confirmed, which holds Upcoming and In stay
* Check-in moves Upcoming to In stay
* Check-out ends the booking as Completed
* A guest can cancel while Pending or Confirmed
* The hotel marks No-show after a missed check-in

**Colour:** Completed, Cancelled and No-show are the states a booking ends in. The composer draws every such state light gray and names it "Final state" in the key. It sets colour by kind, so it can't give Cancelled and No-show their own hue on this board. A different end-state colour on every board is a one-token change to the design file, and a one-off colour is a hand edit in FigJam.

**Left out:** nothing.

**Assumed** (these stand unless you correct them):
* Check-out leaves from In stay and the missed check-in from Upcoming, because check-in is what separates the two
* "Cancel while Confirmed" also covers In stay, since Confirmed contains it. I draw it as you wrote it, as one move from Confirmed to Cancelled. If you meant before check-in only, that move gets a `[from Upcoming]` guard
* The board does not show payment failures, refunds or who can see which status, because you named none of them
* Balanced detail, a mixed audience and a laptop reading distance, with no accent on any one state, because the three end states carry equal weight and the gray fill is the signal

**Still open:** none.

Is this the right reading of the board?