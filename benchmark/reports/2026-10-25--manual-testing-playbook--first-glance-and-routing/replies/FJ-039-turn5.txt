The model passed the pre-write check and composes cleanly, so this is the write gate. Nothing is on the board yet.

**What the board answers**
- **Question:** who does what, in which order, from a customer's first contact to the refund
- **Outcome:** the reader can see where work changes hands and which refunds need a second person

**What should win**
- **First glance:** "Refund issued", the goal and the only accent
- **Second glance:** the handoffs between the four lanes
- **Last glance:** "Approve the refund" in the CS lead lane, which can wait

**The write**
- **Plan and file:** Fernhouse Product, as you supplied it, in the existing file `<test-file-key>`. No new file is created
- **What lands:** one composed board titled "Fernhouse return flow", with 4 lanes (Customer, CS agent, Warehouse, CS lead), 8 nodes, 8 connectors, 2 labelled decision exits, a key and a source line, at Laptop distance. It sits 400 pixels to the right of anything already on the page
- **Still assumed:** the customer sending the parcel back, and the €200 decision sitting after the warehouse check
- **Left out, and named on the board:** the 30-day window outcome, a failed warehouse check and a declined approval
- **Extensions:** none
- **Calls:** `create_session`, one `use_figma` and one `get_figjam` read-back. If the file's owner is on a Starter plan or has a View or Collab seat, that is part of a six-call monthly allowance
- **Rollback:** delete the one board section the write returns. That happens through `use_figma` and only after your separate yes, so the existing content is never touched

Do you want me to write this board to the file?