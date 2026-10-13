You are a fresh reviewer. Investigate, then propose. Edit nothing outside AI Systems/Product Owner/specs/010-requirements-bloat/, run no sync compiler, commit nothing. Read-only commands and gate runs are fine.

Repo: /Users/michelkerkmeester/MEGA/Development/AI Systems.

The problem, in the owner's words: "The requirements still carry some unneeded bloat sometimes. Like in Product Context/z — Product Owner/Story Drafts/Highlights - Onboarding - Instagram ReAuth/Highlights - Onboarding - Instagram ReAuth.md where it explains what's in the sheet."

Read that file's Requirements section. The Initial Instagram Sheet group reads:

- A completely new sheet that explains the situation
- It opens as a bottom sheet over the presentation screen with the page still visible behind it
- It states Instagram is not linked
- It explains that quick connect now works without logging in again
- It carries the one action `Link Instagram`

Four of those five describe what a screen says and shows. They are narrative UI description, not constraints a delivery must satisfy. The rule as written was meant to stop exactly this. Find out why it did not.

Read, in this order:
1. AI Systems/Product Owner/sk-product-owner/assets/story-template.md, the Requirements slot and its Notes For Use
2. AI Systems/Product Owner/sk-product-owner/references/story-mode.md, section 1 Core Rules (the supplied-hard-values bullets), section 3 house grammar (the Requirements and acceptance-criteria bullets), section 4 steps 1 and 4, section 9 checklist
3. AI Systems/Product Owner/sk-product-owner/SKILL.md, the ALWAYS rules and the blocking gate
4. AI Systems/Product Owner/claude project/Custom Instructions.md, the matching rules
5. AI Systems/Product Owner/sk-product-owner/references/quality-scoring.md
6. The five worked examples under sk-product-owner/assets/examples/story/
7. The sixteen rewritten stories under AI Systems/Product Owner/export/Story Drafts/ and the source drafts and context.md files that produced them, to see how widespread this is and which source shapes trigger it

Recent history that matters: Requirements was changed from outcome bullets to hard constraints only, made optional, and then given a rule that every hard value the source supplies travels verbatim, grouped per screen, with each shared screen's reuse map as a constraint. Commits 84bba2e, 1b47426, 3969874 and acd1aa1. Read them with git show. The suspicion worth testing: the carry-through rule tells the model to bring everything the source states into Requirements, and the hard-constraint rule tells it to bring only constraints, and where a source describes a screen in prose the first rule wins.

Deliver, to AI Systems/Product Owner/specs/010-requirements-bloat/findings.md:
1. Why the current rules permit this, quoting the exact sentences that conflict or fail to exclude. Name which rule the model was obeying when it wrote each of the four bloated bullets.
2. How widespread it is: count across the sixteen exported stories how many Requirements bullets are UI description rather than constraints, with per-file numbers and five worst examples quoted.
3. The test that separates the two. Give a one-sentence rule a model can apply to a bullet without judgement, and show it correctly keeps "Uploads up to 1 GB", "Playback uses HLS", "Heading size is h4", "Spacing is 32px", "The action reads Link Instagram" and correctly rejects the four bloated bullets above. State where a borderline case lands and why.
4. The exact edits, file by file, with the current text quoted and the replacement written, for the skill (template, story-mode, SKILL.md, quality-scoring) and the Claude Project (Custom Instructions.md, and any knowledge file that teaches the shape). Keep SKILL.md between 400 and 600 lines and edit it and Custom Instructions.md once each.
5. Whether the worked examples model the wrong thing anywhere, with the lines to change.
6. Whether the format gate can check this mechanically. If a check is possible without misfiring on a legitimate constraint, give the code and the fixture pair. If not, say so plainly and do not propose a heuristic that will misfire.
7. What a story should do with the screen description it drops: which section carries it, or whether it is dropped entirely and the design link stands in its place.

Prose rules for anything you write: no em dashes, no semicolons in prose, no curly quotes, bullets never end in a full stop. Be specific, quote evidence, no praise.
