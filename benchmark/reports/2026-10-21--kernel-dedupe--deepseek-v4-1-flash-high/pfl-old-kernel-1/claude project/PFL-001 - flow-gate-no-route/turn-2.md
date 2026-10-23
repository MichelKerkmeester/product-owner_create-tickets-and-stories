Replay of what is settled:

Reader: the Storefront and Post-purchase teams, before build
Question: what happens between a customer tapping Notify me and the email arriving
Outcome: agree the screens and the one branch before tickets are cut
Scope: no services, no stock sync, no app push on the board
Sources: Lotte's spec, read against the Fernhouse company context

Round two, on entry, exit and actors.

Reading: the spec starts on the product page of a sold-out item, and Fernhouse sells on web, iOS and Android, each with a product page.
Question: does the board show one entry for all three surfaces, or a split by surface?
Recommended: one entry node, the product page of a sold-out item.
Why: the notify-me path is the same on all three surfaces, and a split adds a decision the spec never makes.

Reading: the spec ends with one email when the item is back in stock.
Question: does the flow end when that email goes out, and does the alert clear afterwards?
Recommended: end on the email, and leave the alert clearing off the board.
Why: the spec names one email and nothing after it, so an extra step would be invented.

Reading: the customer taps and types, and two steps happen without them, the alert being saved and the email going out when stock returns.
Question: are those two drawn as automatic steps, with no service names anywhere on the board?
Recommended: yes on both counts.
Why: an actor on a user flow is a person, a system or a timer, and a service name is implementation the board is not for.

Answer, correct either one, or say go on and I will proceed on the recommendations and ask round three on decisions, states and source class.