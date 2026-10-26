Before I draw anything, here's how I've read the brief. Please confirm or correct it.

**Brief question:** What order do the calls run in when a guest pays at Roamstay checkout, and where does a declined card leave the flow?
**Outcome:** One sequence diagram that shows the success path ending in 201 and the decline path ending in 402.

**Settled by the payments brief**
- Participants: Guest app, Booking API, Payment provider, Partner hub
- Guest app → Booking API: post booking
- Booking API holds the room
- Booking API → Payment provider: authorise card
- Card authorised: Booking API confirms the hold, then tells the Partner hub
- Booking API → Guest app: 201
- Card declined: Booking API releases the hold, then Booking API → Guest app: 402

**Assumed (please correct any of these)**
- Holding, confirming and releasing the room happen inside the Booking API, so each one is drawn as a self-call rather than a call to a separate inventory service. If a room or inventory service does this, tell me and I'll add it as a participant
- On a decline, the Partner hub is not told. The brief only mentions the hub on success
- The decline branch splits right after the provider's answer. Retries, timeouts and the provider's own error codes are left out because the brief doesn't cover them

**Open: where the board goes**
You asked for a new board, and also for it to go into the existing file `<test-file-key>`. Flow Mode writes either to a new file it creates or to a file this work has already written to. That file was written outside this work, so I need to check one of these with you before any write:
- **Recommended:** a new FigJam file in the Roamstay Product plan
- Placing it in `<test-file-key>`, which I'd read first so it doesn't cover anything already there

The plan, the calls the write will use and the rollback come in a separate confirmation after you answer this. Nothing is written until you say yes to that.

**Is this reading right, including the two assumptions about the decline path?**