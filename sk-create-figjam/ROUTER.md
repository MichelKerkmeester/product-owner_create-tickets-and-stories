---
title: "sk-create-figjam Router"
description: "Sibling router for sk-create-figjam: the Flow Mode route, the diagram type detection, the loading levels and the resource discovery code a reader parses first."
trigger_phrases:
  - "sk-create-figjam router"
  - "sk-create-figjam routing"
importance_tier: normal
contextType: general
version: 1.0.0.0
router_state: active
skill_pointer: SKILL.md
---

# sk-create-figjam Router

The machine router for [`SKILL.md`](./SKILL.md). `SKILL.md` keeps the short routing prose and the
link that points here; this file holds the routing detail and the machine-readable declaration a
reader parses to decide what loads.

---

## 1. OVERVIEW

A `$flow` or `$figjam` command, FigJam output wording or a request to add notes to or change a FigJam board reaches sk-create-figjam once the hub picks this packet. The packet has one route, Flow Mode, and this router makes the one choice inside it: which of the seven diagram types answers the reader's question, and which type reference and template load beside the Flow pair.

The router answers one question: given a request, which packet-local resources load, in what order, and what happens when nothing matches. A request that is not a diagram returns to the Product Owner packet.

---

## 2. INTENT MODEL

- **Flow Mode**: `$flow`, `$figjam`, FigJam output wording and board notes or changes load `references/flow-mode.md` with `assets/flow-templates.md`, then the detected type's reference and template.
- **Type choice**: one matching type loads its pair, two fitting types ask which question the reader has, and no match asks the reader's question or names a kind the board cannot draw.
- **Hand back**: another artifact command or another artifact's framing returns the request to the Product Owner packet, whose Interactive Mode asks one question, and a request that is not a diagram takes the `UNKNOWN_FALLBACK` branch.

---

## 3. MACHINE ROUTER

The machine-readable projection of the intent model above, moved verbatim from `SKILL.md`: the detection table, the type detection table, the loading levels and the resource discovery code with `TYPE_SIGNALS`. This section is the last in the file.

### Primary Detection Signal

```text
$flow | $figjam               -> Flow Mode
FigJam output wording         -> Flow Mode ("make a FigJam flow ...", "a sequence diagram in FigJam")
board notes or a change       -> Flow Mode ("add notes to the FigJam board", "update the FigJam board", any request with a figma.com/board link)
$quick | $q                   -> Quick energy: every row filled from the sources and the defaults with each inferred row marked assumed, sent as the playback, then the gate as usual
another artifact command      -> hand back to the Product Owner packet, whose Interactive Mode asks one question
another artifact's framing    -> hand back to the Product Owner packet, FigJam is then that artifact's subject ("add a task to update the figjam board")
```

A board that already exists is revised here too. Notes go on top through `references/hybrid-workflow.md`, with the target ids from a `get_figjam` read, which works in a session that did not write the board. An update or a redraw reads the board with `get_figjam` first, opens with a playback of the rows it changes, is made in the model and composed again. The old board section is deleted only on its own yes to a question that names it, never on a bare yes, as `references/flow-mode.md` Sections 5 and 6 set out. A session that did not write the board reads it with `get_figjam` first and takes what the read shows as a source for the intake. Moving, resizing or restyling a composed node is not a route, as rule 4 under NEVER in Section 4 says.

### Type Detection

`TYPE_SIGNALS` in the code below maps the words a request uses to the type that answers them, and `detect_diagram_types` returns every type that matches, in the order the table holds them. `../benchmark/router/flow_types.json` pins two phrasings per type, and `../benchmark/router/differential.py` runs them against this block.

```text
one type matches              -> that type, confirmed against the reader's question
two types fit                 -> ask which question the reader has, as flow-mode.md Section 3 sets out
a named type the brief does not describe -> compare before intake and ask once, naming the mismatch and the recommended type
no type matches               -> ask the reader's question, or say the board cannot draw the kind and offer the nearest drawable type
runbook, timeline of work     -> confirm the type with the reader, because a runbook is a Doc to the Product Owner router and flow-mode.md Section 3 offers a timeline as a gantt
```

### Resource Loading Levels

| Level | Resources |
| --- | --- |
| ALWAYS | the hub `../SKILL.md` and `../ROUTER.md`, this file, `../sk-product-owner/references/hvr-core.md` and `../sk-product-owner/references/conciseness.md` |
| CONDITIONAL | `references/flow-mode.md` with `assets/flow-templates.md` on every Flow route. Then the type's `references/types/<type>.md` and, for every type but user flow, `assets/templates/<type>.md`. `references/quality-rubric.md` with `references/style-guide.md` before the gate, because the rubric checks the palette and the spacing bands against the style guide |
| ON_DEMAND | `references/hybrid-workflow.md` when the gate names an extension. `assets/figjam-design.md` when a request changes how every board looks or a `DESIGN` line needs explaining. `assets/examples/` for a worked example of the type. `../sk-product-owner/references/human-voice-rules.md` for a borderline voice call. `../mcp-figma/SKILL.md` for the `fj` route. `../sk-product-owner/references/interactive-mode.md` when the sources, the type, the target file or the order cannot be settled |

### Resource Discovery

Packet resources are discovered at call time, and `_guard_in_skill` keeps every packet load inside this folder. The two Human Voice cards and the Interactive Mode reference belong to `../sk-product-owner/`, so the hub `../ROUTER.md` names them for a Flow route beside this packet's pair, and this packet never copies them.

```python
import re
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent
RESOURCE_BASES = (SKILL_ROOT / "references", SKILL_ROOT / "assets")
FLOW_PAIR = ("references/flow-mode.md", "assets/flow-templates.md")
DIAGRAM_TYPES = ("user-flow", "process", "architecture", "sequence", "state", "er", "gantt")
TYPE_SIGNALS = {
    "user-flow": ("screen", "screenshot", "a person's path", "signup", "onboarding", "user flow"),
    "process": ("who does what", "handoff", "swimlane", "lane", "process"),
    "architecture": ("service", "component", "system", "infrastructure", "architecture"),
    "sequence": ("call", "message", "api order", "request and response", "sequence"),
    "state": ("status", "lifecycle", "transition", "state"),
    "er": ("table", "entity", "entities", "schema", "data model", "field", "er diagram"),
    "gantt": ("plan", "schedule", "phase", "roadmap", "gantt"),
}
QUALITY_RUBRIC = "references/quality-rubric.md"
STYLE_GUIDE = "references/style-guide.md"
HYBRID_WORKFLOW = "references/hybrid-workflow.md"
BOARD_DESIGN = "assets/figjam-design.md"
UNKNOWN_FALLBACK = {
    "load_level": "UNKNOWN_FALLBACK",
    "needs_disambiguation": True,
    "hand_back": "../sk-product-owner/SKILL.md",
    "resources": [],
}

def discover_markdown_resources():
    documents = []
    for base in RESOURCE_BASES:
        if base.exists():
            documents.extend(path for path in base.rglob("*.md") if path.is_file())
    return {path.relative_to(SKILL_ROOT).as_posix() for path in documents}

def _guard_in_skill(relative_path):
    resolved = (SKILL_ROOT / relative_path).resolve()
    resolved.relative_to(SKILL_ROOT)
    if resolved.suffix.lower() != ".md":
        raise ValueError("Only packet-local markdown resources are routable")
    return resolved.relative_to(SKILL_ROOT).as_posix()

def detect_diagram_types(request):
    text = request.lower()
    return [
        diagram_type for diagram_type, words in TYPE_SIGNALS.items()
        if any(re.search(rf"\b{re.escape(word)}(?:s|es)?\b", text) for word in words)
    ]

def type_resources(diagram_type):
    resources = [f"references/types/{diagram_type}.md"]
    if diagram_type != "user-flow":
        resources.append(f"assets/templates/{diagram_type}.md")
    return resources

def route_flow(is_flow_request, diagram_type=None, extension=False, restyle=False):
    if not is_flow_request:
        return UNKNOWN_FALLBACK
    inventory = discover_markdown_resources()
    loaded = []

    def load_if_present(relative_path):
        guarded = _guard_in_skill(relative_path)
        if guarded in inventory and guarded not in loaded:
            load(guarded)
            loaded.append(guarded)
            return True
        return False

    if not all(load_if_present(path) for path in FLOW_PAIR):
        return {**UNKNOWN_FALLBACK, "resources": loaded}
    if diagram_type not in DIAGRAM_TYPES:
        return {"resources": loaded, "needs_type": True}
    if not all(load_if_present(path) for path in type_resources(diagram_type)):
        return {**UNKNOWN_FALLBACK, "resources": loaded}
    load_if_present(QUALITY_RUBRIC)
    load_if_present(STYLE_GUIDE)
    if extension:
        load_if_present(HYBRID_WORKFLOW)
    if restyle:
        load_if_present(BOARD_DESIGN)
    return {"resources": loaded, "diagram_type": diagram_type}
```

A request that is not a diagram takes the `UNKNOWN_FALLBACK` branch and returns to [`../sk-product-owner/SKILL.md`](../sk-product-owner/SKILL.md) unread past this file. A Flow request with no settled type returns `needs_type`, and the type is asked for before any type file loads. The Product Owner router keeps the `$flow` and `$figjam` commands in its own contract, so a command conflict such as `$task $flow` still asks one question there.
