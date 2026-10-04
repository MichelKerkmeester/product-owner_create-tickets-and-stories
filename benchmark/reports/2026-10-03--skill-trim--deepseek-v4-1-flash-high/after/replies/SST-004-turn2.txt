**Delivered — Story bundle, Story shape, 1 Story + 4 tasks**

`Path: export/002 - Story-order-tracking/002 - Story-order-tracking.md`
`Verified: read-back succeeded; 146 lines`

`Path: export/002 - Story-order-tracking/002.1 - task-ios-tracking-timeline.md`
`Verified: read-back succeeded; 72 lines`

`Path: export/002 - Story-order-tracking/002.2 - task-android-tracking-timeline.md`
`Verified: read-back succeeded; 72 lines`

`Path: export/002 - Story-order-tracking/002.3 - task-web-tracking-timeline.md`
`Verified: read-back succeeded; 72 lines`

`Path: export/002 - Story-order-tracking/002.4 - task-carrier-tracking-webhook.md`
`Verified: read-back succeeded; 77 lines`

`HVR self-scan: 0 hard blockers. Fixed: the "not just" contrast in Story acceptance criterion 1 and its always-cut "just", rewritten to a plain statement. Kept with reason: literal identifiers and supplied strings such as X-Carrier-Signature, NOT_HOME, Arriving Thursday 1 October, The delivery company will call you to book a delivery slot and Order page / Tracking timeline, kept because the source supplied them and supplied values travel verbatim.`

**Quality summary:** All six dimensions at or above floor, Accuracy at 9 with the volume, mapping and timing claims each landing on a supplied line from Yusuf's notes or the brief. Story uses 1,270 words of its 1,400 budget, tasks 371 to 466 of 500. House grammar holds across the set: Story preamble, `* * *` section closes above every `##   ` spacer, `- []` requirement items, no full stop on any bullet, H4-or-shallower depth, no ticket fields, points or INVEST notes. The four-task split follows the order you gave (iOS, Android, web, BE), numbered `002.1` to `002.4`.

**Summary:** The Story carries the cross-cutting product rules (status ladder and code mapping, `occurred_at` ordering, estimate semantics, per-parcel and pallet handling, `90 days` retention, six locales, shipping email) with seven outcome-led criteria covering the three surfaces. Each FE task delivers the timeline, the estimate and the parcel edges on its own surface, and the BE task carries the webhook contract, dedupe, signature, retry schedule and peak volume. Deliberately out of scope and named in the Story's About: a push notification per status, an address or delivery-day change after dispatch, return parcel tracking and the DATA events, per your answer. One derived item to strike if you disagree: the BE task states a peak-day limit of about 43,000 events, worked out from Yusuf's parcel and event counts rather than written down as a limit. No ClickUp tooling is available in this runtime, so the bundle is local only.

**Next:** say if you want the web, iOS and Android tasks collapsed into one cross-platform FE task, or the BE task split into receive/store and status-mapping pieces.