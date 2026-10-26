<figma-url>
Read-back: 8 of 8 nodes, 8 of 8 connectors, 2 of 2 decision exits labelled, 3 of 3 lanes, first glance: Approve the claim
Left out: pickup skipped under €20, a pilot that is not live
Left out: a path for an item that fails inspection, because the runbook gives none
Left out: a limit on second-photo requests, because the runbook gives none
Finding: the connector labels ("Unclear", "Clear", "Logs", "To the warehouse queue") were confirmed on the overview screenshot only, because `get_figjam` returns connector names and not their label text. The connector ends, directions and lane order matched the model by id
Finding: the file was empty before the write, so there was no existing content to compare. The board sits at the page origin
Finding: I did not verify which plan the file belongs to, so I cannot confirm it sits in the Fernhouse Product plan. Nothing was created in the Barter team plan
Finding: the two assumptions from the playback stand. The claims table sits in the CS lane with only the "Damage clear?" decision logging to it, and the second photo returns to the same check. Correcting either means changing the model and composing a new section, and the old one is deleted only on your yes to a question that names it
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.