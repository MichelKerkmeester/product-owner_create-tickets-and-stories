<figma-url>
Read-back: 7 of 7 states, 12 of 12 transitions, 6 of 6 transitions labelled, first glance: Pending, the Sprint retro section left as it was (1 section, 6 of 6 stickies unchanged), labels read visually
Left out: a declined or expired card authorisation, refunds and booking edits, none of which were in the request
Finding: the `get_figjam` read returns layer names and not connector text, so the six transition labels were read from the overview screenshot and not from the read.
Finding: the "check out [from In stay]" and "missed check-in [from Upcoming]" lines run 24 pixels apart over about 240 pixels, right of Confirmed, so they read as near-parallel. A fix is a model change composed again after a yes, such as declaring the No-show move before the Completed move. I have not confirmed that it separates them.
Finding: the "card authorised" line leaves the top of Pending and enters Confirmed at its left edge, so the main route does not read left to right. The composer places a composite from its first inner state, so this is a composer limit and not a model error.
Finding: the booking-status board lands to the right of Sprint retro, so scroll right from the retro stickies to find it.
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.