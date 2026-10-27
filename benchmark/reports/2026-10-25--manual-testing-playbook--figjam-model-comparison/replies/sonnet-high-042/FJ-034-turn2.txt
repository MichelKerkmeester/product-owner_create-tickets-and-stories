Lanes it is. You didn't answer questions 1 and 2, so their recommended answers stand as assumed and the playback names them. Nothing is written yet.

### The reading

| Row | Value | Status |
|---|---|---|
| Reader | CS and warehouse leads | assumed, settled by your answer to question 1 |
| Question | Who does what from the damage report to the released refund, and where does the work change hands? | captured from your request |
| Outcome | The reader sees who owns each step and where the three handoffs fall | assumed, same answer |
| Scope | The path you listed, plus the second-photo loop. Left out: refund amounts, time limits, photo requirements, payment-provider steps, a rejection exit and a failed-inspection exit | assumed, settled by your answer to question 2 |
| Entry | The customer reports damage with a photo | captured |
| Exit | The refund is released | captured |
| Actors | Customer, CS, Warehouse, one lane each | captured |
| Decisions | One: CS approves or asks for a second photo | captured |
| Sources | Your description in the request, taken as current behavior. There is no policy doc to re-read | captured |

The defaults are a balanced detail level, a mixed audience and laptop reading distance.

### The outline

The first line is the sentence the board answers: who handles a damaged-item refund, step by step, and where the work moves between Customer, CS and Warehouse.

1. Customer lane: "Damage reported with photo" starts the flow (Entry)
2. CS lane: "Approve the claim?" is a decision with two exits (Decisions). I merged your "checks it" step into it, because a check step followed straight by this decision says nothing the diamond doesn't
3. Customer lane: "Send a second photo" is the target of the loop. You didn't state this step, so it is my reading of the loop (assumed)
4. Warehouse lane: "Book a pickup" (Actors)
5. Warehouse lane: "Inspect the item" (Actors)
6. Warehouse lane: "Refund released" is the end (Exit)

The connectors are:

* 1 to 2, a handoff from Customer to CS
* 2 to 3, labelled "Second photo needed", a handoff back to Customer
* 3 to 2, closing the loop
* 2 to 4, labelled "Approved", a handoff from CS to Warehouse
* 4 to 5
* 5 to 6

That is 6 nodes and 6 connectors, inside the limit for a process with lanes.

### Two framings

* The happy path on one line, with the second-photo loop beside it. It shows the three handoffs and costs you the failure exits
* A map of every exit, including rejection and a failed inspection. It costs you facts your sources don't state

I recommend the first. It answers your question and draws nothing you didn't say.

### The look

* The accent goes on "Approve the claim?". It is the only branch and it sits at the CS to Warehouse handoff. "Refund released" stays the green goal
* Lanes are the only grouping, so there are no extra zone lines
* The title is "Fernhouse damaged-item refund"
* The subtitle is "Who does what from the damage report to the released refund, with CS approval as the one branch"
* The source line is "Sources: the process as described in the request. Left out: refund rules, a rejection exit, a failed-inspection exit"

Is this reading right? Correct any row or line, or say yes and I'll build and check the model.