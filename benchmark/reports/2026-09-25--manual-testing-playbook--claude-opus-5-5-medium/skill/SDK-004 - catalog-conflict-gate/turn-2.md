I've saved the catalog of the six activity emails. The daily digest is listed at 08:00 in the recipient's local time, as you decided, and the page says the inventory's 07:00 UTC is out of date.

Path: `export/002 - doc-activity-emails-catalog.md`
Verified: read-back succeeded; 166 lines
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: em dashes in the `*   **Term** — definition` bullets and the `Status: Current behavior — …` label, which are the two places the ClickUp layout allows them.

**Quality summary**
- **Source safety:** pass. Every fact comes from the three files. The spec decides timing and who gets each email. The inventory supplies template names, the fields each template fills in, the sending jobs, test-send dates and the pre-change checks. The context file is background only, and all three source files are unchanged.
- **Shape fit:** pass. It's a catalog with one entry per email ID, an index table, rules that apply to all six and a table for Support on why an email didn't arrive.
- **ClickUp layout:** mostly pass. Dividers, bullets, sentence-case headings and heading depth are right, with no spacer headings in the file. I couldn't find the `validate-output-format.cjs` checker in this workspace, so I checked the layout by hand instead.
- **Readability:** pass.
- **Voice:** pass.

**Things I added, so you can strike any of them:**
- **The "Why an email did not arrive" table:** I rearranged the sourced rules into a table for Support. It contains no new facts.
- **Three gaps under Catalog boundaries:**
  - How the digest job sends at 08:00 local time, since the inventory's description of that step is out of date.
  - The event that triggers the workspace invite (EM-05).
  - Whether the Support console shows a member's email settings.
- **A one-line note that push notifications aren't covered:** you asked to leave push out, so delete the line if you don't want it mentioned at all.

The page opens with an index linking to each email's entry. Scheduled and event-triggered emails are grouped separately, and the per-email detail is aimed at both Support and the Notifications engineers.