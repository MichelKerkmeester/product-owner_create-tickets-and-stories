**Playback: Fernhouse return flow (user flow)**

**Question the board answers:** How does a Fernhouse customer start a return in the app, and where does that path stop?
**Outcome:** A reader can follow each screen from the order list to the QR confirmation and see the 30-day cut-off.

**What your sources settled (app screens and returns doc, as you described them):**
- Order list
- Order detail, with a Start a return button
- Return reasons list
- Choice between a drop-off point and a courier pickup
- Confirmation with a QR code
- Returns are open for 30 days after delivery. After that, the app shows Contact support

**What I assumed (each can be corrected):**
- The 30-day check happens on order detail. Inside the window the customer sees Start a return, and after it they see Contact support. That makes Contact support the failure end.
- Both return methods lead to the same QR confirmation. Your description has one confirmation screen.
- The happy path is the main line, with the 30-day exit beside it. The other option was a state map of every exit, but that costs space and the flow only has one exit.
- The QR confirmation is the goal node and carries the accent colour.
- **Free pickup over €100:** it's a proposal under review, so I'll draw it as a note labelled "Proposed, under review" next to the courier pickup. It won't be drawn as a step. The other option is to leave it off the board.

**Open: where the board goes**
- You asked for a new board in the Fernhouse Product plan, and also for the board to go into the existing file `<test-file-key>`. Those two requests point to different places.
- Flow Mode only writes to a new file it creates, or to a board this same work has already written. That existing file is neither, so I can't compose into it.
- **I recommend** a new FigJam file in the Fernhouse Product plan. I'll confirm the plan with `whoami` before the write gate.

Is this reading right, and are you fine with a new file in the Fernhouse Product plan instead of `<test-file-key>`?

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.