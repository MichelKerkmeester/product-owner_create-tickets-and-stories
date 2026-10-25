Check and composition both pass (9 nodes, 8 connectors, 0 crossing pairs, 39,282 chars — under the one-call cap). Quality rubric walked; now the write gate.

**Gate.**

*   Question the board answers: which parts carry a Loomlist block change, and how do they connect?
*   Outcome: an engineer can trace a change from any client, through the gateway and sync-service, to the blocks database, the change stream and the push path that wakes a sleeping iOS device

Glance lines:

*   First glance: Sync Service, the hub every change passes through
*   Second glance: the async push path, Change Stream to Push Worker to Apple Push, which is how a sleeping device still gets the change
*   Last glance: the key and the source line, which name the lanes and the file-storage cut

The write:

*   File: the existing FigJam file `<test-file-key>` — the account holds no plan named "Loomlist Engineering", so the board lands in whatever plan already owns this file; say so now if the file is wrong
*   Writes: one composed board "Loomlist block sync", 9 nodes and 8 connectors in 6 lanes, with title, subtitle, key and source line, placed right of the existing boards. iOS reads as HTTPS to the gateway, since the described wake path presumes a sleeping device holds no socket; Desktop and Web hold the live socket
*   Extensions: none
*   Calls: one `use_figma` write and one `get_figjam` read-back
*   Rollback: delete the one board section the write returns, through `use_figma`, and only after you say yes to the deletion

Write it?