Nothing is written yet. The model passed `flow_check.py` (4 states, 6 transitions) and composed cleanly. Here is my reading of the request, followed by the write gate.

**Playback**
* **Question:** which states does a customer pass through when starting a return from an order, and what moves them on?
* **Type:** state diagram, as you asked. The states are the screens the customer lands on, and each move is the tap or choice that triggers it
* **Entry and exit:** opens an order, and ends when the confirmation is shown
* **Decision:** refund or store credit, drawn as two labelled moves into the same confirmation
* **Reader (assumed):** Post-purchase and Storefront, agreeing the flow before stories are written. Say so if the audience is different
* **Status (assumed):** proposed, not live. Fernhouse context says there is no self-serve return today, since CS creates returns in Admin. The subtitle says "proposed self-serve flow". Tell me if it is approved direction and I will change the subtitle
* **Sources:** your request, class unknown, and the company context for the status check
* **Glances:** first, the refund or store credit choice. Second, the reason step before it. Last, the confirmation end state. A state diagram takes no accent colour, so the composer colours it by role

**Left out:** back and cancel moves, because the request states none. The reason list, refund timing and the 30-day return window are also left out, because the request doesn't mention them

**Gate**
```text
Plan: Fernhouse Product, as you named it. The file is existing, so the write sets no plan.
File: <test-file-key>, an existing file, not a new one.
Writes: one new board section, "Fernhouse return flow", placed 400 px right of existing content. It holds 4 states and 6 transitions, with a title, a key and a source line. Nothing existing is touched.
Calls: create_session, one use_figma, one get_figjam read-back, and get_screenshot if a node needs its own view. A Starter plan or View/Collab seat allows six Figma tool calls a month.
Rollback: delete the one board section the write returns, after your separate yes.
```

If the file turns out not to be a FigJam board, the write stops and I report back.

Write it?