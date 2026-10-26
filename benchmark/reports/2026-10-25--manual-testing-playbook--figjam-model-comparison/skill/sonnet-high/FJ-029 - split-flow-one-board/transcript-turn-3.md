# FJ-029 turn 3 transcript

**User:** Yes, go ahead.

**Tool call:** `mcp__figma-remote__create_session` `{"fileKey": "<draft-file-key>", "description": "Add two FigJam user-flow boards (1. Sign up, 2. Workspace setup) for Loomlist signup and first workspace setup as new sections in the existing file"}`

**Tool call:** `ToolSearch` `{"query": "select:ReadMcpResourceTool,ListMcpResourcesTool", "max_results": 3}`

**Tool result:** `mcp__figma-remote__create_session`

```text
"{\"sessionId\":\"de63346d-1f0a-48dc-a30d-5a55cb2bbd24\"}"
```

**Tool result:** `ToolSearch`

```text
[{"type": "tool_reference", "tool_name": "ReadMcpResourceTool"}, {"type": "tool_reference", "tool_name": "ListMcpResourcesTool"}]
```

**Tool call:** `ReadMcpResourceTool` `{"server": "figma-remote", "uri": "skill://figma/figma-use/SKILL.md"}`

**Tool call:** `ReadMcpResourceTool` `{"server": "figma-remote", "uri": "skill://figma/figma-use-figjam/SKILL.md"}`

**Tool result:** `ReadMcpResourceTool`

```text
"{\"contents\":[{\"uri\":\"skill://figma/figma-use-figjam/SKILL.md\",\"mimeType\":\"text/markdown\",\"text\":\"---\\nname: figma-use-figjam\\ndescription: \\\"This skill helps agents use Figma's use_figma MCP tool in the FigJam context. Can be used alongside figma-use which has foundational context for using the use_figma tool.\\\"\\ndisable-model-invocation: false\\n---\\n\\n# use_figma \u2014 Figma Plugin API Skill for FigJam\\n\\nThis skill contains FigJam-specific context for the `use_figma` MCP tool. The [figma-use](../figma-use/SKILL.md) skill provides foundational context for plugin API execution via MCP as well as the full Figma plugin API for more advanced use-cases that are not described here.\\n\\n**Always include `figma-use-figjam` in the comma-separated `skillNames` parameter when calling `use_figma` for FigJam operations. If this skill was loaded via an MCP resource, you MUST prefix the name with `resource:` (e.g. `resource:figma-use-figjam`).** This is a logging parameter used to track skill usage \u2014 it does not affect execution.\\n\\n> **FigJam URL is `figma.com/board/...`.** Do NOT call `figma.createPage()` in FigJam \u2014 it throws `TypeError: figma.createPage no such property 'createPage' on the figma global object`. `createPage()` is a Design-file API only (`figma.com/design/...`). FigJam files have a single implicit page; organize content with sections instead (see [create-section](references/create-section.md)).\\n\\n## Inspecting FigJam Files\\n\\n
```

**Tool result:** `ReadMcpResourceTool`

```text
"{\"contents\":[{\"uri\":\"skill://figma/figma-use/SKILL.md\",\"mimeType\":\"text/markdown\",\"text\":\"---\\nname: figma-use\\ndescription: \\\"**MANDATORY prerequisite** \u2014 you MUST invoke this skill BEFORE every `use_figma` tool call. NEVER call `use_figma` directly without loading this skill first. Skipping it causes common, hard-to-debug failures. Trigger whenever the user wants to perform a write action or a unique read action that requires JavaScript execution in the Figma file context \u2014 e.g. create/edit/delete nodes, set up variables or tokens, build components and variants, modify auto-layout or fills, bind variables to properties, or inspect file structure programmatically.\\\"\\ndisable-model-invocation: false\\n---\\n# use_figma \u2014 Figma Plugin API Skill\\nUse the `use_figma` tool to execute JavaScript in Figma files via the Plugin API. All detailed reference docs live in `references/`.\\n\\nWhen available, call `create_session` with `fileKey` and `description` before file reads or edits (create the file first if needed), then pass the returned `sessionId` unchanged to every call that accepts it, including follow-ups and work across files.\\n\\n**Always include `figma-use` in the comma-separated `skillNames` parameter when calling `use_figma`. If this skill was loaded via an MCP resource, you MUST prefix the name with `resource:` (e.g. `resource:figma-use`).** This is a logging parameter used to track skill usage \u2014 it does not affect execution.\\
```

**Tool call:** `mcp__figma-remote__get_figjam` `{"fileKey": "<draft-file-key>", "nodeId": "0:1", "includeImagesOfNodes": false, "sessionId": "de63346d-1f0a-48dc-a30d-5a55cb2bbd24"}`

**Tool result:** `mcp__figma-remote__get_figjam`

```text
[{"type": "text", "text": "<canvas id=\"0:1\" name=\"Page 1\" x=\"0\" y=\"0\" width=\"0\" height=\"0\">\n  <section id=\"1:3\" name=\"Start a return\" x=\"0\" y=\"0\" width=\"2808\" height=\"1136\">\n    <text id=\"1:4\" name=\"Start a return\" x=\"80\" y=\"80\" width=\"417\" height=\"77\" />\n    <text id=\"1:5\" name=\"How a Fernhouse customer starts a return in the app, from the order list to a confirmed return\" x=\"80\" y=\"173\" width=\"1440\" height=\"34\" />\n    <section id=\"1:6\" name=\"Find the order\" x=\"80\" y=\"272\" width=\"680\" height=\"308\">\n      <text id=\"1:7\" name=\"Find the order\" x=\"32\" y=\"32\" width=\"163\" height=\"29\" />\n      <shape-with-text id=\"1:12\" x=\"48\" y=\"164\" width=\"224\" height=\"96\" name=\"ROUNDED_RECTANGLE\">Order list</shape-with-text>\n      <shape-with-text id=\"1:16\" x=\"408\" y=\"164\" width=\"224\" height=\"96\" name=\"ROUNDED_RECTANGLE\">Order detail</shape-with-text>\n      <connector id=\"1:40\" x=\"276.5\" y=\"212\" connectorStart=\"1:12\" connectorStartCap=\"NONE\" connectorEnd=\"1:16\" connectorEndCap=\"ARROW_LINES\">edge:orders-&amp;gt;detail</connector>\n    </section>\n    <section id=\"1:8\" name=\"Request the return\" x=\"828\" y=\"272\" width=\"1392\" height=\"484\">\n      <text id=\"1:9\" name=\"Request the return\" x=\"32\" y=\"32\" width=\"218\" height=\"29\" />\n      <shape-with-text id=\"1:20\" x=\"48\" y=\"96\" width=\"360\" height=\"232\" name=\"DIAMOND\">Within 30 days of delivery?</shape-w
```

**Tool call:** `Bash` `{"command": "cat $(cat /tmp/loomlist-scratch-path)/board1.js"}`

**Tool result:** `Bash`

```text
"<persisted-output>\nOutput too large (40.4KB). Full output saved to: /Users/michelkerkmeester/.claude/projects/-private-var-folders-3c-zfqcqsts0kn19cgblj82gqhm0000gn-T-devin-compare-bench-FJ-029/392818cd-506d-45d4-93f0-73919b09895c/tool-results/bfu5g61xr.txt\n\nPreview (first 2KB):\nconst MODEL={\"type\":\"graph\",\"profile\":\"user-flow\",\"direction\":\"LR\",\"zoneMode\":\"stage\",\"zones\":[],\"nodes\":[{\"id\":\"landing\",\"label\":\"Landing page\",\"kind\":\"start\"},{\"id\":\"signUp\",\"label\":\"Sign up with email or Google\",\"kind\":\"screen\"},{\"id\":\"verify\",\"label\":\"Verify the email code\",\"kind\":\"screen\"},{\"id\":\"codeOk\",\"label\":\"Code correct?\",\"kind\":\"decision\",\"accent\":true},{\"id\":\"verified\",\"label\":\"Email verified\",\"kind\":\"success\"},{\"id\":\"codeError\",\"label\":\"Wrong code error with resend\",\"kind\":\"screen\"}],\"edges\":[{\"from\":\"landing\",\"to\":\"signUp\"},{\"from\":\"signUp\",\"to\":\"verify\"},{\"from\":\"verify\",\"to\":\"codeOk\"},{\"from\":\"codeOk\",\"to\":\"verified\",\"label\":\"Yes\"},{\"from\":\"codeOk\",\"to\":\"codeError\",\"label\":\"No\"},{\"from\":\"codeError\",\"to\":\"verify\"}],\"expect\":{\"nodes\":6,\"connectors\":6},\"title\":\"1. Sign up\",\"subtitle\":\"How a new Loomlist user goes from the landing page to a verified email, for the product and design teams\",\"source\":\"Sources: the Loomlist onboarding doc as described in the request. Left out: expired codes, network failures and Google-s
```

**Tool call:** `Read` `{"file_path": "/Users/michelkerkmeester/.claude/projects/-private-var-folders-3c-zfqcqsts0kn19cgblj82gqhm0000gn-T-devin-compare-bench-FJ-029/392818cd-506d-45d4-93f0-73919b09895c/tool-results/bfu5g61xr.txt", "allow_large": true}`

**Tool result:** `Read`

```text
"1\tconst MODEL={\"type\":\"graph\",\"profile\":\"user-flow\",\"direction\":\"LR\",\"zoneMode\":\"stage\",\"zones\":[],\"nodes\":[{\"id\":\"landing\",\"label\":\"Landing page\",\"kind\":\"start\"},{\"id\":\"signUp\",\"label\":\"Sign up with email or Google\",\"kind\":\"screen\"},{\"id\":\"verify\",\"label\":\"Verify the email code\",\"kind\":\"screen\"},{\"id\":\"codeOk\",\"label\":\"Code correct?\",\"kind\":\"decision\",\"accent\":true},{\"id\":\"verified\",\"label\":\"Email verified\",\"kind\":\"success\"},{\"id\":\"codeError\",\"label\":\"Wrong code error with resend\",\"kind\":\"screen\"}],\"edges\":[{\"from\":\"landing\",\"to\":\"signUp\"},{\"from\":\"signUp\",\"to\":\"verify\"},{\"from\":\"verify\",\"to\":\"codeOk\"},{\"from\":\"codeOk\",\"to\":\"verified\",\"label\":\"Yes\"},{\"from\":\"codeOk\",\"to\":\"codeError\",\"label\":\"No\"},{\"from\":\"codeError\",\"to\":\"verify\"}],\"expect\":{\"nodes\":6,\"connectors\":6},\"title\":\"1. Sign up\",\"subtitle\":\"How a new Loomlist user goes from the landing page to a verified email, for the product and design teams\",\"source\":\"Sources: the Loomlist onboarding doc as described in the request. Left out: expired codes, network failures and Google-specific steps.\"};\n2\tconst THEME={};\n3\tconst SWATCH={\n4\twhite:['#FFFFFF','#B3B3B3','#1E1E1E'],black:['#1E1E1E','#B3B3B3','#FFFFFF'],\n5\tdarkGray:['#757575','#5E5E5E','#FFFFFF'],violet:['#874FFF','#5427B4','#FFFFFF'],\n6\tlightBlue:['#C2E5FF','#3DADFF','#1E1E1E'],lightGreen:
```

**Tool call:** `mcp__figma-remote__use_figma` `{"fileKey": "<draft-file-key>", "sessionId": "de63346d-1f0a-48dc-a30d-5a55cb2bbd24", "skillNames": "resource:figma-use,resource:figma-use-figjam", "description": "Compose board \"1. Sign up\" (user flow, 6 nodes, 6 connectors) as a new section beside the existing content", "code": "const MODEL={\"type\":\"graph\",\"profile\":\"user-flow\",\"direction\":\"LR\",\"zoneMode\":\"stage\",\"zones\":[],\"nodes\":[{\"id\":\"landing\",\"label\":\"Landing page\",\"kind\":\"start\"},{\"id\":\"signUp\",\"label\":\"Sign up with email or Google\",\"kind\":\"screen\"},{\"id\":\"verify\",\"label\":\"Veri`

**Tool result:** `mcp__figma-remote__use_figma`

```text
[{"type": "text", "text": "{\"boardId\":\"2:60\",\"tag\":{\"namespace\":\"productowner\",\"key\":\"1. Sign up\"},\"bounds\":{\"x\":3208,\"y\":0,\"w\":1856,\"h\":952},\"counts\":{\"nodes\":6,\"connectors\":6},\"expect\":{\"nodes\":6,\"connectors\":6},\"elements\":[{\"id\":\"2:63\",\"model\":\"landing\",\"kind\":\"start\",\"text\":\"Landing page\"},{\"id\":\"2:67\",\"model\":\"signUp\",\"kind\":\"screen\",\"text\":\"Sign up with email or Google\"},{\"id\":\"2:71\",\"model\":\"verify\",\"kind\":\"screen\",\"text\":\"Verify the email code\"},{\"id\":\"2:75\",\"model\":\"codeOk\",\"kind\":\"decision\",\"text\":\"Code correct?\"},{\"id\":\"2:79\",\"model\":\"verified\",\"kind\":\"success\",\"text\":\"Email verified\"},{\"id\":\"2:83\",\"model\":\"codeError\",\"kind\":\"screen\",\"text\":\"Wrong code error with resend\"}],\"links\":[{\"id\":\"2:87\",\"from\":\"2:63\",\"to\":\"2:67\",\"model\":\"landing->signUp\",\"label\":\"\"},{\"id\":\"2:91\",\"from\":\"2:67\",\"to\":\"2:71\",\"model\":\"signUp->verify\",\"label\":\"\"},{\"id\":\"2:95\",\"from\":\"2:71\",\"to\":\"2:75\",\"model\":\"verify->codeOk\",\"label\":\"\"},{\"id\":\"2:99\",\"from\":\"2:75\",\"to\":\"2:79\",\"model\":\"codeOk->verified\",\"label\":\"Yes\"},{\"id\":\"2:117\",\"from\":\"2:75\",\"to\":\"2:83\",\"model\":\"codeOk->codeError\",\"label\":\"No\",\"via\":\"waypoints\"},{\"id\":\"2:128\",\"from\":\"2:83\",\"to\":\"2:71\",\"model\":\"codeError->verify\",\"label\":\"\",\"via\":\"waypoints\"}],\"warnings\":[],\"created
```

**Assistant:**

Board 1 is written with no warnings. I'm composing board 2, "2. Workspace setup", next.

**Tool call:** `Bash` `{"command": "SCR=$(cat /tmp/loomlist-scratch-path); head -c 1700 $SCR/board2.js | head -2; diff <(sed 1,2d $SCR/board1.js) <(sed 1,2d $SCR/board2.js) && echo \"bodies identical after line 2\"; sed -n 2p $SCR/board2.js"}`

**Tool result (error):** `Bash`

```text
"Exit code 1\ncat: /tmp/loomlist-scratch-path: No such file or directory\nhead: /board2.js: No such file or directory\nsed: /board1.js: No such file or directory\nsed: /board2.js: No such file or directory\nbodies identical after line 2\nsed: /board2.js: No such file or directory"
```

**Tool call:** `Bash` `{"command": "ls -d /tmp/loomlist* 2>&1; ls /private/tmp 2>&1 | head; echo $TMPDIR"}`

**Tool result:** `Bash`

```text
"/tmp/loomlist-block-sync-board.js\n/tmp/loomlist-block-sync-model.md\n/tmp/loomlist-flow.gl6qVB\n_py.txt\n_unused\n_unused_err\n_v.txt\n_x\n004-description.before.json\n004-graph-metadata.before.json\n04BD8F52-DB71-4064-80F1-3E0B5F3B6827\n053-001-graph-metadata.before.json\n053-002-status-before-review.txt\n/var/folders/3c/zfqcqsts0kn19cgblj82gqhm0000gn/T/devin-compare-bench/.sessions/FJ-029/tmp"
```

**Tool call:** `Bash` `{"command": "SCR=/tmp/loomlist-flow.gl6qVB; ls $SCR; sed -n 1p $SCR/board2.js; diff <(sed 1d $SCR/board1.js) <(sed 1d $SCR/board2.js) && echo \"rest identical\""}`

**Tool result:** `Bash`

```text
"board1.js\nboard2.js\nmodel.md\nconst MODEL={\"type\":\"graph\",\"profile\":\"user-flow\",\"direction\":\"LR\",\"zoneMode\":\"stage\",\"zones\":[],\"nodes\":[{\"id\":\"verified\",\"label\":\"Email verified\",\"kind\":\"start\"},{\"id\":\"plan\",\"label\":\"Free or team plan?\",\"kind\":\"decision\",\"accent\":true},{\"id\":\"name\",\"label\":\"Name the workspace\",\"kind\":\"screen\"},{\"id\":\"invite\",\"label\":\"Invite teammates by email, or skip\",\"kind\":\"screen\"},{\"id\":\"template\",\"label\":\"Pick a template or start blank\",\"kind\":\"screen\"},{\"id\":\"editor\",\"label\":\"Editor opens with welcome tip\",\"kind\":\"success\"}],\"edges\":[{\"from\":\"verified\",\"to\":\"plan\"},{\"from\":\"plan\",\"to\":\"name\",\"label\":\"Free\"},{\"from\":\"plan\",\"to\":\"invite\",\"label\":\"Team\"},{\"from\":\"invite\",\"to\":\"name\"},{\"from\":\"name\",\"to\":\"template\"},{\"from\":\"template\",\"to\":\"editor\"}],\"expect\":{\"nodes\":6,\"connectors\":6},\"title\":\"2. Workspace setup\",\"subtitle\":\"How a verified Loomlist user picks a plan and a workspace and reaches the editor, for the product and design teams\",\"source\":\"Sources: the Loomlist onboarding doc as described in the request. Left out: Team billing and what invited teammates see.\"};\nrest identical"
```

**Tool call:** `mcp__figma-remote__use_figma` `{"fileKey": "<draft-file-key>", "sessionId": "de63346d-1f0a-48dc-a30d-5a55cb2bbd24", "skillNames": "resource:figma-use,resource:figma-use-figjam", "description": "Compose board \"2. Workspace setup\" (user flow, 6 nodes, 6 connectors) as a new section to the right of board 1", "code": "const MODEL={\"type\":\"graph\",\"profile\":\"user-flow\",\"direction\":\"LR\",\"zoneMode\":\"stage\",\"zones\":[],\"nodes\":[{\"id\":\"verified\",\"label\":\"Email verified\",\"kind\":\"start\"},{\"id\":\"plan\",\"label\":\"Free or team plan?\",\"kind\":\"decision\",\"accent\":true},{\"id\":\"name\",\"lab`

**Tool result:** `mcp__figma-remote__use_figma`

```text
[{"type": "text", "text": "{\"boardId\":\"3:115\",\"tag\":{\"namespace\":\"productowner\",\"key\":\"2. Workspace setup\"},\"bounds\":{\"x\":5464,\"y\":0,\"w\":2248,\"h\":912},\"counts\":{\"nodes\":6,\"connectors\":6},\"expect\":{\"nodes\":6,\"connectors\":6},\"elements\":[{\"id\":\"3:118\",\"model\":\"verified\",\"kind\":\"start\",\"text\":\"Email verified\"},{\"id\":\"3:122\",\"model\":\"plan\",\"kind\":\"decision\",\"text\":\"Free or team plan?\"},{\"id\":\"3:126\",\"model\":\"name\",\"kind\":\"screen\",\"text\":\"Name the workspace\"},{\"id\":\"3:130\",\"model\":\"invite\",\"kind\":\"screen\",\"text\":\"Invite teammates by email, or skip\"},{\"id\":\"3:134\",\"model\":\"template\",\"kind\":\"screen\",\"text\":\"Pick a template or start blank\"},{\"id\":\"3:138\",\"model\":\"editor\",\"kind\":\"success\",\"text\":\"Editor opens with welcome tip\"}],\"links\":[{\"id\":\"3:142\",\"from\":\"3:118\",\"to\":\"3:122\",\"model\":\"verified->plan\",\"label\":\"\"},{\"id\":\"3:160\",\"from\":\"3:122\",\"to\":\"3:126\",\"model\":\"plan->name\",\"label\":\"Free\",\"via\":\"waypoints\"},{\"id\":\"3:164\",\"from\":\"3:122\",\"to\":\"3:130\",\"model\":\"plan->invite\",\"label\":\"Team\"},{\"id\":\"3:168\",\"from\":\"3:130\",\"to\":\"3:126\",\"model\":\"invite->name\",\"label\":\"\"},{\"id\":\"3:172\",\"from\":\"3:126\",\"to\":\"3:134\",\"model\":\"name->template\",\"label\":\"\"},{\"id\":\"3:176\",\"from\":\"3:134\",\"to\":\"3:138\",\"model\":\"template->editor\",\"label\":\"\"}],\"warni
```

**Assistant:**

Both boards are written with no warnings. Next is the read-back from the file.

**Tool call:** `mcp__figma-remote__get_figjam` `{"fileKey": "<draft-file-key>", "nodeId": "0:1", "includeImagesOfNodes": false, "sessionId": "de63346d-1f0a-48dc-a30d-5a55cb2bbd24"}`

**Tool result:** `mcp__figma-remote__get_figjam`

```text
[{"type": "text", "text": "<canvas id=\"0:1\" name=\"Page 1\" x=\"0\" y=\"0\" width=\"0\" height=\"0\">\n  <section id=\"1:3\" name=\"Start a return\" x=\"0\" y=\"0\" width=\"2808\" height=\"1136\">\n    <text id=\"1:4\" name=\"Start a return\" x=\"80\" y=\"80\" width=\"417\" height=\"77\" />\n    <text id=\"1:5\" name=\"How a Fernhouse customer starts a return in the app, from the order list to a confirmed return\" x=\"80\" y=\"173\" width=\"1440\" height=\"34\" />\n    <section id=\"1:6\" name=\"Find the order\" x=\"80\" y=\"272\" width=\"680\" height=\"308\">\n      <text id=\"1:7\" name=\"Find the order\" x=\"32\" y=\"32\" width=\"163\" height=\"29\" />\n      <shape-with-text id=\"1:12\" x=\"48\" y=\"164\" width=\"224\" height=\"96\" name=\"ROUNDED_RECTANGLE\">Order list</shape-with-text>\n      <shape-with-text id=\"1:16\" x=\"408\" y=\"164\" width=\"224\" height=\"96\" name=\"ROUNDED_RECTANGLE\">Order detail</shape-with-text>\n      <connector id=\"1:40\" x=\"276.5\" y=\"212\" connectorStart=\"1:12\" connectorStartCap=\"NONE\" connectorEnd=\"1:16\" connectorEndCap=\"ARROW_LINES\">edge:orders-&amp;gt;detail</connector>\n    </section>\n    <section id=\"1:8\" name=\"Request the return\" x=\"828\" y=\"272\" width=\"1392\" height=\"484\">\n      <text id=\"1:9\" name=\"Request the return\" x=\"32\" y=\"32\" width=\"218\" height=\"29\" />\n      <shape-with-text id=\"1:20\" x=\"48\" y=\"96\" width=\"360\" height=\"232\" name=\"DIAMOND\">Within 30 days of delivery?</shape-w
```

**Tool call:** `Bash` `{"command": "rm -rf /tmp/loomlist-flow.gl6qVB; ls -d /tmp/loomlist-flow.* 2>&1 | head -1; cd /private/var/folders/3c/zfqcqsts0kn19cgblj82gqhm0000gn/T/devin-compare-bench/FJ-029 && ls export; git status --short | head -30"}`

**Tool result:** `Bash`

```text
"(eval):1: no matches found: /tmp/loomlist-flow.*\n?? .devin/\n?? .env.example\n?? .gitignore\n?? AGENTS.md\n?? Favicon.jpg\n?? LICENSE\n?? README.md\n?? ROUTER.md\n?? SKILL.md\n?? SYNC.md\n?? USER-GUIDE.md\n?? context/\n?? description.json\n?? graph-metadata.json\n?? hub-router.json\n?? leaf-manifest.json\n?? mcp-click-up/\n?? mcp-code-mode/\n?? mcp-figma/\n?? mode-registry.json\n?? scripts/\n?? sk-create-figjam/\n?? sk-product-owner/\n?? vendor.json"
```

**Assistant:**

<figma-url> (1. Sign up) and <figma-url> (2. Workspace setup)
Read-back: 1. Sign up has 6 of 6 nodes, 6 of 6 connectors and 2 of 2 decision exits labelled. 2. Workspace setup has 6 of 6 nodes, 6 of 6 connectors and 2 of 2 decision exits labelled. The existing "Start a return" section is unchanged, with the same ids, positions and sizes as before the write. First glance: the "Code correct?" decision on board 1 and the "Free or team plan?" decision on board 2. Start here: 1. Sign up
Left out: expired codes, network failures, Google-specific steps, Team billing and what invited teammates see, because the doc as you described it states none of them
Finding: The board went into the existing file as two new sections, so no plan was involved. Nothing was created in the Loomlist Product plan or the Barter plan.
Finding: I never saw the onboarding doc, because it isn't in the repo. The boards rest on your description, which I treated as current behavior.
Finding: Four connections are my reading rather than stated in the doc.
* The wrong-code error returns to the code screen.
* Sign up with email or Google is one screen with no branch.
* Skipping the teammate invite is part of that screen, not a separate exit.
* Template or blank is one screen.

Finding: `get_figjam` doesn't return connector text. The Yes, No, Free and Team labels were confirmed on the composing screenshots, not in the board read.
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.
