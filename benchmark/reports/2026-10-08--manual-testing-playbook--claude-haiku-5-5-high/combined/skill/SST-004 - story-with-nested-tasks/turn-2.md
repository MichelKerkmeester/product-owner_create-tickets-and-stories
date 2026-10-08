Export complete. The bundle saved as `002`, and the clarification file `001` is untouched.

Kind: Story, saved as one bundle folder.

Path: `export/002 - Story-order-tracking/002 - Story-order-tracking.md`
Verified: read-back succeeded; 183 lines

Path: `export/002 - Story-order-tracking/002.1 - task-order-page-timeline-ios.md`
Verified: read-back succeeded; 84 lines

Path: `export/002 - Story-order-tracking/002.2 - task-order-page-timeline-android.md`
Verified: read-back succeeded; 84 lines

Path: `export/002 - Story-order-tracking/002.3 - task-order-page-timeline-web.md`
Verified: read-back succeeded; 84 lines

Path: `export/002 - Story-order-tracking/002.4 - task-carrier-tracking-webhook.md`
Verified: read-back succeeded; 81 lines

HVR self-scan: 3 hard blockers. Fixed: three Rabbit holes bullets that ended with a full stop. Kept with reason: `TBD...`, the named house token in the Delivery slots.

Quality: each requirement traces to a supplied value, and every open point is marked where it sits rather than filled in.

Three points stay open, so the Story carries `**Open:**` lines and a Delivery section: the drop at a parcel point, the retry for `ADDRESS_PROBLEM`, `DAMAGED` and `REFUSED`, and orders dispatched before release. I named Hamid for the first and third and Yusuf for the retry rule, based on who wrote each source; change any owner that is wrong. The webhook task is last because you asked for that order, though all three app tasks read what it stores. The source does not say how the mapped status reaches orders-service, so the webhook task flags that hand-off for confirmation.