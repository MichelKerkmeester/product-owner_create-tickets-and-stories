Reading confirmed. Now the write gate, which needs its own yes before anything lands on the board.

**Write gate**

* Question: which statuses does a Roamstay booking pass through, and what moves it between them
* Outcome: the reader can name every status, the event that sets it and every way a booking ends
* First glance: the main path, Pending → Confirmed → Completed
* Second glance: the two early exits, guest cancels and missed check-in → No-show
* Last glance: the key and source line under the board

Target: the existing FigJam board `<test-file-key>`. The write adds one framed board titled `Booking status` — 7 states, 12 transitions, the Confirmed composite drawn as a tinted section, the three end states in the final-state grey, plus title, subtitle, key and source line. It lands 400px right of the rightmost content, so nothing existing is covered. No extensions planned.

Calls: one `use_figma` compose call and one `get_figjam` read-back.

Rollback: delete the one board section this write returns, and only after you say yes to that too.

Write it?