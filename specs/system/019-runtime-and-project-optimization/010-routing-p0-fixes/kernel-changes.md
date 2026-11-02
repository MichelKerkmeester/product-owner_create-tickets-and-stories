---
title: "Kernel routing prose changes"
description: "Records every kernel prose sentence changed while aligning the router contract and renumbering the Router Code section."
trigger_phrases:
  - "kernel router section"
  - "router code heading"
  - "kernel prose change"
---

# Kernel routing prose changes

The kernel remains at v1.2.2. These eight prose sentences changed to point at the renumbered Router Code section, the paired Flow Mode contract and the Story bundle owner.

- Before: `Exact rules: Section 11, Router Code (primary detection signal).`
  After: `Exact rules: Section 10, Router Code (primary detection signal).`
- Before: `Exact rules: Section 11, Router Code (phase detection order).`
  After: `Exact rules: Section 10, Router Code (phase detection order).`
- Before: `Exact rules: Section 11, Router Code (confidence thresholds).`
  After: `Exact rules: Section 10, Router Code (confidence thresholds).`
- Before: `Section 11, Router Code, is the authority for exact routing behaviour, and every `references/...` or `assets/...` stem it names maps to the matching uploaded Knowledge doc, and a missing doc degrades to a smaller resource set instead of a dead reference.`
  After: `Section 10, Router Code, is the authority for exact routing behaviour, and every `references/...` or `assets/...` stem it names maps to the matching uploaded Knowledge doc, and a missing doc degrades to a smaller resource set instead of a dead reference.`
- Before: `Section 4 names each route's signals and use and covers Quick and Interactive handling, while Section 11 holds the exact triggers.`
  After: `Section 4 names each route's signals and use and covers Quick and Interactive handling, while Section 10 holds the exact triggers.`

- Before: `A board URL this session wrote counts as supplied once its read-back matched the model, and it goes under `Flows` with the diagram's name as the link text. A board with a mismatched read-back, or with no read-back possible, is never linked.`
  After: `Paired FigJam outputs follow Templates - Flow Mode Section 8 for artifact link placement after a matching board read-back.`
- Before: `When the route carries `then: "FLOW"`, the artifact is delivered first in its own reply shape, except that this reply ends on the Flow Mode gate and carries no ClickUp offer. Flow Mode then runs with that artifact as its product-doc source, under its own check and its own yes. Once the board's read-back matches, the URL joins the artifact's `Flows` group, or `Related references` for a Doc, and the Project re-renders its Deliverable Block with the link. The ClickUp offer comes once the board link is written back and the artifact is re-saved, because the body link is the only route that carries the board into ClickUp`
  After: `A route carrying `then: "FLOW"` follows Templates - Flow Mode Section 8 for artifact-first delivery, the board gate, read-back, link placement and ClickUp offer.`

- Before: ``- New Story: `export/NNN - Story-[description].md`. A new Story asked for with its task breakdown is one folder, `export/NNN - Story-[description]/`, holding `NNN - Story-[description].md` and one `NNN.[n] - task-[description].md` per task, `n` counting from 1 in the Story's task order. The Story lists its tasks in a `#### **Tasks**` block inside Solution, each task follows Assets - Task Templates and names the Story in a `**Story**` block, and both link the sibling file. Render one Deliverable Block per file, Story first, each followed by its own `Export-equivalent path:` naming its file inside the folder, then one `HVR self-scan:` line for the set``
  After: ``- New Story: `export/NNN - Story-[description].md`. A new Story with its task breakdown follows Templates - Story Mode Section 7 for the bundle folder, task order, Story links and delivery``

The Router Code section heading changed from `## 11. ROUTER CODE` to `## 10. ROUTER CODE`. Its executable block was regenerated from `sk-product-owner/references/router-contract.md` with comments removed.

The paired-output sentence points to the Flow Mode owner, and the Story bundle export line points to the Story Mode owner. The Router Code executable block was regenerated from the synchronized contract.
