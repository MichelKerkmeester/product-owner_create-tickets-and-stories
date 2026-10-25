<figma-url>
Read-back: 7 of 7 states, 12 of 12 transitions, 6 of 6 transitions labelled, first glance: the end states (Completed, No-show and Cancelled in light gray), read visually for the labels
Left out: refunds, payment steps, hotel-side cancellation and any No-show window, none of which your request covered

The new "Booking status" section is on the retro board at x 48448, y -608, to the right of everything already there. The compose call reported 0 warnings and tagged the section.

**What I measured:**
* **From `get_figjam`:** each state shows its label, and Confirmed is a section around Upcoming and In stay. All 12 `edge:` connectors join the right ends in the right direction, with an arrow at the end only. The routed ones run through their anchors from the source node.
* **Read visually:** the outline doesn't return connector label text, so I read the labels from the compose screenshot. They are "card authorised", "check in", "check out", "guest cancels" twice and "hotel marks, missed check-in".

**One layout note:** the Confirmed to Cancelled "guest cancels" line leaves Confirmed on its left edge and runs under the whole diagram. It is correct but long. A shorter route needs a change to the model and a recompose, which I'd only do after a yes from you.

I planned to load Figma's `figma-use` and `figma-use-figjam` guidance before the write, but this session has no tool for loading them. I wrote with the Flow Mode composer alone.

**Delete question:** the older "Booking status" section (`62:66`) is still on the board, so there are now two. Do you want me to delete the old one by its id?

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.