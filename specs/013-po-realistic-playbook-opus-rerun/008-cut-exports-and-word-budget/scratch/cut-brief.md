# Brief: cut the benchmark exports by about 30%

The operator read the Opus 5.5 benchmark exports on 2026-09-26 and found them still bloated. A first pass met the length caps by splitting lines and cut only 2% of the words. This pass cuts words. The operator chose "about 30% fewer": cut restated context, background nobody acts on and repeated explanation, and keep every supplied value, name, number, owner, decision and open question.

## Gates, already answered

- Spec folder: `AI Systems/Product Owner/specs/013-po-realistic-playbook-opus-rerun/008-cut-exports-and-word-budget`. Do not ask about documentation.
- Nobody is at your prompt. Ask nothing and wait for nothing.
- Write authority: only the export files your group list names, edited in place. Read anything else. Run no git command, create no file, run no scenario.
- No em dashes anywhere in what you write.

## Where things are

- Your list: `AI Systems/Product Owner/specs/013-po-realistic-playbook-opus-rerun/008-cut-exports-and-word-budget/scratch/groups/g<N>.txt`, paths relative to `AI Systems/Product Owner/export/benchmark/`.
- Snapshot before this cut: `.../008-cut-exports-and-word-budget/scratch/before-cut/<same path>`. Never edit it.
- Verify: `python3 "AI Systems/Product Owner/specs/013-po-realistic-playbook-opus-rerun/008-cut-exports-and-word-budget/scratch/verify_cut.py" "<export path>"`, run from the repository root. It prints the words before and after and the cut.

## What to cut

- **Restatement.** The About says what a requirement's rationale says again, or a rationale repeats the checklist under it. Say it once, where the reader acts on it.
- **Background nobody acts on.** Narrative of how the problem was found, who said what in a thread, and history that changes no requirement. Keep the fact, drop the story around it.
- **Explanation past the first reason.** One clause of why is enough for a decision or a constraint. Cut the second and third clause that elaborate it.
- **Lead-ins and wrap-ups.** "This means that", "In other words", "As noted above", "which is why", sentences that announce the next section or sum up the last one.
- **Duplicate checklist items.** Merge two items that state the same condition. Never drop a condition: every checklist condition survives, merged or alone.
- **Long phrasing.** "in place of" becomes "instead of", "at the point where" becomes "when", "is able to" becomes "can".

## What never goes

- Every supplied value, name, number, date, time, amount, owner, team, platform, surface, version, id, status word, deadline, link and open question
- Every requirement, checklist condition and acceptance criterion
- Every scope and out-of-scope item, with its reason cut to one clause
- Every decision and who makes it, and every caveat that marks something as not decided, proposed or unconfirmed. A hedge stays a hedge: never turn "may" into "will" or a condition into an unconditional
- No new fact, example, name or claim. Rewording must not change what is true

## Structure that stays byte for byte

Every heading, bold label line, numbered criterion title (`1\. **...**` or `1.  **...**`), table row, code block, HTML comment, `---` or `* * *` divider, `##   ` spacer, italic template line and `- [ ] _Mark as done, if the criteria are met_` line. Given/When/Then lines may be tightened but never dropped or merged. A blockquote may be tightened but never removed.

## House grammar

- Bullets start as the file already does (`- ` or `*   `), never end with a full stop, and use no semicolon, no em dash, no curly quote and no single-asterisk emphasis
- Keep the articles and the reasoning words: `because`, `so`, `when`, `if`, `unless`, `before`, `after`, `rather than`. Telegraphic text fails the gate's keep side
- The caps still hold: a bullet is one sentence of 25 words or fewer, a paragraph at most three sentences and 60 words, an About or Overview opening at most two paragraphs. Cutting should now bring most About openings to two paragraphs

## A worked cut

Before, 64 words:

> The carrier counts a timeout, a `4xx` and a `5xx` as a failed delivery and retries up to 5 more times, after 1 min, 5 min, 15 min, 1 h and 6 h.
>
> The request path therefore does only what the carrier needs to stop retrying, and all label work runs from a queue, so a slow warehouse system can no longer turn one event into several.

After, 41 words:

> The carrier treats a timeout, a `4xx` or a `5xx` as failed and retries up to 5 more times, after 1 min, 5 min, 15 min, 1 h and 6 h. So the request only acknowledges, and label work runs from a queue.

The second sentence restated the About's point about the slow warehouse system, so it went. Every value stayed.

## Two copies of one artifact

A Project scenario can hold a turn-1 file and a `(turn 2)` file of the same artifact. Cut each on its own, and keep their shared sentences worded the same where the text was the same.

## Done means

- Every file in your list prints `PASS` or `KEPT` from the verify script
- Your group's words fall by at least 25%, aiming at 30%. A file cut by less than 20% prints `LIGHT`: say why, for example that it was already lean or holds mostly values
- A file that still fails after your best edit is reported with the script's reason, not forced

Your final message: one line per file, `PASS`, `KEPT` or `FAIL`, with words before and after, then the group's total before and after, then every `LIGHT` file with its reason, then any cut you were unsure kept a fact.
