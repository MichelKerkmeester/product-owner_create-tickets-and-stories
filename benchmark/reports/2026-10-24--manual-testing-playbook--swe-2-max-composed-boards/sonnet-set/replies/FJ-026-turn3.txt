<figma-url>
Read-back: 7 of 7 states, 12 of 12 transitions, 6 of 6 transitions labelled (labels read visually), first glance: the three gray end states
Left out: the 30 minute Pending expiry, it is in the company context but not in your brief
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

The board is a new section named "Booking status" in the existing file, at the right of the existing content. `use_figma` returned 12 of 12 nodes and 12 of 12 connectors with no warnings. Every connector joins the model's two ends and points the way the model draws it. `get_figjam` doesn't return connector label text, so I read the six transition labels off the screenshot.

Completed, Cancelled and No-show are the three light gray boxes. They are the only gray states, and the key calls them "Final state". They share one color, so only the labels tell them apart. A different color per end state is a hand edit in FigJam.

The overview has one finding. The "guest cancels" connector from Confirmed to Cancelled and the "hotel marks no-show" connector leave the same point and share the vertical line at the right of the board. The label sits on that shared stretch, so it can read as applying to the No-show branch too. The fix is to reshape the model, for example by reordering the edges, and compose again. I can't move the connectors. The new board would go in first, and I would delete this one only after your second yes. This is the first attempt, so one more is allowed.