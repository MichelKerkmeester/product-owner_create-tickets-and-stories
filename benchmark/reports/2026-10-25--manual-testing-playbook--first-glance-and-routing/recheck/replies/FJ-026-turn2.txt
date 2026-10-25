The model passes the check and composes. This is the gate. Nothing is on the board yet.

```text
stateDiagram-v2
    direction LR
    NoShow: No-show
    InStay: In stay
    [*] --> Pending
    Pending --> Confirmed: card authorised
    state Confirmed {
        [*] --> Upcoming
        Upcoming --> InStay: check in
        InStay --> [*]
    }
    Confirmed --> Completed: check out
    Pending --> Cancelled: guest cancels
    Confirmed --> Cancelled: guest cancels
    Confirmed --> NoShow: missed check-in
    Completed --> [*]
    Cancelled --> [*]
    NoShow --> [*]
```

Check: `PASSED`, 7 states and 12 transitions. Composer: `COMPOSED`, 12 nodes and 12 connectors to read back.

Question: which statuses can a Roamstay booking be in, and what moves it between them?
Outcome: support can read any booking's status and spot the three statuses a booking ends in.
First glance: Pending, where every booking starts. There is no pink accent, so the layout shows it first at the left. The end states carry your colour request in light gray instead.
Second glance: the events that lead into the end states, which are check out, guest cancels and missed check-in.
Last glance: the source line, which names the left-out expiry.
File: the existing FigJam file `<test-file-key>`, in the Roamstay Product plan as you described. I can't confirm which plan owns the file, because `whoami` lists the plans your account holds and not who owns a file.
Writes: one new board section named "Booking status", with 7 states and 12 transitions, Completed, Cancelled and No-show in light gray, a title, a key and a source line, at laptop reading distance. It lands 400 pixels to the right of everything already on the page, and no existing node is touched. No new file is created.
Extensions: none.
Calls: `create_session`, one `use_figma` and one `get_figjam` read-back. I load Figma's `figma-use` and `figma-use-figjam` skills first. On a Starter plan or a View or Collab seat, Figma allows six tool calls a month and read tools count, so this board would spend part of that allowance.
Left out: the 30-minute expiry of a Pending booking, because no source names an Expired status.
Rollback: delete the one board section the write returns, through `use_figma`, and only after a separate yes from you.

Write it?