<figma-url>
Read-back: 6 of 6 nodes, 5 of 5 connectors, 4 of 4 lanes, each node inside its lane, no async or outside-system edges, first glance: sync-service
Left out: Options A, B and C, not decided until Joana's decision on 2026-10-09 (#sync-eng thread)
Left out: the offline change queue, a proposal in Oskar's offline mode brief
Left out: where sync-service keeps device cursors, which no source names
Finding: the Block storage label is cut off at overview zoom and reads "Block storage (not n...". The full text is stored on the node, so the "not named in sources" warning is hidden until someone zooms in. To fix it I'd shorten the label to "Block storage, assumed" and recompose in the same file, which needs your yes
Finding: the source line marks Entry point as assumed but doesn't mention Block storage. The same recompose would add it, and Hugo's Pages and Databases team can name the real store
Finding: I wrote the board to a new file in <figma-plan-1> drafts with no project, not to `<test-file-key>`, which hasn't been read or changed
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.