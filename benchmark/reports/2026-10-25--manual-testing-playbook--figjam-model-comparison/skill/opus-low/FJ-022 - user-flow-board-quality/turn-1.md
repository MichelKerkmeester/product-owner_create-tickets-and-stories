This is the playback step. Nothing goes on a board until you confirm how I've read the request, and after that the write needs its own yes.

**What the board answers:** How does a Fernhouse customer start a return in the app, and what happens when the 30-day window has closed?
**Outcome:** One user-flow board that takes the customer from the order list to the QR confirmation. The Contact support exit and the proposed free pickup are both shown, and each is clearly marked.

**What your message settled** (you gave me a summary of the app and the returns doc, not the doc itself)
- Screens, in order: Order list, Order detail with a Start a return button, Return reasons list, then a choice between drop-off point and courier pickup, then Confirmation with a QR code
- Rule: returns are open for 30 days after delivery. After that the app shows Contact support
- Proposal under review: free courier pickup for orders over 100 euros. It goes on the board as a dashed note marked "Proposed, under review", not as a branch the app has today

**Outline**
1. Order list → Order detail
2. Order detail → decision: "Delivered 30 days ago or less?"
3. No → Contact support (failure end)
4. Yes → Start a return → Return reasons
5. Return reasons → decision: "Drop-off or pickup?"
6. Drop-off point → Confirmation with QR
7. Courier pickup → Confirmation with QR (goal end, accented). The proposal note is attached to this step

**Framings:** I recommend a happy path running left to right, with the Contact support exit off to the side, because it answers "how do I start a return" at a glance. The alternative is a state map of every exit. It is more complete, but it adds states the sources don't give me.

**What I've assumed (correct any of these)**
- **Where the window check happens.** I placed it at Order detail, with Contact support shown instead of the button. The sources don't say exactly where the app checks it
- **Whether both options lead to the same screen.** I've drawn drop-off and pickup reaching one QR confirmation. A courier pickup might really show a booking slot instead of a QR code
- **Reasons.** The reasons are drawn as a single list step, because none were supplied
- **Title and audience.** Title: "Fernhouse: starting a return in the app". Audience: product team, step-level detail, no zones

**Open before the write gate (not a question yet)**
- **Target file.** The file `<test-file-key>` wasn't written by this work, and a FigJam file has only one page. Writing there means adding to someone else's board, so I'll confirm what's already on it before suggesting it at the gate
- **Plan.** You said "Fernhouse Product plan" for the board and "Barter team plan, drafts, no project" if a new file is needed. I'll check which plans your account holds and settle this at the gate

Does this reading match the app, especially the window check sitting at Order detail and both options ending on the QR confirmation?