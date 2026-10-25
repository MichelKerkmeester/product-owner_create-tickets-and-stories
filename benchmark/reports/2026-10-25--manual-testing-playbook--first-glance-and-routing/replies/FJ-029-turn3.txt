The check changed one thing from the reading you approved, so I'm flagging it before the question. The single board's longest path ran 9 steps and the limit is 8. I split it at the plan choice, and every approved node and label is kept. Both diagrams now pass the check and compose locally, and nothing is written yet.

Question: which screens does a new person pass through from the landing page to the editor, and where do they choose?
Outcome: a reader can agree the steps and branches as one shared reference before design or tickets build on them.
First glance: board 1 shows the code check and its "No, error and resend" loop. Board 2 shows the editor opening with a welcome tip.
Second glance: board 1 shows the email code entry that feeds the check. Board 2 shows the free or team plan choice.
Last glance: board 1 shows the landing page. Board 2 shows the skip inside the team invite step.

Target: the existing FigJam file <test-file-key>, with no new file. You named the Loomlist Product plan, and I have not verified that this file sits in it. Both boards land as new sections 400 pixels to the right of what is already there, so nothing existing is covered.

Writes:
- Board "1. Sign up": 5 nodes and 5 connectors, no zones, ending on "Continue to plan choice"
- Board "2. Workspace setup": 6 nodes and 6 connectors in two zones, Choose a plan and Set up the workspace, starting on "Continue to plan choice"
- Each board has a title, a subtitle, a key and a source line, at Laptop reading distance with balanced detail and a mixed audience

Left out, named: the error screen as its own node (carried on the "No" exit), the skip as its own branch (carried in the invite label), plan prices, screen copy and the Google consent screens.

Assumed: the Google path goes into the email code step, as the doc's order reads. I also read every screen as a person's action and the code check, code send and editor open as the system's.

Extensions: none.

Calls: up to 5, which are create_session, two use_figma (one per board) and two get_figjam read-backs. If the file's plan is a Starter plan or you hold a View or Collab seat, Figma caps tool calls at six a month, and this uses most of that allowance.

Rollback: delete the one board section each write returns, through use_figma. I would do that only on your separate yes, and the file itself stays.

Write both boards?