Your recommended answers are in and marked assumed, so this is the full reading before I model anything.

**Settled**
- Reader: product and design reviewers checking the signup flow against what is built (assumed)
- Question: which screens a new person passes through from the landing page to the first editor, and where they choose or hit an error
- Outcome: the reader can compare the flow with the build and see every choice and the one error
- Must not: no path the doc doesn't state, so no expired code, Google failure or payment screen (assumed)
- Scope: two boards in file `<draft-file-key>`, "1. Sign up" and "2. Workspace setup", handing off at "Email verified" (assumed)
- Settings: Balanced detail, Mixed audience, Laptop distance, no zones (assumed). Each board has 7 nodes, so zones would only add boxes

**Outline.** The first line is the sentence the boards answer: "Which screens does a new person pass through from the Loomlist landing page to the first editor, and where do they choose or hit an error?"

Board 1, "1. Sign up", left to right
- Nodes: Landing page, Sign up with? (Email or Google), a merge dot, Enter email code, Code correct?, Wrong code error with resend, Email verified
- Moves: Landing page to Sign up with?, then Email and Google both to the merge dot, then to Enter email code, then to Code correct?
- Yes goes to Email verified. No goes to the error, and Resend returns to Enter email code (assumed)

Board 2, "2. Workspace setup", left to right
- Nodes: Email verified, Free or team plan?, Ask for teammates' emails, Name the workspace, Template or blank?, Pick a template, Editor with welcome tip
- Moves: Email verified to Free or team plan?, then Team to Ask for teammates' emails and Free to Name the workspace
- Teammates' emails go to Name the workspace, then Template or blank?
- Template goes to Pick a template, then the editor. Blank goes straight to the editor (assumed)

**Two ways to draw the skip**
- Skip on the edge (recommended): the edge out of the emails screen reads "Emails added or skipped". It has 7 nodes. Both outcomes reach the same screen, so a separate diamond would be padding, and the skip stays visible on the edge. The cost is that skipping isn't a branch of its own.
- Skip as a choice: add an "Add emails or skip?" diamond. It has 8 nodes and skipping is a visible branch, but two exits end on the same screen.

**Look (proposed)**
- Accent: the Code correct? choice on board 1, because it is where the error leaves the main path, and the editor goal on board 2
- Titles: "1. Sign up" and "2. Workspace setup", each with a one-sentence subtitle
- Source line: "Sources: Loomlist onboarding doc summary. Left out: nothing."

**Two rows are still open**
1. Does Google sign-up also ask for the email code?
   - Recommended: yes, as your summary orders it, with both methods joining before the code.
   - Why: a Google skip would be a rule the doc doesn't state. This stays assumed until the doc owner confirms.
2. Is the doc current behavior or a proposal?
   - Recommended: current behavior.
   - Why: you described it as how signup works. If it is a proposal, each node would carry that status in its label.

Is this reading right, including the skip drawn on the edge, the Google path and the doc status?