# FJ-036 turn 2 transcript

**User:** Use your recommended answers.

**Assistant:**

Your recommended answers are taken and stay marked assumed. This is the full reading, before any model is drawn.

### The brief

* Reader: the product and design team, assumed
* Question: which screens does a guest pass through when changing booking dates, and where do they choose, assumed
* Outcome: the team can check that every price outcome and the no-room case has a way out, assumed
* Scope: the change-dates flow only, with cancelling, payment failure, guest count changes and the host side left for later boards, assumed
* Entry: the booking page, with Change dates tapped, captured
* Exit: the updated booking, captured
* Actors: the guest, with the app showing rooms and giving the credit, captured
* Decisions: room free on the new dates (Yes, No), then how the new price compares (Higher, Lower, Same), captured
* After other rooms: the guest picks a room and joins the price check, assumed
* Source and class: your message, current behavior, assumed

Assumed rows settle on your correction. The source row also settles on a link to the live screens, or on a note that the flow is a proposal.

### The outline

The sentence the board answers: how a Roamstay guest changes their booking dates in the app, from the booking page to the updated booking.

Nodes, in drawing order:
1. Booking page, where the flow starts
2. Pick new dates
3. Room free on those dates?
4. See other rooms
5. How does the new price compare?
6. Pay the difference
7. Get the difference as credit
8. Updated booking, where the flow ends

Connectors:
1. Booking page to Pick new dates, labelled "Tap Change dates"
2. Pick new dates to Room free on those dates?
3. Room free on those dates? to How does the new price compare?, labelled "Yes"
4. Room free on those dates? to See other rooms, labelled "No"
5. See other rooms to How does the new price compare?, labelled "Pick a room"
6. How does the new price compare? to Pay the difference, labelled "Higher"
7. How does the new price compare? to Get the difference as credit, labelled "Lower"
8. How does the new price compare? to Updated booking, labelled "Same, nothing charged"
9. Pay the difference to Updated booking
10. Get the difference as credit to Updated booking

That is 8 nodes against the budget of 9, and 10 connectors. The remove test cut nothing, because each node is a screen or a choice you named.

### Two framings

* Framing A, recommended: the same-price exit goes straight to the updated booking as "Same, nothing charged". It keeps the board at 8 nodes and shows the no-charge case on the exit where the decision happens. The cost is that nothing charged has no box of its own, so a reader scanning for boxes finds only a label
* Framing B: a separate "Nothing charged" node on the same-price exit. It shows three equal outcomes, but the node is not a screen or an action and it uses the full 9-node budget, leaving no room to add a declined payment later

I recommend A because nothing charged is the absence of an action, and a label says that better than a box.

### The look

* Colour: Updated booking is the goal, drawn green by the board's one style line. There is no failure end and no step in focus, so no other accent appears
* Detail, audience and distance: Balanced, Mixed and Laptop, assumed
* Zones: none, because 8 nodes read without them
* Title: "Change booking dates"
* Subtitle: "How a Roamstay guest changes booking dates in the app, from the booking page to the updated booking"
* Source line: "Sources: the change-dates request. Left out: cancelling, payment failure, guest count changes and the host side."
* Critique questions for the sketch: where does the eye go first and is that the node the board most needs read, can a reader find all three price exits without tracing a line, does the no-room path read as a detour that rejoins the flow, and does any label repeat its shape

### Still open, not guessed

* Whether the guest can go back from other rooms to pick other dates, so no back connector is drawn
* Whether the guest can decline the extra payment, so Pay the difference has one exit
* What the credit is used for later, so the board stops at the updated booking

These three will appear under `Left out:` in the delivery reply.

Is this reading right, or which row should change?

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.
