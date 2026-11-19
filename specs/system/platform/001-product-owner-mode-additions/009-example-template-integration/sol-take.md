# My take on template-example integration

## 1. OVERVIEW

A template-example pair is useful only when the model can answer three questions quickly.
Which scaffold fits this request?
Which filled artifact proves how that scaffold behaves under pressure?
What should be copied as structure, and what should remain specific to the fictional case?

The template supplies constraints and omission rules.
The example supplies judgment.
Without a direct link between them, the model spends tokens rediscovering a relationship the repository already knows.

The current templates are stronger than their retrieval layer.
Their sections distinguish shapes well, but most worked examples are invisible from the point of selection.
The current example descriptions mostly name a subject and format.
They do not say which template section they instantiate.
They also fail to name the hard decision that makes each example worth loading.

That weakness matters because topic similarity is a poor retrieval strategy here.
A dark-mode proposal is useful for its status discipline, not because the next proposal will concern dark mode.
An Android crash is useful because it labels a hypothesis without promoting it to root cause.
A mixed token catalog is useful because status stays local to each entry.
Those are generation patterns, and the descriptions should retrieve on those patterns.

Some examples also overlap at first glance.
The standard-feature task and UI-refinement task both used the canonical task body.
Meanwhile, the parent-task scaffold had no filled instance.
That is a bad allocation of a small example budget.
I am converting the standard-feature example into a parent task for the same saved-presets feature.
It will demonstrate shared scope stated once, child tasks linked cleanly, and no duplicated child requirements.
The UI-refinement example remains the canonical full task and owns the design-parity use case.

My integration scheme is deliberately local.
Each scaffold, tier, or document shape gets a one-line worked-example pointer beside its selection guidance.
Every pointer uses a real path relative to the template file.
Every pointer names the one judgment the example demonstrates.
When a section has several valid contexts, such as the bug scaffold, each example gets its own one-line retrieval cue.

Every example description follows one compact contract.
First, name the exact template section, tier, or shape.
Second, name the hard thing the body demonstrates.
Subject matter comes last, if it still helps retrieval.
This turns frontmatter into an index rather than a caption.

The bodies remain artifacts, not teaching notes.
No body will mention templates, examples, retrieval, or why it was selected.
Any sharpening must read as better product content inside the fictional case.
For stories, that means honest readiness, independent versus shared machinery, and observable scenario guarantees.
For bugs, that means evidence quality, missing-data honesty, and explicit separation of hypothesis from root cause.
For docs, that means source status, local lifecycle labels, precedence, and visible decision gaps.
For tasks, that means scope control, recovery states, design parity, and concise copy changes.

I am not adding folder-level `_index.md` files.
They would repeat the maps already embedded at the model's actual decision point: the template section.
An index would cost another retrieval hop and create a second place for mappings to drift.

The test for success is simple.
A model reading one template section should know exactly which single example to load next and why.
A model retrieving one example by description should know its scaffold before opening the body.
No example should win retrieval merely because its fictional topic resembles the prompt.
Each should win because it demonstrates the generation decision the prompt requires.
