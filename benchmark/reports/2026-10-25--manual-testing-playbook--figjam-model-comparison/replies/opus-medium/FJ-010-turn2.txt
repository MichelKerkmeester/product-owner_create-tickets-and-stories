**Playback: Fernhouse returns user flow**

First, a correction to my last message: the flow has 8 nodes, not 8 screens plus 2 decisions. Only one of the two choices changes the route, as explained under the framings below.

**Brief**
- **Reader:** the Fernhouse product team *(your choice)*
- **Question:** which screens does a customer pass through to return an item, and where can the return stop? *(your choice)*
- **Outcome:** decide whether the 30-day check is in the right place and whether an exit is missing *(your choice)*
- **Scope:** from opening an order to the confirmation screen. It leaves out how refunds and store credit are processed and the warehouse side *(your choice)*
- **Start and end:** it starts when the customer opens an order and ends at the confirmation screen. The not-eligible screen is a second ending *(from the returns doc)*
- **Who acts:** the customer at every step except the 30-day check, which the system makes on its own *(assumed: the doc doesn't say who makes the check)*
- **Choices:** one check that changes the route, whether the order is within 30 days. Choosing refund or store credit doesn't change the route *(from the returns doc)*
- **Source:** your summary of the returns doc, treated as how returns work today *(your choice)*

**Outline**, in drawing order. The board answers: "Which screens does a customer pass through to return an item, and where can the return stop?"
1. Open the order *(start)*
2. Return an item
3. Pick an item and reason
4. Ordered within 30 days? *(the check)*
5. No → Not eligible *(ends here)*
6. Yes → Choose refund or store credit
7. Print the label
8. Return confirmed *(the goal)*

That's 8 nodes and 7 arrows. I merged picking the item and picking the reason into one step so the flow stays under the 9-node limit.

**Two ways to draw the refund or store credit choice**
- **A. One step, "Choose refund or store credit"** *(recommended)*. Both options lead straight to printing the label, so drawing them as separate paths adds two arrows that end in the same place and tell the reader nothing new.
- **B. A two-way choice whose paths rejoin before the label.** This shows both options on the board, but it uses all 9 nodes and leaves no room for an exit you may want to add.

**Look** *(all recommended, all assumed until you say otherwise)*
- **Highlighted node:** the 30-day check, because deciding where it belongs is the reason for the board. The board shows that the check comes after the customer has already picked an item and a reason.
- **Detail, audience and viewing size:** a normal level of detail, written for a mixed team, sized to read on a laptop
- **Zones:** none, because 8 nodes read clearly without grouping
- **Title:** Fernhouse returns
- **Subtitle:** Which screens a customer passes through to return an item, and where the return can stop
- **Source line:** Source: the Fernhouse returns doc, as summarised in the request. Left out: refund and store credit processing, warehouse handling

**Not covered by the doc:** cancelling or going back partway is missing. I'll leave it off the board and list it as a gap rather than guess a path.

Is this reading right, framing A included? Correct any line, or say yes. Next I'll send the write gate as a separate reply. Nothing is written to Figma before you say yes there.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.