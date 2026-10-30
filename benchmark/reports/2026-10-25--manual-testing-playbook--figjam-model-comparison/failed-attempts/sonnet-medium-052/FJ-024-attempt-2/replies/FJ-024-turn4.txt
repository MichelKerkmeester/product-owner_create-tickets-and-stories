<figma-url>
Read-back: 9 of 9 nodes, 8 of 8 connectors, 6 of 6 lanes, first glance: sync-service
Left out: file storage, no call stated in the doc
Finding: the Blocks Database body line "Keeps 30 days of block history" renders as "..." on the board, because the database shape's text area cuts it off. The 30-day rule is in the node's text but a reader can't see it. The fix is a model change, such as moving the rule onto the `Writes Blocks` edge label or shortening it, then composing again after your yes.
Finding: the Change Stream body wraps as "Keeps events for 7" with "days" alone on the second line. The check had flagged the same kind of wrap risk on "Apple Push Service", which I reworded. This is the stream shape's width. A shorter line, such as "Events kept 7 days", would fix it on the next compose.
Finding: I changed the node label from "Apple Push Service" to "Apple Push" after the check flagged the old one. You saw this at the gate.
Finding: the connector read does not return dash patterns or connector label text, so the three dashed async lines and the eight edge labels are confirmed from the composing call's return and the screenshot, not from the read.
Finding: the file's page was empty before the write, so there was no existing content to compare against.
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.