No launch plan came with the request, and nothing in the workspace is one. That gap plus a route gap are the only things holding the board, and one message settles both.

**1. The plan itself**
- Reading: the workspace holds nine context notes across fernhouse, loomlist and roamstay. None is named for a launch and none carries launch dates
- Question: paste the plan, or name the file or ClickUp item it lives in
- Recommended: the plan file with its dates, owners and dependencies
- Why: a gantt reads the plan's own dates and owners, and a date the plan does not state gets asked for rather than estimated

**2. Reader, question and outcome**
- Reading: a launch plan usually means delivery leads tracking what ships when
- Question: who reads the board, and what must they decide from it
- Recommended: the delivery leads, deciding which task is at risk and what a slip moves behind it
- Why: the reader's question fixes the sections, the task count and the reading distance

**3. Timeframe and fixed dates**
- Reading: no dates supplied, so there is no axis yet
- Question: the window the chart covers, and the fixed points that cannot move
- Recommended: one chart across the launch window, with announcement, beta and general availability as milestones
- Why: a sprint and a year do not share one axis, and fixed dates anchor every dependency drawn from them

**4. Route to the board**
- Reading: this session has no Figma connector carrying `generate_diagram`. Code Mode's figma manual is read-only, and `figma-ds-cli` has no gantt verb
- Question: connect the hosted Figma MCP server, or take the checked model instead
- Recommended: connect it, so the chart lands on a board you can share
- Why: a gantt needs the hosted route, because the `fj` fallback has no layout verb

Quality: not scored, clarification only | Kind: Gantt chart | Energy: Standard

### Open items
1. **Task budget**
   - **Situation:** A gantt holds at most 12 tasks, with 5 bars running at once per section, so a longer plan splits rather than shrinks
   - **Open:** If the plan runs past 12 tasks, say whether you want the overview chart, one chart per phase, or both
2. **Sections**
   - **Situation:** Sections come from the plan's own phases once I read it, so nothing is assumed yet
   - **Open:** Name the phase headings if they should differ from the plan's wording

Answer in one message and I'll draw the gantt.