# FJ-025 turn 2 transcript

**User:** Yes, that reading is right.

**Assistant:**

The gate for the write, with the checked model:

```mermaid
sequenceDiagram
    %% title: 1. Checkout payment, authorised card
    %% subtitle: The calls a Roamstay checkout makes when the card is authorised, for the payments team
    %% source: Source: the payments brief in the request. The declined card is board 2.
    %% focus: 3
    participant GuestApp
    participant BookingApi
    participant PaymentProvider
    participant PartnerHub
    GuestApp->>BookingApi: POST /bookings
    BookingApi->>BookingApi: Hold the room
    BookingApi->>PaymentProvider: Authorise card
    PaymentProvider-->>BookingApi: Authorised
    BookingApi->>BookingApi: Confirm the hold
    BookingApi-)PartnerHub: BookingCreated
    BookingApi-->>GuestApp: 201 Booking confirmed
```

```mermaid
sequenceDiagram
    %% title: 2. Checkout payment, declined card
    %% subtitle: The calls a Roamstay checkout makes when the card is declined, for the payments team
    %% source: Source: the payments brief in the request. The authorised card is board 1.
    %% focus: 4
    participant GuestApp
    participant BookingApi
    participant PaymentProvider
    GuestApp->>BookingApi: POST /bookings
    BookingApi->>BookingApi: Hold the room
    BookingApi->>PaymentProvider: Authorise card
    PaymentProvider-->>BookingApi: Declined
    BookingApi->>BookingApi: Release the hold
    BookingApi-->>GuestApp: 402 Payment declined
```

Both diagrams pass `flow_check.py`. The gate:

**Question:** in what order do the guest app, the booking API, the payment provider and the partner hub exchange messages for a Roamstay checkout payment?

**Outcome:** the payments team can trace the checkout calls in order, with their status codes, for an authorised card and for a declined one.

**Board 1 glances:** first glance Authorise card, the call that decides the checkout. Second glance Authorised, the answer that lets the booking API confirm the hold and answer the app. Last glance BookingCreated, the partner hub notify that does not hold up the 201.

**Board 2 glances:** first glance Declined, the answer that turns the path into a release and a 402. Second glance Release the hold, the cleanup the decline triggers. Last glance 402 Payment declined, what the app gets back.

**Plan:** Roamstay Product (as named in the request). **File:** the existing FigJam file <test-file-key>. The two boards land to the right of everything already on the page.

**Writes:** two composed boards. Board 1 "1. Checkout payment, authorised card" with 4 participants and 7 numbered messages, board 2 "2. Checkout payment, declined card" with 3 participants and 6 numbered messages, each with a title, a subtitle, a key and a source line, at the Laptop reading distance.

**Extensions:** none.

**Calls:** two `use_figma` writes, then `get_figjam` read-backs. After the write I will ask separately whether to remove the earlier exact-titled pair (73:562, 74:954).

**Rollback:** delete the two new board sections, nothing else on the file is touched.

Write it?
