I'll write the Partner Hub self-onboarding epic from Freya's brief of 2026-09-22 and the Roamstay context. The brief covers the problem, the partners in and out of scope, the six stages, the success measures and the risks. Before I draft, please answer the open decisions below in one reply.

**1. First release cut:**
- Payouts wait for identity checks, and every listing goes through the Go-live review queue. So as the brief describes it, a partner needs all six stages to go live. Where does the first release cut fall?
  - All six stages for every property type in scope
  - A smaller first group of partners: fewer countries, currencies or property types (say which)
  - One or more stages stay with an Ops agent in the first release (say which)
- Anything outside the cut goes under `Added Later` in Scope. Which capabilities belong there?
- In stage 1, the business registration number is checked against the country's business register. Which countries does the first release cover? The brief doesn't name any.

**2. Child stories:**
- Should there be one child story per stage (six in total), or should any stages be split or merged?
- Ops Tools builds stage 6 in Back office. Stage 5 hands payouts over to Payments. Should those stories sit in this epic, or be listed as dependencies on other squads' work?
- Should the success measures (time per stage, drop-off per stage, send-back share and reasons, guest complaints in the first 90 days) get their own Data story, or stay as release-level outcomes only?

**3. Goal status:**
- Are the 3-business-day median to go-live and the 1,500 self-onboarded properties by 2027-06-30 agreed targets? Or are they Freya's proposed targets until planning closes?

**4. Delivery section:**
- The brief asks for the squads to size the work before planning closes. Should the epic end with a Delivery section (Estimation, Rabbit holes, No-gos), with `TBD...` for anything not yet known?
- If yes, should the three exclusions (more than 40 rooms, chains, properties on a channel manager) and the review queue sizing with Ops Tools go into it?

**5. Title and references:**
- Is `Epic - Partner Hub - Self-onboarding` right, or should the title lead with the `Partner` persona?
- Do you have links to the brief, designs or existing tickets for References? If not, I leave that section out.

**6. What I might get wrong:**
- Only an Owner can change payout details in Partner Hub. Does the Owner have to complete stage 5, or can a Manager start it and an Owner finish it?
- Anything else I shouldn't assume about the partners, the review queue or what counts as go-live?
