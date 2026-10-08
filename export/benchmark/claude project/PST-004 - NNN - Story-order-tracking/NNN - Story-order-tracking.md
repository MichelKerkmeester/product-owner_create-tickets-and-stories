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
