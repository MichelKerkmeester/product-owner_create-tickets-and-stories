Before I draw anything, this is how I read the request.

**Question:** which parts sit behind block sync and how do they connect?
**Type:** architecture. A sequence would show the order of one sync, which you did not ask for.
**Outcome:** a reader can follow one block change from a client through the gateway and sync-service to the change stream, and on to the push that wakes a sleeping iOS device.
**Settled by your request:** the parts, the live socket from each client to the gateway, sync-service writing every block change and publishing it to the change stream, and the push worker reading the stream and waking iOS devices.

**Assumed, so you can correct it:**
* Reader: Loomlist engineers. Nothing names the reader. I took the Loomlist Engineering plan as the hint, so parts keep your names, `sync-service` included. Detail is balanced and the reading distance is a laptop.
* Gateway to sync-service: your request never says the gateway calls sync-service. I draw it as "Routes sync requests", because the architecture type needs a gateway between a client and a service.
* Sync-service to blocks database: I read "writes every block change" as writes to the blocks database.
* Must not do: draw any part or call you did not name.

**Still open, with a default:**
* File storage: you list it as a part, but nothing says which part reads or writes it, and I will not invent a call. Default: leave it off and name it under `Left out`. That also keeps the board at 9 nodes, the architecture budget, where ten would be over. If you tell me which part uses it, I will draw it and split the board into a sync path and a push path.
* The wake hop: Apple's push service reaching the iOS app cannot be drawn. The type has no edge from an outside system to a client, and it would close a loop. The label on the push worker's edge says "Wakes iOS device", and `Left out` names the return hop.
* iOS socket: I draw all three clients with a live socket, as you wrote it. A sleeping iOS device has none, which is why the push exists.

**Where it goes:** into the existing file `<draft-file-key>` as a new section, with nothing already on it changed. I can't check which plan owns that file, because `whoami` lists the plans an account holds and not who owns a file. I am reading it as Loomlist Engineering. I would create a new file in the Barter team plan, in drafts with no project, only if that file can't take the write, and I would ask first.

Is this the right reading of the board?