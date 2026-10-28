Before I draw anything, this is how I read the request. Nothing is written to the board yet.

Question: which screens does a Fernhouse customer pass through to start a return in the app, and where do they choose? That is a user flow.

Outcome: a reader can follow a return from the order list to a confirmed return and see where the 30 day window ends it.

Destination: your existing file `<draft-file-key>`, as a new board section beside what it already holds. The request says both "new board" and "existing file". I read the existing file as the one that governs, so no new file is created.

Settled by the sources: the five screens in the order you listed them (order list, order detail with Start a return, return reasons, drop-off point or courier pickup, confirmation with a QR code) and the 30 day window with Contact support after it, all as current behavior. No screenshots or doc came with the request, so this rests on your description. Only "Start a return" and "Contact support" are your exact words, and the other labels are my wording from your description.

Left out: the free pickup over 100 euros, a proposal under review. Also any screen between the method choice and the confirmation, such as a drop-off map or a pickup slot, because nothing you gave describes one.

Assumed:
* The reader is the Fernhouse product team (you settle it by naming the reader)
* The window check sits on the order detail, so Contact support is its No exit and Pick a reason its Yes exit (you settle it by saying which screen shows Contact support)
* Balanced detail, mixed audience and laptop distance

Outline: Order list to Order detail to Within 30 days of delivery?, which exits to Contact support on No and to Pick a reason on Yes. Pick a reason leads to Drop-off or courier pickup?, whose two exits both reach Return confirmed with QR code. That is 7 screens and 7 connectors.

Framing: I recommend the happy path with the Contact support exit beside it, over a map of every exit, because the question is how a return starts and your sources describe one exit.

Look: left to right in three zones (Find the order, Request the return, Done). The 30 day decision takes the accent because it is where a return can end early, and the confirmation is the goal.

Still open: the Fernhouse context note (`context/fernhouse-context.md`, updated 2026-09-18) says there is no self-serve return today and that customers contact CS, who creates the return in Admin. That contradicts an in-app Start a return flow. I recommend the app and the returns doc govern, because you named them as the sources and the note is six weeks old. If the flow is not in a released app yet, tell me and the board will carry it as approved direction instead.

Is this the right reading of the board, with the app and the returns doc governing over the older context note?