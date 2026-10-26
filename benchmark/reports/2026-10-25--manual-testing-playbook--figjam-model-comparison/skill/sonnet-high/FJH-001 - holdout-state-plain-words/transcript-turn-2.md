# FJH-001 turn 2 transcript

**User:** Use your recommended answers.

**Assistant:**

Here is the full reading, with your recommended answers applied. I haven't drawn anything or written anything to FigJam yet.

**Settled rows**

| Row | Value | Status |
|---|---|---|
| Reader | Post-purchase product and the engineers building the timeline | assumed |
| Question | Which statuses an order can be in and what moves it between them | captured |
| Outcome | The reader sees which system or carrier event causes each move, and which moves the sources don't give | assumed |
| Entry | Payment authorised, from orders-service | captured |
| Exit | `Delivered`, which ends the board because returns are out of scope | assumed |
| Actors | orders-service, the warehouse system and the parcel carrier, by webhook into shipping-service | captured |
| Sources | The order tracking brief (proposal) and the carrier tracking facts (current behaviour, confirmed on a call with the carrier) | captured |

**Moves I would draw**

1. Entry to `Order placed`: payment authorised.
2. `Order placed` to `Packed`: the warehouse reports the order packed.
3. `Packed` to `Shipped`: carrier scan `PU` or `IT`.
4. `Shipped` to `Out for delivery`: carrier `OD`.
5. `Out for delivery` to `Delivered`: carrier `DL`.
6. `Out for delivery` to `Delivery failed`: carrier `EX`.
7. `Delivery failed` to `Out for delivery`: a new `OD` the next working day, after `NOT_HOME`.
8. `Delivery failed` to `Delivered`: `DL` at a parcel point, after a second `NOT_HOME`.

**Three things that change what I told you**

- **I withdraw my earlier example.** I said `Delivery failed` never goes straight to `Delivered`. The carrier notes say a `DL` follows a second `NOT_HOME` when the parcel reaches a parcel point, and they state no `OD` in between. Move 8 is drawn that way and marked assumed. A source saying an `OD` comes first would settle it.
- **Four of the six statuses are proposed, not live.** The company context says the order page shows only `Order placed` and `Shipped` today and never changes after that. `Packed`, `Out for delivery`, `Delivered` and `Delivery failed` come from Hamid's brief. The title will say "proposed" and the subtitle will say what the page shows today.
- **The machine runs per parcel, not per order.** The brief gives one timeline per parcel for an order with several parcels. No source defines the order's overall status in that case, so the subtitle says "per parcel".

**Other assumptions**
- Repeated `IT` scans keep the status at `Shipped`, so I'd draw no loop for them.
- The rule that carrier events are ordered by scan time, with older late events stored but not changing the status, goes in the subtitle. A state diagram has no note nodes.
- The look is laptop distance, balanced detail and a mixed audience. Labels use plain words with the carrier code in brackets, such as `picked up or scanned [PU, IT]`. The first glance is `Delivery failed`, because it's the only status with a way back. A state diagram takes no zones.

**Left out, as `Left out:` lines on the board's reply**
- Cancellation, refunds and returns, because no source gives their statuses
- Pallet orders, which send no tracking events and keep today's page
- What follows an `EX` of `ADDRESS_PROBLEM`, `DAMAGED` or `REFUSED`
- An order's overall status when it has several parcels
- Display rules: the delivery estimate, the 90-day history and the translations

Is that reading right, including move 8 and the "proposed" and "per parcel" framing?
