The model is ready and nothing is written yet. `flow_check.py` passed it as a process with 8 nodes and 8 connectors, and `compose_board.py` composed it with no errors. The board has no connector crossings.

**Question:** who does what in a damaged-item refund, and where does the claim change hands?

**Outcome:** a reader can see which team owns each step. They can also see where an approved claim moves from CS to the warehouse.

**First glance:** "Approve the claim", the CS to warehouse handoff. It is the one highlighted step, and the connector leaving it is labelled "To warehouse queue".

**Second glance:** "Damage clear?", the check that sends a claim to approval or back to the customer for a second photo.

**Last glance:** the claims table, which stays on the board without competing for attention.

**Target:** a new board section in the existing file <test-file-key>, in the Fernhouse Product plan you named. I am not calling `whoami`, because it can't tell me which plan owns this file.

**Writes**
* One composed board with 3 lanes (Customer, CS agent, Warehouse operator), 8 nodes and 8 connectors
* A title, subtitle, key and source line, at Laptop reading distance
* The board lands to the right of anything already on the page, so nothing existing is covered or changed

**Assumed, because you didn't answer them**
* The board is for CS and warehouse leads
* The board shows no services or tools and doesn't present the €20 pickup pilot as live
* One dashed "Logs" link runs from "Damage clear?" to the claims table, which sits in the CS lane

**Left out:** the pickup skipped under €20, because the pilot is not live. The source line also says the runbook has no path for a failed inspection.

**Extensions:** none.

**Calls:** `create_session`, a read of Figma's `figma-use` and `figma-use-figjam` skills, one `use_figma` write and one `get_figjam` read-back. A Starter plan or a View or Collab seat gets only six tool calls a month, and this uses about five of them.

**Rollback:** I delete the one board section the write returns, found by its tag. I do that only after you say yes to the deletion. Nothing else in the file is touched.

Write it?