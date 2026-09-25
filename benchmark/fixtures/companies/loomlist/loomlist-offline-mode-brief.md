# Offline mode, epic brief

Brief by Oskar, Product Manager, Mobile, for the offline mode epic.
Shared with the Sync, Mobile Platform and Web and Desktop teams on 2026-09-23.

## Problem

Loomlist needs a connection for everything past the page already on screen. Between June and August, 23% of iOS and Android sessions started without a connection or lost it within the first minute. In the cancellation survey, 31% of Plus workspaces that gave a reason between April and August named offline access.

Support sees it too. An edit made while the connection is gone is retried until the app closes and then lost, and some of the `lost-edit` tickets Marta raised in #sync-eng start that way.

## Goal

A member on iOS, Android or Desktop can open, read, edit and create pages without a connection, and everyone else sees their changes once the device is back online.

## Platforms

iOS, Android and Desktop. Web is out of scope. A browser tab cannot be relied on to keep a local copy between visits, and Desktop covers the laptop case.

## Scope

**Offline reading.** The device keeps the 500 most recently opened pages with their blocks, inline databases and to-dos, capped at 1 GB, whichever limit comes first. Images and files count toward the cap. A page that falls out of the 500 is removed the next time the app has a connection.

**Offline editing and creation.** Members can edit blocks, check off to-dos and create pages and to-dos with no connection. Every change queues on the device in the order it was made. Sharing, inviting, moving a page to another workspace and deleting a page stay online only, and their controls show as unavailable offline.

**Sync on reconnect.** When the connection returns, queued changes start uploading within 30 seconds, oldest first. Today sync-service resolves every overlap with block-level last-writer-wins on protocol v3, so a phone that was offline for a day can replace a whole morning of a teammate's edits.

**Offline indicator and storage settings.** A small offline marker in the top bar, a count of changes waiting to sync and a storage screen in settings. The storage screen shows space used, lets the member lower the 1 GB cap and clears offline data.

## Dependency

Conflict handling is not settled. Joana, Engineering Manager, Sync, decides how sync-service handles conflicting edits on 2026-10-09, choosing between the options in the #sync-eng thread. Offline editing and creation and Sync on reconnect cannot be finalised until that decision lands. Offline reading and the indicator do not depend on it and can start first.

## Target

Q1 2027 for all four areas on iOS, Android and Desktop.

## How we will know it works

- The share of mobile sessions that hit the no-connection screen drops by half within 8 weeks of release
- `lost-edit` tickets that start with a dropped connection stop coming in

## Out of scope

- Web
- Choosing which pages to keep offline
- Searching pages that are not kept on the device
- Offline access in the Support console
