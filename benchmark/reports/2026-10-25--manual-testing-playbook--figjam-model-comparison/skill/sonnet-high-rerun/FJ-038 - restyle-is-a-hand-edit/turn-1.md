I haven't changed the board. I'm not allowed to move, resize or restyle a node once the composer has drawn it. Flow Mode only changes a board by changing its model and composing it again, and a position or font size on one node isn't something the model can hold.

You have three ways forward:

- **Hand edit in FigJam (my recommendation for this change):** open the file `<draft-file-key>`, select the node labelled "Approve return", drag it right and raise its font size in the text panel. Check the connectors on that node afterwards, because the composer routes them through anchors and they may need a nudge.
- **Reshape the model:** I can't set a position for one node. I can change the diagram's direction, the declaration order, its zones or its edges so "Approve return" lands further right, then compose the board again as a new section in the same file. I'd delete the old section only after you say yes to a question that names it. This won't make the text bigger.
- **Bigger text everywhere:** node label size is a token in `sk-create-figjam/assets/figjam-design.md`. Raising it makes every node on every board larger, not only "Approve return".

Finding: I haven't read the board in this session, so I can't yet confirm the exact label or what sits to the right of "Approve return". If you want the model route, I'll read it with `get_figjam` first.

Which of the three do you want?

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.