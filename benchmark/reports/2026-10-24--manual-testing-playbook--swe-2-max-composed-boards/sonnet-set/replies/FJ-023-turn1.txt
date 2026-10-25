Before I write anything to the file, please check the reading and the write plan below. The checked model is ready: `flow_check.py` passed with 8 nodes, 8 connectors, 2 decision exits and 3 lanes, and the board code composed.

**What the board answers**

A process with 3 lanes: Customer, CS agent and Warehouse operator. It answers who does what in a damaged-item refund and where the claim changes hands.

**Reading of your runbook lines**

* Customer reports damage with a photo through the help form. Drawn as the start, "Damage reported"
* CS agent checks the photo and asks "Damage clear?". Clear goes to "Approve the claim". Unclear goes to "Send a second photo" and loops back to the check
* An approved claim goes to the warehouse queue. This is the handoff, drawn as the edge "Claim queued"
* The operator books a courier pickup, inspects the item and the refund is released. "Refund released" is the end
* The claims table is a dashed "Logs" link to the store
* Refunds under 20 euros skip the pickup. This is a pilot that is not live, so it stays off the board and is named in the source line and in my reply

**Three readings I assumed. Correct any of them**

1. **Which end is highlighted.** I highlight "Approve the claim", the step that sends the claim to the warehouse. The alternative is "Book a courier pickup", the first warehouse step. The runbook doesn't name the slower side, so I took the sending step. The highlight is the violet fill, and the key names it "In focus".
2. **What gets logged.** "Every decision is logged" is drawn from the CS "Damage clear?" decision only. The runbook names no other decision, so the operator's release is not linked to the log.
3. **Who reads it.** I assumed a mixed team of CS and warehouse staff, in plain verbs and the runbook's own words.

**Gap the runbook leaves open**

It doesn't say what happens if the inspection finds something other than damage. The board stops at "Refund released" and draws no failed-inspection path.

**What the reader sees first**

* First glance: "Approve the claim" and its "Claim queued" handoff to the warehouse
* Second glance: the three warehouse steps that follow, ending in the refund
* Last glance: the claims table link and the second-photo loop

**Target file**

You asked for a new board in the Fernhouse Product plan and also for the existing file `<test-file-key>` rather than a new file. I read that as a new board section inside the existing file. The plan name is as you stated it. The tools can't confirm which plan owns that file.

**Write plan**

* **File:** `<test-file-key>`, not a new file
* **Writes:** one board section titled "Damaged-item refund", with a title, subtitle, key and source line. It lands 400 pixels right of whatever the file already holds, so nothing existing is covered
* **Calls:** `create_session`, Figma's `figma-use` and `figma-use-figjam` skill reads, one `use_figma` and one `get_figjam` read-back
* **Allowance:** on a Starter plan or a View or Collab seat, reads count toward the six tool calls a month, so the read-back could be refused
* **Rollback:** delete the one board section the write returns. That needs its own separate yes from you

Reply **yes** to approve both the reading above and the write, or send corrections.