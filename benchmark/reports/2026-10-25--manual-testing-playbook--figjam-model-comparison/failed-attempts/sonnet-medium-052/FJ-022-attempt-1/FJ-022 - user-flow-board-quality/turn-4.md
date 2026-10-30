Question: which screens does a Fernhouse customer pass through to start a return, and where do they choose?
Outcome: the product team can follow a return from the order list to a confirmed return and see where the 30 day window ends it.
First glance: Within 30 days after delivery?, the outlined decision where a return can end early.
Second glance: Order list, the light blue entry, then Order detail, Pick a reason, Contact support (the exit below the row), Drop-off or courier pickup?, Choose a drop-off point, Book a courier pickup (the second way to the goal, below the row) and Return confirmed, the goal. This is the order the check's Glance line prints.
Last glance: the key and the source line, since the goal comes last.

Sketch: the checked model in full, with the check's output as it printed.

```mermaid
flowchart LR
    %% goal: confirmed
    %% title: Start a return
    %% subtitle: How a Fernhouse customer starts a return in the app, from the order list to a confirmed return
    %% source: Sources: the Fernhouse app and the returns doc. Left out: a free pickup over 100 euros, a proposal under review.
    %% level: balanced
    %% zone: Find the order: orders, detail
    %% zone: Request the return: window, support, reason, method, dropoff, pickup
    %% zone: Done: confirmed
    %% about: Find the order | Starts: the order list | Ends: the Start a return button
    %% about: Request the return | Starts: the 30-day check | Ends: drop-off point or courier pickup chosen | Good to know: after 30 days, Contact support
    %% about: Done | Shows a QR code, also sent by email | Scan it at the drop-off point or hand it to the courier
    %% focus: window because returns can end early here
    %% detail: detail | Each item with price and delivery date | Start a return button under the items
    %% detail: reason | Damaged | Wrong size | Not as shown | Changed my mind
    %% detail: dropoff | Map of the 5 nearest points
    %% detail: pickup | A date in the next 3 working days
    orders([Order list]) --> detail[Order detail]
    detail --> window{Within 30 days after delivery?}
    window -->|No| support([Contact support])
    window -->|Yes| reason[Pick a reason]
    reason --> method{Drop-off or courier pickup?}
    method -->|Drop-off| dropoff[Choose a drop-off point]
    method -->|Pickup| pickup[Book a courier pickup]
    dropoff --> confirmed([Return confirmed])
    pickup --> confirmed
    style window fill:#FFC2EC,stroke:#F849C1
```

```text
  diagram 1, user flow: ok, 9 nodes and 9 connectors, widest rank 2 steps, longest path 7 steps, 1.0 connectors per step, labels average 19 characters, 0 crossing pairs
Glance: Within 30 days after delivery? (accent) > Order list > Order detail > Pick a reason > Contact support > Drop-off or courier pickup? > Choose a drop-off point > Book a courier pickup > Return confirmed (goal)
PASSED 1 diagram(s) in model.md
```

Eye first: Within 30 days after delivery?, the one outlined node, and it is the node the board most needs read.
Reads second: the main row from Order list to Return confirmed, which carries the reader past the window to the goal.
Could miss: Book a courier pickup, which sits below the row. Missing it hides the second way a return is made.
Remove next: Order detail, kept because it holds the Start a return button, the step that opens the flow.

Two changes from the playback's outline:
- A goal end cannot carry a body, so the QR code and the email sit in the Done zone's notes and not under Return confirmed.
- The model has no Label or Row warnings.

Plan: Fernhouse Product, as you stated. I did not verify it, because `whoami` only lists the plans your account holds.
File: the existing FigJam file `<test-file-key>`. I read it once and its page is empty, so no section shares the title "Start a return".
Writes: one composed board in a new section, with 9 nodes and 9 connectors in three zones, a title, a key and a source line, at the Laptop distance. No new file is created and nothing already in the file changes.
Left out: a free pickup over 100 euros, a proposal under review. Nothing after the confirmation is drawn.
Extensions: none.
Calls: one `use_figma` and one `get_figjam` read-back. The read of the file before the write is already spent, and I did not need to re-read it afterwards because it was empty.
Rollback: delete the one board section the write returns, through `use_figma`, and only on its own yes.

Write it?