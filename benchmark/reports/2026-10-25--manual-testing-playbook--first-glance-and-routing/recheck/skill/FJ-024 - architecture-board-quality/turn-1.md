Before I draw anything, this is how I read the request.

**Question:** which parts take part in block sync and how do they connect? That makes it an architecture. A sequence would show the order of one sync instead, which you didn't ask for.

**Reader and outcome (assumed):** engineers and product colleagues in Loomlist Engineering. After reading, they can see which parts carry a block change from one client to the others and to a sleeping iOS device. Tell me if the reader is someone else.

**Settled by your request:** nine drawn parts and eight calls.
* The desktop, web and iOS clients each hold a live two-way socket to the API Gateway
* The API Gateway routes to sync-service
* sync-service writes every block change to the blocks database
* sync-service publishes each change to the change stream
* The push worker reads the change stream
* The push worker calls Apple's push service to wake sleeping iOS devices

**Assumed:**
* **Gateway to sync-service:** you didn't name this hop. I took it because the gateway is the clients' only way in, and the board's source line will say it was inferred.
* **Target:** your message says both "new board in the Loomlist Engineering plan" and "the existing file rather than a new file". I read that as no new file, and one new board section inside file `<test-file-key>`.
* **Look:** Laptop reading distance, mixed audience, labels in your words (sync-service as written). The six architecture lanes act as the zones, so there are no extra zone lines.
* **Glances:** first on sync-service, where every change is written and published. Second on the change stream feeding the push worker. Last on Apple's push service.

**Left out:** file storage. You named it but gave it no call to or from any part, and a part with no connector can't sit on this board without me inventing a call. With it the board would have ten parts, one over the nine-part budget. I recommend leaving it off and naming it on the source line. If a service touches it on the sync path, tell me which call and I'll split the board into an overview and a detail board.

**Not drawn:** the hop from Apple's push service to the iOS device. The architecture lanes have no edge from an outside system back to a client. The wake-up shows as the push worker's call out to Apple's push service, labelled with its purpose.

Is this the right reading of the board?