I haven't written anything to the board. The repo has no real damaged-item source, so this is my reading of the request for you to confirm.

**Question:** who handles a damaged-item claim at Fernhouse, and where does it change hands?
**Outcome:** a reader can see which team owns each step, from the customer's contact to the refund.
**Type:** process with three lanes (Customer, CS agent, Warehouse operator). I'd pick this over a user flow because `fernhouse-context.md` says there is no self-serve return, so the customer has no screens to walk through.

**Settled by the sources**
- `context/fernhouse-context.md`, key flow 6 (current behavior), gives the return path:
  - The customer contacts CS.
  - A CS agent creates the return in Admin and emails a return label.
  - The warehouse checks the item.
  - The agent refunds.
- The same file gives the 30-day return window from delivery.
- It also gives the refund limit: a CS agent can refund up to €200, and a CS lead approves anything above.
- `context/fernhouse-carrier-tracking-api-facts.md` shows the carrier can report `DAMAGED` as an `EX` exception code. It says nothing about what happens after.

**Left out**
- The damaged-item runbook in `sk-create-figjam/assets/examples/process-fernhouse-refund.md` (photo check, second photo, courier pickup). That file says every step in it is invented for the example, so drawing it would show made-up steps as current behavior.
- Anything about damage in transit versus damage found on arrival. No source separates them.

**Assumed**
- Balanced detail, mixed audience, Laptop reading distance.
- The board follows the key flow 6 return path, with the damage report as the entry and the refund as the exit.
- The first glance is the CS agent's decision on the claim.
- The board gets no zones.

**Still open**
- Whether a damage claim needs a photo, whether a replacement is offered, and who decides.
- No source answers these, so each would be marked assumed on the board. If you have the real runbook or support macro, point me to it and I'll use that instead.

Is this the right reading? Reply "go on" to accept the assumptions as they stand. Next I'll run the check and send the write gate. The board is written only after your yes to that gate.