# Roamstay company context

Maintained by Leila, Product Operations Lead. Last reviewed on 2026-09-18.

Roamstay is a hotel booking marketplace. Guests search and book stays at hotels, guesthouses and serviced apartments, and partners list and run their properties on it. About 18,000 properties are live, across Europe and the United States.

## Product and surfaces

Roamstay has three surfaces. Each has its own owners and its own release rhythm.

| Surface | Used by | Platforms | Covers |
|---------|---------|-----------|--------|
| Guest app | Guests | iOS, Android, web | Search, property page, checkout, trips, account, chat with Guest Support |
| Partner Hub | Partners | Web, built for desktop | Property profile, rooms, rates and availability, policies, city tax, payouts, bookings list, guest reviews |
| Back office | Ops agents, Guest Support | Web, staff only | Booking lookup, refunds and rebooking, partner verification, go-live review, payout holds |

When a ticket says Guest app without a platform, it means iOS, Android and web together. The web version uses the same services as the apps, but it is built and released on its own.

Partner Hub is where a partner changes what guests see. A price, a photo, a cancellation policy or a city tax rule saved there reaches the Guest app through `partner-service` within 5 minutes.

Back office is invisible to guests and partners. Every refund, rebooking or payout hold made there is logged against the agent who made it.

## Personas and roles

| Persona | Works in | What they do |
|---------|----------|--------------|
| Guest | Guest app | Searches, books and manages stays. Can book signed in or with an email address only |
| Partner | Partner Hub | Runs one or more properties. Partner Hub users are Owner, Manager or Front desk, and only an Owner can change payout details |
| Ops agent | Back office | Roamstay staff who verify new partners, set up and check properties before go-live and handle partner escalations |
| Guest Support agent | Back office and the support desk tool | Answers guest chats and emails in six languages and escalates product defects to the owning squad as a ticket |

Guest Support is its own team inside Operations, next to the Ops agents. A defect reaches a squad as a Guest Support ticket with a priority of Low, Medium, High or Urgent, set by the Tier 2 agent who escalates it.

## Glossary

| Term | Meaning |
|------|---------|
| Stay | One booking's dates at one property, counted in nights. Check-in on a Monday and check-out on a Thursday is 3 nights |
| Property | A hotel, guesthouse or apartment building listed by a partner, identified by a numeric property ID |
| Room type | A kind of room at a property, such as Double room or Family suite, with a maximum occupancy |
| Rate plan | A price for a room type with its own cancellation policy and payment option. One room type often has two or three |
| Free cancellation | A rate plan policy that refunds the guest in full if they cancel before a deadline the partner sets |
| Non-refundable | A rate plan policy with no refund after booking, usually priced lower |
| City tax | A local tax the partner enters in Partner Hub, per adult per night or per stay. It shows as its own `City tax` line in the price breakdown and is part of the total |
| Pay now | The guest pays the full total at booking, and the payment provider charges the card |
| Pay at property | The guest's card is stored as a guarantee and the guest pays the property on arrival |
| Booking reference | `RS-` followed by six letters and digits. It is on the confirmation screen, in every email and in Back office |
| `payment_pending` | The booking state between Pay now and the payment provider's confirmation |
| Go-live | The moment a new property becomes bookable in the Guest app |
| Payout | Money Roamstay sends a partner for completed stays, after commission |

## Services and integrations

| Service | Owner squad | Responsibility |
|---------|-------------|----------------|
| `search-service` | Search | Availability search, ranking, filters and paging, at `25 results` per page |
| `booking-service` | Booking | Creates bookings, owns booking states and references, sends confirmation emails |
| `payments-service` | Payments | Card payments, refunds and payouts with the payment provider, and the webhooks it sends back |
| `partner-service` | Partner | Properties, room types, rate plans, policies, city tax rules and partner users |
| `events-collector` | Data | Receives analytics events from the apps, the web and the services |

Third parties appear by role in tickets and docs, never by name:

- The payment provider takes card payments for Pay now, stores cards for Pay at property and sends partner payouts. Only `payments-service` talks to it, and it reports payment results back by webhook
- The map provider serves map tiles and geocoding for search and the property page
- The email delivery provider sends booking confirmations for `booking-service` and partner emails for `partner-service`
- A channel manager is a partner's own tool for pushing rates and availability to several booking sites at once. It connects to `partner-service` through the partner API
- The identity verification provider checks the identity documents of property owners during partner verification

## Teams and discipline codes

Product and engineering work in six squads: Search, Booking, Payments, Partner, Ops Tools and Data. A Design System group works across all of them. Each squad has a product manager, a product designer and engineers for the surfaces it owns.

| Code | Discipline | Typical work |
|------|------------|--------------|
| `FE` | Front end | Guest app screens on iOS, Android and web, Partner Hub screens |
| `BE` | Back end | Services, APIs, scheduled jobs and webhooks |
| `BO` | Back office | Back office tools and internal flows for Ops agents and Guest Support |
| `FS` | Full stack | One change across a screen and its service, when splitting it would ship half a feature |
| `DATA` | Data and tracking | Tracking events, the tracking plan, dashboards |
| `DS` | Design system | Shared components, tokens and icons |

Task and bug titles follow `{Discipline} - {Surface} - {Feature code} - {Title}`. The surface is Guest app, Partner Hub or Back office, and the feature code comes from the next section. Two titles from the current backlog: `FE - Partner Hub - PHUB - Bulk rate editor` and `BO - Back office - OPS - Refund reason codes`.

Story and epic titles carry no discipline code. A story title reads `{Persona or surface} - {Area} - {Feature}`, as in `Guest - Trips - Add a stay to the calendar`, and an epic title reads `Epic - {Persona or surface} - {Area}`.

## Feature codes

| Code | Area | Owner squad |
|------|------|-------------|
| `SRCH` | Search form, date picker, results list, filters, sort, map | Search |
| `PROP` | Property page, photos, room list, guest reviews | Search |
| `BOOK` | Checkout, booking states, confirmation screen, trips, cancellation | Booking |
| `PAY` | Pay now, Pay at property, refunds, payouts, payment webhooks | Payments |
| `PHUB` | Partner Hub rates, availability, policies, city tax, bookings list | Partner |
| `ONB` | Partner sign-up, verification and go-live | Partner |
| `TRK` | Analytics events and the tracking plan | Data |
| `OPS` | Back office tools for Ops agents and Guest Support | Ops Tools |

A piece of work takes the code of the area it changes, whichever squad picks it up. A city tax change on the checkout screen is `BOOK`, and the setup screen for the same rule in Partner Hub is `PHUB`.

## Platforms and app versions

| Platform | Current version | Released | Minimum OS |
|----------|-----------------|----------|------------|
| iOS | `8.12.0` | `2026-09-16` | iOS 16 |
| Android | `8.12.1` | `2026-09-16` | Android 9 |
| Web | Continuous deploys | Several times a day | Last two major versions of the main browsers |

The apps ship on a two-week release train. The branch is cut on a Monday and the builds go to the stores on the Wednesday after. The previous train was 8.11.2 on both platforms, released on 2026-09-02.

Android went out as 8.12.1 because the 8.12.0 build was turned back by the store over a permissions text, so the two apps carry different numbers for the same train. Android rolls out in stages over 5 days, iOS to everyone on release day.

Apps below 8.6.0 show a forced update screen. Partner Hub and Back office are web only and deploy continuously, like the web version of the Guest app.

## Currencies and locales

Roamstay supports five currencies: `EUR`, `GBP`, `USD`, `CHF` and `SEK`. A partner sets one currency per property in Partner Hub, and the Guest app shows and charges prices in that currency. There is no currency conversion.

Services and events carry money as an integer in minor units. The apps format it for the guest's locale, so the same amount shows as €1,240.50 in `en-GB` and as 1.240,50 € in `de-DE`.

| Locale | Language | Notes |
|--------|----------|-------|
| `en-GB` | English | Default, and the fallback for any missing string |
| `en-US` | English | US spelling, week starts on Sunday |
| `de-DE` | German | Strings run about 30% longer than English, check button widths |
| `fr-FR` | French | Space before the currency sign in prices |
| `es-ES` | Spanish | Space before the currency sign in prices |
| `it-IT` | Italian | Space before the currency sign in prices |
| `nl-NL` | Dutch | Currency sign before the amount, with a space |

Every locale except `en-US` starts the week on Monday. The apps follow the device locale for dates and prices, and the web follows the browser locale. Partner Hub is available in the same seven locales.

## Key flows

### Search

The guest enters a destination, check-in and check-out dates, guests and rooms. A stay runs from 1 night to `30 nights` and check-in can be at most `365 days` ahead. One search covers up to `8 rooms`. `search-service` returns `25 results` per page, sorted by Recommended. The apps load the next page on scroll. The filter sheet holds two filters today, Price and Star rating.

### Property page

The property page shows photos, room types and, for each room type, its rate plans with their cancellation policy and payment option. A partner can set a minimum stay for the property, which the date picker applies on this page.

### Checkout and payment

The guest enters their details and picks a rate plan's payment option. The price breakdown lists the room price per night and the total, with a `City tax` line between them when the property charges it.

With `Pay now`, the payment provider charges the full total, city tax included. The booking waits in `payment_pending` until the payment provider confirms by webhook, then moves to confirmed. A booking still in `payment_pending` after `30 minutes` expires and its room goes back on sale.

With `Pay at property`, the card is stored as a guarantee and the booking confirms at once. The guest pays the property on arrival, city tax included.

### Confirmation and trips

The confirmation screen shows the booking reference, dates, guests and the total. `booking-service` sends the confirmation email at the same moment. The stay then lives under Trips, where the guest can view it, change dates or cancel.

### Cancellation

Before the free cancellation deadline, the guest cancels under Trips and the refund goes back to the card through the payment provider. After the deadline, or on a non-refundable rate plan, the guest contacts Guest Support.

### Partner onboarding today

A partner signs up with a short form on the web. An Ops agent then sets up the property in Back office from the details the partner sends by email. The same agent checks identity and payout details and makes the property live.

## Known constraints

- A stay is at most `30 nights`, and check-in is at most `365 days` ahead
- One booking holds at most `8 rooms`
- A booking in `payment_pending` expires after `30 minutes`
- Prices show and charge in the property's currency, with no conversion
- Roamstay has no loyalty or points scheme. Guests earn no points, and there are no member tiers or member-only prices
- Guests who book with an email address only cannot save a card
- Partner Hub has no mobile app, and its screens are designed for desktop widths
- Back office needs a staff account and is never exposed to partners
- Guest Support covers 07:00 to 23:00 CET, seven days a week

## Analytics conventions

- Event names follow `object_action` in snake_case, with the action in the past tense
- A search filter the guest turns on fires `filter_applied`, with `filter_name` saying which filter
- Every client event carries `app_version`, `session_id`, `platform` and `locale`
- Server events carry the `session_id` of the request that caused them, so client and server events join on it
- Every event carries `source`, which is `client` or `server`
- Money travels as an integer in minor units, in a property whose name ends in `_minor`, with a `currency` property beside it. €129.50 is sent as `12950`
- Events go to `events-collector`, which accepts events from the apps, the web and the services
- The Data team owns the tracking plan. Each event has a row with its trigger, its properties and a status, and a squad builds an event from its row
