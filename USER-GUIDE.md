# Product Owner User Guide

> One line in, a ready-to-ship task, bug, Story or doc out. Ask for a diagram and Product Owner composes a framed FigJam board, checked against its sources before a single shape lands.

---

## 1. OVERVIEW

Product Owner turns rough notes, screenshots and pasted text into backlog work your team can pick up straight away. It writes tasks, subtasks, bug reports, Stories, Epics and product or engineering docs. It also draws diagrams on FigJam boards: user flows, processes, architectures, sequences, state machines, data models and plans.

Two habits run through every request. It asks before it guesses, in one combined question rather than a drip of them. And it writes nothing to ClickUp or Figma until you say yes in the same chat.

| Where you chat | What it delivers |
| --- | --- |
| Claude Desktop or claude.ai, connectors on | Drafts, FigJam boards and ClickUp pushes, each after your yes |
| Claude Desktop or claude.ai, no connector | Every draft, and a diagram as a checked Mermaid model to keep |
| Claude Code, Codex, OpenCode or another terminal agent | The same drafts saved under `export/`, set up as `README.md` describes |

New here? Section 6 connects ClickUp and Figma once per account. Everything else works without them.

---

## 2. ASK FOR AN ARTIFACT

### Pick a Command

Start a message with a command, or describe what you want in plain words. "Write a bug for the login loop" and "document how payouts work" route just as well as `$bug` and `$doc`.

| Command | Short | Result |
| --- | --- | --- |
| `$task` | `$t` | A development task with its requirements and QA checklist |
| `$task --subtask` | none | A subtask under a parent task |
| `$bug` | `$b` | A bug report with steps, expected behavior and evidence |
| `$story` | `$s` | A Story with numbered Given/When/Then acceptance criteria. `$prd` and `$p` work too |
| `$epic` | `$e` | An Epic with its goal and scope, ready to split into Stories |
| `$doc` | `$d` | A guide, catalog, behavior reference, runbook, API reference or proposal |
| `$flow` | `$figjam` | A diagram on a FigJam board, covered in Section 3 |
| `$quick` | `$q` | Place it before any command for the leanest draft with smart defaults |

Need a Story and its tasks together? Ask for both in one message, such as "write a Story for saved searches and break it into tasks". The Story arrives with one task file per task, under one number.

### What It Asks Back

Most requests start with one question, and nothing is drafted until you answer it. The question gathers everything still open in one message: scope, platforms, evidence for a bug, the user and the value for a Story. A doc request also asks which sources to trust, which one wins a conflict and whether each claim is current, approved or only proposed.

Answer in one message and the next reply is the draft. Gaps with a safe default are filled and listed for you to check, so small things never trigger a second round of questions. Only a source conflict, a source you promised but have not sent or a decision you called unsettled can hold the draft again.

### What Comes Back

Every delivery follows the same shape, so you know where to look:

- **The artifact.** In a terminal it is saved under `export/` and read back before the reply, such as `export/009 - task-payout-pause.md`. In a claude.ai Project it renders first in the chat, with the path it would carry
- **A voice check.** One `HVR self-scan:` line counts the AI writing tells it found and fixed
- **A quality line.** Such as `Quality: every floor met | Kind: Task | Energy: Standard`
- **Open items.** Every assumption and addition, numbered, each with what to confirm or strike
- **One closing line.** The ClickUp offer when ClickUp is connected, otherwise `Want me to change anything?`

### Set the Depth

The default is a Standard pass, which weighs the work from at least three angles such as the user, the business and delivery. You can push it either way with plain words:

| Say | Energy | What changes |
| --- | --- | --- |
| `$quick`, "quick" or "just do it" | Quick | Skips routine questions and fills safe defaults. Never skips a promised source or an unsettled decision |
| Nothing | Standard | The full pass, with one question when something is missing |
| "deep", "think longer" or "full depth" | Deep | Weighs all five angles: user, business, technical, risk and delivery. Consults your sources more broadly |
| "skip depth" | Raw | Skips the thinking pass and goes straight to the draft |

---

## 3. DRAW A FIGJAM DIAGRAM

Paste screenshots, a Figma link, a product doc, a schema or a plan, and ask for a board. Product Owner picks the diagram your reader needs, models it with every item tied to its source, checks the model against the type's rules and composes a finished board. No dragging boxes. No guessing at a step the sources never showed.

### Seven Diagram Types

The reader's question picks the type. Name one if you know it, or let it recommend one.

| Your reader asks | Type |
| --- | --- |
| Which screens does a person pass through, and where do they choose? | User flow |
| Who does what, in which order, and where does work change hands? | Process, with a lane per team |
| What parts make up this system and how do they connect? | Architecture |
| In what order do these parties exchange messages? | Sequence |
| Which states exist and what moves the thing between them? | State |
| Which entities exist, what fields do they carry and how do they relate? | ER |
| Which tasks and phases are active when? | Gantt |

When two types fit, such as an architecture and a sequence for the same system, it asks which question your reader has. When the type you named does not match what the sources describe, it says so once and recommends the better fit.

### Ask for a Board

```text
$flow the location change from these screenshots
make a FigJam flow from the signup doc
$figjam the booking status lifecycle from the bookings doc
put the launch plan on a FigJam gantt chart
```

Before it models anything, it interviews you in short rounds until the Brief is ready to draw. The Brief holds nine rows, opening with who reads the board, the one question it answers and what that reader should decide afterwards. Every question shows its reading of your sources and a recommended answer, so "use your recommendations" is always a valid reply. An unanswered row proceeds on that recommendation, marked assumed.

Standard energy caps the interview at three rounds and Deep at five. With `$quick` there are no rounds: it sends one proposed Brief with every inferred row marked, and an offer to draw unless you correct it.

Three settings shape the board, each with a default you can override in plain words:

- **Detail level.** `Balanced` keeps what carries the story. `Simplified` keeps only the main steps and their order. `Faithful` keeps every source item and splits into several diagrams when one would overflow
- **Audience.** `Mixed` uses component names and plain verbs. `Engineer` keeps exact names, paths and status codes. `Executive` names capabilities and outcomes
- **Reading distance.** `Laptop` for one reader at arm's length. `Meeting screen` cuts labels to 32 characters for a shared call. `Wall` cuts the node budget to about two thirds and labels to 25 characters for a review room

### Four Stops Before a Board Lands

A board goes into a shared Figma plan, so the write sits behind stops you control:

1. **The playback.** One reply restates the question, the outcome, what each source settled and every fact it assumed. Answer it, or correct a row. A yes here writes nothing
2. **The gate.** A separate reply shows the checked model and names the Figma plan, the new file, what the write adds, any notes it plans, the tool calls it will spend and how to undo it. It also gives three glance lines: what the eye should land on first, second and last
3. **The write.** Only a yes to the gate's own question writes. A yes to anything else never does
4. **The read-back.** It reads the board back from Figma and counts what landed against the model, such as `Read-back: 8 of 8 nodes, 8 of 8 connectors, 2 of 2 decision exits labelled, first glance: the failed payment`. A mismatch is reported as measured, and the board is never called done

The reply then gives the board URL first and the read-back line second. An `Extensions:` line counts any notes, a `Left out:` line names anything cut or split away and a `Finding:` line carries each open point. The voice check comes last.

### What a Composed Board Looks Like

Every board comes out finished, on an 8 pixel grid, with nothing to tidy by hand:

- **A framed board.** One white section holds everything, named after the board's title
- **A title and subtitle.** The title in 64 pixel type, with a one-sentence subtitle under it
- **Zones.** Tinted sections group related steps. A zone never takes the colour of a step inside it, and two neighbouring zones never read as one
- **Colour by kind.** The same colour means the same thing on every board: a light blue start, light yellow decision diamonds, a light green goal, a light orange exit and a light red error. Colour never stands alone, because shapes and labels carry the meaning too
- **A key.** Under the diagram, with one sample of every colour, line and arrow the board uses and nothing else
- **One pink outline.** A heavy pink outline marks the one thing to see first, such as the failed payment on a checkout flow. It is the only heavy line on the board, and the key names it `In focus`
- **A source line.** Under the key, naming what the board was drawn from

A model too big for one readable board becomes an overview board and a detail board, offered together, never a thinner board that quietly drops steps.

### Revise or Replace a Board

Send the board's link with what should change. A board written in another session works too, because it reads the board back first.

- **Add notes.** Numbered pins with a sticky legend, or a single sticky, go on top of the board after your yes. The diagram underneath stays as it was
- **Change what the board says.** The change goes into the model and the board is composed again after a playback of the rows it touches and a fresh yes. The new board lands beside the old one first and is read back
- **Remove the old board.** It asks once the new one checks out, and deletes the old board only on that second yes. With no second yes, both stay
- **Restyle by hand.** It never moves, resizes or recolours a composed shape. A custom colour or a nudge to one node is a quick edit in FigJam, and it names the node so you can find it
- **Change the look of every board.** Which colour means what, the first-glance accent, the type sizes and the words on the key live in one design file, `sk-create-figjam/assets/figjam-design.md`. Edit it once and every board composed after it follows. An edit that would weaken contrast or compete with the pink outline falls back to the shipped value, and the reply names it on a `Finding:` line. In a claude.ai Project the design arrives as the Knowledge file Assets - Flow Board Design

After two attempts at the same board it stops and asks what is wrong rather than composing a third.

### What It Will Not Draw

Pie charts, mindmaps, Venn diagrams, class diagrams, journeys, timelines, quadrant charts, C4 diagrams, git graphs and requirement diagrams are out of scope. It says so plainly and offers the nearest type it does draw: journeys become user flows, timelines become gantt charts with milestones, class diagrams become ER diagrams and C4 diagrams become architectures. When two or three steps would read better as a list, it says that too.

---

## 4. STEER THE RESULT

### Answer the Open Items

Every addition you did not ask for sits under Open items, numbered, with what the source said and what is still open. Reply with the numbers to strike or confirm, such as "drop 2, confirm 1 with Amsterdam time", and it revises the draft. Anything you did not say stays out of the artifact as fact.

### Refine What You Already Have

Paste an existing task, Story, Epic or doc and say what should change. The refinement keeps its section names, order, links and identifiers, and touches only what you named. In a terminal it saves under the original file name and never overwrites your source. Ask for a full restructure or ClickUp normalization explicitly when you want one.

### Pair an Artifact With a Board

Ask for both in one message, such as "write a Story for the new checkout and make a FigJam flow of its screens". The Story comes first, saved and read back. The board follows from it, with its own playback and gate. Once the board checks out, its link is written into the Story's Flows group and the Story is delivered again, so the copy you keep points at the board.

---

## 5. SEND IT TO CLICKUP

### The Offer

With the ClickUp connector on, every delivery closes on an offer and waits. Without push targets it asks where the artifact goes:

`Where in ClickUp should this go? Send a list link, or I'll upload it as a private doc, which I recommend for now.`

Reply with a list link for a task or a space or folder for a private doc. The push keeps headings, bold text and checkboxes as real formatting, and the reply confirms the body it reads back matches. A link you send is used for that push only. A yes covers one push and never carries over to the next.

### Name Your Push Targets

Tell it once where each kind of work goes, and the offer names the right list or doc for you: `Want me to push this to {that list}, or upload it as a private ClickUp doc instead?` It still waits for your yes.

1. Copy `claude project/templates/Product Owner - Local - Push Targets.md` into `claude project/local/`, which git ignores, so a filled copy never reaches the repository.
2. In ClickUp, open each list your artifacts go to and copy its link from the address bar. Add it under **Lists**, below the team that owns it, with the name your team uses for it.
3. Do the same under **Docs** for each doc that collects pages, such as release notes. A document then lands as a new page in that doc.
4. Upload the filled copy to your own **Product Owner** Project's knowledge, beside the shared files. Terminal agents read the same file from `claude project/local/`, so one copy serves both.

When more than one list could fit, the offer names them and asks which.

---

## 6. CONNECT CLICKUP AND FIGMA

Set this up once per Claude account. Both are remote connectors run by ClickUp and Figma, so nothing installs on your computer.

### What You Need

- **A Claude plan that allows connectors.** ClickUp documents adding its server under **Settings > Connectors** on Pro, Team and Enterprise plans
- **A ClickUp account** with access to the workspace you push to. Sign-in is OAuth, and ClickUp's server takes no API key
- **A Figma account** for boards. Figma limits a Starter plan and a View or Collab seat to six tool calls a month, which one or two boards can use up
- **The Product Owner Project.** Make a Project on claude.ai, paste `claude project/Custom Instructions.md` into its instructions and upload every file in `claude project/knowledge/`, as `claude project/README.md` lists them

### Add the Connectors

1. In Claude Desktop or claude.ai, open **Settings > Connectors**.
2. **ClickUp:** add ClickUp from the connector list. If it is not listed, add a custom connector with the URL `https://mcp.clickup.com/mcp`.
3. **Figma:** add Figma from the connector list. If it is not listed, add a custom connector with the URL `https://mcp.figma.com/mcp`.
4. Sign in when each one asks, and allow access.

Menu names can differ by Claude version. The two URLs are the ones ClickUp and Figma publish.

### Switch Them On in Each Chat

Open **Projects > Product Owner**, start a new chat and switch ClickUp and Figma on under **+ > Connectors**. A connector switched off in the chat counts as no connector, so the Project drafts and offers no push.

### Check That It Works

**ClickUp.** Ask `$quick $task Add a "Copy link" button to the share sheet`. The reply renders the task and closes on the ClickUp offer. Name a target and allow the ClickUp tools if Claude asks. The reply then names what it created and confirms the body it read back matches.

**Figma.** Ask `$quick $flow Draw a user flow for resetting a password: the sign-in page, a forgot-password link, an email with a reset link and a new-password page.`

1. The first reply is one proposed Brief with the rows it assumed. Answer `Yes`. Nothing is written yet.
2. The next reply is the playback. Answer `Yes`. Still nothing is written.
3. The gate follows as its own reply and names your Figma plan. Answer `Yes` and allow the Figma tools if Claude asks.
4. The reply gives the board URL and a `Read-back:` line, such as `Read-back: 6 of 6 nodes, 6 of 6 connectors`. Open the URL to see the board.

A Mermaid block with a note that there is no Figma connector means the connector is off in this chat. Section 7 has the fix.

---

## 7. TROUBLESHOOTING

| What you see | Why | What to do |
| --- | --- | --- |
| No ClickUp offer at the end of a reply | The ClickUp connector is off in this chat or not added | Check **+ > Connectors** in the chat, then **Settings > Connectors** |
| A Mermaid block and "no Figma connector" instead of a board | The Figma connector is off in this chat or not added | Check **+ > Connectors** in the chat, then **Settings > Connectors** |
| It asks where in ClickUp every time | No push targets file is uploaded, or nothing in it fits the artifact | Add the list or doc under a name that says what goes there and upload the file again, as Section 5 shows, or send a list link |
| The ClickUp task shows `##`, `**` or `- []` as text | The push used the plain description field | Ask it to update the task through `markdown_description`, and report it as a defect |
| `Read-back: not possible` with a limit named | Your Figma plan or seat has used its monthly tool calls | The board may still exist, so open your FigJam drafts. Upgrade the seat, or wait for the limit to reset |
| `Read-back: not possible, the connector has no read tool` | The Figma connector exposes no read tool in this chat | The board is not checked, so look at it yourself before you rely on it |
| A plain board with no title, zones or key, and the reply says it was generated | Figma's own generator drew it, because the compose tool was not available | The diagram follows the model, only plainer. Reconnect the Figma connector and ask it to compose the board again |
| A sign-in loop or an access error | The connector's sign-in expired or lacks workspace access | Remove and add the connector again under **Settings > Connectors** |
| It mentions `figma-ds-cli` or Figma Desktop | That is the terminal route, which a Project cannot run | Add the Figma connector, as Section 6 shows. `README.md` sets up the desktop route for terminal agents |
| A ClickUp tool error that names a parameter | ClickUp changed its tool fields | It reads tool names from the connector at run time. Report the error with the tool name |

---

## 8. RELATED RESOURCES

- [README.md](./README.md): What Product Owner is, and the setup for terminal agents
- [sk-create-figjam/SKILL.md](./sk-create-figjam/SKILL.md): The FigJam diagram workflow and the Figma tools it calls
- [sk-product-owner/SKILL.md](./sk-product-owner/SKILL.md): The rules behind every task, bug, Story, Epic and doc
- [claude project/README.md](./claude%20project/README.md): What the Project contains and how to upload it
- [mcp-click-up/SKILL.md](./mcp-click-up/SKILL.md): The ClickUp tools and their parameters
