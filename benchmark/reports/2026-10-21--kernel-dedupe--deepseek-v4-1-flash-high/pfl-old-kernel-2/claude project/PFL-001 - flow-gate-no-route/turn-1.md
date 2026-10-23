No Figma connector is present in this session, so I cannot create the board in the Fernhouse Product plan or read one back. Two routes from here: connect Figma and I write the board, or I run the intake and hand you a checked Mermaid model you paste into a new board yourself. Either way the Brief comes first, so here is round one.

**What the spec already settles**

- Entry: a customer on the product page of a sold-out item taps "Notify me"
- Signed in: the alert saves to their account straight away
- Guest: they type an email address, then the alert saves
- Branch: signed in or guest, the one choice the spec names
- Exit: the item is back in stock and the customer gets one email
- Push alerts in the app: a proposal, nobody has agreed it, so it cannot be drawn as current behavior
- Surface: not named in the spec, so round two asks it

**Round one: reader, question, outcome**

1. Reader
- Reading: Lotte owns the spec, and the board is asked for in the Fernhouse Product plan.
- Question: Who reads this board, and what do they bring to it?
- Recommended: The product group reviewing the feature before build, with the Storefront and Post-purchase leads in the room.
- Why: The spec fixes customer-facing behavior, so the people who build and review it are the readers.

2. Question
- Reading: The spec walks one person from a sold-out product page to a single email, branching once.
- Question: What is the one question the board must answer?
- Recommended: What does a customer do from a sold-out product page to the email, and where does the flow branch?
- Why: The sign-in branch is the only choice, and both paths end on the same email.

3. Outcome
- Reading: The spec stops at one email, and push is unagreed.
- Question: What should the reader be able to decide after reading the board?
- Recommended: That this flow is right to build as drawn, and that in-app push sits outside it for now.
- Why: A scope decision is what a review of an unbuilt feature needs.

Answer these and I test the type against your question, then ask round two (entry, exit, actors) and round three (decisions, sources and class). The whole Brief comes back as one playback before any model is drawn.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: "Notify me", the product's own button label.