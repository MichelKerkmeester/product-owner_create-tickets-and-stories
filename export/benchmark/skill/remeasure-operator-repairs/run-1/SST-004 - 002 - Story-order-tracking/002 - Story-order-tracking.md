# Customer - Order page - Order tracking

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
This story adds a status timeline to the order page on web, iOS and Android. The timeline moves as the parcel moves and shows the expected delivery day when the parcel carrier sends one. It covers parcels only, and pallet items keep today's page.

It leaves out a push notification per status, changing the delivery address or day after dispatch, tracking for return parcels and analytics events for the timeline. The analytics events come in a later story. `Packed` needs no work here, because orders-service already receives it from the warehouse system.

### Problem
* * *
Where is my order is the biggest reason customers contact us. In August CS tagged 5,870 of 18,940 contacts as WISMO, which is 31%. Most of those customers already had a tracking number. What they wanted to know was when the parcel would arrive.

The order page shows `Order placed` until dispatch and `Shipped` after it, with the tracking number, and never changes after that. Customers copy the number into the parcel carrier's own site, and the ones who get lost there contact us.

### Solution
* * *
The order page follows each parcel through the carrier's scans, so a customer can see where the parcel is and when it arrives without leaving Fernhouse. The expected day comes from the carrier only and is never guessed from the dispatch date, so the page never shows a day the carrier has not given.

#### **Expected outcomes**
* * *
*   The WISMO share of contacts drops from `31%` to under `20%` within two months of release
*   Contacts from customers confused by the timeline do not rise

#### **Tasks**
* * *
*   [FE - iOS - TRACK - Order tracking timeline](<002.1 - task-fe-ios-order-tracking-timeline.md>)
*   [FE - Android - TRACK - Order tracking timeline](<002.2 - task-fe-android-order-tracking-timeline.md>)
*   [FE - Web - TRACK - Order tracking timeline](<002.3 - task-fe-web-order-tracking-timeline.md>)
*   [BE - TRACK - Tracking webhook](<002.4 - task-be-tracking-webhook.md>)
##   

## Requirements
* * *
**Status timeline**
* * *
*   Statuses run in this order: `Order placed`, `Packed`, `Shipped`, `Out for delivery`, `Delivered`, `Delivery failed`
*   `Order placed` comes from orders-service when the payment is authorised
*   `Packed` comes from the warehouse system, which orders-service already receives
*   `Shipped` comes from parcel carrier codes `PU` and `IT`
*   `Out for delivery` comes from `OD`
*   `Delivered` comes from `DL`
*   `Delivery failed` comes from `EX` and shows no reason in this story
*   A new `OD` after `Delivery failed` moves the parcel back to `Out for delivery`
*   The timeline shows every step that happened, each with its date and time
*   Carrier codes are mapped to statuses in the tracking webhook task, never in the clients
*   The layout on web, iOS and Android follows the `Order page / Tracking timeline` frame

**Delivery estimate**
* * *
*   When the carrier sends an `eta_window`, the day and the window show under the current status, as `Arriving Thursday 1 October` and `Between 10:00 and 14:00` in the design mock
*   With no `eta_window`, no estimate shows, and none is worked out from the dispatch date
*   The newest `eta_window` by `occurred_at` wins
*   `OD` always carries an `eta_window`, and `IT` carries one only when the carrier can predict the day, mostly inside the Netherlands and Belgium

**Orders with several parcels**
* * *
*   The order page shows one timeline per parcel, with that parcel's items under it

**Tracking history**
* * *
*   Tracking events are kept for `90 days` after delivery
*   After those `90 days` the order page shows the last status only

**Pallet items**
* * *
*   Items over `30 kg` or `120 cm` go by the pallet carrier, which sends no tracking events
*   Pallet items keep today's page plus the line `The delivery company will call you to book a delivery slot`

**Shipping email**
* * *
*   The shipping email keeps the tracking number

**Translations**
* * *
*   Status text is translated for all six locales: `nl-NL`, `nl-BE`, `fr-BE`, `de-DE`, `fr-FR` and `en-GB`
*   The two delivery estimate lines are translated for the same six locales

**Tracking webhook**
* * *
*   The carrier posts `tracking.updated` for every parcel scan to `/webhooks/carrier/tracking` on shipping-service
*   The tracking path stays separate from the label event path, because the carrier signs each subscription with its own secret
*   Every event is checked against `X-Carrier-Signature`, the hex HMAC-SHA256 of the raw body keyed with the tracking subscription's own secret
*   A 2xx goes back within `5 seconds`, or the carrier counts the delivery as failed
*   After a failed delivery the carrier makes up to `5 attempts` more, waiting `1 min, 5 min, 15 min, 1 h, 6 h` before each one, then drops the event
*   Delivery is at least once, so events are deduplicated on `event_id`
*   A dropped event cannot be recovered, because `GET /v1/shipments/{shipment_id}` returns label fields only and tracking history is not part of our plan with the carrier

**Event order**
* * *
*   Events are ordered by `occurred_at`, never by arrival
*   An event whose `occurred_at` is older than the newest one held for that parcel is stored for the history and does not change the status shown

**Volume**
* * *
*   About `3,100` parcels leave on a normal working day and up to `5,400` on the busiest days so far this year
*   Each parcel produces `5 to 8` events, so a peak day means up to about `43,000` events
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

#### Order page
* * *
1\. **Customers can see where their parcel is**
* * *
*   **Given** a customer has a shipped order
*   **When** the carrier scans the parcel and the customer opens the order page on web, iOS or Android
*   **Then** the page shows the parcel's new status
*   **And** every earlier step stays in the timeline with its date and time
* * *
- [ ] _Mark as done, if the criteria are met_

2\. **Customers see an arrival day only when the carrier gives one**
* * *
*   **Given** the carrier has sent a delivery window for a parcel
*   **When** the customer opens the order page
*   **Then** the expected day and window show under the current status
*   **And** a parcel with no delivery window shows no estimate at all
* * *
- [ ] _Mark as done, if the criteria are met_

3\. **A failed delivery and the next attempt are both visible**
* * *
*   **Given** a parcel shows `Delivery failed`
*   **When** the carrier takes it out for delivery again
*   **Then** the page shows `Out for delivery`
*   **And** the failed attempt stays in the timeline
* * *
- [ ] _Mark as done, if the criteria are met_

4\. **Each parcel has its own timeline**
* * *
*   **Given** an order ships in several parcels
*   **When** the customer opens the order page
*   **Then** each parcel shows its own timeline with its own items under it
* * *
- [ ] _Mark as done, if the criteria are met_

5\. **Pallet deliveries keep today's page**
* * *
*   **Given** an order holds pallet items
*   **When** the customer opens the order page
*   **Then** the pallet items keep today's page with the delivery slot line
* * *
- [ ] _Mark as done, if the criteria are met_

6\. **Older orders show where they ended**
* * *
*   **Given** a parcel was delivered longer ago than tracking events are kept
*   **When** the customer opens the order page
*   **Then** the page shows the last status only
* * *
- [ ] _Mark as done, if the criteria are met_

#### Tracking events
* * *
7\. **Late and repeated scans never mislead the customer**
* * *
*   **Given** a scan arrives late or more than once
*   **When** it reaches us
*   **Then** the page keeps the status of the parcel's most recent scan
*   **And** a repeated scan adds no second step to the timeline
* * *
- [ ] _Mark as done, if the criteria are met_

8\. **Busy days lose no scans**
* * *
*   **Given** a peak dispatch day
*   **When** the carrier sends that day's events
*   **Then** every event is accepted in time, so no parcel's timeline misses a step
* * *
- [ ] _Mark as done, if the criteria are met_
* * *
##   
