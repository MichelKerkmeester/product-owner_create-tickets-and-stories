I'll create your task. Before drafting, please answer these in one reply:

**Format & scope:**
- FE covers one client per task. Which client is this for: Web (which also reaches Desktop with no Desktop release), iOS or Android? If you need more than one, should that be one task per client?
- todos-service owns the To-dos view queries. Does it already return a "due today" result, or does this need back end work too? If it does, should the task be FS, or FE with a BE dependency?

**Requirements:**
- Why do members need this chip? Which persona does it serve (Dana, Theo or Mireille), and what problem does it solve?
- How should "today" be defined? The Overdue chip uses the to-do owner's time zone. Should Due today use it too?
- Should to-dos that are already checked off appear under Due today? Overdue leaves them out
- Where does the chip go among All, Assigned to me and Overdue? What exact label should it use?
- What should the list show when no to-dos are due today?
- Can Due today and Overdue be active together, or does the one-active-chip rule stay?

**Design & platform:**
- Do you have Figma links for the chip and its empty state?
- Label copy has to ship in en-US, de-DE, fr-FR, es-ES, ja-JP and pt-BR. Are translations in scope for this task or handled somewhere else?

**Analytics:**
- `filter_selected` currently sends `all`, `assigned_to_me` or `overdue`. Should this task add a new value such as `due_today`? If yes, has the Data team already reviewed it in a tracking plan? Client work waits for that review

**Dependencies:**
- Does this task have a parent, a story or any related tickets? Please give their titles or links

**Validation:**
- What am I likely to get wrong about this chip? Which of the Overdue rules above should Due today not copy?
