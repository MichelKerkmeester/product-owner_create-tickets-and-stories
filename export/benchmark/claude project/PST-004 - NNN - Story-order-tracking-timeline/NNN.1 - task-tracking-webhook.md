# BE - TRACK - Tracking webhook

## About

---

shipping-service receives, stores and maps the carrier's `tracking.updated` events to customer statuses for every order page timeline. The carrier drops an event for good after its last retry, so the endpoint must answer reliably at peak.

**Story**

---

- [Customer - Order tracking - Order page timeline](<NNN - Story-order-tracking-timeline.md>)

**Related tasks**

---

- [BE - TRACK - Packed status from the warehouse system](<NNN.2 - task-packed-status.md>)
- [FE - Web - TRACK - Order page tracking timeline](<NNN.3 - task-web-tracking-timeline.md>)
- [FE - iOS - TRACK - Order page tracking timeline](<NNN.4 - task-ios-tracking-timeline.md>)
- [FE - Android - TRACK - Order page tracking timeline](<NNN.5 - task-android-tracking-timeline.md>)

### Requirements

---

1.  **Receive and verify events**

---

The tracking subscription has its own secret, and a slow answer counts as failed.

**Checklist**

- [] Events arrive at `/webhooks/carrier/tracking` on shipping-service, separate from the label events path
- [] Each event is verified against `X-Carrier-Signature`, the hex HMAC-SHA256 of the raw body keyed with the tracking subscription's secret
- [] A valid event gets a 2xx within `5 seconds`
- [] It holds that time at up to about `43,000` events on a peak day

---

2.  **Deduplicate and order events**

---

Delivery is at least once and out of order: an `IT` can trail the `OD` by over an hour, and retries always arrive late.

**Checklist**

- [] Events are deduplicated on `event_id`
- [] Events are ordered by `occurred_at`, never by arrival
- [] An event older than the parcel's newest is stored for history without changing the status
- [] The newest `eta_window` by `occurred_at` wins
- [] Each event is stored with its `eta_window`, `exception_code`, `delivered_to` and `location` when present

---

3.  **Map carrier codes to customer statuses**

---

**Checklist**

- [] `PU` and `IT` map to `Shipped`
- [] `OD` maps to `Out for delivery`
- [] `DL` maps to `Delivered`
- [] `EX` maps to `Delivery failed`
- [] A new `OD` after an `EX` returns the parcel to `Out for delivery`

---

4.  **Retention**

---

**Checklist**

- [] Tracking events are kept `90 days` after delivery, then only the last status stays for the order page
