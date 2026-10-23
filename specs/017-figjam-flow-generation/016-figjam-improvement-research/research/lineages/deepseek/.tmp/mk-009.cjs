const fs=require("fs");
const dir="specs/z-staging-po-016-research/research/lineages/deepseek";
const sid="fanout-deepseek-1792527089584-nrdj43";
const reg=JSON.parse(fs.readFileSync(dir+"/findings-registry.json","utf8"));
const kq=reg.keyQuestions.map(q=>q.text);
const now=new Date().toISOString();
const rec={type:"iteration",iteration:9,runId:sid,sessionId:sid,lineageId:sid,mode:"research",target_agent:"deep-research",agent_definition_loaded:true,resolved_route:"Resolved route: mode=research target_agent=deep-research",newInfoRatio:0.87,status:"complete",focus:"The claude.ai Project without a Figma connector, and the ClickUp carrier for a board URL",findingsCount:13,noveltyJustification:"All findings are new to the lineage because the Project packaging and ClickUp transport were not read before, and the ratio is set at 0.87 for the one repeated rule.",keyQuestions:kq,answeredQuestions:[kq[4]],ruledOut:["Mirroring mcp-click-up into the Project","Attaching a board screenshot to a ClickUp task as the carrier","Building a Project-side check script substitute"],toolsUsed:["Read","Bash"],sourcesQueried:["AI Systems/Product Owner/claude project/Custom Instructions.md","AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md","AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md","AI Systems/Product Owner/SYNC.md"],timestamp:now,durationMs:600000,graphEvents:[
{type:"node",id:"q-project-clickup",kind:"QUESTION",label:"Project without a connector and the ClickUp carrier"},
{type:"node",id:"f-no-connector",kind:"FINDING",label:"A Project already stops at a checked model"},
{type:"node",id:"f-parity-sentence",kind:"FINDING",label:"The kernel lacks the mirror never-as-the-board qualifier"},
{type:"node",id:"f-clickup-never-fires",kind:"FINDING",label:"Flow renders no Deliverable Block, so the ClickUp offer never fires"},
{type:"node",id:"src-kernel",kind:"SOURCE",label:"Custom Instructions.md",path:"AI Systems/Product Owner/claude project/Custom Instructions.md"},
{type:"node",id:"src-flow-knowledge",kind:"SOURCE",label:"Flow Mode knowledge mirror",path:"AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md"},
{type:"edge",id:"e-kernel-supports-no-connector",source:"src-kernel",target:"f-no-connector",relation:"SUPPORTS"},
{type:"edge",id:"e-mirror-supports-parity",source:"src-flow-knowledge",target:"f-parity-sentence",relation:"SUPPORTS"},
{type:"edge",id:"e-clickup-answers",source:"f-clickup-never-fires",target:"q-project-clickup",relation:"ANSWERS"}
]};
const F=[
["f-iter009-001","The Project kernel is advisory by construction: no local files, no CLI runtime, no ClickUp except the claude.ai connector, and no claim of a save or push it did not perform.","AI Systems/Product Owner/claude project/Custom Instructions.md"],
["f-iter009-002","Flow is the one exception to the Deliverable Block, and the kernel reproduces the CLI reply contract: board URL, Read-back, Extensions, Left out and HVR self-scan.","AI Systems/Product Owner/claude project/Custom Instructions.md"],
["f-iter009-003","With no Figma connector the kernel says so, never claims a board, and offers the checked model as a fenced Mermaid block labelled as the model.","AI Systems/Product Owner/claude project/Custom Instructions.md"],
["f-iter009-004","The Flow Knowledge mirror states the no-connector fallback more tightly: labelled as the model and never as the board, with no image or HTML stand-in and no Desktop route in a Project.","AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md"],
["f-iter009-005","A parity gap exists inside the package: the kernel omits the mirror never-as-the-board qualifier and image ban, so a kernel-only reader gets a weaker rule.","AI Systems/Product Owner/claude project/Custom Instructions.md"],
["f-iter009-006","A Project cannot execute flow_check.py, so the mirror converts the script into a rule-by-rule check before any write, making the Project check quality depend on mirror fidelity.","AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md"],
["f-iter009-007","ClickUp delivery is body-only and markdown-aware: markdown_description for create and update, H1 as task name, never the plain description field, read back with include description.","AI Systems/Product Owner/claude project/Custom Instructions.md"],
["f-iter009-008","The ClickUp transport supports comment threads and file attachments, but an attachment is a file upload, so it is the wrong carrier for a board URL; a comment or body link is right.","AI Systems/Product Owner/mcp-click-up/references/mcp-tools.md"],
["f-iter009-009","The Story and Epic References block has a Flows sub-label and forbids images and paths, so a board URL under Flows is the one legal backlog carrier, and it survives the ClickUp push verbatim.","AI Systems/Product Owner/sk-product-owner/assets/story-template.md"],
["f-iter009-010","The ClickUp offer never fires for a board because it follows a Deliverable Block and Flow Mode renders none, a one-line integration gap in Flow Mode Delivery.","AI Systems/Product Owner/claude project/Custom Instructions.md"],
["f-iter009-011","The Project has no hub, so the kernel carries the FLOW patterns directly and the stage-two handoff defect does not reproduce there; the equivalent gap is the missing ClickUp offer.","AI Systems/Product Owner/claude project/Custom Instructions.md"],
["f-iter009-012","The parity method is manual and documented, and the records state the kernel v1.2.2 review is pending rather than claiming a reviewed package.","AI Systems/Product Owner/SYNC.md"],
["f-iter009-013","mcp-click-up is deliberately not mirrored into the Project because a Project uses its own connector, so the kernel ClickUp contract is the only Project-side authority.","AI Systems/Product Owner/SYNC.md"]
];
const lines=[JSON.stringify(rec)];
for(const [id,label,src] of F) lines.push(JSON.stringify({type:"finding",id,label,iteration:9,sources:[src]}));
lines.push(JSON.stringify({type:"ruled_out",direction:"Mirroring mcp-click-up into the Project",reason:"A Project uses its own ClickUp connector and the CLI verbs do not exist there",iteration:9}));
lines.push(JSON.stringify({type:"ruled_out",direction:"Attaching a board screenshot to a ClickUp task as the carrier",reason:"Artifact rules forbid images and paths, and a picture cannot prove joins",iteration:9}));
lines.push(JSON.stringify({type:"ruled_out",direction:"Building a Project-side check script substitute",reason:"The mirror already converts the script checks and a Project cannot execute one",iteration:9}));
for(const g of rec.graphEvents) lines.push(JSON.stringify({...g,iteration:9}));
fs.writeFileSync(dir+"/deltas/iter-009.jsonl", lines.join("\n")+"\n");
fs.writeFileSync(dir+"/.tmp/iter-009-event.json", JSON.stringify(rec));
console.log("lines",lines.length,"findings",F.length,"answered",kq[4].slice(0,40));
