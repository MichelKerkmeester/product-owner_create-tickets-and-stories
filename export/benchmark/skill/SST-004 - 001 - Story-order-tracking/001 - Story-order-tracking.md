# Customer - Order page - Order tracking

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
A status timeline on the web, iOS and Android order page follows the parcel and shows the delivery day when the parcel carrier gives one.

### Problem
* * *
Where is my order is the top reason to contact Fernhouse: 5,870 of 18,940 August contacts, 31%, most already holding a tracking number and wanting an arrival day.

The order page shows `Order placed` until dispatch, then `Shipped` with the tracking number, and stops. Customers copy the number into the parcel carrier's own site, and those who get lost there contact CS.

### Solution
* * *
Each parcel gets a timeline from carrier tracking events and the warehouse packed signal. The estimate needs a carrier window, because a wrong guessed day sends the customer back to CS.

#### **Expected outcomes**
* * *
*   WISMO share drops from 31% to under 20% within two months of release
*   Timeline confusion contacts do not rise

#### **Tasks**
* * *
*   [FE - iOS - TRACK - Tracking timeline and delivery estimate](<001.1 - task-ios-tracking-timeline.md>)
*   [FE - Android - TRACK - Tracking timeline and delivery estimate](<001.2 - task-android-tracking-timeline.md>)
*   [FE - Web - TRACK - Tracking timeline and delivery estimate](<001.3 - task-web-tracking-timeline.md>)
*   [BE - TRACK - Tracking webhook and status mapping](<001.4 - task-tracking-webhook.md>)
##   

## Requirements
* * *
**Status timeline**
* * *
*   Statuses in order: `Order placed`, `Packed`, `Shipped`, `Out for delivery`, `Delivered`, `Delivery failed`
*   `Order placed` comes from orders-service on payment authorisation, `Packed` from orders-service via the warehouse system
*   `Shipped` comes from carrier codes `PU` (picked up) and `IT` (in transit)
*   `Out for delivery` comes from `OD`, `Delivered` from `DL` and `Delivery failed` from `EX`
*   `Delivery failed` shows no reason, even with an `exception_code`
*   A new `OD` after `Delivery failed` returns to `Out for delivery`
*   Every past step shows its date and time
*   Events are ordered by `occurred_at`, never by arrival
*   An event older than the parcel's newest `occurred_at` is stored but does not change the status

**Delivery estimate**
* * *
*   Day and window sit under the current status per the `Order page / Tracking timeline` design frame: `Arriving Thursday 1 October` and `Between 10:00 and 14:00`
*   The estimate needs an `eta_window`, never derived from dispatch date
*   The newest `eta_window` by `occurred_at` wins
*   `OD` always carries a window
*   `IT` carries one only when the day is predictable, mostly within the Netherlands and Belgium

**Orders with several parcels**
* * *
*   One timeline per parcel, with that parcel's items under it

**Tracking retention**
* * *
*   Events are kept `90 days` after delivery, then only the last status shows

**Pallet items**
* * *
*   Items over `30 kg` or `120 cm` go by the pallet carrier, which has no tracking events, so they keep today's page
*   Pallet items add the line `The delivery company will call you to book a delivery slot`

**Shipping email**
* * *
*   It keeps the tracking number

**Platforms and locales**
* * *
*   Web, iOS and Android follow the `Order page / Tracking timeline` design frame
*   Status text is translated for six locales: `nl-NL`, `nl-BE`, `fr-BE`, `de-DE`, `fr-FR` and `en-GB`

**Parcel carrier tracking events**
* * *
*   One `tracking.updated` per parcel scan, posted to `/webhooks/carrier/tracking` on shipping-service
*   The path stays separate from the label path, because each subscription has its own secret
*   Requests are checked against `X-Carrier-Signature`, the hex HMAC-SHA256 of the raw body keyed with the tracking secret
*   The carrier waits `5 seconds` for a 2xx, else counts a failed delivery
*   It retries up to `5 attempts` more after `1 min, 5 min, 15 min, 1 h, 6 h`, then drops the event
*   At-least-once delivery, so events are deduplicated on `event_id`
*   Dropped events are lost, as `GET /v1/shipments/{shipment_id}` returns label fields only and tracking history is not in the carrier plan
*   `DL` carries `delivered_to`: `recipient`, `neighbour` or `parcel_point`
*   `EX` carries `exception_code`: `NOT_HOME`, `ADDRESS_PROBLEM`, `DAMAGED` or `REFUSED`
*   After an `EX` with `NOT_HOME` the carrier retries next working day with a new `OD`
*   After a second `NOT_HOME` the parcel goes to a parcel point
*   A `DL` with `parcel_point` comes at drop-off, not collection

**Event volume**
* * *
*   About `3,100` parcels leave on a normal day, up to `5,400` on this year's busiest
*   At `5 to 8` events each, a peak day means up to about `43,000`
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

1\. **The order page follows the parcel**
* * *
*   **Given** a dispatched parcel order on web, iOS or Android
*   **When** the carrier scans the parcel
*   **Then** the new status is current, with every earlier step dated and timed
* * *
- [ ] _Mark as done, if the criteria are met_

2\. **Late and repeated events never move the status backwards**
* * *
*   **Given** a parcel showing a status
*   **When** an earlier event arrives late or is resent
*   **Then** the current status does not change
*   **And** the earlier step appears once, in order
* * *
- [ ] _Mark as done, if the criteria are met_

3\. **A failed delivery and the next attempt both stay visible**
* * *
*   **Given** a parcel shown as `Delivery failed`
*   **When** the carrier sends it out again
*   **Then** `Out for delivery` shows as current
*   **And** the failed attempt stays with its date and time, without a reason
* * *
- [ ] _Mark as done, if the criteria are met_

4\. **The estimate appears only when the carrier gives one**
* * *
*   **Given** a parcel on its way
*   **When** the carrier has sent a delivery window
*   **Then** the day and window show under the current status, updating with the carrier
*   **And** with no window, no estimate shows
* * *
- [ ] _Mark as done, if the criteria are met_

5\. **Each parcel in an order has its own timeline**
* * *
*   **Given** an order in several parcels
*   **When** the order page opens
*   **Then** each parcel has its own timeline and items
* * *
- [ ] _Mark as done, if the criteria are met_

6\. **Pallet items keep today's page and say how delivery is booked**
* * *
*   **Given** an order with a pallet item
*   **When** the order page opens
*   **Then** the pallet item keeps today's status display with the booking line, and shows no tracking timeline
* * *
- [ ] _Mark as done, if the criteria are met_

7\. **Old orders fall back to their last status**
* * *
*   **Given** a parcel delivered longer ago than the retention period
*   **When** the order page opens
*   **Then** only the last status shows
* * *
- [ ] _Mark as done, if the criteria are met_
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

*   A dropped or missed `DL` leaves the last status, and the carrier cannot resend it
*   A `DL` with `parcel_point` means `Delivered` shows before the customer collects
*   Every `IT` hub scan maps to `Shipped`, and the brief leaves open whether each is its own step
*   After `Delivery failed`, the newest window can be the failed `OD`'s, and the brief does not say whether it stays

#### No-gos
* * *
Explicit scope exclusions and behaviors the delivery team must not introduce.

*   A push notification per status, following once events prove reliable
*   Changing the delivery address or day after dispatch
*   Tracking for return parcels
*   A reason on `Delivery failed`
*   Analytics for timeline views and carrier link taps, waiting for a later story
* * *
