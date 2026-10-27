The check passed, and the file is ready for the write gate. I read the file once and its page is empty, so no existing section shares the title "Change booking dates", and nothing on it can change.

```text
flowchart LR
    bookingPage([Booking page]) -->|Tap Change dates| pickDates[Pick new dates]
    pickDates --> roomFree{Room free?}
    roomFree -->|Yes| priceCheck{New price vs old?}
    roomFree -->|No| otherRooms[See other rooms]
    otherRooms -->|Pick a room| priceCheck
    priceCheck -->|Higher| pay[Pay the difference]
    priceCheck -->|Lower| credit[Get the difference as credit]
    priceCheck -->|Same| updated([Updated booking])
    pay --> updated
    credit --> updated
    style priceCheck fill:#FFC2EC,stroke:#F849C1
```

Check: 8 nodes, 10 connectors, widest rank 2, longest path 7, 0 crossing pairs, PASSED.

* Question: which screens does a Roamstay guest pass through when changing booking dates, and where do they choose?
* Outcome: the product and design team can decide what the app does in each of the three price cases
* First glance: the New price vs old? decision, the one pink-outlined node
* Second glance: the light blue Booking page entry, and the Higher, Lower and Same exits that lead to the Updated booking goal
* Last glance: See other rooms, the key and the source line
* Plan: Roamstay Product. I can't confirm the plan from my side, so I'm going on your word that file `<draft-file-key>` sits in it
* File: `<draft-file-key>`, as a new section on its one page, with no new file
* Writes: one composed board of 8 nodes and 10 connectors with a title, subtitle, key and source line, at laptop distance with no zones
* Left out: payment failure, host approval and cancellation rules, none stated in your description
* Assumed: the "Pick a room" move after See other rooms, and the automatic room check after Pick new dates, both from your word and not a screen
* Extensions: none
* Calls: one `use_figma` and one `get_figjam` read-back, on top of the session and the one read already made. If your seat is on the Starter plan or a View or Collab seat, that is two more of its six monthly calls
* Rollback: delete the one board section the write returns, only on its own yes to a question that names it

Write it?