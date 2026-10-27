Before I draw anything, this is how I read the request.

**Question:** which statuses can a Roamstay booking have, what moves it between them, and who sets Cancelled and No-show?
**Outcome:** support can read every status and knows who to ask about a Cancelled or a No-show booking.
**Type:** state diagram, because the board is about statuses and the moves between them.
**Settled by the sources:** your request is the only source. It states every status and move, so I treat it as current behavior. There is no doc to re-read.

**Outline**
* Start into Pending, then Pending to Confirmed on "card authorised"
* Confirmed is one section holding Upcoming and In stay, with Upcoming to In stay on "check in"
* Confirmed to Completed on "check out [from In stay]"
* Pending to Cancelled and Confirmed to Cancelled, both on "cancel"
* Confirmed to No-show on "missed check-in [from Upcoming]"
* Completed, Cancelled and No-show each end the booking
* That is 7 states and 6 labelled moves, plus the start and end arrows

**Notes (2 stickies, no pins)**
* Cancelled: "Set by the guest, while the booking is Pending or Confirmed"
* No-show: "Set by the hotel, after a missed check-in"

**Two framings.** Recommended is Confirmed as one section with Upcoming and In stay inside. It shows that cancel and No-show leave from Confirmed, at the cost of a guard on moves only one inner state takes. The other is a flat map with all seven states at one level. That reads simpler but loses the "Confirmed covers" grouping you described.

**Look:** the labels carry the event only and the notes carry who, so the setter is stated once. Title "Booking status". First glance on Cancelled, the first status you asked a note for.

**Left out**
* What happens when card authorisation fails, because the request gives no move out of Pending for it
* Whether anyone other than the guest can cancel, because the request names only the guest

**Assumed**
* The Upcoming to In stay trigger is "check in", and "check out" and "missed check-in" leave from In stay and Upcoming. A doc line or your word settles each
* Balanced detail, a mixed audience and Laptop reading distance
* Cancelled as the first glance

**Still open:** none that blocks the draw. The "anyone other than the guest" point matters for your goal, since the note will say "guest" only.

Is this the right reading of the board?