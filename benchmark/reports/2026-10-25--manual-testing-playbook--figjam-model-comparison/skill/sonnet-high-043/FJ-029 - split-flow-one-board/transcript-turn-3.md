# FJ-029 turn 3 transcript

**User:** Use your recommended answers.

**Assistant:**

This is the full reading. Nothing is drawn or checked yet.

**The question and outcome.** The board answers "Which screens does a new person pass through from the landing page to the editor, and where do they choose?" Afterwards the product and design team can see every branch and agree what each screen needs. The type is a user flow, drawn as two boards in the same file, "1. Sign up" and "2. Workspace setup", which hand off on a shared node.

**What your message settled.** Every node, branch and exit below comes from the order you listed them in, which is the order the boards follow.

Board 1, "1. Sign up", with 6 nodes:
- Start: Open the landing page
- Choice: Sign up with email or Google?
- Screen: Enter the email code
- Choice: Code correct?
- Screen: Wrong code error with resend
- End: Continue to setup, the shared hand-off

Edges: landing to the choice. Email and Google each go to the code screen. The code screen goes to Code correct?. Yes goes to the hand-off. No goes to the error. The error returns to the code screen on Resend.

Board 2, "2. Workspace setup", with 6 nodes:
- Start: Continue to setup
- Choice: Free or team plan?
- Screen: Ask for teammates' emails
- Screen: Name the workspace
- Choice: Pick a template or start blank?
- End: Editor opens with a welcome tip

Edges: the hand-off to the plan choice. Free goes to naming the workspace. Team goes to the teammates screen. That screen goes to naming the workspace twice, once labelled "Add emails" and once labelled "Skip". Naming goes to the template choice. Template and Blank each go to the editor.

**Assumed, and what settles each**
- The reader, the question, the outcome and the scope are assumed because you accepted my recommendations without a source. A source or your correction settles them
- Google joins the code screen. The doc doesn't say whether Google skips it, so a doc line or the product owner settles it
- Resend returns to the code screen. The doc names no move out of the error, so the same two sources settle it
- The doc is treated as current behavior, so no label carries a status. A line saying it is a proposal settles it, and every node would then carry that status

**Left out**
- Plan pricing, account settings and anything the editor does after the welcome tip, by your scope answer
- A separate email entry form and any Google account screen, because the doc names neither
- What happens to the teammates' emails after they are entered, because the doc stops at the screen

**Two framings**
- **A, recommended:** two boards, each with its main route on one straight line and the error and skip branches beside it. It keeps every choice you named and stays under the 9-node budget on both boards
- **B:** one board cut to 9 nodes by folding the sign-up method and the template choice into the labels of the screens around them. It is one place to look, but it loses two of the choices you named and hides where a person decides

**The look, as proposed**
- **Accent:** the hand-off on board 1 and the editor on board 2, each as the goal. No end is a failure, because the wrong-code error is a screen with a way back
- **Detail and audience:** Balanced detail and a Mixed audience, with plain product wording and the doc's own terms
- **Distance:** Laptop, with the standard type scale and no label cut
- **Zones:** none. Each board has six nodes, so a tinted section adds a box without helping the eye
- **Titles:** "1. Sign up" and "2. Workspace setup", each with a one-sentence subtitle. The source line names the onboarding doc and the Left out items above

Does this reading hold, with framing A, this look and Laptop distance? Correct any row or say "yes".
