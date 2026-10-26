Board is on the canvas and read back clean.

<figma-url>

Read-back: `get_figjam` on section 129:4747 returned all 12 nodes and 12 connectors, matching the model exactly — 7 states (Pending, Upcoming, In stay inside the Confirmed composite, plus the three final states Completed, Cancelled, No-show), 6 labelled transitions (card authorised, check-in, check-out, guest cancels ×2, missed check-in), and the key naming the gray group "Final state". Zero warnings from the write. The board sits to the right of the existing content and is tagged `productowner/Booking status`.

Left out: the 30-minute `payment_pending` expiry recorded in the Roamstay context file — the stated lifecycle does not cover it, and the board's source line says so.

Finding: the first `use_figma` call failed on a transcription error before any code ran, so nothing partial landed; the retry wrote one clean section, which the read-back confirms.

Question, separate from this write: the page now holds three boards titled "Booking status" — the two earlier draws and this one. Remove the earlier two? The left-hand one carries two sticky notes that would go with it.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.