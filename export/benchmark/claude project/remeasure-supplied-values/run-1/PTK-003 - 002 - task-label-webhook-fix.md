# BE - SHIP - Label webhook retries and duplicate labels

### About

---

On 2026-09-15, between 14:05 and 15:50, the label webhook handler on shipping-service took 6 to 9 seconds per event. It called the warehouse system before answering, and the warehouse system was slow all afternoon. The carrier stops waiting after `5 seconds` and retries, so most events arrived more than once and were processed every time. Each retry of a `label.failed` with `SERVICE_UNAVAILABLE` created one more shipment, which produced `37 duplicate labels` at `€0.42` each. Calls that hit our own `8-second` timeout on the warehouse system answered `500` and saved nothing. As a result, `12 orders` paid before the `15:00` cut-off had no label at the 18:00 collection and went out a day late.

The carrier bills every label it creates and has no idempotency key on `POST /v1/shipments`. It doesn't dedupe on `reference` either, so any protection against a second label has to be ours. The carrier retries a failed delivery at most 5 times over 7 hours 21 minutes and then drops the event. An event we fail to accept can therefore arrive hours late or not at all. This task keeps the webhook, accepts every event inside the carrier's timeout, makes a repeated event harmless and catches the labels that still don't arrive. It has to be live before the November peak.

Polling only is out of scope. The thread `rejected` it because of the rate limit: the account gets `20 requests per second` across POST and GET, and around the cut-off the POSTs alone reach 14 a second.

**References**

---

- `#fulfilment-eng label webhook thread, 2026-09-16`
- `Parcel carrier label API working notes, 2026-09-11`

### Requirements

---

### **Webhook intake**

---

1.  **Answer inside the carrier's timeout and work from a queue**

---

The request accepts the event and does nothing slow. Everything else, including the warehouse system call, runs from a queue. A slow warehouse system can then delay a label but can no longer make the carrier see a failed delivery.

**Checklist**

- [ ] `X-Carrier-Signature` (the hex `HMAC-SHA256` of the raw body, keyed with the webhook secret) is checked against the raw bytes before the JSON is parsed
- [ ] A request whose signature does not match gets `401`
- [ ] A signed `label.created` or `label.failed` event is stored raw and answered with `200` inside the carrier's `5 seconds`
- [ ] No warehouse system call and no carrier API call happens inside the request
- [ ] Stored events are processed from a queue
- [ ] The warehouse system call keeps its `8-second` timeout and is now made from the queue
- [ ] A slow or failing warehouse system never turns into a `5xx` or a timeout for the carrier

---

2.  **Dedupe on `event_id`**

---

The carrier sends the same `event_id` on every retry of an event, so `event_id` is the key that makes a repeat safe.

**Checklist**

- [ ] An event whose `event_id` was already processed changes nothing, for both `label.created` and `label.failed`
- [ ] Processed ids are kept for `7 days`, well past the carrier's last retry at 7 hours 21 minutes

---

### **Shipments and labels**

---

3.  **Guard against a second open shipment for a parcel**

---

A `label.failed` with `SERVICE_UNAVAILABLE` asks us to create the shipment again. Every new shipment is a billed label, so a new one is created only when the parcel has no other open shipment.

**Checklist**

- [ ] Before creating a shipment again after a `SERVICE_UNAVAILABLE` failure, shipping-service checks whether the parcel has another open shipment
- [ ] When the parcel already has an open shipment, no new `POST /v1/shipments` is sent

> The carrier has not yet confirmed whether a `label.failed` with `SERVICE_UNAVAILABLE` can be followed by a `label.created` for the same shipment. Their engineer thought not and promised to check.

---

4.  **Fetch stragglers with a GET after 10 minutes**

---

A label event can be delayed or dropped, and `GET /v1/shipments/{shipment_id}` still returns the label. The GET shares the `20 requests per second` limit with the POSTs, so it only touches shipments that are still missing a label.

**Checklist**

- [ ] A shipment with no label `10 minutes` after the POST gets a `GET /v1/shipments/{shipment_id}`
- [ ] When the GET returns `label_ready`, the label is taken from the GET response
- [ ] A label taken from the GET is copied into our own storage, the same way a webhook label is, so the pack stations print it from our copy

---

5.  **Alert on shipments that still have no label**

---

**Checklist**

- [ ] A shipment with no label after `30 minutes` posts to `#fulfilment-alerts`
- [ ] On-call gets paged when `more than 5` shipments are in that state at once

---

### **Done**

---

6.  **Replay a slow afternoon in staging**

---

The replay recreates 2026-09-15: the warehouse system is slow, and the carrier retries `label.created` and `label.failed` events, including `SERVICE_UNAVAILABLE` failures.

**Checklist**

- [ ] The replay ends with one shipment and one label per parcel
- [ ] A `label.created` that lands after the 10-minute GET already took the label changes nothing
