The board will answer: **who handles a damaged-item claim, and where does the approved claim pass to the warehouse?** It will show the claim through refund release for CS and warehouse teams. The supplied runbook is the source. The second-photo return to CS review follows the existing section, as you confirmed.

**Target:** Fernhouse Product plan, existing FigJam file `<test-file-key>`  
**Section:** Fernhouse damage claim process  
**Contents:** 3 actor lanes, 10 nodes and 10 connectors  
**Highlight:** The approval step gets the pink focus accent, and its cross-lane connector is labeled “Handoff to warehouse queue”  
**Pilot:** The under-€20 pickup skip stays out of the current path and is labeled as not live  
**Open gap:** The runbook gives no outcome for an unsuccessful inspection  
**Planned extensions:** None  
**After approval:** 1 `use_figma` write, 1 `get_figjam` read-back and 1 screenshot review  
**Rollback target:** The new `Fernhouse damage claim process` section

```mermaid
%% type: process
%% title: Fernhouse damage claim process
%% subtitle: For CS and warehouse teams, follow a customer's photo report through review and refund release
%% source: Source: supplied support runbook. The second-photo route to CS review was confirmed by the requester. Left out: the under-€20 pickup skip, a pilot that is not live, and any failed-inspection outcome, which the runbook does not state.
flowchart LR
    subgraph customer ["Customer"]
        report([Report damage with photo via help form])
        sendSecond[/Send second photo/]
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

The focus check lands on approval beside the labeled warehouse handoff. The unclear-photo loop returns to CS review. Decision logging points to the claims table, while the inactive pilot stays out of the live flow.

May I add this section to the existing FigJam file?