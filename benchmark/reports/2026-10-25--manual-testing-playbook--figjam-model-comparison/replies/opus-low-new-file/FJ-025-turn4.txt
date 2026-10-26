I've stopped before writing anything. No file has been created.

While building the model I found that FigJam sequence diagrams can't draw a branch. The sequence format won't take an authorised-or-declined split. It would flatten the decline messages in with the success messages and lose the split. Each path has to be its own diagram. That means the board won't match what you approved: you said yes to one diagram, and drawing it correctly takes two.

**What would change if you say yes**
- **Plan and file:** no change. A new FigJam file, "Roamstay checkout payment", in the <figma-plan-1> plan
- **Diagram 1, "Card authorised"** (read first): post the booking, hold the room, authorise the card, authorised, confirm the hold, tell the partner hub, 201. That's 7 messages
- **Diagram 2, "Card declined"**: post the booking, hold the room, authorise the card, declined, release the hold, 402. That's 6 messages, with no partner hub message, as you confirmed
- The two diagrams sit side by side in the one file. They share the title, the "Payments brief" source line and the key
- **Calls:** `create_new_file`, two `use_figma` calls (one per diagram) and `get_figjam`. That's one call more than before
- **Undoing it:** the same as before. Deleting the new file removes everything, and I'll only do that if you say yes to a question that names it

**Shall I create "Roamstay checkout payment" in <figma-plan-1> with these two diagrams, "Card authorised" and "Card declined"?**