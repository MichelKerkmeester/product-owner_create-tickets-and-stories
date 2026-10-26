The check passed. Here is the sketch and the gate. The file's page is empty, so no section shares the title "Damaged-item refund".

```text
%% type: process
flowchart LR
    subgraph customer ["Customer"]
        contact([Contacts CS about the damage])
    end
    subgraph cs ["CS agent"]
        create[Create return, email label]
        refund([Refund issued])
    end
    subgraph warehouse ["Warehouse operator"]
        check[Check the returned item]
    end
    contact --> create
    create -->|Channel not stated| check
    check -->|Channel not stated| refund
    style create fill:#FFC2EC,stroke:#F849C1
```

Check: `PASSED`, 4 nodes and 3 connectors, 0 crossing pairs, composed with the default design.

**Question:** who handles a damaged-item refund at Fernhouse, and where does the claim change hands between the customer, the CS agent and the warehouse operator?

**Outcome:** Post-purchase and CS leads can see which lane owns each step and where the claim crosses to the warehouse.

**First glance:** "Create return, email label", the CS step that hands the claim to the warehouse, drawn light pink with the pink outline.

**Second glance:** "Check the returned item", where the claim lands in the warehouse lane.

**Last glance:** the two "Channel not stated" labels and the source line, which keep the gaps visible without competing for attention.

**File:** existing FigJam file `<draft-file-key>`. You placed it in Fernhouse Product, and I haven't verified the plan. The board goes in as a new section, and nothing already on the file changes. No new file is created.

**Writes:** one composed board with 3 lanes, 4 nodes and 3 connectors, plus a title, a subtitle, a key and a source line, at Laptop distance.

**Extensions:** none.

**Calls:** one `use_figma` and one `get_figjam` read-back. I've already spent `create_session` and one `get_figjam` read. A Starter plan or a View or Collab seat allows six tool calls a month, so tell me if that applies.

**Rollback:** I delete the one board section the write returns, and only after you say yes to a question that names it.

Shall I write this board to that file?