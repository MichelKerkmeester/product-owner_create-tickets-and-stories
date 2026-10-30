<figma-url>
Read-back: 7 of 7 states, 12 of 12 transitions, 6 of 6 transitions labelled, first glance: Pending
Left out: what happens when Pending passes 15 minutes, the booking doc doesn't say
Finding: the doc lets a guest cancel while Confirmed, and Confirmed includes In stay, so the board draws "guest cancels" from Confirmed as worded. If cancelling should stop at check-in, the move needs a `[from Upcoming]` guard, which means composing the board again after your yes.
Finding: the "Cancelled" status name is assumed, because the doc only says a guest can cancel.
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.