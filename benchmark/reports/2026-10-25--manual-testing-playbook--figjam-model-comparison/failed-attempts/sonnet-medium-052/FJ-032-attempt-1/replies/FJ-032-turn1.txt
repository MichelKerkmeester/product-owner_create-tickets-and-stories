**Settled so far**

- Type: state diagram, because the question is which statuses a booking can hold and what moves it between them
- Target: board <test-file-key>, added as a new section beside what it holds, with nothing there changed
- Entry: Pending (captured)
- States: Pending, Confirmed with Upcoming and In stay inside it, Completed and No-show (captured). Cancelled is assumed, because a guest can cancel but you did not name the status
- Moves: card authorised, check-out, guest cancel from Pending or Confirmed, and hotel No-show after a missed check-in (captured). Check-in moving Upcoming to In stay is assumed, because you named both states but not the move
- Actors: guest and hotel (captured)
- Booking doc rules: Pending lasts at most 15 minutes while the card is checked, a cancel within 48 hours of check-in keeps the first night's price, and No-show can be marked from 6 hours after the check-in time (captured). I read the doc as current behavior, so tell me if it is a proposal
- Open for the next round: what ends Pending when the card is not authorised within 15 minutes, and whether the 48-hour rule also covers a cancel from Pending

**Question 1**

Reading: the request names no reader, and the board goes on a retro board, so I read it as your team.
Question: who reads the board, and what should they decide after it?
Recommended: the Roamstay product team, deciding which booking statuses exist and which moves are allowed before a story is written
Why: that is what a status diagram answers, and it needs no source beyond your message

**Question 2**

Reading: your message covers the statuses, the moves and three doc rules. It says nothing about card failure, refund amounts or screens.
Question: what must this board not do?
Recommended: no card-failure or refund handling, no screens, and no status beyond the ones you listed plus Cancelled
Why: no source states them, and a guessed status reads as fact on a board

**Question 3**

Reading: the three doc rules each attach to a specific state or move, and no reading distance is named.
Question: which detail level, audience and reading distance?
Recommended: Balanced, Mixed and Laptop
Why: Balanced puts each doc rule on the state or move it governs, and Mixed keeps plain verbs for a product reader

Take the recommended answers, or correct any of them?