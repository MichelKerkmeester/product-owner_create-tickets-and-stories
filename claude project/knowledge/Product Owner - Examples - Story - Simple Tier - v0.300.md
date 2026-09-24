# Product Owner - Examples - Story - Simple Tier - v0.300

Instantiates the house Story shape at its smallest: the story preamble, an About umbrella (Problem, Solution, Expected outcomes, References), no Requirements section because the story carries no hard constraint the acceptance criteria do not already say, two outcome-led Given/When/Then criteria with Mark-as-done, and no Delivery section, so the artifact ends on Acceptance criteria. No optional enrichments.

---

# Fieldstack - Projects - Inline rename

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
The project title sits in the project header. Renaming a project today means leaving the project view for Settings, which turns a one-character fix into a two-click detour. This story makes the header title editable in place, so members never leave the project view to correct a name.

### Problem
* * *
Members leave the project view to correct even one character:
*   The header title is read-only
*   Rename lives in Settings, two clicks away from where the name is shown
* * *

### Solution
* * *
Let the project name be edited where it is read. The header title becomes the field itself, so renaming is a correction made in passing rather than a trip into Settings, and the save happens the moment the member moves on, because a separate button would turn a two-second fix back into a form.
* * *

#### **Expected outcomes**
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

1\. **Rename a project without leaving it**
* * *
*   **Given** the project header shows `"Q3 Launch"`
*   **When** the member edits the title in place and moves focus away
*   **Then** the new name is saved and every project surface shows it, with no separate save step to remember
* * *
- [ ] _Mark as done, if the criteria are met_

2\. **An invalid name never replaces the saved one**
* * *
*   **Given** the last saved name is `"Q3 Launch"`
*   **When** the member leaves the field empty, or takes it past the `60`-character limit, and focus moves away
*   **Then** the saved name stands unchanged everywhere the project appears
*   **And** the member is told what to correct, and the name they typed is still there to fix
* * *
- [ ] _Mark as done, if the criteria are met_
* * *
##   
