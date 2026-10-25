The model passed the pre-write check: 9 nodes, 8 connectors, 6 lanes, 0 crossings. The composed code is 44,872 characters, under the 50,000 one call takes. The Figma tools `use_figma`, `get_figjam`, `create_session` and `whoami` are all connected. Nothing is written yet.

- Question: which parts take part in block sync and how do they connect?
- Outcome: engineers and product people on the Sync team can see which part carries a block change from one client to the others
- First glance: Sync Service, where a block change is written and published
- Second glance: the Change Stream that carries each change on to the Push Worker
- Last glance: Apple Push, the external hop that wakes iOS devices
- Plan: Loomlist Engineering, as you named it. I haven't checked that the file belongs to it.
- File: the existing FigJam file `<test-file-key>`, with no new file. The board lands 400 pixels right of whatever is already there and touches none of it.
- Writes: one composed board titled "Block sync", with 9 nodes and 8 connectors in 6 lanes, plus a subtitle, a key and a source line, at laptop reading distance
- Assumed on the board: every call, because no sync doc was supplied. The source line says so.
- Left out: file storage, over the budget of nine, and `pages-service`, which you did not name
- Extensions: none
- Calls: three, namely `create_session`, one `use_figma` and one `get_figjam` read-back. On a Starter plan or a View or Collab seat that is half the monthly allowance of six.
- Rollback: delete the one board section the write returns, through `use_figma` and only on your separate yes

Write it?