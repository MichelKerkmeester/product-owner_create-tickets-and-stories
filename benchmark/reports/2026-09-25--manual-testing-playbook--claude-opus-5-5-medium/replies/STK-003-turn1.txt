I've written the BE task for Joris. It covers the five points from Noor's summary and keeps polling only out of scope, with the reason the thread rejected it.

Path: `export/001 - task-label-webhook-fix.md`
Verified: read-back succeeded; 125 lines
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

**Quality:** all six dimensions are at or above their floors. The file has an About section, References and six numbered requirement groups. The title follows `{Discipline} - {Feature code} - {Title}` with no surface segment, because no single surface owns the back-end work: **BE - SHIP - Label webhook duplicates and missing labels**. Every number comes from the three context files: the 5-second carrier timeout, the retry schedule, 7 days, 10 and 30 minutes, more than 5 stuck shipments, 20 requests per second, €0.42 per label, and the 37 duplicates and 12 late orders.

**I added these, and none of them were in the thread's five points. Strike any you don't want:**
- **Storage failure:** if the raw event can't be stored, the handler returns a non-2xx so the carrier sends it again.
- **Repeat deliveries:** a duplicate still gets `200`, and an event whose processing fails isn't marked as processed.
- **Open shipment:** I defined it as `label_pending` or `label_ready`.
- **Concurrent failures:** two failure events for the same parcel at the same time still create at most one new shipment.
- **Labels fetched by GET:** they go through the same path as `label.created` events, including the copy to our own storage. A label isn't processed twice when it arrives by GET and by webhook.
- **Rate limit on the GET:** the 10-minute GET stays within the 20 per second limit and retries a `429` after `Retry-After`. This comes from the API notes, not the thread.
- **Alerts:** each alert includes `reference` and `shipment_id` and fires once per shipment.
- **Verification group:** a set of checks that replays the 2026-09-15 conditions in the carrier's test environment.

The task has three open questions as notes, with Joris confirming the first two with Noor before building:
1. Does a shipment still pending at the 10-minute GET get read again before the 30-minute alert?
2. Does a shipment stuck on `ADDRESS_INVALID` count toward the alert and the page?
3. For the carrier: can a `SERVICE_UNAVAILABLE` failure be followed by a `label.created` for the same shipment?