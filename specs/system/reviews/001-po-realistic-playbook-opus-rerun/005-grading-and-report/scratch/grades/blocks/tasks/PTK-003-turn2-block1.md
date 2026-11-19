# BE - SHIP - Label webhook duplicates and late labels

### About

---

On 2026-09-15 the pack stations printed 37 duplicate labels between 14:10 and 15:50. On the same day, 12 orders paid before the `15:00` cut-off had no label when the 18:00 collection came, so they left a day late and CS sent those customers an apology. The carrier bills every label it creates at €0.42, whether or not the parcel ships.

Joris traced both problems to the label webhook handler on shipping-service. The handler called the warehouse system before answering, and because the warehouse system was slow all afternoon, each event took 6 to 9 seconds. The carrier waits `5 seconds` for a `2xx`, so it retried most events in that window and the handler did the work again on every retry. For `label.failed` with `SERVICE_UNAVAILABLE`, every retry created one more shipment, because nothing in the handler looks at `event_id`. The 12 late orders were `label.created` events that hit the handler's own 8-second timeout on the warehouse system. The handler answered `500` and saved nothing. The first try and the first four retries all fell inside the slow window, so those labels only landed with the fifth retry, 6 h after the fourth, after 21:00.

After this task, the webhook answers inside the carrier's timeout and does the work for each event once. Any label the webhook still misses is caught before it costs a collection. The carrier has no idempotency key on `POST /v1/shipments` and does not dedupe on `reference`, so every guard against a second label has to live in shipping-service. The carrier's engineer said an idempotency header is planned but could not give a date. This work has to be live before the November peak.

Polling only is out of scope. The thread rejected it because of the carrier's rate limit of `20 requests per second`, which every POST and GET on the account shares. Around the cut-off, POSTs take up to 14 of those requests per second, so polling several hundred pending labels would make labels arrive later in the busiest hour.

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

The carrier treats a timeout, a `4xx` and a `5xx` as a failed delivery. It then retries up to 5 more times over 7 hours 21 minutes and drops the event after the last retry fails. If the webhook answers fast, a slow dependency can no longer turn one event into several. Because the event is stored before the answer, an answered event is never lost. The warehouse system call itself stays as it is and only moves out of the request.

**Checklist**

- [ ] `/webhooks/carrier/labels` checks `X-Carrier-Signature`, the hex `HMAC-SHA256` of the raw body keyed with the webhook secret, against the raw bytes before parsing the JSON, and answers `401` on a mismatch
- [ ] A valid event is stored raw and answered with `200` within `5 seconds`
- [ ] The request does nothing beyond the signature check and storing the event. The warehouse system call, shipment creation and the label copy all run from the queue
- [ ] Both `label.created` and `label.failed` are processed from the queue after the `200`
- [ ] The warehouse system call keeps its 8-second timeout
- [ ] While the warehouse system is slow, including calls that reach the 8-second timeout, the webhook still answers inside `5 seconds`
- [ ] A queued event whose processing fails, including a warehouse system call that times out, stays queued and is retried, because the carrier never resends an event that got a `2xx`

2.  **Do each event's work once, keyed on `event_id`**

---

Delivery is at least once, and every retry of an event carries the same `event_id`, so `event_id` is the key that tells a retry apart from a new event. Processed ids are kept for `7 days`, which is well past the carrier's last retry 7 hours 21 minutes after the first try.

**Checklist**

- [ ] Every processed `event_id` is kept for `7 days`
- [ ] An event whose `event_id` was already processed still gets a `200` and does not create a shipment or copy a label a second time
- [ ] Two deliveries of the same `event_id` that arrive before the first has finished processing still result in the work being done once
- [ ] A `label.failed` with `SERVICE_UNAVAILABLE` delivered 6 times (the first try plus 5 retries) creates exactly one new shipment

3.  **Never open a second shipment for a parcel**

---

The carrier builds and bills a label for every shipment created, and it has no idempotency key, so a second shipment for the same parcel is a second charge. The `event_id` check stops repeats of a single event. This guard covers every other path that would create a new shipment for a parcel that already has one.

**Checklist**

- [ ] Before it creates a shipment again after a `label.failed` with `SERVICE_UNAVAILABLE`, shipping-service checks that the parcel's `reference`, such as `FH-2291834-1`, has no other open shipment
- [ ] When the parcel already has an open shipment, no new shipment is created
- [ ] A parcel never has more than one shipment in `label_pending` or `label_ready` at the same time

> Still open with the carrier: whether a `label.failed` with `SERVICE_UNAVAILABLE` can be followed by a `label.created` for the same shipment. Their engineer thought not and promised to check.

### **Stragglers and alerting**

---

4.  **Fetch a missing label after 10 minutes**

---

A label usually arrives by webhook within a minute, so a shipment with no label after 10 minutes has lost or delayed its event. `GET /v1/shipments/{shipment_id}` still returns the label even after the carrier has dropped the event. The GET only touches these stragglers, so its share of the `20 requests per second` stays small.

**Checklist**

- [ ] A shipment with no label `10 minutes` after its `POST /v1/shipments` gets a `GET /v1/shipments/{shipment_id}`
- [ ] When the GET returns `label_ready`, shipping-service takes `tracking_number` and `label_url` from the response and copies the label file into its own storage, the same way it does for a `label.created` event
- [ ] Shipments that already have a label are never fetched
- [ ] A `429` from the carrier delays the GET by the number of seconds in `Retry-After` and does not drop it

5.  **Alert on shipments still without a label after 30 minutes**

---

A shipment with no label after 30 minutes needs a person before the 18:00 collection. On 2026-09-15 the 12 missing labels only landed after 21:00, hours after the collection had gone.

**Checklist**

- [ ] A shipment with no label `30 minutes` after its POST posts to `#fulfilment-alerts`
- [ ] Each stuck shipment posts once, not on every check
- [ ] On-call is paged when more than 5 shipments are stuck at once
- [ ] Exactly 5 stuck shipments post to the channel but do not page on-call

### **Definition of done**

---

6.  **Replay a slow afternoon in staging**

---

The task is done when staging reproduces the conditions of 2026-09-15 without any of that day's results. In the replay, the warehouse system answers in 6 to 9 seconds and the carrier retries the events the webhook doesn't answer in time.

**Checklist**

- [ ] Replaying a slow afternoon in staging gives exactly one shipment and one label per parcel
- [ ] A `label.created` that lands after the 10-minute GET has already taken the label changes nothing: no new shipment, no second label copy and no change to the stored `tracking_number` or label
