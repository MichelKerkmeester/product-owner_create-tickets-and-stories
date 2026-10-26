This is the playback of how I've read the payments brief. Nothing has been written to Figma yet.

**What the board answers:** what happens, in order, when a guest pays for a Roamstay booking, and what changes when the card is declined.

**Outcome:** one sequence diagram of the checkout payment, success path and decline path.

**What the payments brief settles**
- Participants, left to right: Guest app, Booking API, Payment provider, Partner hub
- 1. Guest app → Booking API: post booking
- 2. Booking API: hold the room
- 3. Booking API → Payment provider: authorise card
- 4. **Card authorised:** Booking API confirms the hold, notifies the Partner hub and replies 201 to the Guest app
- 5. **Card declined:** Booking API releases the hold and replies 402 to the Guest app. The Partner hub is not told

**What I've assumed (correct me if any are wrong)**
- Holding and releasing the room happen inside the Booking API. I've drawn them as self-steps, not calls to a separate inventory service. The brief names no other service
- The Partner hub notice is one-way, with no reply drawn. The brief doesn't mention a response
- The Payment provider replies with "authorised" or "declined", and the diagram splits into two branches at that reply
- First thing a reader should notice: the declined branch (hold released, 402)

**What's left out**
- Timeouts, retries and an unreachable provider. The brief doesn't cover them, so I'm not drawing them

**Target file to settle before writing:** Flow Mode only writes to a new board it creates, or to a board this same piece of work already wrote. File `<test-file-key>` is neither, so I can't put this diagram there. Your request also asks for both a new board and that existing file. My recommendation is a new board in the Roamstay Product plan. Once you've confirmed this reading, I'll set out the plan, the Figma calls it will use and the rollback, and ask separately before anything is written.

Is this reading of the checkout payment right, or should any step or assumption change?

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.