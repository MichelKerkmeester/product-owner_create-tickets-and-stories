**Playback.** Nothing is drawn or written yet.

**Question the board answers:** After a guest taps Change dates, what do they see and pay for each outcome?
**Outcome:** The reader can tell a guest which of the three price outcomes applies and what happens next.
**Dials:** Balanced detail, Mixed audience, Laptop distance.

**Settled from your request and the help article, both current behavior**
- Entry: the booking page. Exit: the updated booking
- Actor: the guest, with the app responding at each step
- Date picker: shows only nights the hotel has open
- Room not free on the new dates: the guest sees other rooms, up to 3 at the same hotel with their price for the new dates
- Room free, new price higher: the guest pays the difference, charged to the card on file
- Room free, new price lower: the guest gets the difference as credit, kept for 12 months
- Room free, new price the same: nothing is charged
- Updated booking: shown in the app and also sent by email

**Assumed, with what would settle each**
- Reader: Roamstay support and product staff. A named audience or an owner of the board would settle it
- Scope: the flow stops at the other rooms list. The help article says nothing about what the guest does there, so a source for that step would settle it

**Outline** (the reader's question, then one line per node and edge, in drawing order)
1. Booking page, start
2. Booking page to Pick new dates, labelled Tap Change dates. Body: only nights the hotel has open
3. Pick new dates to Room free?
4. Room free? to Other rooms on No. This is an end, with body: up to 3 rooms at the same hotel, with price for the new dates
5. Room free? to New price? on Yes
6. New price? to Pay the difference on Higher. Body: charged to the card on file
7. New price? to Get credit on Lower. Body: kept for 12 months
8. New price? to Nothing charged on Same
9. Pay the difference, Get credit and Nothing charged each to Updated booking. Body: also sent by email

That is 9 nodes and 10 connectors. The email rides on the last step as a body, so it adds no node.

**Two framings**
- Recommended: one spine from the booking page to the updated booking, with Other rooms as a side exit. It costs the guest's next move from the other rooms list, which is named under Left out
- Alternative: two boards, one for the room check and one for the price outcome. That buys room to show what follows the other rooms list, but costs a second board and splits one flow for the sake of one branch

**Look, all proposed**
- Accent on the New price? decision, because the three outcomes differ there
- Goal: Updated booking, with no accent
- No zones, since 9 nodes read as one row
- Title: Change booking dates
- Subtitle: From the booking page to the updated booking, for Roamstay support and product staff
- Source line: the request and the help article, with the other rooms continuation left out

**Target:** the existing FigJam file `<test-file-key>`, not a new file. I read it before the write gate and name any section that shares the title.

Is this reading right, or do you want to correct any row, a framing or the look?