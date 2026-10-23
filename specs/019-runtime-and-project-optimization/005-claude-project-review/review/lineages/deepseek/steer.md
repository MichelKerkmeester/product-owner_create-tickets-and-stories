# Steer: Product Owner Claude Project review

Rulings from the lead. They bind inside this lineage.

1. The review target is the Product Owner files named in ../../../spec.md under Files to Change, not the staging spec itself. Review those files.
2. Read only. Never edit, create or delete a file outside this lineage directory, and run no command that writes elsewhere.
3. Iteration 1: kernel and knowledge correctness against the skill sources, and rule loss from the kernel cuts (git diff HEAD on claude project/Custom Instructions.md). Iteration 2: end-user setup UX for the ClickUp and Figma connectors in Claude Desktop and claude.ai, against AI Systems/Media Editor/USER-GUIDE.md. Iteration 3: connector tool names and parameters the Project assumes, and what evidence backs each, plus anything iterations 1 and 2 left open.
4. Out of scope: Product Owner specs/, export/, benchmark/reports/, claude-plugin/, and AI Systems/Product Context, any screenshot and any figma.com URL, which you never open.
5. Every finding carries P0, P1 or P2, cites [SOURCE: path:line] with a repository-relative path that resolves, and names the file a fix changes.
6. Confirm a finding by opening the cited line before recording it. When unsure, record it as P2 with the doubt stated. When the repository cannot settle a question, such as what a live claude.ai connector exposes, record it as an open question, not as a fact.
