---
title: "FigJam Type - Gantt"
description: "Tasks, phases and milestones on a time axis, drawn as a FigJam gantt chart in one of two date formats, with no styling, anchored dependencies, twelve tasks and five parallel bars per section."
contextType: implementation
importance_tier: important
trigger_phrases:
  - "figjam gantt chart"
  - "roadmap timeline figjam"
  - "launch plan figjam"
  - "milestones on figjam"
version: 1.0.0.0
---

# FigJam Type - Gantt

A gantt chart puts tasks and phases on a time axis, with milestones as points. The generator draws sections as lanes and picks the axis unit from the chart's length. It strips every colour and ignores the axis, weekend and marker settings.

**Loading Condition:** CONDITIONAL, when the Flow route draws a gantt chart
**Purpose:** The grammar, rules, budget and read-back for a gantt chart
**Pairs With:** `assets/templates/gantt.md`

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
- Tags are `done`, `active`, `crit` and `milestone`

---

## 3. RULES

The check enforces:

- **A `dateFormat` of `YYYY-MM-DD` or `HH:mm`,** before the first task, with every start in that format
- **The first task starts on a date,** which anchors the chart, and every `after` names a task above it
- **The right unit for the chart.** A lowercase `m` on a date chart means minutes, so months are `M`, and a one-day chart uses `h` and `m`
- **A milestone has a zero duration,** and the `vert` tag is refused, because the generator skips that task
- **No styling and no ignored setting:** `classDef`, `class`, `style`, `click`, `tickInterval`, `axisFormat`, `excludes`, `includes`, `weekend`, `todayMarker` and their kin
- **camelCase task ids,** each used once, and task names of at most 40 characters with no colon
- **At most 12 tasks,** sections once there are more than 8, and at most 5 bars running at once in one section, sk-design-diagram's gantt budget
- The shared rules: no emoji, markup or literal `\n`

Judged by hand:

- **One chart per timeframe.** A sprint and a year do not share an axis
- **`after` over fixed dates** for work that follows other work, so one slip moves the rest
- **`crit` only on the real critical path,** and `active` only on what runs now. If every bar is critical, none is
- **Task names of two to five words,** with dates on the axis rather than in the name

---

## 4. BUDGET AND SPLITTING

Over budget, collapse each phase to one bar in an overview chart and draw one chart per phase beside it in the same file. At `Meeting screen` distance task names drop to 32 characters. At `Wall` distance the budget drops to 8 tasks and 3 bars running at once in a section, with names at 25 characters, as the reading distance dial in `references/flow-mode.md` Section 4 sets out.

---

## 5. COLOUR AND THE HYBRID PASS

None in the model. Colour-coded phases, notes on a date or a dependency arrow between lanes are hybrid extensions. When the request is mostly those, Figma's advice is to build the timeline directly with `use_figma` instead, and the reply says the board was drawn by hand and has no generated layout.

---

## 6. CALLING THE TOOL

`generate_diagram` with `name`, `mermaidSyntax` and `userIntent`. No `useArchitectureLayoutCode`. The `fj` route cannot draw a gantt chart.

---

## 7. READ-BACK

Count sections, tasks and milestones, and check each task's section and its start or dependency. The generator widens very short bars, so compare order and dependencies, not bar lengths.

```text
Read-back: 3 of 3 sections, 7 of 7 tasks, 2 of 2 milestones
```

---

## 8. PATTERNS AND EXAMPLE

- `assets/templates/gantt.md` holds a phased plan with dependencies and a one-day run of show
- `assets/examples/gantt-loomlist-offline.md` draws a launch plan from a planning doc
