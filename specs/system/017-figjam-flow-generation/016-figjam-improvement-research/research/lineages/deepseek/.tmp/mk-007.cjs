const fs=require("fs");
const dir="specs/z-staging-po-016-research/research/lineages/deepseek";
const sid="fanout-deepseek-1792527089584-nrdj43";
const reg=JSON.parse(fs.readFileSync(dir+"/findings-registry.json","utf8"));
const kq=reg.keyQuestions.map(q=>q.text);
const now=new Date().toISOString();
const rec={type:"iteration",iteration:7,runId:sid,sessionId:sid,lineageId:sid,mode:"research",target_agent:"deep-research",agent_definition_loaded:true,resolved_route:"Resolved route: mode=research target_agent=deep-research",newInfoRatio:0.88,status:"complete",focus:"Two-stage routing, the one-way Flow handoff, and where a board can legitimately land in an artifact",findingsCount:12,noveltyJustification:"Nine findings are new and three extend iteration 3, 5 and 6 rules, giving (9 + 1.5) / 12.",keyQuestions:kq,answeredQuestions:[kq[3]],ruledOut:["Treating the Flow lane in router-contract.md as loadable","Proposing a file attachment pipeline into ClickUp"],toolsUsed:["Read","Bash"],sourcesQueried:["AI Systems/Product Owner/SKILL.md","AI Systems/Product Owner/ROUTER.md","AI Systems/Product Owner/hub-router.json","AI Systems/Product Owner/mode-registry.json","AI Systems/Product Owner/sk-product-owner/references/router-contract.md","AI Systems/Product Owner/sk-product-owner/references/story-mode.md"],timestamp:now,durationMs:600000,graphEvents:[
{type:"node",id:"q-integration",kind:"QUESTION",label:"Request routing and artifact handoff"},
{type:"node",id:"f-one-way-handoff",kind:"FINDING",label:"The Flow handoff is one-way and terminal"},
{type:"node",id:"f-two-protocols",kind:"FINDING",label:"Artifact export and board read-back are incompatible completions"},
{type:"node",id:"f-story-ban",kind:"FINDING",label:"Story Mode forbids images and invented links"},
{type:"node",id:"src-hub-skill",kind:"SOURCE",label:"Product Owner hub SKILL.md",path:"AI Systems/Product Owner/SKILL.md"},
{type:"node",id:"src-story-mode",kind:"SOURCE",label:"story-mode.md",path:"AI Systems/Product Owner/sk-product-owner/references/story-mode.md"},
{type:"edge",id:"e-hub-supports-handoff",source:"src-hub-skill",target:"f-one-way-handoff",relation:"SUPPORTS"},
{type:"edge",id:"e-story-supports-ban",source:"src-story-mode",target:"f-story-ban",relation:"SUPPORTS"},
{type:"edge",id:"e-handoff-answers",source:"f-one-way-handoff",target:"q-integration",relation:"ANSWERS"}
]};
const F=[
["f-iter007-001","Routing is correctly two-stage: the hub selects one of four modes, ROUTER.md maps intent to packet-qualified leaves, and the packet Section 2 routes inside the packet.","AI Systems/Product Owner/SKILL.md"],
["f-iter007-002","Flow is a sibling route with its own leaf set of flow-mode and flow-templates, after which the FigJam packet adds the chosen type reference and template.","AI Systems/Product Owner/ROUTER.md"],
["f-iter007-003","The handoff is prose, not a resolvable resource: the Product Owner map keeps a FLOW lane that a guard drops, and Section 2 hands the route to the other packet.","AI Systems/Product Owner/sk-product-owner/references/router-contract.md"],
["f-iter007-004","The two halves have incompatible completion protocols: artifacts save to export before replying, while Flow is the sole exemption and answers with a board URL, read-back, Left out and self-scan.","AI Systems/Product Owner/AGENTS.md"],
["f-iter007-005","The Flow reply is terminal and carries the board, its proof and the self-scan and nothing else, so a produced board URL has no route back into the request that motivated it.","AI Systems/Product Owner/sk-create-figjam/references/flow-mode.md"],
["f-iter007-006","An artifact word beats FigJam framing: FigJam beside another artifact is that artifact subject, so a runbook with a FigJam process never loads Flow Mode and the diagram is never produced.","AI Systems/Product Owner/sk-product-owner/references/routing.md"],
["f-iter007-007","Doc Mode preserves supplied diagrams as text but has no instruction to commission a board or insert a board link, which is the doc-first pattern the corpus already documents.","AI Systems/Product Owner/sk-product-owner/references/doc-mode.md"],
["f-iter007-008","Story Mode never invents a Figma destination and forbids images or image paths in a Story or Epic, so a board URL returned later in the session cannot legally be carried.","AI Systems/Product Owner/sk-product-owner/references/story-mode.md"],
["f-iter007-009","The registry records no handoff shape for the FigJam mode: it declares backend, tools, packet and aliases, with no input, artifact served or write-back field.","AI Systems/Product Owner/mode-registry.json"],
["f-iter007-010","Stage one refuses ordered bundles by design, so a Story plus its flow costs a disambiguation question even when the order is obvious.","AI Systems/Product Owner/hub-router.json"],
["f-iter007-011","A Flow request naming an artifact crosses the hub skill, the packet router and the Flow packet before any type guidance loads, and no artifact context is carried across.","AI Systems/Product Owner/SKILL.md"],
["f-iter007-012","ClickUp is a separate vendored transport and templates defer images to ClickUp embedding, so a generated board can only travel as a link in the artifact References groups, never an attachment.","AI Systems/Product Owner/sk-product-owner/assets/story-template.md"]
];
const lines=[JSON.stringify(rec)];
for(const [id,label,src] of F) lines.push(JSON.stringify({type:"finding",id,label,iteration:7,sources:[src]}));
lines.push(JSON.stringify({type:"ruled_out",direction:"Treating the Flow lane in router-contract.md as loadable",reason:"The guard drops it by design",iteration:7}));
lines.push(JSON.stringify({type:"ruled_out",direction:"Proposing a file attachment pipeline into ClickUp",reason:"Templates forbid images and image paths in artifacts",iteration:7}));
for(const g of rec.graphEvents) lines.push(JSON.stringify({...g,iteration:7}));
fs.writeFileSync(dir+"/deltas/iter-007.jsonl", lines.join("\n")+"\n");
fs.writeFileSync(dir+"/.tmp/iter-007-event.json", JSON.stringify(rec));
console.log("lines",lines.length,"findings",F.length,"answered",kq[3].slice(0,40));
