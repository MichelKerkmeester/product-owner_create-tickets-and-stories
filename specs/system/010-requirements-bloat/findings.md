# Requirements bloat in Story Mode

Read-only review. Nothing outside this folder was changed, no sync compiler ran, nothing was committed. The format gate and its fixtures were run at baseline and both pass.

Corpus: the sixteen stories under `AI Systems/Product Owner/export/Story Drafts/`, 221 Requirements bullets across the fifteen that carry the section. Rule sources: `sk-product-owner/assets/story-template.md`, `sk-product-owner/references/story-mode.md`, `sk-product-owner/SKILL.md`, `sk-product-owner/references/quality-scoring.md`, `claude project/Custom Instructions.md`, the five worked examples and the four commits `84bba2e`, `1b47426`, `3969874`, `acd1aa1`.

---

## 1. Why the current rules permit this

### 1.1 The source, and what the model was actually looking at

The story's own source folder holds two things. `context.md` gives the Initial Instagram Sheet exactly one line:

```
#### Initial Instagram Sheet
Compeltely new sheet that explains the situation
```

`Screenshots/2 No Instagram ReAuth/` holds four PNGs. `Highlights _ Sheet _ Instagram Auth _ 1.png` is the sheet itself, and its on-screen copy transcribes as:

```
Instagram
Link Instagram to use it for your highlight reel
We noticed your Instagram isn't linked yet.
Did you get stuck reconnecting Instagram after the recent update due to the required login?
Good news! We made it easier:
  You can now quickly connect Instagram without logging in again
  Just tap 'Allow' when prompted
Notice: Quick connect only works if you've logged into Instagram from your browser before.
Otherwise, you'll have to log in first.
[ Link Instagram ]
```

Four of the five bullets at `Highlights - Onboarding - Instagram ReAuth.md:51-55` map onto that picture, not onto `context.md`. This is the shape that triggers the failure: one prose line in the text source, and the whole screen in an image beside it.

### 1.2 The two rules that conflict, quoted

The carry-through rule, `story-mode.md:79`:

> Every line of the source is accounted for, not only the lines under a screen heading. A change stated above the first heading, in a preamble, or for a surface the headings never name, such as the modal that opens the flow or a global change to all screens, is a supplied value like any other.

Reinforced at intake, `story-mode.md:162`:

> Account for every entry in the draft, either as a constraint bullet or as a line in the delivery response naming it deliberately out of scope. A supplied value that appears in neither is a defect rather than an editorial judgement.

The hard-constraint rule, `story-mode.md:116`:

> Requirements hold hard requirements only: the formats, limits, platforms, integrations, compliance rules and performance floors the delivery has to satisfy whatever approach the developer takes. Each group is a bold-lead name, a divider and short `*   ` bullets, one constraint per bullet, stated as a fact or an instruction. Never a `**Checklist**` sub-block or `- [ ]` items, and never a user outcome dressed as a constraint.

The suspicion in the brief is confirmed, and the mechanism is sharper than a tie. The carry-through rule is an instruction with a named defect attached: fail to carry a line and you have shipped a defect. The hard-constraint rule is an adjective plus a two-item exclusion list, and the two items it excludes are a `**Checklist**` and a user outcome. Narrative UI description is neither. The list of what Requirements holds reads as examples, and nothing anywhere states that the list is closed. So a model holding a sixth kind of sentence about a screen finds a rule that orders it to carry the line and no rule that forbids the shape it carries it in. The instruction wins because it is the only one of the two that names a consequence.

The only sentence in the whole set that limits what a screen group contains is `story-mode.md:76`:

> one bold-lead group per screen, named as the source names it, holding that screen's values and nothing else

"and nothing else" is a floor, not a ceiling. It forbids another screen's values from landing in this group. Reading it as a ceiling requires first deciding what counts as a value, which is the thing no rule defines.

### 1.3 Which rule produced each of the four bullets

| Bullet, `...Instagram ReAuth.md` | Rule the model was obeying | Why the rule permitted it |
| --- | --- | --- |
| `:51` `A completely new sheet that explains the situation` | `story-mode.md:78`, the unsupplied-change rule: "Never invent the string, and never drop the line: an unsupplied value is an open constraint, not an absent one" | The source line is a change named without content. The rule names the destination and the prohibition but never the form, so the model satisfied "never drop the line" by copying the line |
| `:52` `It opens as a bottom sheet over the presentation screen with the page still visible behind it` | `story-mode.md:79` plus `:162`, reading the screenshot as a source line | Presentation and composition are not on any exclusion list, and the intake harvest at `:162` invites the model to walk the source and list every change |
| `:53` `It states Instagram is not linked` | `story-mode.md:162`, which lists "exact strings, button copy" as things to harvest | The screenshot supplies the string `We noticed your Instagram isn't linked yet.` The model harvested it and then paraphrased it |
| `:54` `It explains that quick connect now works without logging in again` | same as `:53` | The screenshot supplies `You can now quickly connect Instagram without logging in again` |

`:55` `It carries the one action `Link Instagram`` is the one bullet in the group that obeyed `story-mode.md:75` correctly, because a button label is short enough to survive as a value.

Two consequences worth naming. First, `:53` and `:54` are not only permitted description, they are live violations of a rule that already exists. `story-mode.md:75` says:

> Never generalise a supplied value into a description of itself: `32px` never becomes updated spacing, and `Link Instagram` never becomes updated copy. A generalised value is not a shorter requirement, it is a different and false claim, that the change is still unspecified

`It states Instagram is not linked` is `We noticed your Instagram isn't linked yet.` generalised into a description of itself. The rule did not fire because nothing in the set says a screenshot supplies values. The one rule that mentions images is a prohibition on the artifact carrying one, `story-mode.md:129`: "a Story or Epic never carries an image, a screenshot reference or a file path to one". So the model may read the picture, must not cite it, and has no instruction for how to carry what it saw.

Second, the same four descriptions were copied forward into acceptance criterion 3, whose Then and And clauses read `it opens as a bottom sheet over the presentation screen with the page still visible behind it` and `it states Instagram is not linked, explains that quick connect now works without logging in again`. The rule at `story-mode.md:117` that polices this is stated as a token test:

> The test is mechanical: a criterion that would have to be edited when a design token changes is a criterion holding a constraint that belongs in Requirements

No token appears in those clauses, so the test does not fire.

### 1.4 Every check in the system runs in one direction

Step 4 validation, `story-mode.md:183-184`, checks that supplied values are present and not misplaced. The checklist entries at `:392`, `:394` and `:395` do the same. `quality-scoring.md:100` names two supplied-value failures and both are omission failures, a value generalised and a value dropped. Nothing anywhere reconciles in the other direction, from the bullet back to the source. A Requirements bullet that traces to no supplied value, no reuse entry, no rule and no design pointer is not a finding in any gate.

Relevance, floor 8, is the dimension that would in principle catch it, and `quality-scoring.md:68` states its test at section granularity:

> The test: apply the reconstruction test in `references/conciseness.md` section by section. More than one section a reader could rebuild from what remains puts the score at 6

Four bloated bullets sitting inside a Requirements section that also holds twelve real constraints leave the section as a whole earning its place, so the section-level test scores it a pass.

---

## 2. How widespread it is

221 Requirements bullets across fifteen files. `Creator - Deal applications - Rejection reasons` carries no Requirements section and is excluded from the denominator.

Classification used the test in section 3. A bullet is **description** when its whole content is what a screen says, shows, contains or looks like, and it names no value, limit, condition, effect or named flow a build could get wrong. A bullet is a **rider** when it is a real constraint carrying a trailing clause of screen description that should be trimmed.

| Story | Bullets | Description | Riders | Description rate |
| --- | --- | --- | --- | --- |
| Content Gallery - Media - Change Tabs on Scroll | 7 | 4 | 0 | 57% |
| Highlights - Onboarding - Instagram ReAuth | 17 | 4 | 0 | 24% |
| Onboarding v2 - Highlights Step | 19 | 4 | 0 | 21% |
| Onboarding - Not Approved | 12 | 2 | 0 | 17% |
| Content Gallery - Highlights - Empty state | 10 | 1 | 2 | 10% |
| Creator - Onboarding v2 - Album Navigation | 10 | 1 | 0 | 10% |
| Creator - Media Editor | 13 | 1 | 0 | 8% |
| Onboarding - Birthday | 22 | 1 | 3 | 5% |
| Creator - Onboarding - Social Relink Flow | 27 | 1 | 0 | 4% |
| Creator - Profile - Media Grids | 9 | 0 | 2 | 0% |
| Onboarding - Profile completion from Pre-Approval stage | 20 | 0 | 1 | 0% |
| Content Gallery - Highlights - Edit Reel UX | 13 | 0 | 1 | 0% |
| Creator - Motivation - Edit UX | 13 | 0 | 0 | 0% |
| Creator - Onboarding v2 - Complete Profile | 12 | 0 | 0 | 0% |
| Creator - Settings - Linked Social Media | 17 | 0 | 0 | 0% |
| Creator - Deal applications - Rejection reasons | no section | n/a | n/a | n/a |
| **Total** | **221** | **19** | **9** | **8.6%** |

28 bullets of 221 need an edit, 12.7% of the section across the corpus.

### 2.1 Which source shapes trigger it

Five of the sixteen folders ship a `context.md`. The other eleven ship screenshots only.

| Source shape | Bullets | Description | Rate |
| --- | --- | --- | --- |
| Folder ships a `context.md` | 86 | 5 | 5.8% |
| Folder ships screenshots only | 135 | 14 | 10.4% |
| `context.md` folders excluding ReAuth | 69 | 1 | 1.4% |
| `Creator - Onboarding - Social Relink Flow` alone | 27 | 1 | 3.7% |

The relink flow is the cleanest file in the corpus at 27 bullets, and its `context.md` is the only source that states values. It supplies `h4`, `h3`, `32px`, `10px`, `20px`, `Link Instagram instead of Link my Instagram` and a reuse map per screen. The model had values to carry, so it carried values.

ReAuth is the outlier inside the `context.md` group, and it is the exception that proves the rule. Its `context.md` gives the sheet one prose line and no values at all, and its screenshots carry the whole screen. Given a group heading with nothing to put under it, the model filled the group from the picture.

The finding is that bloat tracks the absence of stated values in the source. Where a source names a screen and supplies nothing, the per-screen grouping rule at `story-mode.md:76` creates an empty container, and the accounting rule at `:79` forbids leaving it empty.

### 2.2 Five worst examples, quoted

1. `Highlights - Onboarding - Instagram ReAuth.md:53`

   > `*   It states Instagram is not linked`

   The screenshot the bullet is describing reads `We noticed your Instagram isn't linked yet.` The bullet replaced a shippable string with a report that a string exists.

2. `Content Gallery - Media - Change Tabs on Scroll.md`, four of seven bullets, the entire styling body of the story

   > `*   The selected tab is a solid light pill with bold dark text`
   > `*   The unselected tabs are translucent pills`
   > `*   The header zone gets a dark gradient, darker at the top and transparent toward the grid`
   > `*   A progressive blur keeps the content underneath readable behind the tabs`

   No pill radius, no gradient stop, no blur radius, no token. Every one is a caption for a design a reader has to open anyway.

3. `Onboarding v2 - Highlights Step.md`, bullets 11 and 13, which the same section then disclaims

   > `*   Platforms that are not linked read as unlinked`
   > `*   Shows the chosen set, with a per-piece edit affordance`

   Bullet 17 of the same section reads `The unlinked-platform state is owned by `Content Gallery - Highlights - Empty state``, and bullet 16 reads `The edit affordance on review tiles and the sheet behind it are owned by `Content Gallery - Highlights - Edit Reel UX``. The story describes two surfaces and then says it does not own either.

4. `Onboarding - Not Approved.md`, bullets 5 and 10

   > `*   A hero collage of creator content cards shows first, then the Barter logo`
   > `*   No back chevron and no bottom navigation`

   Bullet 10 also restates bullet 3, `The state has no navigation bar and no access to the deal feed or the profile`, which is the version that constrains routing rather than chrome.

5. `Onboarding - Birthday.md:` bullet 1

   > `*   Presents as a bottom sheet over the calling screen, carrying a title, a supporting line, the picker and a single confirming action`

   A four-item inventory of what is on one screen. Bullets 13, 14 and 15 of the same file already carry the title, the line and the action as quoted strings, so the inventory adds nothing and duplicates three bullets below it.

---

## 3. The test that separates the two

### 3.1 The rule

> A Requirements bullet must be a sentence a build can fail, so strike any bullet that reports what a screen says, shows or contains without naming a value, limit, condition, effect or named flow that a build could get wrong.

Applying it takes no judgement about importance. It asks one question of the bullet: point at the thing in this sentence that a build could get wrong. If the answer is a number, a unit, a token, a heading level, a platform, a format, an integration, an identifier, a string in backticks, a limit, a trigger condition, a persisted effect, a reuse map or an owning story, the bullet stays. If the only answer is "the screen would look different", the design link already carries it and the bullet goes.

### 3.2 The nine cases

| Bullet | Verdict | The thing a build could get wrong |
| --- | --- | --- |
| Uploads up to `1 GB` | keep | the limit `1 GB` |
| Playback uses `HLS` | keep | the format `HLS` |
| Heading size is `h4` | keep | the token `h4` |
| Spacing is `32px` | keep | the value `32px` |
| The action reads `Link Instagram` | keep | the exact string `Link Instagram` |
| A completely new sheet that explains the situation | strike | nothing, "explains the situation" names no content a build could miss |
| It opens as a bottom sheet over the presentation screen with the page still visible behind it | strike | nothing, the design settles the presentation and the bullet names no alternative it rules out |
| It states Instagram is not linked | strike | nothing as written, and the repair is to quote the copy, which converts it to a keep |
| It explains that quick connect now works without logging in again | strike | same, quote the copy or drop the bullet |

The two struck copy bullets carry their own repair. Quoting the string turns each into a keep, which is what `story-mode.md:75` already demands and what the model failed to do because no rule told it a screenshot supplies strings.

### 3.3 The borderline case, and where it lands

The borderline is presentation shape. Compare two bullets from the corpus.

`Highlights - Onboarding - Instagram ReAuth.md:52`

> `*   It opens as a bottom sheet over the presentation screen with the page still visible behind it`

`Creator - Settings - Linked Social Media.md`, bullet 8

> `*   Opens with a background on top of the Social Connection Overview sheet rather than as a full-height stacked sheet`

Both name a presentation. Neither carries a number or a token. The second lands as a **keep** and the first as a **strike**, because the second names the alternative it rules out. A developer given only the design could ship the full-height stacked sheet and believe they matched it, so the bullet forecloses a choice the design does not. The first bullet forecloses nothing, because a bottom sheet over a visible page is what the screenshot already shows.

The guard on that exception matters, or it becomes a laundering route. **The alternative has to come from the source, not from the writer.** Appending "rather than a full-page screen" to a description the source never framed as a choice invents a decision nobody took, which is an Accuracy failure under `quality-scoring.md:64` rather than a rescued constraint.

---

## 4. The exact edits

Every quoted "current" text below is the live line as of this review. Line numbers are from the files at review time.

### 4.1 `sk-product-owner/assets/story-template.md`

**Edit A, line 110.**

Current:

> - Requirements hold hard requirements only: the formats, limits, platforms, integrations, compliance rules and performance floors the delivery has to satisfy whatever approach the developer takes. Each group is a bold name, a divider and short `*   ` bullets, one constraint per bullet, stated as a fact or an instruction rather than as a user outcome. Never a `**Checklist**`

Replacement:

> - Requirements hold hard requirements only: the formats, limits, platforms, integrations, compliance rules and performance floors the delivery has to satisfy whatever approach the developer takes. Each group is a bold name, a divider and short `*   ` bullets, one constraint per bullet, stated as a fact or an instruction rather than as a user outcome. Every bullet is a sentence a build can fail, so a bullet that reports what a screen says, shows or contains, naming no value, limit, condition, effect or named flow a build could get wrong, is description and is struck rather than reworded. Never a `**Checklist**`

**Edit B, line 111.**

Current, final sentence:

> Where the source names a change without giving its content, point the constraint at the design that settles it rather than inventing the text or dropping the line

Replacement, appended after that sentence:

> A screen the source describes in prose, or shows only in a screenshot, supplies its copy, its labels and its values, and not its layout, its composition or a paraphrase of what it communicates. Carry the strings verbatim in backticks and let the design link carry the rest.

**Edit C, line 113.**

Current, final sentence:

> Never pad it with outcomes to make it look complete

Replacement:

> Never pad it with outcomes or with screen description to make it look complete. A group named for a screen the source mentioned once holds one bullet, and a group that grew past its source grew by description

### 4.2 `sk-product-owner/references/story-mode.md`

**Edit D, line 116, house grammar.**

Current, the exclusion clause:

> Never a `**Checklist**` sub-block or `- [ ]` items, and never a user outcome dressed as a constraint.

Replacement:

> Never a `**Checklist**` sub-block or `- [ ]` items, never a user outcome dressed as a constraint, and never a description of what a screen says, shows or contains. Every bullet is a sentence a build can fail: it names a value, a limit, a condition, an effect or a named flow a build could get wrong, and a bullet that names none of those is description the design link already carries, struck rather than reworded. A bullet naming a presentation shape is a constraint only where the source itself named the alternative it rules out, because an alternative the writer supplies is an invented decision.

**Edit E, line 75, the verbatim rule.**

Current, final sentence:

> A generalised value is not a shorter requirement, it is a different and false claim, that the change is still unspecified

Replacement, appended:

> This binds copy the source shows as much as copy it types. A sheet whose screenshot reads `We noticed your Instagram isn't linked yet.` has supplied that string, so the bullet quotes it, and It states Instagram is not linked is the same generalisation failure as writing `32px` as updated spacing.

**Edit F, line 78, the unsupplied-change rule.**

Current, final sentence:

> Never invent the string, and never drop the line: an unsupplied value is an open constraint, not an absent one

Replacement, appended:

> What travels is the pointer, not the source sentence rewritten. A source line saying a new sheet explains the situation yields one bullet naming the screen and the design that settles it, never a group of bullets recounting what the sheet says.

**Edit G, line 76, the per-screen grouping rule.**

Current, first sentence:

> Where the source organises its values by screen, surface or component, Requirements mirrors that organisation: one bold-lead group per screen, named as the source names it, holding that screen's values and nothing else.

Replacement:

> Where the source organises its values by screen, surface or component, Requirements mirrors that organisation: one bold-lead group per screen, named as the source names it, holding that screen's values and nothing else. The group holds as many bullets as the screen has supplied values, reuse entries and rules, and never more. A screen heading with one prose line under it is a one-bullet group, and an empty container is never filled from the design.

**Edit H, line 79, the accounting rule.**

Current, first sentence:

> Every line of the source is accounted for, not only the lines under a screen heading.

Replacement:

> Every line of the source is accounted for, not only the lines under a screen heading. Accounted for means the change the line names lands in the draft, never that the line's own wording lands in Requirements. A line that gives a value is accounted for by that value, and a line that names a screen without giving one is accounted for by a single bullet pointing at the design.

**Edit I, line 162, Step 1 intake.**

Appended to the paragraph:

> A screenshot the requester supplies is source material like any other line, and what it supplies is its exact copy, its labels and its values. It does not supply its layout, its composition or a paraphrase of what it communicates, because the design link already carries those and a bullet repeating them fixes nothing a build could get wrong.

**Edit J, Step 4, inserted after line 184.**

New bullet:

> - Reconcile in the other direction as well: every bullet in `## Requirements` traces to a supplied value, a reuse entry, a rule or a design pointer. A bullet that traces to none of those is description, and it is struck rather than reworded

**Edit K, line 380, checklist.**

Current:

> - [ ] Story: `#### **Expected outcomes**` present, and `## Requirements`, if present, holds only hard constraints with no outcomes, no `**Checklist**` and no images?

Replacement:

> - [ ] Story: `#### **Expected outcomes**` present, and `## Requirements`, if present, holds only hard constraints with no outcomes, no screen description, no `**Checklist**` and no images?

**Edit L, checklist, inserted after line 392.**

New entry:

> - [ ] Every Requirements bullet is a sentence a build can fail, with no bullet reporting only what a screen says, shows or contains, and every screen's copy quoted verbatim rather than paraphrased?

**Edit M, line 365, section 8, a stale line this review found.**

Current:

> - [`examples/story/prd-example-simple.md`](../assets/examples/story/prd-example-simple.md): a small Story with one requirement, a flat acceptance-criteria list and no Delivery section, so the artifact ends on Acceptance criteria

`prd-example-simple.md` carries no `## Requirements` section at all. Commit `84bba2e` made the section optional and removed it from that example without updating this line. Replacement:

> - [`examples/story/prd-example-simple.md`](../assets/examples/story/prd-example-simple.md): a small Story with no hard constraint to state, so `## Requirements` is omitted entirely, with a flat acceptance-criteria list and no Delivery section, so the artifact ends on Acceptance criteria

### 4.3 `sk-product-owner/SKILL.md`, one edit

File is 405 lines. This edit replaces one line with one line, so it stays 405, inside the 400 to 600 band.

**Edit N, line 268, ALWAYS rule 9.**

Current:

> 9. Write acceptance criteria as outcomes the user can rely on, few in number and open on the mechanism, growing only with the surfaces a story touches. In a Story, Requirements holds hard constraints only, carries every hard value the source supplied with its value, units and notation intact, mirrors the source's own screen or surface grouping where it has one, names each shared screen's reuse map as a constraint, and is omitted only where the source supplies none. A supplied value never travels into an acceptance criterion instead. Keep Task QA checklist items inside a Task's Requirements.

Replacement:

> 9. Write acceptance criteria as outcomes the user can rely on, few in number and open on the mechanism, growing only with the surfaces a story touches. In a Story, Requirements holds hard constraints only, carries every hard value the source supplied with its value, units and notation intact, mirrors the source's own screen or surface grouping where it has one, names each shared screen's reuse map as a constraint, and is omitted only where the source supplies none. Every Requirements bullet is a sentence a build can fail, so a bullet that reports what a screen says, shows or contains, naming no value, limit, condition, effect or named flow a build could get wrong, is description and is struck rather than reworded, and copy a screenshot supplies is quoted verbatim in backticks or dropped. A supplied value never travels into an acceptance criterion instead. Keep Task QA checklist items inside a Task's Requirements.

One concern, stated and then set aside per the one-edit constraint. `SKILL.md:388`, the Blocking Gates entry, restates the Story shape as "one constraint per bullet carrying its supplied value verbatim, each shared screen's reuse map named as a constraint, no outcomes, no checklist and no images". After edit N that sentence describes a contract narrower than the one rule 9 now states, so the gate roster and the ALWAYS rule disagree on whether description is permitted. If a second edit to `SKILL.md` is authorized, the fix is to insert `no screen description` into that list directly after `no outcomes`.

### 4.4 `claude project/Custom Instructions.md`, one edit

**Edit O, line 130, rule 10.** This is the Claude Project's verbatim counterpart of `SKILL.md` ALWAYS rule 9, and it takes the same insertion at the same point.

Current:

> 10. Write acceptance criteria as outcomes the user can rely on, few in number and open on the mechanism, growing only with the surfaces a story touches. In a Story, Requirements holds hard constraints only, carries every hard value the source supplied with its value, units and notation intact, mirrors the source's own screen or surface grouping where it has one, names each shared screen's reuse map as a constraint, and is omitted only where the source supplies none. A supplied value never travels into an acceptance criterion instead. Keep the Task QA checklist inside a Task's Requirements.

Replacement:

> 10. Write acceptance criteria as outcomes the user can rely on, few in number and open on the mechanism, growing only with the surfaces a story touches. In a Story, Requirements holds hard constraints only, carries every hard value the source supplied with its value, units and notation intact, mirrors the source's own screen or surface grouping where it has one, names each shared screen's reuse map as a constraint, and is omitted only where the source supplies none. Every Requirements bullet is a sentence a build can fail, so a bullet that reports what a screen says, shows or contains, naming no value, limit, condition, effect or named flow a build could get wrong, is description and is struck rather than reworded, and copy a screenshot supplies is quoted verbatim in backticks or dropped. A supplied value never travels into an acceptance criterion instead. Keep the Task QA checklist inside a Task's Requirements.

The same concern applies. `Custom Instructions.md:214` carries the long house-format paragraph whose Story clause ends "no outcomes, no build checklist and no images", and it stays narrower than rule 10 until a second edit is authorized.

### 4.5 `sk-product-owner/references/quality-scoring.md`

**Edit P, line 100, the Story paragraph.**

Current, two sentences:

> Two supplied-value failures score here rather than reading as style.

and the paragraph's close:

> A value carried into an acceptance criterion instead costs Clarity, since the criterion is no longer testable as an outcome.

Replacement, the count corrected and one failure added at the end:

> Three supplied-value failures score here rather than reading as style.

and:

> A value carried into an acceptance criterion instead costs Clarity, since the criterion is no longer testable as an outcome. A Requirements bullet that reports what a screen says, shows or contains, naming no value, limit, condition, effect or named flow, is a Relevance failure at 6, and it is scored per bullet rather than per section, because four such bullets sitting beside twelve real constraints leave the section as a whole still earning its place and the section-level reconstruction test scores it a pass.

That last clause is the substantive repair. Without it the rubric keeps reading Relevance at section granularity, which is exactly why the ReAuth story cleared its floors.

### 4.6 Claude Project knowledge files

Three knowledge files teach the shape and each is a derived copy of a skill source, with frontmatter stripped and an H1 plus description line prepended. They are resynced rather than hand-edited:

- `claude project/knowledge/Product Owner - Assets - Story Template - v0.100.md` carries edits A, B and C
- `claude project/knowledge/Product Owner - Templates - Story Mode - v0.400.md` carries edits D through M
- `claude project/knowledge/Product Owner - Rules - Quality Scoring - v0.100.md` carries edit P

The brief forbids running the sync compiler, so the resync is a follow-up step, not part of this proposal. `SKILL.md` is not mirrored, per `SKILL.md:404`, so edit N has no knowledge-file counterpart.

---

## 5. Do the worked examples model the wrong thing

**No line in any of the five examples models description.** A scan of all 93 Requirements bullets in the five examples, the six exported PRDs and the knowledge mirrors found zero bullets that fail the section 3 test. Every bullet in `prd-example-medium.md`, `prd-example-complex.md` and `prd-example-complete.md` carries a value, a rule or an expression in backticks.

The defect is absence, not error, and it is directly upstream of the bug.

**None of the five examples shows a Requirements section grouped per screen.** The three that carry the section group by data concern: `**Access windows**`, `**Redemption limits**`, `**Instant revoke**` in `prd-example-complete.md`, `**Avatar image**`, `**Display name**`, `**Email change**` in `prd-example-medium.md`, `**Release limits**` and `**Pipeline coverage**` in `prd-example-complex.md`. Every one of the sixteen stories groups per screen. The per-screen shape was introduced by commit `1b47426` and never got an exemplar, so a model writing its first per-screen group has nothing to imitate and falls back on describing the screen.

Two lines to change, and one file to add:

1. `story-mode.md:365`, the stale simple-example description, is edit M above. It matters here as well as on its own, because a model looking for the minimal Requirements shape is pointed at an example that has none while being told it has one requirement
2. `story-mode.md`, section 8, add a sixth entry naming a new per-screen example
3. Add `sk-product-owner/assets/examples/story/prd-example-screens.md`, a Story whose Requirements is grouped per screen, carrying one screen with several supplied values, one screen with a `Shared with:` reuse map, and one screen the source names with no content supplied, so the single design-pointer bullet is modelled explicitly

Converting `prd-example-medium.md` to per-screen grouping was considered and rejected. It is the only example of a Story whose constraints are data rules rather than screen values, and losing it would trade one gap for another.

---

## 6. Can the format gate check this mechanically

**Partly, and the honest answer has two halves.** A narrow check on one subclass ships with zero misfires and is given below. A general check on the description class does not exist, and I am not proposing a heuristic for it, because I measured two and both are unusable.

### 6.1 What does not work, with numbers

Both candidates were scored against the 221 hand-classified bullets in the corpus.

| Candidate check | True positives | False positives | Precision | Recall |
| --- | --- | --- | --- | --- |
| Bullet has no backtick and no digit | 19 | 109 | 0.15 | 1.00 |
| Bullet has any display or saying verb and no backtick | 11 | 18 | 0.38 | 0.58 |

The first is the obvious "no supplied value" test and it rejects 109 legitimate constraints, among them `Closing without confirming never writes a value`, `Save stays inactive until the creator changes something`, `The picker returns the selection to the calling screen, or nothing when the creator backs out` and `The Figma mocks are a demonstration of intent, not the UI to build against`. The second still rejects `The state has no navigation bar and no access to the deal feed or the profile` and `The review shows no platform stats row`. `run_fixtures.sh` states the standard these fail:

> The silent half matters more: a gate that fires on a quoted mention, a single hedge or an informative lead-in gets switched off within a week, and then it guards nothing

Neither should ship. The reason is not tuning. A constraint and a description are the same sentence shape in English, and what separates them is whether the design already settles the claim, which is not in the bullet's text.

### 6.2 What does work

One subclass is mechanically separable: a bullet that reports what a screen says while quoting none of the copy. The third-person verb forms `explains`, `states`, `tells` and `informs` inside a Requirements section, in a bullet holding no backticked value, are description by construction, because a bullet saying a screen states something without saying what it states carries no value by definition.

Measured on the corpus: 3 true positives, 0 false positives, precision 1.00. It catches `:51`, `:53` and `:54` of the ReAuth story, three of the four bullets the owner named. Scanned across the 93 Requirements bullets in the worked examples, the six exported PRDs and the Claude Project knowledge mirrors, it fires zero times. The check was written and run end to end against all of that before being proposed here.

Recall against the full description class is 0.16, so this is a copy-paraphrase check and not a description check. It should be named and documented as such, or the next reader will assume the gate covers the class and stop reading Requirements.

Code, placed inside the existing `if (lintingArtifacts) {` block in `benchmark/format/validate-output-format.cjs`, directly after the `0c` Delivery placeholder check at line 686:

```js
    // 0d. a Requirements bullet saying a screen explains, states, tells or
    // informs, while quoting none of the copy, reports that a string exists
    // without carrying the string. The design link already holds what the
    // screen says, so the bullet fixes nothing a build could get wrong, and
    // the repair is to quote the copy in backticks or drop the bullet.
    // Deliberately narrow. Third-person verb forms only, so the noun "state"
    // and the plural "states" never match, and any backtick in the bullet is
    // an exemption, because a bullet that quotes the copy has carried the
    // value the rule asks for. Measured at zero false positives across the
    // 221 Requirements bullets in Story Drafts and the 93 in the worked
    // examples, exports and knowledge mirrors. This catches one subclass. The
    // wider "bullet describes a screen" class is not mechanically separable:
    // the two broad heuristics tried scored 0.15 and 0.38 precision on the
    // same corpus, so Requirements still needs a reader.
    const requirementsIndex = lines.findIndex((line) => line.trim() === '## Requirements');
    if (requirementsIndex >= 0) {
      const nextSection = lines.findIndex((line, i) => i > requirementsIndex && /^## /.test(line));
      const last = nextSection === -1 ? lines.length : nextSection;
      for (let i = requirementsIndex + 1; i < last; i += 1) {
        const bullet = lines[i].match(/^\*   (.*\S)\s*$/);
        if (!bullet || bullet[1].includes('`')) continue;
        if (!/\b(?:explains|states|tells|informs)\b/.test(bullet[1])) continue;
        errors.push(
          `${relative}:${i + 1}: Requirements bullet reports what a screen says without quoting the copy`,
        );
      }
    }
```

### 6.3 The fixture pair

`benchmark/format/fixtures/requirements-narration-violation.md`:

```markdown
# Creator - Onboarding - Instagram ReAuth

## Requirements
* * *
**Initial Instagram Sheet**
* * *
*   It states Instagram is not linked
*   It explains that quick connect now works without logging in again
*   It carries the one action `Link Instagram`
* * *
##   
```

`benchmark/format/fixtures/requirements-narration-exempt.md`:

```markdown
# Creator - Onboarding - Instagram ReAuth

## Requirements
* * *
**Initial Instagram Sheet**
* * *
*   It states `We noticed your Instagram isn't linked yet.`
*   The state has no navigation bar and no access to the deal feed
*   Confirming empties the set, and the surface returns to its first-time empty state
*   A new sheet, laid out as set in the Highlights - Onboarding Flow design
* * *
##   
```

The exempt fixture carries the three shapes that would break a looser check: the same verb with the copy quoted, the noun `state`, and a second noun `state` at the end of a behavioral constraint. Both fixtures were built and run against the check as written. The violation fixture produces exactly two findings, on its first two bullets. The exempt fixture produces none.

`benchmark/format/run_fixtures.sh` entries, added beside the Delivery placeholder pair:

```bash
# A Requirements bullet saying a screen states something, without saying what,
# carries no value. The exempt half matters more here than anywhere: the noun
# "state" appears in a dozen legitimate constraints, so a check that cannot
# tell it from the verb would fire on half the corpus and be switched off.
check "requirements narration fires" 1 "requirements-narration-violation.md:7: Requirements bullet reports what a screen says" "" \
  "${FIXTURES}/requirements-narration-violation.md"
check "requirements narration fires on the second bullet" 1 "requirements-narration-violation.md:8: Requirements bullet reports what a screen says" "" \
  "${FIXTURES}/requirements-narration-violation.md"
check "quoted copy and the noun state stay silent" 0 "validation passed" "reports what a screen says" \
  "${FIXTURES}/requirements-narration-exempt.md"
```

### 6.4 The zero-risk half

The gate already pins two Story contracts by substring at `validate-output-format.cjs:938` and `:941`, so the same treatment fits the new rule and costs nothing:

```js
  if (!storyMode.includes('Every bullet is a sentence a build can fail')) {
    errors.push('sk-product-owner/references/story-mode.md: missing the build-can-fail contract for Requirements bullets');
  }
```

This does not catch a bad artifact. It catches the rule going missing from the instruction surface, which is what `84bba2e` through `acd1aa1` show happening repeatedly to this section.

---

## 7. What a story does with the screen description it drops

**It is dropped entirely, and the References design link stands in its place.** No other section takes it. The exception is copy a developer has to ship, which is a value and goes back into Requirements in backticks.

The three sections a reader might expect to catch it all already refuse it, by rules that are live today:

- **Solution.** `story-mode.md:113` says it "restates neither the constraints in Requirements nor the outcomes in Acceptance criteria, and names no mechanism", and `story-template.md:109` adds "If a Solution bullet could be pasted into Requirements or a criterion unchanged, it belongs there instead". A screen inventory is a mechanism preview
- **Acceptance criteria.** `story-mode.md:117` says a criterion "states what the user can rely on once the work ships and the quality it has to have, from the product's point of view, and leaves the mechanism to the developer". The ReAuth story already broke this. Criterion 3's Then and And clauses are the same four descriptions moved down the page, and neither the criterion nor the requirement is testable as an outcome
- **About.** It is narrative scope and promise, not a screen inventory

**References is where the description already lives.** The ReAuth story carries the link under `Flows`:

```
*   [Highlights - Onboarding Flow](https://www.figma.com/design/MKARl3Qh6qLJfvHFPQxACT/%E2%80%A2-App---Creator?node-id=2652-176256&t=XySRpynK1Wnx3oMd-1)
```

That link is the authority for what the sheet shows, what sits behind it and how it is composed. Four bullets restating it in prose add a second, staler copy of the same information, and the first time the design moves the story becomes wrong in a way nobody will notice.

Applied to the group in the brief, five bullets become two:

```markdown
**Initial Instagram Sheet**
* * *
*   A new sheet, laid out as set in the Highlights - Onboarding Flow design
*   It carries the one action `Link Instagram`
```

If the sheet's copy is settled rather than still moving, the two strings are values and the group is four bullets:

```markdown
**Initial Instagram Sheet**
* * *
*   A new sheet, laid out as set in the Highlights - Onboarding Flow design
*   The heading reads `Link Instagram to use it for your highlight reel`
*   The body opens `We noticed your Instagram isn't linked yet.` and names quick connect as `You can now quickly connect Instagram without logging in again`
*   It carries the one action `Link Instagram`
```

Either version loses nothing. The first drops four bullets because the design link settles all four. The second keeps the copy because a developer has to ship those strings and cannot derive them, which is the distinction the whole rule turns on.

The corpus-wide consequence is worth stating plainly. `Content Gallery - Media - Change Tabs on Scroll` is a pure styling story whose source supplies no token values, so under this rule its Requirements section holds two bullets rather than seven, and one could argue it should be omitted altogether under `story-mode.md:116`, "The section is optional only where there is nothing hard to hold". That is the correct outcome, not a regression. A styling story whose values live only in Figma has a design link and no hard constraints, and a Requirements section padded to look complete is the thing `story-template.md:113` already forbids.
