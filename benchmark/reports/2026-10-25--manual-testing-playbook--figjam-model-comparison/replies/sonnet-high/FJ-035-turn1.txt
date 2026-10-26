I read the target file, so this is the playback before anything is drawn. Nothing has been written.

**Question:** which screens does a Fernhouse customer pass through to start a return in the app, and where do they choose?
**Outcome:** a reader can follow a return from the order list to a confirmed return and see where the 30 day window ends it.

**Settled by your message:**
* The screens are the order list, the order detail with Start a return, the reasons list, the drop-off or pickup choice and the confirmation with a QR code
* The 30 day window runs from delivery and ends in Contact support

**Type:** a user flow, left to right, in three zones: Find the order, Request the return and Done. The confirmation is the goal and Contact support sits below the main line as an exit. That is 9 nodes and 4 labelled exits, with a title, a key and a source line.

**Assumed:**
* Balanced detail, a mixed audience and a laptop reading distance
* The window check sits right after Order detail, so a customer past 30 days gets Contact support where Start a return would have led

**Still open, with my recommendation for each:**
1. **The sources.** No screenshots and no returns doc reached this session, and the file holds neither. I would draw from your description alone and mark the source line that way. If you can attach the screens or the doc, I will read them first.
2. **Current or proposed.** `context/fernhouse-context.md`, updated 2026-09-18, says "There is no self-serve return today": a customer contacts CS and an agent creates the return in Admin. It does match your 30 day window. Your flow describes an in-app return, so it is either unreleased or newer than that note. I would label it current behavior only on your word. Otherwise I would put its status in the source line, since a proposal never reads as current behavior.
3. **The file.** `<draft-file-key>` is a FigJam file, but it holds two Roamstay checkout sequence boards and nothing from Fernhouse. A Fernhouse board would land as a new section beside them, and I would change nothing already there. I cannot tell from here whether it is the board open in your Figma Desktop. I would use the key, as you wrote it.

Is this the right reading of the board, and do you want the recommendations on the three open points?