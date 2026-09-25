I haven't drafted the behavior reference yet, because the two notes contradict each other and neither says which one is authoritative.

**Conflict**
* Note A: the payout pause holds for 24 hours, then releases automatically.
* Note B: the pause holds until the brand clears it manually.

These are two different release mechanisms. I won't merge them or pick one.

**One question, covering everything I need:**
1. **Authority:** Which note is correct, or is there a newer source that settles it? Who owns that call?
2. **Status of each note:** Is the correct behavior what the feature does today (current), an approved direction, or a proposal? Is the other note retired, out of date, or a different variant?
3. **Source set:** Are Notes A and B the only sources? If there's code, a spec, or a ticket, please share it.
4. **Shape:** Do you want a behavior reference for current behavior only, or a version that also records the conflict and an open question?
5. **Scope:** Should the reference cover only the pause and its release, or also triggers, who can pause, what the brand and creator see, and what happens to held payouts?

If both notes are true, say so and say when each applies. For example, they could describe different pause types, or a manual clear could override the 24-hour timer. I can then write both cases as current behavior.