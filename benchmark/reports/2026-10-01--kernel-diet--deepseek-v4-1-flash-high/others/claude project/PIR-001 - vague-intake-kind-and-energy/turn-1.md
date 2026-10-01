```markdown
# Guest loyalty points on stays - what to put in the backlog

The context file covers the surfaces, personas, services and constraints, and it holds no loyalty requirements. I need one round of answers before I draft anything, because this could be a task, a PRD or a decision document.

**0. How should I work this?**
- Quick: lean pass with smart defaults and minimal back-and-forth
- Deeper: more time, more context and the full phase flow

**1. Deliverable type:**
- Task: one scoped change with its acceptance criteria
- Story or Epic: product requirements in the house format with numbered Given/When/Then criteria
- Doc: a proposal that compares the options for leadership before any backlog item exists
- Tell me which one, or tell me what leadership will do with the answer and I will pick

**2. What leadership is asking for:**
- Who asked it, and what would they call success?
- Is a deadline or an event driving the question?

**3. Scope, as far as it is decided:**
- Earning only, or earning and spending?
- Points on completed stays, on nights or on money paid?
- One property group, city or brand first, or the whole marketplace?
- Guest app only, or Partner Hub and Back office too?

**4. Sources and evidence:**
- What has leadership put in writing so far?
- Any business case, competitor scheme or budget for what a point is worth and who pays for it?

**5. Constraints in the context file I have to work around:**
- Prices are in five currencies with no conversion, so what is a point worth across them?
- City tax is part of the total, so do points accrue on it?
- Guests can cancel, get refunded or leave a booking in payment_pending, so what happens to points then?
- Email-only guests have no account, so whose balance is it?
- No feature code covers loyalty, so which squad takes this and what code does the work use?

**6. Assumptions to challenge:**
- I assume a points balance needs a guest account, so correct me if that is wrong
- I assume leadership wants this built, so correct me if they want options first
- What should I not assume about who pays for a point?
```

Export-equivalent path: export/001 - intake-loyalty-points-clarification.md

Route: no artifact command, no artifact framing and an explicit "not sure", so this sits in Interactive intake with no lane resolved and nothing drafted. The artifact takes the next number in its lane once you answer.

Quality status: intake question only. Artifact type, scope, user value and acceptance criteria are all unresolved, and the request also carries an unsettled decision about whether this should exist at all, so holding was the only safe move. The question is single-topic, consolidated and multi-line, it opens with the energy choice, and it does not answer itself.

HVR self-scan: 0 hard blockers. Fixed: no em dash, semicolon, Oxford comma or blocker term survived the pass. Kept with reason: payment_pending (literal booking state name, kept verbatim) and Given/When/Then (the house term for acceptance criteria).

Additions you can strike, all named so you can drop any that do not apply: I trimmed the deliverable menu to Task, Story or Epic, and Doc, since a bug report cannot be the deliverable for a capability that does not exist yet. The constraint questions in section 5 come from the context file, not from you. The three challenge bullets in section 6 are mine.

Next step: answer the six parts in one response. If you would rather I pick a shape from partial answers, say so and tell me how much depth you want.