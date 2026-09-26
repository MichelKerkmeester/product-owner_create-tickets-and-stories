# BE - SHIP - Label webhook queue, dedupe and straggler recovery

### About

---

On 2026-09-15 the pack stations printed 37 duplicate labels between 14:10 and 15:50, and 12 orders paid before the 15:00 cut-off missed the 18:00 collection and went out a day late. The carrier bills every label at €0.42, printed or not, and CS had to apologise to the 12 customers.

Both failures come from the label webhook handler in shipping-service. It calls the warehouse system before answering, and that afternoon the calls took 6 to 9 seconds. The carrier waits 5 seconds for a `2xx`, then treats the delivery as failed and retries. Nothing in the handler looks at `event_id`, so every retry of a `label.failed` with `SERVICE_UNAVAILABLE` created one more shipment, and one more billed label. Events whose warehouse call hit our own 8-second timeout got a `500` and were not saved. Their fifth and last retry comes 6 hours after the fourth, so those labels landed after 21:00.

This task makes the webhook answer inside the carrier's timeout, process each event once, keep one open shipment per parcel and recover labels the webhook did not deliver. It has to be live before the November peak.

Polling only is out of scope. The thread rejected it because the 20 requests per second limit is shared with the POSTs, which reach 14 a second around the cut-off, so labels would arrive later in the busiest hour.

**References**

---

- `#fulfilment-eng label webhook thread, exported by Noor on 2026-09-16`
- `Parcel carrier label API working notes, Joris, 2026-09-11 (carrier integration guide v3.2)`

### Requirements

---

### **Webhook**

---

1.  **Answer inside the carrier's 5 seconds**

---

The carrier counts a timeout, a `4xx` and a `5xx` as a failed delivery and retries, so nothing slow may run inside the request. The work moves to a queue, and an event is stored before it is acknowledged so a slow warehouse system can no longer lose it.

**Checklist**

- [ ] `X-Carrier-Signature` is checked against the raw request body before the JSON is parsed, and a mismatch gets `401`
- [ ] A signed event is stored as received and answered with `200` within 5 seconds
- [ ] The warehouse system call and any shipment creation run from the queue, never inside the request
- [ ] The warehouse system call keeps its 8-second timeout
- [ ] An event whose warehouse call times out stays stored and is not lost

2.  **Process each event once**

---

Delivery is at least once and `event_id` stays the same on every retry of an event, so it is the key that stops a retry from doing the work again.

**Checklist**

- [ ] An event whose `event_id` was already processed is answered with `2xx` and does no work
- [ ] Processed `event_id` values are kept for 7 days, well past the carrier's last retry at 7 hours 21 minutes

### **Shipments**

---

3.  **One open shipment per parcel**

---

The carrier has no idempotency key on `POST /v1/shipments` and does not dedupe on `reference`, so every second shipment for a parcel is a second billed label. The guard has to be ours.

**Checklist**

- [ ] No shipment is created for a parcel that already has an open shipment, including the re-create after a `label.failed` with `SERVICE_UNAVAILABLE`
- [ ] A shipment in `label_pending` or `label_ready` counts as open
- [ ] The carrier's answer on whether a `label.created` can follow a `SERVICE_UNAVAILABLE` for the same shipment is recorded on this task before release

4.  **Recover labels the webhook did not deliver**

---

A dropped or late label event does not lose the label, because `GET /v1/shipments/{shipment_id}` still returns it. Reading only the stragglers keeps these calls well inside the shared rate limit.

**Checklist**

- [ ] A shipment with no label 10 minutes after its POST gets one `GET /v1/shipments/{shipment_id}`
- [ ] When the GET returns `label_ready`, the label is taken from it and copied into our own storage, the same way a webhook label is
- [ ] A `label.created` that arrives after the GET already took the label changes nothing on the shipment or the stored label
- [ ] These GETs stay inside the 20 requests per second shared with the POSTs, and a `429` is retried after its `Retry-After`

### **Alerting**

---

5.  **Stuck labels reach a person**

---

A label that arrives too late makes an order miss the 18:00 collection, as the 12 late orders on 2026-09-15 did, so a stuck label has to reach someone while there is still time to act.

**Checklist**

- [ ] A shipment with no label 30 minutes after its POST posts to `#fulfilment-alerts`
- [ ] On-call is paged when more than 5 shipments are in that state at once

### **Done**

---

6.  **Staging replay of a slow afternoon**

---

The fix is done when the failure of 2026-09-15 can no longer happen in staging.

**Checklist**

- [ ] Replaying a slow afternoon in staging, with warehouse system calls taking 6 to 9 seconds, gives one shipment and one label per parcel
- [ ] In the same replay, a `label.created` that lands after the 10-minute GET already took the label changes nothing
