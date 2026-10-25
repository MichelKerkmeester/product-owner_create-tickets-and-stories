Nothing is written to the board. This is the third proposal, a sketch in chat. I also ran the pre-write check on it, and it passed: 9 nodes, 11 connectors, 0 crossing pairs, longest path 7 steps.

```mermaid
flowchart LR
    %% title: Change booking dates
    %% subtitle: What a Roamstay guest sees and pays at each outcome of changing their booking dates
    %% source: Source: the request, 2026-10-25. Left out: failed payment, cancellation, platform split, payment option.
    %% zone: Find a room: bookingPage, pickDates, roomFree, otherRooms
    %% zone: Settle the price: newPrice, payDiff, credit, noCharge, updated
    bookingPage([Booking page]) -->|Tap Change dates| pickDates[Pick new dates]
    pickDates --> roomFree{Room free?}
    roomFree -->|Yes| newPrice{New price?}
    roomFree -->|No| otherRooms[See other rooms]
    otherRooms -->|Pick a room| newPrice
    newPrice -->|Higher| payDiff[Pay the difference]
    newPrice -->|Lower| credit[Difference back as credit]
    newPrice -->|Same| noCharge[Nothing charged]
    payDiff --> updated([Updated booking])
    credit --> updated
    noCharge --> updated
    style updated fill:#CDF4D3,stroke:#66D575
```

**How it should read on the board**

* The main line runs left to right: Booking page, Pick new dates, Room free?, New price?, then one outcome, then Updated booking
* `See other rooms` sits beside the main line and rejoins at `New price?`
* The three outcomes stack beside each other and all point to `Updated booking`, which is the green goal

**Is this sketch right?** I recommend yes, because it matches the outline and Framing 2 you approved. If it is, the next step is the look: which node the colour marks, the title, the subtitle and the source line. I'll propose each with a recommended answer. After that comes the gate, which is its own reply, and the write waits for your yes to it.