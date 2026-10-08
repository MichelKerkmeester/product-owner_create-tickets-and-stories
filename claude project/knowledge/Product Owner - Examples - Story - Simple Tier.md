# Product Owner - Examples - Story - Simple Tier

Instantiates the house Story shape at its smallest: a Problem section, a Solution with Expected outcomes and References, no Requirements section because the story carries no hard constraint the acceptance criteria do not already say, two outcome-led Given/When/Then criteria with Mark-as-done, and no Delivery section, so the artifact ends on Acceptance criteria. No optional enrichments.

---

# Fieldstack - Projects - Inline rename

* * *
## Problem
* * *
Renaming a project today means leaving the project view for Settings, because the title in the project header is read-only. Rename lives two clicks away from where the name is shown, so a one-character fix turns into a detour. Every typo in a project name costs a member that detour before the team sees the right name.
* * *
##   

## Solution
* * *
Let the project name be edited where it is read. The header title becomes the field itself, so renaming is a correction made in passing rather than a trip into Settings, and the save happens the moment the member moves on, because a separate button would turn a two-second fix back into a form.
* * *

**Expected outcomes**
* * *
*   Members fix a typo without leaving the project view
*   No separate save action is needed for a rename
* * *

#### **References**
* * *
Components
*   [Page | Project header](https://figma.example/fieldstack/project-header)
Flows
*   [Inline rename](https://figma.example/fieldstack/inline-rename)
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

1 ) **Rename a project without leaving it**
* * *
*   **Given** the project header shows `"Q3 Launch"`
*   **When** the member edits the title in place and moves focus away
*   **Then** the new name is saved
*   **And** every project surface shows it, with no separate save step to remember
* * *
- [] _Mark as done, if the criteria are met_

2 ) **An invalid name never replaces the saved one**
* * *
*   **Given** the last saved name is `"Q3 Launch"`
*   **When** the member leaves the field empty, or takes it past the `60`-character limit, and focus moves away
*   **Then** the saved name stands unchanged everywhere the project appears
*   **And** the member is told what to correct
*   **And** the name they typed is still there to fix
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   
