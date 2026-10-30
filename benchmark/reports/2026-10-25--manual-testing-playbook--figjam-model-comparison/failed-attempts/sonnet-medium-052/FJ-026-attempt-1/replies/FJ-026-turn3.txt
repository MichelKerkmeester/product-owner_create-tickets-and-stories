**Question:** which statuses can a Roamstay booking be in, and what moves it between them?
**Outcome:** support can read every booking status and spot the three it ends in.
**First glance:** Pending, the light blue first state where every booking starts.
**Second glance:** Upcoming and In stay, the states inside Confirmed, read with the section that frames them.
**Last glance:** Cancelled, marked by the focus line with a pink outline where it is drawn. Completed and No-show follow, each in light gray with the end-state ring.

**Sketch:** the checked model, with the check's output as it printed.

```mermaid
stateDiagram-v2
    %% title: Booking status
    %% subtitle: Every status a Roamstay booking passes through, from the pending card check to a completed, cancelled or missed stay
    %% source: Source: the booking doc lines quoted in the request. Left out: where a booking goes when the 15-minute card check ends without authorisation.
    %% level: balanced
    %% focus: Cancelled because support must spot it
    %% detail: Pending | Card is being checked | Lasts 15 minutes at most
    %% detail: Upcoming | Guest can change dates | No-show from 6 hours after check-in time
    %% detail: InStay | Hotel can add charges to the room
    %% detail: Cancelled | Cancel within 48 hours of check-in | keeps the first night's price
    direction LR
    state "In stay" as InStay
    state "No-show" as NoShow
    [*] --> Pending
    Pending --> Confirmed: card authorised
    state Confirmed {
        [*] --> Upcoming
        Upcoming --> InStay: check in
        InStay --> [*]
    }
    Confirmed --> Completed: check out [from In stay]
    Pending --> Cancelled: guest cancels
    Confirmed --> Cancelled: guest cancels
    Confirmed --> NoShow: missed check-in [from Upcoming]
    Completed --> [*]
    Cancelled --> [*]
    NoShow --> [*]
```

```text
  diagram 1, state: ok, 7 states and 12 transitions
PASSED 1 diagram(s) in model.md
```

**Eye first:** Pending, the light blue first state. Cancelled is the state the request names, and its pink outline marks it where it is drawn.
**Reads second:** Upcoming and In stay inside Confirmed. They carry the booking from the card check to the stay, and their bodies hold the date-change, No-show and room-charge rules.
**Could miss:** No-show. It leaves from Confirmed with the guard `from Upcoming`, so a reader could take it for a guest action when the hotel marks it.
**Remove next:** In stay. It stays because check-out leaves from it and it carries the room-charge rule.

**Plan:** Roamstay Product, as you named it. **File:** `<test-file-key>`. I read it once and it is empty, so no section shares the title "Booking status".
**Writes:** one new section, "Booking status", with 7 states and 12 transitions, a title, a key and a source line. The three end states are light gray and keyed "Final state". The reading distance is Laptop.
**Left out:** where a booking goes when the 15-minute card check ends without authorisation, because the doc leaves it open.
**Extensions:** none.
**Calls:** one `use_figma` and one `get_figjam` read-back. Figma caps a Starter plan or a View or Collab seat at six tool calls a month and this work has already used two, so tell me if that applies to you.
**Rollback:** delete the one board section the write returns, on your yes to a question that names it.

Write it?