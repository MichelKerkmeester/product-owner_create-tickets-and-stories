Nothing is written to the board yet. Before I draw, this is what I found and how I read your request.

**Finding:** the board already shows this lifecycle twice, so a new copy would be a third one.
- **First "Booking status" section:** at the far left of the page (`62:66`). Its source line says "the Roamstay Product team request".
- **Second "Booking status" section:** further right, after "2. Checkout payment, declined card" (`73:785`). Its source line says "the Product Owner's lifecycle description".
- **What both contain:** Pending, Confirmed (with Upcoming and InStay inside), Completed, Cancelled and No-show, with Cancelled reached from Pending and Confirmed and No-show reached from Confirmed. I haven't compared their transition label wording against yours.
- **The retro itself:** the only retro content I found is the "Sprint retro" section of six stickies. The rest of the page holds other diagrams.

**Question:** which statuses can a Roamstay booking have, and what moves it between them? That is a state diagram.

**Outcome:** a reader can see every status and the event behind each move.

**Settled by your message** (all current behavior):
- A booking is Pending until the card is authorised, then Confirmed.
- Confirmed covers Upcoming and In stay.
- Check-out ends it as Completed.
- A guest can cancel while Pending or Confirmed.
- The hotel marks No-show after a missed check-in.

**Assumed:**
- Check-in moves Upcoming to In stay. Your message doesn't state that trigger, so you'd settle it.
- No-show is reached from Confirmed, not from Pending.
- Balanced detail, a mixed audience and the Laptop reading distance.

**Left out:** refunds, payment steps and any No-show time window, because you didn't state them.

**Question for you:** should I still draw it as a third copy, placed to the right of everything on the page? I recommend not, because two copies already say the same thing. If you want one of the two changed, tell me which and what to change.