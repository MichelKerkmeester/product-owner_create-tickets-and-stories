All checks confirm the shape. The parser supports the description form (`state "In stay" as InStay`), the check forces cross-composite moves to run at composite level, and the composer already colours every state a booking ends in light gray with the key naming it "Final state" — so the end-state colouring needs no extension.

Before anything is drawn, here is how I read the request.

**Question:** which statuses exist and what moves a booking between them?
**Outcome:** support can read every booking status and spot the statuses a booking ends in.
**Settled by your description:** a booking starts Pending and stays there until the card is authorised, which confirms it. Confirmed holds Upcoming and In stay, and check-in moves Upcoming to In stay. Check-out ends the stay as Completed. A guest can cancel while Pending or Confirmed, and the hotel marks No-show after a missed check-in. The composer already draws every state a booking ends in light gray and names it Final state in the key, so the end states stand out with no extra styling.
**Shape:** Confirmed drawn as a composite holding Upcoming and In stay, as you describe. Five flat statuses would lose the check-in move you named, so I recommend the composite.
**Board text:** titled Booking status, with a subtitle naming Guest Support as the reader.
**Left out:** nothing.
**Assumed:** balanced detail and a mixed audience.
**On this file:** nine boards from earlier sessions already sit on the page titled Booking status or Booking status lifecycle, the latest written 25 Oct 14:12. The new board lands to the right of everything already there and touches nothing. Taking down any old board waits for its own yes after the write.
**Still open:** none.

Is this the right reading of the board?