I read the existing FigJam file and made no changes. I prepared this model from your description:

- Desktop, web, and iOS clients connect to the API gateway by live socket
- The gateway routes block changes to sync-service *(assumption)*
- sync-service writes changes to the blocks database and publishes them to the change stream
- The push worker reads the stream, then uses Apple Push Notification service to wake sleeping iOS devices
- File storage appears as a component, with no connector because its access path wasn’t specified

I can’t run the required Flow Mode pre-write check yet: shell reads fail with `sandbox_apply: Operation not permitted`, so I couldn’t load `sk-create-figjam/SKILL.md` and its routed references. Your `AGENTS.md` requires those instructions and a separate yes at the write gate before I edit the board.

Can you restore workspace file access or provide the Flow Mode instructions so I can continue?