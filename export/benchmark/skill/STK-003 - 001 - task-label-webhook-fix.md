# BE - SHIP - Label webhook duplicates and missing labels

## About

---

On 2026-09-15, between 14:10 and 15:50, the pack stations printed 37 duplicate labels, and 12 orders paid before the 15:00 cut-off missed the 18:00 collection and shipped a day late. The shipping-service label webhook called the warehouse system before answering, taking 6 to 9 seconds against the carrier's 5.

Scope is the five points Noor summarised in #fulfilment-eng on 2026-09-16. The thread ruled out polling only, a GET of every pending shipment, since POSTs use 14 of the shared 20 requests per second account limit near the cut-off. Joris (Backend, Fulfilment) takes this Fulfilment board task, which has no parent and must be live before the November peak.

**References**

---

- [Label webhook thread, #fulfilment-eng, 2026-09-16](../context/fernhouse-carrier-label-thread.md)
- [Parcel carrier label API, working notes](../context/fernhouse-carrier-label-api-notes.md)

Impacted

- `shipping-service`, `/webhooks/carrier/labels` for `label.created` and `label.failed`

### Requirements

---

1.  **Answer inside the carrier's 5 seconds**

---

The carrier treats a timeout, `4xx` or `5xx` as failed and retries up to 5 more times, after 1 min, 5 min, 15 min, 1 h and 6 h. On 2026-09-15, calls hitting our 8-second warehouse system timeout answered `500` and saved nothing. So the request only acknowledges, and a queue does the label work.

**Checklist**

- [] `X-Carrier-Signature` must equal the hex `HMAC-SHA256` of the raw body, checked before JSON parsing, or the answer is `401`
- [] A signed `label.created` or `label.failed` is stored raw, queued and answered `200`, calling neither the warehouse system nor the carrier
- [] The warehouse system call moves to the queue and keeps its 8-second timeout
- [] Events are answered within 5 seconds even when the warehouse system is slow or down
- [] An event that cannot be stored gets a non-`2xx`, so the carrier redelivers it
- [] The webhook secret comes from the shipping-service secrets store entry, with a separate secret for the carrier's test environment

---

2.  **Process each event once**

---

Delivery is at least once with a stable `event_id`, and the last retry comes 7 hours 21 minutes after the first, so 7 days of ids covers it.

**Checklist**

- [] An `event_id` processed in the last 7 days causes no new shipment, warehouse system call or second label copy
- [] A repeat still gets `200`, so the carrier stops retrying
- [] An event that fails, including on the 8-second warehouse system timeout, is not recorded as processed, so it is retried

---

3.  **Never open a second shipment for a parcel**

---

`POST /v1/shipments` has no idempotency key and the carrier does not dedupe on `reference`, so every repeat POST is another label billed at €0.42, printed or not, which Finance checks line by line. The carrier's planned idempotency header has no date, so the guard is ours. This gap caused all 37 duplicates.

**Checklist**

- [] After `label.failed` with `SERVICE_UNAVAILABLE`, no POST is sent if the parcel's `reference`, such as `FH-2291834-1`, has a shipment in `label_pending` or `label_ready`
- [] Two concurrent failure events for one parcel create at most one shipment

> Still open with the carrier: whether a `label.failed` with `SERVICE_UNAVAILABLE` can be followed by a `label.created` for the same shipment. Their engineer thought not and promised to check. If it can, the guard is revisited, since a re-created parcel could get two labels.

---

4.  **Fetch labels the webhook missed after 10 minutes**

---

The 12 late orders' `label.created` events failed on the first try and four retries, and the fifth comes 6 h later, so those labels landed after 21:00. `GET /v1/shipments/{shipment_id}` still returns a dropped event's label, and reading only waiting shipments stays inside the rate limit.

**Checklist**

- [] A shipment with no label 10 minutes after its POST gets `GET /v1/shipments/{shipment_id}`
- [] On a `label_ready` GET, `tracking_number` and `label_url` are handled as for `label.created`, including copying the label file to our storage
- [] Whichever of `label.created` and the GET delivers a label second changes nothing: no second label copy, new tracking number or warehouse system call
- [] GETs share the 20 requests per second limit with POSTs, and a `429` waits its `Retry-After` seconds

> The thread does not say whether a shipment still `label_pending` at the 10-minute GET is read again before the 30-minute alert. Joris confirms with Noor before building it.

---

5.  **Alert on shipments stuck without a label**

---

A label missing after 30 minutes needs a person, because an order missing the 18:00 collection ships a day late.

**Checklist**

- [] A shipment with no label 30 minutes after its POST is posted once to `#fulfilment-alerts` with its `reference` and `shipment_id`
- [] On-call is paged when more than 5 shipments are stuck at once

> The thread does not say whether a `label_failed` shipment with `ADDRESS_INVALID`, waiting on a CS agent and the customer, counts toward the alert and the page. Joris confirms with Noor before building it.

---

6.  **Done**

---

The test replays a slow afternoon like 2026-09-15 in staging, because that afternoon produced both the duplicate and the late labels this task removes.

**Checklist**

- [] The replay gives one shipment and one label per parcel
- [] In that replay, a `label.created` after the 10-minute GET took the label changes nothing
