The model passes the pre-write check and composes cleanly. Nothing is written yet, and I've spent no Figma calls. The `figma` tools `create_session`, `use_figma` and `get_figjam` are all connected.

**Playback**
- **Question the board answers:** who handles a Fernhouse return today, and where does it change hands?
- **Type:** process with three lanes (Customer, CS agent, Warehouse), left to right.
- **Reader and outcome:** the Post-purchase team and CS leads, who should see where the handoffs sit.
- **Dials:** balanced detail, mixed audience, laptop reading distance.
- **Source:** `context/fernhouse-context.md`, Key flows item 6, class current behavior.

**Board, 6 nodes and 5 connectors**
1. Customer contacts CS (start, Customer lane)
2. Within 30 days? (decision, CS agent lane)
3. Create the return in Admin (CS agent lane, reached on the Yes exit)
4. Email the return label (CS agent lane)
5. Check the item (Warehouse lane)
6. Refund issued (end, CS agent lane, drawn as the goal)

The subtitle carries "6 days on average from first contact", which the source states. I'm adding no accent or step in focus, because no source says which handoff causes the delay.

**Assumed rows (correct either of these before the yes)**
- The CS agent applies the 30-day check. The source states the rule but not who applies it.
- The decision has a Yes exit only. No source states what happens outside 30 days, so I'm not inventing a No branch.

**Glance lines**
- **First:** a return crosses three hands before the refund.
- **Second:** the steps in order, with the 30-day check at the front.
- **Last:** the open points in the source line.

**Left out:** what happens outside 30 days (no source), a failed item check (no source), the customer's parcel travelling to the warehouse (not stated, so the label-to-check edge is read from the source's step order) and the 1,900 monthly requests (a volume, not a step). I also did not draw the self-serve app flow from the skill's worked example. It has invented screens, and the company context says no self-serve return exists today.

**Write gate**
- **File:** `<test-file-key>`, an existing FigJam file, so no new file is created. The plan was fixed when the file was made, and I can't confirm it is Fernhouse Product without a read. Tell me if that matters.
- **Writes:** one composed board titled "Fernhouse return today", with 3 lanes, a key and a source line. It lands 400 px right of existing content and covers nothing.
- **Calls:** `create_session`, one `use_figma` and one `get_figjam` read-back. If the board needs a close look, I'll add a `get_screenshot`. On a Starter plan or a View or Collab seat, Figma caps tool calls at six a month, and read calls count toward that.
- **Rollback:** I'd delete only the one board section the write returns, and only after you say yes to that deletion.

A yes confirms both the reading and the write. Write it?