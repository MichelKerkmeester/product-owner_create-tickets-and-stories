<figma-url>
Read-back: 9 of 9 nodes, 8 of 8 connectors, 6 of 6 lanes, first glance: sync-service. The Roamstay "Stays model" section already in the file is unchanged.
Left out: file storage, because no call to it is stated.
Left out: the wake hop from Apple Push to the iOS app, because the architecture type has no edge from an outside system to a client. The label "Wakes iOS device" on the push worker's edge carries it.
Finding: `get_figjam` does not report connector labels or dashed lines. I confirmed the eight labels and the four dashed async edges on the overview screenshot of the board, not from the node read.
Finding: I could not check that file `<draft-file-key>` sits in the Loomlist Engineering plan, so please confirm it. I wrote by file key and created no new file, so nothing went into the Barter team plan.
Finding: if you tell me which part reads or writes file storage, I can add it and split the board into a sync path and a push path.
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.