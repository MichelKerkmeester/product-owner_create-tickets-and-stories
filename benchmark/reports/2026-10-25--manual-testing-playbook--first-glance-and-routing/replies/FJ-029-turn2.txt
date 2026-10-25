Your answers are in, so this is the playback of the reading before anything is modelled. Nothing is written.

Settled
- Reader: product and design teammates in the Loomlist Product plan, checking the onboarding path screen by screen
- Question: which screens does a new person pass through from the landing page to the editor, and where do they choose?
- Outcome: agree the steps and branches as one shared reference before design or tickets build on them
- Off limits: plan prices, screen copy, the Google consent screens and anything the doc does not state
- Entry and exit: the landing page, and the editor opening with a welcome tip
- Type and layout: a user flow, left to right, in three zones: Sign up, Choose a plan, Set up the workspace

Outline, in drawing order (9 nodes, 10 connectors)
1. Landing page (start)
2. Sign up with email or Google
3. Enter the email code
4. Code correct? Yes goes to 5. "No, error and resend" goes back to 3
5. Free or team plan? Free goes to 7. Team goes to 6
6. Invite teammates, or skip
7. Name the workspace
8. Pick a template or start blank
9. Editor opens with a welcome tip (the goal, and the first thing the board should show)

Connectors with no label (1 to 2, 2 to 3, 3 to 4, 6 to 7, 7 to 8, 8 to 9) follow the doc's written order. The doc states no trigger for them, so I add none.

Two framings
- Happy path with the branches beside it (recommended). The error and the skip ride on a connector label and a node label. That keeps it at 9 nodes on one board, which is what you asked for
- A state map with the error screen and the skip as their own nodes. That is 10 or more nodes, so it splits into two boards in the same file at the plan choice

Left out, named
- The error screen as its own node, carried on the "No" exit
- The skip as its own branch, carried in the invite label
- The off-limits items above

Assumed
- Actors: a person on every screen, and the system sends and checks the code and opens the editor. The doc settles this

Still open, two questions for this one reply:

1. Does the doc describe the live product?
   Reading: you called it the onboarding doc but did not say whether it describes today's product, an approved direction or a proposal.
   Recommended: treat it as current behavior.
   Why: a proposal drawn as current behavior would mislead the reader. Tell me if any step is a proposal and I'll mark it in its label.

2. Does the Google path also go through the email code?
   Reading: the doc lists "email or Google" and then "verify the email code" in one sequence, with no separate Google branch.
   Recommended: draw both methods into the code step, because that is the doc's order, and mark it assumed.
   Why: a Google account may skip the code. If it does, the board needs an extra decision and a node, and that pushes it past one board.

A yes, or a correction to either question, moves the work on to the model.