Read-back matched the model, so I'm writing up the result.

<figma-url>
Read-back: 9 of 9 nodes, 8 of 8 connectors, 6 of 6 lanes, first glance: Sync Service
Left out: file storage, off the sync path, cut at the balanced detail level. The Apple Push wake-up of the iOS App is also not an edge, because the architecture rules allow no edge from an outside system to a client, so the Push Worker's edge label carries it.
Finding: the eight calls are my wiring, not a doc's, and the board's source line says so. The sync-service doc settles them.
Finding: the `get_figjam` outline lists no connector labels or dash patterns. I read the eight labels and the three dashed async or outside edges (Publishes, Consumes, Apple Push) from the overview screenshot.
Finding: "Writes Blocks" runs over the top of the Events zone and passes about 26 pixels right of the "Services" title. It touches nothing, but fixing the long route means reshaping the model and recomposing after your yes.
Finding: I didn't load Figma's `figma-use` and `figma-use-figjam` skills before the write, because this runtime has no loader for them. The composed code ran with no warnings.
Finding: I didn't call `whoami`, so I haven't confirmed the file `<test-file-key>` sits in the Loomlist Engineering plan. No new file was created.
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.