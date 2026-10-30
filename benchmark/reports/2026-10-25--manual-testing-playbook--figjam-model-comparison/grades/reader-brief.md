# Reader brief

The prompt each fresh reader of a scored FigJam board receives, and the wording a grader brief uses to score Composition from the readers' notes. Two readers read each board. Fill the angle-bracket slots and send the prompt unchanged otherwise.

## Reader prompt

You are a fresh reader of a FigJam board, seeing it for the first time. You are a product manager at the company the board is about, who knows the product but did not see the request or the sources.

Open only these images and no other file: `<overview image>` (overview) and `<full-size image>` (100%, zoom in as needed). Look at the overview first. Do not read any transcript, model, scenario, skill file or another reader's notes. When two boards of one flow sit side by side in one file, the brief names both images and you read them together as one set.

First, before anything else, write your reading order. List in order the parts of the board your eye lands on in the overview, one line each, naming each shape or group by its label, such as the title, a coloured state, a section or a key. Say where the frame (title block, key, lanes, zones, sections) sits in that order, but list the parts inside it separately.

Then answer these questions from the board alone, each in one or two sentences, and say how sure you are and where on the board you found it. Q4 and Q5 are there only when the scenario names source questions. For each, name the card, note, field or label you read the answer from, or write that the board does not say:

- Q1: `<question 1>`
- Q2: `<question 2>`
- Q3: `<question 3>`
- Q4: `<source question 4>`
- Q5: `<source question 5>`

Then answer in plain prose under these headings:

1. Title and the question this board answers.
2. The main path or structure from start to end, naming the shapes.
3. Every decision or branch and where each exit goes.
4. What the key says each colour, shape, outline and line style means, and whether every mark on the board is in the key.
5. Anything you could not read, could not follow or found ambiguous, with where it sits.
6. One sentence: could you act on this board without asking anyone, yes or no and why.

Write everything to `<output path>`. Finish the file with one last line, `Order: <label> > <label> > ...`, that repeats the reading order you wrote first, at the top of the note, with the board's nodes only and in that same order, using the labels exactly as printed on the board. It is the order your eye landed on them in the overview, not the order the flow runs. Leave out the title, the subtitle, lanes, zones, the key and the footnote. Name every node once.

## Grader brief wording

Substance scores from both readers' answers to Q4 and Q5 against the scenario's answers, as the playbook's Section 3 sets out. An answer that names nothing on the board to point at does not count.

On a user flow or a process, Composition is the output of `run/composition_check.py` on the plan and the readers' notes, never a reading by eye. Other board types print no `Glance:` line, so they score by the playbook's Composition row.

- Plan: the `Glance:` line the check printed for the board the run wrote, which is the last one printed before the write.
- Run: `python3 run/composition_check.py --plan "<Glance line>" <reader a note> <reader b note>`.
- Paste the script's lines into the record's Composition reason. The level in the record is the level the script prints.
- A note with no `Order:` line, or an `Order:` line that leaves out a node the plan names, stops the script. Ask the reader to finish the note. Do not repair the line by hand.
- The completeness check reruns the script on every scored board and diffs its level against the record. It reads no reader prose.
- Notes written before the `Order:` line existed score with `--legacy-list`, which reads their numbered reading order list.
