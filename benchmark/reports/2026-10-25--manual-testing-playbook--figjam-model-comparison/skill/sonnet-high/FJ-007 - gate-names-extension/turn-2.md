The model passes the pre-write check, so this is the write gate. The checked sketch is below.

```text
stateDiagram-v2
    direction LR
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

check: diagram 1, state: ok, 7 states and 12 transitions, PASSED
composed: 12 nodes and 12 connectors to read back
```

**Question:** which statuses exist, and who sets Cancelled and No-show?
**Outcome:** support can see how a booking reaches Cancelled or No-show and who sets each, so they know who to ask.
**First glance:** Pending, the light blue first state. I set no accent, so the board shows whatever the layout shows first.
**Second glance:** the moves into Cancelled and No-show, "guest cancels" and "missed check-in [from Upcoming]", and the two notes beside them.
**Last glance:** Completed, in light gray with the other final states.

**File:** your existing FigJam file `<draft-file-key>`. The board lands as a new section beside what is already there, and nothing already on the file changes. You said the file sits in the Roamstay Product plan. I can't confirm that from the key, and no plan is needed to write into an existing file.
**New file, only if needed:** if that file turns out not to be a FigJam board or won't accept the write, I'd create one in the Barter team plan, left in drafts with no project, and write the board there.
**Writes:** one composed board titled "Booking status lifecycle". It has 7 states and 12 transitions, a key and a source line, at laptop reading distance.
**Extensions:** two single stickies in one colour, named `note:1` and `note:2`:
* `note:1` beside Cancelled: "Set by the guest, while a booking is Pending or Confirmed"
* `note:2` beside No-show: "Set by the hotel, after a missed check-in"

**Calls:** five.
* `create_session`
* one `get_figjam` read before the write, to record what the file holds
* one `use_figma` for the board
* one `use_figma` for the two notes
* one `get_figjam` read-back

The fallback adds `whoami` and `create_new_file`. A Starter plan or a View or Collab seat is limited to six tool calls a month, so five leaves one spare.
**Rollback:** delete the one board section the write returns, which removes the board and its notes. If only the notes need to go, I delete the two returned note ids. Either deletion runs only after a yes to a question that names it.

Write it?