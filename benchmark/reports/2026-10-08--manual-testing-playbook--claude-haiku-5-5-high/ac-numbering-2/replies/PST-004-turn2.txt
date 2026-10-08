```markdown
# Customer - Order tracking - Order page timeline

* * *
## Problem
* * *
In August, 5,870 of 18,940 contacts (31%) were tagged WISMO, the helpdesk tag for where-is-my-order questions, which is the biggest reason customers contact us. Most of those customers already had a tracking number and wanted to know when the parcel would arrive, which the order page could not tell them. Today the order page on web and in the apps shows `Order placed` until dispatch and `Shipped` after it, and it never changes after that. Customers copy the tracking number into the carrier's own site, and the ones who get lost there contact us.
* * *
##   

## Solution
* * *
Show a status timeline on the order page on web, iOS and Android, so customers see where each parcel is without leaving the page. The timeline moves as the carrier reports scans, in the order they happened. Where the carrier gives a delivery window, the current status shows its day and window, and where it gives none, no estimate shows.

**Expected outcomes**
* * *
*   A customer sees where each parcel is on the order page, without copying the tracking number into the carrier's site
*   The timeline moves as the parcel moves, with each step's date and time
*   A customer whose delivery failed sees that status on the order page
*   The WISMO share of contacts drops from 31% to under 20% within two months, with no rise in contacts from customers confused by the timeline

#### **Tasks**
* * *
*   [FE - iOS - TRACK - Order page timeline](<NNN.1 - task-ios-order-timeline.md>)
*   [FE - Android - TRACK - Order page timeline](<NNN.2 - task-android-order-timeline.md>)
*   [FE - Web - TRACK - Order page timeline](<NNN.3 - task-web-order-timeline.md>)
*   [BE - TRACK - Carrier tracking webhook](<NNN.4 - task-carrier-tracking-webhook.md>)
* * *
##   

## Requirements
* * *
**Status steps**
* * *
- [] The six statuses appear in this order: `Order placed`, `Packed`, `Shipped`, `Out for delivery`, `Delivered` and `Delivery failed`
- [] `Order placed` comes from orders-service when payment is authorised, and `Packed` comes from the warehouse system, which orders-service already receives
- [] `Shipped` comes from carrier codes `PU` and `IT`, `Out for delivery` from `OD`, `Delivered` from `DL` and `Delivery failed` from `EX`
- [] Each step shows its date and time

**Delivered at a parcel point**
* * *
**Open:** Whether a `DL` with `delivered_to` set to `parcel_point` shows `Delivered`. The parcel is dropped there and not collected, and the carrier's five status codes include no collection event. Product settles it.

- [] A `DL` with `delivered_to` set to `recipient` or `neighbour` shows `Delivered`

**Delivery failed**
* * *
- [] `Delivery failed` shows no carrier reason in this story

**Retry after a failed delivery**
* * *
**Open:** Whether `ADDRESS_PROBLEM`, `DAMAGED` and `REFUSED` also bring a new `OD`. The carrier's notes name a retry only after `NOT_HOME`, and the carrier's integration team settles it.

- [] After `NOT_HOME`, a new `OD` moves the order back to `Out for delivery`

**Delivery estimate**
* * *
- [] When the carrier sends a window, the current status shows its day and window on two lines, as the design mock shows: `Arriving Thursday 1 October` and then `Between 10:00 and 14:00`
- [] When the carrier sends no window, no estimate shows, and the dispatch date never sets one

**Parcels and pallet items**
* * *
- [] Each parcel in an order has its own timeline, with that parcel's items under it
- [] An item that goes by the pallet carrier keeps today's page, with the line `The delivery company will call you to book a delivery slot`

**Carrier events**
* * *
- [] Carrier events arrive at `/webhooks/carrier/tracking` on shipping-service
- [] Each request is checked against `X-Carrier-Signature`, the hex HMAC-SHA256 of the raw body, keyed with the tracking subscription's own secret
- [] Each request gets a 2xx response within `5 seconds`, since any other response counts as a failed delivery
- [] Events are deduplicated on `event_id`, since the carrier delivers at least once
- [] Events are ordered by `occurred_at`, never by arrival, and an event older than the newest held for its parcel does not change the status shown
- [] Where events carry different `eta_window` values, the newest by `occurred_at` wins
- [] Peak days carry up to about `43,000` events, from `5,400` parcels at `5` to `8` events each

**Retention**
* * *
- [] Tracking events are kept for `90 days` after delivery, and after that the order page shows the last status only

**Shipping email**
* * *
- [] The shipping email keeps the tracking number

**Translation**
* * *
- [] Status text is translated for all six locales: `nl-NL`, `nl-BE`, `fr-BE`, `de-DE`, `fr-FR` and `en-GB`
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

#### Timeline
* * *
1 ) **The order page shows every step the parcel has taken**
* * *
*   **Given** a parcel that has been picked up and is in transit
*   **When** the customer opens the order page on web or in the apps
*   **Then** the timeline lists every step that happened, each with its date and time
*   **And** the current status is the newest step the carrier has reported
* * *
- [] _Mark as done, if the criteria are met_

2 ) **The timeline moves as the parcel moves**
* * *
*   **Given** a parcel that is in transit
*   **When** the carrier reports that the parcel is out for delivery
*   **Then** the current status moves to the out for delivery step
*   **And** the earlier steps stay on the timeline with their dates and times
* * *
- [] _Mark as done, if the criteria are met_

3 ) **A late scan never moves the status back**
* * *
*   **Given** a parcel whose newest step is out for delivery
*   **When** an older scan of the same parcel arrives after it
*   **Then** the older scan appears in the timeline at its own point in time
*   **And** the current status does not change
* * *
- [] _Mark as done, if the criteria are met_

4 ) **A failed delivery shows the failure and the retry that follows**
* * *
*   **Given** a parcel whose delivery failed because the customer was not home
*   **When** the customer opens the order page
*   **Then** the failed delivery step shows, with no carrier reason
*   **And** a new out for delivery step returns the current status to out for delivery
* * *
- [] _Mark as done, if the criteria are met_

#### Estimate and parcels
* * *
5 ) **The estimate follows the carrier's window**
* * *
*   **Given** a parcel with a current status
*   **When** the customer opens the order page
*   **Then** the day and window show under the current status when the carrier has sent a window
*   **And** no estimate shows when the carrier has sent none
* * *
- [] _Mark as done, if the criteria are met_

6 ) **Each parcel in an order has its own timeline**
* * *
*   **Given** an order whose items travel in more than one parcel
*   **When** the customer opens the order page
*   **Then** each parcel shows its own timeline, with that parcel's items under it
*   **And** an item that goes by the pallet carrier keeps today's page
* * *
- [] _Mark as done, if the criteria are met_

7 ) **Old tracking history reduces to the last status**
* * *
*   **Given** a delivered parcel whose retention period has passed
*   **When** the customer opens the order page
*   **Then** the order page shows only the last status
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   

## Delivery
* * *
#### Estimation
* * *
*   TBD...

#### Rabbit holes
* * *
*   Whether `ADDRESS_PROBLEM`, `DAMAGED` and `REFUSED` also bring a new `OD` stays open until the carrier confirms it, as Requirements states
*   Whether a `DL` at a `parcel_point` shows `Delivered` stays open until Product settles it, as Requirements states
*   Polling the carrier's shipment API to recover a missed `DL`, since that API returns label fields only and no tracking history

#### No-gos
* * *
*   A push notification for each status, which comes after the events are trusted
*   Changing the delivery address or day after dispatch
*   Tracking for return parcels
*   A carrier reason on `Delivery failed` in this story
*   Tracking events for the timeline view and the carrier link tap, which wait for a later story
* * *
```

Export-equivalent path: export/NNN - Story-order-tracking/NNN - Story-order-tracking.md

```markdown
# FE - iOS - TRACK - Order page timeline

## About

---

The iOS app's order page shows a status timeline for each parcel, with that parcel's items under it and the delivery estimate under the current status. Customers see where a parcel is without copying its tracking number into the carrier's site.

The timeline shows the events that the BE tracking webhook task stores, so this task depends on that task.

**References**

---

Page

- `Order page / Tracking timeline` frame

**Story**

---

- [Customer - Order tracking - Order page timeline](<NNN - Story-order-tracking.md>)

### Requirements

---

### **Timeline and status**

---

1.  **Steps and current status**

---

The order page lists every step the parcel has taken, in the order the scans happened.

**Checklist**

- [] Each step shows its date and time
- [] The current status reads `Order placed`, `Packed`, `Shipped`, `Out for delivery`, `Delivered` or `Delivery failed`
- [] Each parcel of an order has its own timeline, with that parcel's items under it
- [] A scan that arrives late appears at its own point in time and does not change the current status

2.  **Delivery estimate**

---

When the carrier sends a delivery window, the estimate sits under the current status.

**Checklist**

- [] The estimate shows the day and the window on two lines, as the design mock shows: `Arriving Thursday 1 October` and then `Between 10:00 and 14:00`
- [] No estimate shows when the carrier sends no window, and the dispatch date never sets one

3.  **Failed delivery**

---

A failed delivery shows its own status, and a new out for delivery step can follow it.

**Checklist**

- [] `Delivery failed` shows no carrier reason
- [] After a `NOT_HOME` failure, a new `OD` moves the status back to `Out for delivery`

4.  **Pallet items, copy and retention**

---

Items that go by the pallet carrier have no tracking events, so they keep today's page.

**Checklist**

- [] An item that goes by the pallet carrier keeps today's page, with the line `The delivery company will call you to book a delivery slot`
- [] Status text is translated for all six locales: `nl-NL`, `nl-BE`, `fr-BE`, `de-DE`, `fr-FR` and `en-GB`
- [] Once `90 days` have passed since delivery, the order page shows the last status only
```

Export-equivalent path: export/NNN - Story-order-tracking/NNN.1 - task-ios-order-timeline.md

```markdown
# FE - Android - TRACK - Order page timeline

## About

---

The Android app's order page shows a status timeline for each parcel, with that parcel's items under it and the delivery estimate under the current status. Customers see where a parcel is without copying its tracking number into the carrier's site.

The timeline shows the events that the BE tracking webhook task stores, so this task depends on that task.

**References**

---

Page

- `Order page / Tracking timeline` frame

**Story**

---

- [Customer - Order tracking - Order page timeline](<NNN - Story-order-tracking.md>)

### Requirements

---

### **Timeline and status**

---

1.  **Steps and current status**

---

The order page lists every step the parcel has taken, in the order the scans happened.

**Checklist**

- [] Each step shows its date and time
- [] The current status reads `Order placed`, `Packed`, `Shipped`, `Out for delivery`, `Delivered` or `Delivery failed`
- [] Each parcel of an order has its own timeline, with that parcel's items under it
- [] A scan that arrives late appears at its own point in time and does not change the current status

2.  **Delivery estimate**

---

When the carrier sends a delivery window, the estimate sits under the current status.

**Checklist**

- [] The estimate shows the day and the window on two lines, as the design mock shows: `Arriving Thursday 1 October` and then `Between 10:00 and 14:00`
- [] No estimate shows when the carrier sends no window, and the dispatch date never sets one

3.  **Failed delivery**

---

A failed delivery shows its own status, and a new out for delivery step can follow it.

**Checklist**

- [] `Delivery failed` shows no carrier reason
- [] After a `NOT_HOME` failure, a new `OD` moves the status back to `Out for delivery`

4.  **Pallet items, copy and retention**

---

Items that go by the pallet carrier have no tracking events, so they keep today's page.

**Checklist**

- [] An item that goes by the pallet carrier keeps today's page, with the line `The delivery company will call you to book a delivery slot`
- [] Status text is translated for all six locales: `nl-NL`, `nl-BE`, `fr-BE`, `de-DE`, `fr-FR` and `en-GB`
- [] Once `90 days` have passed since delivery, the order page shows the last status only
```

Export-equivalent path: export/NNN - Story-order-tracking/NNN.2 - task-android-order-timeline.md

```markdown
# FE - Web - TRACK - Order page timeline

## About

---

The web order page shows a status timeline for each parcel, with that parcel's items under it and the delivery estimate under the current status. Customers see where a parcel is without copying its tracking number into the carrier's site. Web is one responsive build for desktop and mobile browsers, so the timeline holds at both widths.

The timeline shows the events that the BE tracking webhook task stores, so this task depends on that task.

**References**

---

Page

- `Order page / Tracking timeline` frame

**Story**

---

- [Customer - Order tracking - Order page timeline](<NNN - Story-order-tracking.md>)

### Requirements

---

### **Timeline and status**

---

1.  **Steps and current status**

---

The order page lists every step the parcel has taken, in the order the scans happened.

**Checklist**

- [] Each step shows its date and time
- [] The current status reads `Order placed`, `Packed`, `Shipped`, `Out for delivery`, `Delivered` or `Delivery failed`
- [] Each parcel of an order has its own timeline, with that parcel's items under it
- [] A scan that arrives late appears at its own point in time and does not change the current status

2.  **Delivery estimate**

---

When the carrier sends a delivery window, the estimate sits under the current status.

**Checklist**

- [] The estimate shows the day and the window on two lines, as the design mock shows: `Arriving Thursday 1 October` and then `Between 10:00 and 14:00`
- [] No estimate shows when the carrier sends no window, and the dispatch date never sets one

3.  **Failed delivery**

---

A failed delivery shows its own status, and a new out for delivery step can follow it.

**Checklist**

- [] `Delivery failed` shows no carrier reason
- [] After a `NOT_HOME` failure, a new `OD` moves the status back to `Out for delivery`

4.  **Pallet items, copy and retention**

---

Items that go by the pallet carrier have no tracking events, so they keep today's page.

**Checklist**

- [] An item that goes by the pallet carrier keeps today's page, with the line `The delivery company will call you to book a delivery slot`
- [] Status text is translated for all six locales: `nl-NL`, `nl-BE`, `fr-BE`, `de-DE`, `fr-FR` and `en-GB`
- [] Once `90 days` have passed since delivery, the order page shows the last status only
```

Export-equivalent path: export/NNN - Story-order-tracking/NNN.3 - task-web-order-timeline.md

```markdown
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
```

Export-equivalent path: export/NNN - Story-order-tracking/NNN.4 - task-carrier-tracking-webhook.md

Artifact kind: Story, with four tasks in the order you named them. The Story keeps two Open lines: whether a parcel-point drop shows `Delivered`, and whether a retry follows `ADDRESS_PROBLEM`, `DAMAGED` or `REFUSED`. Those Open lines force the Delivery section, where Estimation stays `TBD...`.

Two settling parties are my pointers, not sourced decisions, so strike either one you do not want: Product for the parcel-point question, and the carrier's integration team for the retry question.

Not covered, and not added:

- No task serves the timeline data from the backend to web and the apps. You named four tasks, so I did not add a read task.
- The owner team for the webhook is still open. It lands on shipping-service, which Fulfilment owns.
- The sources do not say whether guests can open an order page, since guests get order emails but no order history.
- The sources do not say which timezone the delivery window uses.

Quality status: checked against the Story and Task templates for house grammar, heading depth and checkbox form. Two Open lines remain by design. The NNN numbers are reconciled when you save outside the Project.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: `TBD...`, the Story Mode Delivery placeholder.