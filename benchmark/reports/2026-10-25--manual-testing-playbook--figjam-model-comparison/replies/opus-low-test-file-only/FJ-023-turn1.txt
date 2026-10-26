This is the playback step. Nothing is written to a board until you confirm what I've read here and then give a separate yes at the write gate.

**What the board answers:** how a damaged-item refund moves between the customer, CS and the warehouse, and where the claim is handed to the warehouse.

**Diagram:** a process in three lanes (Customer, CS, Warehouse).

**What the runbook gives me:**
1. Customer: reports the damage with a photo through the help form.
2. CS agent: checks the photo. This is a decision with two exits:
   - **Clear damage:** the agent approves the claim on the spot.
   - **Unclear:** the agent asks for a second photo, and the claim goes back to the customer to send another.
3. **Highlighted handoff:** the approved claim goes to the warehouse queue. This is the one accented step and the first thing a reader should see.
4. Warehouse operator: books a courier pickup.
5. Warehouse operator: inspects the item when it arrives.
6. Warehouse operator: releases the refund. The process ends here.

**Assumptions to confirm:**
- **Claims table:** I'll show "every decision is logged in the claims table" as one note on the board. Drawing a log step after every decision would clutter the diagram.
- **Under-20-euro pilot:** this skips the pickup but isn't live yet, so I'll leave it out of the drawn process and list it under "Left out" when I deliver. The other option is a note marked "proposed, not live".
- **Second photo:** the runbook doesn't say what happens if the second photo is still unclear, such as a rejection or an escalation. I'll draw only the loop back to the photo check and flag the gap.
- **Customer refund:** the runbook doesn't say whether the customer is notified when the refund is released, so I won't draw that.

**To settle at the gate:** you asked for a new board, but also to write into file `<test-file-key>`. I can only write into an existing file if it's a board this work created. Otherwise the board goes into a new file, so I'll ask you to choose at the gate.

Is this reading right, including leaving the pilot out and keeping the claims table as one note?