---
title: "Rules - Conciseness - On Demand Rationale - v0.100"
description: "The reasons behind the conciseness layer: the vocabulary candidates that were refused and why, the worked cut and keep pairs, the connective argument, and the roster of what blocks against what advises."
version: "0.100"
contextType: reference
importance_tier: high
trigger_phrases:
  - "conciseness rationale"
  - "rejected vocabulary"
  - "why is this term not banned"
  - "worked cuts"
  - "block or advise"
  - "drop-in conciseness block"
---

# Rules - Conciseness - On Demand Rationale - v0.100

The reasons behind the conciseness layer: the vocabulary candidates that were refused and why, the worked cut and keep pairs, the connective argument, and the roster of what blocks against what advises.

**Loading Condition:** ON_DEMAND. Never read in order to write a document, since paying for a justification on every turn is what made the layer too expensive to load
**Purpose:** Holds what a maintainer needs while changing a rule, so the always-loaded card can hold only what a writer needs while writing
**Scope:** What the validator holds, the boundaries of the reconstruction test, the refused vocabulary with the correct writing each term would have failed, one worked pair per named cut rule, five worked keeps, the perimeter worked case, rhetorical against semantic connectives, a worked list-to-prose conversion, the check roster, the drop-in instruction block, and the division of labour with the Human Voice card
**Output Path:** None. It explains the rules another file enforces, and writes no artifact
**Authority:** `Rules - Conciseness - v0.100` is the rule. This file is the reason, so a disagreement between them is a defect in this file. Section numbers below match the card, which is what lets a rule and its reason be found from either side
**Read It When:** adding or removing a blocked term, changing a floor, moving a check between blocking and advisory, or answering why a rule is the shape it is. A writer producing a deliverable never needs it

---

## 1. WHAT THE VALIDATOR HOLDS

The validator holds three kinds of check against the card.

- **Vocabulary checks** name exact terms. Section 3.2 of the card states every one of them, so a writer is never failed for wording no instruction file gave them. A guard inside the validator fails its own run when a term reaches a blocking list without being written into the card
- **Shape checks** match a sentence or line pattern rather than a word. Sections 3.4 and 8 of the card state each shape and the near-miss it deliberately leaves alone
- **Ratio checks** count connectives and articles across the prose in a document. Section 5.2 of the card states the floors and the perimeter they are measured over

The guard is the reason a term cannot be added to the gate alone. A blocking term absent from the always-loaded card is a rule enforced in code and unstated in prose, which is the split that keeps producing writers punished for wording nobody gave them.

---

## 2. THE RECONSTRUCTION TEST, AND ITS BOUNDARIES

Two worked pairs show the line the test draws.

- A sentence reading "The reapply action is unavailable once the deal stops accepting applications, so a creator cannot apply to a closed deal" survives a cut down to "Reapply is unavailable on a closed deal", because a reader rebuilds the reason from the state. The trailing clause was free
- The same sentence does not survive a cut down to "Reapply respects deal state", because nothing in the remainder says which state or what happens in it. The cut moved the rule into the reader's head

### What the test is not

The reconstruction test is not a word budget, and it does not reward a shorter answer over a correct one. A document that halves its length while dropping one caveat has failed the test on that caveat, whatever happened to the total.

It is also not a document-level verdict. Applying it per document produces a single judgement about length, which is the judgement that strips connectives. Applying it per cut produces a decision about each removal, and the decisions add up to a length nobody had to target.

### Who the reader is

The test asks about a reader who does not already know the answer. That reader is the one who opens the artifact three weeks later with no memory of the conversation that produced it, and no access to the reasoning that stayed in the reply. Every cut is judged against them rather than against the person who asked for the work.

---

## 3.3 TERMS THIS LAYER REFUSES TO BAN

The blocking lists in Section 3.2 of the card are short on purpose, and the terms below were considered and left out. Each carries content in at least one shape the fleet ships, so banning it would fail correct writing. This is the record of the refusal. Re-proposing one of these terms means answering the case against it first.

- **A rate or a proportion.** "often", "sometimes", "usually", "largely" and "mostly" state how frequently something holds, which the scope qualifier keep rule protects as content rather than uncertainty
- **A degree on a quantity.** "roughly", "nearly", "almost", "virtually" and "more or less" modify a number. A number the writer knows exactly should be stated exactly, and a number that genuinely carries a range needs the range
- **A literal line of copy.** "the bottom line" names a real line of text in a copy artifact, so a ban on it would reach shipped microcopy
- **A modal in a specification.** "should" and "would" carry obligation and conditional behaviour, which acceptance criteria are made of
- **A genuine synthesis.** "taken together" introduces a conclusion the parts do not carry alone, which is new information rather than a recap
- **A plain-language gloss.** "in other words" earns its place where it translates jargon, which is exactly what a Glossary shape exists to do
- **Anything the fleet already ships beside another marker.** "fairly", "quite", "rather", "essentially", "basically" and "can be" each already sit next to an existing hedge somewhere in the shipped corpus, so promoting them would turn correct prose red on the day the change landed

Twenty-one terms across seven categories, and the categories are the durable part. A candidate that falls into one of them is refused for the reason the category states, without a fresh corpus sweep.

---

## 3.4 THE TWO CUT RULES THE VALIDATOR SETTLES ALONE

Both shapes are stated in the card. The discriminating examples are here, because precision comes from the near-miss rather than from the definition.

**Importance assertion.**

- Fires on "This is important." and on "These details are essential", because removing the marker leaves nothing
- Stays silent on "The euro value matters because a brand pastes one variation and ships another", because the sentence names what matters and why
- Stays silent on "The critical path runs from brief to export", because the marker is doing descriptive work

**Effort reporting.**

- Fires on "I reviewed the reapply path against the current brief", because the reader wants the finding rather than the pass that produced it
- Stays silent on "A reviewer checked the reapply path against the current brief and found it open", because the subject is the process the artifact documents rather than the author
- Stays silent on a quoted mention, since a document naming a shape is not using it

Both were probed against all three export trees and all three source perimeters before they were promoted to blocking. Zero hits, so neither landed a gate that was red on arrival.

---

## 3.5 WORKED CUTS

One pair per named rule. The left side is what arrives, the right side is what ships. Every example is quoted, so a rule that bans a phrase can still show the phrase.

- **Question echo.** "You asked how the payout window works. The payout window opens on Monday" becomes "The payout window opens on Monday"
- **Intent narration.** "Now I will walk through the three routing bands" becomes "Routing has three bands"
- **Compliance acknowledgement.** "Happy to help with the acceptance criteria. Criterion one covers the empty state" becomes "Criterion one covers the empty state"
- **Terminal recap.** A closing paragraph reading "So the router binds the token, scores the keywords and falls back to intake" is deleted outright when the body already said all three
- **Hedge stack.** "The cap might possibly apply per deal" becomes "The cap applies per deal" when it does, and "The cap may apply per deal, and product has not decided" when it is genuinely open
- **Importance assertion.** "Verification is critical. Read the file back and require non-empty content" becomes "Read the file back and require non-empty content"
- **The conclusion move.** A whole paragraph opening "To sum up" goes, not only the two words that open it
- **Both-sides padding.** "A weekly cycle is faster, though a monthly cycle batches fewer transfers" becomes "A weekly cycle is faster" when nobody proposed monthly
- **Empty enumeration.** "There are three signals worth considering: the command, the framing and the keyword score" becomes the analysis of what each signal decides
- **Heading echo.** Under a heading reading "Export verification", a first sentence reading "This section describes export verification" is cut and the section opens on "Read the artifact back from the exact path"
- **Restated constraint.** "You said the deal is a two-night stay for two. The two-night stay for two includes breakfast" becomes "The stay includes breakfast"
- **Effort reporting.** "I checked every variation against the ledger and the obligations match" becomes "Every variation carries the same obligations"
- **Count padding.** A three-item list stays a three-item list. The triad rule counts triads per 150 words and never bans one, so a fourth invented item is the padding this layer removes

---

## 4.1 WORKED KEEPS

Five pairs, each showing a cut that looked free and was not. The repair is on the right.

- **Semantic connective.** "Reapply is unavailable on a closed deal. Applications are rejected" loses the relation. "Reapply is unavailable on a closed deal, because a closed deal accepts no applications" keeps it
- **Scope qualifier.** "Spacer headings stay in the file export" applies everywhere. "Spacer headings stay in a Story or Epic file export, and never in a Doc export" says where
- **Negative case.** "Verify the save" leaves the boundary invisible. "Verify the save. A returned path is not verification, and a planned write is not either" draws it
- **Referent.** "It retries once, then blocks delivery" leaves the subject to guess. "The export retries once, then blocks delivery" names it
- **Example.** "Sanitize header values" is unusable alone. "Sanitize header values: strip markdown control characters and truncate to 50 characters" is usable

Grammar is never the target. A sentence missing its article reads as a headline, and a body full of headlines is a document a reader has to translate before they can use it.

---

## 5.3 THE PROSE PERIMETER, AND WHY IT IS NOT THE WHOLE FILE

Measured across a whole file, both floors give the wrong answer on a structured artifact, because a headline list, a field block, a hashtag run and a variation label say nothing about compression either way. A deal template scoring zero connectives across its whole file is correct rather than telegraphic, and a check that reports it learns to be ignored, which removes the counterweight the cut side needs.

A worked case pins the perimeter. A four-variation deal template runs 344 words at zero semantic connectives across the file, which a file-level ratio flags every time. Its paragraph prose is 32 words, which is under the 200-word floor, so the check stays silent and the artifact ships. The same document rewritten as 250 words of connective-free explanation fails, correctly.

The file-level advisory this replaced fired on 12 targets across the three systems. The prose-scoped version fires on 2, and every case it drops is a structured artifact whose paragraph prose runs 38 to 291 words of field-and-headline content. In exchange the check went from advisory to blocking on a deliverable.

### 5.4 Repairing an over-compressed pass

The card states the repair in one sentence. The full order below is the cheapest route back.

1. Find each pair of adjacent clauses whose relation is implied and name it, using `because`, `so`, `unless`, `which means`, `since`, `while` or `rather than`
2. Restore the subject wherever a pronoun or bare noun sits more than a clause from its antecedent
3. Restore articles and finite verbs in every sentence that reads as a headline
4. Restore the one example per non-obvious rule, since an abstract rule with nothing showing its use is the signature that costs a reader the most
5. Re-measure. A pass that lands just above a floor has usually restored the relations without restoring the reasoning, so read the result rather than trusting the number

A repaired document is longer than the compressed one and shorter than the original. That is the intended shape.

---

## 6. RHETORICAL CONNECTIVES VERSUS SEMANTIC ONES

The Human Voice standard penalises `however`, `furthermore`, `moreover`, `additionally` and `consequently` from the third use. Those are rhetorical: they signal a turn in the argument that the sentence order usually already signals.

Semantic connectives are a different category. `because`, `so`, `unless`, `which means`, `since`, `otherwise` and `while` state a relation between two propositions, and the relation is content. They are never capped, never counted against the rhetorical limit, and never removed to save words.

Read that cap as licence to strip connectives and the output arrives telegraphic, which is the failure this layer exists to prevent. The article floor and the connective floor exist to catch exactly that reading, which is why the keep side is countable at all.

---

## 7.2 A WORKED CONVERSION

A bulleted block reading "Router binds token", "Keyword pass runs second", "Total weight separates ties" carries three deleted relations. As prose it reads "The router binds an exact command token first, because a keyword-first pass would bind the wrong intent. Keyword scoring runs second, and total weight separates two lanes that reached the same band."

Two sentences replaced three fragments, the word count barely moved, and the reasoning came back. That trade is what this layer asks for whenever a list is hiding an argument.

---

## 8. WHY THE PURITY ENUMERATION EXISTS

The rule is not new and the failure is not hypothetical. Exports have shipped with their own scoring appended to the body, which is how the enumeration in Section 8.1 of the card came to be written down.

The ban anchors on position rather than on vocabulary, because the corpus proves a word-level ban fails correct writing. A shipped requirement reads "which of content quality, communication and timeliness scores strongest and which weakest", so a ban on "score" or "weakest" fails a correct specification. A shipped headline opens "Score a Fjell serum set and earn 150 euro", so a ban on the verb fails shipped copy. A compliant deal template writes `Scoring: DEAL 24/25` inside its line-1 comment header, so a ban that reads comments fails every compliant export in that system.

A heading therefore fires when it carries an unambiguous acronym, or when its own leading label is the report name. A body line fires when its own opening is the report. Every HTML comment span is blanked first, since invisible when rendered is the whole test.

---

## 9. WHAT BLOCKS AND WHAT ADVISES

The format validator runs in two modes, and the same rule can carry different weight in each.

**On a produced deliverable, these block.** Bullet punctuation, the three Human Voice punctuation marks, the sentence-opener list, the hedge stack, the heading echo, the terminal recap, the importance assertion, the effort report, the connective floor, the article floor and every shape in the purity enumeration.

**On a system's own instruction sources, these block.** The sentence-opener list, the hedge stack, the heading echo and the terminal recap, plus the Human Voice punctuation marks on the files that teach the voice. Bullet punctuation blocks where a system's sources are already clean and reports a standing debt where they are not.

**These advise rather than block.** The bullet ratio, the heading density, the importance assertion and the effort report on an instruction file, and both prose floors on an instruction file. A ratio is evidence, and an instruction file has to be able to state a shape in order to teach it.

The purity enumeration never runs on an instruction source at all. A file whose job is to ban a scoring block has to be able to write one down.

### 9.1 The check roster

| Check | On a deliverable | On an instruction source | Stated in the card at |
| --- | --- | --- | --- |
| Sentence opener | blocks | blocks | 3.2 |
| Terminal recap opener | blocks | blocks | 3.2 |
| Hedge stack | blocks | blocks | 3.2 |
| Heading echo | blocks | blocks | 3.2 |
| Importance assertion | blocks | advises | 3.4 |
| Effort reporting | blocks | advises | 3.4 |
| Prose connective floor | blocks | advises | 5.2 |
| Prose article floor | blocks | advises | 5.2 |
| Bullet ratio | advises | advises | 7 |
| Heading density | advises | advises | 7 |
| Deliverable purity | blocks | not run | 8.1 |

The pairing across the middle rows is the point. Each cut-side row that blocks on a deliverable has a keep-side row blocking beside it, so a writer cannot satisfy the gate by cutting alone.

---

## 10. DROP-IN INSTRUCTION BLOCK

Copy the block below into a system prompt that has no room for the card.

> Answer the question. Do not restate it, do not announce what you are about to do, and do not agree to do it first.
>
> Cut anything a reader could rebuild from what remains. Keep what they could not rebuild: the reason, the scope, the caveat, the number, the one example that makes a rule usable.
>
> Never delete `because`, `so`, `unless`, `which means`, `since` or `otherwise` to save words. Those carry the logic. The cap on `however`, `furthermore` and `moreover` limits rhetoric, not reasoning.
>
> One hedge per claim or none. No closing paragraph that repeats the body. No sentence whose only content is that something matters. No sentence that narrates the pass instead of reporting what it found.
>
> Prose when items differ in weight or their order encodes reasoning. Bullets when three to seven items are genuinely parallel. Tables when every row shares fields.
>
> Write full sentences. Articles, copulas and finite verbs are not a compression target.
>
> The artifact carries the deliverable. Scores, self-scans, assumption tags and process notes go in the reply, or in the line-1 HTML comment that renders as nothing.

---

## 11. DIVISION OF LABOUR WITH THE HUMAN VOICE CARD

The Human Voice card and the conciseness layer are read on every request and they do not overlap.

The card governs word choice and punctuation. It holds the hard blockers, the banned metaphors, the always-cut modifiers, the em dash and semicolon bans, and the straight-quote requirement. A violation of the card is counted in the hard blocker total that the delivery response reports.

The layer governs quantity, structure and load-bearing-ness. It holds the reconstruction test, the cut and keep rules, the over-compression floors, the format choice and the deliverable purity enumeration. A violation there is an edit, so it is fixed in place and never counted in that total.

Two consequences follow from the split.

- A document can clear every hard blocker and still be three times too long, which is the case the layer exists for
- A document can be exactly the right length and still fail the card, which is the case the card exists for

Where the two appear to disagree, the card wins on any question of wording and the layer wins on any question of what is present at all. A term the card sanctions stays, and a paragraph the layer cuts goes, even when every word in it was sanctioned.
