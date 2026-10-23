No board yet. An architecture can only be drawn through Figma's hosted MCP, whose `generate_diagram` tool takes the model, and this session has no Figma MCP connection. The only MCP server wired is code_mode, whose figma manual runs Framelink's reader and carries no `generate_diagram`. The installed figma-ds-cli 1.2.0 does have an `fj` group, but it only draws shapes and connectors, with no layout verb, so it cannot draw an architecture, and its daemon is not answering (`fj info` fails). Connecting Figma's hosted MCP at https://mcp.figma.com/mcp, through Figma's plugin or this client's connector, is what unblocks the write.

The files stop short as well. They name the services and what each owns. They name no gateway, no store and no event stream, and state one service-to-service path. Figma's architecture layout accepts no device-to-service connector and needs every service to hold a way in and a way out, so a model built from the files alone fails the pre-write check: three services come back with no way in or no way out. Filling that gap with an invented gateway or store is the one thing the type forbids.

What the files settle:

- A sync session is one exchange between a device and sync-service: the device uploads changed blocks then pulls newer ones
- sync-service resolves conflicts by block-level last-writer-wins on protocol v3, and the replaced version is written nowhere, page history included
- pages-service is the only service other services read block data through, and it owns page history
- share-service answers every page access question, though no file names sync-service among its callers, so that edge would be inferred
- The four surfaces are Desktop, Web, iOS and Android. Offline reading and editing are briefed for Q1 2027, and the conflict choice is undecided, owned by Joana with a decision on 2026-10-09

Three questions settle the brief.

Reading: the files give no edge layer, and a device cannot be drawn reaching a service directly.
Question: What does a device's sync session reach first?
Recommended: One API gateway in front of the services.
Why: Without it the board cannot show a device reaching sync-service, and a gateway is the only lane the layout allows between them.

Reading: no store is named for blocks, and none for device cursors. pages-service reads and writes blocks but has no stated outbound call, which the check refuses.
Question: Which stores sit behind pages-service and sync-service?
Recommended: A blocks store under pages-service and a cursor store under sync-service, named from the sync engineering doc if one exists.
Why: A service with no way out fails the check, so the sync path would stop at pages-service.

Reading: the request names no reader. The decision trail points at the Sync team.
Question: Who reads this board, and what do they decide after it?
Recommended: The Sync team at the offline-mode kickoff, deciding where conflict handling has to change, with protocol v3 as the current behavior and options A, B and C kept off the board.
Why: The reader sets labels and detail, and the options are proposals with no decision, so drawing them as current would overstate what ships.

Answer those or accept the recommendations and I will send the node and edge list for a yes before anything is drawn, with a table of the sync path as the fallback if the board stays blocked.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.