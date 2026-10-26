## Write gate

Architecture fits the question about system parts and connections. A sequence diagram would emphasize message order that the request does not fully specify. One architecture diagram would exceed the 9-node limit, so the checked model uses two path diagrams and repeats shared components where needed.

The first diagram focuses on `sync-service`; the second focuses on `pushWorker`. The change stream advances the reading between block writes and push delivery. File storage is shown as an assumed connection. Protocols, retries and failure behavior are left out.

**Block sync**

```mermaid
%% type: architecture
%% title: Loomlist block sync
%% subtitle: For Loomlist engineers, trace each block change from a client through sync and storage to the event stream
%% source: User request and accepted connections. File-storage access is assumed. Left out: protocols, retries and failure behavior.
%% focus: syncService
flowchart LR
    subgraph client ["Clients"]
        desktopClient[Desktop client]
        webClient[Web client]
        iosClient[iOS client]
    end
    subgraph gateway ["Gateway"]
        apiGateway[API gateway]
    end
    subgraph service ["Services"]
        syncService[sync-service]
    end
    subgraph async ["Event stream"]
        changeStream[Block change stream]
    end
    subgraph datastore ["Data stores"]
        blocksDatabase[Blocks database]
        fileStorage[File storage]
    end
    desktopClient <-->|"Live socket"| apiGateway
    webClient <-->|"Live socket"| apiGateway
    iosClient <-->|"Live socket"| apiGateway
    apiGateway -->|"Routes block sync"| syncService
    syncService -->|"Writes every block change"| blocksDatabase
    syncService -->|"Reads/writes files (assumed)"| fileStorage
    syncService -.->|"Publishes every block change"| changeStream
```

**iOS push wake**

```mermaid
%% type: architecture
%% title: Loomlist iOS push wake
%% subtitle: For Loomlist engineers, follow block changes through push delivery to sleeping iOS devices
%% source: User request and accepted connections. Left out: push protocols, retries and failure behavior.
%% focus: pushWorker
flowchart LR
    subgraph gateway ["Gateway"]
        apiGateway[API gateway]
    end
    subgraph service ["Services"]
        syncService[sync-service]
        pushWorker[Push worker]
    end
    subgraph async ["Event stream"]
        changeStream[Block change stream]
    end
    subgraph external ["Outside"]
        applePush[Apple Push Service]
    end
    apiGateway -->|"Routes block sync"| syncService
    syncService -.->|"Publishes every block change"| changeStream
    changeStream -.->|"Delivers block changes"| pushWorker
    pushWorker -.->|"Apple Push Service: Wakes iOS"| applePush
```

The check passed for both diagrams with zero crossing pairs. The default FigJam design reported no warnings. Detail is faithful, the audience is engineering, and the reading distance is laptop. The existing page content stays in place; the composer will place these sections to its right. No extensions are planned.

Writing will use two `use_figma` calls, followed by one `get_figjam` read-back and two `get_screenshot` reads. The session and initial file read are complete. Rollback would remove only the two sections created by this write, after separate confirmation.

Do you approve writing these two framed diagrams to the existing file `<test-file-key>` in the Loomlist Engineering plan?