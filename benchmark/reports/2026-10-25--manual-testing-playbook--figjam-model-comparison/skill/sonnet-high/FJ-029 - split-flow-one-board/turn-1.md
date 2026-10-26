Nothing is written yet. This is the playback of my reading, and it needs one answer before I model anything.

**What I read from your message**

* **Source:** your message is the only source I have. I couldn't find the onboarding doc in this repo or the Loomlist context files. I'm treating your description as the doc's content and as current behavior.
* **Type:** user flow. The question is which screens a new person passes through and where they choose.
* **Entry and exit:** the flow starts at the landing page and ends when the editor opens with a welcome tip. The welcome tip is the goal and the first glance.
* **Target:** you named the existing file `<draft-file-key>`, so I read that as the target. The board goes in as new sections beside what is already there, and nothing already on the file changes. That makes the Loomlist Product plan irrelevant for now, since no new file is needed. If the file turns out to be unwritable, the gate will say so before anything is created in the Barter plan.

**What I assumed, from the doc's order and nothing else**

* "Sign up with email or Google" is one screen with no branch, because the doc doesn't say whether Google skips the code.
* A wrong code shows an error with a resend, and that error returns to the code screen.
* "Teammates' emails, or skip" is one screen, because the skip and the submit both lead to naming the workspace.
* "Template or blank" is one screen leading to the editor.
* Free goes straight to naming the workspace.
* The labels use the doc's words, and the audience and detail level stay at mixed and balanced.

**Three questions**

1. **Reader, question and outcome.**
   * Reading: your message names none of them.
   * Recommended: the Loomlist product and design teams, asking "what does a new person pass through before the editor, and where can they choose or get stuck?" The outcome is that they can see which step to change.
   * Why: it is the one question this flow can answer.
2. **What must the board not do?**
   * Reading: the doc names only the wrong-code error.
   * Recommended: leave out expired codes, network failures, Google-specific steps, Team billing and what teammates see when invited.
   * Why: none of these appear in your description, and drawing them would add steps the doc never states.
3. **One board or two?**
   * Reading: the flow has 10 nodes and a user flow holds at most 9.
   * Recommended: two boards in the same file, "1. Sign up" (landing to verified email) and "2. Workspace setup" (plan to editor). Each has 6 nodes and they hand off on "Email verified".
   * Why: the alternative is dropping the wrong-code error to reach 9 nodes, which loses a branch you asked for.

Reply with corrections, or "use the recommendations" and I'll take all three as stated and move to the model.