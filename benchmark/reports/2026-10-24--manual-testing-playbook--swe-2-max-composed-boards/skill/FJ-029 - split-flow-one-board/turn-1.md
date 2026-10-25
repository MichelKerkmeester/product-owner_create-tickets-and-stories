Everything I need is loaded and the hosted Figma route is fully connected (`use_figma`, `get_figjam`, `create_session` all present). This is a **user flow**: the reader's question is which screens a new member passes through and where they choose or get sent back.

Brief playback before the questions:

- **Reader:** open, recommendation below
- **Question:** open, recommendation below
- **Outcome:** open, recommendation below
- **Scope:** the signup and first workspace setup, nothing after the editor opens
- **Entry:** the landing page
- **Exit:** the editor opens with a welcome tip, and that is done
- **Actors:** the new member at every step; Loomlist sends the code email automatically
- **Decisions and states:** email or Google sign-up, code right or wrong with error and resend on wrong, free or team plan with teammates' emails or skip on team, template or blank
- **Sources and class:** the onboarding doc as supplied in your request, current behavior

Three intake questions, each with my reading and recommendation:

**1. Reader and question**
Reading: the board goes on the Loomlist Product plan for teammates reviewing onboarding.
Question: who reads this and what must it answer?
Recommended: the Loomlist product team, answering "which screens does a new member pass through from the landing page to the editor, and where do they choose or get sent back?"
Why: that is the question a signup-and-setup user flow answers, and it sets what earns a node.

**2. The Google path**
Reading: the doc lists "sign up with email or Google" then "verify the email code" in one sequence, which reads as both paths reaching the code screen.
Question: does a Google sign-up also land on the email code screen, or skip it?
Recommended: both reach it, drawn as the doc's order states.
Why: the source states the order and nothing in it marks Google as exempt; if it skips, the Google exit joins the flow after the code decision instead.

**3. What the board must not do**
Reading: the request covers signup and first setup only.
Question: what should stay off this board?
Recommended: only the described path, so no billing or payment step, no invite-acceptance flow on the teammate side and nothing past the welcome tip.
Why: a board that refused nothing is the expensive case, and the doc's stated scope ends at the editor.

Skip any of these and my recommendation stands, marked assumed and named again in the playback before the write gate.