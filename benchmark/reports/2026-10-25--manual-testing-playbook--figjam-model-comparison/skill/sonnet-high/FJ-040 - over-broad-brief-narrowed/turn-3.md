Nothing is written yet. All three diagrams pass `flow_check.py` and compose, and the write waits for your yes at this gate.

**Two changes from the playback**
- Warehouse now has 10 nodes, not 11. I merged "Order paid" and "send to the warehouse system" into one start node, because the longest path was 9 steps and the limit is 8.
- The lanes follow the order work first reaches them. On Warehouse that makes shipping-service sit before Warehouse.

**The checked model**

```mermaid
%% type: process
flowchart LR
    %% title: 1. Returns
    %% subtitle: Who handles a return, from the customer's contact to the refund, with 30 days from delivery and 6 days on average to refund
    %% source: Source: Fernhouse company context, key flow 6, updated 2026-09-18. Left out: outside the window, a failed item check, the self-serve return that does not exist yet.
    subgraph customer ["Customer"]
        ask([Contact CS about a return])
        sendBack["Send the item back (assumed)"]
    end
    subgraph csAgent ["CS agent"]
        create[Create the return in Admin]
        label[Email the return label]
        handoff([Refund needed])
    end
    subgraph whOp ["Warehouse operator"]
        check[Check the item]
    end
    ask --> create
    create --> label
    label --> sendBack
    sendBack --> check
    check --> handoff
    style customer fill:#F5F5F5,stroke:#B3B3B3
    style csAgent fill:#F5F5F5,stroke:#B3B3B3
    style whOp fill:#F5F5F5,stroke:#B3B3B3
    style create fill:#FFC2EC,stroke:#F849C1
```

```mermaid
%% type: process
flowchart LR
    %% title: 2. Refunds
    %% subtitle: Who approves a refund, from the moment one is needed to the refund issued, with a CS lead above €200 per order
    %% source: Source: Fernhouse company context, roles and key flow 6, updated 2026-09-18. Left out: who issues the refund after approval, a decline, how the money reaches the customer, the refund email.
    subgraph csAgent ["CS agent"]
        need([Refund needed])
        limit{Over €200 per order?}
        issue[Issue the refund]
        done([Refund issued])
    end
    subgraph csLead ["CS lead"]
        approve[Approve the refund]
    end
    need --> limit
    limit -->|No| issue
    limit -->|Yes| approve
    approve --> done
    issue --> done
    style csAgent fill:#F5F5F5,stroke:#B3B3B3
    style csLead fill:#F5F5F5,stroke:#B3B3B3
    style limit fill:#FFC2EC,stroke:#F849C1
```

```mermaid
%% type: process
flowchart LR
    %% title: 3. Warehouse
    %% subtitle: How a paid order leaves the warehouse, by parcel carrier collection or by pallet booking
    %% source: Source: Fernhouse company context, key flow 4 and constraints, updated 2026-09-18, and the label API notes of 2026-09-11. Left out: label failures and the proposed webhook fixes, orders paid after 15:00, mixed parcel and pallet orders, picking of pallet items.
    subgraph orders ["orders-service"]
        paid(["Paid order sent to the warehouse system"])
    end
    subgraph ship ["shipping-service"]
        split{Parcel or pallet item?}
        ask[Ask for a label per parcel]
        got[Receive the label by webhook]
        book["Send the daily booking file at 16:00"]
    end
    subgraph wh ["Warehouse"]
        pick[Start picking]
        pack[Pack and label the parcel]
    end
    subgraph parcelCar ["Parcel carrier"]
        build[Build the label]
        collect(["Collect at 18:00 if paid before 15:00"])
    end
    subgraph palletCar ["Pallet carrier"]
        slot([Call the customer to book a slot])
    end
    paid --> split
    split -->|Parcel| pick
    split -->|Pallet| book
    pick --> ask
    ask --> build
    build -->|Webhook| got
    got --> pack
    pack -->|Packed| collect
    book --> slot
    style orders fill:#F5F5F5,stroke:#B3B3B3
    style ship fill:#F5F5F5,stroke:#B3B3B3
    style wh fill:#F5F5F5,stroke:#B3B3B3
    style parcelCar fill:#F5F5F5,stroke:#B3B3B3
    style palletCar fill:#F5F5F5,stroke:#B3B3B3
    style collect fill:#CDF4D3,stroke:#66D575
```

**Question:** who does what in each Fernhouse area, and which service owns each step?
**Outcome:** a reader can see who owns each step and where work changes hands before writing a ticket.

**Glances**
- Returns
  - First: Create the return in Admin, because every return waits on an agent today.
  - Second: Check the item, where the warehouse hands back to CS.
  - Last: the Refund needed end, which leads into board 2.
- Refunds
  - First: the "Over €200 per order?" decision.
  - Second: Approve the refund, the CS lead step.
  - Last: Refund issued.
- Warehouse
  - First: Collect at 18:00 if paid before 15:00.
  - Second: the "Parcel or pallet item?" split.
  - Last: Call the customer to book a slot, the pallet end, which no source gives tracking for.

**Target:** file `<draft-file-key>`, as three new sections placed 400 pixels right of what the file holds. Nothing already on it changes.
- A named file needs no `create_new_file` and no plan, so neither the Fernhouse Product plan nor the Barter team plan is used.
- If the file can't be opened, I stop and ask, because your two plan instructions conflict.

**Writes:** three composed boards in the order Returns, Refunds, Warehouse, at laptop distance with balanced detail.
- Returns has 6 nodes, 5 connectors and 3 lanes.
- Refunds has 5 nodes, 5 connectors, 2 lanes and 2 labelled exits.
- Warehouse has 10 nodes, 9 connectors, 5 lanes and 2 labelled exits.
- Each board has a title, a key and a source line.

**Extensions:** none.

**Calls:** `create_session`, one `get_figjam` read of the file before the write, three `use_figma` composes and one `get_figjam` read-back, six in all. On a Starter plan or a View or Collab seat, Figma allows six tool calls a month, and read tools count. This write would use the whole allowance.

**Rollback:** delete the three board sections the write returns, found by their tags. I do this only on a yes to a question that names them.

Do you want me to write these three boards to file `<draft-file-key>`?