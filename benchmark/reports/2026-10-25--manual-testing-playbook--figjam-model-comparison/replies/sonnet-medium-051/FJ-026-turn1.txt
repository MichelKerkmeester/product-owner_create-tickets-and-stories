Here is how I read the request so far.

**Settled by your message**
* **Reader:** support, who need to spot the end states.
* **Question:** which booking statuses exist and what moves a booking between them? That is a state diagram.
* **Outcome:** support can read every status and spot the ones a booking ends in.
* **States:** Pending, Confirmed (containing Upcoming and In stay), Completed, Cancelled and No-show.
* **Moves:**
  * Pending to Confirmed when the card is authorised.
  * Upcoming to In stay at check-in.
  * Confirmed to Completed at check-out.
  * Pending or Confirmed to Cancelled when the guest cancels.
  * Confirmed to No-show when the hotel marks a missed check-in.
* **End-state colour:** the board draws every state the booking ends from (Completed, Cancelled, No-show) in light gray and lists them in the key as "Final state". A request for colour needs no extra step.
* **Target:** the existing FigJam file `<test-file-key>`, as a new section beside what it already holds. I'll read the file once before the write gate. I can't check from here that the file sits in Roamstay Product, because `whoami` lists the plans you belong to and not which plan owns a file. The gate will state the plan as you supplied it.

**Assumed**
* Detail is balanced, the audience is mixed and the reading distance is Laptop.
* "Cancelled" is the end state's name, because your message names the action and not the state.

**Two questions**

1. Reading: "Cancel while Pending or Confirmed" can mean any Confirmed status, which includes In stay.
   Question: can a guest cancel once they are In stay?
   Recommended: no. Cancellation leaves from Pending and Upcoming only, and the board labels it `guest cancels [from Upcoming]`.
   Why: a guest who has checked in ends the booking by checking out, and your message names no cancel after check-in.

2. Reading: your message gives five states and six moves, and no failed authorisation, expiry, refund or modification.
   Question: what must this board not do?
   Recommended: show only the moves you listed. Payment failure, expiry, refunds and edits stay off the board, and the reply names them under `Left out:`.
   Why: none of them is in your message, and a status the sources never stated would read as current behaviour.

Take the recommended answers, or correct any of them?