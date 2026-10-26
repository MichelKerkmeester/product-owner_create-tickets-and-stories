Here's how I'm reading the brief, including your answers. Please confirm it or correct it before I write the model. Nothing has been written yet.

**What the board answers**
- **Question:** when a Roamstay guest pays at checkout, in what order do the guest app, booking API, payment provider and partner hub send messages?
- **Outcome:** engineers and product people working on checkout can see which party makes each call, and in what order, before they change the flow.

**Already settled**
- **From the payments brief:** the four parties and the six steps in order. The flow starts when the app posts the booking and ends when the API answers the app with 201.
- **From your answers:** who the board is for, and that it shows only the path where everything succeeds.

**Assumed (correct me if wrong)**
- **Holding and confirming the room:** I'm drawing both as work inside the booking API, so no fifth party. This changes if the hold calls a separate inventory system.
- **What the brief describes:** I'm treating it as how checkout works today, not a planned change. This changes if the brief is a proposal, and then the subtitle would say so.

**Outline, in drawing order**
1. Guest app → Booking API: post booking
2. Booking API → Booking API: hold room
3. Booking API → Payment provider: authorise card
4. Booking API → Booking API: confirm hold
5. Booking API → Partner hub: notify booking
6. Booking API → Guest app: 201 Created

**Two ways to draw it**
- **Sequence diagram, success path only (recommended):** it shows exactly the order the brief gives. It leaves out failures.
- **Architecture view:** it shows which parts connect to which, but loses the order. That's the main thing your reader needs, so I'm not recommending it.

**Look**
- **Highlighted step:** the "authorise card" call, because the board is about the payment.
- **Detail:** one arrow per step in the brief, with no request or response bodies.
- **Zones:** none, because four parties read fine without grouping.
- **Title:** Roamstay checkout payment
- **Subtitle:** Message order when a guest books and pays, success path only
- **Source line:** Roamstay payments brief

**Left out**
- The payment provider's reply to the authorisation and any reply from the partner hub, because the brief doesn't state either.
- A declined card and other failures, as you agreed.

Does this reading match the payments brief, or should a step, party or assumption change?