Gate for the write. The model passed the check, and the file's page is empty, so no section shares the title and nothing already there can change.

The board answers: which services does a block change pass through, and what wakes a sleeping iOS device? A Loomlist engineer should be able to place a new service or find where a sync bug lives.

Glance lines:
- First glance: the change stream, where the write path turns into the wake path
- Second glance: sync-service, which feeds the stream
- Last glance: Apple's push service, which can wait

The sketch, exactly as the check read it:

```text
%% type: architecture
%% title: Loomlist block sync services
%% subtitle: From a block change on any client to a woken iOS device, for Loomlist engineers
%% source: Source: the sync services description. Left out: file storage, no caller stated.
%% focus: stream
flowchart LR
    subgraph client ["Clients"]
        desktop[Desktop client]
        web[Web client]
        ios[iOS client]
    end
    subgraph gateway ["Gateway"]
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
        stream[Change stream]
    end
    subgraph external ["Outside"]
        apns["Apple's push service"]
    end
    desktop <-->|"Live socket"| api
    web <-->|"Live socket"| api
    ios <-->|"Live socket"| api
    api -->|"Routes block changes"| sync
    sync -->|"Writes blocks"| blocks
    sync -.->|"Produces block changes"| stream
    stream -.->|"Consumes"| push
    push -.->|"Push service: Wakes sleeping iOS devices"| apns
```

```text
diagram 1, architecture: ok, 9 nodes and 8 connectors, widest rank 3 steps, longest path 6 steps, 0.9 connectors per step, labels average 13 characters, 0 crossing pairs
Label: Apple's push service leaves 'service' alone on its last line, so shorten it, or reword it in the source's words, when that keeps the meaning
PASSED 1 diagram(s) in model.mmd
```

The four critique questions, one line each:
- Where the eye goes first: the change stream, and it is the node the board most needs read, because every block change passes through it and the push path starts there
- What it reads second: sync-service, which advances the first glance by showing what feeds the stream
- What a reader could miss: the last hop from Apple's push service to the device is only in an edge label, and file storage is absent, so a reader could assume it plays no part in sync
- What the remove test would cut next: the API gateway, which stays because it carries the three live sockets and the lanes require it between clients and services

The check kept one wording it flagged. FigJam may leave "service" alone on the last line of the Apple's push service node. Both wordings in your terms wrap that way, so I kept your term. The push worker's edge label reads "Push service: Wakes sleeping iOS devices" and not the longer form I proposed, because the check caps labels at 40 characters.

Left out:
- File storage, no part is described as calling it, so it returns when you name a caller and the board then splits in two
- Apple's push service to the iOS device, no edge exists for it, so the hop rides in the push worker's edge label

The write:
- Target: file <test-file-key>, in the Loomlist Engineering plan as you stated it, as a new section titled "Loomlist block sync services" placed beside what the page holds, which is nothing now
- Extensions: none
- Calls: one `use_figma` call to compose the board and one `get_figjam` call to read it back. Together with the session and the read already made, that is four tool calls, which matters if the plan is Starter or your seat is View or Collab, where Figma caps tool calls at six a month
- Rollback: deleting the one board section the write returns. That runs only on its own yes from you

Do you want me to write this board to the file?