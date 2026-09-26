# BE - SHIP - Label webhook duplicates and late labels

## About

---

On 2026-09-15 the pack stations printed 37 duplicate labels between 14:10 and 15:50, and 12 orders paid before the `15:00` cut-off missed the 18:00 collection, leaving a day late with a CS apology. The carrier bills every label at €0.42, shipped or not.

The shipping-service label webhook called the warehouse system, slow all afternoon, before answering, taking 6 to 9 seconds against the carrier's `5 seconds` wait for a `2xx`. Each retry redid the work, and a `label.failed` with `SERVICE_UNAVAILABLE` made another shipment, because nothing checks `event_id`.

The 12 late orders' `label.created` events hit the handler's 8-second warehouse timeout, got `500` and saved nothing until the fifth retry, 6 h after the fourth, after 21:00.

The carrier has no idempotency key on `POST /v1/shipments` and no dedupe on `reference`, so every guard lives in shipping-service. The carrier's engineer said an idempotency header is planned but gave no date. This work must be live before the November peak.

The thread ruled polling only out of scope, because every POST and GET shares the carrier's `20 requests per second` limit, with POSTs at up to 14 around the cut-off.

**References**

---

- `#fulfilment-eng label webhook thread, exported by Noor on 2026-09-16`
- `Parcel carrier label API working notes, Joris, 2026-09-11`
- `Parcel carrier integration guide for labels, version 3.2`

### Requirements

---

### **Webhook handling**

---

1.  **Answer inside the carrier's 5 seconds and work from a queue**

---

The carrier treats a timeout, `4xx` or `5xx` as failed, retries up to 5 more times over 7 hours 21 minutes, then drops the event. Storing before answering means an answered event is never lost.

**Checklist**

- [] `/webhooks/carrier/labels` checks `X-Carrier-Signature`, the hex `HMAC-SHA256` of the raw body keyed with the webhook secret
- [] It checks raw bytes before JSON parsing, and a mismatch gets `401`
- [] A valid event is stored raw and gets `200` within `5 seconds`
- [] The warehouse call, shipment creation and label copy run from the queue, not the request
- [] `label.created` and `label.failed` both process from the queue after the `200`
- [] The warehouse call keeps its 8-second timeout
- [] While the warehouse system is slow, even to the 8-second timeout, the webhook still answers inside `5 seconds`
- [] A failed queued event, including a warehouse timeout, stays queued for retry, because the carrier never resends after a `2xx`

2.  **Do each event's work once, keyed on `event_id`**

---

Delivery is at least once and retries share an `event_id`, so it marks repeats, and `7 days` outlasts every retry.

**Checklist**

- [] Every processed `event_id` is kept `7 days`
- [] A repeat `event_id` still gets `200` but no second shipment or label copy
- [] Two concurrent deliveries of one `event_id` still do the work once
- [] A `label.failed` with `SERVICE_UNAVAILABLE` delivered 6 times, first try plus 5 retries, creates exactly one new shipment

3.  **Never open a second shipment for a parcel**

---

A second shipment is a second billed label, so this guard covers every path the `event_id` check misses.

**Checklist**

- [] Before re-creating a shipment after a `label.failed` with `SERVICE_UNAVAILABLE`, shipping-service creates none if the parcel's `reference`, such as `FH-2291834-1`, has another open shipment
- [] A parcel never has two shipments in `label_pending` or `label_ready` at once

> Still open with the carrier: whether a `label.failed` with `SERVICE_UNAVAILABLE` can be followed by a `label.created` for the same shipment. Their engineer thought not and promised to check.

### **Stragglers and alerting**

---

4.  **Fetch a missing label after 10 minutes**

---

Labels usually arrive within a minute, so one missing at 10 minutes has a lost or delayed event. `GET /v1/shipments/{shipment_id}` returns it even after the carrier drops the event, and fetching only stragglers keeps its share of the `20 requests per second` small.

**Checklist**

- [] A shipment with no label `10 minutes` after its `POST /v1/shipments` gets a `GET /v1/shipments/{shipment_id}`
- [] On `label_ready`, shipping-service stores `tracking_number` and `label_url` and copies the label file into its own storage, as for `label.created`
- [] Shipments with a label are never fetched
- [] A `429` delays the GET by `Retry-After` seconds, never dropping it

5.  **Alert on shipments still without a label after 30 minutes**

---

A shipment unlabeled at 30 minutes needs a person before the 18:00 collection.

**Checklist**

- [] A shipment with no label `30 minutes` after its POST posts to `#fulfilment-alerts`
- [] Each stuck shipment posts once, not per check
- [] More than 5 stuck at once pages on-call
- [] Exactly 5 stuck shipments post without paging on-call

### **Definition of done**

---

6.  **Replay a slow afternoon in staging**

---

The task is done when staging reproduces 2026-09-15 without that day's results: the warehouse system answers in 6 to 9 seconds and the carrier retries unanswered events.

**Checklist**

- [] The staging replay gives exactly one shipment and one label per parcel
- [] A `label.created` after the 10-minute GET took the label changes nothing: no new shipment, label copy or change to the stored `tracking_number` or label
