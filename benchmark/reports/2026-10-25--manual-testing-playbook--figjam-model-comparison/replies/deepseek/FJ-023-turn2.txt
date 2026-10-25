**Question:** who does what in a damaged-item refund, and where does the claim change hands?

**Outcome:** a reader can see which team owns each step, and where the claim moves from CS to the warehouse.

**First glance:** Book a courier pickup, the step where the claim lands in the warehouse lane
**Second glance:** Damage clear?, the check that decides whether the claim moves on
**Last glance:** the claims table, where every decision is logged

**Plan:** Fernhouse Product. **File:** the existing FigJam file `<test-file-key>`, with the board added as a new section.

**Existing:** that file already holds a section titled "Damaged-item refund" from an earlier board. The new board lands to its right, and that section stays as it is. Removing it would be a separate request.

**Writes:** one composed board, 3 lanes, 8 nodes and 8 connectors, with a title, a key and a source line, at the Laptop reading distance.

**Extensions:** none.

**Calls:** one `use_figma` to compose the board and one `get_figjam` to read it back. The session and the first file read are already spent.

**Rollback:** delete the board section this write returns, and only if you say yes to that deletion separately.

The checked sketch:

```mermaid
%% type: process
flowchart LR
    %% title: Damaged-item refund
    %% subtitle: Who handles a damaged-item claim, from the customer's report to the released refund
    %% source: Source: the support runbook. Left out: pickup skipped under 20 euros, a pilot that is not live.
    subgraph customer ["Customer"]
        report([Report damage with a photo])
        photo[/Send a second photo/]
    end
    subgraph cs ["CS agent"]
        check{Damage clear?}
        approve[Approve the claim]
        log[(Claims table)]
    end
    subgraph warehouse ["Warehouse operator"]
        pickup[Book a courier pickup]
        inspect[Inspect the item]
        refund([Refund released])
    end
    report -->|"Help form"| check
    check -->|Unclear| photo
    photo --> check
    check -->|Clear| approve
    approve -->|"Claim queued"| pickup
    check -.->|"Decision logged"| log
    pickup --> inspect
    inspect --> refund
    style customer fill:#F5F5F5,stroke:#B3B3B3
    style cs fill:#F5F5F5,stroke:#B3B3B3
    style warehouse fill:#F5F5F5,stroke:#B3B3B3
    style pickup fill:#C2E5FF,stroke:#3DADFF
```

Write it?