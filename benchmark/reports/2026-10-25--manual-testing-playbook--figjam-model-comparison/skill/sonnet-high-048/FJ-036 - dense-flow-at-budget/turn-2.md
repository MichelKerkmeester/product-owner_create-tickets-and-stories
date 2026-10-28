Settled so far:

- Reader and question: the Roamstay Product team, asking which screens a guest passes through to change dates and where they choose (assumed, accepted as recommended)
- Outcome: agree that the flow covers the room check and all three price outcomes (assumed)
- Must not draw: payment failures, refund mechanics, cancellation or any step your message does not state (assumed)
- Dials: Balanced detail, Mixed audience, Laptop distance (assumed)
- Entry: the Booking page, where the guest taps Change dates
- Exit: the guest sees the updated booking
- Actors: the Roamstay guest, with the room check and the price comparison as system steps (assumed)
- Decisions: "Room free on the new dates?" has Yes and No exits, and the new price against the old one has three exits (pay the difference, credit the difference, no charge)
- Sources: your message only, taken as current behavior (assumed)
- Destination: file <draft-file-key>, as a new section beside what it holds

Nothing is written to the board yet. The last round left one row open, so round two asks about it alone.

**1. Where Other rooms leads**
Reading: your message says a guest sees other rooms when the room is not free, and it states no step after that. The three price outcomes depend on the new price, and another room carries its own price
Question: what does the guest do from Other rooms
Recommended: the guest picks a room, and the flow joins the price comparison, with the connector labelled "Pick a room"
Why: the price outcomes are the next stated step, and this adds an edge rather than a tenth node

**2. The case where no other room is free**
Reading: your message states no case where Other rooms comes up empty
Question: should the board show it
Recommended: leave it off the board and name it under "Left out" as a point your message left open
Why: no source states it, and the nine-node budget is already full

Take the recommended answers, or correct any of them?