Before I draw anything, this is how I read the request.

**Question:** which statuses does a Roamstay booking pass through, and what moves it between them?
**Outcome:** support can read every booking status and spot the three statuses a booking ends in.
**Type:** state diagram. Your request lists statuses and the events between them, and nothing in it is a screen path or a message exchange.

**Settled by your request:**
* Pending is the start, and it lasts until the card is authorised.
* Confirmed holds Upcoming and In stay, and check-in moves Upcoming to In stay.
* Check-out ends the booking as Completed, and only from In stay.
* A guest can cancel from Pending or Confirmed.
* The hotel marks No-show after a missed check-in, and only from Upcoming.

**End-state colour:** Mermaid cannot colour a state diagram, so I won't set colours in the model. The composer draws every state the booking ends in (Completed, Cancelled and No-show) in light gray and names it "Final state" in the key. All three share that one gray, so the board separates them by their names and the events leading into them, not by colour. If support needs a different colour per outcome, that is a hand edit in FigJam after the write.

**Target file, assumed:** you named both the Roamstay Product plan and the existing file `<draft-file-key>`. I'm taking the existing file, because a key names a file that already exists and a plan only matters when a new file is created. The board lands as a new section beside what the file holds, nothing already there changes, and no new file or draft is created.

**Other assumptions:** balanced detail, a mixed audience and the Laptop reading distance. I'm treating your description as current behavior, since you gave no document to cite.

**Left out:** the timing of the No-show mark, because your request gives none. I won't draw a deadline or a "day after" rule.

**Still open:** none.

Is this the right reading of the board?