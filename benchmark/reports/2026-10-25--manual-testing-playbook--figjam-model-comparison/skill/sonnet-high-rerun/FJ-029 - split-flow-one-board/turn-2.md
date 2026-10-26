Here is the reading before anything is modelled. Your recommended answers are accepted, so the rows below marked assumed stay assumed until you correct them.

The board answers one question: which screens does a new person pass through, and where do they choose, from the landing page to the first editor session? After reading it, the product team can check each branch (wrong code, plan, skip, blank) against what is built.

The rows:
- Reader: the product team. Assumed, settled by you
- Question and outcome: as above. Assumed, settled by you
- Scope: landing page to the welcome tip. Settings, billing, anything after the tip and a separate Google path are out. Assumed
- Entry: the landing page. Captured
- Exit: the editor with the welcome tip. Captured
- Actors: the person makes every move except the code check and the editor opening, which the system does. Assumed
- Decisions: code right or wrong, free or team plan, invite or skip on the teammates step, template or blank. Captured
- Sources and class: the onboarding doc as summarised in your request, treated as current behavior. Assumed, settled by the doc itself
- Google: one sign-up screen followed by the code step. Assumed, settled by whoever owns sign-up
- Skip: an exit from the teammates step with no decision of its own. Assumed

The outline has nine nodes and ten connectors, in drawing order:
1. Landing page, the start
2. Sign up (email or Google), a screen
3. Enter email code, a screen
4. Code right?, a decision. Wrong code goes back to Enter email code, labelled "Wrong code: error with resend". Right code goes to the plan choice
5. Free or team plan?, a decision. Free goes to Name the workspace and Team goes to Invite teammates
6. Invite teammates, a screen. It goes to Name the workspace, labelled "Send invites or skip"
7. Name the workspace, a screen
8. Pick a template or blank, a screen
9. Editor with welcome tip, the end

Two framings:
- Main path with branches beside it. The wrong-code error is a connector label, not a screen. It fits one board at nine nodes. This is the one I recommend, because the reader's job is spotting the branches and a straight spine makes them easy to find.
- A state map with the error screen as its own node. That makes ten nodes, so it splits into "1. Sign up" and "2. Workspace setup". The error screen is visible, but the reader opens two boards.

The look, proposed:
- Colour marks one node: the editor with welcome tip, as the goal. No end is a failure.
- Detail is balanced and the audience is mixed, both read from the rows. Reading distance is a laptop, since you didn't name another.
- Two zones in flow order: "Create the account" (landing page to code check) and "Set up the workspace" (plan choice to editor).
- Title: "Loomlist signup and workspace setup". Subtitle: "How a new person goes from the landing page to the first editor session, with the code, plan, skip and blank choices".
- Source line: "Sources: the Loomlist onboarding doc, as summarised in the request. Folded: the wrong-code error, into a connector label. Left out: a separate Google path and anything after the welcome tip".

The gate will ask four things about the drawn sketch:
- Where does the eye go first, and is that the node the board most needs read?
- Can a reader find the wrong-code loop without being told?
- Does the team detour read as optional?
- Does any label need the product's own word?

Does this reading hold, or what should change?