The read-back contains all 10 nodes and 10 connectors. The screenshot shows the “Send second photo” label clipped.

Flow Mode requires a new yes before rewriting after a screenshot finding. I’ve prepared a checked model with that label shortened to “Send new photo.” Adding it creates a corrected section; I’ll read it back, then ask separately whether to remove the first version, section `168:6021`.

**Target:** Fernhouse Product plan, existing FigJam file `<test-file-key>`  
**Correction:** Add the model below as a corrected section  
**Planned extensions:** None  
**After approval:** One `use_figma` write and one `get_figjam` read-back  
**Rollback target:** The corrected section

```mermaid
%% type: process
%% title: Fernhouse damage claim process
%% subtitle: For CS and warehouse teams, follow a customer's photo report through review and refund release
%% source: Source: supplied support runbook. The second-photo route to CS review was confirmed by the requester. Left out: the under-€20 pickup skip, a pilot that is not live, and any failed-inspection outcome, which the runbook does not state.
flowchart LR
    subgraph customer ["Customer"]
        report([Report damage with photo via help form])
        sendSecond[/Send new photo/]
    end
    subgraph cs ["CS agent"]
        photoClear{Damage clear in photo?}
        approve[Approve clear damage on the spot]
        request[Request a second photo]
        claims[(Claims table)]
    end
    subgraph warehouse ["Warehouse operator"]
        queue[(Warehouse queue)]
        book[Book a courier pickup]
        inspect[Inspect item on arrival]
        refund([Release the refund])
    end
    report --> photoClear
    photoClear -->|Clear| approve
    photoClear -->|Unclear| request
    photoClear -->|Log every decision| claims
    request --> sendSecond
    sendSecond --> photoClear
    approve -->|Handoff to warehouse queue| queue
    queue --> book
    book --> inspect
    inspect --> refund
    style approve fill:#FFC2EC,stroke:#F849C1
```

May I add this corrected section to the existing FigJam file?