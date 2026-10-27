I accepted the round-two recommendations, so the three rows stay assumed. This is the full playback. It covers the reading only, and nothing is written to FigJam.

**What the board answers**
- Question: which screens does a new person pass through from the landing page to the first editor view, and where do they choose? (assumed)
- Outcome: the product team can confirm each screen and choice matches the onboarding doc (assumed)
- Type: user flow

**What each source settled**
- Your message (captured): entry, exit, the five choices, the error with a resend on a wrong code, and the existing file as the destination
- Your accepted answers (assumed): reader, question, outcome, and what the board leaves out
- Actors (assumed): a person acts on every move. Two steps are automatic system steps: the wrong-code error and the editor opening with its tip. The code email is not a node, because the "Enter email code" screen implies it
- Google (assumed): one "Sign up with email or Google" screen. Both methods lead to the code screen
- Resend (assumed): it returns to the code screen
- Doc status (assumed): current behavior. The source line will call the doc your summary of it
- Rows still open: none unasked

**The outline**

The first line is the sentence the board answers: "Which screens does a new person pass through from the landing page to the first editor view, and where do they choose?"

The split is two boards in the same file, read left to right, with "1. Sign up" first. The first board ends on "Email verified". The second starts on the same label.

Board 1, "1. Sign up" (6 nodes, 6 connectors, 2 labelled exits)

| Item | Detail | Brief row |
|---|---|---|
| Node | Landing page, start | Entry |
| Node | Sign up with email or Google, screen | Decisions |
| Node | Enter email code, screen | Decisions |
| Node | Code correct?, decision | Decisions |
| Node | Error with resend, screen, automatic | Decisions |
| Node | Email verified, end and hand-off, the goal | Exit |
| Edge | Landing page to Sign up | Entry |
| Edge | Sign up to Enter email code | Decisions |
| Edge | Enter email code to Code correct? | Decisions |
| Edge | Code correct? to Email verified, "Yes" | Decisions |
| Edge | Code correct? to Error with resend, "No" | Decisions |
| Edge | Error with resend to Enter email code, "Resend" | Decisions |

Board 2, "2. Setup" (8 nodes, 10 connectors, 6 labelled exits)

| Item | Detail | Brief row |
|---|---|---|
| Node | Email verified, start | Entry |
| Node | Free or team plan?, decision | Decisions |
| Node | Add teammates' emails?, decision | Decisions |
| Node | Enter teammates' emails, screen | Decisions |
| Node | Name the workspace, screen | Decisions |
| Node | Template or blank?, decision | Decisions |
| Node | Choose a template, screen | Decisions |
| Node | Editor with welcome tip, end, the goal, automatic | Exit |
| Edge | Email verified to Free or team plan? | Entry |
| Edge | Free or team plan? to Name the workspace, "Free" | Decisions |
| Edge | Free or team plan? to Add teammates' emails?, "Team" | Decisions |
| Edge | Add teammates' emails? to Enter teammates' emails, "Add emails" | Decisions |
| Edge | Add teammates' emails? to Name the workspace, "Skip" | Decisions |
| Edge | Enter teammates' emails to Name the workspace | Decisions |
| Edge | Name the workspace to Template or blank? | Decisions |
| Edge | Template or blank? to Choose a template, "Template" | Decisions |
| Edge | Template or blank? to Editor with welcome tip, "Blank" | Decisions |
| Edge | Choose a template to Editor with welcome tip | Decisions |

I ran the remove test on this text and cut nothing. A reader would miss the error screen, the email step and the template step, and you named all three.

**Two framings**
- Happy path with the branches beside it (recommended): the route from the landing page to the editor sits on one straight line, with the wrong-code error and the skip beside it. It shows the main route at a glance, and the cost is that branches get less weight.
- State map of every exit: each choice is a hub with all its exits shown at equal weight. It shows every exit evenly, but it loses the main route and adds nodes, which pushes board 2 toward its budget.

**The look (all proposed, all assumed until you correct them)**
- Colour: the goal on each board (Email verified, then the editor). No failure end, because the wrong code loops back and is not an end. No step in focus
- Detail and audience: Balanced detail, Mixed audience and Laptop reading distance
- Zones: none. Six and eight nodes read without them
- Board 1 text: title "1. Sign up", subtitle "How a new person signs up and verifies their email, from the landing page to a verified account"
- Board 2 text: title "2. Setup", subtitle "How a verified person picks a plan, names a workspace and opens the editor"
- Source line: "Source: the Loomlist onboarding doc, in the requester's summary. Left out: billing, error states beyond a wrong code."
- Four critique questions, answered against the checked sketch: where does the eye go first, and is that the node the board most needs read? Does any node repeat another? Do the exits read the same way throughout? Can a reader say what happens after a wrong code without asking?

If you send the onboarding doc itself, I'll read it and move the assumed rows to captured. It would also settle the Google question properly.

Does this reading hold, or which line changes?