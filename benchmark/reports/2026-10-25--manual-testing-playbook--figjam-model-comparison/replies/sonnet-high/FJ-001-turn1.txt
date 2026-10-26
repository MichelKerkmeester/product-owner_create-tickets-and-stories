Before I draw anything, this is how I read the request. Nothing has been written to Figma yet.

**Target.** The board goes into the existing FigJam file `<draft-file-key>` as a new section beside what it already holds, and nothing already on the file changes. That means no new file, so the Barter team plan and drafts fallback isn't used. I can't confirm which plan owns that file. `whoami` lists the plans your account holds, but it doesn't say which one owns a file. I'm reading "Roamstay Product plan" as where the file lives, and I won't create anything in that plan.

**Question:** in what order do the guest app, the booking API, the payment provider and the partner hub exchange messages at checkout? A sequence diagram answers it.

**Outcome (assumed):** the payments and booking engineers can read the checkout calls in order, for a card that is authorised. Your message doesn't name a reader.

**Settled by your summary of the payments brief:**
* The order of the calls
* The 201 that answers the app

The brief itself isn't in the repo, so I'm working from your summary only, and every message below is sourced to it.

**How I'd draw it:** 4 participants and 7 numbered messages, inside the 5 and 12 budget.
1. GuestApp to BookingApi: Post the booking
2. BookingApi to itself: Hold the room
3. BookingApi to PaymentProvider: Authorise the card
4. PaymentProvider to BookingApi: Card authorised
5. BookingApi to itself: Confirm the hold
6. BookingApi to PartnerHub: Booking created
7. BookingApi to GuestApp: 201

**Assumed, because your summary doesn't state it:**
* **Messages 2 and 5:** self-messages on the booking API. Your summary doesn't say another party holds the room.
* **Message 4:** the provider's answer is drawn as a return. You wrote only that the API asks it to authorise.
* **Message 6:** fire-and-forget. You didn't say whether the API waits for the hub before it answers the app.
* **Labels:** written in your words, with no paths. The summary gives no route for the post, and 201 is the only status it states.
* **Scope:** the authorised-card path only. A declined card, a retry and any hub failure are left out, because your summary doesn't cover them. This is what the board must not do: draw a failure path nobody described.
* **Dials:** balanced detail, an engineer audience and Laptop reading distance.

**One conflict.** `context/roamstay-context.md` says only `payments-service` talks to the payment provider, while your summary has the booking API calling it. I recommend the brief governs, because it is the specific source for this flow. If the context file is right, a fifth party sits between messages 3 and 4, and you'd tell me what to call it.

Is this the right reading, and do the assumed items stand as written? Recommended: yes to all, since nothing in your summary points the other way.