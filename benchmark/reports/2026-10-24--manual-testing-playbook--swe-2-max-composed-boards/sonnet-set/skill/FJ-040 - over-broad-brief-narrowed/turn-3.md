The model for all four boards passes `flow_check.py`, and each composes. Nothing is written yet.

One change from the playback: the Warehouse board ran 9 steps and the limit is 8. I merged "Order paid" and "Send the order to the warehouse system" into one start step, "Paid order sent to the warehouse". No source item was lost.

Check results:
- 1. Returns: 6 nodes, 5 connectors, 3 lanes, 0 crossings
- 2. Refunds: 5 nodes, 5 connectors, 3 lanes, 2 of 2 decision exits labelled, 0 crossings
- 3. Warehouse: 8 nodes, 7 connectors, 4 lanes, 0 crossings
- 4. Billing: 5 nodes, 4 connectors, 4 lanes, 0 crossings

Glance lines:

| Board | First glance | Second glance | Last glance |
|---|---|---|---|
| Returns | "Continue to refund", the goal and the hand-off | Which lane owns each step | The 30-day window and the two gaps in the source line |
| Refunds | "Approve the refund", the one step in focus | The "Refund over €200?" decision | The refund email end |
| Warehouse | "Collected at 18:00", the goal | The label request and its return to the shipping service | The pallet and after-cut-off omissions in the source line |
| Billing | "Order placed", the goal | "Authorise the payment" | The declined-payment gap in the source line |

Three edges are inferred from lane order, not stated outright:
- "Receive the label event" to "Pack and label the parcel" (Warehouse)
- "Report the order packed" to "Collected at 18:00" (Warehouse)
- "Send the item back" in Returns, which you confirmed

Gate:
- Plan and file: the Fernhouse Product plan as you named it, in the existing file `<test-file-key>`. No new file is created.
- Writes: four composed boards in the order Returns, Refunds, Warehouse, Billing, read left to right with 400 pixels between them. Each has a title, subtitle, key and source line. There are no extensions.
- Calls: `create_session` once, then `use_figma` four times (one per board) and `get_figjam` four times to read back. That is about nine calls. A Starter plan or a View or Collab seat is limited to six tool calls a month, so tell me if that applies and I'll write fewer boards per run.
- Rollback: delete the four board sections the writes return, through `use_figma`, only after your separate yes to the deletion.
- Left out, as the reply will state:
  - Signup
  - Self-serve returns
  - The pallet carrier
  - The after-30-days exit
  - A failed item check
  - A CS lead rejecting a refund
  - Where refunded money returns to
  - Orders after the 15:00 cut-off
  - A declined payment
  - Saved cards
  - Discount splits on orders from before 2026-05-01

Write it?

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.