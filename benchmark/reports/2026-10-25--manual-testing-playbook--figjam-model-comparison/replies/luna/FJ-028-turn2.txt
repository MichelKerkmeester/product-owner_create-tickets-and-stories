## Write gate

Flow Mode requires a separate yes after the checked-model preview. Your earlier yes confirmed the reading.

**Target:** Loomlist Product plan, existing FigJam file `<test-file-key>`

I’ll add a new section titled **Loomlist offline mode launch schedule** and one Android note beside the Release milestone. The note will say: “Android follows next quarter; not yet approved. Start date and duration are not set.”

**Check:** The model passed for one Gantt diagram. The composer reports six scheduled items, two sections, six nodes and five dependency arrows, using the FigJam default design.

**Question and outcome:** When can offline mode reach release, and which dependency chain sets the date? The chart shows the path to the 5% beta and release.

**First glance:** Desktop and iOS integration.  
**Second glance:** The critical chain through beta to the 21 December release.  
**Last glance:** Android’s unapproved status and the schedule gaps.

**Review checks:** The eye lands on integration, the task identified as critical; its dependencies lead to the release date; parallel build work remains visible; Android stays secondary because it has no approved schedule.

```mermaid
%% title: Loomlist offline mode launch schedule
%% subtitle: The Loomlist Product team can track the 5% beta and release against the critical path
%% source: Source: user-provided launch plan. Main approval status is unstated. Left out: owners and an Android work bar without an approved date or duration
%% focus: integration
gantt
    title Loomlist offline mode launch
    dateFormat YYYY-MM-DD
    section Design and build
    Conflict-screen design :crit, screenDesign, 2026-11-02, 2w
    Sync engine build :syncEngine, 2026-11-02, 3w
    Conflict-screen build :crit, screenBuild, after screenDesign, 2w
    Desktop and iOS integration :crit, integration, after screenBuild syncEngine, 1w
    section Beta and release
    Beta to 5% of workspaces :crit, beta, after integration, 2w
    Release :milestone, release, after beta, 0d
```

The write will use two `use_figma` calls, one for the Gantt and one for the Android note, followed by one `get_figjam` read-back. Rollback removes only the new section and its note; existing content stays untouched.

Should I write this section and note into the specified FigJam file?