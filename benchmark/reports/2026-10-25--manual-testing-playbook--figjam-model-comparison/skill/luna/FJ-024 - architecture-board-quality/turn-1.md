### Intake: Loomlist block sync

**Reading:** The reader is Loomlist Engineering. The diagram should show how the listed services connect block sync to the iOS wake path.

**Question:** What should the diagram avoid implying?

**Recommended:** Keep to the named components and paths. Leave protocols, retries, and failure behavior out; label any inferred file storage connection as assumed.

**Why:** The request does not specify those details.

**Reading:** The request names 10 components, while the architecture format allows up to 9 nodes per diagram. It names file storage but does not say which service connects to it.

**Question:** Should I split the content into “Block sync” and “iOS push wake” diagrams in the existing file, and assume sync-service reads and writes file storage?

**Recommended:** Yes, with the storage connection labeled as an assumption.

**Why:** That keeps every named component within the diagram limit.

I’ve read the existing FigJam file. Reply with corrections or accept these recommendations, and I’ll prepare the model for your review.