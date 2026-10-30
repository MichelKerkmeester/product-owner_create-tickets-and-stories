**Gate**

Question: which statuses can a Roamstay booking hold, and what moves it between them?
Outcome: the product team can agree the statuses and the allowed moves before a story is written.
First glance: Pending, the light blue first state where every booking starts, carrying the 15-minute rule.
Second glance: Upcoming and In stay, the states inside the Confirmed section.
Last glance: Completed, Cancelled and No-show, the end states in light gray, with the 6-hour rule on No-show.

Sketch, the checked model in full:

```text
stateDiagram-v2
    %% title: Roamstay booking statuses
    %% subtitle: From a Pending booking to Completed, Cancelled or No-show, for the Roamstay product team
    %% source: Sources: the request and the booking doc as quoted. Left out: what ends Pending after 15 minutes
    %% level: balanced
    %% detail: Pending | Lasts at most 15 minutes | While the card is checked
    %% detail: NoShow | Marked by the hotel | From 6 hours after check-in time
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
    Pending --> Cancelled: cancel
    Confirmed --> Cancelled: cancel / first night kept if within 48h
    Confirmed --> NoShow: missed check-in [from Upcoming]
    Completed --> [*]
    Cancelled --> [*]
    NoShow --> [*]
```

```text
  diagram 1, state: ok, 7 states and 12 transitions
PASSED 1 diagram(s) in model.md
```

Two small changes from the outline. The check counts 12 transitions, not 11, because I added the exit arrow inside Confirmed, the same shape as the worked example. The 48-hour label now says "within 48h" instead of "<48h", because the board takes no markup characters.

Eye first: Pending, which is the right node because every booking starts there and its 15-minute rule sits in the body.
Reads second: Upcoming and In stay, which carry a booking from authorisation to check-out.
Could miss: the 6-hour rule on No-show, which would make a missed check-in look like an immediate No-show. It sits in the body so it reads with the state.
Remove next: In stay, kept because check-out leaves from it and the doc names it.

File: board <test-file-key>. It holds one section, "Sprint retro", with six stickies, and no section shares this title. The new board lands as a section 400 pixels to its right, and nothing already there changes. The file needs no plan.
Writes: one composed board of 7 states and 12 transitions, with a title, a key and a source line, at the Laptop reading distance. The composed code is 44,322 characters, inside the 50,000 one call takes.
Extensions: none.
Calls: one `use_figma`, one `get_figjam` read-back of the new board and one more read of the file to confirm the retro section is unchanged. If the file is on a Starter plan or you have a View or Collab seat, the monthly allowance is six tool calls, and this work has spent two and will spend three more.
Rollback: delete the one new section, only on a yes that names it. The Sprint retro section is never touched.
Left out: what ends Pending after 15 minutes, the doc does not say

Write this board to <test-file-key>?