Question: who does what, and where does a damaged-item claim change hands?
Outcome: a reader can see which of the customer, CS and the warehouse owns each step of a damaged-item refund, and that the claim crosses from CS into the warehouse queue at the approval.
First glance: Approve the claim, the sending step of the handoff to the warehouse.
Second glance: Damage clear in the photo?, the decision beside it on its row, then Damage reported, the light blue entry. After that come Send the second photo, the loop back to the customer, the Claims table, the Warehouse queue, Book a courier, Inspect the item and Refund released, the goal. This is the order the check's Glance line prints.
Last glance: the key and the source line, since the goal comes last.

Sketch, the checked model in full:

```mermaid
%% type: process
flowchart LR
    %% title: Damaged-item refund
    %% subtitle: Who handles a damaged-item claim, from the customer's report to the released refund
    %% source: Source: the support runbook text. Left out: pickup skipped under 20 euros, a pilot that is not live. Every decision is logged in the claims table.
    subgraph customer ["Customer"]
        report([Damage reported])
        photo[/Send the second photo/]
    end
    subgraph cs ["CS agent"]
        check{Damage clear in the photo?}
        approve[Approve the claim]
        log[(Claims table)]
    end
    subgraph warehouse ["Warehouse operator"]
        queue[(Warehouse queue)]
        pickup[Book a courier]
        inspect[Inspect the item]
        refund([Refund released])
    end
    report --> check
    check -->|Unclear| photo
    photo --> check
    check -->|Clear| approve
    approve -->|"Handoff to warehouse"| queue
    approve -->|"Logs"| log
    queue --> pickup
    pickup --> inspect
    inspect --> refund
    style customer fill:#F5F5F5,stroke:#B3B3B3
    style cs fill:#F5F5F5,stroke:#B3B3B3
    style warehouse fill:#F5F5F5,stroke:#B3B3B3
    style approve fill:#FFE0C2,stroke:#FF9E42
```

```text
  diagram 1, process: ok, 9 nodes and 9 connectors, widest rank 2 steps, longest path 7 steps, 1.0 connectors per step, labels average 17 characters, 0 crossing pairs
Glance: Approve the claim (accent) > Damage clear in the photo? > Damage reported > Send the second photo > Claims table > Warehouse queue > Book a courier > Inspect the item > Refund released (goal)
PASSED 1 diagram(s) in model.md
```

The composer also printed COMPOSED for it: 9 nodes and 9 connectors to read back, 42,346 characters, which fits one `use_figma` call.

Eye first: Approve the claim, with the labelled "Handoff to warehouse" connector leaving it. That is the node and line the board most needs read.
Reads second: Damage clear in the photo? beside it, then the claim from Damage reported to Refund released, column by column across the lanes, which shows who holds the claim at each step.
Could miss: Send the second photo, the loop back to the customer, which would hide why some claims stall.
Remove next: the Claims table, kept because the runbook logs every decision there. It is drawn from the approval only, and the source line says the other decisions write to it too.

Plan: Fernhouse Product. File: <draft-file-key>, the existing file you named. I read it once and its page is empty, so no section shares this title and the title stays "Damaged-item refund".
Writes: one composed board section, 3 lanes, 9 nodes and 9 connectors, with a title, a key and a source line, at the Laptop reading distance. Nothing else on the file is touched.
Left out:
* The pickup skipped under 20 euros, a pilot that is not live and so a proposal
* An exit for damage that stays unclear after the second photo, and for an inspection that finds a problem, because the runbook text does not say what happens
Extensions: none.
Calls: one `use_figma` and one `get_figjam` read-back. Two more calls were already spent on the session and the file read. Figma limits a Starter plan and a View or Collab seat to six tool calls a month, so tell me if that applies to you. I will load Figma's `figma-use` and `figma-use-figjam` skills before the write.
Rollback: delete the one board section the write returns, which removes everything drawn inside it, and only on your yes to a question that names it.

Write it?