Question: which parts take part in block sync and how do they connect?
Outcome: Loomlist Engineering can tell which part to open for a problem with writes, delivery or wake-ups.
First glance: sync-service, where every block change is written and published.
Second glance: the API gateway, the Change stream and the Push worker. The gateway is where a client's change enters, and the stream and worker carry it on.
Last glance: Apple push, the external hop that wakes a sleeping iOS device.

Sketch, the checked model as it printed:

```text
%% type: architecture
flowchart LR
    %% title: Block sync
    %% subtitle: How a block change travels from a client to the other devices, ending in an iOS wake-up, for Loomlist Engineering
    %% source: Sources: the platform doc as relayed in the request. Left out: file storage, no call to or from it is stated.
    %% level: balanced
    %% focus: sync because every change is written here
    %% detail: api | Checks the session token | Keeps each client socket open
    %% detail: sync | Merges edits to the same block
    %% detail: blocks | Keeps 30 days of block history
    %% detail: changes | Keeps events for 7 days
    %% detail: push | At most one wake-up per device per minute
    subgraph client ["Clients"]
        desktop[Desktop client]
        webClient[Web client]
        ios[iOS client]
    end
    subgraph gateway ["Edge"]
        api[API gateway]
    end
    subgraph service ["Services"]
        sync[sync-service]
        push[Push worker]
    end
    subgraph datastore ["Stores"]
        blocks[Blocks database]
    end
    subgraph async ["Events"]
        changes[Change stream]
    end
    subgraph external ["External"]
        apns[Apple push]
    end
    desktop <-->|"Live socket"| api
    webClient <-->|"Live socket"| api
    ios <-->|"Live socket"| api
    api -->|"Routes sync requests"| sync
    sync -->|"Writes blocks"| blocks
    sync -.->|"Publishes changes"| changes
    changes -.->|"Feeds events"| push
    push -.->|"Apple push: Wakes device"| apns

  diagram 1, architecture: ok, 9 nodes and 8 connectors, widest rank 3 steps, longest path 6 steps, 0.9 connectors per step, labels average 12 characters, 0 crossing pairs
PASSED 1 diagram(s) in model.md
```

Eye first: sync-service, and it is the node the board most needs read, since it is the only part that both writes and publishes.
Reads second: the API gateway and the Change stream, which show how a change enters and how it leaves.
Could miss: Apple push in the External lane. Missing it would hide how a sleeping iOS device hears of a change.
Remove next: the Web client, kept because it is one of the three clients you named.

Plan: Loomlist Engineering. I read the file once, and it is empty, so no section shares the title `Block sync`.
File: the existing `<test-file-key>`. The board goes in as a new section, and no new file is created.
Writes: one composed board of 9 nodes and 8 connectors in 6 lanes, with a title, a key and a source line, at Laptop distance. The label `Apple push` replaces `Apple's push service`, because FigJam would strand the word "service" alone on a last line.
Left out: file storage, no source states a call to or from it.
Extensions: none.
Calls: one `use_figma` and one `get_figjam` read-back, after the `create_session` and `get_figjam` calls already made.
Rollback: delete the one board section the write returns.

Write it?