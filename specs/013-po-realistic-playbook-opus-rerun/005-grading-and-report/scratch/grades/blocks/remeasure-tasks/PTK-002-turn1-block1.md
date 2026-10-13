I'll create your task. Ines's notes cover the limits, the five states, the copy keys and the edge cases, so I'll write the acceptance checklist from them. Before I draft, I need these answers in one reply:

**Format & scope:**
- Your conventions say "Guest app" with no platform means iOS, Android and web together. Should this be one FE task for all three, or one task per platform, given that web is built and released on its own?
- State 5, the property's minimum stay, only happens on the property page, which uses the `PROP` feature code. Should it stay in this task (`FE - Guest app - SRCH - Date picker stay limits`) or go into its own `PROP` task?

**Requirements:**
- Is anything in the notes out of scope for this task, or should anything be added? If nothing changes, I'll cover states 1 to 5, the five edge cases, the screen reader announcement and the Monday or Sunday week start

**Design & platform:**
- Can you send the Figma link to the `Date picker / Stay limits` frame? The notes name the frame but give no URL

**Dependencies:**
- The notes say the 30-night maximum and the 365-day window come from search-service config, and the minimum stay comes with the property details. Do the apps and web already receive these values, or does a BE task need to land first? If so, what is its title or link?
- Can the design system calendar already show a day as disabled while still accepting a tap? If not, is there a DS task I should link?
- Is there a parent story or epic, or a Guest Support ticket for the 23 August chats, that I should link?

**Validation:**
- Hana sent the six copy keys for translation. Should the task wait until all seven locales are in, or can it ship with the en-GB fallback?
- When a saved search that breaks a limit gets cleared, does the guest see any message, or does the picker just open in state 1? I'll assume there's no message unless you tell me otherwise
