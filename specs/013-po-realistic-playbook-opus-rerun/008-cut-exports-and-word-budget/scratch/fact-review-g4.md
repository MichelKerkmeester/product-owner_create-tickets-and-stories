claude project/PDK-004 - 002 - doc-loomlist-activity-emails.md | 62 | 58 | Dropped | "The `digest-sender` job, which builds the list for each recipient and hands the batch to the email delivery provider" (the hand-off survives in the Sender rule; what the job does, building each recipient's list, appears nowhere)
claude project/PEP-002 - 002 - Epic-offline-mode.md | 36 | 35 | Changed | "Start uploading queued changes within 30 seconds of the connection returning, oldest first" (cut reads "Upload queued changes oldest first, within 30 seconds of reconnecting", so a start deadline now reads as a finish deadline)
claude project/PEP-002 - 002 - Epic-offline-mode.md | 103 | 97 | Changed | "from settings they can see the space offline data uses, lower the cap and clear offline data" (cut "can lower the cap and clear it" makes the cap the thing cleared)
claude project/PIR-002 - 002 - Story-customer-wishlist-account-wishlist-in-apps.md | 23 | 23 | Dropped | "Items saved on a device before signing in move into that list, so the switch never costs a customer what they already saved." (the only reason given for moving device items into the account list)
claude project/PIR-002 - 002 - Story-customer-wishlist-account-wishlist-in-apps.md | 49 | 48 | Dropped | "A product saved in both lists is kept once and counts once toward the limit" (cut keeps "counts once" and loses "is kept once", the deduplication requirement)
claude project/PIR-002 - 002 - Story-customer-wishlist-account-wishlist-in-apps.md | 64 | 63 | Changed | "When they add or remove an item on either surface" (cut "When they change an item on either" no longer names add and remove as the triggering actions)
skill/SDK-003 - 002 - doc-sync-conflict-options.md | 21 | 21 | Changed | "Pages edited on phones are over-represented in conflicts, since phones sync less often in the background." (cut "their edits dominate conflicts" turns over-representation into a majority claim no figure supports)
skill/SDK-003 - 002 - doc-sync-conflict-options.md | 110 | 100 | Changed | "Tomasz runs a two-week spike on Option B against a sample of real August conflicts" (cut drops "a sample of", so the spike reads as covering all August conflicts)
skill/SDK-003 - 002 - doc-sync-conflict-options.md | 136 | 124 | Dropped | "Settle mixed-version behavior during a rollout, when some clients keep a base version and others still run v3, which the thread does not cover" (the reason the item is open is gone, while its sibling to-do-fields item keeps its reason)
skill/SST-004 - 001 - Story-order-tracking/001 - Story-order-tracking.md | 15 | 15 | Dropped | "Customers copy the number into the parcel carrier's own site, and the ones who get lost there contact CS." (today's workaround and how it feeds CS; line 13's "Most of those customers already had a tracking number" went with it; the FE tasks keep only "so customers skip the carrier's site")
skill/SST-004 - 001 - Story-order-tracking/001 - Story-order-tracking.md | 98 | 89 | Changed | "After a second `NOT_HOME` the parcel goes to a parcel point" (cut "and a second sends it to a parcel point" leaves "a second" free to mean a second `OD` or retry rather than a second `NOT_HOME`)
skill/SST-004 - 001 - Story-order-tracking/001 - Story-order-tracking.md | 159 | 150 | Changed | "Then the pallet item keeps today's status display with the booking line, and shows no tracking timeline" (cut "it keeps today's display ... and no timeline" follows "an order with a pallet item", so the whole order, parcel items included, now reads as keeping today's display)

Files read: 11 (snapshot and cut for each). Problems found: 12.

No problems: claude project/PBG-001 - NNN - bug-ios-cart-badge-stale-after-remove.md, skill/SST-003 - fernhouse-save-card-draft.md, and the four SST-004 tasks 001.1, 001.2, 001.3 and 001.4.

## Verdicts on the cuts the writer flagged

- SDK-003, Cost bullets under A, B and C: fine. The trade-off table carries all three costs under "Cost, Tomasz's estimate".
- SDK-003, A's "Leaves open" bullet: fine. The table's "Two edits to the same text still lose one" carries it.
- SDK-003, B's "Not stated" to-do-fields bullet: fine. Open decisions line 123 carries the examples and the reason "as the thread covers block text only".
- SDK-003, Option C paragraph pointed at the table: fine. The table carries always-merge, no copy, protocol v4, the page and client migration and the two-quarter cost.
- SDK-003, Tomasz's lean toward B depending on Saskia's fallback: fine. The positions table keeps "Leans B | Only with Saskia's formatting fallback", and line 60 keeps the fallback in the spike.
- SDK-003, the sentence on what the spike is for: fine. Joana's row names storage cost and fallback rate as unknown, and open decisions lines 120 and 121 carry both measurements.
- SDK-003, C's "This round" bullet: fine. Line 102 "unsized before 2026-10-09" and the out-of-scope "Sizing Option C in this round" carry it.
- PDK-004, the EM-02 and EM-03 mentions-in-replies notes: fine. The shared rule "Mention inside a reply, Sends EM-02 only, never EM-03 too" carries it.
- PDK-004, the "Other emails" and "Push notifications" boundary bullets: fine. The Overview out-of-scope line carries both, with the owning teams.
- PDK-004, the one-line intros for EM-02, EM-03, EM-04 and EM-06: fine. Each restated its Sent when bullet.
- PDK-004, EM-02's explanation of what a mention is: fine. It is background, not a condition.
- PDK-004, the two glossary entries merged into rules: fine. The Time zone rule carries profile time zone and local time, and the Footer rule carries the footer and the EM-05 exception.
- PDK-004, "builds each recipient's list" for digest-sender: Dropped, listed above.
- SST-003, the merged 5-card limit bullets: fine. Line 33 keeps 5 per account, across platforms, sixth refused.
- SST-003, "even on a tenth order": fine. It is color.
- SST-004 Story, "customers who get lost on the carrier's site contact CS": Dropped, listed above.
- SST-004 Story, the compressed NOT_HOME retry condition: Changed, listed above.
- SST-004 001.1 to 001.3, "`Delivery failed` never shows a reason": fine. "Never" still covers the case where the carrier sends one, and the Story line 42 keeps "even with an `exception_code`".
- SST-004 001.3, dropped "which now holds the web layout beside the apps": fine. Checklist line 40 keeps "Layout matches the web layout in the `Order page / Tracking timeline` design frame".
- SST-004 001.4 About, the missed-DL line: fine. The Story keeps "A dropped or missed `DL` leaves the last status, and the carrier cannot resend it" in Rabbit holes (line 176), and 001.4 keeps the requirement and its reason.
- PEP-002, "Desktop covers the laptop case": fine. The first reason for leaving Web out stays.
- PEP-002, the benefit sentence repeating the Goal: fine.
- PIR-002, "This story saves": fine. The wording is unchanged from the snapshot, and in a Story signed off for delivery it reads as the proposed change, backed by line 11's "this is a product change, not a fix" and requirements such as "as today" for the unchanged case.
- SST-004 FE tasks read alike: confirmed. A diff between the cut 001.1 and 001.2 shows only the title, the platform word in About and the related-task link. A diff between 001.1 and 001.3 shows the same plus checklist line 40's "web layout in", which the snapshot also had.
