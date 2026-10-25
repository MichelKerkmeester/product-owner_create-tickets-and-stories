<figma-url>
Read-back: 7 of 7 states, 12 of 12 transitions, 6 of 6 transitions labelled, first glance: the end states, with the two notes beside Cancelled and No-show
Extensions: 2 of 2 notes, 0 overlaps
Left out: refunds and payment steps, cancellation by the hotel or Roamstay, and any No-show window, because the request gives none of them
Findings, as measured:
* The board shows "InStay" and "NoShow", not "In stay" and "No-show". I left out the description lines that would show your wording, so this is a miss on my side. Fixing it means recomposing the board, and I'd only delete the current one after a second yes from you.
* The stickies are 144 pixels square and Figma's API can't resize them, so each note has blank space under its text. Moving or reshaping them is a hand edit in FigJam.
* The Cancelled and No-show arrows leave the edge of the Confirmed box, not Upcoming. A missed check-in can only happen before check-in, but a diagram can't draw a move out of a state inside a box.

The board is a new section named "Booking status" in your existing file, 400 pixels right of what was there. The state, transition and note counts come from a `get_figjam` read of the board. The six transition labels come from the list the write returned and the screenshot, because the read doesn't return label text. The "check in" label is the one I assumed, so correct it if support uses another word.
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

Do you want me to recompose the board with "In stay" and "No-show" in the labels?