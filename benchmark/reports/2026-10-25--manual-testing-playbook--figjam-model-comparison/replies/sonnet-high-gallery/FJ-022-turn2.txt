Here is the full reading, played back before anything is modelled. Nothing is drawn or written yet.

**The question the board answers:** which screens does a Fernhouse customer pass through to start a return in the app, and where does the 30 day window end it?

**Outcome:** a reader can follow a return from the order list to the confirmation and see where the window stops it.

**What each row rests on**
- Question: captured. It's your wording
- Reader: assumed. A Fernhouse product or support colleague. You can settle it by naming the real reader
- Outcome: assumed, as above. You can settle it by stating what the reader should decide or do
- Scope: captured. One flow, starting a return in the app
- Entry: captured. The order list
- Exit: captured. The confirmation with a QR code, or Contact support after 30 days
- Actors: captured. The customer moves through the screens, and the app decides whether the window is open
- Decisions: captured for the 30 day window and for drop-off point versus courier pickup. The placement of the window check is assumed: it sits on the order detail, and Contact support shows there after 30 days. The returns doc or a screenshot of an expired order would settle it
- Sources and class: captured, with one caveat. I have your description of the app and the returns doc, not the files. The 30 day window and Contact support are current behavior per the returns doc as you describe it
- Live status: assumed. The flow is live. The Fernhouse context note from 2026-09-18 says there is no self-serve return, and the app and the returns doc govern over it. The reply will carry a `Finding:` line naming the clash. A release note or your confirmation would settle it

**What the board must not do (assumed from your "use the recommended answers")**
- Show the free pickup as live
- Add screens beyond the five you listed
- Cover what support does with a return after it is submitted

**Left out:** the free pickup for orders over €100, a proposal under review. It's named on the source line and in the reply.

**The outline, in drawing order.** The first line is the sentence passed to the write.
1. Which screens does a customer pass through to start a return in the app, and where does the 30 day window end it?
2. Node `Order list`, the start (Entry)
3. Node `Order detail (Start a return)`, a screen (Screens)
4. Node `Within 30 days of delivery?`, a decision (Decisions)
5. Node `Contact support`, an exit (Exit)
6. Node `Pick a reason`, a screen (Screens)
7. Node `Drop-off or pickup?`, a decision (Decisions)
8. Node `Confirmation with QR code`, the goal (Exit)
9. Edges, in order:
   - Order list to Order detail
   - Order detail to the window check
   - No from the window check to Contact support
   - Yes from the window check to Pick a reason
   - Pick a reason to the drop-off or pickup choice
   - Drop-off point from the choice to the confirmation
   - Courier pickup from the choice to the confirmation

That's 7 nodes and 7 connectors, within the 9 node budget. Both choices reach the one confirmation, and no edge carries a trigger your sources don't state.

**Two framings**
- The path with a side exit (recommended). The main line runs from the order list to the confirmation and Contact support sits below it. It answers your question directly. The cost is that the 30 day rule reads as a branch rather than a headline.
- Window first. The 30 day rule is the centre and both outcomes carry equal weight. The rule gets more attention. The cost is that the main line shortens, and the board then answers a different question about the window rather than the path.

**The look (all assumed, correctable now)**
- Colour: the confirmation is the one accented goal. Contact support is a plain exit and not a failure, since a closed window is expected behavior
- Detail and audience: balanced detail, a mixed audience in the app's own words, read on a laptop
- Zones: three. "Find the order" holds Order list and Order detail. "Request the return" holds the window check, Contact support, Pick a reason and the choice. "Done" holds the confirmation
- Text: the title is `Start a return`. The subtitle is "How a Fernhouse customer starts a return in the app, from the order list to a confirmed return". The source line is "Sources: the app and the returns doc, as described in the request. Left out: free pickup for orders over €100, a proposal under review."
- Critique: the write gate will answer four questions about the sketch, starting with where the eye goes first and whether that is the node the board most needs read

Is this the right reading of the board? If any assumed row is wrong, name it and I'll replay only the rows it touches.