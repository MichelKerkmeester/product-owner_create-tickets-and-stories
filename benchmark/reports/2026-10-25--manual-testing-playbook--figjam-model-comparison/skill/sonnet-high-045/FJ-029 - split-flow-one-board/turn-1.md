**Playback so far.** Your message is the only source I have, because the onboarding doc isn't in the repository.

- Entry: the Loomlist landing page
- Exit: the editor opens with a welcome tip
- Choices: email or Google sign-up, free or team plan, and template or blank
- Branches: a wrong code shows an error with a resend, and a team plan asks for teammates' emails and lets you skip
- Target: a new section in the existing FigJam file `<draft-file-key>`, with nothing already on it changed
- Type: user flow, because the question is which screens a person passes through and where they choose

I haven't read or written the file yet. It takes one `get_figjam` read before the write gate.

**Question 1: reader, question and outcome**
- Reading: nothing in your message says who reads the board or what they decide next
- Recommended: a product team reviewing onboarding asks "which screens does a new person pass through from landing to editor, and where do they choose?" The outcome is that the reader can check each choice and the one error branch against the build
- Why: it matches the steps you listed and the user-flow type

**Question 2: what the board must not do**
- Reading: your list names no exclusions
- Recommended: no field-level detail, no returning-user sign-in and no error state beyond the wrong code
- Why: the doc excerpt only describes the first-time path

**Question 3: one board or two**
- Reading: the flow needs about 11 nodes against a user-flow budget of 9. You said "a new board", which names a destination and not a single-board limit
- Recommended: two boards in the same file, `1. Sign up` and `2. Workspace setup`, joined at the hand-off "Email verified". Board 1 runs from the landing page to the verified code. Board 2 runs from the plan choice to the editor
- Why: a split keeps every step, and a single board would cut some of them

If you leave any of these unanswered, I'll proceed on the recommendation and mark it assumed. The next reply is the full playback, including the open points the doc leaves unclear. One is whether a Google sign-up skips the email code. No board is written until you say yes at the write gate.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.