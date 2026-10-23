Round one is closed. Still no Figma connector in this session, so this still ends in a checked model unless you attach Figma before the write.

**What the Brief holds so far**

- Reader: the product group reviewing the feature before build
- Question: what a customer does from a sold-out product page to the email, and where the flow branches
- Outcome: that this flow is right to build as drawn, and that in-app push sits outside it
- Entry: the product page of a sold-out item, "Notify me" tapped
- Branch: signed in or guest
- Signed in: saved to the account straight away, with no confirmation step
- Guest: types an email address, then saved, with no confirmation step
- Exit: the item is back in stock and one email goes out
- Push alerts in the app: a proposal, not agreed, so it cannot be drawn as current behavior
- Shape: one person, a few screens, one choice, so the reading is a user flow

**Round two: entry, exit, actors**

1. Surface
- Reading: the spec starts on the product page of a sold-out item, and Fernhouse runs that page on web, iOS and Android.
- Question: does the board cover all three surfaces, or web only?
- Recommended: all three in one flow, with no platform split.
- Why: A split needs the paths to differ, and the button and what follows it read the same on each.

2. Where the flow ends
- Reading: the spec ends at one email when the item comes back in stock.
- Question: does the alert close once that email goes out?
- Recommended: Yes, the alert is used up when the email sends, so the flow ends there.
- Why: One email per alert means the save cannot outlive the send, or a second restock would send a second email.

3. Who fires the email
- Reading: stock syncs from the warehouse system into catalog-service, and every email leaves through the email delivery provider.
- Question: what triggers the email when stock returns?
- Recommended: the stock sync into catalog-service fires the saved alerts, and the email delivery provider sends the one email.
- Why: Stock is only known from that sync, and mail only leaves through that provider. Labels stay plain for a mixed audience.

Answer these and round three closes the Brief: the case where the item never restocks, where the push proposal goes, and the class each source holds. The whole Brief then comes back as one playback before I draw anything.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: "Notify me", the product's own button label.