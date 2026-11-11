---
title: "Product Owner - Examples - Story - Sectioned Shape"
description: "Instantiates the sectioned Story shape at large size: the Mobile Story of a Desktop and Mobile pair for one thermostat app. Problem lists three gaps, Solution groups its changes, and Requirements open on a dependency section before three numbered sections with design links and every state enumerated. Seven outcome-led criteria close on design fidelity, with no Delivery section."
contextType: general
importance_tier: normal
trigger_phrases: ["sectioned story example", "large story example", "worked story example"]
version: 0.17.0.13
---

# Hearthly - Thermostat - Mobile: Room cards & schedule

* * *
## Problem
* * *
When homeowners check their rooms and adjust a day's heating in the Hearthly app on Mobile, three gaps get in the way:

*   **Silent rooms:** a room with no sensor reading shows a blank card, so the homeowner cannot tell a dead sensor from a cold room
*   **Schedule edits:** a heating block changes only through a form, so the homeowner leaves the schedule to move it by one step
*   **Room sheet:** the sheet always opens at full height, so it hides the schedule it belongs to
* * *
##   

## Solution
* * *
Let a homeowner read every room at a glance and edit a day's schedule where it is shown. The story bundles three main changes and a few small UI/UX improvements.

**Main changes**
* * *
*   A room card with no reading says so, instead of showing nothing
*   A schedule block moves by dragging its handle, and the time stays readable under the finger
*   The room sheet sizes to its content, up to a fixed maximum

**Small UI/UX improvements**
* * *
*   A bigger handle hit area, so a block is easier to grab
*   Tapping anywhere on a room card opens its sheet

**Expected outcomes**
* * *
*   Homeowners tell a dead sensor from a cold room at a glance
*   Homeowners adjust a block in one drag, without leaving the schedule
*   The schedule stays in view while a sheet is open
*   The room cards and the schedule share one consistent look on Mobile

#### **References**
* * *
Components
*   [Room card](https://figma.example/hearthly/room-card)
*   [Schedule block](https://figma.example/hearthly/schedule-block)
Flows
*   [Edit a day's schedule](https://figma.example/hearthly/edit-schedule)
* * *
##   

## Requirements
* * *
### 1\. Token dependency
* * *
The Hearthly design tokens v2 are needed to build this story, so the work starts once that ticket ships.
[Hearthly design tokens v2](https://tasks.hearthly.example/t/design-tokens-v2)

- [] Integrate the v2 tokens into the Hearthly app
- [] The cards, the schedule and the sheet take every shadow and background gradient from those tokens, so none is hard-coded
###   

### 2\. Room cards
* * *
**User flow:** a homeowner scans the room cards on the Mobile home screen

Design
[Mobile - Room card](https://figma.example/hearthly/mobile-room-card)
[Mobile - Room card - Empty states](https://figma.example/hearthly/mobile-room-card-empty)

#### **Card content**
* * *
**Header**
* * *
- [] Room name: `Semi Bold / Large (1.125 REM, 18px)`
- [] Temperature: `Bold / Display (2 REM, 32px)`, with the unit `°C` in `Regular / Large (1.125 REM, 18px)`
- [] Sensor icon: `24px` (`1.5 REM`)

**Humidity chip**
* * *
- [] Label: `Medium / Base (1 REM, 16px)`
- [] Icon: `16px` (`1 REM`)

**Missing data (empty states)**
* * *
- [] Implement each empty state of the card as the linked design shows it
- [] Missing temperature: the reading shows `--`, so the humidity chip keeps its place
- [] Missing humidity: the chip is hidden, and the name and temperature stay
- [] Missing temperature and humidity: the card shows the room name and the label `No sensor data`
- [] Sensor offline (edge case): the card keeps its last reading and adds the label `Offline`, so a stale value never reads as live
###   

### 3\. Schedule editor
* * *
**User flow:** a homeowner edits a day's heating schedule by dragging a block handle

Design
[Mobile - Schedule block](https://figma.example/hearthly/mobile-schedule-block)
[Mobile - Schedule block - Drag](https://figma.example/hearthly/mobile-schedule-drag)

#### **Block**
* * *
**Handle**
* * *
- [] Handle at rest: `4 x 24 px`
- [] Hit area: `44 x 44 px`, taller than the visible handle, so the block is easy to grab
- [] The hit area never changes during or after a drag

**Snapping**
* * *
- [] A block snaps to `15 min` steps
- [] A block is never shorter than `15 min`

#### **Drag and release**
* * *
**While dragging**
* * *
- [] The handle grows from `4px` to `8px` wide
- [] The time readout above the block grows from `Regular / Large (1.125 REM, 18px)` to `Bold / Display (2 REM, 32px)`, so the time stays readable under the finger
- [] Every other block of the day dims to `40%` opacity, so the active block stands out

**On release**
* * *
- [] The handle returns to `4px`
- [] The readout returns to `Regular / Large (1.125 REM, 18px)`
- [] The other blocks return to `100%` opacity

**Midnight edge case**
* * *
- [] A block that ends after `00:00` continues on the next day's row
- [] Both rows show it as one block, with the readout on the row being dragged
###   

### 4\. Room sheet
* * *
**User flow:** a homeowner taps a room card or a schedule block and opens the room's sheet

Design
[Mobile - Room sheet](https://figma.example/hearthly/mobile-room-sheet)

**Sheet height**
* * *
- [] Max height: `60% DVH`, so the schedule stays visible above the sheet
- [] Content shorter than `60% DVH`: the sheet height follows the content
- [] Content taller than `60% DVH`: the sheet stays at max height and scrolls

**Sheet content**
* * *
- [] A room with no notes reads `No notes for this room yet.`
- [] Shared with: the room card tap and the schedule block tap, one sheet for both
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

1 ) **A room without a reading still reads clearly**
* * *
*   **Given** a homeowner on Mobile opens a home screen with a room that reports no temperature, no humidity or neither
*   **When** the cards render
*   **Then** each card shows the matching empty state from the linked design
*   **And** a room whose sensor is offline keeps its last reading
*   **And** the card says the sensor is offline
* * *
- [] _Mark as done, if the criteria are met_
* * *

2 ) **A block follows the finger and lands on a clean time**
* * *
*   **Given** a homeowner on Mobile edits a day's schedule
*   **When** they drag a block handle and release it
*   **Then** the block follows the finger
*   **And** it lands on a time the schedule accepts
*   **And** it never ends up shorter than the shortest allowed block
* * *
- [] _Mark as done, if the criteria are met_
* * *

3 ) **The schedule stays readable while a block moves**
* * *
*   **Given** a homeowner on Mobile drags a block handle
*   **When** the drag starts
*   **Then** the time stays readable under the finger
*   **And** the other blocks step back so the active block stands out
*   **And** on release, everything returns to rest with no jump
* * *
- [] _Mark as done, if the criteria are met_
* * *

4 ) **A block that crosses midnight stays one block**
* * *
*   **Given** a block that ends after midnight
*   **When** the homeowner drags it
*   **Then** it moves as one block across both days
*   **And** both days show the same times
* * *
- [] _Mark as done, if the criteria are met_
* * *

5 ) **The sheet keeps the schedule in view**
* * *
*   **Given** a homeowner on Mobile taps a room card
*   **When** the sheet opens
*   **Then** the schedule stays visible above it
*   **And** the sheet fits its content up to its maximum height, then scrolls
*   **And** a room with no notes shows the no-notes message
* * *
- [] _Mark as done, if the criteria are met_
* * *

6 ) **Both entry points open the same sheet**
* * *
*   **Given** a homeowner on Mobile views a room card and a schedule block of the same room
*   **When** they tap either one
*   **Then** the same sheet opens with the same content
* * *
- [] _Mark as done, if the criteria are met_
* * *

7 ) **Every change is applied, and it matches Figma 1:1**
* * *
*   **Given** a homeowner on Mobile opens the home screen and a schedule
*   **When** the cards, the schedule and the sheet show
*   **Then** every change in this story is applied, including the cards, the handles and the sheet
*   **And** every shadow and background gradient is taken 1:1 from the Hearthly design tokens v2, with nothing hard-coded
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   
