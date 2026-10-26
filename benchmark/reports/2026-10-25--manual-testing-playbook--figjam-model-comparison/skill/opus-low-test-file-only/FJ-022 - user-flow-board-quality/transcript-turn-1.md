# FJ-022 turn 1 transcript

**User:** $flow how a Fernhouse customer starts a return in the app, on a new board in our Fernhouse Product plan. From the app and the returns doc: the order list, the order detail with a Start a return button, a list of return reasons, a choice between a drop-off point and a courier pickup, and a confirmation with a QR code. Returns are open for 30 days after delivery, after that the app shows Contact support. A free pickup for orders over 100 euros is a proposal under review.

Write the board into the existing FigJam file with key <test-file-key> rather than a new file.

**Tool call:** `Bash` `{"command": "cd sk-create-figjam; grep -n -i -E \"existing file|file key|new file|plan|team|gate|question|conflict\" references/flow-mode.md | head -60"}`

**Tool result:** `Bash`

```text
"3:description: \"Product Owner flow-mode workflow: screenshots, Figma flows, product docs, schemas and plans turned into a checked Mermaid model of the right FigJam diagram type, written to a board and delivered as the board URL with a read-back line and the HVR self-scan line.\"\n18:Flow-mode guidance for FigJam diagrams. The workflow picks the diagram type the reader's question needs, turns screenshots, a Figma flow, a product doc, a schema or a plan into a Mermaid model of that type, checks it, writes it to a FigJam board and reads the board back before replying.\n22:**Scope:** Type choice, intake per input type, the model, the pre-write check, the quality pass, the write gate, the composed, generated and `fj` write routes, the hybrid extension, the read-back and the reply\n26:**Hands Off To:** the vendored `../mcp-figma/` packet for `figma-ds-cli` mechanics and its mutating gate, and `../sk-product-owner/references/interactive-mode.md` when the type, the sources, the target file or the order cannot be settled from what was supplied\n34:Provides the flow-mode workflow for drawing a diagram on a FigJam board. Flow Mode owns the route, the type choice, the intake, the model, the check, the gate, the read-back and the reply. The write composes a framed board from the checked model through one of three routes, and the board is the only deliverable.\n40:- A process or decision flow, with a lane per team when work changes hands\n41:- An architecture, a sequence of calls, a stat
```

**Assistant:**

I haven't drawn or written anything yet. Two things need settling first, so here they are as one question.

**1. Where the board goes.** You asked for a new board in the Fernhouse Product plan, and also to write into the existing file `<test-file-key>`. Flow Mode can write only to a new file it creates or to a board this work already wrote. It can't write into a file someone else made, because it can't safely roll that write back.
- **Recommended:** a new FigJam file in the Fernhouse Product plan, named "Fernhouse – Start a return". Any later diagrams for this work go into that same file.
- If `<test-file-key>` has to hold the board, tell me which file it is and confirm you accept that undoing the write means deleting the section I add. I'll ask you to confirm the trade-off again before anything is written.

**2. Sources and a few details.** Your message mentions the app and the returns doc, but neither was attached. Please send the screenshots and the doc. If you'd rather I draw from your summary alone, I'll mark the steps it doesn't cover as assumed. The defaults below apply unless you correct them:
- **Diagram type:** a user flow (a path through screens). Order list → order detail → **Start a return** → return reasons → choose drop-off point or courier pickup → confirmation with QR code.
- **Fork:** on the order detail screen, a check for "within 30 days of delivery". If yes, **Start a return**. If no, the screen shows **Contact support**, which ends the flow.
- **Free pickup over €100:** drawn as a note marked *Proposed – under review* on the courier pickup option, not as a step in the flow.
- **Reader and question:** product and design asking "how does a customer start a return today?" Highlight colour on the **Start a return** step. Sized for reading on a laptop.
- **Gaps:** how the 30 days are counted (calendar or business days), whether one order can have several reasons, and what happens on the QR screen after the customer sees it. These will be marked as unknown unless your sources answer them.

When you reply, I'll show the outline and model back to you. Nothing is written until you say yes at that step.
