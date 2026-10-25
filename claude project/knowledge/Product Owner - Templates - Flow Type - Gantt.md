# Product Owner - Templates - Flow Type - Gantt

A gantt chart puts tasks and phases on a time axis, with milestones as points. The composer draws each section as a tinted band, each task as a named row with its bar on a shared axis and each milestone as a diamond, and picks the tick spacing from the chart's length. Neither it nor the generated fallback honours colour, axis, weekend or marker settings, so a model never sets them.

---

## 1. WHEN TO USE

**The reader's question:** which tasks and phases are active when?

- A release plan or a launch plan with dates
- A sprint or a phase plan with dependencies between tasks
- A one-day run of show, in hours

Use a process when there are no dates and the order of steps is the point. Figma's `timeline` kind is not drawn, so a list of dated events with no durations is a gantt chart of milestones.

---

## 2. WHAT THE BOARD DRAWS

```text
gantt
    title Offline mode launch
    dateFormat YYYY-MM-DD
    section Build
    Sync engine :active, sync, 2026-11-02, 3w
    Conflict screen :screen, after sync, 2w
    section Launch
    Release :milestone, after screen, 0d
```

- `dateFormat YYYY-MM-DD` for a chart of days or longer, and `HH:mm` for one day
- A task is `Name :tags, id, start, duration or end`. The tags and the id are optional, the start and the end are not
- A start is a date or time in the declared format, or `after` one or more task ids
- A duration is a number and a unit: `d` days, `w` weeks, `M` months, `y` years, or `h` and `m` for hours and minutes on a one-day chart
- Tags are `done`, `active`, `crit` and `milestone`, and the tag sets the bar's colour role: `done` for done, `inProgress` for active, `error` for critical and `neutral` for an untagged task, with the bar's length written inside it when it fits. Assets - Flow Board Design names the swatch each role draws. A critical bar also ends that label with `, critical` and takes a heavier outline, so it still stands out in greyscale

---

## 3. RULES

Check these rule by rule before the gate:

- **A `dateFormat` of `YYYY-MM-DD` or `HH:mm`,** before the first task, with every start in that format
- **The first task starts on a date,** which anchors the chart, and every `after` names a task above it
- **The right unit for the chart.** A lowercase `m` on a date chart means minutes, so months are `M`, and a one-day chart uses `h` and `m`
- **A milestone has a zero duration,** and the `vert` tag is refused, because the generated fallback skips that task
- **No styling and no ignored setting:** `classDef`, `class`, `style`, `click`, `tickInterval`, `axisFormat`, `excludes`, `includes`, `weekend`, `todayMarker` and their kin
- **camelCase task ids,** each used once, and task names of at most 40 characters with no colon
- **At most 12 tasks,** sections once there are more than 8, and at most 5 bars running at once in one section, the house diagram guide's gantt budget
- The shared rules: no emoji, markup or literal `\n`

Judged by hand:

- **One chart per timeframe.** A sprint and a year do not share an axis
- **`after` over fixed dates** for work that follows other work, so one slip moves the rest
- **`crit` only on the real critical path,** and `active` only on what runs now. If every bar is critical, none is
- **Task names of two to five words,** with dates on the axis rather than in the name

---

## 4. BUDGET AND SPLITTING

Over budget, collapse each phase to one bar in an overview chart and draw one chart per phase beside it in the same file. At `Meeting screen` distance task names drop to 32 characters. At `Wall` distance the budget drops to 8 tasks and 3 bars running at once in a section, with names at 25 characters, as the reading distance dial in Templates - Flow Mode Section 4 sets out.

---

## 5. COLOUR, ZONES AND NOTES

None in the model. The tags colour the bars and the sections are the zones. The composer draws no dependency arrow, because an `after` already sets where a bar starts. A note on a date goes on through Templates - Flow Hybrid Workflow. A `%% focus: <id or name>` line may name the one task or milestone the first glance lands on. It is a comment, so the model stays styleless.

---

## 6. WRITING THE BOARD

The model is placed into Assets - Flow Board Composer and one `use_figma` call draws the board, as Templates - Flow Mode Section 6 sets out. On the generated fallback, `generate_diagram` takes `name`, `mermaidSyntax` and `userIntent` with no `useArchitectureLayoutCode`.

---

## 7. READ-BACK

Count sections, tasks and milestones, and check each task's section and its start or dependency. A milestone is counted once, as a milestone and not again as a task, so counting every task line in the model gives the board's tasks plus its milestones. Both routes widen very short bars to stay visible, the composer to 16 pixels, so compare order and dependencies, not bar lengths.

```text
Read-back: 3 of 3 sections, 7 of 7 tasks, 2 of 2 milestones
```

---

## 8. PATTERNS AND EXAMPLE

- Assets - Flow Templates - Gantt holds a phased plan with dependencies and a one-day run of show
- Examples - Flow - Gantt draws a launch plan from a planning doc
