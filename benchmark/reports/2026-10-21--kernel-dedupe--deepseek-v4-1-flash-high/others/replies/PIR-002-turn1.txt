```markdown
# Fernhouse wishlist on web and in the apps: bug or Story

Two artifact commands arrived in one request, and the two sources disagree on what this change is. CS asks for a bug fix while Storefront says the split has always been the built behaviour. The answers below settle the kind and the scope in one pass.

## Energy level

**What the sources show:** neither command names an energy level, and both sources arrive with 412 contacts of detail.

**Recommendation:** Standard, because the sources are dense enough that a lean pass would mostly restate them.

- Say quick for a lean pass on smart defaults
- Say deeper for a longer pass that weighs both sources in full

## Artifact kind and shape

**What the sources show:** the app wishlist is device-local by design and unchanged in 4.8.0 or 4.8.2, so nothing regressed. Lotte has not answered whether the apps should change.

**Recommendation:** Story, because there is no defect to report and the ask is a product decision to make the wishlist one list.

- Choose Bug only if a source says the apps were meant to sync, since that would make today's behaviour a defect
- Say Story or an Epic with child stories if the outcome needs splitting by surface
- Name Lotte's decision if she has settled it, because the sources say nobody has picked it up

## Scope

**What the sources show:** the 412 contacts split four ways, 171 losing the app list after a new phone or reinstall, 138 missing app items on web, 64 missing web items in the app and 39 stopped by the 50 item limit.

**Recommendation:** cover all four groups, because each describes the same split between a device list and an account list.

- Confirm whether all four groups are in scope or only the cross-device loss
- Confirm the 50 item limit stays at 50 once the lists merge

## Signed-out customers

**What the sources show:** the app wishlist works without an account and web needs sign-in, so one merged list has to serve both cases.

**Recommendation:** keep a device-only list for signed-out app users and merge it into the account list at sign-in.

- Confirm a signed-out customer can still save items in the app
- Say what happens to that device list when the customer signs in later

## Release and ownership

**What the sources show:** 4.9.0 is the next app release, most customers take about a week to update, and anything needed sooner has to be server-side.

**Recommendation:** target 4.9.0, because the split is long-standing and no customer is blocked within a day.

- Confirm 4.9.0, or say if this has to land sooner
- Confirm accounts-service owns the merged list, since the wishlist spans accounts-service and app storage
```

Export-equivalent path: `export/NNN - intake-wishlist-cross-device-loss-clarification.md`
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.
Quality: not scored, clarification only | Kind: Bug or Story | Energy: Standard

The question settles the artifact kind first, then scope, signed-out handling and the release target. It favours Story because Storefront confirmed the app list is device-local by design, so there is no defect to write up. Bug stays open only if a source says the apps were meant to sync.

### Open items
None identified

Answer in one message and I'll draft the Story, or the bug if you pick that.