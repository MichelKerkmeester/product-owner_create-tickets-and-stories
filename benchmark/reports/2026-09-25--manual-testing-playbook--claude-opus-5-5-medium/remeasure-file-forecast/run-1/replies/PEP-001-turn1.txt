```markdown
I'll draft the Partner Hub self-onboarding Epic from Freya's brief (2026-09-22) and the Roamstay company context. The brief already covers the problem, the goal, the six stages, who's in and out, the success measures and the risks. Before drafting, I need the decisions below in one response:

**1. First release cut:**
The brief says a fast go-live matters more than covering every property type, and the cut isn't agreed yet. A partner can't go live without passing all six stages: payouts wait for the identity checks, and every listing goes through the Go-live review queue. So a cut can narrow who enters or how much a stage covers. It can't drop a stage. How should the Epic handle this?
- Put all six stages in `## Scope` and keep the release cut out of the Epic for now
- Put all six stages in Scope and record the cut as an open question under Rabbit holes, so the squads size against it before planning closes
- Name the cut now (for example fewer launch countries, fewer property types or a lower room limit than 40), and I'll put the rest under `#### Added Later`

**2. Child stories:**
- One child story per stage, six in all, named as plain text because none exist yet? Or a different split, such as stage 6 as two stories: the partner's view of a sent-back listing in Partner Hub, and the Back office queue for Ops Tools?
- Save and come back at any point: a story of its own, or part of each stage?
- The four success measures need tracking events from the Data squad. Should a tracking story sit in Scope, or is that handled elsewhere? This would be my addition, because the brief doesn't name it

**3. Title:**
The work spans Partner Hub and Back office and three squads. Should it be `Epic - Partner - Self-onboarding` (persona) or `Epic - Partner Hub - Self-onboarding` (surface)?

**4. Release-level acceptance criteria:**
- Are the median of 3 business days and the 1,500 properties by 2027-06-30 acceptance criteria, or Goal-only targets with criteria written as release behavior (a partner goes live with no Ops agent setup, no payout before both checks pass, review within 1 business day)?
- Should the 1 business day review stand as a criterion before Ops Tools has sized the queue?

**5. Delivery section:**
Freya wants something the squads can size before planning closes. That calls for `## Delivery` with Estimation, Rabbit holes and No-gos set to `TBD...` where unknown, plus External dependencies for the business register checks and the identity verification provider. Keep it or leave it out?

**6. Scope edges the brief leaves open:**
- At launch, is it every country Roamstay covers in Europe and the US, all seven Partner Hub locales and all five currencies, or a subset?
- How are partners with a channel manager or more than 40 rooms sent to assisted onboarding: a question at sign-up, or outside this Epic?
- Only an Owner can change payout details, so is the Partner Hub user created at sign-up always the Owner?

**7. References:**
Do you have links to include, such as the brief in ClickUp, Figma files or related tickets? Without links I'll leave out References.
```

Export-equivalent path: `export/001 - Epic-partner-hub-self-onboarding-clarification.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: `TBD...` (the fixed Delivery placeholder, quoted as a named option).

I haven't drafted anything yet. This block holds only my questions, because `$epic` needs your answers first. Some points are still open: the first release cut, how to split the child stories, the title, and whether the targets are acceptance criteria or goals. Freya's brief settles the rest.

**Additions for you to confirm:** Two parts of the questions come from me, not the brief:
- **Tracking story:** a possible child story for the tracking events the success measures need
- **Launch coverage:** which countries, locales and currencies are in the first release

The Epic comes next once you answer. No ClickUp connector is available in this session, so I can't offer to push it to ClickUp.