`COMPOSED` clean: 9 nodes, 8 connectors, 48,435 characters (under the one-call limit), drawn in the shipped FigJam default design. Here's the gate:

```text
Question: which parts take part in Loomlist block sync and how do they connect?
Outcome: the Loomlist Engineering team can trace a block change from one client to the others and see which part owns each hop.
First glance: Sync Service, where every block change is written and published.
Second glance: the Change Stream handing each change on to the Push Worker.
Last glance: Apple Push Service, the external hop that wakes sleeping iOS devices.

Plan: Loomlist Engineering, as you named it. File: the existing FigJam file <test-file-key>.
It already holds earlier boards, including several titled "Block sync" and one "Loomlist block sync" — this write adds a new board beside them and touches nothing already there.
Writes: one composed board, 9 nodes and 8 connectors in 6 lanes, with a title, a key and a source line, at the Laptop reading distance.
Extensions: none.
Calls: one use_figma compose and one get_figjam read-back. The session is already open.
Rollback: delete the one board section the write returns, and only after a second yes from you.

Sketch (the checked model):
flowchart LR
    Clients: Desktop App, Web Client, iOS App --"Holds live socket"<--> API Gateway
    API Gateway --"Routes block sync"--> Sync Service
    Sync Service --"Writes block changes"--> Blocks Database
    Sync Service -."Publishes".-> Change Stream
    Change Stream -."Reads".-> Push Worker
    Push Worker -."Apple Push Service: Wakes iOS devices".-> Apple Push Service

Write it?
```

**Write it?**