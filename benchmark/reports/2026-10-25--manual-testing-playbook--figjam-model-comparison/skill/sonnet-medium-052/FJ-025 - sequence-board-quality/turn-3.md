The file read came back as an empty page, so nothing is on it and no section shares either board title. The check passed and both boards composed. Nothing is written yet.

Question: in what order do the guest app, the booking API, the payment provider and the partner hub exchange messages when a guest pays at checkout?
Outcome: an engineer can read both checkout payment paths in order, with what each call carries and the status code it ends on, and check the 15 minute hold against the code.

Glance lines:

- Board 1, first glance: Authorise card (message 3), the call that decides the checkout
- Board 1, second glance: Authorised, which lets the API confirm the hold and answer the app with 201
- Board 1, last glance: the booking post, the hold, Confirm the hold and the hub message (booking id and dates), which does not hold up the 201
- Board 2, first glance: Declined (message 4), the answer that ends the checkout
- Board 2, second glance: Release the hold and 402 Card declined
- Board 2, last glance: the booking post, the hold and Authorise card

Sketch, the checked model exactly as the check read it:

```text
sequenceDiagram
    title 1. Checkout payment, card authorised
    %% subtitle: The calls from the booking post to the 201, for a card that is authorised, for engineers on checkout and payments
    %% source: Source: the payments brief. Left out: the declined card, drawn on board 2. Hold expiry and retries, which the brief does not state.
    %% focus: 3 because it decides the checkout
    participant GuestApp
    participant BookingApi
    participant PaymentProvider
    participant PartnerHub
    GuestApp->>BookingApi: Post booking: room, dates, card token
    BookingApi->>BookingApi: Hold the room for 15 minutes
    BookingApi->>PaymentProvider: Authorise card
    PaymentProvider-->>BookingApi: Authorised
    BookingApi->>BookingApi: Confirm the hold
    BookingApi-)PartnerHub: Booking id and dates
    BookingApi-->>GuestApp: 201

sequenceDiagram
    title 2. Checkout payment, card declined
    %% subtitle: The calls from the booking post to the 402, for a card that is declined, for engineers on checkout and payments
    %% source: Source: the payments brief. Left out: a partner hub message and hold expiry, which the brief does not state.
    %% focus: 4 because a decline ends checkout
    participant GuestApp
    participant BookingApi
    participant PaymentProvider
    GuestApp->>BookingApi: Post booking: room, dates, card token
    BookingApi->>BookingApi: Hold the room for 15 minutes
    BookingApi->>PaymentProvider: Authorise card
    PaymentProvider-->>BookingApi: Declined
    BookingApi->>BookingApi: Release the hold
    BookingApi-->>GuestApp: 402 Card declined
```

```text
  diagram 1, sequence: ok, 4 participants and 7 messages
  diagram 2, sequence: ok, 3 participants and 6 messages
PASSED 2 diagram(s) in model.md
```

Critique of the sketch:

- Eye first: Authorise card on board 1 and Declined on board 2. Each is the message its board most needs read
- Reads second: Authorised on board 1 and Release the hold with 402 on board 2, and each advances the first
- Could miss: the hub message on board 1. Missing it hides that the hub hears of the booking without holding up the 201
- Remove next: Confirm the hold, kept because the brief lists it between the authorisation and the hub message

Plan: Roamstay Product, as you stated. I did not check which plan owns the file
File: <test-file-key>, as two new sections beside what it holds. It holds nothing now
Writes: board 1 (4 participants, 7 numbered messages) then board 2 (3 participants, 6 numbered messages). Each has a title, a subtitle, a key and a source line, at laptop reading distance. Board 1 is written first so the boards read left to right with the authorised path first
Left out: the hub message on a decline, hold expiry at 15 minutes and retries, because the brief does not state them. The booking post carries no URL because the brief gives none
Extensions: none
Calls: two `use_figma` calls and one `get_figjam` read-back. The read of the empty file is already spent. A Starter plan or a View or Collab seat has six tool calls a month and reads count, so on one of those the read-back could be refused. I would then report `Read-back: not possible` and not call the boards done
Rollback: delete the two board sections the writes return, through `use_figma`, and only after a yes that names them

Write both boards to this file?