const fs=require("fs");
const dir="specs/z-staging-po-016-research/research/lineages/deepseek";
const sid="fanout-deepseek-1792527089584-nrdj43";
const reg=JSON.parse(fs.readFileSync(dir+"/findings-registry.json","utf8"));
const kq=reg.keyQuestions.map(q=>q.text);
const now=new Date().toISOString();
const rec={type:"iteration",iteration:8,runId:sid,sessionId:sid,lineageId:sid,mode:"research",target_agent:"deep-research",agent_definition_loaded:true,resolved_route:"Resolved route: mode=research target_agent=deep-research",newInfoRatio:0.85,status:"complete",focus:"Read-back, revision, fileKey reuse, retry and rollback, read directly",findingsCount:13,noveltyJustification:"Nine findings are new and four extend iteration 4, 5, 6 and 7 rules, giving (9 + 2.0) / 13.",keyQuestions:kq,answeredQuestions:[kq[2]],ruledOut:["Adopting a preserve-positions update model inside Flow Mode","Replacing the model-to-board read-back with a screenshot-only check"],toolsUsed:["Read","Bash"],sourcesQueried:["AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md","AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md","specs/z-staging-po-016-research/corpus/memi-design__mermaid-jam/README.md","specs/z-staging-po-016-research/corpus/ompug__diagram-codebase/README.md","specs/z-staging-po-016-research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/SKILL.md"],timestamp:now,durationMs:600000,graphEvents:[
{type:"node",id:"q-readback-revision",kind:"QUESTION",label:"Read-back, revision, fileKey reuse, failure and retry"},
{type:"node",id:"f-read-before-retry",kind:"FINDING",label:"A timeout is unknown, not failed; read before retry"},
{type:"node",id:"f-two-attempts",kind:"FINDING",label:"Two unrelated skills cap regeneration at two attempts"},
{type:"node",id:"f-all-or-nothing",kind:"FINDING",label:"Revision is all-or-nothing at diagram granularity"},
{type:"node",id:"src-flow-mode",kind:"SOURCE",label:"flow-mode.md",path:"AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md"},
{type:"node",id:"src-adobe-skill",kind:"SOURCE",label:"spectrum-diagrams SKILL.md",path:"specs/z-staging-po-016-research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/SKILL.md"},
{type:"edge",id:"e-flow-supports-retry",source:"src-flow-mode",target:"f-read-before-retry",relation:"SUPPORTS"},
{type:"edge",id:"e-adobe-supports-two",source:"src-adobe-skill",target:"f-two-attempts",relation:"SUPPORTS"},
{type:"edge",id:"e-retry-answers",source:"f-read-before-retry",target:"q-readback-revision",relation:"ANSWERS"}
]};
const F=[
["f-iter008-001","Revision continuity is fileKey-based: the first call creates a file, every later diagram of the same work and every revision passes that fileKey, and one board holds the work.","AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md"],
["f-iter008-002","The retry rule refuses to assume failure means nothing landed: read the target before retrying, retry only when the diagram is absent, and ask the user to look for a first-call draft because there is no fileKey.","AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md"],
["f-iter008-003","Rollback is scoped to what this write created: delete only those nodes and connectors, after the user agrees, and stop if a node to delete was not created by this write.","AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md"],
["f-iter008-004","Mismatch repair reports measured counts, deletes the created nodes and regenerates under the same fileKey only after agreement, because a second write beside the first duplicates; after two attempts, stop and ask.","AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md"],
["f-iter008-005","Adobe independently caps regeneration at two attempts on one complaint and then asks what is wrong, converging with the packet on a bounded retry.","specs/z-staging-po-016-research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/SKILL.md"],
["f-iter008-006","Read-back compares board to model by count, label, endpoints, direction and type extras, and a screenshot read is labelled visual because a picture cannot prove which nodes a connector joins.","AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md"],
["f-iter008-007","The rubric checks the board visually for stretched shapes, cut labels, overlaps with existing content and any post-generation movement, a separate check from the structural read-back.","AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md"],
["f-iter008-008","The plan is fixed before the write because a board in the wrong plan is visible to that plan members as soon as it lands, a confidentiality gate no corpus source has.","AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md"],
["f-iter008-009","Extension failure is explicit partial success: the diagram stands and the reply reports what landed and what did not.","AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md"],
["f-iter008-010","Revision is all-or-nothing at diagram granularity: generated nodes may never be moved, so a bad layout is fixed only by splitting or reshaping, while mermaid-jam preserves moved positions and diagram-codebase regenerates only affected diagrams.","AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md"],
["f-iter008-011","The fj fallback changes read-back semantics because each edge label is a separate text node counted as a label, never a node, so one model yields different counts per route.","AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md"],
["f-iter008-012","With no route the packet refuses a stand-in file, naming what is missing and offering the checked model instead, where every corpus alternative produces an image, a board or Mermaid text.","AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md"],
["f-iter008-013","The 9-node and 12-connector budget with split-not-shrink and ordered cuts is the strictest density rule in the corpus, and the no-move rule is why it protects legibility before the write.","AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md"]
];
const lines=[JSON.stringify(rec)];
for(const [id,label,src] of F) lines.push(JSON.stringify({type:"finding",id,label,iteration:8,sources:[src]}));
lines.push(JSON.stringify({type:"ruled_out",direction:"Adopting a preserve-positions update model inside Flow Mode",reason:"The generator owns layout, so preserved positions cannot be reconciled with the no-move rule",iteration:8}));
lines.push(JSON.stringify({type:"ruled_out",direction:"Replacing the model-to-board read-back with a screenshot-only check",reason:"A picture cannot prove which nodes a connector joins",iteration:8}));
for(const g of rec.graphEvents) lines.push(JSON.stringify({...g,iteration:8}));
fs.writeFileSync(dir+"/deltas/iter-008.jsonl", lines.join("\n")+"\n");
fs.writeFileSync(dir+"/.tmp/iter-008-event.json", JSON.stringify(rec));
console.log("lines",lines.length,"findings",F.length,"answered",kq[2].slice(0,40));
