The model passes `scripts/flow_check.py` and composes cleanly. Nothing is written yet. The Figma tools are connected in this turn's listing, and the search found `use_figma`, `get_figjam`, `get_screenshot` and `create_session`.

* **Question:** which parts take part in block sync, and how do they connect?
* **Outcome:** Sync and Mobile Platform engineers can see which parts carry a block change from one device to the others.
* **First glance:** Sync Service, where every block change is written and published.
* **Second glance:** the Change Stream that carries each change on to the Push Worker.
* **Last glance:** Apple Push, the external hop that wakes devices.
* **Plan and file:** Loomlist Engineering, existing FigJam file `<test-file-key>`. The board lands as a new section 400 pixels right of what is already on the page, and nothing existing is touched.
* **Writes:** one composed board titled "Block sync", with 9 nodes and 8 connectors in 6 lanes, plus a key and a source line. Detail is balanced, the audience is mixed and the reading distance is laptop. The source line says the calls are assumed and that file storage and Android are left out.
* **Extensions:** none.
* **Calls:** `create_session` on the file, one `use_figma` and one `get_figjam` read-back. If the file turns out not to be a FigJam board, the write stops. A Starter plan or a View or Collab seat is limited to six tool calls a month, and this uses three of them.
* **Rollback:** delete the one board section the write returns. That happens only after you say yes to the deletion.

Write it?