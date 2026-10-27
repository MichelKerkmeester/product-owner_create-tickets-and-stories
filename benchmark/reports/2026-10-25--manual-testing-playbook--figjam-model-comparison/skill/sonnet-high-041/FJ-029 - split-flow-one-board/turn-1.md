I'm treating this as a user flow, because you're asking which screens a new person passes through and where they choose. Nothing has been written to the board yet. I have no onboarding doc in the workspace, so I'm working from your summary of it.

**What I have so far**
- Entry: the landing page
- Exit: the editor opening with a welcome tip
- Choices: email or Google, code right or wrong, free or team plan, add teammates' emails or skip, template or blank
- Error path: a wrong code shows an error with a resend
- Actors: a new person. The doc gives no system or timer steps
- Source: your summary of the onboarding doc, with no status given (current, approved or proposed)
- Target: file `<draft-file-key>`, drawn as a new section beside what it already holds. Nothing already there changes, and no new file is created. The key can't tell me which plan owns the file, so I'm taking Loomlist Product from you.

**Size.** The flow comes to about 12 screens and choices, plus a merge dot where the email and Google paths rejoin. A user flow holds 9 per board. "On a new board" names where it goes, not a single board, so I can split it.

**Still open, for the next round.** Does Google sign-up also ask for the email code, and is the doc current behavior or a proposal?

**Round one**

1. Reader and outcome
   - Reading: the file is in the product plan, so the readers are the product team. The question is which screens a new person passes through from landing to the first editor, and where they choose or hit an error.
   - Question: who reads the board, and what should they decide after reading it?
   - Recommended: product and design reviewers checking the signup flow against what is built.
   - Why: it keeps the labels in plain product words, with no API names.

2. What the board must not do
   - Reading: your message names one error path (the wrong code) and one skip (teammates' emails). It says nothing about expired codes, a failed Google sign-in or payment.
   - Question: should the board draw only what the doc states?
   - Recommended: yes, with no expired-code, Google-failure or payment screens.
   - Why: a screen the doc never mentions would read as current behavior.

3. Split
   - Reading: the flow is over the 9-node budget for one board.
   - Question: do you want one board or two?
   - Recommended: two boards in this file, read left to right. "1. Sign up" runs from the landing page to a hand-off called "Email verified". "2. Workspace setup" starts from that same hand-off and runs to the editor.
   - Why: it splits at a natural hand-off and drops no step. A single board would mean cutting the template pick.

Answer all three, or say "use the recommended answers" and I'll go on with them marked as assumed.