I've read the Flow packet, the sequence type reference, the rubric and the palette. Before drawing anything, two things block the draw, so this reply is the intake round, not a board.

**Reading:** The type is settled. A sequence answers "in what order do these parties exchange messages", so I am not asking about the type. Figma's generator draws at most 5 participants and 12 messages, with message labels of 40 characters or fewer, and one path per diagram because a branch renders flat. What is not settled is the flow. Your request names no product, no parties, no messages and no order, and no source was attached, so every row of the board's brief would be a guess rather than something read off your system. Entry and exit are the one pair already answered by the message set: the flow starts at the app's checkout submit and ends at the confirmation response.

**Sources**
Reading: none attached
Question: is there an API brief, a doc section, a ticket, or the routes and handlers I should read instead of working from your answer here
Recommended: work from your answers below, marked assumed and named before anything is drawn
Why: a diagram of a real partial system beats a polished one of an imagined system

**Parties, in column order**
Reading: the request names only "the checkout payment"
Question: which systems send and receive the messages
Recommended: GuestApp, CheckoutApi, PaymentProvider, PaymentWebhook
Why: four parties covers the shape most checkout systems run and leaves one slot under the five-party cap

**Messages and their order**
Reading: no message is named
Question: what is sent, what comes back, and in which order
Recommended: `POST /checkout`, then `Create payment intent`, then `202 Accepted` with the intent id, then `Authorise card`, then `200 Approved`, then the `payment_intent.succeeded` callback, then `Capture payment`, then `201 Confirmed` back to the app
Why: eight messages sits under the twelve-message cap, and each label carries a path or a status code so the board says something a list of steps cannot

**Which path**
Reading: the type's rules allow one path per diagram
Question: happy path first, or the declined-card path
Recommended: the happy path
Why: the failure path is a second diagram in the same file, drawn after this one

**Reader and decision**
Reading: nothing states an audience
Question: who opens this board, and what do they decide having read it
Recommended: engineers on the checkout and payments teams, deciding where a payment can stall between the app and the provider
Why: the reader settles the label vocabulary, which is exact paths and status codes for engineers and plainer verbs for a mixed team

**One limit on delivery in this session.** A sequence needs the hosted Figma MCP that carries `generate_diagram`. It is not connected here. The `figma-ds-cli` fallback draws a user flow and an unlaned process only, so it cannot draw a sequence, and the Code Mode `figma` manual in this workspace runs a server with no diagram tool. Once you answer, the pre-write check and the quality pass still run, and what comes next is a checked Mermaid sequence model you can keep. Writing it to a FigJam board needs this client connected to Figma's hosted server, from the Figma plugin or the client's own connector.

Answer the five parts and the checked model follows. Nothing was written to `export/` and no board was drawn.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.