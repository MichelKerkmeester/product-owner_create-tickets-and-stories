```markdown
# Offline mode Epic - clarification

* * *
Oskar's brief settles this Epic's problem, goal, four scope areas and two release measures, so Problem, Goal, Solution and the release-level acceptance criteria are ready to draft.
One decision is still open, and it settles `## Scope` on its own, so the draft waits on your answer.

## The open decision

The brief names four areas and three platforms, and the choice below decides what a single child story owns.

| Grouping | Child stories | What one story owns |
|----------|---------------|---------------------|
| One per area | 4 | One area across iOS, Android and Desktop |
| One per area and platform | 12 | One area on one platform, with Scope grouped by area |
| One per platform | 3 | All four areas on one platform |
| A split you name | your call | Give the story list and how Scope should group it |

## What the choice changes

- Option A keeps the shared work in one story, because the local page store, the edit queue and the reconnect upload behave the same on every platform
- Options B and C put each platform's own release schedule in its own story, and repeat the shared work across stories
- The brief starts offline reading and the offline indicator ahead of offline editing and sync on reconnect, so say whether that sequencing becomes an `#### Added Later` group or all four areas land together in Q1 2027

## What I will assume unless you correct it

- The title reads `# Epic - Platform - Offline mode`, because the work lands on three platforms rather than with one persona
- The two measures under "How we will know it works" become the release-level acceptance criteria
- Joana's sync conflict decision of 2026-10-09 sits as a dependency of the affected child stories rather than as an open question in Scope
- The local page store, the edit queue and the reconnect upload are one shared mechanism rather than three per-platform builds
- The brief's four exclusions stay out of the draft, and no `## Delivery` section is added unless you ask for one
- I derive each child story title from the grouping you pick unless you name one yourself
```

Export-equivalent path: `export/001 - Epic-offline-mode-clarification.md`

HVR self-scan: 0 hard blockers. Fixed: none, since no source hedge or filler phrase is carried into the question. Kept with reason: the literal section names `## Scope`, `## Delivery` and `#### Added Later` in backticks as house identifiers, and "How we will know it works" as the brief's own heading quoted intact.

Quality status: clarity, completeness and assumption challenge pass. Artifact kind resolved as Epic, Scope blocked on one open decision, no requirement checklist, `## Delivery` not forced.

The child-story set is the one thing I cannot infer safely. You gave two candidate splits and the brief supports both, and Scope is the section that separates an Epic from a Story, so drafting now would mean inventing a split. The four assumptions worth a second look are the `Platform` title segment, the shared-mechanism reading, the no-Delivery choice, and carrying Joana's 2026-10-09 sync decision as a child-story dependency. Answer the grouping and the Epic drafts straight from the brief, with About, Scope and the two release measures as release-level criteria. The Epic comes next once you answer.