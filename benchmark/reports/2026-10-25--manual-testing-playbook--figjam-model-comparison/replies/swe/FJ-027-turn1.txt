Before I draw anything, this is how I read the request.

Question: which entities exist in the stays model, which fields join them and how do they relate?
Outcome: a reader can see the six stay tables, how they join and which sit on the guest side and which on the partner side.
Settled by the sources: the schema note gives the six tables, their keys and how they join, and the request asks for the partner tables apart from the guest tables. Guest Support ticket 58213 settles the columns support asks about: booking reference, check-in and check-out, booking and payment status, amount, refundable and payment option.
Left out: the note's other columns, which neither a join nor a support question cites.
Assumed: balanced detail and Laptop reading distance, so each table keeps its keys plus the support columns, with `email` and `country` on Guest, `name` and `city` on Property, and `name` and `capacity` on Room kept for identification. Two zones named Guest side and Partner side. And the board lands as a new board in existing file `<test-file-key>`, which already holds three earlier Stays model boards this write does not replace.
Still open: none.

Is this the right reading of the board?