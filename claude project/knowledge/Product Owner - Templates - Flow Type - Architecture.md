# Product Owner - Templates - Flow Type - Architecture

An architecture shows which deployable parts make up a system and how they connect. The composer places every part by the lane it sits in, one column per lane, and the lane sets the part's kind and colour role. Figma's generated fallback uses its own lane layout, which errors or silently mis-draws when its rules are broken, so the check holds every one of them on both routes.

---

## 1. WHEN TO USE

**The reader's question:** what parts make up this system and how do they connect?

- Clients, gateways, services, stores, queues and outside systems, and the calls between them
- One request path through a system, such as checkout or sync

Use a sequence when the order of the calls is the point, a process when people do the work, and an ER diagram when the subject is data rather than services. A Product Owner reader often wants the sequence, so ask when a request names both.

---

## 2. WHAT THE BOARD DRAWS

```text
%% type: architecture
flowchart LR
```

Every node sits in one of six lanes. The lane id is fixed and the label is free: `subgraph service ["Core Services"]`.

| Lane id | Holds |
|---|---|
| `client` | Web, mobile and desktop apps, a CLI, the people using them |
| `gateway` | A CDN, a load balancer, an API gateway, a reverse proxy |
| `service` | Services, a monolith, serverless functions, workers, scheduled jobs |
| `datastore` | Databases, caches, object storage, search indexes |
| `external` | Payment, identity, monitoring and other outside services |
| `async` | Message infrastructure such as a queue or an event stream |

The composer runs the lanes as columns, each a tinted section named after its label. The board stands the lanes in the order client, gateway, service, async, datastore, external, so a queue sits beside the service that writes to it. The accepted lane vocabulary and its check order are unchanged. It assigns each lane's kind: a client takes the `client` role, a gateway the `gateway` role, a service the `neutral` role, a store the `store` role in a cylinder, an outside system the `external` role and a queue the `queue` role in a queue shape, and Assets - Flow Board Design names the swatch each role draws. So every node is written `id[Label]` with no style.

### Allowed edges

| From | To | Edge | Use for |
|---|---|---|---|
| client | gateway | `-->` | A request |
| client | gateway | `<-->` | A live two-way channel, written client first |
| gateway | service | `-->` | Routing |
| service | service | `-->` | An internal call |
| service | service | `<-->` | A streaming channel |
| service | service | `<---` | A return flow, written with the left node first: `orders <---\|"Refund"\| payments` |
| service | datastore | `-->` | A read or a write |
| service | async | `-.->` | Producing events |
| async | service | `-.->` | Consuming events |
| service | external | `-.->` | A call out, labelled `"Service: Purpose"` |

Anything not in the table is wrong by construction, and the fix is the missing lane in between: a gateway between a client and a service, a service between a gateway and a store. So even a simplified board keeps one gateway node. A gateway node named in capability words, such as Entry point, is the lane the check requires and is marked assumed on the source line, not an invented component.

---

## 3. RULES

Check these rule by rule before the gate:

- **`flowchart LR` only,** every node in one of the six lanes, each lane declared once and never nested, and no edge joining a lane
- **Plain `[Label]` nodes and no styling,** since the lane assigns both
- **Only the edges in the table,** and every edge touching `async` or `external` dotted
- **No two edges between the same pair.** Merge them into one edge with one label. Figma's own complete example draws two between a web app and its load balancer, which breaks its own rule, so the stricter rule wins here
- **No cycle among the forward and two-way edges.** A returning flow is a backward edge
- **Every service has a way in and a way out,** and every other node a connector
- **Every edge between two lanes carries a label,** and an edge to an outside system reads `"Service: Purpose"`
- **At most 9 nodes and 12 connectors,** the house diagram guide's general budget, inside Figma's advice of 15 to 20 edges
- The shared rules: labels, quoting, ids, no emoji or markup

Judged by hand:

- **One node is one deployable unit.** Ask whether it can be deployed, restarted or scaled on its own. A module inside a service is not a node
- **A worker that reads a queue is a service, never `async`**
- **A read replica, a shard or change data capture is not its own node** unless the flow addresses it on its own
- **Edge labels are verbs from the source's side,** such as `Reads Users` or `Produces`
- **No diagram carries the same label on four or more edges.** Every edge keeps its label, and each names what its own call does rather than restating the layout
- **Never invent a service, a store or a call to fill a lane, except the gateway the allowed-edge table requires.** An empty lane is honest. Ask one focused question when the system is described only vaguely

---

## 4. BUDGET AND SPLITTING

Draw one flow per diagram. A system with more parts than the budget splits by request path, such as browsing and checkout, each diagram in the same file and named after its path. Name what each path leaves out under `Left out:`. At `Meeting screen` distance edge labels drop to 32 characters. At `Wall` distance the budget drops to 6 nodes and 8 connectors, with labels at 25 characters, as the reading distance dial in Templates - Flow Mode Section 4 sets out.

---

## 5. COLOUR, ZONES AND NOTES

None in the model. The lanes are the zones, and the lane fixes each part's colour. A note on a service, such as its owner or its latency, goes on through the pins and legend recipe in Templates - Flow Hybrid Workflow, which suits a dense architecture best. A `%% focus: <id>` line may name the one node the first glance lands on. It is a comment, so the model stays styleless. Architecture and sequence take no style line. A `%% focus:` line marks their first glance, and it is refused where it names nothing.

---

## 6. WRITING THE BOARD

The model is placed into Assets - Flow Board Composer and one `use_figma` call draws the board, as Templates - Flow Mode Section 6 sets out. On the generated fallback, `generate_diagram` takes `name`, `mermaidSyntax` and `userIntent`. It also takes `useArchitectureLayoutCode` set to `"FIGMA_DIAGRAM_2026"`. Without that value the generator lays the diagram out as an ordinary flowchart.

---

## 7. READ-BACK

Count nodes, connectors and lanes, and check that each node sits inside its lane's section and each edge touching `async` or `external` is dashed.

```text
Read-back: 8 of 8 nodes, 9 of 9 connectors, 6 of 6 lanes
```

---

## 8. PATTERNS AND EXAMPLE

- Assets - Flow Templates - Architecture holds a request path and an event-driven path
- Examples - Flow - Architecture draws a sync path from an engineering doc
