# BE - SHIP - Label webhook duplicates and missing labels

### About

---

On 2026-09-15, between 14:10 and 15:50, the pack stations printed 37 duplicate labels, and 12 orders paid before the 15:00 cut-off had no label when the 18:00 collection came, so they shipped a day late.

The label webhook handler in shipping-service called the warehouse system before answering and took 6 to 9 seconds per event, while the carrier waits 5 seconds. Every retry repeated the work: each retry of a `label.failed` with `SERVICE_UNAVAILABLE` created one more billed shipment. Calls that hit our own 8-second warehouse system timeout answered `500` and saved nothing.

Scope is the five points Noor summarised in #fulfilment-eng on 2026-09-16: answer inside the carrier's timeout, process each event once, never open a second shipment for a parcel, pick up labels the webhook missed and alert before a missing label costs a collection. Each carrier label costs €0.42, printed or not, and Finance checks the invoice line by line.

Polling only, meaning a GET of every pending shipment in place of the webhook, is out of scope. The thread rejected it because the 20 requests per second account limit is shared with the POSTs, which reach 14 a second around the cut-off.

Joris (Backend, Fulfilment) takes this task, which sits on the Fulfilment board with no parent task and has to be live before the November peak.

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

The carrier counts a timeout, a `4xx` and a `5xx` as a failed delivery and retries up to 5 more times, after 1 min, 5 min, 15 min, 1 h and 6 h.

The request path therefore does only what the carrier needs to stop retrying, and all label work runs from a queue, so a slow warehouse system can no longer turn one event into several.

**Checklist**

- [ ] `X-Carrier-Signature` is checked as the hex `HMAC-SHA256` of the raw request body before the JSON is parsed, and a mismatch is answered with `401`
- [ ] A signed event is stored raw, queued and answered with `200`, with no call to the warehouse system or the carrier inside the request
- [ ] Both `label.created` and `label.failed` take this path
- [ ] The warehouse system call moves out of the request into the queued work and keeps its 8-second timeout
- [ ] Events are answered within 5 seconds while the warehouse system is slow or unavailable
- [ ] An event that cannot be stored is answered with a non-`2xx`, so the carrier delivers it again rather than it being lost
- [ ] The webhook secret is read from the secrets store under the shipping-service entry, and the carrier's test environment uses its separate test secret

---

2.  **Process each event once**

---

Delivery is at least once, and `event_id` stays the same on every retry of an event. The last retry arrives 7 hours 21 minutes after the first try, so keeping processed ids for 7 days covers every retry with a wide margin.

**Checklist**

- [ ] An event whose `event_id` was already processed causes no further work: no new shipment, no warehouse system call and no second copy of the label
- [ ] Processed `event_id` values are kept for 7 days
- [ ] A repeat delivery of an already processed event is still answered with `200`, so the carrier stops retrying it
- [ ] An event whose processing fails, including on the 8-second warehouse system timeout, is not recorded as processed, so it is retried rather than dropped

---

3.  **Never open a second shipment for a parcel**

---

`POST /v1/shipments` has no idempotency key and the carrier does not dedupe on `reference`, so every repeat POST is a second billed label. The carrier has an idempotency header planned with no date, which is why this guard has to be ours. On 2026-09-15 this gap produced all 37 duplicates.

**Checklist**

- [ ] Before a shipment is created again after `label.failed` with `SERVICE_UNAVAILABLE`, shipping-service checks that the parcel (its `reference`, such as `FH-2291834-1`) has no other open shipment
- [ ] An open shipment is one in `label_pending` or `label_ready`
- [ ] When the parcel already has an open shipment, no POST is sent
- [ ] Two failure events for the same parcel processed at the same time still lead to at most one new shipment

> Still open with the carrier: whether a `label.failed` with `SERVICE_UNAVAILABLE` can be followed by a `label.created` for the same shipment. Their engineer thought not and promised to check. If it can, a re-created parcel could still end up with two labels, so the guard is revisited once the carrier answers.

---

4.  **Fetch labels the webhook missed after 10 minutes**

---

The 12 late orders on 2026-09-15 had `label.created` events that failed on the first try and the first four retries. The fifth retry comes 6 h after the fourth, so those labels landed after 21:00.

A dropped event does not lose the label, since `GET /v1/shipments/{shipment_id}` still returns it, so reading the stragglers recovers them long before the collection. This touches only shipments still waiting, which keeps it inside the rate limit that ruled out polling only.

**Checklist**

- [ ] A shipment with no label 10 minutes after its POST gets `GET /v1/shipments/{shipment_id}`
- [ ] When the GET returns `label_ready`, `tracking_number` and `label_url` are handled exactly as for a `label.created` event, including copying the label file to our own storage
- [ ] A `label.created` arriving after the 10-minute GET already took the label changes nothing: no second label copy, new tracking number or warehouse system call
- [ ] A label already taken from a `label.created` event is not processed again when a GET for the same shipment returns it
- [ ] GETs share the 20 requests per second account limit with the POSTs, and a `429` is retried after the seconds in its `Retry-After` header

> The thread does not say whether a shipment still `label_pending` at the 10-minute GET is read again before the 30-minute alert. Joris confirms this with Noor before building it.

---

5.  **Alert on shipments stuck without a label**

---

A label that is still missing after 30 minutes needs a person, because the pack stations already wait on labels at 15:00 and an order that misses the 18:00 collection ships a day late.

**Checklist**

- [ ] A shipment with no label 30 minutes after its POST posts to `#fulfilment-alerts` with its `reference` and `shipment_id`
- [ ] Each stuck shipment is posted once, not on every check
- [ ] On-call is paged when more than 5 shipments are in that state at once

> The thread does not say whether a shipment in `label_failed` with `ADDRESS_INVALID`, which waits on a CS agent and the customer, counts toward the alert and the page. Joris confirms this with Noor before building it.

---

6.  **Done**

---

The test is a replay in staging of a slow afternoon like 2026-09-15, because that afternoon produced both the duplicate labels and the late labels this task removes.

**Checklist**

- [ ] Replaying a slow afternoon in staging gives one shipment and one label per parcel
- [ ] In that replay, a `label.created` that lands after the 10-minute GET already took the label changes nothing
