`PASSED`: 9 nodes, 9 connectors, widest rank 2, longest path 7, 0 crossing pairs — inside the user-flow budget.

Quality pass against the rubric:
- **Type fit**: a user flow answers "which screens, where do they choose"; no list or table does that better at 9 nodes.
- **Remove test**: the merge dot from the first draft is already cut — both methods lead straight to the confirmation. Every remaining node is a screen the source names, a decision the reader chooses at, or an exit the 30-day rule needs.
- **Signal**: one `style` line on the goal; three zones cover all 9 nodes; labels use the app's own words.
- **Provenance**: every node is current behavior from the app screens or the returns doc. The €100 free pickup is a proposal under review, so it is left out and named in the source line — never drawn as current. The context doc's "no self-serve return" line stays a finding, as you confirmed.

Gate — this asks about the write alone:

```text
Question: which screens does a customer pass through to start a return in the app, and where do they choose?
Outcome: a reader can follow a return from the order list to a confirmed return with its QR code, and see where the 30 day window ends it.

First glance: the confirmed return with its QR code, the goal the flow reaches.
Second glance: the drop-off or courier pickup choice that leads to it.
Last glance: Contact support, the exit after the 30 day window.

The checked model:

flowchart LR
    %% title: Start a return
    %% subtitle: How a Fernhouse customer starts a return in the app, from the order list to a confirmed return
    %% source: Sources: the app screens and the returns doc. Left out: a free pickup over 100 euros, a proposal under review.
    %% zone: Find the order: orders, detail
    %% zone: Request the return: window, support, reason, method, dropoff, pickup
    %% zone: Done: confirmed
    orders([Order list]) --> detail[Order detail]
    detail --> window{Within 30 days?}
    window -->|No| support([Contact support])
    window -->|Yes| reason[Pick a reason]
    reason --> method{Drop-off or pickup?}
    method -->|Drop-off| dropoff[Choose a drop-off point]
    method -->|Pickup| pickup[Book a courier pickup]
    dropoff --> confirmed([Confirmation with QR code])
    pickup --> confirmed
    style confirmed fill:#CDF4D3,stroke:#66D575

flow_check: PASSED, 9 nodes and 9 connectors, 0 crossing pairs.

Plan: Fernhouse Product. File: the existing FigJam file <test-file-key>. The board lands as a new framed section 400 px to the right of any content already on the page.
Writes: one composed board, 9 nodes and 9 connectors in three zones, with a title, a key and a source line, at Laptop reading distance.
Extensions: none.
Calls: create_session, one get_figjam baseline read of the file, one use_figma and one get_figjam read-back.
Rollback: delete the one board section the write returns, on its own yes afterwards.

Write it?
```