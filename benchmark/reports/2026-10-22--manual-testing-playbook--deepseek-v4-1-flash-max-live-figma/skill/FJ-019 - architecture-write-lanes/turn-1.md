The model is checked and passes. I have not written it, because the destination you named is not in the account.

### What it answers

Which parts take part in block sync and how they connect. Not the order of one sync, which is a sequence.

### The model

Clients: Desktop App, Web Client, iOS App. Edge: API Gateway. Services: Sync Service, Push Worker. Stores: Blocks DB. Events: Change Stream. External: Apple Push.

Desktop and Web hold a live socket to the gateway, iOS syncs over HTTPS, so the gateway is the one way in. It routes to Sync Service, which writes the block to Blocks DB and publishes the change to Change Stream. Push Worker reads the stream and calls Apple Push to wake a sleeping device.

Nine nodes, six lanes, eight connectors, no crossing pairs in the check.

### File storage is out

You listed it and the board leaves it out, for two reasons that agree. No source states a call from Sync Service to file storage, so placing it means inventing that call. And the architecture layout takes nine nodes, which the rest of your list already fills. I can draw a second diagram for media blocks beside it if you want file storage shown.

### The calls are my reading

The parts came from you. The connectors did not, so I read them from what each part does. Three carry the point: sync writes the block, sync publishes to the stream, the worker calls Apple. Correct any before I draw.

### The plan

`whoami` returns three plans, and none is Loomlist Engineering.

- <figma-plan-3>, View seat on Starter
- <figma-plan-1>, Full seat on Pro
- <figma-plan-2>, Full seat on Pro

<figma-plan-1> is the recommendation. A View seat cannot hold a board you will edit, and that plan's Starter allowance is six Figma tool calls a month.

### The gate

- File: a new FigJam file, created by the first call
- Write: one architecture named "Block sync", nine nodes and eight connectors across six lanes, with the architecture layout code, then one title text node above it
- Extensions: none
- Read calls: one `get_figjam` read-back and one screenshot
- Rollback: delete the new file

Which plan owns the board, and do I write it?