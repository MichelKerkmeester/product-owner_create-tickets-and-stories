# FJ-026 turn 2 transcript

**User:** Use your recommended answers.

**Assistant:**

Before I draw anything, this is the reading, the outline and the look.

**Reading**
* **Question:** which booking statuses exist and what moves a booking between them?
* **Outcome:** support can read every status and spot the three a booking ends in.
* **Dials:** balanced detail, a mixed audience and the Laptop reading distance, all assumed.
* **Settled by your message and your answers:**
  * The five statuses and six moves you listed.
  * Cancellation leaves from Pending and Upcoming only, not from In stay.
  * The board shows only the moves you listed.
* **Assumed:**
  * "Cancelled" is the end state's name.
  * The source line reads "Source: the Roamstay booking status description given in the request." Your message is the only source, so it counts as current behaviour until you say otherwise.
* **Left out:** payment failure, expiry, refunds, booking edits and cancellation after check-in. The reply will name each one.
* **Still open:** none.

**Outline**

The first line is the question the board answers.
1. Which statuses exist and what moves a booking between them?
2. Pending is the first state, where every booking starts.
3. Confirmed is a section that holds Upcoming and In stay.
4. Completed, Cancelled and No-show are the three end states.
5. Pending to Confirmed: `card authorised`.
6. Upcoming to In stay: `check in`.
7. Confirmed to Completed: `check out [from In stay]`.
8. Pending to Cancelled: `guest cancels`.
9. Confirmed to Cancelled: `guest cancels [from Upcoming]`.
10. Confirmed to No-show: `missed check-in [from Upcoming]`.
11. Each end state leaves to the machine's end dot.

The board has 7 states and 12 transitions, within the nine-state budget. Every item traces to a line of your message, so the remove test cuts nothing.

**Two framings**
* **A. Confirmed as a section (recommended).** It matches how you described Confirmed, which covers Upcoming and In stay, so support sees the grouping. The cost is that the exits that only Upcoming or In stay take carry a `[from ...]` guard in their label.
* **B. Seven flat states.** Each exit leaves from its exact state, so no guards are needed. The cost is that Confirmed disappears as a status, even though it is the status support sees.

**Look**
* **Colour:** the composer draws Completed, Cancelled and No-show in light gray with a heavy outline and lists them as "Final state" in the key. Your request needs nothing more.
* **First glance:** Pending, the light blue first state.
* **Second glance:** Upcoming and In stay, read with the Confirmed section around them.
* **Last glance:** the three end states. A `%% focus:` line marks one of them with a pink outline. I recommend Cancelled, because two states lead into it and support will meet it most.
* **Title:** "Booking status". If the file already holds a section with that title, I'll name it at the gate and recommend "Booking status 2".
* **Subtitle:** "Every status a Roamstay booking passes through, from the pending request to a completed, cancelled or missed stay, and what moves it on".
* **Zones:** only the Confirmed section.

Is this the right reading of the board?
