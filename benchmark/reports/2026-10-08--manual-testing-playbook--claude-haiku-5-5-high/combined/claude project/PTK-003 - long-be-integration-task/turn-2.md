```markdown
# BE - SHIP - Label webhook fix

Noted: a standalone task on the Fulfilment board, the 8-second warehouse timeout kept and the two done criteria. Before drafting, I need the five decisions below in one response.

**Late label after a recreate:** After a `label.failed` with `SERVICE_UNAVAILABLE`, the handler creates the shipment again. If the carrier can still send `label.created` for the first shipment, the parcel ends with two labels, and the notes list no cancel call. Should the task hold the recreate until the carrier answers, or build the handling now while the answer is open?

**Other error codes:** The thread covers recreating only for `SERVICE_UNAVAILABLE`. Should `ADDRESS_INVALID` and `OTHER` keep their current handling?

**Straggler label copy:** The 10-minute GET returns a `label_url` that expires after 24 hours. Should that path also copy the label into our own storage, as the webhook path does?

**Signature check:** Is the `X-Carrier-Signature` check, with `401` on mismatch against the raw body, part of this task, or already in place?

**Out of scope:** Confirm these stay out: the 37 duplicate labels already billed, the 12 late orders already sent late and any repair of shipments stuck before the fix. Name any you want in.

Unless you change them, the acceptance conditions are the thread's values plus your two done criteria.
```

Export-equivalent path: `export/NNN - task-label-webhook-fix-clarification.md`

This is a second clarification because the first round left the failure path, the signature check and the out-of-scope items open. The first one stays as it stands. The carrier's answer on `label.created` after `label.failed` decides the guard, and the notes list no cancel call, so I have not drafted around it. Once you answer, the task takes the next number in the task lane.

Quality status: not applicable, no artifact drafted.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.