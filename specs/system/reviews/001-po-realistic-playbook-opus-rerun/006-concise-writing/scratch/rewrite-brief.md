# Brief: rewrite benchmark exports to the length caps

The operator decided on 2026-09-26 to edit the Opus 5.5 benchmark exports by hand so they read tighter. The verdicts stay as graded. This is a copy edit, never a content change.

## Gates, already answered

- Spec folder: `AI Systems/Product Owner/specs/013-po-realistic-playbook-opus-rerun/006-concise-writing`. Do not ask about documentation.
- Nobody is at your prompt. Ask nothing and wait for nothing.
- Write authority: only the export files your dispatch lists, edited in place. Read anything else. Run no git command, create no file, run no scenario.
- No em dashes anywhere in what you write.

## Where things are

- Exports: `AI Systems/Product Owner/export/benchmark/`, paths in your list relative to it.
- Graded originals: `AI Systems/Product Owner/specs/013-po-realistic-playbook-opus-rerun/006-concise-writing/scratch/before/`, same relative paths. Never edit these.
- Verify script: `python3 "AI Systems/Product Owner/specs/013-po-realistic-playbook-opus-rerun/006-concise-writing/scratch/verify_rewrite.py" "<export path>"`, run from the repository root.

## The caps

- A bullet is one sentence of 25 words or fewer.
- A paragraph is at most 3 sentences and 60 words.
- An About or Overview opening holds at most 2 paragraphs: the prose before its first heading or bold label, such as `**References**`.
- Exempt: code, tables, blockquotes and Given/When/Then lines. A backticked or double-quoted span counts as one word.

## How to get there

- Cut restatement, throat-clearing and anything the reader can rebuild from what remains.
- Split a long sentence into two, and split a paragraph that runs long.
- A multi-sentence bullet becomes one sentence: join with a colon or comma, or split it into two bullets. Split only in an unnumbered list, never in numbered steps.
- Keep the reasoning words: `because`, `so`, `when`, `if`, `unless`, `before`, `after`, `rather than`. Keep the articles. Telegraphic text fails the gate's keep side.

## What never changes

- Every heading line, bold label line, numbered criterion title (`1\. **...**`), Given/When/Then line, table row, blockquote, code block, HTML comment, `* * *` divider, `##   ` spacer and fixed template line (the italic intro lines, `- [ ] _Mark as done, if the criteria are met_` (other checklist items may be shortened), `All acceptance criteria below must be met...`). Leave these lines byte for byte.
- Every backticked value, number, date, name, owner, link and open question. Nothing is added, generalized or dropped.
- No new fact, no new example, no new name. When a cap can only be met by dropping a value, keep the value and report the line.
- A fact is more than a backticked value or a number: platforms, surfaces, sign-offs, escalation paths, what is out of scope and why, and today's workaround all count. Cut a sentence only when the body states the same content again. An About that cannot reach two paragraphs without dropping a fact stays over the cap and is reported.
- House grammar: bullets start `*   ` or `- ` as the file already does, never end with a full stop, and use no semicolon, no em dash, no curly quote and no single-asterisk emphasis.

## Known fixes

- Three Doc exports carry prose em dashes in link or source lines (`PDK-001` both files, `PDK-004 - 002`). Replace each with a comma or colon.
- `skill/SIR-001 - 001 - intake-guest-loyalty-points-clarification.md`: change the label `**2. Why it matters**` to `**2. What points should achieve**`, since the gate reads the old label as an importance assertion. This is the only structural line you may change.
- `claude project/PEP-003 - 001 - Epic-self-serve-returns.md` fails the gate's connective floor. Restore reasoning words while you tighten it.

## Done means

Every file in your list prints `PASS` from the verify script. A file that still fails after your best edit is reported with the script's reason, not forced.

Your final message: one line per file, `PASS` or `FAIL` with the reason, then the words before and after for your whole list.
