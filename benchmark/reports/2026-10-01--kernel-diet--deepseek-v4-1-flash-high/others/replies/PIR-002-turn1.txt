```markdown
# Wishlist across web and the apps - clarification

I detected two deliverables in one request, Bug and Story, and the two sources pull in different directions. Tell me which one to produce, answer the fields for that lane, and I will draft it.

**0. How should I work this?**
- Quick - lean pass with smart defaults, minimal back-and-forth
- Deeper - take more time, read more context and apply the full phase flow

**1. Deliverable and the unsettled decision**
- Maud's note asks Storefront to fix the wishlist and reads it as a bug
- Teun's reply says the app wishlist has always been stored on the device and the web wishlist on the account
- He says nothing changed in 4.8.0 or 4.8.2, and that changing the apps is a product call he has passed to Lotte
- Lotte has not answered, so the direction is unset
- Choose Bug, Story, or both with the order, and tell me whose decision settles the direction

**2. If Bug**
- The unexpected behavior, in the customer's words, and which of the four contact groups it covers
- Expected behavior: what the customer should see instead, and on which surface
- Platform and version, for example iOS 4.8.0, Android 4.8.2 or older
- Whether sign-in or a reinstall is involved, and whether the list is gone or only not shown
- Scope: one platform or all three, and one direction of the mismatch or both
- Evidence: contact IDs or app logs, plus screenshots where you have them
- Whether the loss reproduces, or is only ever reported

**3. If Story**
- Role and value: the Connextra line, who the user is and what one wishlist should get them
- Requirements: the concrete list the PRD must cover, in your words
- Candidates to keep or strike: one shared list across web, iOS and Android, web sign-in, device-only lists at first sign-in, and the 50-item limit
- Shared machinery: whether the requirements run through one mechanism, such as accounts-service as the single store the apps read and write
- Evidence: the exact identifiers and thresholds to carry into the spec blocks
- Open decisions: what happens to existing device-only lists, and whether a guest gets a wishlist at all

**4. Either way**
- Confirm the surfaces, Web, iOS, Android or all three, and that the feature code is WISH
- Give the discipline code if you have one in mind
- Name anything that should stay out of scope

**5. Assumptions to challenge**
- What am I likely to assume wrongly about the customers affected, or about the promise this ticket makes
```

Export-equivalent path: `export/001 - intake-wishlist-lost-on-phone-change-clarification.md`

HVR self-scan: 0 hard blockers. Fixed: no banned wording needed changing. Kept with reason: the hyphen-space separators in the two energy lines follow the interactive intake template word for word, and Web, iOS and Android stay capitalized as product identifiers.

Quality status: intake question held at the Interactive gate. One question, single topic, no self-answer, and it waits rather than drafting. Clarity, completeness, assumption challenge, perspective diversity and mechanism depth each read at 8 or above, since the two lanes trade off against each other and only you can settle which one the request wants.

I did not draft an artifact. The two commands conflict, and the one fact that would resolve them is missing: Teun's reply says the app wishlist was always device-local and that any change is a product call, while Maud's note reads the same behavior as broken. With Lotte's answer outstanding, writing either lane would assert a direction or an expected behavior nobody has confirmed.

Assumptions you can correct: I read `context/fernhouse-context.md` and `context/fernhouse-wishlist-feedback.md` as the full source set and treated Teun's note as describing shipped behavior rather than as a ruling on the ticket. I treated Lotte's unanswered call as genuinely open, so I could not pick the lane for you. I also assumed this is Fernhouse, not one of the other products in `context/`.

Answer the one response above and the artifact follows as a new Deliverable Block. Name Lotte's decision and the lane, and I can draft without another round.