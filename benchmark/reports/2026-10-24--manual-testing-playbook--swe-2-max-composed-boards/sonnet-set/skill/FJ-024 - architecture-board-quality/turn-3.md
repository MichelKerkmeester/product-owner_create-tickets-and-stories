<figma-url>
Read-back: 9 of 9 nodes, 8 of 8 connectors, 6 of 6 lanes, first glance: sync-service writing a block and publishing it to the change stream
Left out: file storage, no connection stated. The Apple push service to iOS app hop, because an architecture has no edge from an outside system back to a client, so the "Wakes iOS device" label carries it.

The board is in the existing file, 400 pixels right of what was there. Nothing existing was touched, and the write returned no warnings.

**Read-back**
- **Nodes and lanes:** every node sits in its own lane, and the labels match the model.
- **Connectors:** each connector has the model's two ends and direction.
  - The three live sockets are two-way.
  - The other five run one way.
  - The three edges touching the change stream or Apple's push service are dashed.
- **Labels:** `get_figjam` doesn't return connector label text. The labels are confirmed from the write result and the screenshot, not from the read-back.

**Layout findings from the overview screenshot**
1. **"Consumes" edge:**
   - On the Change stream, the Consumes connector (change stream to Push worker) leaves the top, runs left, then drops and doubles back under the Push worker. It crosses the "Publishes changes" line and strikes through the "Events" zone title.
   - The check had counted 0 crossings in the model, so this one appears only after layout.
2. **Web app "Live socket":**
   - The edge routes up over the "Edge" zone title and strikes it through.
   - The "Live socket" labels for desktop and web stack close together.
3. **"Publishes changes" line:** it grazes the top border of the External zone.

I haven't moved or restyled anything, because composed nodes are never edited in place. The fix is a reshaped model composed again, for example a different declaration order or an edge reversed. I can't promise that clears all three. A recompose writes a second board first. I'd delete this one only after you say yes to that separately. After two attempts I'd stop and ask. You can also nudge the lines by hand in FigJam.

I assumed the gateway-to-sync-service edge, Engineering as the reader and laptop reading distance. The temporary model and composed code are deleted.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.