Before I draw anything, this is how I read the request. Nothing has been written to the board.

**Question:** which entities exist, which keys join them and how many of each. That is an ER diagram.
**Outcome:** a support agent can see the six stay tables, how they join and which tables sit on the guest side and which on the partner side.
**Target:** the existing file `<test-file-key>`, as one new board section. That file already belongs to a plan, so I won't create a new file. I haven't checked that it sits in Roamstay Product, so tell me if it doesn't.
**Settled by your message:** six entities (Guest, Booking, Payment, Property, Room, Rate Plan) and these joins:
* Guest makes Booking
* Booking reserves one Room under one Rate Plan
* Booking holds Payments
* Property offers Rooms
* Property publishes Rate Plans

**Assumed:** the guest zone holds Guest, Booking and Payment, and the partner zone holds Property, Room and Rate Plan. The reader is Guest Support.

One round of questions follows.

1. **The schema note itself**
   Reading: your message names the tables and joins, but the note with the keys and columns didn't come with it. I won't invent column names, because an ER board has to be read from the schema.
   Question: can you paste the note, or list the columns support asks about for each table?
   Recommended: paste the note, and I'll keep the primary and foreign keys plus the handful of columns you name.
   Why: only the note shows which columns support actually asks about.

2. **The minimum side of each join**
   Reading: "one room under one rate plan" fixes a booking at exactly one of each. Your message doesn't say whether a property can exist with no rooms yet, or whether a booking always has a payment.
   Question: which of these is right?
   Recommended: draw Property to Room and Property to Rate Plan as one to zero-or-more, and Booking to Payment as one to zero-or-more.
   Why: the Roamstay context says a Pay at property booking only stores a guarantee card. I read that as a booking that may have no payment, but I don't know how the schema records a guarantee. Unanswered, this stays marked assumed.

3. **The reader**
   Reading: "the few columns support asks about" points to Guest Support agents.
   Question: is Guest Support the audience?
   Recommended: yes.
   Why: it keeps the board to keys and lookup columns.

Is this the right reading, and can you send the note?