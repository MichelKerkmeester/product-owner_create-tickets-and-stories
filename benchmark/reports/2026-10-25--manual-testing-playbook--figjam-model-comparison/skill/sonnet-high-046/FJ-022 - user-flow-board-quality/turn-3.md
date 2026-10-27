Nothing is written yet. The check passed on the final model, the composer built the board code, and the target file is empty, so no section there shares the title.

**Gate**

* Question: which screens does a customer pass through to start a return, and where do they choose?
* Outcome: the product and design team can confirm the path and see where the 30 day window ends a return
* First glance: Within 30 days of delivery?, the decision where the window ends a return
* Second glance: the main row in path order, Order list, Order detail, Start a return, Return reasons, Drop-off or pickup? and Confirmation with QR code
* Last glance: Contact support, the exit after 30 days, drawn below the row

The sketch is the model below. The check printed `PASSED 1 diagram(s) in model.md`: 8 nodes, 8 connectors, longest path 7 steps, 0 crossing pairs.

```text
flowchart LR
    %% goal: confirmed
    %% title: Start a return
    %% subtitle: For the product and design team: how a Fernhouse customer starts a return in the app and where the 30 day window ends it
    %% source: Sources: the app screens and the returns doc, as described in the request. Left out: free pickup for orders over 100 euros, a proposal under review.
    %% zone: Find the order: orders, detail, window, support
    %% zone: Request the return: start, reason, method
    %% zone: Done: confirmed
    orders([Order list]) --> detail[Order detail]
    detail --> window{Within 30 days of delivery?}
    window -->|Yes| start[Start a return]
    window -->|No| support([Contact support])
    start --> reason[Return reasons]
    reason --> method{Drop-off or pickup?}
    method -->|Drop-off point| confirmed([Confirmation with QR code])
    method -->|Courier pickup| confirmed
    style window fill:#FFC2EC,stroke:#F849C1
```

* Eye first: the outlined yellow Within 30 days of delivery? diamond, and it is the node the board most needs read
* Reads second: the main row from Order list to the confirmation, which carries the reader past the window to the goal
* Could miss: Contact support below the row, which would hide that a return can stop at 30 days
* Remove next: Start a return, kept because it is the control the returns doc names

**What the write does**
* Plan: Fernhouse Product, as you stated. I can't verify the plan from here
* File: <draft-file-key>, an existing FigJam file, with the board added as a new section. The file holds nothing yet, so nothing existing changes
* Writes: one composed board of 8 nodes and 8 connectors in three zones, with a title, a key and a source line, at Laptop reading distance
* Extensions: none
* Calls: one `use_figma` and one `get_figjam` read-back. I already spent a session call and one read on the empty file. Figma caps a Starter plan or a View or Collab seat at six tool calls a month, and I can't see which applies to you
* Rollback: delete the one board section the write returns, only on a yes that names it

Left out: the free pickup for orders over 100 euros, a proposal under review. Also left out: any screen after the method choice, such as picking a drop-off point or booking a pickup, because the sources name only the choice.

Finding: I shortened the method decision from "Drop-off point or courier pickup?" to "Drop-off or pickup?". Under the full wording the board wrapped the last word alone, and the check shows the shorter label still leaves "pickup?" alone on its last line. The exits keep "Drop-off point" and "Courier pickup". "Return method?" would avoid the wrap but isn't a word from your sources, so I kept the shorter label.

Write this board to that file?