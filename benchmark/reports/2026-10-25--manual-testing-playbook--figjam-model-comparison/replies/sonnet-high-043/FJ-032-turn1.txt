I read the board first. It holds one section, "Sprint retro", with six stickies and nothing else. No section is titled "Booking status", so the new board has nothing to clash with, and the retro content stays as it is.

Before I draw anything, this is how I read the request.

**Reader:** the team on the retro board. This is assumed, and a product doc or a word from you would settle it.
**Question:** which statuses can a Roamstay booking have, and what moves it between them?
**Outcome:** the team can agree on every status and the event behind each move.
**Type:** state diagram, because the question is about statuses and the moves between them. A process or a sequence would answer who does what, which you did not ask for.

**Settled by your request**
* Pending until the card is authorised, then Confirmed
* Confirmed covers Upcoming and In stay
* Check-out ends the booking as Completed
* A guest can cancel while Pending or Confirmed
* The hotel marks No-show after a missed check-in

**Assumed**
* Check-in moves Upcoming to In stay. You did not state this trigger, but a missed check-in and a check-out both imply it. Recommended: label it "check in"
* Check-out leaves from In stay only, and No-show from Upcoming only. The labels carry those guards, such as "missed check-in [from Upcoming]", because a move out of Confirmed otherwise reads as open from both inner states
* Cancel is drawn from Confirmed as a whole, as you wrote it, so the board also shows a guest cancelling during In stay. If cancelling should stop at check-in, the label becomes "guest cancels [from Upcoming]"
* Balanced detail, a mixed audience and a Laptop reading distance

**Left out:** a declined or expired card authorisation, refunds and edits to a booking. None were in your request, so Pending has exactly two exits, card authorised and guest cancels. That is about seven states, inside the nine-state budget, so one board holds it without a split.

Is this the right reading of the board? If you say nothing on a point, I take the recommended answer above.