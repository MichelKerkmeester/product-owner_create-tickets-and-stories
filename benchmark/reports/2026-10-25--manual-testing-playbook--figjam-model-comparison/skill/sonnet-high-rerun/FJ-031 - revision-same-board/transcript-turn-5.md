# FJ-031 turn 5 transcript

**User:** change the Fernhouse return flow on that board: after 30 days the app now shows Request an exception instead of Contact support

**Assistant:**

Here is how I read the change before I touch the board.

**What changes**
* Node 4 changes from "Contact support" to "Request an exception". It stays the exit on the "No" branch of "Within 30 days?", so the connector and its "No" label stay as they are
* Everything else in the outline stays the same: 7 nodes, 7 connectors, the three zones and the goal with the accent
* Last glance: Request an exception, the exit after 30 days. First and second glance are unchanged
* Source line: "Sources: the Fernhouse app, the returns doc and a later team update. Left out: free pickup over €100, a proposal under review."

**A source conflict, and how I read it**
The returns doc, Section 2, says the app shows Contact support after 30 days. Your message now says it shows Request an exception. I recommend your message governs, because it is the later statement and the board's purpose is current behavior. The doc line is then outdated, and the board's source line says a later update changed it.

**Assumed, and what would settle each**
* Request an exception is a screen or action that leaves this flow, so it stays an end node in the orange "Leaves the flow" colour. A source for what it opens would settle it, and the board draws nothing past it
* The change applies to the same 30-day rule, so the "Within 30 days?" decision, its label and the Start a return exit are unchanged
* The existing board never gets edited in place. I compose a new board, check it, read it back, and only then ask whether to delete the old one by its title. Because the file already holds "Start a return 15", I recommend the title "Start a return 16" for the new one

The other "Start a return" sections in the file that still say Contact support stay as they are, since you didn't ask about them.

Is this the right reading of the change?
