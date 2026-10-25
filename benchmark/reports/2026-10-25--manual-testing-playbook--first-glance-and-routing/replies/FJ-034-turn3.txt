The model passed the pre-write check, so this is the gate. The 8 steps and 8 connectors read as a laned process with 0 crossing pairs. The composed code is 44,479 of the 50,000 characters one `use_figma` call takes. The `use_figma`, `get_figjam` and `create_session` tools are all connected in this session.

**What the board must deliver**
Question: who does what, and where does a damaged-item refund change hands between the customer, CS and the warehouse?
Outcome: CS and warehouse leads agree who owns each handoff.

**What should win, in order**
1. First glance: "Refund released", the green goal with the pink outline.
2. Second glance: the two handoffs, from Customer to CS and from CS to Warehouse on "Approved".
3. Last glance: the second-photo loop and the source line, which names what was left out.

**The write**
- File: `<test-file-key>`, the existing FigJam file, not a new one. You named the Fernhouse Product plan. I haven't confirmed that this file sits in that plan, because the tools can't tell me which plan owns a file.
- Content: one board section titled "Damaged-item refund", with a subtitle, three lanes (Customer, CS and Warehouse), 8 steps, 8 connectors, a key and a source line. It lands 400 pixels to the right of what is already on the page, so nothing existing is touched.
- Tag: the section carries a small tag with the title, the write time and the counts. A later session uses it to find this board.
- Extensions: none. No notes or pins are added.
- Team colour: no per-team fills, as agreed. Those are a hand edit in FigJam afterwards.
- Left out, as named in the playback: the outcome after a second photo, a failed inspection, refund policy and the pickup carrier.

**Calls**
The write uses 3 tool calls: `create_session`, one `use_figma` call to compose the board and `get_figjam` to read it back. If a node needs its own screenshot, that is a fourth call. A Starter plan or a View or Collab seat is limited to six tool calls a month, and this write would spend half of that.

**Rollback**
I would delete only the one board section this write returns, through `use_figma`. That happens only after you say yes to the deletion, and it costs one more call. If the read-back can't run, I can't delete anything and you would remove the board by hand.

Do you want me to write this board into `<test-file-key>` now?