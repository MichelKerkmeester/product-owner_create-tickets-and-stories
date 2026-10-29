Here's the gate for the write.

**Question:** which statuses can a Roamstay booking be in, and what moves it between them?
**Outcome:** the product and engineering team agree the status values and allowed moves before a story is written.
**First glance:** Pending, the light blue first state where every booking starts.
**Second glance:** Upcoming and In stay, the states inside Confirmed, read with the section that frames them.
**Last glance:** Completed, Cancelled and No-show, the end states, each in light gray with its heavy outline.

**Sketch**, the checked model in full:

```text
stateDiagram-v2
    %% title: Roamstay booking status lifecycle
    %% subtitle: From a new Pending booking to Completed, Cancelled or No-show, for the product and engineering team
    %% source: Sources: the team's description of the booking statuses. Left out: authorisation failure, refunds and booking changes, none stated.
    direction LR
    state "In stay" as InStay
    state "No-show" as NoShow
    [*] --> Pending
    Pending --> Confirmed: card authorised
    state Confirmed {
        [*] --> Upcoming
        Upcoming --> InStay: check-in
    }
    Confirmed --> Completed: check-out [from In stay]
    Pending --> Cancelled: guest cancels
    Confirmed --> Cancelled: guest cancels
    Confirmed --> NoShow: missed check-in [from Upcoming]
    Completed --> [*]
    Cancelled --> [*]
    NoShow --> [*]
```

```text
  diagram 1, state: ok, 7 states and 11 transitions
PASSED 1 diagram(s) in model.md
```

* **Eye first:** Pending, the first state the layout always shows. It is the right start, because every booking enters there.
* **Reads second:** Upcoming and In stay inside Confirmed, which carry the booking from payment to the stay.
* **Could miss:** the `[from Upcoming]` and `[from In stay]` guards. Without them, No-show and Check-out would read as open from every state in Confirmed.
* **Remove next:** In stay. It stays because check-out leaves from it.

**Target:** the existing FigJam file `<test-file-key>`, which needs no plan. I read it once. It holds one section, "Sprint retro", with six stickies, and no section shares my title.
**Writes:** one composed board, 7 states and 11 transitions, with a title, a key and a source line, placed as a new section to the right of "Sprint retro". Nothing already on the file changes.
**Extensions:** none.
**Left out:** authorisation failure, refunds and booking changes, because nothing states them.
**Calls:** one `use_figma` write, one `get_figjam` read-back and one more `get_figjam` read to confirm the stickies are untouched. A Starter plan or a View or Collab seat is limited to six tool calls a month, and reads count, so this plus the read I already made uses four of them.
**Rollback:** delete the one new board section the write returns. I delete it only on a reply that names it.

Write it?