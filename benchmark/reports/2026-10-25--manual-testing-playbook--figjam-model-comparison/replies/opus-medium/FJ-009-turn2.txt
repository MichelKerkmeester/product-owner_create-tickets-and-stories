The chart passed the pre-write check, and I've composed the code for it. Nothing is written yet.

**Checked chart**

```text
gantt
    title Loomlist offline mode launch plan
    dateFormat YYYY-MM-DD
    section Design
    Design :crit, design, 2026-11-02, 2w
    section Build
    Sync engine :sync, 2026-11-02, 3w
    Conflict screen build :crit, screen, after design, 2w
    Integration :crit, integrate, after sync screen, 1w
    section Launch
    Beta :crit, beta, after integrate, 2w
    Release :milestone, release, after beta, 0d
```

- **What it answers:** which work runs when before the offline mode release, and what sets the release date. A reader sees that Design, Conflict screen build, Integration and Beta set Release on 21 Dec 2026, and that Sync engine has a week of slack.
- **First glance:** the Release milestone, 21 Dec.
- **Second glance:** the four critical bars that lead to it.
- **Last glance:** the Sync engine bar and its slack, and the source line.
- **Check:** passed, 6 tasks in 3 sections. On the board that's 5 tasks, 1 milestone and 5 dependency arrows, drawn in the default FigJam design at laptop reading distance.

**The write**
- **File:** `<test-file-key>`, the existing FigJam file. The board keeps whatever plan the file already belongs to. Your Figma account has no plan called "Loomlist Product". It has <figma-plan-1>, <figma-plan-2> and the personal <figma-plan-3> plan.
- **What gets written:** one new board section titled "Loomlist offline mode launch plan", 400 px to the right of everything on the page. The 9 offline mode boards already in the file stay as they are.
- **Extensions:** none.
- **Calls:** one `use_figma` to draw the board and one `get_figjam` to read it back.
- **If the write into that file fails:** I'll stop and ask before creating a new file. A new board can't reuse this yes. My recommendation for that case is a new FigJam file in the <figma-plan-1> plan, left in drafts with no project.
- **Rollback:** delete the one section this write creates. That only happens if you say yes to a question that names it.

Shall I write this board into `<test-file-key>` now?

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.