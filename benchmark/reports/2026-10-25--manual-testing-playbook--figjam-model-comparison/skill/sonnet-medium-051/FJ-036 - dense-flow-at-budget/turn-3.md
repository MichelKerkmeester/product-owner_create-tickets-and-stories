**Reading so far**

* Question: which screens does a guest pass through when changing booking dates, and how does the price outcome route them
* Outcome: the product and design team can confirm each branch matches the app or point out a missing one
* Detail, audience and distance: Balanced, Mixed, Laptop
* Settled by your message: entry, exit, actor and both choices (room free, price higher, lower or same)
* Assumed, with what would settle each:
  * Reader, question and outcome as above, until you name a different reader
  * Your message describes how the app works today, until a screen or doc says otherwise
  * After the other rooms, the guest picks a room and joins the price check, until you say they go back to the dates instead
* Not asked: nothing else is open
* Left out of the board: failed payment, change-window rules, host approval and cancellation, because your message doesn't describe them

**Outline, in drawing order**

The board answers: which screens does a guest pass through to change booking dates, and how does the price outcome route them.

1. Booking page, where the flow starts (Entry)
2. Pick new dates, reached by the label "Tap Change dates" (Entry, Actors)
3. Room free? (Decisions)
4. See other rooms, on the No exit (Decisions, assumed next step)
5. New price?, with exits Higher, Lower and Same, reached from Room free? on Yes and from the other rooms with the label "Pick a room" (Decisions, assumed)
6. Pay the difference, on Higher (Decisions)
7. Difference credited, on Lower (Decisions)
8. Nothing charged, on Same (Decisions)
9. Updated booking shown, the end, reached from all three price outcomes (Exit)

That is 9 nodes and 12 connectors, so it fits the user flow budget with no merge dot. Remove test: every node is a step or choice you described, so none comes out.

**Two ways to frame it**

* One board with the main route straight across and the other rooms and the three price outcomes beside it. This shows all branches at once, and it costs a little density at the price check. I recommend this one
* Two boards, "1. Pick dates" and "2. Settle the price". Each reads more easily, but a reader has to jump between boards to see the whole flow, and the flow only just fits one board anyway

**The look**

* Colour accent: the New price? choice, because it is where the three outcomes split and the reader most needs it. The goal, Updated booking shown, is named but not coloured
* Direction: left to right
* Zones: none, because 9 nodes read without them
* Title: Change booking dates
* Subtitle: From the booking page to the updated booking, for the product and design team
* Source line: Sources: the request description, read as current app behavior. Left out: failed payment, change-window rules, host approval and cancellation

Is this reading right, or what should change?