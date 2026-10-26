Lanes are in. Your reply didn't answer questions 1 and 2, so I'm proceeding on the recommended answers and marking them assumed below. Nothing is written yet, and this message asks about the reading only.

## Brief as it stands

- Reader: new CS and warehouse staff (assumed, settled by your answer to question 1)
- Question: who does what from a damage report to a released refund, and where does work change hands
- Outcome: the reader knows their own step and where it hands over (assumed)
- Scope: the stated path only. Claim rejection, a failed inspection and a limit on second photos are left out (assumed, because your sentence doesn't state them)
- Entry and exit: the customer's report is the start. The released refund is the goal
- Actors: Customer, CS and Warehouse as lanes, in that order (corrected: lanes in place of team colours)
- Source and class: your message, read as current behavior as you described it and not checked against a doc

## Outline

Each line is a node or an edge in drawing order, and each traces to a Brief row.

1. The board answers one question: who does what, and where does work change hands, from a damage report to a released refund
2. Customer lane: Report damage with a photo (start)
3. CS lane: Photo approved? (decision, which folds in "CS checks it")
4. Approved leads to Warehouse lane: Book a pickup
5. Second photo leads to CS lane: Ask for a second photo
6. That step leads to Customer lane: Send a second photo, which loops back to Photo approved?
7. Warehouse lane: Book a pickup, then Inspect the item, then Refund released (the goal)

That is 7 nodes, 7 connectors, 2 labelled decision exits and 3 lanes, inside the process budget of 12 nodes and 16 connectors. The remove test cut one node, a separate "CS checks the photo" step, because the decision already says CS checks and decides. Asking for the second photo and sending it stay as two nodes, one per owner, so the loop shows its handoff back to the customer.

## Two framings

- A, recommended: three lanes with the approved path on one straight line and the second-photo loop beside it. It shows the three handoffs, CS to Customer, Customer back to CS and CS to Warehouse. It costs width, which stays small at 7 nodes
- B: one plain decision flow with no lanes and the team named in each label, such as "CS: Ask for a second photo". It reads shorter, but it drops the lane-per-team grouping you asked for and hides who owns each step

## The look

- Colour marks kind only: start light blue, steps white, the decision light yellow and the goal light green. The key names each one
- First glance, assumed: the Photo approved? decision with the pink outline, because it is the only point where the claim loops or hands to the warehouse. The alternative is Refund released, if the money release is what the reader must see first
- Zones: none, because the lanes already group the steps
- Title: Fernhouse damaged-item refund
- Subtitle: Who does what from a damage report to a released refund, for new CS and warehouse staff
- Source line: Source: the request description. Left out: claim rejection, failed inspection and a limit on second photos, none of them stated
- Detail Balanced, audience Mixed and reading distance Laptop, all defaults

## Question

Is this reading right? Correct any line you disagree with, such as the reader, a lane, the first glance or a path to add. If it is right, say so and I'll send the gate, which names the file, what gets written and the rollback.