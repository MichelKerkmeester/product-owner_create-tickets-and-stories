Updated model passes the check and composes. Revision gate:

**Change:** one node label — the `No` exit of `Within 30 days?` reads `Request an exception` instead of `Contact support`. Still an exit end node; 9 nodes, 9 connectors, same three zones, title, key and source line unchanged.

**How a revision lands:** the new board is composed first beside the old one in the same file, read back against the model, and only then is the old board section `28:1608` (found by its `productowner` tag, key `Start a return`) deleted — so a failed write never leaves you with no board.

**Plan:** Fernhouse Product. **File:** existing FigJam `<test-file-key>`.
**Calls:** one `use_figma` to compose, one `get_figjam` read-back, then one `use_figma` to remove the old section.
**Rollback:** delete the new board section; the old board stays until the new one verifies.

Write it?