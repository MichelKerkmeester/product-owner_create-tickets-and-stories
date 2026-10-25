<figma-url>
Read-back: 7 of 7 nodes, 7 of 7 connectors, 4 of 4 decision exits labelled, 3 of 3 zones holding their nodes, 1 label overlap, exit labels read visually
Left out: free pickup for orders over €100, a proposal under review
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

The board is written but I'm not calling it done, because the overview shows one defect.

**Finding**
* The "Drop-off point" label on the first connector from "Drop-off or pickup?" sits on top of the "Done" zone heading. It is at the top right of the board, above "Confirmation with QR code" (connector `48:2080`). The label and heading both become hard to read
* The composer sent that connector over the top of the zone because both method exits end on the same node
* The counts, labels, arrow directions and zone membership all match the model. `get_figjam` doesn't return connector label text, so the four exit labels were read from the overview screenshot only

**Proposed fix**
* Remove the "Done" zone and put the confirmation inside "Request the return". No zone heading is then left for the loop to cross
* I composed this version locally with no Figma call. The check passed with 7 nodes, 7 connectors and 0 crossing pairs, and the geometry trace shows the confirmation inside the zone, far from its heading. The trace doesn't model label placement on connectors, so I can't prove the overlap is gone until it is drawn
* This would be the second and last attempt on this board. If it still overlaps, I'll stop and ask, and you could nudge the label by hand in FigJam

**Needs your yes**
1. Compose the corrected board into the same file, beside this one. It costs one `use_figma` and one `get_figjam` read-back
2. A separate yes to then delete the current board section `48:2023`. Until you give it, both boards stay