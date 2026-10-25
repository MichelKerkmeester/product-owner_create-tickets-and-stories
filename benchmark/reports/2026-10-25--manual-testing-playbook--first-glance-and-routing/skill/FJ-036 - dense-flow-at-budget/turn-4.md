Nothing is written yet. This is the outline pass, the first of three proposals, and it is text only.

**The sentence the board answers:** what does a Roamstay guest see and pay at each outcome of changing their booking dates?

**Nodes (9, the user-flow limit)**

1. `Booking page`: the flow starts here (Entry)
2. `Pick new dates`: a screen (Actors)
3. `Room free?`: a decision with 2 exits (Decisions)
4. `See other rooms`: a screen, shown only when the room isn't free (Decisions)
5. `New price?`: a decision with 3 exits (Decisions)
6. `Pay the difference`: the higher outcome (Outcomes)
7. `Difference back as credit`: the lower outcome (Outcomes)
8. `Nothing charged`: the same-price outcome (Outcomes)
9. `Updated booking`: the flow ends here (Exit)

**Connectors (11, the limit is 12)**

1. Booking page to Pick new dates, labelled `Tap Change dates` (guest)
2. Pick new dates to Room free? (system check)
3. Room free? to New price?, labelled `Yes`
4. Room free? to See other rooms, labelled `No`
5. See other rooms to New price?, labelled `Pick a room` (assumed, from the "After other rooms" row)
6. New price? to Pay the difference, labelled `Higher`
7. New price? to Difference back as credit, labelled `Lower`
8. New price? to Nothing charged, labelled `Same`
9. Pay the difference to Updated booking
10. Difference back as credit to Updated booking
11. Nothing charged to Updated booking

**What the remove test cut**

* A separate `Tap Change dates` node, folded into connector 1's label because the tap is the move and not a screen
* A merge dot, because nothing here is a platform split and the three outcomes can join `Updated booking` directly
* A payment screen and a confirmation message, because you described neither

The main route runs Booking page, Pick new dates, Room free?, New price?, then an outcome, then Updated booking. The other-rooms step sits beside it.

Is this outline right? I recommend yes, because it holds every step and outcome you described and nothing you didn't. If it is, the next proposal is two framings of the board to choose between, and then a text sketch.