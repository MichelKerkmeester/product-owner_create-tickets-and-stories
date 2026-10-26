I haven't drawn anything. The stays schema note isn't in the repo's `context/` folder, and your FigJam file `<draft-file-key>` doesn't hold it either. I read that file, and it has three boards: "Start a return", "1. Sign up" and "2. Workspace setup".

The only stays schema in the repo is the invented Roamstay tables in `sk-create-figjam/assets/examples/er-roamstay-stays.md`. That is a worked example, so I won't draw it as your model.

**Question:** Can you paste the schema note, or tell me where it lives (a file path, a ClickUp doc or a link)?

I'd also like your answers to two things. If you don't answer, I'll go with the recommendation.
1. **Reader and outcome.** I read this as an ER diagram for whoever builds against stays data, answering "which entities exist, which fields join them and how many of each?". Recommended: keys, foreign keys and the few columns a stays story would cite, with the full column list left out. That keeps the relationships readable.
2. **What the board must not do.** Recommended: no entities from outside the stays model, and no relationship or cardinality that the note doesn't state. Anything the note leaves open goes in a `Left out:` line.

Once the note is here, I'll play back my reading for your answer. After that you get a separate write gate. The new board would go in as a section beside the three existing ones, and none of them would change. I won't create a new file.

Finding: no stays schema note was found in the repo or on the FigJam file, so the model is blocked until you send it.
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.