# BE - TRACK - Carrier tracking webhook

## About

---

The back end receives the carrier's tracking events, stores them and maps each carrier code to the status the customer sees. The three front-end tasks show what this task stores, so they depend on it.

**Story**

---

- [Customer - Order tracking - Order page timeline](<NNN - Story-order-tracking.md>)

### Requirements

---

### **Receiving events**

---

1.  **Carrier requests**

---

The carrier posts each scan to one endpoint and retries any response other than 2xx.

**Checklist**

- [] Carrier events arrive at `/webhooks/carrier/tracking` on shipping-service
- [] Each request is checked against `X-Carrier-Signature`, the hex HMAC-SHA256 of the raw body, keyed with the tracking subscription's own secret
- [] Each request gets a 2xx response within `5 seconds`, since any other response counts as a failed delivery
- [] Events are deduplicated on `event_id`, which repeats on every retry of the same event
- [] The carrier retries a failed delivery up to `5 attempts`, waiting `1 min`, `5 min`, `15 min`, `1 h` and `6 h` before each one, then drops the event
- [] Peak days carry up to about `43,000` events, from `5,400` parcels at `5` to `8` events each

2.  **Event order and window**

---

Events arrive out of order, so the status follows scan time, not arrival.

**Checklist**

- [] Events are ordered by `occurred_at`, never by arrival
- [] An event older than the newest one held for its parcel is stored for history and does not change the status shown
- [] Where events carry different `eta_window` values, the one with the newest `occurred_at` wins
- [] A missing `eta_window` is never replaced by an estimate from the dispatch date

3.  **Status mapping**

---

Each carrier code maps to one status the customer sees.

**Checklist**

- [] `PU` and `IT` map to `Shipped`
- [] `OD` maps to `Out for delivery`
- [] `DL` with `delivered_to` set to `recipient` or `neighbour` maps to `Delivered`
- [] `EX` maps to `Delivery failed`, and `Order placed` and `Packed` are not set here

> Open in the Story: whether a `DL` with `delivered_to` set to `parcel_point` maps to `Delivered`. Leave that case unmapped until the Story settles it. Whether `ADDRESS_PROBLEM`, `DAMAGED` and `REFUSED` also bring a new `OD` is open too.

4.  **Storage and retention**

---

Tracking events outlive the delivery for a fixed period.

**Checklist**

- [] Tracking events are kept for `90 days` after delivery
- [] After that period, the order page shows the last status only

> A dropped event is gone for good, and the carrier's shipment API returns label fields only. A missed `DL` leaves the order on its last status, and no task in this Story recovers it.
