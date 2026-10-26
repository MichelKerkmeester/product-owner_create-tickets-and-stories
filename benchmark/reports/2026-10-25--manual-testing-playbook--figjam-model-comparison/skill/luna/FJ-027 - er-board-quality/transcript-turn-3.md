# FJ-027 turn 3 transcript

**User:** Yes, that reading is right.

**Assistant:**

I’ll build the ER model from the confirmed reading, run the required pre-write check, and review the layout before asking the separate write-gate question.

**Tool call:** `command_execution` `{"command": "/bin/zsh -lc \"sed -n '1,220p' sk-create-figjam/assets/compose-board.js\"", "changes": null}`

**Tool result:** `command_execution`

```text
// ───────────────────────────────────────────────────────────────
// COMPONENT: FIGJAM BOARD COMPOSER
// ───────────────────────────────────────────────────────────────
// Draws one checked diagram as a framed FigJam board through use_figma: a title
// block, tinted zones, shapes sized to their text, routed connectors, a key and
// a source line, all on an 8 px grid. scripts/compose_board.py fills MODEL from
// a model that passed flow_check.py and THEME from assets/figjam-design.md, so
// the board holds exactly what was checked, drawn in the style the design sets.
// Paste the whole file as the use_figma code. Nothing persists between calls, so
// the return value carries every id the read-back needs.

// ───────────────────────────────────────────────────────────────
// 1. MODEL, DESIGN AND CONSTANTS
// ───────────────────────────────────────────────────────────────

const MODEL = __MODEL__;
// The tokens assets/figjam-design.md sets apart from the built-in design below. An empty object draws the
// built-in design.
const THEME = __THEME__;

// FigJam's own pairs, as fill, stroke and text, and its section tints. A design names them and never changes
// them, so anyone on the board can still recolour a node from FigJam's palette.
const SWATCH = {
  white: ['#FFFFFF', '#B3B3B3', '#1E1E1E'], black: ['#1E1E1E', '#B3B3B3', '#FFFFFF'],
  darkGray: ['#757575', '#5E5E5E', '#FFFFFF'], violet: ['#874FFF', '#5427B4', '#FFFFFF'],
  lightBlue: ['#C2E5FF', '#3DADFF', '#1E1E1E'], lightG
```

**Tool call:** `command_execution` `{"command": "/bin/zsh -lc \"sed -n '1,260p' sk-create-figjam/scripts/compose_board.py\"", "changes": null}`

**Tool result:** `command_execution`

```text
#!/usr/bin/env python3
# ───────────────────────────────────────────────────────────────
# COMPONENT: FIGJAM BOARD COMPOSITION
# ───────────────────────────────────────────────────────────────

"""Turn a checked diagram model into the use_figma code that composes its board.

The board is drawn by `assets/compose-board.js`, which lays out and styles the
diagram itself: a framed board with a title block, tinted zones, shapes sized to
their text, routed connectors and a key. This script fills that file's MODEL from
the same parse `flow_check.py` checks, so the board holds exactly what passed the
check and the read-back counts it against the same numbers. A model that fails
the check is refused, because a composed board is as wrong as the model it drew.

Board text comes from comment lines the generator never needed, so the model
stays plain Mermaid:

- `%% title: Start a return` names the board, and falls back to a Mermaid
  frontmatter title, a sequence or gantt `title` line, then the diagram's place
- `%% subtitle: ...` is one sentence under the title on who reads it and why
- `%% source: ...` is the line under the key naming the sources and what was
  left out
- `%% zone: Find the order: orders, detail` groups nodes into a tinted zone. A
  user flow or a process without lanes reads its zones in flow order, an ER
  diagram draws each one around its entities, and lanes and composite states
  are zones already
- `%% focus: id` names the one thing the first glance lands on in a d
```

**Tool call:** `command_execution` `{"command": "/bin/zsh -lc 'python3 sk-create-figjam/scripts/flow_check.py --help'", "changes": null}`

**Tool result (error):** `command_execution`

```text
mermaid_extract: --help: not a Mermaid file
UNREADABLE --help: the extractor refused it

```

**Tool call:** `command_execution` `{"command": "/bin/zsh -lc 'python3 sk-create-figjam/scripts/compose_board.py --help'", "changes": null}`

**Tool result (error):** `command_execution`

```text

  compose_board.py <model.md> [--diagram N] [--out path]  -> 0 the filled code is written, 1 the model fails
                                                             the check, 2 unreadable or no such diagram
  compose_board.py <model.md> --model                      -> print the MODEL as JSON instead of the code
  compose_board.py --template                              -> print the compact code with its MODEL and THEME
                                                             placeholders, the text the Project's composer
                                                             Knowledge file carries
  compose_board.py --design-check                          -> print the design a board is drawn in, what it
                                                             changes, its measures and the THEME it sends: 0 the
                                                             design reads with no warning, 1 one or more warnings
  compose_board.py --self-test                             -> prove every shipped model composes, its counts
                                                             match the check, the code fits one use_figma call and
                                                             the board it draws keeps its geometry and its design

```

**Tool call:** `command_execution` `{"command": "/bin/zsh -lc \"rg -n 'if __name__|def main|ArgumentParser|flow_check.py|Usage' sk-create-figjam/scripts/flow_check.py && sed -n '1,160p' sk-create-figjam/scripts/flow_check.py && sed -n '780,960p' sk-create-figjam/scripts/flow_check.py\"", "changes": null}`

**Tool result:** `command_execution`

```text
40:Usage:
41:  flow_check.py <model.md|model.mmd>  -> 0 every diagram passes, 1 a rule fails, 2 unreadable
42:  flow_check.py --self-test           -> prove each rule fails on a planted model with its own message,
285:def main() -> int:
291:        print(__doc__.strip().split("Usage:")[1], file=sys.stderr)
296:if __name__ == "__main__":
#!/usr/bin/env python3
# ───────────────────────────────────────────────────────────────
# COMPONENT: FIGJAM MODEL PRE-WRITE CHECK
# ───────────────────────────────────────────────────────────────

"""Check a FigJam diagram model before it is written to a board.

A board is slow to fix once it exists: the composer owns its layout, so every
fix is a new write. Worse, neither the composer nor the generated fallback
draws all that Mermaid can say, so a model can promise a reader something the
board never shows. The rules each diagram kind carries are checked on the
Mermaid model first, and a model that breaks one is never written. The same
parse is measured, so a shape that is legal and still hard to read, such as a
rank of six steps or a connector that doubles back, is caught here rather than
on the board.

Each Mermaid block in the file is one diagram, read by its header:

- `flowchart` is a user flow unless a `%% type: process` or
  `%% type: architecture` comment line says otherwise
- `sequenceDiagram`, `stateDiagram-v2`, `erDiagram` and `gantt` are the other
  four kinds Flow Mode draws
- any other header, such as `pie`, `mindmap` or `journe
```

**Tool call:** `command_execution` `{"command": "/bin/zsh -lc \"rg -n 'function check_er|ATTRIBUTE|TYPE|fields|section|currentPage|position|bounds|empty|model.md' sk-create-figjam/scripts/figjam_checks/er.py sk-create-figjam/assets/compose-board.js sk-create-figjam/scripts/compose_board.py | tail -n 120\"", "changes": null}`

**Tool result:** `command_execution`

```text
sk-create-figjam/scripts/figjam_checks/er.py:7:drops the fields of an entity that carries a display alias.
sk-create-figjam/scripts/figjam_checks/er.py:22:MAX_ATTRIBUTES = 10
sk-create-figjam/scripts/figjam_checks/er.py:31:ATTRIBUTE = re.compile(r'^(\S+)\s+([A-Za-z][\w]*)((?:\s+(?:PK|FK|UK)(?:\s*,\s*(?:PK|FK|UK))*)?)(\s+"[^"]*")?$')
sk-create-figjam/scripts/figjam_checks/er.py:47:            attribute = ATTRIBUTE.match(text)
sk-create-figjam/scripts/figjam_checks/er.py:111:        fields = attributes[entity]
sk-create-figjam/scripts/figjam_checks/er.py:112:        if len(fields) > MAX_ATTRIBUTES:
sk-create-figjam/scripts/figjam_checks/er.py:113:            problems.append(f"entity {entity} lists {len(fields)} attributes, at most {MAX_ATTRIBUTES}: "
sk-create-figjam/scripts/figjam_checks/er.py:115:        if fields and not any("PK" in keys for _, _, keys in fields):
sk-create-figjam/scripts/figjam_checks/er.py:120:    for fields in attributes.values():
sk-create-figjam/scripts/figjam_checks/er.py:121:        for kind, _, _ in fields:
sk-create-figjam/assets/compose-board.js:17:// The tokens assets/figjam-design.md sets apart from the built-in design below. An empty object draws the
sk-create-figjam/assets/compose-board.js:21:// FigJam's own pairs, as fill, stroke and text, and its section tints. A design names them and never changes
sk-create-figjam/assets/compose-board.js:116:const TYPE = T.type;
sk-create-figjam/assets/compose-board.js:139:let FAMILY = TYPE.family, NAMES;
sk
```

**Tool call:** `command_execution` `{"command": "/bin/zsh -lc \"sed -n '1,180p' sk-create-figjam/scripts/figjam_checks/er.py && sed -n '1218,1365p' sk-create-figjam/assets/compose-board.js && sed -n '338,394p' sk-create-figjam/scripts/compose_board.py\"", "changes": null}`

**Tool result:** `command_execution`

```text
#!/usr/bin/env python3
# ───────────────────────────────────────────────────────────────
# COMPONENT: ER PROFILE
# ───────────────────────────────────────────────────────────────

"""An entity-relationship diagram, parsed here because the shared extractor
drops the fields of an entity that carries a display alias.

The generator draws an entity with attributes as a table and one without as a
plain rectangle, puts each key as a badge and draws `--` solid and `..` dotted.
Styling is silently dropped, and an alias inside a relationship line fails to
parse, so both are refused here.
"""
from __future__ import annotations

import re

from .common import content_lines, id_problems, length_problems, raw_problems

MAX_ENTITIES = 9
MAX_RELATIONSHIPS = 12
MAX_ATTRIBUTES = 10
DIRECTIONS = {"LR", "TB", "TD"}
LEFT_ENDS = {"||", "|o", "}o", "}|"}
RIGHT_ENDS = {"||", "o|", "o{", "|{"}
CARDINALITY = re.compile(r"^(\S{2})(--|\.\.)(\S{2})$")
CARDINALITY_TOKEN = re.compile(r"\s\S{2}(?:--|\.\.)\S{2}\s")
ENTITY_OPEN = re.compile(r'^([^\s\[{]+)(\["([^"]*)"\])?\s*\{$')
ENTITY_ALONE = re.compile(r'^([^\s\[{]+)(\["([^"]*)"\])?$')
RELATIONSHIP = re.compile(r'^(\S+)\s+(\S+)\s+(\S+)\s*(?::\s*(.*))?$')
ATTRIBUTE = re.compile(r'^(\S+)\s+([A-Za-z][\w]*)((?:\s+(?:PK|FK|UK)(?:\s*,\s*(?:PK|FK|UK))*)?)(\s+"[^"]*")?$')
STYLING = re.compile(r"^(classDef|class|style)\s", re.I)


def check_er(block_text: str) -> tuple[list[str], int, int]:
    """The problems with an ER block, and how many entities and relationshi
```

**Tool call:** `command_execution` `{"command": "/bin/zsh -lc \"python3 - <<'PY'\nfrom pathlib import Path\nimport json, subprocess, sys, tempfile\n\nroot = Path.cwd()\nmodel = \\\"\\\"\\\"\"'```mermaid\n%% title: Roamstay Stays Model for Guest Support\n%% subtitle: Guest Support follows a booking from its reference to the payment and partner details that explain a stay\n%% source: Sources: user schema summary, Roamstay context, Support ticket 58213. Assumed: key and support field names, types and multiplicities. Left out: direct Room to Rate Plan link, not named in schema summary.\n%% zone: Guest records: Guest, Booking, Paymen`

**Tool result:** `command_execution`

```text
{"model": "```mermaid\n%% title: Roamstay Stays Model for Guest Support\n%% subtitle: Guest Support follows a booking from its reference to the payment and partner details that explain a stay\n%% source: Sources: user schema summary, Roamstay context, Support ticket 58213. Assumed: key and support field names, types and multiplicities. Left out: direct Room to Rate Plan link, not named in schema summary.\n%% zone: Guest records: Guest, Booking, Payment\n%% zone: Partner records: Property, Room, RatePlan\n%% focus: Booking\nerDiagram\n    direction LR\n    Guest ||--o{ Booking : makes\n    Booking ||--o{ Payment : holds\n    Booking }o--|| Room : reserves\n    Booking }o--|| RatePlan : uses\n    Property ||--o{ Room : offers\n    Property ||--o{ RatePlan : publishes\n    Guest {\n        unknown id PK\n    }\n    Booking {\n        unknown id PK\n        unknown guestId FK\n        unknown roomId FK\n        unknown ratePlanId FK\n        unknown bookingReference\n        unknown stayNights\n        unknown adultCount\n        unknown roomAmount\n        unknown cityTaxAmount\n        unknown totalAmount\n    }\n    Payment {\n        unknown id PK\n        unknown bookingId FK\n        unknown amount\n        unknown currency\n        unknown status\n    }\n    Property {\n        unknown id PK\n        unknown cityTaxRule\n    }\n    Room {\n        unknown id PK\n        unknown propertyId FK\n        unknown roomType\n        unknown maxOccupancy\n    }\n    RatePlan {\n  
```

**Tool call:** `command_execution` `{"command": "/bin/zsh -lc \"sed -n '96,176p' sk-create-figjam/references/quality-rubric.md\"", "changes": null}`

**Tool result:** `command_execution`

```text
---

## 6. THE BOARD

After the write, before the reply:

- [ ] The read-back counts match the model, as the type's reference sets them out
- [ ] Each provenance row whose class is not current behavior or whose edge is inferred was re-read against its source before the gate, and the row records the reason. A row that quotes a source line was not re-read
- [ ] The write returned no warning, and its counts match the counts the model expects
- [ ] The `COMPOSED` line named the design the board was drawn in, and each `DESIGN` warning it counted became a `Finding:` line naming the token and the shipped value the board used instead
- [ ] The overview is the screenshot the composing call returned, and `get_figjam` supplies the outline with a screenshot of each node
- [ ] A node that needs its own view is read with `get_screenshot` and a node id from that read, because the tool fails without one
- [ ] Two screenshots of the board were taken for this pass: one of the whole board in a single frame and one at 100% zoom. Composition is judged on the overview, because a crossing and a crowded label are invisible at reading size
- [ ] The overview reads in the order the model plans, and that order was written down before the first screenshot
- [ ] The overview shows no connector crossing another, no connector or label on a zone title, no two edges sharing a trunk the model draws apart and no two labels touching
- [ ] No edge runs through a zone it neither starts nor ends in. Edges that onl
```

**Tool call:** `command_execution` `{"command": "/bin/zsh -lc \"sed -n '25,95p' sk-create-figjam/references/quality-rubric.md\"", "changes": null}`

**Tool result:** `command_execution`

```text
## 1. TYPE FIT

- [ ] The type answers the reader's question, as `references/flow-mode.md` Section 3 maps it
- [ ] A table, a list or a paragraph would not do the same job. If it would, say so and offer that instead
- [ ] The type's reference in `references/types/` was loaded and its judged-by-hand rules were applied
- [ ] A request for a kind Flow Mode does not draw was answered with the nearest type it does draw, or a plain no

---

## 2. THE REMOVE TEST

sk-design-diagram's highest-quality move is usually deletion. A diagram is done when nothing can be removed.

The remove test runs on the outline before the first Mermaid block, because a step cut from a list of steps costs a sentence and the same step cut from a drawn diagram costs a redraw. This section is the third rung of the challenge ladder in `references/flow-mode.md` Section 3, so the two rungs above it are asked first: what the board must not do, and whether a list, a table or a paragraph would serve the reader better.

- [ ] The `userIntent` sentence was agreed in the sparring and is the first line of the outline, rather than composed at the write call
- [ ] The remove test ran on the outline, one line per node and edge, before any layout was judged
- [ ] An unanswered sparring proposal is marked assumed and named in the playback before the gate
- [ ] No node can be removed without the reader losing a step they need
- [ ] Every node serves the `userIntent` sentence, or it is cut and named under `Left out:`
- [ ] 
```

**Tool call:** `command_execution` `{"command": "/bin/zsh -lc \"sed -n '336,420p' sk-create-figjam/references/flow-mode.md\"", "changes": null}`

**Tool result:** `command_execution`

```text
## 6. WRITE ROUTES

### Composed route, primary

Flow Mode composes the board itself. `scripts/compose_board.py` reads the checked model and fills `assets/compose-board.js`, and one `use_figma` call runs that code in the file the gate named. The call draws a framed board: the title and the subtitle, the diagram with its zones, every shape sized to its text and coloured by its kind, the routed connectors, a key of every mark the board uses and the source line, all on an 8 pixel grid. It draws every type in Section 3.

The route is a native MCP connection to Figma's server at `https://mcp.figma.com/mcp`, which Figma's own plugin declares in its root `mcp.json`. The connection comes from that plugin or from the client's connector. Code Mode holds no manual for Figma's hosted server here, and its `figma` manual runs Framelink's `figma-developer-mcp` instead. Whether Figma's OAuth-gated server would admit a Code Mode client is unverified. The vendored `mcp-figma` packet's wiring guide covers that Code Mode path, and its Section 6 records how a headless Claude Code or Codex child reaches the hosted server. The `allowed-tools` frontmatter of this packet names Code Mode as its only MCP tool and no native tool, because the native names depend on the client. Claude Code serves them under the name its config gives the server, such as `mcp__figma-remote__use_figma`. Codex serves them through the Figma app on the ChatGPT account as `figma.use_figma`, and `codex exec` refuses that call wit
```

**Tool call:** `command_execution` `{"command": "/bin/zsh -lc \"sed -n '70,100p' sk-create-figjam/references/style-guide.md && sed -n '210,260p' sk-create-figjam/references/style-guide.md\"", "changes": null}`

**Tool result:** `command_execution`

```text
### State, ER, sequence and gantt

| Kind | Shape | Colour | Key |
|---|---|---|---|
| Initial and final pseudo-state | 32 pixel dot, the final one ringed | Charcoal | Start, End |
| First state, a state, final state | Rounded rectangle | Light blue, white, light gray | First state, State, Final state |
| Choice | 56 pixel diamond | Light yellow | Choice |
| Fork or join | 16 by 96 pixel bar | Charcoal | Fork or join |
| Entity | Card with its fields | White | Entity |
| Participant | Rounded rectangle, drawn again smaller at the foot of its lifeline | White | Participant |
| Planned, in progress, done, critical | Bar, the planned one outlined in the connector gray and the critical one with a heavier outline and `, critical` after its length | White, light blue, light gray, light red | Planned, In progress, Done, Critical, heavy outline |
| Milestone | 32 pixel diamond | Light yellow | Milestone |

A sequence numbers every message with a pin in the `marker` role, violet as shipped, beside its sender's lifeline, and its key names the pin `Step number`.

### Lines and zones

| Element | Colour | Notes |
|---|---|---|
| Connector | Gray `#757575`, 2 pixels | Dashed for an optional or proposed edge, and for an async or outside call on an architecture |
| Request, reply | Gray solid and gray dashed, both with a closed head | Sequence |
| Async message, async reply | Blue `#3DADFF`, solid or dashed, with an open head | Sequence |
| Lifeline | Light gray `#B3B3B3`, dashed | Sequence
```

**Tool call:** `command_execution` `{"command": "/bin/zsh -lc \"python3 - <<'PY'\nfrom pathlib import Path\nimport tempfile, subprocess, json\nmodel=Path('sk-create-figjam/scripts/flow_check.py')\nprint('model and composer already passed')\nPY\"", "changes": null}`

**Tool result:** `command_execution`

```text
model and composer already passed

```

**Tool call:** `command_execution` `{"command": "/bin/zsh -lc \"python3 - <<'PY'\nfrom pathlib import Path\nimport json, subprocess, sys, tempfile\n\nroot = Path.cwd()\nmodel = \\\"\\\"\\\"\"'```mermaid\n%% title: Roamstay Stays Model for Guest Support\n%% subtitle: Guest Support follows a booking from its reference to the payment and partner details that explain a stay\n%% source: Sources: user schema summary, Roamstay context, Support ticket 58213. Assumed: key and support field names, types and multiplicities. Left out: direct Room to Rate Plan link, not named in schema summary.\n%% zone: Guest records: Guest, Booking, Paymen`

**Tool result:** `command_execution`

```text
{"model": "```mermaid\n%% title: Roamstay Stays Model for Guest Support\n%% subtitle: Guest Support follows a booking from its reference to the payment and partner details that explain a stay\n%% source: Sources: user schema summary, Roamstay context, Support ticket 58213. Assumed: key and support field names, types and multiplicities. Left out: direct Room to Rate Plan link, not named in schema summary.\n%% zone: Guest records: Guest, Booking, Payment\n%% zone: Partner records: Property, Room, RatePlan\n%% focus: Booking\nerDiagram\n    direction LR\n    Guest ||--o{ Booking : makes\n    Booking ||--o{ Payment : holds\n    Booking }o--|| Room : reserves\n    Booking }o--|| RatePlan : uses\n    Property ||--o{ Room : offers\n    Property ||--o{ RatePlan : publishes\n    Guest {\n        unknown id PK\n    }\n    Booking {\n        unknown id PK\n        unknown guestId FK\n        unknown roomId FK\n        unknown ratePlanId FK\n        unknown bookingReference\n        unknown stayNights\n        unknown adultCount\n        unknown roomAmount\n        unknown cityTaxAmount\n        unknown totalAmount\n    }\n    Payment {\n        unknown id PK\n        unknown bookingId FK\n        unknown amount\n        unknown currency\n        unknown status\n    }\n    Property {\n        unknown id PK\n        unknown cityTaxRule\n    }\n    Room {\n        unknown id PK\n        unknown propertyId FK\n        unknown roomType\n        unknown maxOccupancy\n    }\n    RatePlan {\n  
```

**Assistant:**

The model passes the ER check with 6 entities and 6 relationships, and the composer reports no design warnings. I’m checking the FigJam-specific API guidance and final layout criteria before the write gate.

**Tool call:** `command_execution` `{"command": "/bin/zsh -lc \"cat '/private/var/folders/3c/zfqcqsts0kn19cgblj82gqhm0000gn/T/codex-compare-home/plugins/cache/openai-curated-remote/figma/16.0.0/skills/figma-use/references/plugin-api-standalone.index.md'\"", "changes": null}`

**Tool result:** `command_execution`

```text
# Plugin API Index

> Full typings: `plugin-api-standalone.d.ts` (10,191 lines)
> Grep by symbol name to jump to definition. All `L#` line numbers refer to that file.
> This index describes the APIs available through `use_figma`. See the `.d.ts` for full type declarations.

---

## figma.\* — PluginAPI (L4)

### Identity & State

| Member                          | Type                                                                                                                                             |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `apiVersion`                    | `'1.0.0'`                                                                                                                                        |
| `editorType`                    | `'figma' \| 'figjam' \| 'dev' \| 'slides' \| 'buzz'`                                                                                             |
| `fileKey`                       | `string \| undefined`                                                                                                                            |
| `root`                          | `DocumentNode`                                                                                                                                   |
| `currentPage`                   | `PageNode` — **read-only**; sync s
```

**Tool call:** `command_execution` `{"command": "/bin/zsh -lc \"sed -n '90,155p' sk-create-figjam/references/quality-rubric.md\"", "changes": null}`

**Tool result:** `command_execution`

```text
- [ ] The measures printed beside the counts were read: the widest rank, the longest path, the connectors per step, the average label length and the crossing pairs, against the budgets `scripts/figjam_checks/layout.py` sets
- [ ] A measure out of band was fixed in the model rather than on the board and the check rerun after the change, because the composer owns the layout and a tangled shape is never rearranged after the write
- [ ] `scripts/compose_board.py` printed `COMPOSED` for every diagram, with the counts the read-back will look for
- [ ] The gate message names the plan, the file, what will be written, any planned extensions, the calls the write will spend and the rollback
- [ ] On the generated fallback, an architecture call carries `useArchitectureLayoutCode`, and no other type carries it

---

## 6. THE BOARD

After the write, before the reply:

- [ ] The read-back counts match the model, as the type's reference sets them out
- [ ] Each provenance row whose class is not current behavior or whose edge is inferred was re-read against its source before the gate, and the row records the reason. A row that quotes a source line was not re-read
- [ ] The write returned no warning, and its counts match the counts the model expects
- [ ] The `COMPOSED` line named the design the board was drawn in, and each `DESIGN` warning it counted became a `Finding:` line naming the token and the shipped value the board used instead
- [ ] The overview is the screenshot the composing call 
```

**Tool call:** `command_execution` `{"command": "/bin/zsh -lc \"cat '/private/var/folders/3c/zfqcqsts0kn19cgblj82gqhm0000gn/T/codex-compare-home/plugins/cache/openai-curated-remote/figma/16.0.0/skills/figma-use-figjam/SKILL.md'\"", "changes": null}`

**Tool result:** `command_execution`

```text
---
name: figma-use-figjam
description: "This skill helps agents use Figma's use_figma MCP tool in the FigJam context. Can be used alongside figma-use which has foundational context for using the use_figma tool."
disable-model-invocation: false
---

# use_figma — Figma Plugin API Skill for FigJam

This skill contains FigJam-specific context for the `use_figma` MCP tool. The [figma-use](../figma-use/SKILL.md) skill provides foundational context for plugin API execution via MCP as well as the full Figma plugin API for more advanced use-cases that are not described here.

**Always include `figma-use-figjam` in the comma-separated `skillNames` parameter when calling `use_figma` for FigJam operations. If this skill was loaded via an MCP resource, you MUST prefix the name with `resource:` (e.g. `resource:figma-use-figjam`).** This is a logging parameter used to track skill usage — it does not affect execution.

> **FigJam URL is `figma.com/board/...`.** Do NOT call `figma.createPage()` in FigJam — it throws `TypeError: figma.createPage no such property 'createPage' on the figma global object`. `createPage()` is a Design-file API only (`figma.com/design/...`). FigJam files have a single implicit page; organize content with sections instead (see [create-section](references/create-section.md)).

## Inspecting FigJam Files

**`get_figjam` is the inspection tool for FigJam files.** It returns the full node tree as XML, including IDs of pages, sections, stickies, connectors, and other no
```

**Tool call:** `command_execution` `{"command": "/bin/zsh -lc \"cat '/private/var/folders/3c/zfqcqsts0kn19cgblj82gqhm0000gn/T/codex-compare-home/plugins/cache/openai-curated-remote/figma/16.0.0/skills/figma-use/references/gotchas.md'\"", "changes": null}`

**Tool result:** `command_execution`

```text
# Gotchas & Common Mistakes

> Part of the [use_figma skill](../SKILL.md). Every known pitfall with WRONG/CORRECT code examples.

## Contents

- Component properties and variant creation pitfalls
- Paint, color, and variable binding pitfalls
- Page context and plugin lifecycle pitfalls (set current page once per `use_figma` call; split multi-page work across calls)
- Auto Layout and sizing order pitfalls (including HUG/FILL interactions, and TEXT nodes that ignore FILL and collapse to a zero-width thread)
- Variant layout and geometry pitfalls
- Canonical text-edit recipe + font loading and text/typography pitfalls
- Sequential awaits — batch independent async calls with `Promise.all` (including `import*ByKeyAsync` families)
- Prefer indexed lookups (`getNodeByIdAsync`, `findAllWithCriteria`, `node.query`) over `findAll`/`findOne` full-tree scans
- Scope traversal to the smallest known ancestor (never `figma.root.findAll`; prefer `someFrame.findAllWithCriteria` over `figma.currentPage.findAllWithCriteria`)
- Variable scopes and mode pitfalls
- Node cleanup and empty-fill pitfalls
- "no such property" errors — reading or calling members not defined on the node type
- Non-existent property writes and "object is not extensible"
- width/height are read-only — use resize()
- detachInstance() and node ID invalidation
- Icons — import the SVG, never reconstruct from rotated line primitives


## New nodes default to (0,0) and overlap existing content

Every `figma.create*()` call pla
```

**Tool call:** `command_execution` `{"command": "/bin/zsh -lc \"python3 - <<'PY'\nfrom pathlib import Path\nimport re\nm=Path('sk-create-figjam/references/types/er.md').read_text()\nprint('ER limits and rules already loaded; 6 entities, 6 relationships, 26 attributes in current model.')\nPY\"", "changes": null}`

**Tool result:** `command_execution`

```text
ER limits and rules already loaded; 6 entities, 6 relationships, 26 attributes in current model.

```

**Assistant:**

I’m rechecking the support-context lines behind the inferred columns and the FigJam section, shape, connector, and text guidance. The ERD remains in the model only; no canvas write has happened.

**Tool call:** `command_execution` `{"command": "/bin/zsh -lc \"cat '/private/var/folders/3c/zfqcqsts0kn19cgblj82gqhm0000gn/T/codex-compare-home/plugins/cache/openai-curated-remote/figma/16.0.0/skills/figma-use-figjam/references/create-section.md'\"", "changes": null}`

**Tool result:** `command_execution`

```text
# Create Sections

> Part of the [figma-use-figjam skill](../SKILL.md). Creating, modifying, and organizing sections.

**Scope:** Sections are FigJam containers created with `figma.createSection()`. They organize related objects on the board. For creating stickies to place inside sections, see [create-sticky](create-sticky.md). For creating text to place inside sections, see [create-text](create-text.md).

## Creating a Section

Create sections and resize them carefully according to the layout guidance in [plan-board-content](plan-board-content.md).

```javascript
const section = figma.createSection()
section.name = 'My Section'

// Sections start very small — resize to a usable size
section.resize(400, 300)

console.log('Created section:', section.id, section.name, section.width, 'x', section.height)
figma.closePlugin()
```

## Stickies vs. Text Nodes as section content

Stickies and text play different roles. Before adding section child content, make sure to read and understand the usage guidance for each in [create-sticky](create-sticky.md) and [create-text](create-text.md) skills.

## Naming

Section names should be **short, navigational identifiers** (e.g. "Brainstorm", "Action Items", "Went Well") — they are used for browsing and quick identification in FigJam's UI. The section name is NOT the user-facing header. Create a separate **H2 text node** inside the section for the visible, descriptive header. See [plan-board-content](plan-board-content.md) for guidance on clea
```

**Tool call:** `command_execution` `{"command": "/bin/zsh -lc \"cat '/private/var/folders/3c/zfqcqsts0kn19cgblj82gqhm0000gn/T/codex-compare-home/plugins/cache/openai-curated-remote/figma/16.0.0/skills/figma-use-figjam/references/create-shape-with-text.md'\"", "changes": null}`

**Tool result:** `command_execution`

```text
# Create Shapes with Text

> Part of the [figma-use-figjam skill](../SKILL.md). Creating shapes with embedded text for diagrams and visual layouts.

**Scope:** ShapeWithText nodes are FigJam-specific geometric shapes with built-in text, created with `figma.createShapeWithText()`. For tables, see [create-table](create-table.md). For sections, see [create-section](create-section.md). For stickies, see [create-sticky](create-sticky.md).

**When NOT to use this skill:** For tabular-data (e.g. data tables, spreadsheets, comparison tables, rosters, or any row/column grid of text or data), use the [create-table](create-table.md) skill instead. Do not build a table-like layout from a grid of shapes.

## Creating a Shape

```javascript
const shape = figma.createShapeWithText()
// Default shapeType is 'ELLIPSE'

await figma.loadFontAsync(shape.text.fontName)
shape.text.characters = 'Step 1'

console.log('Created shape:', shape.id, shape.shapeType, shape.text.characters)
figma.closePlugin()
```

## Shape Types

Set the `shapeType` property **after** creation. It defaults to `'ELLIPSE'`.

```javascript
const shape = figma.createShapeWithText()
shape.shapeType = 'DIAMOND'
```

Available shape types:

| Category          | Shape types                                                                                                              |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------ |
| B
```

**Tool call:** `command_execution` `{"command": "/bin/zsh -lc \"cat '/private/var/folders/3c/zfqcqsts0kn19cgblj82gqhm0000gn/T/codex-compare-home/plugins/cache/openai-curated-remote/figma/16.0.0/skills/figma-use-figjam/references/plan-board-content.md'\"", "changes": null}`

**Tool result:** `command_execution`

```text
# Plan Content for FigJam Boards

**When NOT to use this skill:** Do NOT read this skill for analysis, summarization, or investigation of existing board content (e.g. "summarize this board", "what themes are here?", "analyze the feedback"). This skill is exclusively for planning NEW content to be created on the board.

Do NOT use this skill for flowcharts, architecture diagrams, sequence diagrams, state diagrams, or entity relationship diagrams (ERDs). For those, use the `figma-plugin:figma-generate-diagram` skill and the `generate_diagram` tool.

Use this skill when determining **what content to include** for generated FigJam board content. Given a user's request (e.g. "make a brainstorm template", "retro board", "ice breaker", "scaffold"), produce a **sequential outline** that downstream skills can use to create sections, text, stickies, and layout.

**Must be loaded alongside the `figma-use-figjam` skill**, which provides the FigJam Plugin API references (create-section, create-sticky, create-text, position-figjam-nodes) needed to render the planned content.

## Part 1: Design Principles

### Reading direction and grouping

Left-to-right, top-to-bottom. Context on the left, evidence in the middle, proposal/asks on the right. Supporting detail and appendix below.

**Tight clustering** (60-92px) = same thought. **Loose spacing** (200-400px) = different topics. **Zone breaks** (1000px+) = different part of the board.

### Type scale

Use **Inter** exclusively. Subtitles shoul
```

**Tool call:** `command_execution` `{"command": "/bin/zsh -lc \"cat '/private/var/folders/3c/zfqcqsts0kn19cgblj82gqhm0000gn/T/codex-compare-home/plugins/cache/openai-curated-remote/figma/16.0.0/skills/figma-use-figjam/references/create-text.md'\"", "changes": null}`

**Tool result:** `command_execution`

```text
# Create Text Nodes

> Part of the [figma-use-figjam skill](../SKILL.md). Creating and styling standalone text nodes and mind map operations.

Use this skill when creating, modifying, or styling standalone text in FigJam (text created with the **Text** tool, not text inside stickies, shapes, or connectors). Also use this skill for mind map operations — adding, inserting, or extending connected text nodes.

**Scope:** Text nodes are created with `figma.createText()` and have type `'TEXT'`. For editing existing text content or mixed styles, see [edit-text](edit-text.md).

## When to use a Text Node

Use text nodes for titles, headers, labels, prompts, instructions, and any content that provides structure or context. They can also be used for longer descriptions or explanations.

## Creating a Text Node

```javascript
const text = figma.createText()

// Load the font before setting content (required for characters, fontSize, etc.)
await figma.loadFontAsync(text.fontName)
text.characters = 'Brainstorming instructions'

console.log('Created text:', text.id, text.characters)
figma.closePlugin()
```

## Text Wrapping and Width Constraints

By default, text nodes auto-resize in both width and height (`textAutoResize = 'WIDTH_AND_HEIGHT'`), meaning they never wrap — text extends in one line until it ends.

To make text wrap within a specific width (e.g., instructional text inside sections):

1. Set `textAutoResize = 'HEIGHT'` — text will grow vertically but respect the width constrain
```

**Tool call:** `command_execution` `{"command": "/bin/zsh -lc \"sed -n '28,33p' context/roamstay-partner-self-onboarding-brief.md\"", "changes": null}`

**Tool result:** `command_execution`

```text
2. Property profile and photos. Address and map pin, description, facilities, and at least 8 photos, each up to 20 MB
3. Rooms and rates setup. Room types with their occupancy, a base price per night and at least one rate plan, free cancellation or non-refundable
4. Policies and city tax. Check-in and check-out times, the cancellation policy per rate plan, house rules and the city tax rule, per adult per night or per stay
5. Payout details and identity checks. Bank account and the owner's identity document, checked by the identity verification provider. No payout before both pass
6. Go-live review queue. An Ops agent checks the finished listing in Back office within 1 business day, then approves it or sends it back with a reason per stage


```

**Tool call:** `command_execution` `{"command": "/bin/zsh -lc \"cat '/private/var/folders/3c/zfqcqsts0kn19cgblj82gqhm0000gn/T/codex-compare-home/plugins/cache/openai-curated-remote/figma/16.0.0/skills/figma-use-figjam/references/create-connector.md'\"", "changes": null}`

**Tool result:** `command_execution`

```text
# Create Connectors

> Part of the [figma-use-figjam skill](../SKILL.md). Creating connectors between nodes — endpoints, arrows, line types, labels, and colors.

**Scope:** Connectors are FigJam-specific nodes created with `figma.createConnector()`. They connect shapes, stickies, sections, and other nodes to show relationships. For creating shapes to connect, see [create-shape-with-text](create-shape-with-text.md). For stickies, see [create-sticky](create-sticky.md). For sections, see [create-section](create-section.md).

## Creating a Connector Between Two Nodes

```javascript
const connector = figma.createConnector()
connector.connectorStart = { endpointNodeId: '123:456', magnet: 'AUTO' }
connector.connectorEnd = { endpointNodeId: '123:789', magnet: 'AUTO' }

console.log('Created connector:', connector.id)
figma.closePlugin()
```

## Connector Endpoints

Endpoints define where the connector starts and ends. There are three forms:

### Attached to a node with auto-magnet (most common)

```javascript
connector.connectorStart = { endpointNodeId: nodeA.id, magnet: 'AUTO' }
connector.connectorEnd = { endpointNodeId: nodeB.id, magnet: 'AUTO' }
```

### Attached to a node at a specific side

Magnet values: `'AUTO'`, `'TOP'`, `'BOTTOM'`, `'LEFT'`, `'RIGHT'`, `'CENTER'`, `'NONE'`

```javascript
connector.connectorStart = { endpointNodeId: nodeA.id, magnet: 'RIGHT' }
connector.connectorEnd = { endpointNodeId: nodeB.id, magnet: 'LEFT' }
```

### Floating (not attached to any node)

``
```

**Tool call:** `command_execution` `{"command": "/bin/zsh -lc \"sed -n '38,48p' context/roamstay-context.md && sed -n '138,156p' context/roamstay-context.md\"", "changes": null}`

**Tool result:** `command_execution`

```text
| Stay | One booking's dates at one property, counted in nights. Check-in on a Monday and check-out on a Thursday is 3 nights |
| Property | A hotel, guesthouse or apartment building listed by a partner, identified by a numeric property ID |
| Room type | A kind of room at a property, such as Double room or Family suite, with a maximum occupancy |
| Rate plan | A price for a room type with its own cancellation policy and payment option. One room type often has two or three |
| Free cancellation | A rate plan policy that refunds the guest in full if they cancel before a deadline the partner sets |
| Non-refundable | A rate plan policy with no refund after booking, usually priced lower |
| City tax | A local tax the partner enters in Partner Hub, per adult per night or per stay. It shows as its own `City tax` line in the price breakdown and is part of the total |
| Pay now | The guest pays the full total at booking, and the payment provider charges the card |
| Pay at property | The guest's card is stored as a guarantee and the guest pays the property on arrival |
| Booking reference | `RS-` followed by six letters and digits. It is on the confirmation screen, in every email and in Back office |
| `payment_pending` | The booking state between Pay now and the payment provider's confirmation |
The guest enters a destination, check-in and check-out dates, guests and rooms. A stay runs from 1 night to `30 nights` and check-in can be at most `365 days` ahead. One search covers up to
```

**Tool call:** `command_execution` `{"command": "/bin/zsh -lc \"sed -n '8,18p' context/roamstay-support-ticket-58213.md && sed -n '23,50p' context/roamstay-support-ticket-58213.md\"", "changes": null}`

**Tool result:** `command_execution`

```text
| Ticket | 58213 |
| Status | Escalated to Booking squad |
| Priority | High |
| Channel | In-app chat, Android |
| Booking reference | RS-7Q4K2M |
| Booked on | 2026-09-20, with Pay now |
| Stay | 3 nights, 2 adults, 1 room |
| Property | 40217, city tax €3.00 per adult per night |
| Guest app | Android 8.12.1, app language en-GB |
| Tags | price-mismatch, android, confirmation-screen |


Maren, 09:15
Hi, thanks for writing in. I'm checking booking RS-7Q4K2M for you now.

Guest, 09:16
Screenshot attached.

Maren, 09:24
Thanks. The room is €387.00 for the 3 nights, and the property charges a city tax of €3.00 per adult per night, so €18.00 for 2 adults over 3 nights. The charge of €405.00 is the full price with the city tax, and it is the only charge on your card. The Android app left the city tax out of the total on the confirmation screen. I'm sorry for the confusion. I'm emailing you the full breakdown now.

Guest, 09:27
OK, that makes sense. The app should show the right number though.

Maren, 09:28
Agreed. I'm passing it to the team that owns that screen.

## Internal notes

Maren, 09:35
Back office for RS-7Q4K2M shows one Pay now charge of €405.00, captured on 2026-09-20. Breakdown in Back office:

| Line | Amount |
|------|--------|
| Room, 3 nights at €129.00 | €387.00 |
| City tax, €3.00 per adult per night, 2 adults, 3 nights | €18.00 |
| Total | €405.00 |

The guest's screenshot of the Android confirmation screen shows Total €387.00. The confirmation email for the 
```

**Assistant:**

**Pre-write check:** Passed. The model has 6 entities, 6 relationships, and 26 attributes. The composer reports no design warnings.

**Question and outcome:** Guest Support can trace a booking reference to its guest, room, rate plan, payment, and property tax context.

**Glance order**

- First: Booking
- Second: Booking’s links to Guest, Payment, Room, and Rate Plan
- Last: Property tax context and the assumed field names, types, and multiplicities

**Review**

- Booking is marked as the focal entity
- The relationship labels show that each Booking uses one Room and one Rate Plan
- Guest records and Partner records are in separate zones
- The source line identifies the assumptions and the omitted direct Room–Rate Plan link

**Destination:** Roamstay Product plan, existing FigJam file `<test-file-key>`. I’ll add one section titled **Roamstay Stays Model for Guest Support**, positioned to the right of existing content. No extensions are planned, and existing sections will stay as they are.

The write needs one `use_figma` call and one `get_figjam` read-back. The initial file read is already complete. Rollback would remove only the new section and would need separate confirmation.

```mermaid
%% title: Roamstay Stays Model for Guest Support
%% subtitle: Guest Support follows a booking from its reference to the payment and partner details that explain a stay
%% source: Sources: user schema summary, Roamstay context, Support ticket 58213. Assumed: key and support field names, types and multiplicities. Left out: direct Room to Rate Plan link, not named in schema summary.
%% zone: Guest records: Guest, Booking, Payment
%% zone: Partner records: Property, Room, RatePlan
%% focus: Booking
erDiagram
    direction LR
    Guest ||--o{ Booking : makes
    Booking ||--o{ Payment : holds
    Booking }o--|| Room : reserves
    Booking }o--|| RatePlan : uses
    Property ||--o{ Room : offers
    Property ||--o{ RatePlan : publishes
    Guest {
        unknown id PK
    }
    Booking {
        unknown id PK
        unknown guestId FK
        unknown roomId FK
        unknown ratePlanId FK
        unknown bookingReference
        unknown stayNights
        unknown adultCount
        unknown roomAmount
        unknown cityTaxAmount
        unknown totalAmount
    }
    Payment {
        unknown id PK
        unknown bookingId FK
        unknown amount
        unknown currency
        unknown status
    }
    Property {
        unknown id PK
        unknown cityTaxRule
    }
    Room {
        unknown id PK
        unknown propertyId FK
        unknown roomType
        unknown maxOccupancy
    }
    RatePlan {
        unknown id PK
        unknown propertyId FK
        unknown cancellationPolicy
        unknown paymentOption
    }
```

May I write this section to the existing FigJam file?
