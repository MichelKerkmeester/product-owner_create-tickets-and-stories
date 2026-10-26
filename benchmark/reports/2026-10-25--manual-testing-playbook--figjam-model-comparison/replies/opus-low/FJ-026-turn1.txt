Here's how I've read the lifecycle so far. Nothing has been drawn or written yet.

**What the board answers:** what state is this booking in, and which states are final? Support should be able to spot a finished booking at a glance.

**Diagram type:** state machine.

**States**
- **Pending:** the starting state, until the card is authorised
- **Confirmed:** a parent state with two sub-states:
  - **Upcoming:** entered first, as soon as the booking is Confirmed
  - **In stay:** reached from Upcoming at check-in
- **Completed:** end state, reached from In stay at check-out
- **Cancelled:** end state, set by the guest
- **No-show:** end state, set by the hotel

**Transitions**
- Pending → Confirmed: "card authorised"
- Upcoming → In stay: "check-in"
- In stay → Completed: "check-out"
- Pending → Cancelled: "guest cancels"
- Confirmed → Cancelled: "guest cancels"
- Upcoming → No-show: "hotel marks no-show after missed check-in"

**End-state colour:** Completed, Cancelled and No-show get the board's end-state colour, so they stand out from the live states. Completed takes the success colour, and Cancelled and No-show take the failed-end colour.

**Assumed (correct me if any are wrong)**
1. **Cancelling during a stay:** you said "Confirmed", and Confirmed covers In stay. I've drawn the guest-cancel edge from the Confirmed parent, so it covers both sub-states. If a guest can't cancel once checked in, the edge should start at Upcoming only.
2. **Failed card authorisation:** your notes don't say what happens. I've left it off the board rather than guessing, and it'll appear as a left-out item. Does a failed card leave the booking Pending, cancel it, or go to some other state?
3. **No-show applies only to Upcoming.** It doesn't apply to Pending, since a booking without an authorised card can't miss a check-in.

I'll settle where the board goes as a separate question before anything is written. Your request asks for a new board in the Roamstay Product plan, but also names the existing file `<test-file-key>` and the Barter team plan as a fallback.

**Is this reading right, including the three assumptions?**