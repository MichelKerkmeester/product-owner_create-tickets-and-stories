# Product Owner - Reference - Connector Setup

Guided setup for the two optional connectors this Project delivers through: ClickUp for tasks and private docs, Figma for FigJam boards. Walk the user through it one step at a time, and call it done only when the check in section 4 gives the expected reply in a new chat.

---

## 1. OVERVIEW

Both connectors are remote servers run by ClickUp and Figma. Nothing installs on the user's computer, and they work in Claude Desktop and in claude.ai in a browser. Without them the Project still drafts every artifact for copying and gives a diagram as a Mermaid block. A connector counts as present only when its tools are listed in the conversation, so one added in Settings but switched off in the chat is absent.

---

## 2. WHAT THE USER NEEDS

1. A Claude plan that allows connectors. ClickUp documents adding its server under **Settings > Connectors** on Pro, Team and Enterprise plans.
2. A ClickUp account with access to the workspace they push to. Sign-in is OAuth, and ClickUp's server takes no API key.
3. A Figma account for diagrams. Figma limits tool calls on Starter plans and on View or Collab seats.

---

## 3. ADD AND SWITCH ON THE CONNECTORS

Once per Claude account:

1. Open **Settings > Connectors**.
2. **ClickUp:** add it from the list, or add a custom connector with the URL `https://mcp.clickup.com/mcp`.
3. **Figma:** add it from the list, or add a custom connector with the URL `https://mcp.figma.com/mcp`.
4. Sign in when each one asks and allow access.

Then in each chat of this Project, switch both on under **+ > Connectors**. Menu names can differ by Claude version, and the two URLs are the ones ClickUp and Figma publish.

---

## 4. SET YOUR CLICKUP PUSH TARGETS

Optional. The user copies the template `Product Owner - Local - Push Targets.md`, adds each ClickUp list and doc by name under the team that owns it, and uploads the filled copy to their own Project only. The ClickUp offer then names the list or doc that fits, or asks between the ones that could, and a document lands as a new page in the named doc. Every push still waits for their yes.

---

## 5. CHECK THAT IT WORKS

- **ClickUp:** in a new chat, `$quick $task Add a "Copy link" button to the share sheet` ends on `Where in ClickUp should this go? Send a list link, or I'll upload it as a private doc, which I recommend for now.` After the user names a target and approves, the reply names what it created and confirms the read-back body matches
- **Figma:** `$flow` with a short password-reset flow shows the checked model and a write gate. After `Yes`, the reply gives the board URL and a `Read-back:` line counting what landed

---

## 6. TROUBLESHOOTING

- **No ClickUp offer, or a Mermaid block with no board:** the connector is off in this chat or not added. Check **+ > Connectors**, then **Settings > Connectors**
- **The Project asks where in ClickUp every time:** no push targets file is uploaded, or no list or doc in it fits the artifact. Add one under a name that says what goes there, upload the file again, or send a list link
- **Asked about Figma Desktop or `figma-ds-cli`:** that route is for terminal agents, and a Project cannot run it. A Project draws through the Figma connector, so add that instead. The repository README sets up the desktop route for a terminal
- **`##` or `**` shows as text in ClickUp:** the push used the plain description field. Update the task through `markdown_description`
- **`Read-back: not possible` with a limit named:** the Figma plan or seat used its monthly tool calls. The board may still exist in the FigJam drafts
- **A sign-in loop or an access error:** remove and add the connector again under **Settings > Connectors**
- **A ClickUp tool error that names a parameter:** ClickUp changed its tool fields. The Project reads tool names from the connector at run time, so report the error with the tool name
