# Customer - Order tracking - Order page timeline

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
The order page on web, iOS and Android gets a per-parcel timeline from payment to delivery, with the delivery day when the carrier sends one. It covers parcels only, because the pallet carrier sends no tracking events.

#### Problem
* * *
"Where is my order" is the top reason customers contact Fernhouse: in August CS tagged `5,870` of `18,940` contacts as WISMO, `31%`. Most had a tracking number but wanted an arrival day.

The page shows `Order placed`, then `Shipped` after dispatch, and never changes, so customers lost on the carrier's site contact CS.

#### Solution
* * *
The order page replaces the carrier's site, showing an arrival day and window only when the carrier sends one.

**Expected outcomes**
* * *
*   The WISMO share of contacts drops from `31%` to under `20%` within two months of release
*   Contacts from customers confused by the timeline do not rise

#### **Tasks**
* * *
*   [BE - TRACK - Tracking webhook](<NNN.1 - task-tracking-webhook.md>)
*   [BE - TRACK - Packed status from the warehouse system](<NNN.2 - task-packed-status.md>)
*   [FE - Web - TRACK - Order page tracking timeline](<NNN.3 - task-web-tracking-timeline.md>)
*   [FE - iOS - TRACK - Order page tracking timeline](<NNN.4 - task-ios-tracking-timeline.md>)
*   [FE - Android - TRACK - Order page tracking timeline](<NNN.5 - task-android-tracking-timeline.md>)
*   [DATA - TRACK - Tracking timeline events](<NNN.6 - task-tracking-timeline-events.md>)
* * *
##   

## Requirements
* * *
**Status timeline**
* * *
**Open:** the web layout, because design mocked only the apps.

- [] It shows on the `Web`, `iOS` and `Android` order page
- [] Statuses in order: `Order placed`, `Packed`, `Shipped`, `Out for delivery`, `Delivered`, `Delivery failed`
- [] `Order placed` comes from orders-service on payment authorisation
- [] `Packed` comes from the warehouse system
- [] Carrier codes map `PU` and `IT` to `Shipped`, `OD` to `Out for delivery`, `DL` to `Delivered` and `EX` to `Delivery failed`
- [] A new `OD` after `Delivery failed` returns to `Out for delivery`
- [] Every past step shows its date and time

**Delivery failed**
* * *
**Open:** whether `Delivery failed` shows the carrier's reason. Maud from CS says yes for not home, no for reasons implying Fernhouse's fault, and Hamid settles it with CS.

- [] The `exception_code` values are `NOT_HOME`, `ADDRESS_PROBLEM`, `DAMAGED` and `REFUSED`

**Delivery estimate**
* * *
- [] An estimate shows under the current status only with an `eta_window`
- [] Per the `Order page / Tracking timeline` design frame, the day line reads `Arriving Thursday 1 October` and the window line `Between 10:00 and 14:00`
- [] No estimate is derived from the dispatch date
- [] The newest `eta_window` by `occurred_at` wins
- [] An `OD` always carries a window, and an `IT` only when the carrier can predict the day, mostly inside the Netherlands and Belgium

**Order page rules**
* * *
- [] A multi-parcel order shows one timeline per parcel, with its items
- [] Tracking events are kept `90 days` after delivery, then only the last status shows
- [] Items over `30 kg` or `120 cm` go by the pallet carrier, keeping today's page plus `The delivery company will call you to book a delivery slot`
- [] The shipping email keeps the tracking number
- [] Status text is translated into `nl-NL`, `nl-BE`, `fr-BE`, `de-DE`, `fr-FR` and `en-GB`

**Carrier tracking events**
* * *
- [] The carrier posts one `tracking.updated` event per scan to `/webhooks/carrier/tracking` on shipping-service
- [] This path is separate from the label events path, because each subscription has its own secret
- [] `X-Carrier-Signature` signs each event as the hex HMAC-SHA256 of the raw body, keyed with the tracking subscription's secret
- [] The carrier waits `5 seconds` for a 2xx, and anything else counts as failed
- [] It then makes up to `5 attempts` more, after `1 min, 5 min, 15 min, 1 h, 6 h`, then drops the event
- [] Delivery is at least once, so events are deduplicated on `event_id`
- [] A dropped event is lost, because `GET /v1/shipments/{shipment_id}` returns label fields only and the carrier plan has no tracking history
- [] About `3,100` parcels leave on a normal day, up to `5,400` on the busiest
- [] At `5` to `8` events per parcel, a peak day brings up to about `43,000`

**Event order**
* * *
- [] Events can arrive `out of order`, and an `IT` can reach shipping-service over an hour after the parcel's `OD`
- [] The timeline orders by `occurred_at`, never by arrival
- [] An event older than the parcel's newest is stored for history without changing the status
- [] After an `EX` with `NOT_HOME` the carrier retries the next working day with a new `OD`
- [] After a second `NOT_HOME` the parcel goes to a parcel point
- [] The parcel-point `DL` sets `delivered_to` to `parcel_point` at drop-off, not collection

**Analytics**
* * *
- [] Events cover timeline views and carrier link taps
- [] Each needs a Data team tracking plan row and a DATA task before any FE task sends it
- [] Names follow `object_action` in snake_case with a past-tense verb
- [] Every event carries `platform`, `app_version`, `market`, `locale` and `customer_type`
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

1\. **The order page shows where the parcel is now**
* * *
*   **Given** a customer opens a shipped order on web, iOS or Android
*   **When** the carrier scanned the parcel since their last visit
*   **Then** the timeline shows that scan's status and every earlier step with date and time
*   **And** status text is in the customer's locale
* * *
- [] _Mark as done, if the criteria are met_

2\. **A late or repeated scan never moves the status backwards**
* * *
*   **Given** an order showing `Out for delivery`
*   **When** an older in-transit scan or retried event arrives
*   **Then** the status stays `Out for delivery`
*   **And** the older scan appears once in history, at its own time
* * *
- [] _Mark as done, if the criteria are met_

3\. **The delivery estimate appears only when the carrier gives one**
* * *
*   **Given** a parcel on its way
*   **When** the carrier sent a delivery window
*   **Then** the newest day and window appear under the current status
*   **And** with no window, no estimate appears
* * *
- [] _Mark as done, if the criteria are met_

4\. **A failed delivery and the next attempt both stay visible**
* * *
*   **Given** the carrier could not deliver
*   **When** the customer opens the order
*   **Then** it shows `Delivery failed`
*   **And** a new attempt returns it to `Out for delivery`, keeping the failed attempt in the timeline
* * *
- [] _Mark as done, if the criteria are met_

5\. **Each parcel in a split order has its own timeline**
* * *
*   **Given** an order shipping in several parcels
*   **When** the customer opens it
*   **Then** each parcel has its own timeline with its items
* * *
- [] _Mark as done, if the criteria are met_

6\. **Pallet deliveries keep today's page with a booking note**
* * *
*   **Given** an order with a pallet carrier item
*   **When** the customer opens it
*   **Then** that shipment keeps today's page with the slot booking note
* * *
- [] _Mark as done, if the criteria are met_

7\. **Old deliveries show their last status**
* * *
*   **Given** an order delivered longer ago than the tracking retention period
*   **When** the customer opens it
*   **Then** the page shows the last status only
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   

## Delivery
* * *
#### Estimation
* * *
The delivery budget or expected size for the approved scope.

*   TBD...

#### Rabbit holes
* * *
Areas that could waste effort, create ambiguity or distract from the intended outcome.

*   The `Delivery failed` reason, open until Hamid settles it with CS
*   The web layout, open until design delivers it
*   A dropped `DL` leaves the order on its last status for good, with no carrier history to recover it
*   A parcel-point `DL` shows `Delivered` before collection

#### No-gos
* * *
Explicit scope exclusions and behaviors the delivery team must not introduce.

*   A push notification per status, which follows once the events are trusted
*   Changing the delivery address or day after dispatch
*   Tracking for return parcels
* * *
