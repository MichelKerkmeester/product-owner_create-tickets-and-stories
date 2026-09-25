# Order tracking on web and in the apps, PM brief

Written by Hamid, Product Manager, Post-purchase, on 2026-09-18, to be refined into a story with its tasks under it. Contact numbers come from the helpdesk, pulled on 2026-09-17.

## Why now

Where is my order is the biggest reason customers contact us. In August CS tagged 5,870 of 18,940 contacts as WISMO, which is 31%. Most of those customers already had a tracking number. What they wanted to know was when the parcel would arrive, and our order page could not tell them.

Today the order page on web and in the apps shows `Order placed` until dispatch and `Shipped` after it, with the tracking number, and it never changes after that. Customers copy the number into the parcel carrier's own site, and the ones who get lost there contact us.

## What we want

A status timeline on the order page, on web, iOS and Android, that moves as the parcel moves, with the expected delivery day when the carrier gives one.

The statuses, in order:

| Status the customer sees | Where it comes from |
|--------------------------|---------------------|
| `Order placed` | orders-service, when the payment is authorised |
| `Packed` | the warehouse system, when the order is packed |
| `Shipped` | parcel carrier codes `PU` (picked up) and `IT` (in transit) |
| `Out for delivery` | parcel carrier code `OD` |
| `Delivered` | parcel carrier code `DL` |
| `Delivery failed` | parcel carrier code `EX` |

After `Delivery failed` the carrier usually tries again the next working day, and a new `OD` moves the order back to `Out for delivery`. The timeline shows every step that happened, each with its date and time.

## Delivery estimate

When the carrier sends a delivery window, show the day and the window under the current status. From the design mock in the `Order page / Tracking timeline` frame:

`Arriving Thursday 1 October`

`Between 10:00 and 14:00`

When there is no window, show no estimate at all. We do not guess one from the dispatch date.

## Rules I already know

- An order with several parcels shows one timeline per parcel, with that parcel's items under it
- Tracking events are kept for `90 days` after delivery. After that the order page shows the last status only
- Items over `30 kg` or `120 cm` go by the pallet carrier, which sends no tracking events. Those keep today's page plus the line "The delivery company will call you to book a delivery slot"
- The shipping email keeps the tracking number, since some customers still want the carrier's page
- Status text is translated for all six locales

## Out of scope for this story

- A push notification for each status. That comes after, once we trust the events
- Changing the delivery address or day after dispatch
- Tracking for return parcels

## Engineering notes so far

Yusuf wrote up the parcel carrier's tracking API after a call with their integration team. The short version: events come by webhook, can arrive in any order, and carry the time of the scan. The tasks I expect under the story:

- `BE tracking webhook`: receive and store tracking events and map carrier codes to our statuses
- BE: `Packed` from the warehouse system into orders-service
- FE Web: timeline and delivery estimate on the order page
- FE iOS: the same
- FE Android: the same
- DATA: events for the timeline being viewed and the carrier link being tapped

## How we will know it worked

The WISMO share of contacts drops from 31% to under 20% within two months of release, with no rise in contacts from customers confused by the timeline.

## Open questions

- Should `Delivery failed` say why, when the carrier gives a reason? Maud from CS says yes for not home, and no for anything that sounds like our fault
- Design has mocked the timeline for the apps only so far. The web layout is still to come
