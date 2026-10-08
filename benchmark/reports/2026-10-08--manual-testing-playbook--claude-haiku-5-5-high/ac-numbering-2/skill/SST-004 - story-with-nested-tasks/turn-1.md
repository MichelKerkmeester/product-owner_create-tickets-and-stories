Path: `export/001 - Story-order-tracking-clarification.md`
Verified: read-back succeeded; 21 lines
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

This is a Story (with its tasks as one bundle), but there is no draft yet. The `$story` command asks its context question before drafting, and this file holds only that question. It asks you to settle six points: the task split, which team owns the handoff from shipping-service to the order status, whether `Delivery failed` shows a reason, what a parcel point drop shows, which time zone the delivery window uses, and whether FE Web waits for the web layout. It also lists three defaults I'll apply unless you change them: mixed parcel and pallet orders, translation inside each FE task, and the carrier rules as hard constraints.

Once you answer, the bundle saves as `export/002 - Story-order-tracking/`, and the clarification file stays unchanged.