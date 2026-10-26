Nothing is written to the file yet. This is intake round one, and I need three answers before I model the board.

**Settled so far**
- Question: which screens does a Fernhouse customer pass through to start a return in the app, and where do they choose? That is a user flow.
- Screens in the order you listed them: the order list, the order detail with a Start a return button, a list of return reasons, a choice between a drop-off point and a courier pickup, and a confirmation with a QR code.
- Window: returns are open for 30 days after delivery, and after that the app shows Contact support. I class this as current behavior.
- Left out: the free pickup for orders over 100 euros. It is a proposal under review, so it stays off the board and goes on the `Left out:` line.
- Target: a new section in the existing file `<draft-file-key>`, beside what it already holds and with nothing already there touched.
- Plan: I read "new board in our Fernhouse Product plan" as a new section in that existing file. I can't confirm which plan owns the file. A new file is created only if that file can't be written, and then it goes in the Barter team plan, in drafts, with no project, as you said. Your two plan lines differ for a new file, so tell me if Fernhouse Product should win in that case.

**1. Who reads the board and what do they decide?**
- Reading: the request names the customer's path but not the reader.
- Recommended: the Fernhouse product and design team, who should be able to follow a return from the order list to a confirmed return and see where the 30-day window ends it.
- Why: it matches the screens and the window rule you gave.

**2. What must the board not do?**
- Reading: the sources show five screens, one window rule and one proposal.
- Recommended: it never draws the free pickup as live behavior, and it adds no step the sources don't state. That rules out choosing a drop-off point or a pickup slot, and anything after the confirmation.
- Why: your list goes straight from the method choice to the confirmation, so a step between them would be invented.

**3. Where does the 30-day rule sit in the flow?**
- Reading: the doc says the app shows Contact support after 30 days, but not on which screen. I also take your list order as walk order, so reasons come before the method choice.
- Recommended: a "Within 30 days?" choice right after Order detail. Yes, labelled "Tap Start a return", goes on to the reasons, and No goes to Contact support as an exit beside the main line.
- Why: Order detail is the first screen where the app can differ, and it keeps the failure exit visible without adding a screen. That gives 7 nodes, inside the 9-node budget.

Answer any of these, or say "go with the recommendations" and I'll send the full playback next. A recommendation I use without your answer is marked assumed in that playback, so you can correct it before the write gate.