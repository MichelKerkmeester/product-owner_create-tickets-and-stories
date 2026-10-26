Before I draw this, I need three answers. Each has a recommended answer, so replying "use the recommendations" is enough.

**What I read.** This is a state diagram, because you're asking which statuses exist and what moves an order between them. I took "an order" to mean a Fernhouse order. The `context/` folder holds two sources for it:
- Hamid's order tracking brief (2026-09-18) names six customer statuses: `Order placed`, `Packed`, `Shipped`, `Out for delivery`, `Delivered` and `Delivery failed`.
- Yusuf's carrier tracking facts (2026-09-21) give the carrier codes behind them (`PU`, `IT`, `OD`, `DL`, `EX`) and the rule that an event older than the newest one held for a parcel doesn't change the status.

If you meant a different company or source, tell me before answering.

The sources don't cover cancelled orders, refunds, returns or what happens after an `EX` that isn't `NOT_HOME`. The pallet carrier sends no events at all.

1. **Who reads the board?**
   - Reading: this looks like the status field being agreed before the tracking tasks are written.
   - Recommended: Post-purchase product and the engineers building the timeline.
   - Why: both sources are written for them.

2. **What should the reader be able to do afterwards?**
   - Recommended: see which system or carrier event causes each move, and which moves can't happen. For example, `Delivery failed` goes back to `Out for delivery` but never straight to `Delivered`.
   - Why: that is what the brief and the API notes spell out.

3. **What must the board not do?**
   - Recommended: draw only the six sourced statuses and the moves the two sources state. Leave out cancellation, refunds, returns, pallet orders and the `EX` cases with no stated next step.
   - I would list those under `Left out:` rather than invent them.
   - Why: no source gives their statuses, and drawing them would present guesses as current behaviour.

Once these are settled, I'll replay the settled rows and ask for the write gate separately. Per your instruction, the board goes into FigJam file `<draft-file-key>` as a new section beside what is already there. Nothing existing changes and no new file is created.