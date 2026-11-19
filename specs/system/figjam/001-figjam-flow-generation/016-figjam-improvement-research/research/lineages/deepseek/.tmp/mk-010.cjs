const fs=require("fs");
const dir="specs/z-staging-po-016-research/research/lineages/deepseek";
const sid="fanout-deepseek-1792527089584-nrdj43";
const reg=JSON.parse(fs.readFileSync(dir+"/findings-registry.json","utf8"));
const kq=reg.keyQuestions.map(q=>q.text);
const now=new Date().toISOString();
const rec={type:"iteration",iteration:10,runId:sid,sessionId:sid,lineageId:sid,mode:"research",target_agent:"deep-research",agent_definition_loaded:true,resolved_route:"Resolved route: mode=research target_agent=deep-research",newInfoRatio:0.42,status:"complete",focus:"Synthesis: twelve ranked improvements, five of them integration changes",findingsCount:12,noveltyJustification:"The synthesis compiles prior findings and adds no new source evidence, so the ratio is set at 0.42 for the new ranking and the evidence-boundary analysis.",keyQuestions:kq,answeredQuestions:[],ruledOut:["Ranking coverage reporting above the run manifest","Proposing a new packet for diagrams","A blanket budget raise from 9 to 25 nodes","An export-and-embed delivery path inside Flow Mode","Preserving manually moved positions during a revision","Mirroring mcp-click-up into the Project","A screenshot as proof of structure"],toolsUsed:["Read","Bash"],sourcesQueried:["specs/z-staging-po-016-research/research/lineages/deepseek/iterations/iteration-001.md","specs/z-staging-po-016-research/research/lineages/deepseek/iterations/iteration-009.md","AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md","specs/z-staging-po-016-research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/references/diagram-house-style.md","specs/z-staging-po-016-research/corpus/ompug__diagram-codebase/docs/DESIGN.md"],timestamp:now,durationMs:600000,graphEvents:[
{type:"node",id:"q-synthesis",kind:"QUESTION",label:"Ranked improvements across the packet and the integration"},
{type:"node",id:"f-rank-1-accent",kind:"FINDING",label:"Accent test and one-message caption"},
{type:"node",id:"f-rank-7-linkback",kind:"FINDING",label:"Write the board URL back into the artifact"},
{type:"node",id:"f-rank-9-order",kind:"FINDING",label:"Form the artifact-then-diagram order"},
{type:"node",id:"src-adobe-house",kind:"SOURCE",label:"diagram-house-style.md",path:"specs/z-staging-po-016-research/corpus/adobe__spectrum-design-data/.ai/skills/spectrum-diagrams/references/diagram-house-style.md"},
{type:"node",id:"src-flow-mode",kind:"SOURCE",label:"flow-mode.md",path:"AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md"},
{type:"edge",id:"e-adobe-supports-accent",source:"src-adobe-house",target:"f-rank-1-accent",relation:"SUPPORTS"},
{type:"edge",id:"e-flow-supports-linkback",source:"src-flow-mode",target:"f-rank-7-linkback",relation:"SUPPORTS"},
{type:"edge",id:"e-accent-answers",source:"f-rank-1-accent",target:"q-synthesis",relation:"ANSWERS"}
]};
const F=[
["f-iter010-001","Rank 1: replace the four-candidate accent menu with Adobe one-node test and a one-message caption that cuts anything not serving it, changing style-guide and quality-rubric.","AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md"],
["f-iter010-002","Rank 2: add a redundant-edge-label rule and a neutral light-to-dark ordering ramp, changing style-guide and the type judged-by-hand lists.","AI Systems/Product Owner/sk-create-figjam/references/style-guide.md"],
["f-iter010-003","Rank 3: add a bounded post-write critic pass over the Mermaid and a screenshot, applied in one batch and stopped by the existing two-attempt bound.","AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md"],
["f-iter010-004","Rank 4: emit a run manifest carrying the fileKey, written node ids, pending action and content hash, the prerequisite for any revision mode.","AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md"],
["f-iter010-005","Rank 5: add a coverage and skipped report beside Left out, accounting for every source item as drawn, split or skipped with a reason.","AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md"],
["f-iter010-006","Rank 6: make the node budget type-specific rather than one global nine, because a gantt or ER legitimately carries more nodes than a user flow, while a flat raise is unsupported.","AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md"],
["f-iter010-007","Rank 7 integration: write the board URL back into the asking artifact, using the Story and Epic Flows reference group or a Doc Visual diagram section, and treat a same-session board as a supplied link.","AI Systems/Product Owner/sk-product-owner/assets/story-template.md"],
["f-iter010-008","Rank 8 integration: carry the artifact into Flow Mode as a source class so labels quote the Story or Doc own words, and pass the artifact reference across the router guard.","AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md"],
["f-iter010-009","Rank 9 integration: form the artifact-then-diagram ordered bundle at stage one instead of asking which comes first when the request names both.","AI Systems/Product Owner/SKILL.md"],
["f-iter010-010","Rank 10 integration: offer ClickUp after a Flow reply and carry the board URL as a body link or comment, never as an attachment.","AI Systems/Product Owner/claude project/Custom Instructions.md"],
["f-iter010-011","Rank 11 integration: carry the Flow Knowledge never-as-the-board qualifier and the image ban into the kernel sentence, which currently offers the model without it.","AI Systems/Product Owner/claude project/Custom Instructions.md"],
["f-iter010-012","Rank 12: define a revision as a scoped rewrite under the same fileKey with a change summary, and state that moved positions cannot be preserved because the generator owns layout.","AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md"]
];
const lines=[JSON.stringify(rec)];
for(const [id,label,src] of F) lines.push(JSON.stringify({type:"finding",id,label,iteration:10,sources:[src]}));
for(const d of rec.ruledOut) lines.push(JSON.stringify({type:"ruled_out",direction:d,reason:"The evidence does not support it; recorded in iteration 10",iteration:10}));
for(const g of rec.graphEvents) lines.push(JSON.stringify({...g,iteration:10}));
fs.writeFileSync(dir+"/deltas/iter-010.jsonl", lines.join("\n")+"\n");
fs.writeFileSync(dir+"/.tmp/iter-010-event.json", JSON.stringify(rec));
console.log("lines",lines.length,"findings",F.length);
