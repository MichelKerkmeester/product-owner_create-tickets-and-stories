Nothing is written yet. I stopped at the plan, because your two instructions point at different places.

**Reading:** `whoami` lists three plans on your account:
* <figma-plan-3> is a Starter plan with a View seat, and it's the only personal one
* <figma-plan-1> is a Pro plan with you as admin
* <figma-plan-2> is a Pro plan with you as member

None is named Roamstay Product. <figma-plan-1> and <figma-plan-2> are team plans, so a board there would break your "never in a team or organization plan" rule.

**Question:** Should the board go in the <figma-plan-3> plan, or did you mean a Roamstay Product plan that isn't on this account?

**Recommended:** <figma-plan-3>. It's the only plan that meets the never-rule, and I'm treating the never-rule as the stricter instruction. Figma shows it with an internal `team::` key, but it's the plan named for you.

**What I'd draw:** The model passed the pre-write check with 6 entities and 6 relationships.
* **Relationships:** Guest makes Booking, Booking holds Payment, Room is reserved by Booking, Rate Plan prices Booking, Property offers Room and Property publishes Rate Plan.
* **Columns:** keys only, which is 12 attributes. Each entity has an `id PK`, and each many-side entity has an `FK` for every relationship pointing at it. There is no `UK` and there are no other columns.
* **Assumed, correct me:**
  * Every relationship is one-to-zero-or-more.
  * All key types are `string`, because you gave me no schema.
  * Layout is one section with no zones.
* **Possible clash:** `context/roamstay-context.md` says one booking holds up to 8 rooms. That doesn't fit a single `roomId` on Booking, which is how you described it. I drew it as you described it. Tell me if you want a Booking-to-Room junction instead.

**Gate:**
* **Plan and file:** a new FigJam file named "Stays model" in <figma-plan-3>.
* **Write:** one composed board with a title, a key and a source line.
* **Calls:** `create_new_file`, `create_session`, one `use_figma` and one `get_figjam` read-back. `whoami` already spent one. A Starter plan with a View seat is capped at six tool calls a month, so this uses most of what's left.
* **Rollback:** delete the new file.

Write it in <figma-plan-3>?

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.