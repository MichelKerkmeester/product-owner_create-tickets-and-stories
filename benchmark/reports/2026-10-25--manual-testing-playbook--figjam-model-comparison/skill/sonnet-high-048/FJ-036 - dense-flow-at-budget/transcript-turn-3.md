# FJ-036 turn 3 transcript

**User:** Use your recommended answers.

**Assistant:**

Here is the full reading before any model is written.

Question the board answers: which screens does a Roamstay guest pass through to change their booking dates, and where do they choose?
Reader: the Roamstay Product team
Outcome: they can agree that the flow covers the room check and all three price outcomes
Dials: Balanced detail, Mixed audience, Laptop distance
Type: user flow, at nine nodes and eleven connectors, inside the nine-node budget

What each source settled:
- Your message settled the entry, the exit, both decisions and the three price outcomes, all as stated
- The destination is the file <draft-file-key>, drawn as a new section beside what it holds
- Nothing is unasked

What is assumed, and what would settle each:
- Reader, outcome and dials are my recommended answers. A correction from you settles them
- Your message is taken as current behavior, not a proposal. A source naming it a proposal settles that
- The room check and the price comparison are system steps. The product's own flow settles that
- From Other rooms the guest picks a room and joins the price comparison. A screen or a correction settles that
- The case where no other room is free is left off the board

Outline, in drawing order. The first line is the sentence the write will carry:

Which screens does a Roamstay guest pass through to change their booking dates, and where do they choose?

Nodes:
- Booking page, where the flow starts (Entry)
- Pick new dates, a screen (Entry)
- "Room free on those dates?", a decision (Decisions)
- Other rooms, a screen (Decisions)
- "New price compared to old?", a decision with three exits (Decisions)
- Pay the difference (Decisions)
- Get the difference as credit (Decisions)
- Nothing charged (Decisions)
- Updated booking, where the flow ends (Exit)

Connectors:
- Booking page to Pick new dates, labelled "Tap Change dates"
- Pick new dates to the room decision
- Room decision to the price decision, labelled "Yes"
- Room decision to Other rooms, labelled "No"
- Other rooms to the price decision, labelled "Pick a room" (assumed)
- Price decision to Pay the difference, labelled "Higher"
- Price decision to Get the difference as credit, labelled "Lower"
- Price decision to Nothing charged, labelled "Same"
- Each of the three outcomes to Updated booking

The remove test would cut Nothing charged first, with "Same" running straight to Updated booking. It stays because the three price outcomes then read side by side.

Two framings:
- One path with the branches beside it: the main row runs from the Booking page to Updated booking, with Other rooms and the two other price outcomes beside it. It shows the common route first and costs the reader a little more effort to compare the three outcomes
- Two stages in zones, "Choose a room" and "Settle the price": it groups the two choices but adds two frames around nine nodes
- Recommended: the first. At nine nodes the flow reads without zones

The look:
- Colour marks the price decision. It is where the money moves and the reader's last choice, and the goal is named as Updated booking on a goal line without the accent
- Zones: none
- Title: Change booking dates
- Subtitle: How a Roamstay guest changes the dates of a booking in the app, from the booking page to the updated booking
- Source line: Sources: the flow as described in the request. Left out: the case where no other room is free

Is this reading right, or what should change?
