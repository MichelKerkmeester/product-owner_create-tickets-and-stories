Before I draw anything, this is how I read the request. Nothing is written until the gate that follows.

Question: which statuses can a Roamstay booking be in, and what moves it between them?
Reader: Guest Support
Outcome: support can read any booking's status and spot the three statuses a booking ends in.
Type: a state diagram, because the question is about statuses and the events between them.

Settled by your message, the only source, taken as current behavior:
- Pending until the card is authorised, then Confirmed
- Confirmed covers Upcoming and In stay, and check-in moves Upcoming to In stay
- Check-out ends the booking as Completed
- A guest can cancel while Pending or Confirmed
- The hotel marks No-show after a missed check-in

Outline, in drawing order:
1. Start, then Pending
2. Pending to Confirmed: card authorised
3. Confirmed opens at Upcoming
4. Upcoming to In stay: check in
5. Confirmed to Completed: check out
6. Pending to Cancelled: guest cancels
7. Confirmed to Cancelled: guest cancels
8. Confirmed to No-show: missed check-in
9. Completed, Cancelled and No-show each end the booking

Two framings:
- Recommended: Confirmed as a section around Upcoming and In stay. It matches your wording and keeps Confirmed a status. The cost is that check-out, cancel and No-show leave the whole section, so the board cannot show that check-out follows In stay only or that No-show follows Upcoming only.
- Alternative: six flat states with no Confirmed. It draws check-out from In stay and No-show from Upcoming. It drops Confirmed, which you named as a status, and draws cancel twice.

Colour:
- The composer draws every state a booking ends from in light gray, with a ringed end dot, and the key calls it Final state. Completed, Cancelled and No-show share that one gray, and Upcoming and In stay stay white.
- A state diagram takes no colour from the model, so a different colour per end state, such as red for Cancelled, would be a hand edit in FigJam afterwards.
- The pink accent can mark one node only. Recommended: none, because marking one end state would make it outweigh the other two.

Look:
- Title: Booking status
- Subtitle: How Guest Support reads where a Roamstay booking is, what moves it on and where it ends
- Source line: the booking lifecycle as described in the request
- Labels read In stay and No-show in your spelling

Assumed:
- Cancelled is the status name, and Cancelled and No-show are end states like Completed. Your message names the events but not those two status words.
- Balanced detail, a mixed audience and laptop reading distance.

Still open:
- Reading: `roamstay-context.md` says a booking in `payment_pending` expires after 30 minutes and its room goes back on sale. The incident notes log it as "booking expired". I read your Pending as `payment_pending`. Your lifecycle has no exit for the expiry, and no source names an Expired status.
- Recommended: leave it off the board and name it under Left out, because drawing it would invent a status name.

A yes, or a correction to any line above, is enough. Where you don't answer, the recommended choices stand and I name them as assumed at the gate.

Is this the right reading of the board?