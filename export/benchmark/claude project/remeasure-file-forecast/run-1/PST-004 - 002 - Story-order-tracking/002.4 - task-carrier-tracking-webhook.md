# BE - TRACK - Carrier tracking webhook and status mapping

### About

---

The parcel carrier sends a `tracking.updated` event for every scan of a parcel. This task receives and stores those events and maps carrier codes to the statuses customers see, so the order page on web, iOS and Android can show a timeline for each parcel. orders-service already receives `Packed` from the warehouse system, so no work is needed there. Yusuf's notes on the carrier's tracking events guide (version 2.4) and the 2026-09-19 call with the carrier are the source for the rules below.

**Story**

---

- [Customer - Order tracking - Order page timeline](<002 - Story-order-tracking.md>)

**Related tasks**

---

- [FE - iOS - TRACK - Order page tracking timeline](<002.1 - task-ios-order-tracking-timeline.md>)
- [FE - Android - TRACK - Order page tracking timeline](<002.2 - task-android-order-tracking-timeline.md>)
- [FE - Web - TRACK - Order page tracking timeline](<002.3 - task-web-order-tracking-timeline.md>)

### Requirements

---

1.  **Receive tracking events**

---

A dropped event is gone for good, because `GET /v1/shipments/{shipment_id}` returns label fields only. The webhook has to accept every real event the first time it can.

**Checklist**

- [ ] The carrier posts `tracking.updated` to `/webhooks/carrier/tracking` on shipping-service, separate from the label webhook path
- [ ] Every event is checked against `X-Carrier-Signature`, the hex HMAC-SHA256 of the raw body, keyed with the tracking subscription's own secret
- [ ] An event whose signature does not match changes no parcel
- [ ] The webhook answers with a 2xx within `5 seconds`
- [ ] Events are deduplicated on `event_id`, which stays the same on every retry
- [ ] The webhook handles peak days of up to 5,400 parcels at 5 to 8 events each, about 43,000 events

2.  **Map carrier codes to statuses**

---

The carrier's codes become the statuses customers see on the order page.

**Checklist**

- [ ] `PU` and `IT` map to `Shipped`
- [ ] `OD` maps to `Out for delivery`
- [ ] `DL` maps to `Delivered`
- [ ] `EX` maps to `Delivery failed`
- [ ] A new `OD` after `EX` moves the parcel back to `Out for delivery`
- [ ] The order page can read each parcel's steps with their date and time, its current status and its newest `eta_window`, alongside `Order placed` and `Packed` from orders-service

3.  **Event order**

---

Hub scans upload in batches and retries arrive late by design, so events arrive out of order. On busy days an `IT` can arrive more than an hour after the `OD` for the same parcel.

**Checklist**

- [ ] Events are ordered by `occurred_at`, never by arrival
- [ ] An event with an `occurred_at` older than the newest event held for that parcel is stored for the history and does not change the current status
- [ ] The newest `eta_window` by `occurred_at` wins

4.  **Retention**

---

Tracking history is only needed for as long as customers are likely to look at it.

**Checklist**

- [ ] Tracking events are kept for `90 days` after delivery
- [ ] After `90 days` the parcel keeps its last status only
