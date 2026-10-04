Path: `export/002 - Story-free-cancellation-filter.md`
Verified: read-back succeeded; 140 lines
HVR self-scan: 0 hard blockers. Fixed: none needed (the always-cut modifier `also` came out during drafting as an edit). Kept with reason: `Given`/`When`/`Then`/`And` repeat verbatim as the house fixed labels, `* * *` is the house divider, and the backticked strings, numbers and identifiers (`Free cancellation until 14 Oct`, `d MMM`, `No stays with free cancellation for these dates`, `Clear filter`, `filter_applied`, `filter_name`, `free_cancellation`, `8.13.0`, `1,146 stays`, `312 stays`) are supplied values quoted verbatim in Requirements.

**Quality summary (Story kind, Story shape, saved in the Story lane at `002`)**

| Dimension | Result |
| --- | --- |
| Completeness | Preamble, About, Problem, Solution, Expected outcomes, Requirements, seven acceptance criteria |
| Clarity | Every requirement reads as a constraint a build can fail |
| Actionability | Criteria state outcomes, with the mechanism left to the developer |
| Accuracy | Every value traces to Tomas's notes or the two asks, nothing invented |
| Relevance | No ticket fields, points or process material |
| Mechanism Depth | Problems framed by surface, so edge cases land in the right group |

The Story kind is a **Story** for the Search squad, H1 `Guest - Search - Free cancellation filter`. Both asks are in as constraints, the first in the Result card badge group and the second in the Results with the filter on group, and one format check passes clean on the export.

One reading to confirm: I took the badge ask as fixing which calendar date shows, so the deadline is the property's local date while Tomas's `d MMM` guest-locale pattern still sets its format. If the ask was meant to replace that pattern with the property's locale, say so and I will change that one item. The clarification at `export/001` is untouched.