# BE - SHIP - Label webhook handling under slow downstream calls

### About

---

On 2026-09-15 the label webhook handler on shipping-service took 6 to 9 seconds per event, because it called the warehouse system before answering and the warehouse system was slow all afternoon. The parcel carrier waits `5 seconds` for a `2xx`, so it retried most events. Each retry of a `label.failed` with `SERVICE_UNAVAILABLE` created one more shipment, which gave `37 duplicate labels` at `€0.42` each. The carrier bills every label it creates. Separately, `12 orders` paid before the `15:00` cut-off missed the 18:00 collection. The handler hit its 8-second warehouse timeout, answered `500` and saved nothing, and the carrier's fifth retry landed after 21:00.

This task keeps the webhook and makes it safe under a slow warehouse system. The handler answers inside the carrier's timeout and does the work from a queue. It ignores repeated events and never opens a second shipment for a parcel. A 10-minute GET collects stragglers, and alerts fire when labels stay missing. The result is one shipment and one label per parcel, and labels in time for the collection.

Owner: Joris. Board: Fulfilment. No parent task. It has to be live before the November peak.

Polling only is out of scope. The thread rejected it because the account's `20 requests per second` limit is shared with the POSTs, which reach up to 14 a second around the cut-off.

**References**

---

- `fernhouse-carrier-label-api-notes.md` (carrier label API notes, Joris, 2026-09-11)
- `fernhouse-carrier-label-thread.md` (#fulfilment-eng thread and Noor's summary, 2026-09-16)
- `fernhouse-context.md` (ticket conventions)

### Requirements

---

1.  **Answer inside the carrier's timeout and work from a queue**

---

Nothing slow runs inside the webhook request. The handler checks the signature, stores the raw event, answers and hands the event to a queue. The warehouse system call moves to the queue worker and keeps its 8-second timeout. A slow or timed-out warehouse call can then no longer make the carrier retry or lose an event.

**Checklist**

- [ ] `/webhooks/carrier/labels` answers `200` within the carrier's `5 seconds` for both `label.created` and `label.failed`, whatever the warehouse system's response time
- [ ] `X-Carrier-Signature` is checked as hex `HMAC-SHA256` of the raw request body before the JSON is parsed, and a mismatch answers `401`
- [ ] The raw event is stored before the `200` is sent
- [ ] The warehouse system is called only from the queue worker, with the timeout still at `8 seconds`
- [ ] A warehouse call that times out or fails leaves the stored event available to process again, so no label is lost
- [ ] The label file is copied into our own storage when the event is processed, so pack stations never depend on the carrier's `label_url`, which expires after `24 hours`

---

2.  **Dedupe on event_id**

---

Delivery is at least once, and `event_id` stays the same on every retry of an event. A repeated event must never repeat the work.

**Checklist**

- [ ] An event whose `event_id` was already processed is answered `200` and does nothing else
- [ ] Processed `event_id` values are kept for `7 days`, well past the carrier's last retry at 7 hours 21 minutes

---

3.  **Guard against a second open shipment for a parcel**

---

`POST /v1/shipments` has no idempotency key and the carrier does not dedupe on `reference`, so a second POST for a parcel creates a second billed label. The guard has to be ours.

**Checklist**

- [ ] Before a shipment is created again after a `label.failed` with `SERVICE_UNAVAILABLE`, shipping-service checks that the parcel, by `reference` such as `FH-2291834-1`, has no other open shipment
- [ ] A shipment in `label_pending` or `label_ready` counts as open, and the re-create is skipped when one exists
- [ ] Handling of `ADDRESS_INVALID` and `OTHER` stays as it is today

> Open with the carrier: can a `label.failed` with `SERVICE_UNAVAILABLE` be followed by a `label.created` for the same shipment? Their engineer thought not and promised to check. If it can, a re-created shipment would still produce a second label, so the answer decides whether this guard is enough.

---

4.  **GET after 10 minutes for stragglers**

---

A dropped or delayed event must not leave a parcel without a label. `GET /v1/shipments/{shipment_id}` still returns the label after the carrier drops an event.

**Checklist**

- [ ] A shipment with no label `10 minutes` after its POST gets one `GET /v1/shipments/{shipment_id}`
- [ ] When the GET returns `label_ready`, the label is taken from `label_url` and stored the same way as a label from `label.created`
- [ ] A `label.created` that arrives after the GET already took the label changes nothing: no second stored label, no second print and no warehouse call
- [ ] The GETs stay inside the shared `20 requests per second` account limit, and a `429` waits for the `Retry-After` seconds before trying again

> Not decided yet: what happens when the 10-minute GET returns `label_failed`. Settle this with Noor before this group is built.

---

5.  **Alerting on missing labels**

---

A label still missing after the GET needs a person, before the collection is missed.

**Checklist**

- [ ] A shipment with no label `30 minutes` after its POST posts to `#fulfilment-alerts`
- [ ] On-call gets paged when `more than 5` shipments are in that state at once

---

6.  **Staging replay**

---

Done means the 2026-09-15 afternoon cannot happen again. The replay runs in staging against the carrier's test environment, which signs with its own test secret.

**Checklist**

- [ ] Replaying a slow afternoon in staging, with the warehouse system answering in 6 to 9 seconds and the carrier retrying events, gives one shipment and one label per parcel
- [ ] In the same replay, a `label.created` that lands after the 10-minute GET already took the label changes nothing
