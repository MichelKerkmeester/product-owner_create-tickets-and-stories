Your request covers five flows that answer different questions, so I need one answer from you before I model anything.

Reading: `context/fernhouse-context.md` covers returns, refunds and the warehouse check in detail. It has the CS agent, CS lead and Warehouse operator roles, the 30-day return window, the €200 agent refund limit and the label email. For signup it only says accounts-service handles sign-in, with no steps or screens. It describes no billing beyond the payment session inside checkout, and the warehouse is described outbound only, from paid order to carrier collection. Signup is a user flow, and returns, refunds and the warehouse are a laned process, so two types fit.

Question: Which question does the reader bring to this board? Either who does what, from a return request to the refund (a laned process), or which screens a customer passes through at signup (a user flow). If it is the second, please send the signup screens, because I won't draw steps no source states.

Recommended: one laned process board, "Return to refund", with lanes for Customer, CS agent, Warehouse operator and CS lead. It would leave these for later boards:
*   Signup, which needs screens
*   Billing, which needs you to say whether it means the checkout payment or something else
*   Outbound warehouse fulfilment, which is its own process or an architecture

Why: returns, the warehouse check and the refund are one chain of hand-offs, and the sources already cover it. A board of all five would pass the node budget and mix types that read differently.

The board would go into file `<draft-file-key>` as a new section beside what it already holds, so no plan or new file is involved. I'll read that file once before the write gate and name any section that shares the title. Nothing is written until you answer here and then say yes to the gate.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.