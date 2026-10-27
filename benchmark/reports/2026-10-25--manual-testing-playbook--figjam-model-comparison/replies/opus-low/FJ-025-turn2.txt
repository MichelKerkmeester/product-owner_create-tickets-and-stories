The model passed the check: two sequence diagrams on one board. The approved and declined paths are drawn separately, because a branch inside one sequence diagram renders flat.

**Question:** In what order do the guest app, booking API, payment provider and partner hub exchange messages during checkout payment?

**Outcome:** The payments team can read the checkout calls in order, with their status codes, for both an approved card and a declined card.

**What the reader should see:**
- **First:** "Authorise card", the call to the payment provider that decides the checkout.
- **Next:** the provider's answer. "Authorised" leads to confirming the hold and 201. "Declined" leads to releasing the hold and 402.
- **Last:** "Tell the partner hub", which happens on the approved path only.

**Plan:** <figma-plan-1> (`team::<plan-id>`).

**File:** a new FigJam file named "Roamstay checkout payment", created in that plan. It stays in drafts with no project. File `<test-file-key>` isn't touched.

**What gets written:** one board with two diagrams:
- **Card approved:** 4 participants and 7 messages.
- **Card declined:** 3 participants and 6 messages.

Each diagram gets a title, a key and a source line.

**Extensions:** none.

**Calls:** `create_new_file`, `create_session`, two `use_figma` calls and one `get_figjam` read-back. Your seat on <figma-plan-1> is Full on a Pro plan, so the six-call monthly limit doesn't apply.

**Rollback:** delete the new file.

Should I go ahead and write it?

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.