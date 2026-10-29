---
title: "sk-product-owner Router"
description: "Sibling router for sk-product-owner: the router mechanics, then the artifact command table and the resource loading levels a reader parses first."
trigger_phrases:
  - "sk-product-owner router"
  - "sk-product-owner routing"
importance_tier: normal
contextType: general
version: 1.0.0.0
router_state: active
skill_pointer: SKILL.md
---

# sk-product-owner Router

The machine router for [`SKILL.md`](./SKILL.md). `SKILL.md` keeps the short routing prose and the
link that points here; this file holds the routing detail and the machine-readable declaration a
reader parses to decide what loads.

---

## 1. OVERVIEW

A request for a Task, a Bug, a Doc, a Story or PRD, an Epic or a clarification reaches sk-product-owner once the hub picks this packet, and this router binds it to one artifact mode by its command or its framing, or to Interactive Mode when two artifacts compete or none is named. A single Flow route hands off to `sk-create-figjam`, and an artifact that also asks for a FigJam board loads the artifact first and Flow Mode second.

The router answers one question: given a request, which packet-local resources load, in what order, and what happens when nothing matches. The hub [`../ROUTER.md`](../ROUTER.md) maps the packet's intents to leaves, and this file routes inside the packet.

---

## 2. INTENT MODEL

### Router Mechanics

[`references/routing.md`](references/routing.md) holds the routing steps, the confidence thresholds, the semantic topic table and the Story shape rules. [`references/router-contract.md`](references/router-contract.md) runs this router as Python, the algorithm `../benchmark/router/differential.py` holds `../benchmark/router/route_contract.py` equal to, and it is ON_DEMAND. Its `discover_markdown_resources` builds the inventory from `references/` and `assets/`, its `_guard_in_skill` refuses any path outside this packet and any file that is not markdown, and its fallback branch returns `UNKNOWN_FALLBACK_CHECKLIST` with the one clarifying question. The code stays in that file alone, because the kernel copies it and `../benchmark/router/differential.py` fails any second copy.

`references/routing.md` is detail-only and is not a runtime lane. This router and the router contract carry the resources and executable rules used on each route. Read `routing.md` for routing maintenance or when the thresholds, topic table or Story shape rules need explanation.

---

## 3. MACHINE ROUTER

The machine-readable projection of the intent model above, moved verbatim from `SKILL.md`: the artifact command table with the single-route handoff rule and the resource loading levels. This section is the last in the file.

### Primary Detection Signal

Detect the artifact command or framing and bind the correct mode before loading references.

```text
$task | $t                    -> Task Mode
$task --subtask               -> Task Mode (child-task scope)
$bug | $b                     -> Bug Mode
$doc | $d                     -> Doc Mode -> source-authority and conflict gate before draft
$story | $s | $prd | $p       -> Story Mode (Story shape)
$epic | $e                    -> Story Mode (Epic shape)
$flow | $figjam               -> Flow Mode -> see the single-route handoff rule below
$quick | $q                   -> energy override only, never an intent
2+ artifact commands          -> Interactive Mode (one consolidated question)
no command, framing hit       -> route by artifact framing ("write a task/bug/prd/story/doc ...", "make a FigJam flow ...")
artifact + FigJam output verb -> the artifact first, then Flow Mode (route.then = FLOW, flow-mode.md Section 8)
artifact framing about FigJam -> that artifact, FigJam is its subject ("add a task to update the figjam board")
board notes or edit request   -> Flow Mode ("add notes to the figjam board", a figma.com/board link)
no command, no framing        -> score semantic topics, route by confidence threshold
confidence < LOW (0.40)       -> follow the Quick fallback in `references/routing.md` Section 2
```

A single Flow route hands off to `sk-create-figjam`. When Flow appears with another artifact command, the command-conflict rule above keeps the request in Interactive Mode.

### Resource Loading Levels

Resources are discovered recursively by `discover_markdown_resources` from `references/` (the mode workflows, and byte copies of the four shared cards whose originals live in the outer repository's `z — Knowledge/`) and `assets/` (templates and worked examples).

| Level | Resources |
| --- | --- |
| ALWAYS | The router's ALWAYS lane loads `references/hvr-core.md` and `references/conciseness.md`. The hub `../SKILL.md` and `../ROUTER.md` and this file are already in context when this packet is chosen, and Section 3 of `assets/interactive-response-templates.md` is read before the first reply |
| CONDITIONAL | One routed pair, never more, then the Flow lane when the route carries `then: "FLOW"`. Task loads `references/task-mode.md` with `assets/task-templates.md`. Bug loads `references/bug-mode.md` with `assets/bug-report-template.md`. Doc loads `references/doc-mode.md` with `assets/doc-templates.md`. Story loads `references/story-mode.md` with the one scaffold its shape resolved: `assets/story-template.md` or `assets/epic-template.md`, never both. A single Flow route follows the Section 2 handoff to [`../sk-create-figjam/SKILL.md`](../sk-create-figjam/SKILL.md), which loads its own pair beside the two ALWAYS cards. Interactive loads `references/interactive-mode.md` with `assets/interactive-response-templates.md` |
| ON_DEMAND | `references/human-voice-rules.md` for a borderline voice call or a scored pass. `references/quality-scoring.md` for a borderline quality dimension. One reference or asset for a missing fact or template detail. At most one worked example from `assets/examples/<mode>/`, never a bulk folder read |
