# FJ-032 turn 3 transcript

**User:** Use your recommended answers.

**Assistant:**

**Reading**

- Question the board answers: which statuses can a Roamstay booking hold, and what moves it between them?
- Outcome: the product team can agree the statuses and the allowed moves before a story is written
- Dials: Balanced detail, Mixed audience, Laptop distance
- Your message settled the entry, the states, the moves and the actors. The booking doc as you quoted it settled the 15-minute, 48-hour and 6-hour rules

**Outline, in drawing order**

1. Question: which statuses can a booking hold, and what moves it between them?
2. Start, then Pending, with the body "Lasts at most 15 minutes" and "While the card is checked"
3. Pending to Confirmed: card authorised
4. Confirmed, drawn as a section around Upcoming and In stay, entered at Upcoming
5. Upcoming to In stay: check-in
6. Confirmed to Completed: check-out [from In stay]
7. Pending to Cancelled: cancel
8. Confirmed to Cancelled: cancel / first night kept if <48h
9. Confirmed to No-show: missed check-in [from Upcoming], with the body "Marked by the hotel" and "From 6 hours after check-in time"
10. Completed, Cancelled and No-show each end the booking

That is 7 states and 11 arrows, inside the budget of 9 and 12.

**Two framings**

- A status map shows every state and every exit, with the doc rules on the moves they govern. It is busier, but it answers which moves are allowed.
- A happy path from Pending to Completed with cancel and No-show left out is cleaner, but it hides the moves the team needs to agree.

I recommend the status map.

**Look**

- No `%% focus:` line, because the request names no state. The eye starts on Pending, the first state, and the states inside Confirmed come next
- Title: Roamstay booking statuses
- Subtitle: From a Pending booking to Completed, Cancelled or No-show, for the Roamstay product team
- Source line: Sources: the request and the booking doc as quoted. Left out: what ends Pending after 15 minutes
- No zone lines, because Confirmed is already a section

**Assumed, and what would settle each**

- Reader, must-not list and dials: your say-so
- Cancelled as a status, and the check-in move from Upcoming to In stay: a status list or the booking doc
- Completed, Cancelled and No-show all end the booking: the booking doc
- The booking doc is current behavior: a note that it is a proposal
- No move for a card not authorised within 15 minutes, with the gap named under `Left out:`: the doc's rule for that case
- The 48-hour rule sits on the Confirmed cancel only: a statement that it also covers Pending

One reading to check. Cancel leaves Confirmed as a whole, as you described it, so it reads as open during In stay too. If a guest can cancel only before check-in, the label gains [from Upcoming].

Is this reading right, or which row should change?
