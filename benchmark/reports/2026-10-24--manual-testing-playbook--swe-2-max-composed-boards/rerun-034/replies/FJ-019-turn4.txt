<figma-url>
Read-back: 9 of 9 nodes, 8 of 8 connectors, 6 of 6 lanes, first glance: Sync Service
Left out: file storage, no call to it stated. Android client and its push service, not requested.
Findings: two connectors run through the External lane. "Publishes changes", from Sync Service to Change Stream, crosses the top of the External lane. "Consumes changes", from Change Stream to Push Worker, runs along its bottom edge. The iOS App connector's "Sync requests" label sits on the top border of the Clients lane. The composer sets the lane order, so a model change can't fix these. If they bother you, drag those labels and the External section by hand in FigJam.
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

The board is a new section in the existing file, to the right of what was there. It has 9 nodes and 8 connectors, and the write returned no warnings. The six lanes hold the right nodes, every arrow points forward and the three calls into the Change Stream, Push Worker and Apple Push are dashed. I checked the dashing on the overview screenshot, because the `get_figjam` read doesn't report line style. I also checked connector direction and start and end nodes against the model.

The calls on the board are the draft you accepted, so the source line says they are assumed.

The rollback is to delete the section with id `67:192`, and I'd do that only after your yes.