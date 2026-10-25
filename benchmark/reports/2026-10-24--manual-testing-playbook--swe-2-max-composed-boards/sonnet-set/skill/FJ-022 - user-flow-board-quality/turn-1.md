Nothing is written to the board yet. Here is what I've settled so far, with three questions before I build the model.

**Settled**
* Question: which screens does a customer pass through to start a return, and where do they choose? That makes it a user flow
* Entry is the order list. Exits are the confirmation with QR code and Contact support
* Decisions are the 30-day window and drop-off point versus courier pickup. Both are current behavior from the app and the returns doc
* The free pickup for orders over €100 is a proposal under review. It stays off the flow and is named on the board's source line
* Target is your existing file `<test-file-key>`. The new board goes beside what is already there, with no new file and no new page. You named the Fernhouse Product plan. I haven't verified it, because a board keeps the plan its file was created in

**Question 1: source conflict**
* Reading: `context/fernhouse-context.md` (updated 2026-09-18) says "There is no self-serve return today". Customers contact CS, and an agent creates the return in Admin. Your app screens show a self-serve flow
* Question: is the Start a return flow live in the app today?
* Recommended: treat the app and the returns doc as governing, and mark that assumed
* Why: you read them directly, and the note is five weeks old. If the screens are not shipped yet, the board must say proposed, so I need to know

**Question 2: reader and outcome**
* Reading: no source names who reads the board
* Question: who is it for, and what should they be able to do afterwards?
* Recommended: Fernhouse product and CS, who can then see the full customer path and where the 30-day cut-off sends someone to Contact support
* Why: CS handles return requests today, and the returns doc is internal

**Question 3: what the board must not do**
* Reading: you named five screens and one time rule
* Question: what should the board refuse to show?
* Recommended: no CS or Admin steps, no free-pickup proposal and no screen between the method choice and the confirmation
* Why: none of your sources show those screens, and a drawn guess would read as current behavior

**Assumed for now**
* The returns doc doesn't say which screen shows Contact support after 30 days. I'd put the window check right after Order detail. I'll confirm this in the next round with entry, exit and actors

If you skip a question, I'll go with the recommended answer and name it in the write gate. That gate lists the file, the calls (`create_session`, `use_figma`, `get_figjam` read-back) and the rollback. I'll write only after your yes there.