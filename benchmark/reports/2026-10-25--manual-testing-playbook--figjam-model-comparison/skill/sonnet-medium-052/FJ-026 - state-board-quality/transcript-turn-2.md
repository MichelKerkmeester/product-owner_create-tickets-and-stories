# FJ-026 turn 2 transcript

**User:** Use your recommended answers.

**Assistant:**

Before I draw anything, this is how I read the request.

**Question:** which statuses does a Roamstay booking have, what moves it between them, and which ones are final?
**Outcome:** support can read every booking status and spot the statuses a booking ends in.
**Detail, audience and distance:** Balanced detail, a Mixed audience and the Laptop reading distance.

**Settled by the sources:**
- Pending lasts until the card is authorised.
- Confirmed covers Upcoming and In stay. Check-in moves Upcoming to In stay.
- Check-out ends the stay as Completed.
- A guest can cancel while Pending or Confirmed.
- The hotel marks No-show after a missed check-in.
- The five rules from your booking doc sit as short lines inside the state they belong to, not as extra states or branches:
  - Pending: stays at most 15 minutes while the card is checked.
  - Upcoming: the guest can still change dates.
  - In stay: the hotel can add charges to the room.
  - Cancelled: a cancel within 48 hours of check-in keeps the first night's price.
  - No-show: the hotel can mark it from 6 hours after the check-in time.

**Colour:** Completed, Cancelled and No-show are the machine's end states, so the composer draws them in light gray and the key names them "Final state". The states inside Confirmed stay white, because leaving Confirmed is what ends the booking. Cancelled also carries the pink focus outline, so it is the first thing support's eye lands on among the end states.

**Destination:** a new section in the existing file `<test-file-key>`. It is not a new file, and nothing already on the file changes.

**Left out:** what happens when Pending passes 15 minutes, because the doc doesn't say.

**Assumed:**
- The question and outcome above, which you accepted as my recommendation and no source states. A correction from you settles it.
- The cancelled status is called Cancelled, since the doc never names it.
- A guest can cancel from Confirmed, which includes In stay, exactly as the doc words it. I'll flag this as an open point in the reply. A statement from you or the doc that cancelling stops at check-in settles it.

**Still open:** none.

Is this the right reading of the board?
