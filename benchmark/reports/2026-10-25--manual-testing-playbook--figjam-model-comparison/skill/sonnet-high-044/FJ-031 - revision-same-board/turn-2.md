Before I draw anything, this is how I read the request. A yes to this settles the reading only, and nothing is written.

Question: which screens does a Fernhouse customer pass through to start a return, and where do they choose?

Outcome: a reader can follow a return from the order list to a confirmed return and see where the 30 day window stops it.

Settled by your description:
- The five screens give the order list, Order detail with Start a return, the list of return reasons, the drop-off or courier pickup choice and the confirmation with a QR code
- The returns doc gives the 30 day window after delivery and the Contact support exit after it, both current behavior

Reader, outcome and exclusions are your accepted answers from round one. The reader is the Fernhouse product team, the detail is balanced, the audience is mixed and the board is read on a laptop. These stay assumed until you correct them.

Left out:
- The free pickup over 100 euros, a proposal under review
- Anything after the confirmation, such as what happens at the drop-off point or on a courier visit

Two facts are assumed, because your description doesn't state them:
1. The window check sits after Order detail. The doc says the app shows Contact support once the window has passed, but not on which screen. A screenshot of the screen that shows Contact support would settle it.
2. The screens run in the order you listed them, and nothing sits between the method choice and the confirmation. If picking a drop-off point or booking a pickup slot is a screen of its own, it needs a source or a screenshot.

Outline, in drawing order. The first line is the sentence the board answers, and the rest is one line per node and edge:
- Board question: which screens does a Fernhouse customer pass through to start a return, and where do they choose?
- Order list, the start (the order list screen)
- Order detail, a screen (the order detail with the Start a return button)
- Within 30 days of delivery?, a decision (the returns doc)
- Contact support, an end (the returns doc)
- Return reason, a screen (the list of reasons)
- Drop-off or pickup?, a decision (the method choice)
- Confirmation with QR code, the goal (the confirmation screen)
- Edges: Order list to Order detail, Order detail to the window check, then No to Contact support and Yes to Return reason, Return reason to the method choice, then Drop-off point and Courier pickup both to the confirmation

That is 7 nodes and 7 connectors, inside the 9 node budget. No node fails the remove test.

Two framings:
- A happy path with the exits beside it (recommended). The main line runs from the order list to the confirmation, Contact support sits below it and the two method exits rejoin at the confirmation. It reads fastest and answers the question.
- A state map of every exit. It shows more ways out, but your sources name only one, so it would draw exits nobody gave me.

Look, all recommended and assumed until you say otherwise:
- The confirmation is the one accent, as the goal, so the eye lands where the flow ends. The gate then answers four critique questions about the sketch, starting with where the eye goes first.
- Three zones, left to right: Find the order, Request the return and Done
- Title "Start a return", subtitle "How a Fernhouse customer starts a return in the app, from the order list to a confirmed return"
- Source line: "Sources: the request's description of the app screens and the returns doc. Left out: free pickup over 100 euros, a proposal under review."

Is this the right reading of the board?