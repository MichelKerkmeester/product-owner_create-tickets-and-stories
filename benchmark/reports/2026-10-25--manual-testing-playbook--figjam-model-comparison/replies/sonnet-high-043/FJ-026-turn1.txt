Before I draw anything, this is how I read the request.

**Question:** which statuses does a Roamstay booking pass through, and which of them end it?
**Outcome:** support can read every booking status and spot the three that end a booking.
**Reader:** support. **Detail:** balanced. **Audience:** mixed. **Reading distance:** Laptop.

**Outline, in drawing order**
* A booking starts as Pending
* Pending to Confirmed: card authorised
* Confirmed is one section holding Upcoming and In stay, and a booking enters it as Upcoming
* Upcoming to In stay: check in
* Confirmed to Completed: check out
* Pending to Cancelled and Confirmed to Cancelled: guest cancels
* Confirmed to No-show: missed check-in, marked by the hotel
* Completed, Cancelled and No-show each end the booking

That makes 7 states. The remove test cut nothing, because every state and move is in your request. I read it as a state diagram. A table would not show Confirmed holding two statuses or the three ways out.

**Two framings**
* Recommended: a state map with Confirmed as a section. It shows both inner statuses and every exit at once
* The alternative is a flat seven-state map with no section. It costs the "Confirmed covers Upcoming and In stay" grouping and draws cancel twice

**Assumed**
* **Class:** current behavior, because you state the lifecycle flatly and attached no doc. A bookings doc or ticket would settle it, and any line that is a proposal would be labelled as one
* **Where two moves leave from:** check out leaves from In stay and a missed check-in leaves from Upcoming, because a stay cannot end before it starts and a check-in cannot be missed after one. The board shows both as guards on the move out of Confirmed
* **Colour:** the composer draws every state a booking ends from in light gray with a heavy outline, keyed as Final state. Completed, Cancelled and No-show therefore share one colour and are told apart by label. It cannot give Cancelled and No-show a red of their own, and a different colour for either would be a hand edit in FigJam afterwards
* **First glance:** Cancelled, marked with the pink outline, because it is the only end state two moves reach
* **Labels:** In stay and No-show keep your spelling through a description line
* **Title:** Booking status. The subtitle says who reads it and why, and the source line reads "Source: your request"

**Not on the board:** refunds, payment retries, screen detail and any status beyond the seven you named.

**Left out:** what happens to a Pending booking whose card is never authorised, because the request is silent on it.

**Still open:** can a guest cancel while In stay? Confirmed covers In stay, so as written the cancel move leaves the whole section. I recommend drawing it as written and flagging it on a `Finding:` line, because that is what your request says. If cancel is Upcoming only, I would guard it as "from Upcoming".

A yes takes every recommended answer above. Is this the right reading of the board?