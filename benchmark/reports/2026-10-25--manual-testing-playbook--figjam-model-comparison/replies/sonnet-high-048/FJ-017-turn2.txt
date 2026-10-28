Plan check: your account holds no plan named "Roamstay Product". It holds <figma-plan-1>, a Pro plan on a Full seat, and I read that as the <figma-plan-5> team plan you meant. The check passed and the board composes.

**Question:** which statuses does a Roamstay booking pass through, and who sets Cancelled and No-show?
**Outcome:** support can read every status, see which ones end a booking and know who to ask about Cancelled and No-show.
**First glance:** Pending, the light blue first state where every booking starts.
**Second glance:** Upcoming and In stay, the states inside Confirmed, read with the section that frames them.
**Last glance:** Cancelled and No-show with their notes, then Completed, each end state in light gray with its heavy outline.

**Sketch:** the checked model, with every `%%` line and the check's `PASSED` line as it printed.

```text
stateDiagram-v2
    %% title: Booking status
    %% subtitle: Every status a Roamstay booking passes through, and what moves it on
    %% source: Source: the product team's description of the booking lifecycle.
    %% notes: Cancelled, NoShow
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

  diagram 1, state: ok, 7 states and 12 transitions
Sides: Cancelled takes its sticky below, left aligned
Sides: No-show takes its sticky left, centred
PASSED 1 diagram(s) in model.md
```

**Eye first:** Pending, the first state the layout always shows. It is not the state the notes explain, but the notes sit beside the two end states they belong to.
**Reads second:** Upcoming and In stay inside Confirmed, which carry the booking from card authorisation to the stay.
**Could miss:** the two notes. Missing them costs support the answer to who to ask.
**Remove next:** In stay, kept because check-out leaves from it.

**Plan:** <figma-plan-1> (Pro, Full seat)
**File:** a new FigJam file named "Booking status", in your drafts with no project.
**Writes:** one composed board with 7 states and 12 transitions, a title, a key and a source line, at laptop distance.
**Extensions:** two single stickies named `note:1` and `note:2`.
- On Cancelled: "Set by the guest, while the booking is Pending or Confirmed". It sits below the state.
- On No-show: "Set by the hotel after a missed check-in". It sits to the left of the state.

**Left out:** a declined card, a hotel-side cancellation and a refund, because your message states none of them.
**Calls:** `create_new_file`, `create_session`, one `use_figma` for the board, one for the notes, and a `get_figjam` read-back after each.
**Rollback:** delete the new file, which removes the board and both notes.

Write it?