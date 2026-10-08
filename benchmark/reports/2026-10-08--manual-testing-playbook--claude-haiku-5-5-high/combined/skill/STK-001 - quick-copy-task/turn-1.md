export/001 - task-free-shipping-banner-copy.md

Verified: read-back succeeded; 49 lines
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

Quality summary: Accuracy is strongest, since each banner string and threshold traces to the banner line in context/fernhouse-context.md (lines 20 and 128-132). Completeness and Relevance are covered by the three requirement groups: banner copy, translations and small-phone fit.

The task changes the free-shipping banner to `Free shipping over €50` and `Free shipping over £45`, with the threshold amounts unchanged. The translations follow the new English lines, since the context file names the English lines as the source strings for every locale. The small-phone check runs per locale, because translated lines can be longer than the English.

Additions I made that you did not ask for, so you can strike them:
- **Translations (requirement 2).** Derived from the context file's "source strings for every locale" note. No translated strings were supplied, so none are written in the task.
- **Per-locale small-phone check (requirement 3).** Added because translated lines can wrap even when the English does.
- **Title surface.** The title uses `Web` because the template takes one surface. The change also covers iOS and Android. If you track platforms separately, split the work into per-platform subtasks under an FS parent.

Open points:
- The context file does not say where the banner copy is set. I assumed client code (FE). If it comes from promotions-service, the discipline becomes BE or FS.
- No phone width was supplied, so the small-phone checks name no device.
- If the copy ships in the apps, it reaches most customers about a week after release.
- I did not edit context/fernhouse-context.md. Its line 20 still shows the old copy, so the owning team should update it when this ships.