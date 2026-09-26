I've written the task. It's saved and I read it back to confirm the save worked.

Path: `export/002 - task-label-webhook-fix.md`
Verified: read-back succeeded; 113 lines
HVR self-scan: 0 hard blockers. Fixed: two claims the sources don't support ("the same slow afternoon would cost far more orders" and a guessed cause for several stuck labels at once), replaced with the 12 late orders from 2026-09-15. Kept with reason: none.

It has six requirement groups: answer inside the carrier's 5 seconds, handle each `event_id` once, one open shipment per parcel, the 10-minute GET for late labels, alerting, and your staging replay as the definition of done. The warehouse call keeps its 8-second timeout and only moves out of the request. Polling only is listed as out of scope, with the rate-limit reason. It meets the quality bar I check against, and every requirement comes from the thread, the API notes or your reply.

**Additions I made that you didn't ask for (strike any you don't want):**
- An event whose warehouse call times out stays stored and isn't lost. This follows from "store the raw event", but I wrote it as its own check.
- A repeat of an `event_id` that was already handled gets a `2xx` reply. The carrier retries on any `4xx`, so without this the retries would keep coming.
- Open means `label_pending` or `label_ready`. The guard covers every shipment creation for a parcel, not only the re-create after a failure. I went with the wider reading because your "one shipment per parcel" needs it.
- A label picked up by the 10-minute GET is copied into our own storage, the same way a webhook label is.
- The GETs stay within the 20 requests per second limit and wait out a `429` using its `Retry-After`.
- The carrier's answer on whether a `label.created` can follow a `SERVICE_UNAVAILABLE` is recorded on the task before release.

**Left out on purpose:**
- **Other failure codes:** handling for `ADDRESS_INVALID` and `OTHER` doesn't change.
- **Alert details:** the task doesn't say what goes in a `#fulfilment-alerts` post or which on-call rotation gets paged.
- **Peak deadline:** the task says "before the November peak" with no date, because none was given.

I can also create it on the Fulfilment board in ClickUp, with no parent, if you'd like. I'll only do that once you say so.