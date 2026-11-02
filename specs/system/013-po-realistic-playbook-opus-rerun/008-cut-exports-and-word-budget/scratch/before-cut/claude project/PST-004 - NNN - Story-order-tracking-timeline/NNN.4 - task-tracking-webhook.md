# BE - TRACK - Tracking webhook

### About

---

shipping-service receives the parcel carrier's `tracking.updated` events, stores them and maps each carrier code to the status the customer sees. Every timeline on the order page depends on this task. A tracking event the carrier drops after its last retry cannot be recovered, so the endpoint has to answer reliably at peak volume.

**Story**

---

- [Customer - Order tracking - Order page timeline](<NNN - Story-order-tracking-timeline.md>)

**Related tasks**

---

- [FE - iOS - TRACK - Order page tracking timeline](<NNN.1 - task-ios-tracking-timeline.md>)
- [FE - Android - TRACK - Order page tracking timeline](<NNN.2 - task-android-tracking-timeline.md>)
- [FE - Web - TRACK - Order page tracking timeline](<NNN.3 - task-web-tracking-timeline.md>)

### Requirements

---

1.  **Receive and verify events**

---

The carrier signs the tracking subscription with its own secret and treats a slow answer as a failure. After five failed retries, the event is gone for good.

**Checklist**

- [ ] Events arrive at `/webhooks/carrier/tracking` on shipping-service, separate from the label events path
- [ ] Each event is verified against `X-Carrier-Signature`, the hex HMAC-SHA256 of the raw body keyed with the tracking subscription's secret
- [ ] A valid event gets a 2xx within `5 seconds`
- [ ] The endpoint keeps within that time at up to about `43,000` events on a peak day

---

2.  **Deduplicate and order events**

---

Delivery is at least once and events can arrive out of order. An `IT` can arrive more than an hour after the `OD`, and a retried event always arrives late.

**Checklist**

- [ ] Events are deduplicated on `event_id`
- [ ] Events are ordered by `occurred_at`, never by arrival
- [ ] An event older than the newest one held for that parcel is stored for the history and does not change the status shown
- [ ] The newest `eta_window` by `occurred_at` wins
- [ ] Each event is stored with its `eta_window`, `exception_code`, `delivered_to` and `location` when present

---

3.  **Map carrier codes to customer statuses**

---

**Checklist**

- [ ] `PU` and `IT` map to `Shipped`
- [ ] `OD` maps to `Out for delivery`
- [ ] `DL` maps to `Delivered`
- [ ] `EX` maps to `Delivery failed`
- [ ] A new `OD` after an `EX` moves the parcel back to `Out for delivery`

---

4.  **Retention**

---

**Checklist**

- [ ] Tracking events are kept for `90 days` after delivery, after which only the last status remains available to the order page
