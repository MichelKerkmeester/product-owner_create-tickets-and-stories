Paste the engineering notes, and in the same reply confirm the fields below so the draft can make definitive claims:

- **Status:** Are the notes current production behavior, a draft, or a mix? If they mix statuses (for example existing behavior alongside planned changes), point out which parts are which
- **Conflicts:** Do any of the notes contradict each other about how the retry pipeline behaves? If so, which one governs
- **Scope:** Anything that should stay out, such as other notification stages, warning-fatigue logic or analytics
- **Depth:** Support-team level should explain triggers, retry timings and what support can tell a merchant. Say if you need deeper engineering detail (queue names, IDs, failure codes) kept in

Once the notes land, the document will be a behavior reference: what triggers a retry, how the retry sequence behaves, where it stops, and what boundaries support should not promise past
