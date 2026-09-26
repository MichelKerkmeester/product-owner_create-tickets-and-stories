# BE - TRACK - Tracking webhook

### About

---

The order page timeline on web, iOS and Android depends on the parcel carrier's tracking events. This task receives and stores those events and maps each carrier code to the status the customer sees.

The carrier sends each event by webhook, can deliver events in any order and drops an event for good after its last retry. Tracking history cannot be fetched again later, so a missed `DL` leaves the order on its last status. The endpoint's reliability decides whether a customer ever sees `Delivered`.

**Story**

---

- [Customer - Order page - Order tracking](<002 - Story-order-tracking.md>)

**Related tasks**

---

- [FE - iOS - TRACK - Tracking timeline on the order page](<002.1 - task-ios-tracking-timeline.md>)
- [FE - Android - TRACK - Tracking timeline on the order page](<002.2 - task-android-tracking-timeline.md>)
- [FE - Web - TRACK - Tracking timeline on the order page](<002.3 - task-web-tracking-timeline.md>)

### Requirements

---

1.  **Receiving events**

---

Every `tracking.updated` event the carrier sends is accepted once and only once, even on the busiest days.

**Checklist**

- [ ] Events are received at `/webhooks/carrier/tracking` on shipping-service, on a path separate from the label events
- [ ] Each request is verified against `X-Carrier-Signature`, the hex HMAC-SHA256 of the raw body keyed with the tracking subscription's own secret
- [ ] The endpoint answers with a 2xx within `5 seconds`
- [ ] A retried event is recognised by its `event_id` and stored once
- [ ] The endpoint handles up to about `43,000` events on a peak day, from up to `5,400` parcels at 5 to 8 events each

> The carrier counts anything other than a 2xx within 5 seconds as a failed delivery. It makes up to `5 attempts` more, waiting `1 min, 5 min, 15 min, 1 h, 6 h`, then drops the event. `GET /v1/shipments/{shipment_id}` returns label fields only, so a dropped event cannot be recovered.

2.  **Status mapping**

---

Each carrier code becomes one status the order page shows.

**Checklist**

- [ ] `PU` and `IT` map to `Shipped`
- [ ] `OD` maps to `Out for delivery`
- [ ] `DL` maps to `Delivered`
- [ ] `EX` maps to `Delivery failed`, and no failure reason reaches the order page
- [ ] A new `OD` after an `EX` moves the parcel back to `Out for delivery`
- [ ] `Order placed` and `Packed` still come from orders-service, which already receives `Packed` from the warehouse system

3.  **Event order and delivery estimate**

---

Events can arrive out of order. On busy days an `IT` can reach us more than an hour after the `OD` for the same parcel, and retried events arrive late by design. The status shown has to follow the time of the scan.

**Checklist**

- [ ] Events are ordered by `occurred_at`, never by arrival
- [ ] An event older than the newest one held for that parcel is stored for the history and does not change the status shown
- [ ] The newest `eta_window` by `occurred_at` becomes the delivery estimate
- [ ] A parcel with no `eta_window` has no estimate

> An `OD` always carries an `eta_window`. An `IT` carries one only when the carrier can predict the day, which is mostly inside the Netherlands and Belgium.

4.  **Retention**

---

**Checklist**

- [ ] Tracking events are kept for `90 days` after delivery, and after that only the last status is kept for the order page
- [ ] Pallet shipments have no tracking events, because the pallet carrier sends none
