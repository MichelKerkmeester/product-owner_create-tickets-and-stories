# Booking funnel tracking plan, draft v0.3

Source: tracking plan draft in the Data team space, shared with the Booking and Search squads for comments
Written by Nadia, Data Analyst, Data team. Last edited on 2026-09-15
Comments close at the Booking squad refinement on 2026-09-24

## Why we're redoing this

We can't draw one clean funnel from search to booking today. The problems, in the order they hurt:

- `checkout_complete` fires when the confirmation screen renders on the client. We lose the booking when the app closes before the screen draws, and count it twice when the guest reopens the confirmation from Trips
- The web sends amounts as decimals and the apps send minor units, so revenue per step doesn't add up across platforms
- Search and property page events carry dates in three different formats

## Events

| Event | Fires when | Sent from | Status |
|-------|------------|-----------|--------|
| `search_submitted` | The guest taps Search with a destination and valid dates | Client | changed |
| `property_viewed` | The property page opens | Client | changed |
| `room_selected` | The guest picks a room type and rate plan | Client | new |
| `checkout_started` | The checkout screen opens | Client | new |
| `payment_submitted` | The guest taps Pay now, or confirms a Pay at property booking | Client | new |
| `booking_confirmed` | `booking-service` moves the booking to confirmed | Server, `booking-service` | new |
| `checkout_complete` | The confirmation screen renders | Client | deprecated, removal on 2026-11-01 |
| `date_changed` | The guest changes dates on the property page | Client | proposed |

Status key: new, changed (a live event whose properties change), deprecated (fires until its removal date), proposed (raised in comments).

## Properties

The common properties from our analytics conventions (`app_version`, `session_id`, `platform`, `locale` and `source`) go on every event and aren't repeated below.

| Property | Type | Example | On events |
|----------|------|---------|-----------|
| `destination_id` | integer | 1187 | `search_submitted` |
| `property_id` | integer | 51876 | `property_viewed` and every later step |
| `check_in` | date, `YYYY-MM-DD` | first night of the stay | every event in the table |
| `check_out` | date, `YYYY-MM-DD` | departure day | every event in the table |
| `nights` | integer | 4 | every event in the table |
| `guests` | integer, adults plus children | 2 | every event in the table |
| `rooms` | integer | 1 | every event in the table |
| `room_type_id` | integer | 88213 | `room_selected` onward |
| `rate_plan_id` | integer | 301442 | `room_selected` onward |
| `total_amount_minor` | integer, minor units, city tax included | 51600 | `room_selected` onward |
| `currency` | ISO code | EUR | `room_selected` onward |
| `payment_option` | `pay_now` or `pay_at_property` | pay_now | `payment_submitted`, `booking_confirmed` |
| `booking_id` | string, the booking reference | RS-2MF8QD | `booking_confirmed` |

## Notes per event

- `search_submitted` and `property_viewed` exist today. They move their dates to `check_in` and `check_out` in `YYYY-MM-DD` and gain `nights` and `guests`
- `room_selected` fires once per pick. A guest who goes back and picks another room sends it again
- `payment_submitted` fires on the tap, before the payment provider answers. It tells us the guest tried to pay, and nothing about whether the payment went through
- `booking_confirmed` is sent by `booking-service` with `source` set to `server`, when a Pay now booking leaves `payment_pending` or when a Pay at property booking is created. It copies `session_id` and `app_version` from the checkout request. Every booking count should use this event
- `checkout_complete` keeps firing next to `booking_confirmed` until 2026-11-01, so dashboards can move over. From that date `events-collector` drops it, whatever app version sends it
- `date_changed` has no properties agreed yet beyond the common ones and the dates

## Comments

Tomas, Product Manager, Search, 2026-09-11
Could we add a `date_changed` event on the property page? We'd like to know how often guests change dates after they see prices.

Nadia, 2026-09-12
Added the row as proposed. Open point: one event per tap in the picker, or one when the new range is applied? Let's settle that with Search.

Oskar, Android engineer, 2026-09-15
For `room_selected`, the Android app doesn't know `total_amount_minor` until the price call returns. Is it fine to send the event after that call instead of on the tap?

Nadia, 2026-09-15
Yes, send it once the price is known. A few hundred milliseconds late is fine.

## Who builds what

- Apps and web: the client events, on iOS, Android and web together
- Booking squad: `booking_confirmed` in `booking-service`
- Data team: the funnel dashboard, moved from `checkout_complete` to `booking_confirmed` before 2026-11-01
