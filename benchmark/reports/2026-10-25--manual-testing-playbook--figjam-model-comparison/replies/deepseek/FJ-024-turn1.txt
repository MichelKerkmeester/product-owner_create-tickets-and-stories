Before I draw anything, this is how I read the request.

```
Question: which parts carry a block change from one Loomlist client to the others, and how do they connect?
Outcome: the engineering team can see where a block change is written, where it is published, and how a sleeping iOS device is woken.
Settled by the request: ten named parts and the calls between them. The desktop, web and iOS clients each hold a live socket to the gateway, sync-service writes every block change and publishes it to the change stream, and the push worker reads the stream and wakes sleeping iOS devices.
Assumed: balanced detail, a mixed audience so sync-service reads Sync Service, and the Laptop reading distance.
Left out: file storage. Nothing in the request puts it on the sync path, and ten parts is one over the nine node budget an architecture board holds.
Still open: none.
```

Is this the right reading of the board?