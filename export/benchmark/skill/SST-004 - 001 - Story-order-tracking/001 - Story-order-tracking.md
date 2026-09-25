# Customer - Order page - Order tracking

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
This story adds a status timeline to the order page on web, iOS and Android. The timeline moves as the parcel moves and shows the expected delivery day when the parcel carrier gives one.

### Problem
* * *
Where is my order is the largest reason customers contact Fernhouse. In August, CS tagged 5,870 of 18,940 contacts as WISMO, which is 31%. Most of those customers already had a tracking number. What they wanted to know was when the parcel would arrive, and the order page could not tell them.

Today the order page shows `Order placed` until dispatch and `Shipped` after it, with the tracking number, and it never changes after that. Customers copy the number into the parcel carrier's own site, and the ones who get lost there contact CS.

### Solution
* * *
Each parcel gets its own timeline on the order page, fed by the parcel carrier's tracking events and by the warehouse system's packed signal, so a customer can see where the parcel is and when it should arrive without leaving Fernhouse. The delivery estimate appears only when the carrier sends a window, because a guessed day that proves wrong sends the customer back to CS. Pallet items keep today's page, since the pallet carrier sends no tracking events.

#### **Expected outcomes**
* * *
*   The WISMO share of contacts drops from 31% to under 20% within two months of release
*   Contacts from customers confused by the timeline do not rise

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
*   The statuses, in order: `Order placed`, `Packed`, `Shipped`, `Out for delivery`, `Delivered`, `Delivery failed`
*   `Order placed` comes from orders-service when the payment is authorised
*   `Packed` comes from orders-service, which already receives it from the warehouse system when the order is packed
*   `Shipped` comes from parcel carrier codes `PU` (picked up) and `IT` (in transit)
*   `Out for delivery` comes from code `OD`
*   `Delivered` comes from code `DL`
*   `Delivery failed` comes from code `EX`
*   `Delivery failed` shows no reason, even when the carrier sends an `exception_code`
*   A new `OD` after `Delivery failed` moves the order back to `Out for delivery`
*   The timeline shows every step that happened, each with its date and time
*   Events are ordered by `occurred_at`, never by arrival
*   An event whose `occurred_at` is older than the newest one held for that parcel is stored for the history and does not change the status shown

**Delivery estimate**
* * *
*   The day and the window show under the current status, in the format of the `Order page / Tracking timeline` design frame: `Arriving Thursday 1 October` and `Between 10:00 and 14:00`
*   The estimate shows only when the carrier sends an `eta_window`
*   With no window, no estimate shows, and none is derived from the dispatch date
*   The newest `eta_window` by `occurred_at` wins
*   `OD` always carries a window. `IT` carries one only when the carrier can predict the day, mostly inside the Netherlands and Belgium

**Orders with several parcels**
* * *
*   One timeline per parcel, with that parcel's items under it

**Tracking retention**
* * *
*   Tracking events are kept for `90 days` after delivery, and after that the order page shows the last status only

**Pallet items**
* * *
*   Items over `30 kg` or `120 cm` go by the pallet carrier, which sends no tracking events
*   Pallet items keep today's page plus the line `The delivery company will call you to book a delivery slot`

**Shipping email**
* * *
*   The shipping email keeps the tracking number

**Platforms and locales**
* * *
*   The timeline ships on web, iOS and Android
*   The web, iOS and Android layouts follow the `Order page / Tracking timeline` design frame
*   Status text is translated for all six locales: `nl-NL`, `nl-BE`, `fr-BE`, `de-DE`, `fr-FR` and `en-GB`

**Parcel carrier tracking events**
* * *
*   One event type, `tracking.updated`, is sent for every scan of a parcel
*   The carrier posts it to `/webhooks/carrier/tracking` on shipping-service
*   The tracking path stays separate from the label event path, because the carrier signs each subscription with its own secret
*   Every request is checked against `X-Carrier-Signature`, the hex HMAC-SHA256 of the raw body, keyed with the tracking subscription's own secret
*   The carrier waits `5 seconds` for a 2xx, and anything else counts as a failed delivery
*   After a failed delivery the carrier makes up to `5 attempts` more, waiting `1 min, 5 min, 15 min, 1 h, 6 h` before each one, then drops the event
*   Delivery is at least once, so events are deduplicated on `event_id`
*   A dropped event is gone for good: `GET /v1/shipments/{shipment_id}` returns label fields only, and tracking history is not part of the carrier plan
*   `DL` carries `delivered_to`: `recipient`, `neighbour` or `parcel_point`
*   `EX` carries `exception_code`: `NOT_HOME`, `ADDRESS_PROBLEM`, `DAMAGED` or `REFUSED`
*   After an `EX` with `NOT_HOME` the carrier tries again the next working day, which sends a new `OD`
*   After a second `NOT_HOME` the parcel goes to a parcel point, and the `DL` with `parcel_point` comes when the parcel is dropped there, not when the customer collects it

**Event volume**
* * *
*   About `3,100` parcels leave on a normal working day, and up to `5,400` on the busiest days so far this year
*   Each parcel produces `5 to 8` events, so a peak day means up to about `43,000` events
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

1\. **The order page follows the parcel**
* * *
*   **Given** a customer with a dispatched parcel order on web, iOS or Android
*   **When** the parcel carrier scans the parcel
*   **Then** the order page shows the new status as current, with every earlier step and its date and time still in the timeline
* * *
- [ ] _Mark as done, if the criteria are met_

2\. **Late and repeated events never move the status backwards**
* * *
*   **Given** a parcel whose order page shows a status
*   **When** an event that happened earlier arrives late, or the carrier sends the same event again
*   **Then** the current status does not change
*   **And** the earlier step appears in the timeline once, in the order it happened
* * *
- [ ] _Mark as done, if the criteria are met_

3\. **A failed delivery and the next attempt both stay visible**
* * *
*   **Given** a parcel shown as `Delivery failed`
*   **When** the carrier sends the parcel out again
*   **Then** the order page shows `Out for delivery` as current
*   **And** the failed attempt stays in the timeline with its date and time, and without a reason
* * *
- [ ] _Mark as done, if the criteria are met_

4\. **The estimate appears only when the carrier gives one**
* * *
*   **Given** a parcel on its way
*   **When** the carrier has sent a delivery window
*   **Then** the customer sees the expected day and window under the current status, updated when the carrier changes it
*   **And** when the carrier has sent no window, the customer sees no estimate at all
* * *
- [ ] _Mark as done, if the criteria are met_

5\. **Each parcel in an order has its own timeline**
* * *
*   **Given** an order that ships in several parcels
*   **When** the customer opens the order page
*   **Then** each parcel shows its own timeline with its own items under it
* * *
- [ ] _Mark as done, if the criteria are met_

6\. **Pallet items keep today's page and say how delivery is booked**
* * *
*   **Given** an order with a pallet item
*   **When** the customer opens the order page
*   **Then** the pallet item keeps today's status display with the booking line, and shows no tracking timeline
* * *
- [ ] _Mark as done, if the criteria are met_

7\. **Old orders fall back to their last status**
* * *
*   **Given** a parcel delivered longer ago than the tracking retention period
*   **When** the customer opens the order page
*   **Then** the order page shows the last status only
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

*   A dropped or missed `DL` leaves the order on its last status, and the carrier has no way to send it again
*   A `DL` with `parcel_point` comes when the parcel is dropped at the parcel point, so `Delivered` shows before the customer has collected it
*   Every `IT` hub scan maps to `Shipped`, and the brief does not settle whether each scan is its own timeline step
*   After `Delivery failed`, the newest window can still be the one from the failed `OD`, and the brief does not say whether it stays on screen

#### No-gos
* * *
Explicit scope exclusions and behaviors the delivery team must not introduce.

*   A push notification for each status, which follows once the events have proven reliable
*   Changing the delivery address or day after dispatch
*   Tracking for return parcels
*   A reason on `Delivery failed`
*   Analytics events for the timeline being viewed and the carrier link being tapped, which wait for a later story
* * *
