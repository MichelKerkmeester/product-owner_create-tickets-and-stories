# Brief: review the export rewrite for lost or changed facts

The Opus 5.5 benchmark exports were edited to length caps. A script already proved that every heading, backticked value, number and link survived. It cannot see a fact carried in plain words, so you read for that.

## Gates, already answered

- Spec folder: `AI Systems/Product Owner/specs/013-po-realistic-playbook-opus-rerun/006-concise-writing`. Do not ask about documentation.
- Nobody is at your prompt. Ask nothing and wait for nothing.
- Read-only on the exports and the snapshots. Write exactly one file, the one your dispatch names. Run no git command.
- No em dashes in what you write.

## Where things are

- Edited exports: `AI Systems/Product Owner/export/benchmark/<path>`.
- Graded originals: `AI Systems/Product Owner/specs/013-po-realistic-playbook-opus-rerun/006-concise-writing/scratch/before/<path>`, same relative paths.
- `diff "<before>" "<after>"` shows each changed hunk. Files with no diff need no reading.

## The question, for every changed hunk

Did the edit drop, change, generalize or add a fact? A fact is anything a reader of the ticket would act on or cite: who, what, where, when, why, platform, surface, owner, sign-off, escalation path, scope and out-of-scope, a reason or a cause, a condition, an order of steps, today's state or workaround, a status word, and a question left open.

- **Kept:** the same fact is still in the hunk, or elsewhere in the same file. Name the line.
- **Dropped:** the fact appears nowhere in the edited file.
- **Changed:** the fact is still there but now means something else: a reason became an instruction, a condition became unconditional, "or" became "and", a hedge became a claim, or the reverse.
- **Added:** the edit says something the original did not.

Shortened wording that keeps the meaning is fine and needs no entry.

## What you return

Your file opens with one line per problem: `path | before line | after line | Dropped, Changed or Added | the fact, quoted from the original`. Then a count of files read and problems found. Say plainly when a file has none. Quote rather than paraphrase.

Your final message is the path of your file and the problem lines, nothing else.
