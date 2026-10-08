The Story now reads back with the fix in place. Here is the bundle.

**Story:** `export/002 - Story-order-tracking/002 - Story-order-tracking.md`
Verified: read-back succeeded; 187 lines

**Tasks, in your order:**

- `export/002 - Story-order-tracking/002.1 - task-order-tracking-ios.md`
  Verified: read-back succeeded; 69 lines
- `export/002 - Story-order-tracking/002.2 - task-order-tracking-android.md`
  Verified: read-back succeeded; 69 lines
- `export/002 - Story-order-tracking/002.3 - task-order-tracking-web.md`
  Verified: read-back succeeded; 70 lines
- `export/002 - Story-order-tracking/002.4 - task-carrier-tracking-webhook.md`
  Verified: read-back succeeded; 98 lines

HVR self-scan: 0 hard blockers. Fixed: rather (always-cut modifier, removed in place). Kept with reason: TBD... (the fixed house placeholder for unknown Delivery values, set in story-mode section 6.9).

Quality summary: Story prose is 1,341 words against a 1,400 cap, and the webhook task is 461 against 500. The other tasks run 320 to 343. Bullets carry no full stops, and the bundle has no dashes or semicolons.

The Story is a Story with its tasks, and the three questions you did not answer are now `**Open:**` lines in Requirements, which also brings in the Delivery section. They are the owner of the status handoff, whether a parcel-point drop shows `Delivered` and the time zone of the window. The webhook task is listed last, but the three front-end tasks depend on its data, so you may want to reorder it.

Additions I made that you did not state, so you can strike any of them:
- Mixed parcel and pallet orders keep a timeline for the parcel and today's page for the pallet item (acceptance criterion 6).
- Status text translation sits inside each front-end task.
- The carrier rules and the peak volume of about 43,000 events go into the webhook task as constraints.
- The platform support (iOS 16, Android 9, two latest browser versions) and the app store approval dependency come from the company background.
- Acceptance criteria 3, 4 and 7 come from the carrier ordering rule, the failed-delivery flow and the tracking history rule.

No Figma link is in the bundle, because none was supplied. The frame appears by name only.