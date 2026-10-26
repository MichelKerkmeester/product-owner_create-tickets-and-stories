I've taken your recommended answers, and they settle round one. The workspace source covers entry, exit, actors and states, so I'm skipping rounds two and three. Below is the full playback of how I'm reading things. It has no model yet, and nothing is written until you give a separate yes at the write gate.

**What the board answers**
- **Reader:** product and engineering in the Booking squad (assumed)
- **Question:** which statuses can a booking hold, and what moves it between them?
- **Outcome:** the squad can check edge cases, such as expiry and cancellation, before planning work
- **Scope:** statuses and their triggers only. Payment-provider internals, refunds and screens stay off the board (assumed)

**Sources**
- **`context/roamstay-context.md`** (current behavior, reviewed 2026-09-18). This is Roamstay's lifecycle, not Barter's. You didn't send a source, so I'm using it as assumed. Send another source to replace it.
- **`context/roamstay-booking-funnel-tracking-plan.md`** confirms the two ways in: a Pay now booking leaves `payment_pending`, and a Pay at property booking confirms as soon as it's created.

**Outline**
- **Entry, Pay now:** guest pays → `payment_pending`
- **Entry, Pay at property:** guest books → Confirmed at once, with the card stored as a guarantee
- `payment_pending` → Confirmed: the payment provider confirms by webhook
- `payment_pending` → Expired: still unpaid after 30 minutes, and the room goes back on sale. Expired is an end state.
- Confirmed → Cancelled: the guest cancels under Trips before the free-cancellation deadline. Cancelled is an end state.

That's 4 states and 3 labelled moves between them, well inside the 9-state budget.

**Two ways to draw it**
- **A, recommended:** only what the source states, with each gap listed on the `Left out:` line. The board is small, but every line on it has a source.
- **B:** also draw the after-deadline cancellation through Guest Support and the date change as moves marked assumed. That covers more, but it puts guesses on a board engineers will plan from.

**Left out under A (the source doesn't give a status for these)**
- What follows Confirmed. The source mentions payouts for "completed stays" but names no Completed or No-show state, so Confirmed gets no end arrow.
- Cancellation after the deadline or on a non-refundable rate plan. The source only says the guest contacts Guest Support.
- A date change under Trips. The source doesn't say whether the status changes.

**Look (all recommended, so assumed until you correct them)**
- Detail: Balanced. Audience: Mixed. Reading distance: Laptop.
- First glance: `payment_pending`, where the expiry edge case starts. No zones.
- **Title:** Booking status lifecycle
- **Subtitle:** Which statuses a booking can hold and what moves it between them
- **Source line:** Roamstay company context, reviewed 2026-09-18

**Question:** Is this reading right, with framing A, Roamstay's lifecycle as the source and Confirmed left with no end arrow?
- Recommended: yes.
- Why: everything drawn has a source, and the three gaps are listed instead of guessed.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.