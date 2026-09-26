I've written Joris's task: **BE - SHIP - Label webhook handling under slow downstream calls**. It covers the five points from the thread, and your two "done" conditions make up the final staging replay group.

Path: `export/002 - task-label-webhook-fix.md`
Verified: read-back succeeded; 113 lines
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

**Quality summary:** Every section the task needs is there. Carrier values are copied exactly from the API notes: the `5 seconds` timeout, the `HMAC-SHA256` signature check and the `20 requests per second` limit. The thread's numbers are also exact: `7 days`, `10 minutes`, `30 minutes` and `more than 5`. The About section explains the cost of the 2026-09-15 incident. The 8-second timeout on the warehouse system call stays, and that call moves out of the webhook request into the queue.

**Things I added that none of the sources say. Strike any you don't want:**
- **Open shipment:** a shipment in `label_pending` or `label_ready` counts as open for the duplicate guard.
- **Other failure codes:** handling for `ADDRESS_INVALID` and `OTHER` stays as it is today.
- **Rate limit:** the 10-minute GETs stay within the shared rate limit and wait out the `Retry-After` time on a `429`.
- **Failed warehouse calls:** if the call times out or fails, the stored event stays available to process again.
- **Late `label.created`:** "changes nothing" is spelled out as no second stored label, no second print and no warehouse call.
- **Label copy:** a label fetched by the GET is stored the same way as one from the webhook.
- **Test environment:** the staging replay runs against the carrier's test environment.
- **Title:** I used the title I suggested earlier, since you didn't change it.

**Still open, marked as notes in the task:**
- **Unanswered carrier question:** can a `SERVICE_UNAVAILABLE` failure be followed by a `label.created` for the same shipment? The answer decides whether the guard is enough on its own.
- **GET finds a failed label:** there's no decision yet on what happens when the 10-minute GET returns `label_failed`. I pointed this to Noor.

The task has no link to the "label webhook ticket" Noor mentioned. Send me the link if it exists and I'll add it.