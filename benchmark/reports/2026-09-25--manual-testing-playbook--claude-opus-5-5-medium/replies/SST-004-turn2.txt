I've updated the bundle in place. There are now four tasks in the order you gave. I deleted the Packed and DATA task files and renumbered the rest.

Path: `export/001 - Story-order-tracking/001 - Story-order-tracking.md`
Verified: read-back succeeded; 196 lines

Path: `export/001 - Story-order-tracking/001.1 - task-ios-tracking-timeline.md`
Verified: read-back succeeded; 73 lines

Path: `export/001 - Story-order-tracking/001.2 - task-android-tracking-timeline.md`
Verified: read-back succeeded; 73 lines

Path: `export/001 - Story-order-tracking/001.3 - task-web-tracking-timeline.md`
Verified: read-back succeeded; 73 lines

Path: `export/001 - Story-order-tracking/001.4 - task-tracking-webhook.md`
Verified: read-back succeeded; 85 lines

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: `TBD...` in Estimation (a fixed Story Mode placeholder), "etc." in the ClickUp story preamble (fixed house text copied word for word), `Order page / Tracking timeline` (the design frame's own name).

**What changed**
- **Packed:** Requirements now says `Packed` comes from orders-service, which already gets it from the warehouse system. The front-end and webhook tasks repeat this, so nobody builds it again.
- **Delivery failed:** Requirements now says `Delivery failed` shows no reason, and acceptance criterion 3 checks for that. The webhook task also no longer sends `exception_code` to the order page.
- **Web layout:** all three front-end tasks now point at the `Order page / Tracking timeline` frame. The web task no longer says it waits for design.
- **Analytics:** I took it out of Requirements and the front-end tasks. It's now listed as out of scope, waiting for a later story. "A reason on `Delivery failed`" is listed as out of scope too.

**Checks:** the Story has no Open lines left. Every task links the Story and the other three tasks, and no link points to a deleted file.

**Your call:** with both open questions answered, nothing requires the Delivery section any more. I kept it because it still holds the brief's out-of-scope list, your two new exclusions and four risks. Three of those risks are my own additions: parcel-point deliveries show `Delivered` before pickup, it's unclear whether each hub scan is its own timeline step, and an old delivery window may stay on screen after a failed delivery. Tell me if you'd rather drop the section or any of those risks.