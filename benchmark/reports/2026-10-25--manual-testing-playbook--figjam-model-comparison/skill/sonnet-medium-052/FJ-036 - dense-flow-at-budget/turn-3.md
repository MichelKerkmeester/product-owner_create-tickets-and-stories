Here is the full reading before I model anything.

**What the board answers**
* Question: what does a guest go through to change their booking dates, and what happens to the money?
* Outcome: a product or support teammate new to the feature can explain the three price outcomes
* Dials: Balanced detail, Mixed audience, Laptop distance, all `assumed`
* Sources: your description and the help article, read as current behavior

**What each source settled**
* Your description gave the steps, the room check and the three price exits
* The help article gave the date picker rule, the 3-room limit, the card on file, the 12-month credit and the email
* Your last answers settled the reader, what the board refuses and that picking another room leads to the price check

**Facts I assumed**
* The reader is a teammate new to the feature
* Picking another room leads to the price check
* "Higher", "lower" and "same" compare the new price with the booking's current price
* The guest acts on taps and picks, and the system checks the room and the price and sends the email
* The email rides in the final step's body rather than as its own node, to hold the 9-node budget

**Outline**, in drawing order. The first line is the sentence the board answers.
1. A teammate sees what a guest passes through to change dates and how the price outcome is settled
2. Node: Booking page, where the flow starts
3. Node: Pick new dates. Body: only nights the hotel has open
4. Node: Room free? A decision with Yes and No exits
5. Node: See other rooms. Body: up to 3 rooms at the same hotel, with the price for the new dates
6. Node: New price? A decision with Higher, Lower and Same exits
7. Node: Pay the difference. Body: charged to the card on file
8. Node: Get credit. Body: kept for 12 months
9. Node: Nothing charged
10. Node: Updated booking shown, the goal. Body: also sent by email
11. Edges: Booking page to Pick new dates, labelled "Tap Change dates". Pick new dates to Room free?. Room free? to New price? on Yes. Room free? to See other rooms on No. See other rooms to New price?, labelled "Pick a room". New price? to Pay the difference on Higher, to Get credit on Lower and to Nothing charged on Same. Each of those three to Updated booking shown

That is 9 nodes and 11 connectors, with no merge dot because the three outcomes each draw their own line to the end. Every node passes the remove test, because cutting any of them drops a step or an outcome you named.

**Two framings**
* End to end: the main row runs from the booking page through the room check and the price check to the updated booking, with other rooms beside it. It shows the guest's path and the money rules together
* Price rules only: it starts at the price check and shows the three outcomes. It is simpler and drops the date picker and the other rooms

I recommend end to end, because your reader needs both the path and the money, and 9 nodes fit.

**The look**
* Focus: the New price? decision gets the accent, because the price sets what happens next
* Goal: Updated booking shown, named without the accent
* Zones: none, because 9 nodes in a short chain read clearly and the bodies already carry the rules
* Title: Change booking dates
* Subtitle: From the booking page to the updated booking, for a teammate learning the feature
* Source line: Sources: your description and the Roamstay help article. Left out: cancellation or refund, a failed card charge, hotel-side steps, screen layouts.

Is this reading right, or should I change any row before I draw it?