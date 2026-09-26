# View-only share links, clarification before drafting

I'll write this as a new Story from Kofi's design notes of 2026-09-15, using the Loomlist context page for background. Before drafting, I need the decisions below answered in one reply:

**Story or Epic:** The notes cover four areas: the Share panel switch, the plan limits and the Team Admin workspace switch, the viewer page, and mobile links opening the app. Should this be one Story covering all four, or an Epic with one child story per area? If it is one Story, should the Team Admin switch that turns off every link in the workspace stay in it or move to a separate story?

**Status of the notes:** The context page still lists "Pages are shared by invite only. There is no public link to a page" as a current constraint. Has Lena approved the design in Kofi's notes as the scope to build, or should the Story present it as proposed until she signs off?

**Sub-page inheritance:** `Do sub-pages inherit the link?` is not decided. Design says yes, Caio says no, and Lena settles it after talking to the security reviewer, with no date set. Which option do you want?
- A: Scope the Story to a link on a single page, as the frames do, and mark the sub-page question as an `**Open:**` line on the requirement. That also adds a Delivery section to the Story, and what Duplicate copies stays open with it
- B: Leave sub-pages out of the Story entirely and track the question somewhere else

Also, is the security review a sign-off that blocks release (I would list it under External dependencies, date TBD), or is it only input to Lena's decision?

**Role and value:** Who is the main user of the Story: the member sharing the page (Dana, Theo or Mireille) or the person opening the link? What benefit should the Story promise? The notes give one piece of evidence: in research sessions, readers who hit a sign-in wall on a linked page stopped reading.

**Gaps in the notes:** The notes don't cover these. Should I include them as open constraints, or leave them out?
- Analytics events. The context page says new events go to the Data team's tracking plan before client work starts
- Copy for Copy link, Reset link, Try Loomlist, Duplicate and the sign-in prompt in de-DE, fr-FR, es-ES, ja-JP and pt-BR
- The design file link for the frames `Share / View-only link`, `Share / Link settings` and `Shared page / Viewer`. I will only add links you give me

**Delivery section:** Do you want estimation, rabbit holes and no-gos in the Story? Choosing option A above adds the section in any case.
