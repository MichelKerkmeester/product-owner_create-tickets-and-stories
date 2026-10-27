# FJ-025 turn 1 transcript

**User:** $figjam draw the Roamstay checkout payment as a sequence diagram on a new board in our Roamstay Product plan. From the payments brief: the guest app posts the booking, the booking API holds the room, asks the payment provider to authorise the card, confirms the hold, tells the partner hub and answers the app with 201. A declined card releases the hold and returns 402.

Write the board into the existing FigJam file with key <test-file-key> rather than a new file.

**Assistant:**

I’m applying the FigJam Flow Mode instructions and will check the required sequence-diagram rules and board context before I make any changes.

**Tool call:** `read_mcp_resource` `{"server": "codex_apps", "uri": "skill://figma/figma-use/SKILL.md"}`

**Tool result (error):** `read_mcp_resource`

```text
{'message': 'resources/read failed: resources/read failed for `codex_apps` (skill://figma/figma-use/SKILL.md): Mcp error: -32002: Unknown resource({"uri":"skill://figma/figma-use/SKILL.md"})'}
```

**Tool call:** `read_mcp_resource` `{"server": "figma", "uri": "skill://figma/figma-use/SKILL.md"}`

**Tool result (error):** `read_mcp_resource`

```text
{'message': "resources/read failed: unknown MCP server 'figma'"}
```

**Tool call:** `list_mcp_resources` `{"server": "codex_apps"}`

**Tool result:** `list_mcp_resources`

```text
{'content': [{'type': 'text', 'text': '{"server":"codex_apps","resources":[{"server":"codex_apps","uri":"plugin://plugin_asdk_app_69431e6d26b88191b4029488aeb42f5b","name":"plugin_asdk_app_69431e6d26b88191b4029488aeb42f5b","title":"ClickUp","description":"Manage tasks, collaborate with your team, and ship work without leaving ChatGPT or Codex. Post comments with threaded replies and @mentions to keep conversations moving. Send messages in ClickUp Chat. Write and edit Docs and pages. Track time, set custom fields, and search your entire workspace in natural language. Every action syncs to ClickUp in real time, so teammates see your updates instantly.","mimeType":"mcp/plugin","_meta":{"plugin_id":"plugin_asdk_app_69431e6d26b88191b4029488aeb42f5b","plugin_name":"clickup","plugin_release_id":"pluginrel_84dbc156884881918831ad8744442705","plugin_release_version":"2.0.0","apps":["app://asdk_app_69431e6d26b88191b4029488aeb42f5b"],"skills":[],"requires_executor":false,"mcp_servers":[],"contents":["bundle"],"bundle":"plugin://plugin_asdk_app_69431e6d26b88191b4029488aeb42f5b/bundle"}},{"server":"codex_apps","uri":"plugin://plugin_connector_1p_2330815c823c8191941e5dc465bb899f","name":"plugin_connector_1p_2330815c823c8191941e5dc465bb899f","title":"Default templates","description":"OpenAI default document, presentation, and spreadsheet templates.","mimeType":"mcp/plugin","_meta":{"plugin_id":"plugin_connector_1p_2330815c823c8191941e5dc465bb899f","plugin_name":"openai-templates","plugin_rele
```

**Assistant:**

I’m also loading the required Figma sequence-diagram guidance so the board uses the supported Mermaid structure.

**Tool call:** `read_mcp_resource` `{"server": "codex_apps", "uri": "skill://plugin_connector_68df038e0ba48191908c8434991bbac2/figma-generate-diagram"}`

**Tool result:** `read_mcp_resource`

```text
{'content': [{'type': 'text', 'text': '{"server":"codex_apps","uri":"skill://plugin_connector_68df038e0ba48191908c8434991bbac2/figma-generate-diagram","contents":[{"uri":"skill://plugin_connector_68df038e0ba48191908c8434991bbac2/figma-generate-diagram/SKILL.md","mimeType":"text/markdown","text":"---\\nname: figma-generate-diagram\\ndescription: \\"MANDATORY prerequisite — load this skill BEFORE every `generate_diagram` tool call. NEVER call `generate_diagram` directly without loading this skill first. Trigger whenever the user asks to create, generate, draw, render, sketch, or build a diagram — flowchart, architecture diagram, sequence diagram, ERD or entity-relationship diagram, state diagram or state machine, gantt chart, or timeline. Also trigger when the user mentions Mermaid syntax or wants a system architecture, decision tree, dependency graph, API call flow, auth handshake, schema, or pipeline visualized in FigJam. Routes to type-specific guidance, sets universal Mermaid constraints, and tells you when to use a different diagram type or skip the tool entirely (mindmaps, pie charts, class diagrams, etc.).\\"\\n---\\n\\n# generate-diagram\\n\\n**You MUST load this skill before every `generate_diagram` tool call.** Skipping it causes preventable rendering failures and low-quality output.\\n\\n`generate_diagram` takes Mermaid.js syntax and produces an editable FigJam diagram. This skill routes you to the right per-type guidance and sets universal constraints.\\n\\n## Step 
```

**Tool call:** `read_mcp_resource` `{"server": "codex_apps", "uri": "skill://plugin_connector_68df038e0ba48191908c8434991bbac2/figma-generate-diagram/references/sequence.md"}`

**Tool result:** `read_mcp_resource`

```text
{'content': [{'type': 'text', 'text': '{"server":"codex_apps","uri":"skill://plugin_connector_68df038e0ba48191908c8434991bbac2/figma-generate-diagram/references/sequence.md","contents":[{"uri":"skill://plugin_connector_68df038e0ba48191908c8434991bbac2/figma-generate-diagram/references/sequence.md","mimeType":"text/markdown","text":"# Sequence Diagrams\\n\\nUse this reference for **sequence diagrams** — interactions over time between parties (services, users, systems). API request/response flows, auth handshakes, multi-service choreography, RPC call traces, event cascades.\\n\\nThe renderer is a **narrow subset** of full Mermaid sequence — read §5 carefully, because several features people commonly reach for (notes, loops, alt/else, activation boxes, colored blocks, autonumber) are silently dropped by our handler. The good news: most of those can be added back on top of the generated diagram with `use_figma` — see §7 for the hybrid workflow.\\n\\n## Contents\\n\\n1. [When to use a sequence diagram](#1-when-to-use-a-sequence-diagram)\\n2. [Required skeleton](#2-required-skeleton)\\n3. [Participants](#3-participants)\\n4. [Messages](#4-messages)\\n5. [What\'s NOT supported](#5-whats-not-supported)\\n6. [Best practices](#6-best-practices)\\n7. [Hybrid workflow: `generate_diagram` first, then `use_figma` for everything else](#7-hybrid-workflow-generate_diagram-first-then-use_figma-for-everything-else)\\n8. [Validation checklist](#8-validation-checklist)\\n9. [Complete example](#9-
```

**Tool call:** `figma.create_session` `{"fileKey": "<test-file-key>", "description": "Add the Roamstay checkout payment sequence diagram(s) to the existing FigJam file"}`

**Tool result:** `figma.create_session`

```text
{'content': [{'type': 'text', 'text': '{"sessionId":"fa258de3-960c-42a3-be88-f9dff2f34bc0"}'}], '_meta': {'mcpRequestId': '337a5e06-c5dc-4e9f-89d6-e2a04deba44d', 'io.modelcontextprotocol/serverInfo': {'name': 'Figma MCP Server', 'version': '1.0.0', 'icons': [{'src': 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIAAAACgCAYAAADEkmT9AAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAhGVYSWZNTQAqAAAACAAFARIAAwAAAAEAAQAAARoABQAAAAEAAABKARsABQAAAAEAAABSASgAAwAAAAEAAgAAh2kABAAAAAEAAABaAAAAAAAAAEgAAAABAAAASAAAAAEAA6ABAAMAAAABAAEAAKACAAQAAAABAAAAgKADAAQAAAABAAAAoAAAAAB6dUZwAAAACXBIWXMAAAsTAAALEwEAmpwYAAABWWlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iWE1QIENvcmUgNi4wLjAiPgogICA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPgogICAgICA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIgogICAgICAgICAgICB4bWxuczp0aWZmPSJodHRwOi8vbnMuYWRvYmUuY29tL3RpZmYvMS4wLyI+CiAgICAgICAgIDx0aWZmOk9yaWVudGF0aW9uPjE8L3RpZmY6T3JpZW50YXRpb24+CiAgICAgIDwvcmRmOkRlc2NyaXB0aW9uPgogICA8L3JkZjpSREY+CjwveDp4bXBtZXRhPgoZXuEHAAARfklEQVR4Ae1de4xU1Rn/zr1zd5ddWFgRorEvAkrUAhURSgx2MI3PVEvMbuTV1jZVu2Aq/GGFBBhsUtBUaNr6jNZWqCbMH2gbEK3pbtWGiiBBomktCbamUSG47rLvmXtPf9+5c5fdZRd2Zu7unoHvJPO6j3O+8/se5zvf+c4dIimCgCAgCAgCgoAgIAgIAoKAICAICAKCgCAgCAgCgoAgIAgIAoKAICAICAKCgCAgCAgCgoAgIAgIAoKAICAICAKCgCAgCAgCgoAgIAgIAoKAICAICAKCgCAgCAgCgoAgIAgIAoKAICAICAKCgCAgCAgCgoAgIAgIAoKAICAICAKCgCAgCAgCgoAgYAsCyhZCCqVDEzmUTDqF3k/Jgu/EjY2BSl
```

**Tool call:** `figma.whoami` `{}`

**Tool result:** `figma.whoami`

```text
{'content': [{'type': 'text', 'text': '{"whoami":{"user_id":"<redacted>","handle":"<redacted>","email":"<email>","code_layers_enabled":true,"plans":[{"name":"<figma-plan-3>","seat":"View","tier":"starter","key":"team::<plan-id>","role":"admin","specs_enabled":true,"code_layers_enabled":true},{"name":"<figma-plan-1>","seat":"Full","tier":"pro","key":"team::<plan-id>","role":"admin","specs_enabled":false,"code_layers_enabled":true},{"name":"<figma-plan-2>","seat":"Full","tier":"pro","key":"team::<plan-id>","role":"member","specs_enabled":false,"code_layers_enabled":true}]},"instructions":"For more details on rate limits and access, refer to https://developers.figma.com/docs/figma-mcp-server/rate-limits-access/"}'}], '_meta': {'mcpRequestId': 'd4481f0e-21b5-4280-885e-1bf0fb9cd565', 'io.modelcontextprotocol/serverInfo': {'name': 'Figma MCP Server', 'version': '1.0.0', 'icons': [{'src': 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIAAAACgCAYAAADEkmT9AAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAhGVYSWZNTQAqAAAACAAFARIAAwAAAAEAAQAAARoABQAAAAEAAABKARsABQAAAAEAAABSASgAAwAAAAEAAgAAh2kABAAAAAEAAABaAAAAAAAAAEgAAAABAAAASAAAAAEAA6ABAAMAAAABAAEAAKACAAQAAAABAAAAgKADAAQAAAABAAAAoAAAAAB6dUZwAAAACXBIWXMAAAsTAAALEwEAmpwYAAABWWlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iWE1QIENvcmUgNi4wLjAiPgogICA8cmRmOlJERiB4bWxuczpyZGY9Imh0dH
```

**Assistant:**

The connected Figma account doesn’t list a plan named “Roamstay Product”; the existing file key you supplied is the clear write target, so I’m checking that file directly and will keep the diagram there.

**Tool call:** `figma.get_figjam` `{"fileKey": "<test-file-key>", "nodeId": "0:1", "sessionId": "fa258de3-960c-42a3-be88-f9dff2f34bc0"}`

**Tool result:** `figma.get_figjam`

```text
{'content': [{'type': 'text', 'text': '<canvas id="0:1" name="Page 1" x="0" y="0" width="0" height="0">\n  <shape-with-text id="1:3" x="768" y="-492" width="224" height="128" name="ROUNDED_RECTANGLE">Order list</shape-with-text>\n  <shape-with-text id="1:6" x="768" y="-236" width="224" height="128" name="SQUARE">Order detail</shape-with-text>\n  <shape-with-text id="1:9" x="780" y="20" width="200" height="200" name="DIAMOND">Within 30 days?</shape-with-text>\n  <shape-with-text id="1:12" x="608" y="476" width="224" height="128" name="ROUNDED_RECTANGLE">Contact support</shape-with-text>\n  <shape-with-text id="1:15" x="928" y="476" width="224" height="128" name="SQUARE">Pick a reason</shape-with-text>\n  <shape-with-text id="1:18" x="940" y="732" width="200" height="200" name="DIAMOND">Drop-off or pickup?</shape-with-text>\n  <shape-with-text id="1:21" x="768" y="1188" width="224" height="128" name="SQUARE">Choose a drop-off point</shape-with-text>\n  <shape-with-text id="1:24" x="1088" y="1188" width="224" height="128" name="SQUARE">Book a courier pickup</shape-with-text>\n  <shape-with-text id="1:27" x="928" y="1444" width="224" height="128" name="ROUNDED_RECTANGLE">Return confirmed with QR code</shape-with-text>\n  <connector id="1:30" x="880" y="-356" connectorStart="1:3" connectorStartCap="NONE" connectorEnd="1:6" connectorEndCap="ARROW_LINES"></connector>\n  <connector id="1:34" x="880" y="-100" connectorStart="1:6" connectorStartCap="NONE" connectorEnd="1:9" connectorEn
```

**Tool call:** `figma.get_figjam` `{"fileKey": "<test-file-key>", "nodeId": "0:1", "sessionId": "fa258de3-960c-42a3-be88-f9dff2f34bc0"}`

**Tool result:** `figma.get_figjam`

```text
{'content': [{'type': 'text', 'text': '<canvas id="0:1" name="Page 1" x="0" y="0" width="0" height="0">\n  <shape-with-text id="1:3" x="768" y="-492" width="224" height="128" name="ROUNDED_RECTANGLE">Order list</shape-with-text>\n  <shape-with-text id="1:6" x="768" y="-236" width="224" height="128" name="SQUARE">Order detail</shape-with-text>\n  <shape-with-text id="1:9" x="780" y="20" width="200" height="200" name="DIAMOND">Within 30 days?</shape-with-text>\n  <shape-with-text id="1:12" x="608" y="476" width="224" height="128" name="ROUNDED_RECTANGLE">Contact support</shape-with-text>\n  <shape-with-text id="1:15" x="928" y="476" width="224" height="128" name="SQUARE">Pick a reason</shape-with-text>\n  <shape-with-text id="1:18" x="940" y="732" width="200" height="200" name="DIAMOND">Drop-off or pickup?</shape-with-text>\n  <shape-with-text id="1:21" x="768" y="1188" width="224" height="128" name="SQUARE">Choose a drop-off point</shape-with-text>\n  <shape-with-text id="1:24" x="1088" y="1188" width="224" height="128" name="SQUARE">Book a courier pickup</shape-with-text>\n  <shape-with-text id="1:27" x="928" y="1444" width="224" height="128" name="ROUNDED_RECTANGLE">Return confirmed with QR code</shape-with-text>\n  <connector id="1:30" x="880" y="-356" connectorStart="1:3" connectorStartCap="NONE" connectorEnd="1:6" connectorEndCap="ARROW_LINES"></connector>\n  <connector id="1:34" x="880" y="-100" connectorStart="1:6" connectorStartCap="NONE" connectorEnd="1:9" connectorEn
```

**Tool call:** `figma.get_figjam` `{"fileKey": "<test-file-key>", "nodeId": "0:1", "sessionId": "fa258de3-960c-42a3-be88-f9dff2f34bc0"}`

**Tool result:** `figma.get_figjam`

```text
{'content': [{'type': 'text', 'text': '<canvas id="0:1" name="Page 1" x="0" y="0" width="0" height="0">\n  <shape-with-text id="1:3" x="768" y="-492" width="224" height="128" name="ROUNDED_RECTANGLE">Order list</shape-with-text>\n  <shape-with-text id="1:6" x="768" y="-236" width="224" height="128" name="SQUARE">Order detail</shape-with-text>\n  <shape-with-text id="1:9" x="780" y="20" width="200" height="200" name="DIAMOND">Within 30 days?</shape-with-text>\n  <shape-with-text id="1:12" x="608" y="476" width="224" height="128" name="ROUNDED_RECTANGLE">Contact support</shape-with-text>\n  <shape-with-text id="1:15" x="928" y="476" width="224" height="128" name="SQUARE">Pick a reason</shape-with-text>\n  <shape-with-text id="1:18" x="940" y="732" width="200" height="200" name="DIAMOND">Drop-off or pickup?</shape-with-text>\n  <shape-with-text id="1:21" x="768" y="1188" width="224" height="128" name="SQUARE">Choose a drop-off point</shape-with-text>\n  <shape-with-text id="1:24" x="1088" y="1188" width="224" height="128" name="SQUARE">Book a courier pickup</shape-with-text>\n  <shape-with-text id="1:27" x="928" y="1444" width="224" height="128" name="ROUNDED_RECTANGLE">Return confirmed with QR code</shape-with-text>\n  <connector id="1:30" x="880" y="-356" connectorStart="1:3" connectorStartCap="NONE" connectorEnd="1:6" connectorEndCap="ARROW_LINES"></connector>\n  <connector id="1:34" x="880" y="-100" connectorStart="1:6" connectorStartCap="NONE" connectorEnd="1:9" connectorEn
```

**Tool call:** `figma.get_figjam` `{"fileKey": "<test-file-key>", "nodeId": "0:1", "sessionId": "fa258de3-960c-42a3-be88-f9dff2f34bc0"}`

**Tool result:** `figma.get_figjam`

```text
{'content': [{'type': 'text', 'text': '<canvas id="0:1" name="Page 1" x="0" y="0" width="0" height="0">\n  <shape-with-text id="1:3" x="768" y="-492" width="224" height="128" name="ROUNDED_RECTANGLE">Order list</shape-with-text>\n  <shape-with-text id="1:6" x="768" y="-236" width="224" height="128" name="SQUARE">Order detail</shape-with-text>\n  <shape-with-text id="1:9" x="780" y="20" width="200" height="200" name="DIAMOND">Within 30 days?</shape-with-text>\n  <shape-with-text id="1:12" x="608" y="476" width="224" height="128" name="ROUNDED_RECTANGLE">Contact support</shape-with-text>\n  <shape-with-text id="1:15" x="928" y="476" width="224" height="128" name="SQUARE">Pick a reason</shape-with-text>\n  <shape-with-text id="1:18" x="940" y="732" width="200" height="200" name="DIAMOND">Drop-off or pickup?</shape-with-text>\n  <shape-with-text id="1:21" x="768" y="1188" width="224" height="128" name="SQUARE">Choose a drop-off point</shape-with-text>\n  <shape-with-text id="1:24" x="1088" y="1188" width="224" height="128" name="SQUARE">Book a courier pickup</shape-with-text>\n  <shape-with-text id="1:27" x="928" y="1444" width="224" height="128" name="ROUNDED_RECTANGLE">Return confirmed with QR code</shape-with-text>\n  <connector id="1:30" x="880" y="-356" connectorStart="1:3" connectorStartCap="NONE" connectorEnd="1:6" connectorEndCap="ARROW_LINES"></connector>\n  <connector id="1:34" x="880" y="-100" connectorStart="1:6" connectorStartCap="NONE" connectorEnd="1:9" connectorEn
```

**Assistant:**

The existing file already contains several earlier checkout diagrams. I’ll add two new sequences based on this brief: the authorised path and the declined-card path. Hold, confirm and release appear as Booking API self-messages because the brief names no separate room service; the webhook and `payment_pending` steps are left out.

**Tool call:** `figma.generate_diagram` `{"fileKey": "<test-file-key>", "sessionId": "fa258de3-960c-42a3-be88-f9dff2f34bc0", "name": "Roamstay checkout payment — authorised card", "userIntent": "Show the authorised checkout payment sequence from the payments brief.", "mermaidSyntax": "sequenceDiagram\n    title Roamstay checkout payment, authorised card\n    participant GuestApp\n    participant BookingApi\n    participant PaymentProvider\n    participant PartnerHub\n\n    GuestApp->>BookingApi: POST booking\n    BookingApi->>BookingApi: Hold room\n    BookingApi->>PaymentProvider: Authorise card\n    PaymentProvider-->>Bookin`

**Tool result:** `figma.generate_diagram`

```text
{'content': [{'type': 'text', 'text': 'We have displayed the interactive diagram widget to the user. The diagram has been added to the existing file.'}], '_meta': {'name': 'Roamstay checkout payment — authorised card', 'claimFileUrl': '<figma-url> 'imageUrl': 'https://s3-alpha.figma.com/thumbnails/328ccf6f-e15d-48f2-ba69-99ca649bbd73?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQ4GOSFWCTQAAMWLW%2F20261026%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261026T085814Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=504f5a6dc554b856bc812db8a031efb28572c97c9625ad4e944b2fd6b6de0c9c', 'expiresAt': '2026-11-02T08:58:14.407Z', 'mcpRequestId': 'f7773e3e-0823-4347-9f25-9485749d3adb', 'io.modelcontextprotocol/serverInfo': {'name': 'Figma MCP Server', 'version': '1.0.0', 'icons': [{'src': 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIAAAACgCAYAAADEkmT9AAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAhGVYSWZNTQAqAAAACAAFARIAAwAAAAEAAQAAARoABQAAAAEAAABKARsABQAAAAEAAABSASgAAwAAAAEAAgAAh2kABAAAAAEAAABaAAAAAAAAAEgAAAABAAAASAAAAAEAA6ABAAMAAAABAAEAAKACAAQAAAABAAAAgKADAAQAAAABAAAAoAAAAAB6dUZwAAAACXBIWXMAAAsTAAALEwEAmpwYAAABWWlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iWE1QIENvcmUgNi4wLjAiPgogICA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPgogICAgICA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIgogICAgICAgICAgICB4bWx
```

**Tool call:** `figma.generate_diagram` `{"fileKey": "<test-file-key>", "sessionId": "fa258de3-960c-42a3-be88-f9dff2f34bc0", "name": "Roamstay checkout payment — declined card", "userIntent": "Show the declined-card checkout sequence from the payments brief.", "mermaidSyntax": "sequenceDiagram\n    title Roamstay checkout payment, declined card\n    participant GuestApp\n    participant BookingApi\n    participant PaymentProvider\n\n    GuestApp->>BookingApi: POST booking\n    BookingApi->>BookingApi: Hold room\n    BookingApi->>PaymentProvider: Authorise card\n    PaymentProvider-->>BookingApi: Card declined\n    BookingApi->`

**Tool result:** `figma.generate_diagram`

```text
{'content': [{'type': 'text', 'text': 'We have displayed the interactive diagram widget to the user. The diagram has been added to the existing file.'}], '_meta': {'name': 'Roamstay checkout payment — declined card', 'claimFileUrl': '<figma-url> 'imageUrl': 'https://s3-alpha.figma.com/thumbnails/199edf04-9852-4898-8390-b46c937a5b30?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQ4GOSFWCTQAAMWLW%2F20261026%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261026T085822Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=fdee2379987296af32de2df8bdbc4a508329fe1a1b03c71fd405b557865e688c', 'expiresAt': '2026-11-02T08:58:22.743Z', 'mcpRequestId': '6316a215-c778-41b4-9104-424b3e718cff', 'io.modelcontextprotocol/serverInfo': {'name': 'Figma MCP Server', 'version': '1.0.0', 'icons': [{'src': 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIAAAACgCAYAAADEkmT9AAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAhGVYSWZNTQAqAAAACAAFARIAAwAAAAEAAQAAARoABQAAAAEAAABKARsABQAAAAEAAABSASgAAwAAAAEAAgAAh2kABAAAAAEAAABaAAAAAAAAAEgAAAABAAAASAAAAAEAA6ABAAMAAAABAAEAAKACAAQAAAABAAAAgKADAAQAAAABAAAAoAAAAAB6dUZwAAAACXBIWXMAAAsTAAALEwEAmpwYAAABWWlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iWE1QIENvcmUgNi4wLjAiPgogICA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPgogICAgICA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIgogICAgICAgICAgICB4bWxuc
```

**Assistant:**

Both diagrams were added to the supplied FigJam file. I’m reading the file back now to confirm the new sections and their message labels are present.

**Tool call:** `figma.get_figjam` `{"fileKey": "<test-file-key>", "nodeId": "0:1", "sessionId": "fa258de3-960c-42a3-be88-f9dff2f34bc0"}`

**Tool result:** `figma.get_figjam`

```text
{'content': [{'type': 'text', 'text': '<canvas id="0:1" name="Page 1" x="0" y="0" width="0" height="0">\n  <shape-with-text id="1:3" x="768" y="-492" width="224" height="128" name="ROUNDED_RECTANGLE">Order list</shape-with-text>\n  <shape-with-text id="1:6" x="768" y="-236" width="224" height="128" name="SQUARE">Order detail</shape-with-text>\n  <shape-with-text id="1:9" x="780" y="20" width="200" height="200" name="DIAMOND">Within 30 days?</shape-with-text>\n  <shape-with-text id="1:12" x="608" y="476" width="224" height="128" name="ROUNDED_RECTANGLE">Contact support</shape-with-text>\n  <shape-with-text id="1:15" x="928" y="476" width="224" height="128" name="SQUARE">Pick a reason</shape-with-text>\n  <shape-with-text id="1:18" x="940" y="732" width="200" height="200" name="DIAMOND">Drop-off or pickup?</shape-with-text>\n  <shape-with-text id="1:21" x="768" y="1188" width="224" height="128" name="SQUARE">Choose a drop-off point</shape-with-text>\n  <shape-with-text id="1:24" x="1088" y="1188" width="224" height="128" name="SQUARE">Book a courier pickup</shape-with-text>\n  <shape-with-text id="1:27" x="928" y="1444" width="224" height="128" name="ROUNDED_RECTANGLE">Return confirmed with QR code</shape-with-text>\n  <connector id="1:30" x="880" y="-356" connectorStart="1:3" connectorStartCap="NONE" connectorEnd="1:6" connectorEndCap="ARROW_LINES"></connector>\n  <connector id="1:34" x="880" y="-100" connectorStart="1:6" connectorStartCap="NONE" connectorEnd="1:9" connectorEn
```

**Tool call:** `figma.get_figjam` `{"fileKey": "<test-file-key>", "nodeId": "0:1", "sessionId": "fa258de3-960c-42a3-be88-f9dff2f34bc0"}`

**Tool result:** `figma.get_figjam`

```text
{'content': [{'type': 'text', 'text': '<canvas id="0:1" name="Page 1" x="0" y="0" width="0" height="0">\n  <shape-with-text id="1:3" x="768" y="-492" width="224" height="128" name="ROUNDED_RECTANGLE">Order list</shape-with-text>\n  <shape-with-text id="1:6" x="768" y="-236" width="224" height="128" name="SQUARE">Order detail</shape-with-text>\n  <shape-with-text id="1:9" x="780" y="20" width="200" height="200" name="DIAMOND">Within 30 days?</shape-with-text>\n  <shape-with-text id="1:12" x="608" y="476" width="224" height="128" name="ROUNDED_RECTANGLE">Contact support</shape-with-text>\n  <shape-with-text id="1:15" x="928" y="476" width="224" height="128" name="SQUARE">Pick a reason</shape-with-text>\n  <shape-with-text id="1:18" x="940" y="732" width="200" height="200" name="DIAMOND">Drop-off or pickup?</shape-with-text>\n  <shape-with-text id="1:21" x="768" y="1188" width="224" height="128" name="SQUARE">Choose a drop-off point</shape-with-text>\n  <shape-with-text id="1:24" x="1088" y="1188" width="224" height="128" name="SQUARE">Book a courier pickup</shape-with-text>\n  <shape-with-text id="1:27" x="928" y="1444" width="224" height="128" name="ROUNDED_RECTANGLE">Return confirmed with QR code</shape-with-text>\n  <connector id="1:30" x="880" y="-356" connectorStart="1:3" connectorStartCap="NONE" connectorEnd="1:6" connectorEndCap="ARROW_LINES"></connector>\n  <connector id="1:34" x="880" y="-100" connectorStart="1:6" connectorStartCap="NONE" connectorEnd="1:9" connectorEn
```

**Assistant:**

The read-back exposed a renderer gap: it dropped the Booking API’s hold, confirm and release self-messages. I’m adding those three brief-backed actions as FigJam annotations so the board preserves them without inventing a separate room service.

**Tool call:** `read_mcp_resource` `{"server": "codex_apps", "uri": "skill://plugin_connector_68df038e0ba48191908c8434991bbac2/figma-use"}`

**Tool result:** `read_mcp_resource`

```text
{'content': [{'type': 'text', 'text': '{"server":"codex_apps","uri":"skill://plugin_connector_68df038e0ba48191908c8434991bbac2/figma-use","contents":[{"uri":"skill://plugin_connector_68df038e0ba48191908c8434991bbac2/figma-use/SKILL.md","mimeType":"text/markdown","text":"---\\nname: figma-use\\ndescription: \\"**MANDATORY prerequisite** — you MUST invoke this skill BEFORE every `use_figma` tool call. NEVER call `use_figma` directly without loading this skill first. Skipping it causes common, hard-to-debug failures. Trigger whenever the user wants to perform a write action or a unique read action that requires JavaScript execution in the Figma file context — e.g. create/edit/delete nodes, set up variables or tokens, build components and variants, modify auto-layout or fills, bind variables to properties, or inspect file structure programmatically.\\"\\ndisable-model-invocation: false\\n---\\n\\n# use_figma — Figma Plugin API Skill\\n\\nUse the `use_figma` tool to execute JavaScript in Figma files via the Plugin API. All detailed reference docs live in `references/`.\\n\\n**Always include `figma-use` in the comma-separated `skillNames` parameter when calling `use_figma`. If this skill was loaded via an MCP resource, you MUST prefix the name with `resource:` (e.g. `resource:figma-use`).** This is a logging parameter used to track skill usage — it does not affect execution.\\n\\n**If Figma MCP tools appear as deferred tools, batch-load all their schemas in a single `ToolSearch` ca
```

**Tool call:** `read_mcp_resource` `{"server": "codex_apps", "uri": "skill://plugin_connector_68df038e0ba48191908c8434991bbac2/figma-generate-diagram/references/workflow.md"}`

**Tool result:** `read_mcp_resource`

```text
{'content': [{'type': 'text', 'text': '{"server":"codex_apps","uri":"skill://plugin_connector_68df038e0ba48191908c8434991bbac2/figma-generate-diagram/references/workflow.md","contents":[{"uri":"skill://plugin_connector_68df038e0ba48191908c8434991bbac2/figma-generate-diagram/references/workflow.md","mimeType":"text/markdown","text":"# Hybrid Diagram Workflow\\n\\nMermaid\'s syntax can\'t express everything a good diagram needs — annotations tied to specific data, domain color-coding, callouts that live _next_ to the diagram rather than inside it. This reference covers the **hybrid workflow**: use `generate_diagram` to scaffold the structural diagram, then use `use_figma` (via the [figma-use-figjam](../../figma-use-figjam/SKILL.md) skill) to layer on what Mermaid can\'t do.\\n\\n**This is a judgment tool, not a procedure.** The hybrid workflow costs extra tokens and latency. Deploy it when the user\'s ask genuinely benefits — not on every diagram. When in doubt, ship the base diagram first; the user can tell you what\'s missing.\\n\\n## 1. When to reach for the hybrid workflow\\n\\nSignals that say **yes, go hybrid**:\\n\\n- User explicitly asks for something Mermaid can\'t do — _\\"add notes explaining the branches\\"_, _\\"color-code by team\\"_, _\\"callout the drop-offs with conversion numbers\\"_, _\\"annotate the critical path with the SLA\\"_.\\n- User shared attachable data (quotes, metrics, research notes, ticket links) that clearly maps to specific nodes.\\n- The diag
```

**Tool call:** `read_mcp_resource` `{"server": "codex_apps", "uri": "skill://plugin_connector_68df038e0ba48191908c8434991bbac2/figma-use-figjam"}`

**Tool result:** `read_mcp_resource`

```text
{'content': [{'type': 'text', 'text': '{"server":"codex_apps","uri":"skill://plugin_connector_68df038e0ba48191908c8434991bbac2/figma-use-figjam","contents":[{"uri":"skill://plugin_connector_68df038e0ba48191908c8434991bbac2/figma-use-figjam/SKILL.md","mimeType":"text/markdown","text":"---\\nname: figma-use-figjam\\ndescription: \\"This skill helps agents use Figma\'s use_figma MCP tool in the FigJam context. Can be used alongside figma-use which has foundational context for using the use_figma tool.\\"\\ndisable-model-invocation: false\\n---\\n\\n# use_figma — Figma Plugin API Skill for FigJam\\n\\nThis skill contains FigJam-specific context for the `use_figma` MCP tool. The [figma-use](../figma-use/SKILL.md) skill provides foundational context for plugin API execution via MCP as well as the full Figma plugin API for more advanced use-cases that are not described here.\\n\\n**Always include `figma-use-figjam` in the comma-separated `skillNames` parameter when calling `use_figma` for FigJam operations. If this skill was loaded via an MCP resource, you MUST prefix the name with `resource:` (e.g. `resource:figma-use-figjam`).** This is a logging parameter used to track skill usage — it does not affect execution.\\n\\n> **FigJam URL is `figma.com/board/...`.** Do NOT call `figma.createPage()` in FigJam — it throws `TypeError: figma.createPage no such property \'createPage\' on the figma global object`. `createPage()` is a Design-file API only (`figma.com/design/...`). FigJam files
```

**Tool call:** `read_mcp_resource` `{"server": "codex_apps", "uri": "skill://plugin_connector_68df038e0ba48191908c8434991bbac2/figma-use-figjam/references/create-text.md"}`

**Tool result:** `read_mcp_resource`

```text
{'content': [{'type': 'text', 'text': '{"server":"codex_apps","uri":"skill://plugin_connector_68df038e0ba48191908c8434991bbac2/figma-use-figjam/references/create-text.md","contents":[{"uri":"skill://plugin_connector_68df038e0ba48191908c8434991bbac2/figma-use-figjam/references/create-text.md","mimeType":"text/markdown","text":"# Create Text Nodes\\n\\n> Part of the [figma-use-figjam skill](../SKILL.md). Creating and styling standalone text nodes and mind map operations.\\n\\nUse this skill when creating, modifying, or styling standalone text in FigJam (text created with the **Text** tool, not text inside stickies, shapes, or connectors). Also use this skill for mind map operations — adding, inserting, or extending connected text nodes.\\n\\n**Scope:** Text nodes are created with `figma.createText()` and have type `\'TEXT\'`. For editing existing text content or mixed styles, see [edit-text](edit-text.md).\\n\\n## When to use a Text Node\\n\\nUse text nodes for titles, headers, labels, prompts, instructions, and any content that provides structure or context. They can also be used for longer descriptions or explanations.\\n\\n## Creating a Text Node\\n\\n```javascript\\nconst text = figma.createText()\\n\\n// Load the font before setting content (required for characters, fontSize, etc.)\\nawait figma.loadFontAsync(text.fontName)\\ntext.characters = \'Brainstorming instructions\'\\n\\nconsole.log(\'Created text:\', text.id, text.characters)\\nfigma.closePlugin()\\n```\\n\\n## Te
```

**Tool call:** `read_mcp_resource` `{"server": "codex_apps", "uri": "skill://plugin_connector_68df038e0ba48191908c8434991bbac2/figma-use-figjam/references/create-text.md"}`

**Tool result:** `read_mcp_resource`

```text
{'content': [{'type': 'text', 'text': '{"server":"codex_apps","uri":"skill://plugin_connector_68df038e0ba48191908c8434991bbac2/figma-use-figjam/references/create-text.md","contents":[{"uri":"skill://plugin_connector_68df038e0ba48191908c8434991bbac2/figma-use-figjam/references/create-text.md","mimeType":"text/markdown","text":"# Create Text Nodes\\n\\n> Part of the [figma-use-figjam skill](../SKILL.md). Creating and styling standalone text nodes and mind map operations.\\n\\nUse this skill when creating, modifying, or styling standalone text in FigJam (text created with the **Text** tool, not text inside stickies, shapes, or connectors). Also use this skill for mind map operations — adding, inserting, or extending connected text nodes.\\n\\n**Scope:** Text nodes are created with `figma.createText()` and have type `\'TEXT\'`. For editing existing text content or mixed styles, see [edit-text](edit-text.md).\\n\\n## When to use a Text Node\\n\\nUse text nodes for titles, headers, labels, prompts, instructions, and any content that provides structure or context. They can also be used for longer descriptions or explanations.\\n\\n## Creating a Text Node\\n\\n```javascript\\nconst text = figma.createText()\\n\\n// Load the font before setting content (required for characters, fontSize, etc.)\\nawait figma.loadFontAsync(text.fontName)\\ntext.characters = \'Brainstorming instructions\'\\n\\nconsole.log(\'Created text:\', text.id, text.characters)\\nfigma.closePlugin()\\n```\\n\\n## Te
```

**Tool call:** `read_mcp_resource` `{"server": "codex_apps", "uri": "skill://plugin_connector_68df038e0ba48191908c8434991bbac2/figma-use"}`

**Tool result:** `read_mcp_resource`

```text
{'content': [{'type': 'text', 'text': '{"server":"codex_apps","uri":"skill://plugin_connector_68df038e0ba48191908c8434991bbac2/figma-use","contents":[{"uri":"skill://plugin_connector_68df038e0ba48191908c8434991bbac2/figma-use/SKILL.md","mimeType":"text/markdown","text":"---\\nname: figma-use\\ndescription: \\"**MANDATORY prerequisite** — you MUST invoke this skill BEFORE every `use_figma` tool call. NEVER call `use_figma` directly without loading this skill first. Skipping it causes common, hard-to-debug failures. Trigger whenever the user wants to perform a write action or a unique read action that requires JavaScript execution in the Figma file context — e.g. create/edit/delete nodes, set up variables or tokens, build components and variants, modify auto-layout or fills, bind variables to properties, or inspect file structure programmatically.\\"\\ndisable-model-invocation: false\\n---\\n\\n# use_figma — Figma Plugin API Skill\\n\\nUse the `use_figma` tool to execute JavaScript in Figma files via the Plugin API. All detailed reference docs live in `references/`.\\n\\n**Always include `figma-use` in the comma-separated `skillNames` parameter when calling `use_figma`. If this skill was loaded via an MCP resource, you MUST prefix the name with `resource:` (e.g. `resource:figma-use`).** This is a logging parameter used to track skill usage — it does not affect execution.\\n\\n**If Figma MCP tools appear as deferred tools, batch-load all their schemas in a single `ToolSearch` ca
```

**Tool call:** `read_mcp_resource` `{"server": "codex_apps", "uri": "skill://plugin_connector_68df038e0ba48191908c8434991bbac2/figma-use-figjam"}`

**Tool result:** `read_mcp_resource`

```text
{'content': [{'type': 'text', 'text': '{"server":"codex_apps","uri":"skill://plugin_connector_68df038e0ba48191908c8434991bbac2/figma-use-figjam","contents":[{"uri":"skill://plugin_connector_68df038e0ba48191908c8434991bbac2/figma-use-figjam/SKILL.md","mimeType":"text/markdown","text":"---\\nname: figma-use-figjam\\ndescription: \\"This skill helps agents use Figma\'s use_figma MCP tool in the FigJam context. Can be used alongside figma-use which has foundational context for using the use_figma tool.\\"\\ndisable-model-invocation: false\\n---\\n\\n# use_figma — Figma Plugin API Skill for FigJam\\n\\nThis skill contains FigJam-specific context for the `use_figma` MCP tool. The [figma-use](../figma-use/SKILL.md) skill provides foundational context for plugin API execution via MCP as well as the full Figma plugin API for more advanced use-cases that are not described here.\\n\\n**Always include `figma-use-figjam` in the comma-separated `skillNames` parameter when calling `use_figma` for FigJam operations. If this skill was loaded via an MCP resource, you MUST prefix the name with `resource:` (e.g. `resource:figma-use-figjam`).** This is a logging parameter used to track skill usage — it does not affect execution.\\n\\n> **FigJam URL is `figma.com/board/...`.** Do NOT call `figma.createPage()` in FigJam — it throws `TypeError: figma.createPage no such property \'createPage\' on the figma global object`. `createPage()` is a Design-file API only (`figma.com/design/...`). FigJam files
```

**Tool call:** `read_mcp_resource` `{"server": "codex_apps", "uri": "skill://plugin_connector_68df038e0ba48191908c8434991bbac2/figma-use-figjam/references/create-text.md"}`

**Tool result:** `read_mcp_resource`

```text
{'content': [{'type': 'text', 'text': '{"server":"codex_apps","uri":"skill://plugin_connector_68df038e0ba48191908c8434991bbac2/figma-use-figjam/references/create-text.md","contents":[{"uri":"skill://plugin_connector_68df038e0ba48191908c8434991bbac2/figma-use-figjam/references/create-text.md","mimeType":"text/markdown","text":"# Create Text Nodes\\n\\n> Part of the [figma-use-figjam skill](../SKILL.md). Creating and styling standalone text nodes and mind map operations.\\n\\nUse this skill when creating, modifying, or styling standalone text in FigJam (text created with the **Text** tool, not text inside stickies, shapes, or connectors). Also use this skill for mind map operations — adding, inserting, or extending connected text nodes.\\n\\n**Scope:** Text nodes are created with `figma.createText()` and have type `\'TEXT\'`. For editing existing text content or mixed styles, see [edit-text](edit-text.md).\\n\\n## When to use a Text Node\\n\\nUse text nodes for titles, headers, labels, prompts, instructions, and any content that provides structure or context. They can also be used for longer descriptions or explanations.\\n\\n## Creating a Text Node\\n\\n```javascript\\nconst text = figma.createText()\\n\\n// Load the font before setting content (required for characters, fontSize, etc.)\\nawait figma.loadFontAsync(text.fontName)\\ntext.characters = \'Brainstorming instructions\'\\n\\nconsole.log(\'Created text:\', text.id, text.characters)\\nfigma.closePlugin()\\n```\\n\\n## Te
```

**Tool call:** `read_mcp_resource` `{"server": "codex_apps", "uri": "skill://plugin_connector_68df038e0ba48191908c8434991bbac2/figma-use-figjam/references/position-figjam-nodes.md"}`

**Tool result:** `read_mcp_resource`

```text
{'content': [{'type': 'text', 'text': '{"server":"codex_apps","uri":"skill://plugin_connector_68df038e0ba48191908c8434991bbac2/figma-use-figjam/references/position-figjam-nodes.md","contents":[{"uri":"skill://plugin_connector_68df038e0ba48191908c8434991bbac2/figma-use-figjam/references/position-figjam-nodes.md","mimeType":"text/markdown","text":"# FigJam Node Positioning Tutorial\\n\\n> Part of the [figma-use-figjam skill](../SKILL.md). Positioning, sizing, and reparenting nodes on the canvas.\\n\\nUse this skill when working with positioning, sizing, and reparenting nodes.\\n\\n## Basics of how nodes are positioned\\n\\nNodes may be positioned by setting their `x` and `y` properties. Nodes are positioned with respect to their parent.\\n\\n```javascript\\n// Position (relative to parent)\\nnode.x = 100\\nnode.y = 200\\n```\\n\\n## Positioning Nodes Relative to Existing Nodes\\n\\nIt\'s important to remember that `node.x` and `node.y` are relative to the node\'s parent, not the page. For example: a node inside a section has coordinates relative to that section\'s origin.\\n\\nWhen creating or placing a node relative to an existing node:\\n\\n1. **Find the parent**: Locate the parent of the existing node.\\n2. **Add new node to parent**: Call `parent.appendChild()` to add the new node to the parent.\\n3. **Position within parent**: Position the new node within the parent. The x / y coordinates of the new node will be with respect to the top-left corner of the parent.\\n4. **Ens
```

**Tool call:** `read_mcp_resource` `{"server": "codex_apps", "uri": "skill://plugin_connector_68df038e0ba48191908c8434991bbac2/figma-use-figjam/references/plan-board-content.md"}`

**Tool result:** `read_mcp_resource`

```text
{'content': [{'type': 'text', 'text': '{"server":"codex_apps","uri":"skill://plugin_connector_68df038e0ba48191908c8434991bbac2/figma-use-figjam/references/plan-board-content.md","contents":[{"uri":"skill://plugin_connector_68df038e0ba48191908c8434991bbac2/figma-use-figjam/references/plan-board-content.md","mimeType":"text/markdown","text":"# Plan Content for FigJam Boards\\n\\n**When NOT to use this skill:** Do NOT read this skill for analysis, summarization, or investigation of existing board content (e.g. \\"summarize this board\\", \\"what themes are here?\\", \\"analyze the feedback\\"). This skill is exclusively for planning NEW content to be created on the board.\\n\\nDo NOT use this skill for flowcharts, architecture diagrams, sequence diagrams, state diagrams, or entity relationship diagrams (ERDs). For those, use the `figma-plugin:figma-generate-diagram` skill and the `generate_diagram` tool.\\n\\nUse this skill when determining **what content to include** for generated FigJam board content. Given a user\'s request (e.g. \\"make a brainstorm template\\", \\"retro board\\", \\"ice breaker\\", \\"scaffold\\"), produce a **sequential outline** that downstream skills can use to create sections, text, stickies, and layout.\\n\\n**Must be loaded alongside the `figma-use-figjam` skill**, which provides the FigJam Plugin API references (create-section, create-sticky, create-text, position-figjam-nodes) needed to render the planned content.\\n\\n## Part 1: Design Principles\\
```

**Tool call:** `read_mcp_resource` `{"server": "codex_apps", "uri": "skill://plugin_connector_68df038e0ba48191908c8434991bbac2/figma-use/references/plugin-api-standalone.index.md"}`

**Tool result:** `read_mcp_resource`

```text
{'content': [{'type': 'text', 'text': '{"server":"codex_apps","uri":"skill://plugin_connector_68df038e0ba48191908c8434991bbac2/figma-use/references/plugin-api-standalone.index.md","contents":[{"uri":"skill://plugin_connector_68df038e0ba48191908c8434991bbac2/figma-use/references/plugin-api-standalone.index.md","mimeType":"text/markdown","text":"# Plugin API Index\\n\\n> Full typings: `plugin-api-standalone.d.ts` (10,191 lines)\\n> Grep by symbol name to jump to definition. All `L#` line numbers refer to that file.\\n> This index describes the APIs available through `use_figma`. See the `.d.ts` for full type declarations.\\n\\n---\\n\\n## figma.\\\\* — PluginAPI (L4)\\n\\n### Identity & State\\n\\n| Member                          | Type                                                                                                                                             |\\n| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |\\n| `apiVersion`                    | `\'1.0.0\'`                                                                                                                                        |\\n| `editorType`                    | `\'figma\' \\\\| \'figjam\' \\\\| \'dev\' \\\\| \'slides\' \\\\| \'buzz\'`                                                                                             |\\n| `fileKey`                    
```

**Tool call:** `figma.get_figjam` `{"fileKey": "<test-file-key>", "nodeId": "0:1", "sessionId": "fa258de3-960c-42a3-be88-f9dff2f34bc0"}`

**Tool result:** `figma.get_figjam`

```text
{'content': [{'type': 'text', 'text': '<canvas id="0:1" name="Page 1" x="0" y="0" width="0" height="0">\n  <shape-with-text id="1:3" x="768" y="-492" width="224" height="128" name="ROUNDED_RECTANGLE">Order list</shape-with-text>\n  <shape-with-text id="1:6" x="768" y="-236" width="224" height="128" name="SQUARE">Order detail</shape-with-text>\n  <shape-with-text id="1:9" x="780" y="20" width="200" height="200" name="DIAMOND">Within 30 days?</shape-with-text>\n  <shape-with-text id="1:12" x="608" y="476" width="224" height="128" name="ROUNDED_RECTANGLE">Contact support</shape-with-text>\n  <shape-with-text id="1:15" x="928" y="476" width="224" height="128" name="SQUARE">Pick a reason</shape-with-text>\n  <shape-with-text id="1:18" x="940" y="732" width="200" height="200" name="DIAMOND">Drop-off or pickup?</shape-with-text>\n  <shape-with-text id="1:21" x="768" y="1188" width="224" height="128" name="SQUARE">Choose a drop-off point</shape-with-text>\n  <shape-with-text id="1:24" x="1088" y="1188" width="224" height="128" name="SQUARE">Book a courier pickup</shape-with-text>\n  <shape-with-text id="1:27" x="928" y="1444" width="224" height="128" name="ROUNDED_RECTANGLE">Return confirmed with QR code</shape-with-text>\n  <connector id="1:30" x="880" y="-356" connectorStart="1:3" connectorStartCap="NONE" connectorEnd="1:6" connectorEndCap="ARROW_LINES"></connector>\n  <connector id="1:34" x="880" y="-100" connectorStart="1:6" connectorStartCap="NONE" connectorEnd="1:9" connectorEn
```

**Tool call:** `figma.use_figma` `{"fileKey": "<test-file-key>", "sessionId": "fa258de3-960c-42a3-be88-f9dff2f34bc0", "skillNames": "resource:figma-use,resource:figma-use-figjam", "description": "Add the brief-backed Booking API internal actions omitted by the sequence renderer", "code": "const specs = [\n  { sectionId: \"161:5870\", label: \"Booking API: Hold room\", y: 288 },\n  { sectionId: \"161:5870\", label: \"Booking API: Confirm hold\", y: 528 },\n  { sectionId: \"162:5919\", label: \"Booking API: Hold room\", y: 288 },\n  { sectionId: \"162:5919\", label: \"Booking API: Release hold\", y: 528 }\n];\n\nconst nod`

**Tool result:** `figma.use_figma`

```text
{'content': [{'type': 'text', 'text': '{"createdNodeIds":["163:5958","163:5959","163:5960","163:5961"],"labels":[{"id":"163:5958","name":"Booking API: Hold room","sectionId":"161:5870","x":238,"y":288},{"id":"163:5959","name":"Booking API: Confirm hold","sectionId":"161:5870","x":218,"y":528},{"id":"163:5960","name":"Booking API: Hold room","sectionId":"162:5919","x":238,"y":288},{"id":"163:5961","name":"Booking API: Release hold","sectionId":"162:5919","x":219,"y":528}]}'}], '_meta': {'mcpRequestId': 'e56d30ba-e76a-486b-bdee-4a5399f2e0dc', 'io.modelcontextprotocol/serverInfo': {'name': 'Figma MCP Server', 'version': '1.0.0', 'icons': [{'src': 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIAAAACgCAYAAADEkmT9AAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAhGVYSWZNTQAqAAAACAAFARIAAwAAAAEAAQAAARoABQAAAAEAAABKARsABQAAAAEAAABSASgAAwAAAAEAAgAAh2kABAAAAAEAAABaAAAAAAAAAEgAAAABAAAASAAAAAEAA6ABAAMAAAABAAEAAKACAAQAAAABAAAAgKADAAQAAAABAAAAoAAAAAB6dUZwAAAACXBIWXMAAAsTAAALEwEAmpwYAAABWWlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iWE1QIENvcmUgNi4wLjAiPgogICA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPgogICAgICA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIgogICAgICAgICAgICB4bWxuczp0aWZmPSJodHRwOi8vbnMuYWRvYmUuY29tL3RpZmYvMS4wLyI+CiAgICAgICAgIDx0aWZmOk9yaWVudGF0aW9uPjE8L3RpZmY6T3JpZW50YXRpb24+CiAgICAgIDwvcmRmOkRlc2NyaXB0aW9uPgogICA8L3JkZjpSREY+CjwveDp4bXBtZXRhPgoZXuEHAAARf
```

**Tool call:** `figma.get_screenshot` `{"fileKey": "<test-file-key>", "nodeId": "161:5870", "sessionId": "fa258de3-960c-42a3-be88-f9dff2f34bc0", "maxDimension": 1800, "enableBase64Response": true}`

**Tool result:** `figma.get_screenshot`

```text
{'content': [{'type': 'text', 'text': '{"image_url":"<figma-url> {'type': 'image', 'data': 'iVBORw0KGgoAAAANSUhEUgAABMQAAAP8CAYAAACpvmK0AAAACXBIWXMAAAPoAAAD6AG1e1JrAAAgAElEQVR4Xuzdf6ylVWE3+mfoqDMtI2Di286AMYUIV/C+twVaJAzqmzAQjfCPCqM216gd9CY3uSAjbd60AvpGWxxE/yqCaJpblF/9AzA2gok/CkFfGW5u60DAH0mrMwMxcUYGymjVufnu3jV9zp69z7P3OXufc/Zen0+yc87ZZ+3n19577Wd991rrWbd3794jzRjWrVvX+7l58+auogAAAACw5hzXVQAAAAAA5olADAAAAICqCMQAAAAAqIpADAAAAICqCMQAAAAAqIpADAAAAICqCMQAAAAAqIpADAAAAICqCMQAAAAAqIpADAAAAICqCMQAAAAAqIpADAAAAICqCMQAAAAAqIpADAAAAICqCMQAAAAAqIpADAAAAICqCMQAAAAAqMr6rgKsXT/5yU+Oue+UU04ZWBYAAACA/yAQmxHf/va3e7cnnniid/vxj388tOxZZ53VC8Ze//rXNxdffLGQDFi1OqvL+973vublL395M2sefPDBXl3c5aqrruoqAgAArIJ1e/fuPdKMYd26db2fmzdv7irKMj333HPN5z//+d7t5z//ebNUCcjS6Hz729/eVRRgIj796U83N998c1ex5pFHHpnJ0H7nzp3NPffc01Ws+Zd/+ZeuIgAAwCowh9gabkxu3bq116BcThgWe/bsaa655pre8u69996u4gAAAABzzZDJNTgv2JVXXtkLsSYtwywTjGWYz0c+8pFmKfLYQ4cOLVpm06ZNzZlnnrloGQAAAIDVIhBbQxI2bd++fdk9wrrcfvvtzaOPPtrcddddY8/dk7BusfnLInOXZdkAAAAAa5Ehk2uoZ9hKhGHt8G3Hjh1dxQAAAADmjkCswjCsyBXgMmE/AAAAQE0EYmvAZz7zmc5hiNOSSfsTyAEAAADUwhxiqyxh1N13392M6oQTTmjOO++85uKLL27OP//83hxguWU5uWUy/gcffLDX+2sUzz33XK+X2FIn2QcAAACYNQKxVTbOkMVMVn/TTTc1p5xyyjH/y325pcz73//+5qtf/WrzsY99bKSeZ/fcc09z1VVXjT3BPgAAAMAsMmRylY3ak+uss87qXblxUBg2yCWXXNLceeedvR5lo/QSyyT7AAAAADXQQ2wVJYjKEMdRfPKTn2zGlfAsQyGvueaarqLNo48+2utdNivHLcND9+7d
```

**Tool call:** `figma.get_screenshot` `{"fileKey": "<test-file-key>", "nodeId": "162:5919", "sessionId": "fa258de3-960c-42a3-be88-f9dff2f34bc0", "maxDimension": 1800, "enableBase64Response": true}`

**Tool result:** `figma.get_screenshot`

```text
{'content': [{'type': 'text', 'text': '{"image_url":"<figma-url> {'type': 'image', 'data': 'iVBORw0KGgoAAAANSUhEUgAAA6wAAAOsCAYAAABOOztEAAAACXBIWXMAAAPoAAAD6AG1e1JrAAAgAElEQVR4XuzdW4xlZZ0//NVO+x+YoQVM5s006IUQIIKZGMCooRmYhMZogBsVGrwwHgDvhnMmJkqjiSbIQe84eMhcCAjOBQc1ookwYsQIXMwIBlAno9Jt3gtB6Qw9x37z3f/3V7Nq9d61d52fqvp8kp2q2rVOe+29nv181/OsZ207dOjQoQ4AAAAa87ppEwAAAMB6EFgBAABoksAKAABAkwRWAAAAmiSwAgAA0CSBFQAAgCYJrAAAADRJYAUAAKBJAisAAABNElgBAABoksAKAABAkwRWAAAAmiSwAgAA0CSBFQAAgCYJrAAAADRJYAUAAKBJAisAAABNElgBAABo0vZpE7B5Pfnkk6PHNB/96Ee7N7zhDd1G8+ijj3bPPffctMm6q666atokAADAOhBYt7CE1dtvv33aZN0HPvCBDRtYH3jggWmTCawAANAoXYIBAABoksAKAABAkwRWAAAAmiSwAgAA0CSBFQAAgCYJrAAAADRJYAUAAKBJAisAAABNElgBAABo0vZuFf3xj3/sfv7zn3e//e1vR3+/6U1v6nbs2NGdeuqp3VKXl2VlmfGGN7xh9HjrW986+rlWsg312sp6bcukfZ1tOP7445e8r1dTtvGll16a29aV+GwAAABbKLA++eST3XXXXddN88QTTxz23Fe/+tXu0Ucf7X784x+PnefNb35z9653vau76qqrRkFlWhD75je/ueDy4t3vfnf3gQ98YPRYadmG7I9sQx5/+MMfFpy+Xt973vOebvfu3d1qyXZlX2f//OY3vxk7zdFHH92df/75M+3r1dJ/D5977rmp+6/ey+zD9dpmAABg/W07dOjQoXH/SEC75JJLumn+9V//de73hJErrrhiYngaSivg1Vdf3X30ox9dMDTPurwKi/fdd9+KBJ0KhHlMC1kLbU/C4koG6aVu18c+9rHu05/+9NzfX/ziF7vbb7+9m+ZHP/rRkvbnUrez74Mf/OCSw3Y+Ow888MCiPsMAAMAmvIY1YXXPnj2LCpcJNDfddNMoOA3luQTmxSwvMv173/ve0fYsR8Ly+973vlGgW2rYqu259tpru127ds3rArtUWcZSt+srX/nKaN9kv6+2tKbmNS9lO/sSOM8666yxnxEAAGBzW5HAmhCVsLrUYJJQk1a4xbb8TZJAlrC71IC41LC8kCw
```

**Tool call:** `figma.get_figjam` `{"fileKey": "<test-file-key>", "nodeId": "0:1", "sessionId": "fa258de3-960c-42a3-be88-f9dff2f34bc0"}`

**Tool result:** `figma.get_figjam`

```text
{'content': [{'type': 'text', 'text': '<canvas id="0:1" name="Page 1" x="0" y="0" width="0" height="0">\n  <shape-with-text id="1:3" x="768" y="-492" width="224" height="128" name="ROUNDED_RECTANGLE">Order list</shape-with-text>\n  <shape-with-text id="1:6" x="768" y="-236" width="224" height="128" name="SQUARE">Order detail</shape-with-text>\n  <shape-with-text id="1:9" x="780" y="20" width="200" height="200" name="DIAMOND">Within 30 days?</shape-with-text>\n  <shape-with-text id="1:12" x="608" y="476" width="224" height="128" name="ROUNDED_RECTANGLE">Contact support</shape-with-text>\n  <shape-with-text id="1:15" x="928" y="476" width="224" height="128" name="SQUARE">Pick a reason</shape-with-text>\n  <shape-with-text id="1:18" x="940" y="732" width="200" height="200" name="DIAMOND">Drop-off or pickup?</shape-with-text>\n  <shape-with-text id="1:21" x="768" y="1188" width="224" height="128" name="SQUARE">Choose a drop-off point</shape-with-text>\n  <shape-with-text id="1:24" x="1088" y="1188" width="224" height="128" name="SQUARE">Book a courier pickup</shape-with-text>\n  <shape-with-text id="1:27" x="928" y="1444" width="224" height="128" name="ROUNDED_RECTANGLE">Return confirmed with QR code</shape-with-text>\n  <connector id="1:30" x="880" y="-356" connectorStart="1:3" connectorStartCap="NONE" connectorEnd="1:6" connectorEndCap="ARROW_LINES"></connector>\n  <connector id="1:34" x="880" y="-100" connectorStart="1:6" connectorStartCap="NONE" connectorEnd="1:9" connectorEn
```

**Tool call:** `figma.get_screenshot` `{"fileKey": "<test-file-key>", "nodeId": "161:5870", "sessionId": "fa258de3-960c-42a3-be88-f9dff2f34bc0", "maxDimension": 1600, "enableBase64Response": true, "contentsOnly": true}`

**Tool result:** `figma.get_screenshot`

```text
{'content': [{'type': 'text', 'text': '{"image_url":"<figma-url> {'type': 'image', 'data': 'iVBORw0KGgoAAAANSUhEUgAABMQAAAP8CAYAAACpvmK0AAAACXBIWXMAAAPoAAAD6AG1e1JrAAAgAElEQVR4Xuzdf6ylZWEv+nfoYGdaRgaTnnYGTU8hwhE853qBVg1DpQmD0Qj/qICaHI/aQW9ykzsITM1pK6An2o6D4F8XwR9pblB+2OQCxkYwEVuIenRobytwwR/3+IMZSBNnlLGMCMzNd/U803evWWu/a+291t57refzSVb23ms/6/211nrW+3zX8zzvumZM+/btO5KfW7Zs6SoKAAAAAGvOcV0FAAAAAGCeCMQAAAAAqIpADAAAAICqCMQAAAAAqIpADAAAAICqCMQAAAAAqIpADAAAAICqCMQAAAAAqIpADAAAAICqCMQAAAAAqIpADAAAAICqCMQAAAAAqIpADAAAAICqCMQAAAAAqIpADAAAAICqCMQAAAAAqIpADAAAAICqrO8qwNr1k5/85Jj7XvrSlw4sCwAAAMC/EojNiG984xu92yOPPNK7/fjHPx5a9swzz+wFY695zWuaCy+8UEgGrFqd1eXd73538+IXv7iZNffee2+vLu6yc+fOriIAAMAqWNeMad++fUfyc8uWLV1FWaaf//znzWc+85ne7Wc/+1mzVAnI0uh8y1ve0lUUYCJuvPHG5oYbbugq1jz44IMzGdpfddVVzZ133tlVrPnhD3/YVQQAAFgF5hBbw43Jbdu29RqUywnD4uGHH26uvPLK3vK+8IUvdBUHAAAAmGuGTK7BecEuv/zyXog1aRlmmWAsw3w++MEPNkuRxz799NOLltm0aVNzxhlnLFoGAAAAYLUIxNaQhE2XXXbZsnuEdfn0pz/dfP3rX29uv/32sefuSVi32PxlkbnLsmwAAACAtciQyTXUM2wlwrB2+LZjx46uYgAAAABzRyBWYRhW5ApwmbAfAAAAoCYCsTXgE5/4ROcwxGnJpP0J5AAAAABqYQ6xVZYw6o477mhGdeKJJzavfvWrmwsvvLB57Wtf25sDLLcsJ7dMxn/vvff2en+N4uc//3mvl9hSJ9kHAAAAmDUCsVU2zpDFTFZ//fXXNy996UuP+V/uyy1l3vOe9zRf/vKXmw9/+MMj9Ty78847m507d449wT4AAADALDJkcpWN2pPrzDPP7F25cVAYNsjrX//65rbbbuv1KBull1gm2QcAAACogR5iqyhBVIY4juJjH/tYM66EZxkKeeWVV3YVbb7+9a/3epfNynHL8NAnnnii
```

**Tool call:** `figma.get_screenshot` `{"fileKey": "<test-file-key>", "nodeId": "162:5919", "sessionId": "fa258de3-960c-42a3-be88-f9dff2f34bc0", "maxDimension": 1600, "enableBase64Response": true, "contentsOnly": true}`

**Tool result:** `figma.get_screenshot`

```text
{'content': [{'type': 'text', 'text': '{"image_url":"<figma-url> {'type': 'image', 'data': 'iVBORw0KGgoAAAANSUhEUgAAA6wAAAOsCAYAAABOOztEAAAACXBIWXMAAAPoAAAD6AG1e1JrAAAgAElEQVR4XuzdW4xlZZ0//NVO+x+YoQVM5s006IUQIIKZGMCooRmYhMZogBsVGrwwHgDvhnMmJkqjiSbIQe84eMhcCAjOBQc1ookwYsQIXMwIBlAno9Jt3gtB6Qw9x37z3f/3V7Nq9d61d52fqvp8kp2q2rVOe+29nv181/OsZ207dOjQoQ4AAAAa87ppEwAAAMB6EFgBAABoksAKAABAkwRWAAAAmiSwAgAA0CSBFQAAgCYJrAAAADRJYAUAAKBJAisAAABNElgBAABoksAKAABAkwRWAAAAmiSwAgAA0CSBFQAAgCYJrAAAADRJYAUAAKBJAisAAABNElgBAABo0vZpE7B5Pfnkk6PHNB/96Ee7N7zhDd1G8+ijj3bPPffctMm6q666atokAADAOhBYt7CE1dtvv33aZN0HPvCBDRtYH3jggWmTCawAANAoXYIBAABoksAKAABAkwRWAAAAmiSwAgAA0CSBFQAAgCYJrAAAADRJYAUAAKBJAisAAABNElgBAABo0vZuFf3xj3/sfv7zn3e//e1vR3+/6U1v6nbs2NGdeuqp3VKXl2VlmfGGN7xh9HjrW986+rlWsg312sp6bcukfZ1tOP7445e8r1dTtvGll16a29aV+GwAAABbKLA++eST3XXXXddN88QTTxz23Fe/+tXu0Ucf7X784x+PnefNb35z9653vau76qqrRkFlWhD75je/ueDy4t3vfnf3gQ98YPRYadmG7I9sQx5/+MMfFpy+Xt973vOebvfu3d1qyXZlX2f//OY3vxk7zdFHH92df/75M+3r1dJ/D5977rmp+6/ey+zD9dpmAABg/W07dOjQoXH/SEC75JJLumn+9V//de73hJErrrhiYngaSivg1Vdf3X30ox9dMDTPurwKi/fdd9+KBJ0KhHlMC1kLbU/C4koG6aVu18c+9rHu05/+9NzfX/ziF7vbb7+9m+ZHP/rRkvbnUrez74Mf/OCSw3Y+Ow888MCiPsMAAMAmvIY1YXXPnj2LCpcJNDfddNMoOA3luQTmxSwvMv173/ve0fYsR8Ly+973vlGgW2rYqu259tpru127ds3rArtUWcZSt+srX/nKaN9kv6+2tKbmNS9lO/sSOM8666yxnxEAAGBzW5HAmhCVsLrUYJJQk1a4xbb8TZJAlrC71IC41LC8kCw
```

**Tool call:** `figma.get_figjam` `{"fileKey": "<test-file-key>", "nodeId": "0:1", "sessionId": "fa258de3-960c-42a3-be88-f9dff2f34bc0"}`

**Tool result:** `figma.get_figjam`

```text
{'content': [{'type': 'text', 'text': '<canvas id="0:1" name="Page 1" x="0" y="0" width="0" height="0">\n  <shape-with-text id="1:3" x="768" y="-492" width="224" height="128" name="ROUNDED_RECTANGLE">Order list</shape-with-text>\n  <shape-with-text id="1:6" x="768" y="-236" width="224" height="128" name="SQUARE">Order detail</shape-with-text>\n  <shape-with-text id="1:9" x="780" y="20" width="200" height="200" name="DIAMOND">Within 30 days?</shape-with-text>\n  <shape-with-text id="1:12" x="608" y="476" width="224" height="128" name="ROUNDED_RECTANGLE">Contact support</shape-with-text>\n  <shape-with-text id="1:15" x="928" y="476" width="224" height="128" name="SQUARE">Pick a reason</shape-with-text>\n  <shape-with-text id="1:18" x="940" y="732" width="200" height="200" name="DIAMOND">Drop-off or pickup?</shape-with-text>\n  <shape-with-text id="1:21" x="768" y="1188" width="224" height="128" name="SQUARE">Choose a drop-off point</shape-with-text>\n  <shape-with-text id="1:24" x="1088" y="1188" width="224" height="128" name="SQUARE">Book a courier pickup</shape-with-text>\n  <shape-with-text id="1:27" x="928" y="1444" width="224" height="128" name="ROUNDED_RECTANGLE">Return confirmed with QR code</shape-with-text>\n  <connector id="1:30" x="880" y="-356" connectorStart="1:3" connectorStartCap="NONE" connectorEnd="1:6" connectorEndCap="ARROW_LINES"></connector>\n  <connector id="1:34" x="880" y="-100" connectorStart="1:6" connectorStartCap="NONE" connectorEnd="1:9" connectorEn
```

**Assistant:**

The two new sections overlap existing canvas content. I’m moving the complete sections to a clear area at the right edge of the plan so the flows and their labels are readable together.

**Tool call:** `figma.use_figma` `{"fileKey": "<test-file-key>", "sessionId": "fa258de3-960c-42a3-be88-f9dff2f34bc0", "skillNames": "resource:figma-use,resource:figma-use-figjam", "description": "Place the two new checkout sequence sections in clear space on the existing plan board", "code": "const moves = [\n  {id: \"161:5870\", x: 210000},\n  {id: \"162:5919\", x: 211300}\n];\nconst results = [];\nfor (const move of moves) {\n  const node = await figma.getNodeByIdAsync(move.id);\n  if (!node || node.type !== \"SECTION\") throw new Error(\"Expected section \" + move.id);\n  node.x = move.x;\n  results.push({id: node.id`

**Tool result:** `figma.use_figma`

```text
{'content': [{'type': 'text', 'text': '{"mutatedNodeIds":["161:5870","162:5919"],"sections":[{"id":"161:5870","name":"Roamstay checkout payment — authorised card","x":210000,"y":-492,"width":1140,"height":940},{"id":"162:5919","name":"Roamstay checkout payment — declined card","x":211300,"y":-492,"width":860,"height":860}]}'}], '_meta': {'mcpRequestId': 'aa6599fc-ef8e-4157-aad2-5c1834f19024', 'io.modelcontextprotocol/serverInfo': {'name': 'Figma MCP Server', 'version': '1.0.0', 'icons': [{'src': 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIAAAACgCAYAAADEkmT9AAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAhGVYSWZNTQAqAAAACAAFARIAAwAAAAEAAQAAARoABQAAAAEAAABKARsABQAAAAEAAABSASgAAwAAAAEAAgAAh2kABAAAAAEAAABaAAAAAAAAAEgAAAABAAAASAAAAAEAA6ABAAMAAAABAAEAAKACAAQAAAABAAAAgKADAAQAAAABAAAAoAAAAAB6dUZwAAAACXBIWXMAAAsTAAALEwEAmpwYAAABWWlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iWE1QIENvcmUgNi4wLjAiPgogICA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPgogICAgICA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIgogICAgICAgICAgICB4bWxuczp0aWZmPSJodHRwOi8vbnMuYWRvYmUuY29tL3RpZmYvMS4wLyI+CiAgICAgICAgIDx0aWZmOk9yaWVudGF0aW9uPjE8L3RpZmY6T3JpZW50YXRpb24+CiAgICAgIDwvcmRmOkRlc2NyaXB0aW9uPgogICA8L3JkZjpSREY+CjwveDp4bXBtZXRhPgoZXuEHAAARfklEQVR4Ae1de4xU1Rn/zr1zd5ddWFgRorEvAkrUAhURSgx2MI3PVEvMbuTV1jZVu2Aq/GGFBBhsUtBUaNr6jNZWqCbMH2gbEK3pbtWGiiBBomktCbamUSG47rLvmXtPf9+5c5fdZRd2Zu7unoHvJPO6
```

**Tool call:** `figma.get_screenshot` `{"fileKey": "<test-file-key>", "nodeId": "162:5919", "sessionId": "fa258de3-960c-42a3-be88-f9dff2f34bc0", "maxDimension": 1600, "enableBase64Response": true}`

**Tool result:** `figma.get_screenshot`

```text
{'content': [{'type': 'text', 'text': '{"image_url":"<figma-url> {'type': 'image', 'data': 'iVBORw0KGgoAAAANSUhEUgAAA6wAAAOsCAYAAABOOztEAAAACXBIWXMAAAPoAAAD6AG1e1JrAAAgAElEQVR4XuzdSYytZZ0/8PfatM1Ng4KrvqALIUAE4wIwarw0dMLFaICNigwL48CwawQknU4U0EQTmkF3DA7pBYOgC4bWCCZCi1EjsFDRAGov9HJdCQoJN73o+8/39P9X/dZ7z1TDqXqq6vNJTqrqnHc+533q/Z5neHft37//UAcAAACNecOsCQAAAGAzCKwAAAA0SWAFAACgSQIrAAAATRJYAQAAaJLACgAAQJMEVgAAAJoksAIAANAkgRUAAIAmCawAAAA0SWAFAACgSQIrAAAATRJYAQAAaJLACgAAQJMEVgAAAJoksAIAANAkgRUAAIAmCawAAAA0SWAFAACgSQIrAAAATRJYAQAAaJLACgAAQJMEVgAAAJoksAIAANAkgRUAAIAmCawAAAA0SWAFAACgSQIrAAAATRJYAQAAaJLACgAAQJMEVgAAAJoksAIAANAkgRUAAIAmCawAAAA0SWAFAACgSQIrAAAATRJYAQAAaJLACgAAQJMEVgAAAJp0RLcN7Nq1a/Q4dOjQrEkBAAC2tV3/Pxv9z//8z+j3rWzLBtbhgRdWAQAAuqVs9IY3vGHL56UjtnJtat6A3bt3d2984xu7I444YvQAAADYyf77v/97VLt68ODB7vXXX++2siO2Yq1qwurf/d3fdcccc8yybw0AAAB2uje+8Y2jn0ceeWR39NFHd6+++uqy4LqValuP2IpNgHPQjzrqqKnTAwAA7HR/8zd/M6roy8/XXntt9NxWGv/nDVstsCaoCqsAAADzS6Xfm970ptHvWyWsbpnAmgOaR/qr5kADAACwMn//938/6lpZ4wJtBVsisFY/VTWrAAAAq7fVxgFqfksr+ad21SjAAAAAq1d3WomtUMvafGAtGeEKAACAtUmz4K1iywTWjGoFAADA2myllqtbJrD+7d/+7axJAAAA2EaVgVsmsAIAALCzCKwAAAA0SWAFAACgSQIrAAAATRJYAQAAaJLACgAAQJMEVgAAAJoksAIAANAkgRUAAIAmCawAAAA0SWAFAACgSQIrAAAATRJYAQAAaJLACgAAQJMEVgAAAJoksAIAANAkgRUAAIAmCawAAAA0SWAFAACgSQIrAAAATRJYAQAAaJLACgAAQJMEVgAAAJoksAIAANAkgRUAAIAmCawAAAA0SWAFAACgSQIrAAAATRJ
```

**Tool call:** `figma.get_screenshot` `{"fileKey": "<test-file-key>", "nodeId": "161:5870", "sessionId": "fa258de3-960c-42a3-be88-f9dff2f34bc0", "maxDimension": 1600, "enableBase64Response": true}`

**Tool result:** `figma.get_screenshot`

```text
{'content': [{'type': 'text', 'text': '{"image_url":"<figma-url> {'type': 'image', 'data': 'iVBORw0KGgoAAAANSUhEUgAABMQAAAP8CAYAAACpvmK0AAAACXBIWXMAAAPoAAAD6AG1e1JrAAAgAElEQVR4Xuzda6xl5V0/8HUobWciUwdemM5UXwgBYmmMARo1DoEmTI0GeKNyTWy8cPFdC5QYEwVq0iZkAH3Hpdb0BZe2+oJLNaVNCpZGTYEYLTVAqYk6TF8VFBImxjj/fHf+v+k6a/btnLP3uT2fT7Jz9t7nWdd91nPW+u7nedbK0aNHT3QAAAAA0IjTZhUAAAAAgN1EIAYAAABAUwRiAAAAADRFIAYAAABAUwRiAAAAADRFIAYAAABAUwRiAAAAADRFIAYAAABAUwRiAAAAADRFIAYAAABAUwRiAAAAADRFIAYAAABAUwRiAAAAADRFIAYAAABAUwRiAAAAADRFIAYAAABAUwRiAAAAADRFIAYAAABAUwRiAAAAADRFIAYAAABAUwRiAAAAADRFIAYAAABAUwRiAAAAADRFIAYAAABAUwRiAAAAADRFIAYAAABAUwRiAAAAADRFIAYAAABAUwRiAAAAADRFIAYAAABAUwRiAAAAADRFIAYAAABAUwRiAAAAADRFIAYAAABAUwRiAAAAADRFIAYAAABAUwRiAAAAADRFIAYAAABAUwRiAAAAADTl9G4XWFlZGT1OnDgxqygAAAAA61DZy//93/+Nnu9kOzYQG+54YRgAAADA8pz4/w2RTjvttB2fx5y+k1uD5QPYu3dv9773va87/fTTRw8AAAAAFu9//ud/Rq3Djh8/3r377rvdTnb6TmwVljDs/e9/f7d///5VqSQAAAAAy/G+971v9HPPnj3dvn37urfffntVMLaTWoudvhO7SGann3HGGVPLAwAAALAc73nPe0YNlfLznXfeGb23k8Z3P22nBWIJwoRhAAAAAFtv37593Qc+8IHR850Shu2YQCw7NI+MF5YdDQAAAMD28BM/8ROjoa1q3PedYEcEYjVOmJZhAAAAANvP/h02zvu2X9NKFtM6zF0kAQAAALaf0047bZTdxE5oJbbtA7GSOxgAAAAAsD29//3v73aKHROI5a4FAAAAAGxPp59+erdT7JhA7L3vfe+sIgAAAABskffsoMZMOyYQAwAAAIBFEIgBAAAA0BSBGAAAAABNEYgBAAAA0BSBGAAAAABNEYgBAAAA0BSBGAAAAABNEYgBAAAA0BSBGAAAAABNEYgBAAAA0BSBGAAAAABNEYgBAAAA0BSBGAAAAABN
```

**Tool call:** `figma.get_figjam` `{"fileKey": "<test-file-key>", "nodeId": "0:1", "sessionId": "fa258de3-960c-42a3-be88-f9dff2f34bc0"}`

**Tool result:** `figma.get_figjam`

```text
{'content': [{'type': 'text', 'text': '<canvas id="0:1" name="Page 1" x="0" y="0" width="0" height="0">\n  <shape-with-text id="1:3" x="768" y="-492" width="224" height="128" name="ROUNDED_RECTANGLE">Order list</shape-with-text>\n  <shape-with-text id="1:6" x="768" y="-236" width="224" height="128" name="SQUARE">Order detail</shape-with-text>\n  <shape-with-text id="1:9" x="780" y="20" width="200" height="200" name="DIAMOND">Within 30 days?</shape-with-text>\n  <shape-with-text id="1:12" x="608" y="476" width="224" height="128" name="ROUNDED_RECTANGLE">Contact support</shape-with-text>\n  <shape-with-text id="1:15" x="928" y="476" width="224" height="128" name="SQUARE">Pick a reason</shape-with-text>\n  <shape-with-text id="1:18" x="940" y="732" width="200" height="200" name="DIAMOND">Drop-off or pickup?</shape-with-text>\n  <shape-with-text id="1:21" x="768" y="1188" width="224" height="128" name="SQUARE">Choose a drop-off point</shape-with-text>\n  <shape-with-text id="1:24" x="1088" y="1188" width="224" height="128" name="SQUARE">Book a courier pickup</shape-with-text>\n  <shape-with-text id="1:27" x="928" y="1444" width="224" height="128" name="ROUNDED_RECTANGLE">Return confirmed with QR code</shape-with-text>\n  <connector id="1:30" x="880" y="-356" connectorStart="1:3" connectorStartCap="NONE" connectorEnd="1:6" connectorEndCap="ARROW_LINES"></connector>\n  <connector id="1:34" x="880" y="-100" connectorStart="1:6" connectorStartCap="NONE" connectorEnd="1:9" connectorEn
```

**Assistant:**

Board: [Roamstay checkout payment sequences](<figma-url>

Read-back: succeeded; both authorised and declined flows show the requested steps, including the 201 and 402 responses.

Extensions: Added Booking API labels for “Hold room,” “Confirm hold” and “Release hold” because the renderer omitted self-messages. Moved both sections into clear board space.

Left out: No webhook confirmation or `payment_pending` step; the supplied brief doesn’t describe them.

Finding: The file already contains earlier checkout diagrams; these are new sections in that file.

Finding: The connected plan list didn’t include “Roamstay Product”; I used the supplied, writable file key.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.
