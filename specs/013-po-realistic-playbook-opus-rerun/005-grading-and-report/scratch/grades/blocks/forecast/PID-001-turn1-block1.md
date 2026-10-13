I'll create your task. Before drafting, I need the answers below in one reply.

**Format & scope:**
- This is front end (FE) work under the TODO feature code. Each FE task covers one client, so the title will read `FE - {Platform} - TODO - Due today filter chip`
- Which client is this for? A Web change also reaches Desktop the next time it loads, with no Desktop release
- If iOS and Android need the chip too, should I write one task per platform or an FS parent that splits into them?

**Requirements:**
- What counts as "due today"? I'd start from the Overdue rule: not checked off, with a due date equal to today in the to-do owner's time zone. Should to-dos already checked off today or overdue to-dos also appear?
- Where does the chip go relative to All, Assigned to me and Overdue? Does the one-active-chip rule still apply?
- What should the list show when nothing is due today?
- Do you already have acceptance criteria you want included?

**Design & platform:**
- Is there a Figma link for the chip and the empty state?

**Dependencies:**
- Does todos-service already support a due-today query, or does this need a BE ticket first?
- Analytics: `filter_selected` would need a new `filter` value, most likely `due_today`. The Data team reviews tracking plan changes before any client work starts. Has that been approved, or should I list it as a blocking dependency?
- The app ships in six locales (en-US, de-DE, fr-FR, es-ES, ja-JP and pt-BR). Who provides the chip label strings?
- Are there any related or dependent tickets?

**Validation:**
- You called this small. I read that as meaning the query already exists and only the chip is new. Is that right?
- What else am I likely to get wrong?
