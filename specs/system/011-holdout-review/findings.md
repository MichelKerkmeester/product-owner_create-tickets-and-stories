# Held-out review: Creator - Deals - Saved Deals Shelf

Read-only. Nothing outside `AI Systems/Product Owner/specs/011-holdout-review/` was touched, no sync compiler ran, nothing was committed. The format gate and its fixture suite were run at baseline and the fixtures pass 18/18.

What was run:

- `node benchmark/format/validate-output-format.cjs` against the artifact, and against all seventeen stories under `export/Story Drafts/` for comparison
- `bash benchmark/format/run_fixtures.sh` at baseline
- a Python pass over the 261 Requirements bullets in those seventeen stories, plus the 67 in the worked examples, the Claude Project knowledge mirrors and the numbered exports, to measure the phrase-list check proposed in `AI Systems/Product Owner/specs/010-requirements-bloat/findings.md` section 6.2

Two facts frame everything below.

**The artifact is the only one of seventeen that fails the format gate.** It exits 1 on `:44`. The other sixteen exit 0.

**The ReAuth story did not prove the rule generalises.** `story-mode.md:105-108` prints a four-line Requirements group as the worked example of what a described screen becomes. The Initial Instagram Sheet group in `export/Story Drafts/Highlights - Onboarding - Instagram ReAuth/Highlights - Onboarding - Instagram ReAuth.md` is byte-identical to those four lines, verified by `diff`. The rules print the answer for that one story, and the story reproduces it. This holdout is the first source where the model had to apply the rule rather than copy the exemplar, and the rule did not hold.

---

## 1. Trap-by-trap verdict

Seven of the eight trap families held. One failed. Two of the seven held with a defect worth naming.

| Trap | Source | Artifact | Verdict |
| --- | --- | --- | --- |
| `24px` card edge | `context.md:16` | `:29` | held, backticked |
| `44x44` tap target | `context.md:18` | `:31` | held, backticked |
| `2` columns | `context.md:28` | `:40` | held, backticked |
| `h3` heading | `context.md:29` | `:41` | held, backticked |
| `24px` heading-to-grid spacing | `context.md:30` | `:42` | held, backticked |
| `50` cap | `context.md:32` | `:44` | value held, bullet fails the gate |
| second menu item | `context.md:27` | `:39` | value held, not backticked |
| `Saved to your shelf` | `context.md:19` | `:33` | held |
| `Nothing saved yet` | `context.md:40` | `:51` | held |
| `Browse deals` | `context.md:42` | `:53` | held |
| empty-state body, paraphrased | `context.md:41` | `:52` | **failed**, carried verbatim from the source |
| reuse map, deal card | `context.md:21-24` | `:35` | held as a `Shared with:` constraint |
| reuse map, shelf | `context.md:34-36` | `:46` | held as a `Shared with:` constraint |
| Deal expiry cross-ticket dependency | `context.md:7`, `:33` | `:17`, `:45` | carried, not invented, but weakened |
| Highlights delete warning pattern | `context.md:47` | `:59` | held, points rather than restates |
| push notifications out of scope | `context.md:49-50` | `:61-63` | carried, Delivery correctly stayed absent, bullet carries scope language |

One source change was dropped outright and no trap covers it. `context.md:12` reads `Updated bookmark icon, tooltip copy and toast`. The toast landed at `:33` and the tooltip landed at `:32` as a design pointer. The updated bookmark icon landed nowhere. `:29` states where the icon sits, not that it changes. Under `story-mode.md:195` a supplied change that appears in neither Requirements nor the delivery response is a defect rather than an editorial judgement.

---

## 2. The one surviving paraphrase

### 2.1 Why the rule failed on it

`context.md:41` reads `Body explains that bookmarking a deal keeps it here`. `:52` of the artifact reads `*   Body explains that bookmarking a deal keeps it here`. The source sentence survived into the artifact unchanged, including its verb.

Four mechanisms let it through, in order of force.

**The keep-list rescued it.** `story-mode.md:149` states the positive test as an enumeration: a bullet stays when it "names a value, a limit, a condition, an effect or a named flow a build could get wrong". Bookmarking a deal keeping it on the shelf reads as an effect. The rule's own escape hatch fits the bullet, which is not true of `It states Instagram is not linked`, where nothing on the list applies. A model that runs the enumeration honestly keeps this bullet.

**The subject moved from the screen to a slot.** `story-mode.md:149` forbids "a description of what a screen says, shows or contains", and the worked example at `:98` uses `It says Instagram is not linked`, where the subject is the sheet. Here the subject is `Body`, a named component slot. A bullet about a named slot reads as a constraint on that slot rather than as a report about a screen. The prohibition names the wrong grammatical subject.

**The group did not look like the exemplar.** The worked example at `:94-117` shows a screen heading with nothing under it, filled from the design. The Shelf empty state group holds three legitimate bullets already, one layout reuse and two exact strings. A group that carries supplied values does not pattern-match the empty-container case the rules illustrate.

**The exemplar is one story deep.** As established above, the ReAuth group in the corpus is a byte copy of the rules. There is no second worked example, and there is no per-screen worked example in `assets/examples/story/` at all, which `AI Systems/Product Owner/specs/010-requirements-bloat/findings.md` section 5 already flagged and which was never added.

### 2.2 The smallest change that catches it

**The answer is a named phrase list, not a principle.** Three attempts at a principle have now been made. `ba2bec3` stated it in prose, `095479a` illustrated it, and the holdout reproduced the failure with a different subject and the same verb. A prose principle that has to decide whether a sentence "names an effect" cannot separate `Body explains that bookmarking a deal keeps it here` from `Unsaving from the card shows no toast`, because both name an effect and only one carries a value.

The list is already written and already measured, in `AI Systems/Product Owner/specs/010-requirements-bloat/findings.md` section 6.2, and it was never implemented.

**The list.** In a `## Requirements` bullet holding no backtick, these four third-person verb forms are description by construction:

- `explains`
- `states`
- `tells`
- `informs`

The exemption is any backtick anywhere in the bullet, because a bullet that quotes the copy has carried the value the rule asks for. Third-person forms only, so the noun `state` and the plural noun `states` never match.

**Re-measured today, on a corpus that did not exist when 060 ran.**

| Corpus | Bullets | Hits |
| --- | --- | --- |
| Requirements bullets across all seventeen `export/Story Drafts/` stories | 261 | 1 |
| Requirements bullets in the five worked examples, the knowledge mirrors and the numbered exports | 67 | 0 |

The single hit is `Creator - Deals - Saved Deals Shelf.md:52`. Precision 1.00 against a corpus of 328 bullets, and the one thing it fires on is the one bullet under review.

**Widening the list misfires, and the numbers say so.** Adding `describes`, `says`, `shows`, `indicates`, `communicates`, `conveys`, `mentions` and `reads as` takes the same corpus from 1 hit to 17. Sixteen of the seventeen are legitimate constraints, among them `Each video shows its duration as an overlay`, `The review shows no platform stats row`, `The control bar shows rotate left, crop and rotate right, in that order` and `Unsaving from the card shows no toast`. The list stays at four verbs.

**Recall is low and must be stated.** This is a copy-paraphrase check, not a description check. It catches the bullet that reports a screen says something without saying what. It does not catch a layout inventory. Name it that way in the code comment or the next reader will assume the gate covers the class.

The prose change is secondary and follows the same list. See P1-5 below.

---

## 3. The out-of-scope line

`context.md:49-50` reads `#### Notifications` and `No push when a saved deal is about to expire, decided out of scope for now`. The artifact put it at `:61-63` as a `**Notifications**` Requirements group holding one bullet.

**It belongs in Requirements, as a constraint. Not a forced Delivery section, and not dropped.** Three reasons, each against a live rule.

**No Delivery forcing fired.** `story-mode.md:154` names exactly three openers: the requester asks, a requirement carries an `**Open:**` line, or an undated constraint outside the team's control exists. The requester asked for no delivery view. No `**Open:**` line exists. The Deal expiry ticket is work another internal team owes, which `story-mode.md:156` states explicitly is "ordinary scheduling and belongs in Estimation", not an external dependency. Opening Delivery here produces three `TBD...` slots and one No-go, which `:154` calls worse than an absent section.

**`story-mode.md:155` does not fire on a source line.** Its trigger is "a request naming the section or any of its parts", and the parenthetical list that includes `out of scope` qualifies the request, not the source. The source is material, not the ask. The model read this correctly, and the rule is ambiguous enough that it could have read it either way. See P2-4.

**A prohibition is a constraint a build can fail.** A developer can ship an expiry push. The corpus already treats negative constraints as house-legitimate: `Onboarding - Not Approved.md` carries `The state has no navigation bar and no access to the deal feed or the profile`, and `AI Systems/Product Owner/specs/010-requirements-bloat/findings.md` section 6.1 lists that bullet among the legitimate constraints a looser check would wrongly reject. `Creator - Onboarding v2 - Complete Profile.md:46` carries `The review shows no platform stats row`. Same shape.

**What is wrong with the bullet as written.** The trailing clause `out of scope for this delivery` is scope language, and scope exclusions are what the No-gos slot owns. With no Delivery section there is no No-gos slot, so the clause has nowhere to be and it names nothing a build can fail. Strike the clause, keep the constraint, keep the group name, because `story-mode.md:76` requires mirroring the source's own heading. See P2-2.

Dropping the line is not available. `story-mode.md:195` makes a supplied entry that appears in neither Requirements nor the delivery response a defect.

---

## 4. Every other section, judged

### H1

`# Creator - Deals - Saved Deals Shelf`. Correct. Persona, area, feature, per `story-mode.md:168`. No `PRD -` prefix, no short code. The source's own title is `Saved deals shelf` and the folder name supplied the first two segments, which is the intended derivation.

### The story preamble

`:3-5`. Verbatim, plain italic lines, directly under the title divider. Correct per `story-mode.md:175-181`.

### About

`:9`. Two sentences, scope then framing. Correct shape. Two notes:

- the second sentence, "so most of the build is assembly rather than new design", is `context.md:5` carried near-verbatim. `story-mode.md:80` says source prose is material and never copy. It is also a sizing claim, which is Estimation territory
- the section close is missing. `:22` is a bullet and `:23` is the `##   ` spacer with no `* * *` between them. `story-mode.md:151` requires a `* * *` directly above every `##   ` spacer. See P1-2

### Problem

`:13`. Correct. One sentence, states what breaks today, matches `context.md:3` without carrying its hedging or its first-person framing. `story-mode.md:80` held here.

### Solution

**Fails.** `:17` is a preview of Requirements, not a decision. Five clauses map one-to-one onto Requirements bullets that sit fifteen lines below:

| Solution clause at `:17` | Requirements bullet it restates |
| --- | --- |
| carries across the deal feed, deal detail and brand profile deal list | `:35` |
| reachable from the profile menu | `:39` |
| ordered newest first | `:43` |
| an unsave confirmation that defaults to keeping the deal | `:58` |
| stays visible on the shelf, dimmed, once the Deal expiry ticket defines that state | `:45` |

`story-mode.md:147` says Solution "restates neither the constraints in Requirements nor the outcomes in Acceptance criteria, and names no mechanism". `story-template.md:109` gives the test: "If a Solution bullet could be pasted into Requirements or a criterion unchanged, it belongs there instead". Five of them could be. The opening clause, "A bookmark icon on the deal card saves a deal without opening it", also names the mechanism. Checklist item `story-mode.md:413` asks precisely this and it was not run or not applied. See P1-1.

### Expected outcomes

`:21-22`. Correct. Two bullets, both results for the user, neither ends in a full stop, neither restates a constraint.

### References

Absent, and correctly absent, because the source supplies no links and `story-template.md:66` says omit the section when none are supplied.

The consequence is worth stating. `:32` reads `Tooltip copy is updated per the design`, which is the design-pointer form `story-mode.md:78` demands, but with no References block the pointer resolves to nothing. The same will be true of any repair to `:52` that points at a design. The rules require a pointer and forbid inventing a link, so a source with no links produces pointers a developer cannot follow. See P2-6.

### Requirements

Covered in sections 1 to 3 above. Grouping mirrors the source's five headings, `story-mode.md:76` held. Bullet counts track supplied values with no padding, `story-template.md:113` held. Both reuse maps landed as constraints in their own groups, `story-mode.md:77` and checklist `:429` held.

### Acceptance criteria

Six criteria in three surface groups. Judged against `story-mode.md:150`.

**No criterion holds a value that Requirements should own. That trap held cleanly, and it is the strongest result in the artifact.** Each of the six leaves its value behind:

- `:87` says "ordered newest saved first" and leaves the sort rule where `:43` states it
- `:95` says "with an action to browse deals" in lowercase prose, leaving `Browse deals` backticked at `:53`
- `:109` says "has already reached the saved deals limit" and leaves `50` at `:44`
- `:77` says "a toast confirms it" and leaves `Saved to your shelf` at `:33`
- `:121` says "keep is the default action" and leaves the button pair at `:58`
- `:103` says "shown dimmed" and leaves the dimmed-expiry rule at `:45`

Applying the mechanical test at `story-mode.md:150`, no criterion would need editing if a design token changed.

**The count is defensible.** The story touches four surfaces and one limit edge. Six criteria across three groups sits inside "the number of surfaces and considerations the story touches". The group names are actions rather than surfaces, which matches the `#### Upload` and `#### Playback` example at `story-template.md:117`.

**Criterion 4 asserts a behaviour the story says is not defined yet.** `:99-103` states that an expired saved deal remains in the grid, shown dimmed, as a shippable outcome. `:45` makes that same behaviour conditional on the Deal expiry ticket, and `context.md:7` says this story depends on that ticket landing first. `story-mode.md:74` bans an acceptance criterion asserting an open part, and the checklist repeats it at `:419`. No `**Open:**` line was written, so the ban technically does not fire, which is the gap. See P2-3.

**Section close is correct.** `:124` carries the `* * *` above the `:125` spacer, and that spacer is the file's last line, per `story-mode.md:151`.

### Delivery

Absent, and correctly absent. No requester ask, no `**Open:**` line, no undated external constraint. Under `story-mode.md:154` and checklist `:424` this is the right output, and `quality-scoring.md:102` states that scoring an absent Delivery as a Completeness miss is a rubric error.

---

## 5. The output path

**The artifact should be at `AI Systems/Product Owner/export/006 - PRD-saved-deals-shelf.md`.**

Four files state the contract and all four agree:

- `sk-product-owner/SKILL.md:207`, `New PRD Story: export/[###] - PRD-[description].md`
- `sk-product-owner/references/story-mode.md:25`, the frontmatter Output Path
- `sk-product-owner/references/story-mode.md:369-375`, section 7 Export Contract
- `sk-product-owner/assets/story-template.md:22`, the asset's Output Path

`export/Story Drafts/{name}/{name}.md` was the Story Draft lane and commit `e7819e4` deleted it along with the kind, the `$draft` and `$dr` tokens and the promotion rule. Nothing in the current rule set mentions `Story Drafts`. Confirmed by grep across `AI Systems/`, which returns zero hits outside the export tree itself. The existing sixteen stories sit at that path because `AI Systems/Product Owner/specs/009-story-drafts-rewrite/run.sh:17` instructed a one-off in-place overwrite, which was a run instruction and never a rule.

`006` is the next free number in the export directory, whose highest current entry is `005 - PRD-creator-wallet-balance-instant-payout.md`.

**A second problem sits underneath the path, and it is worse.** `Product Context/z — Product Owner` is a symlink to `AI Systems/Product Owner/export`, verified by `readlink`. The source and the export are the same directory. `Product Context/z — Product Owner/Story Drafts/Creator - Deals - Saved Deals Shelf/Creator - Deals - Saved Deals Shelf.md` and the export copy are byte-identical because they are one file. Two consequences:

- the artifact is now sitting beside its own source, so a rerun reading that folder sees the answer
- `.gitignore:68` masks `**/export/*`, so both the held-out source and the artifact are untracked

See P1-3 and section 7.

---

## 6. Redundant, contradictory or unreachable after the four Requirements changes

**Contradictory, and it produced a defect in this artifact.** `story-template.md:71-73` prints the scaffold ending

```
Lifecycle
*   [{link}]({url})
##   
```

with no `* * *` above the spacer, while `story-mode.md:151` requires one above every `##   `. The scaffold is what a new Story is copied from, so it teaches the omission. Measured across the seventeen stories, four carry the defect: this artifact, `Creator - Onboarding - Social Relink Flow`, `Creator - Onboarding v2 - Complete Profile` and `Onboarding - Birthday`. The gate sanctions the divider where it appears but never requires it, so nothing catches this. See P1-2.

**Redundant, with a stated authority to defer to.** `story-mode.md:20` says "Everything the shapes share lives here, so a rule has one authority rather than two copies that drift apart". After `ba2bec3`, `story-template.md:110-113` restates the Requirements contract from `story-mode.md:75-79` and `:149` in near-identical words across four bullets. That is the exact drift risk the authority sentence names. Cut the duplication down to a pointer. See P3-3.

**Contradictory in effect.** `story-mode.md:78` still says "never drop the line", and `:149` says a description bullet "is struck rather than reworded". `:79` resolves it by redefining accounted for, but a model reading `:78` alone finds an absolute instruction to keep the line, which is the older and more repeated one. `095479a`'s own commit message names this ordering effect as the reason the rerun failed. The word `line` is doing the damage. See P1-5.

**Over-broad after the four changes.** `story-mode.md:79` says a change stated above the first heading "gets its own bold-lead group named for the surface it changes, and it is never folded into a neighbouring screen". `context.md:12-13` is a preamble summary, `Updated bookmark icon, tooltip copy and toast`, immediately followed by `+ Screen updates below`, and its three changes all belong to the deal card the next heading names. Obeying `:79` literally produces a duplicate group holding the same three changes as the group below it, which `:76` forbids in the same breath ("never more"). The artifact folded them, which was the right call and a rule violation at the same time. See P3-4.

**Stale, and `AI Systems/Product Owner/specs/010-requirements-bloat/findings.md` already flagged it as edit M, which was never applied.** `story-mode.md:399` describes `prd-example-simple.md` as "a small Story with one requirement". That file carries no `## Requirements` section at all, verified by grep. A model looking for the minimal Requirements shape is pointed at an example that has none. See P2-5.

**Typo, unreachable as written.** `story-mode.md:150` reads "never with its size or the number of requirements keep." The trailing `keep` is a fragment left from an edit.

**Not redundant, and worth stating so nobody cuts it.** `quality-scoring.md:100` now scores a description bullet per bullet rather than per section, which is the repair that stops four bad bullets from hiding behind twelve good ones. It is live and correct. Leave it.

---

## 7. Keeping the source as a permanent fixture

**Yes. It is the only source in the repository the skill has never seen, and it has already earned its keep by failing a rule that two commits claimed to have fixed.** The ReAuth byte-identity finding above is the argument: every other source in the corpus has either been written from, or is printed inside the rules, so no rule change can be tested against them honestly.

**Where it should live.** `AI Systems/Product Owner/benchmark/holdout/creator-deals-saved-deals-shelf/`, holding:

- `context.md`, the source unchanged
- `traps.md`, the eight trap families and the expected verdict per trap, in the shape of section 1 above
- `run.sh`, a runner mirroring `AI Systems/Product Owner/specs/011-holdout-review/run.sh`

`benchmark/` is git-tracked, verified with `git ls-files`. The current location is not, because `.gitignore:68` masks the whole export tree. Moving it out of the export tree also breaks the symlink coupling that put the artifact beside its own source.

**What should reference it, and what must not.** The reference has to sit somewhere a rule change is visible from and a runtime load is not.

- reference it from `AI Systems/Product Owner/benchmark/holdout/README.md` and from `AI Systems/Product Owner/README.md`. Neither is on any load path, verified by grep against `SKILL.md` and `AGENTS.md`
- add a mechanical pin in `benchmark/format/validate-output-format.cjs` beside the four existing `storyMode.includes` pins at `:932-941`, so deleting the Requirements contract from the instruction surface fails the gate without needing a model run
- do **not** reference it from `sk-product-owner/**`, `claude project/**` or `AGENTS.md`. Those load into the model's context. `SKILL.md:54` names `benchmark/router/` for exactly this reason, and the consequence is that the router fixtures are not held out. A holdout named in a loaded file is burned on the next run
- do **not** leave it under `Product Context/z — Product Owner/`, which resolves into the export tree

**One rule to add with it.** The Requirements contract is now four files deep and has been rewritten three times in two days. Any change to `story-mode.md:75-79`, `story-mode.md:149`, or `story-template.md:110-113` should re-run the holdout before it lands. That belongs in `benchmark/holdout/README.md`, not in a loaded file.

---

## 8. Ranked changes

### P0

**P0-1. The artifact fails the format gate.**

- File: `AI Systems/Product Owner/export/Story Drafts/Creator - Deals - Saved Deals Shelf/Creator - Deals - Saved Deals Shelf.md`, line 44
- Current: `*   Holds at most \`50\` saved deals; saving beyond that replaces nothing and shows an error`
- Replacement: `*   Holds at most \`50\` saved deals, and saving beyond that replaces nothing and shows an error`
- Evidence: `node benchmark/format/validate-output-format.cjs` exits 1 with `:44: prose semicolon (HVR bans it, use two sentences)`. The other sixteen stories exit 0. The source at `context.md:32` uses a comma, so the semicolon was introduced by the model

**P0-2. The surviving paraphrase.**

- File: same artifact, line 52
- Current: `*   Body explains that bookmarking a deal keeps it here`
- Replacement: `*   Body copy follows the Highlights empty state design`
- Rationale: this is the pointer form `story-mode.md:78` requires, and it matches `:59` of the same artifact, `Copy follows the Highlights delete warning pattern`, which is already a legitimate pointer in the same file. A plain strike is the alternative, and it returns as a quoted bullet the day the source supplies the string

**P0-3. Ship the phrase-list check that was specified and never implemented.**

- File: `AI Systems/Product Owner/benchmark/format/validate-output-format.cjs`, inside the `if (lintingArtifacts) {` block, directly after the `0c` Delivery placeholder check
- Current: absent
- Replacement: the `0d` block given verbatim in `AI Systems/Product Owner/specs/010-requirements-bloat/findings.md` section 6.2, with its two fixtures from section 6.3 and its three `run_fixtures.sh` entries
- Evidence: re-measured today at 1 hit across 261 Requirements bullets in the seventeen stories and 0 across the 67 in examples, mirrors and numbered exports. The single hit is the bullet in P0-2. Precision 1.00 on 328 bullets
- Name it a copy-paraphrase check in the comment, not a description check. Recall against the wider class is 0.16

### P1

**P1-1. Solution is a preview of Requirements.**

- File: same artifact, line 17
- Current: the whole paragraph, whose five clauses are tabulated in section 4 above
- Replacement: `A creator can bookmark a deal wherever they meet it, and every bookmark collects in one place on their profile that they can trust to still hold what they put there. The shelf reuses the profile media grid and the Highlights empty state rather than introducing new surfaces, because the value here is the round trip back to a deal and not a new way of looking at one.`
- Rule: `story-mode.md:147`, `story-template.md:109`, checklist `story-mode.md:413`

**P1-2. The template scaffold omits the About section close, and four of seventeen stories inherit the defect.**

- File: `AI Systems/Product Owner/sk-product-owner/assets/story-template.md`, between lines 72 and 73
- Current:
  ```
  *   [{link}]({url})
  ##   
  ```
- Replacement:
  ```
  *   [{link}]({url})
  * * *
  ##   
  ```
- And in the artifact, `AI Systems/Product Owner/export/Story Drafts/Creator - Deals - Saved Deals Shelf/Creator - Deals - Saved Deals Shelf.md`, insert `* * *` as a new line between line 22 and line 23
- Rule: `story-mode.md:151`. The gate sanctions the divider but never requires it, which is why four files carry the defect silently

**P1-3. The artifact is at a retired path, inside a gitignored tree that is also the source folder.**

- File: `AI Systems/Product Owner/export/Story Drafts/Creator - Deals - Saved Deals Shelf/Creator - Deals - Saved Deals Shelf.md`
- Current path: `export/Story Drafts/<name>/<name>.md`
- Replacement path: `export/006 - PRD-saved-deals-shelf.md`
- Stated by: `sk-product-owner/SKILL.md:207`, `references/story-mode.md:25`, `references/story-mode.md:369-375`, `assets/story-template.md:22`. The old convention was deleted by `e7819e4`
- Move the source to `benchmark/holdout/` per section 7 in the same pass, so the export tree stops being the source tree

**P1-4. Pin the Requirements contract in the gate.**

- File: `AI Systems/Product Owner/benchmark/format/validate-output-format.cjs`, after line 941
- Current: four `storyMode.includes` pins, none covering the contract `ba2bec3` added
- Replacement, appended:
  ```js
  if (!storyMode.includes('Every bullet is a sentence a build can fail')) {
    errors.push('sk-product-owner/references/story-mode.md: missing the build-can-fail contract for Requirements bullets');
  }
  ```
- Rationale: `AI Systems/Product Owner/specs/010-requirements-bloat/findings.md` section 6.4 proposed it and it was not applied. It does not catch a bad artifact, it catches the rule going missing, which is what the commit history shows happening to this section repeatedly

**P1-5. Close the "never drop the line" hole in prose, with the same four verbs.**

- File: `AI Systems/Product Owner/sk-product-owner/references/story-mode.md`, line 78
- Current, the clause: `Never invent the string, and never drop the line: an unsupplied value is an open constraint, not an absent one.`
- Replacement: `Never invent the string, and never drop the change: an unsupplied value is an open constraint, not an absent one. The line itself is always dropped, and only the change it names travels. A bullet whose verb is explains, states, tells or informs, and which quotes none of the copy, has kept the line instead of the change, whatever its subject: a screen, a sheet, a body, a headline or a label`
- Rationale: the word `line` is what the model obeyed. Naming the four verbs in prose keeps the instruction surface and the gate saying the same thing, which is the pattern `story-mode.md:151` and the gate pins already follow

### P2

**P2-1. A supplied change was dropped.**

- File: same artifact, after line 32
- Current: no bullet carries `Updated bookmark icon` from `context.md:12`
- Replacement, inserted: `*   The bookmark icon is updated per the design`
- Rule: `story-mode.md:195`, a supplied change in neither Requirements nor the delivery response is a defect

**P2-2. The out-of-scope bullet carries scope language that names nothing a build can fail.**

- File: same artifact, line 63
- Current: `*   No push notification when a saved deal is about to expire, out of scope for this delivery`
- Replacement: `*   No push notification fires when a saved deal is about to expire`
- Keep the `**Notifications**` group name, per `story-mode.md:76`. Report the scope decision in the delivery response, which is where `story-mode.md:195` puts a deliberate exclusion when no Delivery section exists

**P2-3. The cross-ticket dependency was weakened and a criterion asserts the blocked behaviour.**

- File: same artifact, lines 45 and 99-103
- Current at `:45`: `*   Expired deals stay in the grid, dimmed, once the Deal expiry ticket defines that state`
- Replacement at `:45`: `*   Expired deals stay in the grid, dimmed, using the expiry state the Deal expiry ticket defines`
- And insert a `**Dependencies**` group before the `* * *` at `:64`, matching the precedent in `Creator - Profile - Media Grids.md`: `*   Depends on the Deal expiry ticket landing first, which defines the state an expired saved deal shows`
- Rationale: `context.md:7` states a blocking sequence, "landing first". `once the Deal expiry ticket defines that state` reads as a condition on the behaviour rather than an ordering constraint on the delivery, and criterion 4 then asserts the behaviour as shippable. Either add an `**Open:**` line and let it open Delivery per `story-mode.md:74`, or state the dependency plainly and leave criterion 4 as the outcome the dependency unblocks

**P2-4. `story-mode.md:155` does not say whose words trigger Delivery.**

- File: `AI Systems/Product Owner/sk-product-owner/references/story-mode.md`, line 155
- Current, the opening: `What opts it in: a request naming the section or any of its parts (delivery section, estimation, estimate, sizing, how long, rabbit holes, no-gos, out of scope, scope exclusions, external dependencies)`
- Replacement: `What opts it in: a request from the requester naming the section or any of its parts (delivery section, estimation, estimate, sizing, how long, rabbit holes, no-gos, out of scope, scope exclusions, external dependencies). The trigger is the ask and never the source. A source line saying a change is out of scope is a constraint the delivery must satisfy, so it becomes a Requirements bullet stating the prohibition, and it opts nothing in`

**P2-5. The stale worked-example description, unapplied edit M from 060.**

- File: `AI Systems/Product Owner/sk-product-owner/references/story-mode.md`, line 399
- Current: `- [\`examples/story/prd-example-simple.md\`](../assets/examples/story/prd-example-simple.md): a small Story with one requirement, a flat acceptance-criteria list and no Delivery section, so the artifact ends on Acceptance criteria`
- Replacement: `- [\`examples/story/prd-example-simple.md\`](../assets/examples/story/prd-example-simple.md): a small Story with no hard constraint to state, so \`## Requirements\` is omitted entirely, with a flat acceptance-criteria list and no Delivery section, so the artifact ends on Acceptance criteria`
- Evidence: `grep -c "## Requirements" prd-example-simple.md` returns 0

**P2-6. No worked example shows a per-screen Requirements section.**

- File: `AI Systems/Product Owner/sk-product-owner/assets/examples/story/prd-example-screens.md`, to be added, plus a sixth entry in `story-mode.md` section 8
- Current: absent. All five examples group by data concern. All seventeen stories group per screen
- Content: one screen with several supplied values, one screen with a `Shared with:` reuse map, one screen the source names with no content supplied so the single design-pointer bullet is modelled, and one screen whose copy the source paraphrases so the struck bullet is modelled
- Rationale: `AI Systems/Product Owner/specs/010-requirements-bloat/findings.md` section 5 proposed it and it was not added. It is the direct fix for the "the group did not look like the exemplar" mechanism in section 2.1 above

**P2-7. A design pointer with no design to point at.**

- File: `AI Systems/Product Owner/sk-product-owner/references/story-mode.md`, line 78
- Current: `is carried as a constraint pointing at the design or the party that settles it`
- Replacement, appended to that sentence: `Where no design link was supplied, the pointer names the design or the party in plain text and the delivery response asks for the link, because a pointer a developer cannot follow is an open constraint that has to be visible as one`
- Evidence: `:32` of the artifact points at a design, and the artifact has no References section because the source supplied no links

### P3

**P3-1. Backtick handling is inconsistent inside one artifact.**

- File: same artifact, lines 29 and 39
- Current at `:29`: `*   Bookmark icon sits \`top right\` of the card, \`24px\` from each edge`
- Current at `:39`: `*   Reachable from the profile menu, second item, below Highlights`
- Replacement at `:29`: `*   Bookmark icon sits top right of the card, \`24px\` from each edge`
- Replacement at `:39`: `*   Reachable from the profile menu, \`second\` item, below Highlights`
- Rationale: `story-mode.md:161` limits backticks to exact expressions, thresholds, field names and event names. `top right` is prose the source did not quote. The menu position is an ordinal the source did supply, and `:75` lists a button order among the values that travel in backticks

**P3-2. Editing fragment.**

- File: `AI Systems/Product Owner/sk-product-owner/references/story-mode.md`, line 150
- Current: `never with its size or the number of requirements keep.`
- Replacement: `never with its size or the number of requirements.`

**P3-3. The template restates the Requirements contract the reference owns.**

- File: `AI Systems/Product Owner/sk-product-owner/assets/story-template.md`, lines 110 to 113
- Current: four bullets restating `story-mode.md:75-79` and `:149` in near-identical words
- Replacement: one bullet, `- Requirements hold hard requirements only, and the full contract lives in [story-mode.md](../references/story-mode.md) section 3: what a bullet must name to stay, how supplied values travel, how a described screen becomes a design pointer, and when the section is omitted`
- Rule: `story-mode.md:20`, one authority rather than two copies that drift apart

**P3-4. The preamble-group rule forces a duplicate group on a summary line.**

- File: `AI Systems/Product Owner/sk-product-owner/references/story-mode.md`, line 79
- Current, the clause: `It gets its own bold-lead group named for the surface it changes, and it is never folded into a neighbouring screen or dropped because the source did not give it a heading`
- Replacement: `It gets its own bold-lead group named for the surface it changes, and it is never folded into a neighbouring screen or dropped because the source did not give it a heading. The exception is a preamble line that summarises changes the headings below it then detail, which is one change stated twice and belongs in the group that details it`
- Evidence: `context.md:12-13` reads `Updated bookmark icon, tooltip copy and toast` followed by `+ Screen updates below`, and all three changes belong to the deal card the next heading names

**P3-5. About carries source prose as copy.**

- File: same artifact, line 9
- Current, the second sentence: `The shelf and its empty state reuse the profile media grid and the Highlights empty-state pattern, so most of the build is assembly rather than new design.`
- Replacement: `The shelf and its empty state reuse the profile media grid and the Highlights empty-state pattern.`
- Rule: `story-mode.md:80`, source prose is material and never copy. The dropped clause is a sizing claim, which Estimation owns
