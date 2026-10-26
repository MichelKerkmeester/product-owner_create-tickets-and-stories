Before I draw anything, this is how I read the request. I have not seen the schema note itself. The six tables and their joins below come from your message.

Question: which stay tables exist, which keys join them and how many of each?
Outcome: a reader can see the six tables, the keys that tie them together and which tables sit on the guest side and which on the partner side.
Reader: the Roamstay product team, assumed. A reply naming another reader corrects it.

Settled by your message, six tables and six joins:
Guest makes Booking
Booking holds Payment
Room is reserved by Booking
Rate Plan prices Booking
Property offers Room
Property publishes Rate Plan

Booking carries one room key and one rate plan key, since it reserves one room under one rate plan.
Zones: Guest side holds Guest, Booking and Payment. Partner side holds Property, Room and Rate Plan, the three tables a property owns.

Assumed: each join reads as exactly one parent to zero or more children. A guest can have no booking yet and a booking can have no payment, as with a pay-at-property stay. The nullability and constraints in the schema note would settle it. Booking to Room and Booking to Rate Plan stay exactly one, as you stated.

Open:
Reading: you want the keys plus the few columns support asks about, but your message does not name those columns, and I do not guess fields.
Question: which columns does support ask about?
Recommended: keys only, a primary key on every table and a foreign key on each join, plus any columns you name in your reply.
Why: a guessed column would sit on the board as fact.

What the board must not do: become the full schema.
Recommended: no table beyond the six and no column outside the keys and your support columns. Every other column goes under `Left out:` in the reply.

Is this the right reading of the board?