Nothing is written yet. This is the first intake round. Your request names ten parts but not the calls between them, and an architecture board draws calls, so I need those before I build the model.

**What I read from the request**
* Type: architecture, because you ask which services sit behind block sync. If the real question is the order of one sync, that is a sequence diagram instead
* Parts: desktop, web and iOS clients, API gateway, sync-service, push worker, blocks database, file storage, change stream and Apple's push service. That is 10
* Target: a new board section in file `<test-file-key>`, in the Loomlist Engineering plan. The composer places it to the right of existing content and touches nothing already there
* Assumed for now: balanced detail, a mixed audience (so `sync-service` reads "Sync Service") and laptop reading distance
* Left out: the Android client and its push service. They are not in your list, so I read that as intended

**1. Reader and outcome**
* Reading: no reader is named. The Loomlist context page lists the Sync team under Joana
* Question: who opens this board, and what should they be able to decide or do after?
* Recommended: Sync and Mobile Platform engineers, who can then see which parts carry a block change from one device to the others
* Why: that is the question your request asks

**2. The calls between the parts**
* Reading: your list has no calls. The context page says sync-service owns sync sessions and device cursors. It also says push for mentions, replies and shares goes out through each mobile platform's push service, and that nothing else sends push. That leaves it unclear whether your push worker is a separate sync worker or part of that notifications path
* Question: which doc or repo states the calls, or do you confirm this draft? It is my guess, not read from a source
  * Desktop, web and iOS to API gateway: "Sync requests"
  * API gateway to sync-service: "Routes sync"
  * Sync-service to blocks database: "Writes blocks"
  * Sync-service to change stream: "Publishes changes"
  * Change stream to push worker: "Consumes changes"
  * Push worker to Apple's push service: "Apple Push: Wakes device"
* File storage: I have no recommendation. Which part reads or writes it?
* Why: a node with no call is not allowed on this board. Any call I add without a source would be invented

**3. Ten parts is over the budget**
* Reading: one architecture board holds at most 9 nodes and 12 connectors, and I will not cut file storage silently because you named it
* Question: split or cut?
* Recommended: split by request path into two boards in the same file, the change path (nine parts) and the file path (file storage with the parts that call it). If your answer to question 2 is that nothing in sync touches file storage, cut it instead and name it under `Left out:`
* Why: splitting keeps every part you listed

Answer, accept or correct each one. If you skip one, I proceed on its recommendation and mark it assumed. Next come the playback of the full reading and then the write gate, where you say yes to the write itself.