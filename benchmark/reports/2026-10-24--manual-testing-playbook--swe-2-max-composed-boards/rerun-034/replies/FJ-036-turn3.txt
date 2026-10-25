This is the full playback of my reading, before any model is drawn. Nothing is written and no plan or calls are named yet.

**What the board answers**
* Question: which screens does a guest pass through to change booking dates, and where does the price decide what they pay?
* Outcome: the Booking squad can see the no-room path and all three price outcomes and agree on them

**What your request settled (captured)**
* Reader: the Booking squad (product manager, designer and engineers)
* Entry: Booking page, where the guest taps Change dates
* Exit: the guest sees the updated booking
* Actors: the guest picks dates and a room, and the system checks the room and compares prices
* Decisions: whether the room is free, and whether the new price is higher, lower or the same
* Scope: one main path with those two decisions. Type and look: a user flow, left to right, balanced detail, mixed audience, laptop distance, no zones

**Assumed (each one named so you can correct it)**
* After the guest sees other rooms, they pick one and go to the price check. Your request does not say what follows, and a different ending would change one connector
* The flow is current behavior. Your request gives no status, and a proposal would put that status in the subtitle and labels

**The outline, by row**
1. Board sentence: which screens does a guest pass through to change booking dates, and where does the price decide what they pay?
2. Nodes in drawing order: Booking page (start), Pick new dates, Room free? (decision), See other rooms, New price? (decision), Pay the difference, Get the difference as credit, No charge, Updated booking (end)
3. Connectors: Booking page to Pick new dates, labelled "Tap Change dates". Pick new dates to Room free?. Room free? to New price? on Yes, and to See other rooms on No. See other rooms to New price?, labelled "Pick a room". New price? to Pay the difference on Higher, to Get the difference as credit on Lower, and to No charge on Same. Each of those three to Updated booking
4. The count is 9 nodes and 11 connectors, with 5 labelled decision exits. That is inside the 9-node budget
5. Look: Updated booking is the goal and the only accent. No failure end, no step in focus
6. Text: title "Change booking dates". Subtitle "How a Roamstay guest changes the dates of a booking in the app, from the booking page to the updated booking". Source line "Sources: the product owner's description of the flow. Left out: failed payments, cancellation, stay limits, Guest Support, leaving without a change"

Is this reading right, including the two assumed rows? Correct any line and I'll replay only the rows it touches.