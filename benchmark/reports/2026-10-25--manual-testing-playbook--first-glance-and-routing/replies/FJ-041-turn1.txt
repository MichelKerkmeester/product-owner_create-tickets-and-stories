Nothing is written yet. Before I draw, I need two answers: which diagram type you want, and who the board is for. Here is what I've settled so far.

**What I've settled**

* Entry: the customer opens an order (from your message)
* Exit: the customer sees a confirmation (from your message)
* Actor: the customer, with no CS agent or warehouse step (from your message)
* Choices: the reason, then refund or store credit (from your message)
* Source class: proposal. `fernhouse-context.md` says there is no self-serve return today. The customer contacts CS, an agent creates the return in Admin, and the warehouse checks the item. I'll mark the board "Proposed" so it doesn't read as current behavior.
* Target: the existing file `<test-file-key>`, as a new board section on its page. I won't create a file, so no plan lookup is needed.

**Questions**

1. **Type**
   * Reading: you asked for a state diagram, but the steps you listed are taps and screens. That describes a path through screens, and a state diagram answers a different question (which states exist and what moves the thing between them).
   * Question: should I draw a user flow or a state diagram?
   * Recommended: a user flow, because every step you named is a screen and a choice.
   * Why: a state diagram only fits if the screens count as states and the taps as events. That is possible, but it reads as a user flow with state labels.
   * If you keep the state diagram, the states would be Order open, Return started, Reason chosen, Resolution chosen and Confirmed.

2. **Reader and outcome**
   * Reading: your message names no reader.
   * Question: who reads this board, and what do they decide after it?
   * Recommended: the Post-purchase team and design, to agree the customer's path before a story is written.
   * Why: Post-purchase owns orders, refunds and returns. If you don't answer, this stands as assumed and I'll name it again before the write.

3. **What the board must not do**
   * Reading: the context file holds a 30-day return window, and a refund currently takes 6 days on average.
   * Question: should the board stay on the customer's path only?
   * Recommended: yes. The board would leave out the 30-day eligibility check, the CS and Admin steps, the refund payout and any failure path. All four would be named on a `Left out:` line.
   * Why: you listed seven steps and no branches beyond the two resolutions.

Once you answer, I'll send one playback of the settled rows. After that comes the write gate, which names the file, the calls it will spend and the rollback. The board is only written after your yes to that gate.