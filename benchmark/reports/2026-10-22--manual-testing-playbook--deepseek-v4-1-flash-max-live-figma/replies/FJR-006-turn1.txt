No schema note is in this workspace, so there are no tables to model from yet.

**Reading:** The workspace holds the Roamstay company context and six Roamstay notes, and none of them lists a table with its keys. The only stays schema on disk is a worked example on a fictional company.

**Question, in three parts:**
- **The note:** paste the schema note, or give me its path or link. I need every table with its primary key and foreign keys. If the note is lost, say so and I will read another source you name
- **The reader and their decision:** who opens the board, and what they settle with it. Recommended: Booking squad engineers deciding how the stays tables join before a build. Why: an ER board is read by whoever builds against the model
- **Scope and grouping:** recommended one board covering the guest side and the property side of a stay, with keys and cardinalities and no full column list. Say if you want the partner tables grouped apart from the guest tables, or a different split. Why: the budget is nine entities, and the joins are the part a reader decides on

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.
Quality: not scored, clarification only | Kind: FigJam ER diagram | Energy: Standard

### Open items
1. **Write route**
   - **Situation:** No hosted Figma connector is attached to this session, and the `fj` fallback cannot draw an ER diagram
   - **Open:** Attach the hosted Figma MCP for the write, or take the checked Mermaid model to draw the board yourself
2. **Detail and distance**
   - **Situation:** I plan balanced detail at laptop distance, with two domain tints if you want the guest and partner sides grouped
   - **Open:** Name meeting screen or wall if the board will be read further away

Answer in one message and I'll draft the FigJam ER diagram.