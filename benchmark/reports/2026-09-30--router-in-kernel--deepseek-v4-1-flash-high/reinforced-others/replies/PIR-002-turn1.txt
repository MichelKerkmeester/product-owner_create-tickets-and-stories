```markdown
# Fernhouse wishlist - bug or story clarification

Two artifact commands arrived together, `$bug` and `$story`, and both context files are in hand. Choose one primary deliverable and fill in the unresolved fields below in one response.

**0. How should I work this?**
- Quick - lean pass with smart defaults, minimal back-and-forth
- Deeper - read more of the context and apply the full phase flow

**1. Primary deliverable**
- Bug - defect report with observed behaviour, numbered reproduction steps, expected behaviour and the fixed four-item QA checklist
- Story - PRD in the house format for one feature area, numbered acceptance criteria, and Requirements only where the source supplies hard values
- Epic - the same house format at release level, if the work splits across child stories
- Task - if this is a known change on one surface rather than a defect report or a PRD

**2. The call that decides the artifact**

Whether the app wishlist keeping its items on the device is a defect or the intended design is still an open product call. What the sources establish:
- The app wishlist is saved on the device and the web wishlist in `accounts-service`, and the app one works without an account
- Nothing changed in `4.8.0` or `4.8.2`, and the Storefront reply says the app wishlist has always worked this way, so there is no previous working behaviour to cite
- CS asks for the wishlist to be the same everywhere and calls the item loss a bug, on 412 contacts and 23 complaint tags

Which is it: a report of behaviour that contradicts an expectation someone owns, or a PRD that changes how the wishlist behaves? For a bug report, name the expected behaviour that is violated and who owns that statement.

**3. Scope**
- Do all 412 contacts sit in one deliverable, or only the 171 new-phone and reinstall contacts?
- The app-to-web group (138) and the web-to-app group (64) are the two-list problem, and the 50-item limit (39) is separate. Which are in scope?
- Does the app wishlist become account-backed, keep device storage with a merge or recovery path, or stay undecided? An undecided direction becomes an `**Open:**` line naming who settles it
- Platforms: `iOS`, `Android`, `Web` or all three

**4. Requirements and success**
- Which requirements should the artifact carry, or is the direction still to be decided?
- What does success look like: no list lost after a reinstall, one list visible on both surfaces, or fewer wishlist contacts per month?
- Which team and discipline code owns handoff, since this touches app storage and `accounts-service`

**5. Evidence and references**
- Do the contact counts, the monthly split and the customer quotes travel into the artifact as evidence?
- Anything beyond the two context files, such as a helpdesk sample or a design frame?

**6. What should I not assume?**
- What am I likely to get wrong about the customer expectation, the two lists or the product call?
```

Export-equivalent path: `export/001 - intake-wishlist-bug-or-story-clarification.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

Quality status: Interactive Mode delivery. One consolidated question, no draft and no answer to my own question, which the conflicting-command rule requires. Completeness of the ask, source fidelity and voice all pass. Six-dimension gate read at the depth the clarification shape calls for.

Why this came out as a question rather than an artifact: `$bug` and `$story` are two conflicting artifact commands, so routing cannot resolve, and the artifact type, the scope and the expected behaviour are all genuinely open. The sources also conflict on the central point, since CS reports item loss as a defect while Storefront describes device storage as the original build and confirms no change in `4.8.0` or `4.8.2`.

Assumptions you can correct:
- The two context files are the whole evidence set
- The CS note and the Storefront reply both describe current behaviour rather than recording a decision
- The 412 contacts are one problem to scope into a single deliverable, not a bug report plus a separate Story
- The fix direction is Lotte's to set, so it can travel as an `**Open:**` line instead of a decided requirement

Answer the six fields in one reply and I will draft the artifact, which takes the next number in whichever lane the answer selects.