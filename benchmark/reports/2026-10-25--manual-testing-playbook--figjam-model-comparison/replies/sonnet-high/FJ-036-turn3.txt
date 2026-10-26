**Playback.** Nothing is drawn or written yet. This is the reading I will model, and I need one answer on it.

**The sentence the board answers:** what does a guest see and pay when they change their booking dates?

**Reader and outcome:** the Roamstay product and design team can check each branch and its price outcome against the product.

**What each source settled**
- Your request gave the entry, the exit, the room check and the three price outcomes
- Your recommended answers gave the reader, the question, the scope and the dials (Balanced detail, mixed audience, laptop reading distance)
- Left out by scope: payment failure, change deadlines, fees and the host's side

**Assumed, with no source behind it**
- After the guest sees other rooms, they pick one and the flow goes on to the price check. A screen of the other-rooms step or your word would settle it
- The flow is current behavior. A doc or screenshot showing it is built would settle it

**Outline, in drawing order**
1. Booking page (start), from your entry
2. Pick new dates, with "Change dates" as the label on the edge into it
3. Room free? (decision), exits Yes and No
4. See other rooms, on the No exit
5. New price vs old? (decision), exits Higher, Lower and Same. It takes the Yes exit and the other-rooms step, the latter labelled "Pick a room" (the assumed move)
6. Pay the difference, on Higher
7. Difference returned as credit, on Lower
8. Nothing charged, on Same
9. Updated booking (end), reached from all three outcomes

That is 9 nodes and 11 connectors, which is the full budget for a user flow, so any step added later forces a split. The remove test cut a separate "Tap Change dates" node and a separate "Pick a room" node, since each is a move rather than a screen. It also cut a merge dot, because the three outcomes can arrow straight into the end.

**Two framings**
- **One board, whole path (recommended):** the main line runs booking page to updated booking, with the other-rooms detour beside it. It costs a full-budget board. It buys one picture of the whole question
- **Two boards:** an availability board and a price board. Each is lighter, but the reader loses the single path and has to join the two by hand

**The look, proposed**
- **First glance:** the price check, marked as the one accent, because its three exits are the part a reader compares. Second glance is the three outcomes, and last glance is the other-rooms detour and the source line
- **Zones:** none. One path of 9 nodes does not need grouping
- **Title:** "Change booking dates"
- **Subtitle:** "How a Roamstay guest changes the dates of a booking in the app, from the booking page to the updated booking"
- **Source line:** "Sources: the product owner's description of the date-change flow, treated as current behavior. Assumed: after seeing other rooms the guest picks one. Left out: payment failure, change deadlines, fees and the host's side"

**Four questions the gate will answer about the drawn sketch**
1. Where does the eye go first, and is that the price check?
2. Does the other-rooms detour read as a side branch rather than a second main path?
3. Do the three price exits read as one kind of choice?
4. Does the board answer the guest question without anything beside it?

Does this reading match the product, or what should change?