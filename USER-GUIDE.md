# Product Owner User Guide

Connecting ClickUp and Figma to the Product Owner Project in Claude Desktop or claude.ai, with the checks that prove each connector works.

---

## 1. OVERVIEW

The Product Owner Project writes tasks, bugs, Stories, Epics and docs, and draws FigJam diagrams. It works without any connector: it renders each artifact for you to copy, and a diagram as a Mermaid block. Two optional connectors let it deliver for you:

- **ClickUp connector:** after you approve it, the Project creates the task in a ClickUp list or uploads the artifact as a private ClickUp doc
- **Figma connector:** after you approve it, the Project draws the diagram on a new FigJam board in your Figma plan and reads it back to check it

Both are remote connectors run by ClickUp and Figma. Nothing installs on your computer, and they work in Claude Desktop and in claude.ai in a browser. The Project never writes to either service without your yes in the same chat.

| Where you chat | What the Project can do |
| --- | --- |
| Claude Desktop or claude.ai with the connectors on | Draft, then push to ClickUp and draw FigJam boards after your yes |
| Claude Desktop or claude.ai with no connector | Draft every artifact, and give a diagram as a Mermaid block |
| Claude Code, Codex, OpenCode or another terminal agent | Use the command-line skill instead, set up in `README.md` under Connect ClickUp and Figma |

Setup takes three parts: add the connectors once per Claude account, open the Project with them switched on, and optionally tell it where your ClickUp work goes. Section 5 then proves each connector end to end.

---

## 2. PREREQUISITES

- **A Claude plan that allows connectors.** ClickUp documents adding its server under **Settings > Connectors** on Pro, Team and Enterprise plans
- **A ClickUp account** with access to the workspace you push to. Sign-in is OAuth, and ClickUp's server does not take API keys
- **A Figma account** for diagrams. Figma limits tool calls on Starter plans and on View or Collab seats, and the Project names that limit when a read-back is refused
- **The Product Owner Project.** To create it, make a Project on claude.ai, paste `claude project/Custom Instructions.md` into its instructions and upload every file in `claude project/knowledge/`, as `claude project/README.md` lists them

---

## 3. INSTALLATION

### Add the Connectors

Do this once per Claude account.

1. In Claude Desktop or claude.ai, open **Settings > Connectors**.
2. **ClickUp:** add ClickUp from the connector list. If it is not listed, add a custom connector with the URL `https://mcp.clickup.com/mcp`.
3. **Figma:** add Figma from the connector list. If it is not listed, add a custom connector with the URL `https://mcp.figma.com/mcp`.
4. Sign in when each one asks, and allow access. ClickUp and Figma open their own sign-in pages.

Menu names can differ by Claude version. The two URLs are the ones ClickUp and Figma publish.

### Open the Product Owner Project

1. Open **Projects > Product Owner** and start a new chat.
2. Under **+ > Connectors**, switch ClickUp and Figma on for this chat.

A connector switched off in the chat is the same as no connector. The Project then drafts and offers no push.

---

## 4. CONFIGURATION

### ClickUp Push Targets (Optional)

Without push targets the Project asks where each artifact goes, because a Project cannot read files on your computer. With them, it offers the list or doc that fits straight away, but it still waits for your yes.

1. Copy `claude project/templates/Product Owner - Local - Push Targets.md` into `claude project/local/`, which git ignores, so a filled copy never reaches the repository.
2. In ClickUp, open each list your artifacts go to and copy its link from the address bar. Add it under **Lists**, below the team that owns it, with the name your team uses for it.
3. Do the same for each doc that should collect pages, such as release notes, under **Docs**. A document then lands as a new page in that doc.
4. Upload the filled copy to your **Product Owner** Project's knowledge, beside the shared files. Upload it to your own Project only.

The Project matches each artifact against the names and teams. When one fits it names it, and when more than one could fit it asks which. Terminal agents read the same file from `claude project/local/`, so one filled copy serves both.

---

## 5. VERIFICATION

### ClickUp

1. Ask `$quick $task Add a "Copy link" button to the share sheet`.
2. The reply renders the task, then closes on `Where in ClickUp should this go? Send a list link, or I'll upload it as a private doc, which I recommend for now.` With a list in your push targets file that fits, it closes on `Want me to push this to {that list}, or upload it as a private ClickUp doc instead?` instead. Either line only appears when the ClickUp connector is on.
3. Answer with a space or folder for a private doc, or a list link for a task. Allow the ClickUp tools if Claude asks.
4. The reply names what it created and confirms the body it reads back matches. In ClickUp the headings, bold text and checkboxes render as formatting, never as `##` or `**`.

### Figma

1. Ask `$quick $flow Draw a user flow for resetting a password: the sign-in page, a forgot-password link, an email with a reset link and a new-password page.`
2. The first reply is one proposed Brief with the rows it assumed. Answer `Yes`. Nothing is written yet.
3. The next reply plays the reading back: the question the board answers, the outcome it must deliver and every assumed fact. Answer `Yes`. Nothing is written yet either.
4. The gate is its own reply, and it names your Figma plan. It also states the question and the outcome, three glance lines, a new FigJam file, what the write adds, the calls it spends and how to undo it, then waits for one yes. A yes to the Brief or the playback never writes.
5. Answer `Yes` to the gate. Allow the Figma tools if Claude asks.
6. The reply gives the board URL and a `Read-back:` line that counts what landed, such as `Read-back: 6 of 6 nodes, 6 of 6 connectors`. Open the URL to see the board.

A Mermaid block with a note that there is no Figma connector means the connector is off in this chat, see section 6.

### What to Ask Next

Start a request with one of these, or describe what you want in plain words:

- `$task` for a task, and `$task --subtask` for a subtask under a parent
- `$bug` for a bug report
- `$doc` for a product or engineering doc
- `$story` for a Story, and `$epic` for an Epic
- `$flow` for a FigJam diagram
- `$quick` before any of them for the narrowest useful draft with no questions

---

## 6. TROUBLESHOOTING

| What you see | Why | What to do |
| --- | --- | --- |
| No ClickUp offer at the end of a reply | The ClickUp connector is off in this chat or not added | Check **+ > Connectors** in the chat, then **Settings > Connectors** |
| A Mermaid block and "no Figma connector" instead of a board | The Figma connector is off in this chat or not added | Check **+ > Connectors** in the chat, then **Settings > Connectors** |
| The Project asks where in ClickUp every time | No push targets file is uploaded, or nothing in it fits the artifact | Add the list or doc under a name that says what goes there and upload the file again, see section 4, or send a list link |
| The ClickUp task shows `##`, `**` or `- []` as text | The push used the plain description field | Ask the Project to update the task through `markdown_description`, and report it as a defect |
| `Read-back: not possible` with a limit named | Your Figma plan or seat has used its monthly tool calls | The board may still exist, so open your FigJam drafts. Upgrade the seat, or wait for the limit to reset |
| `Read-back: not possible, the connector has no read tool` | The Figma connector exposes no read tool in this chat | The board is not checked, so look at it yourself before you rely on it |
| A sign-in loop or an access error | The connector's sign-in expired or lacks workspace access | Remove and add the connector again under **Settings > Connectors** |
| The Project mentions `figma-ds-cli` or Figma Desktop | That is the terminal route, which a Project cannot run | Add the Figma connector, see section 3. `README.md` sets up the desktop route for terminal agents |
| A ClickUp tool error that names a parameter | ClickUp changed its tool fields | The Project reads tool names from the connector at run time. Report the error with the tool name |

---

## 7. RELATED RESOURCES

- [README.md](./README.md): What Product Owner is, and the command-line setup for terminal agents
- [claude project/README.md](./claude%20project/README.md): What the Project contains and how to upload it
- [mcp-click-up/SKILL.md](./mcp-click-up/SKILL.md): The ClickUp tools and their parameters
- [sk-create-figjam/SKILL.md](./sk-create-figjam/SKILL.md): The diagram flow and the Figma connector tools it calls
- [mcp-figma/SKILL.md](./mcp-figma/SKILL.md): The Figma Desktop tools of the terminal route
