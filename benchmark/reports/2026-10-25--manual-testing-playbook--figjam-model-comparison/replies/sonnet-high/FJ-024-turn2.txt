The model passed the pre-write check and composes cleanly. Nothing has been written yet.

```text
Check: diagram 1, architecture: ok, 9 nodes and 8 connectors, 6 lanes, 0 crossing pairs
```

```mermaid
%% type: architecture
flowchart LR
    subgraph client ["Clients"]
        desktop[Desktop App]
        webClient[Web App]
        ios[iOS App]
    end
    subgraph gateway ["Edge"]
        api[API Gateway]
    end
    subgraph service ["Services"]
        sync[sync-service]
        push[Push Worker]
    end
    subgraph datastore ["Stores"]
        blocks[Blocks Database]
    end
    subgraph async ["Events"]
        changes[Change Stream]
    end
    subgraph external ["External"]
        apns[Apple Push]
    end
    desktop <-->|"Live socket"| api
    webClient <-->|"Live socket"| api
    ios <-->|"Live socket"| api
    api -->|"Routes sync requests"| sync
    sync -->|"Writes block changes"| blocks
    sync -.->|"Publishes changes"| changes
    changes -.->|"Feeds"| push
    push -.->|"Apple Push: Wakes iOS device"| apns
```

```text
Question: which parts sit behind block sync and how do they connect?
Outcome: a reader can follow one block change from a client through the gateway and sync-service to the change stream, and on to the push that wakes a sleeping iOS device.
First glance: sync-service, where every block change is written and published.
Second glance: the Change Stream that carries each change on to the Push Worker.
Last glance: Apple Push, the external hop that wakes sleeping iOS devices.
Plan: Loomlist Engineering, as you named it. File: the existing FigJam file <draft-file-key>.
Writes: one composed board, 9 nodes and 8 connectors in 6 lanes, with a title, a key and a source line, at the Laptop reading distance. It lands as a new section beside what the file holds, and nothing already there changes.
Left out: file storage, because no call to it is stated. The wake hop from Apple Push to the iOS app, because the type cannot draw it.
Extensions: none.
Calls: create_session, a get_figjam read of the file before the write, one use_figma and a get_figjam read-back. That is four calls, and on a Starter plan or a View or Collab seat they count against the six tool calls Figma allows each month.
Rollback: delete the one board section the write returns, and only on a yes to a question that names it. If the file can't take the write, I stop and ask before creating anything in the Barter team plan.
Write it?
```