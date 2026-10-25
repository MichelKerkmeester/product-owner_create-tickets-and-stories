// ───────────────────────────────────────────────────────────────
// COMPONENT: FIGJAM BOARD COMPOSER
// ───────────────────────────────────────────────────────────────
// Draws one checked diagram as a framed FigJam board through use_figma: a title
// block, tinted zones, shapes sized to their text, routed connectors, a key and
// a source line, all on an 8 px grid. scripts/compose_board.py fills MODEL from
// a model that passed flow_check.py, so the board holds exactly what was checked.
// Paste the whole file as the use_figma code. Nothing persists between calls, so
// the return value carries every id the read-back needs.
const MODEL = __MODEL__;

const h = (r, g, b) => ({ r: r / 255, g: g / 255, b: b / 255 });
const solid = (c) => [{ type: 'SOLID', color: c }];
const DARK = h(0x1e, 0x1e, 0x1e);
const WHITE = h(0xff, 0xff, 0xff);
const LINE = h(0x75, 0x75, 0x75);
const FAINT = h(0xd9, 0xd9, 0xd9);
const LIFELINE = h(0xb3, 0xb3, 0xb3);
const ASYNC = h(0x3d, 0xad, 0xff);

// FigJam's coordinated pairs, written as hex/255 so the colour picker keeps them as palette swatches.
const SHAPE = {
  white: { fill: WHITE, stroke: h(0xb3, 0xb3, 0xb3), text: DARK },
  black: { fill: DARK, stroke: h(0xb3, 0xb3, 0xb3), text: WHITE },
  darkGray: { fill: LINE, stroke: h(0x5e, 0x5e, 0x5e), text: WHITE },
  violet: { fill: h(0x87, 0x4f, 0xff), stroke: h(0x54, 0x27, 0xb4), text: WHITE },
  lightBlue: { fill: h(0xc2, 0xe5, 0xff), stroke: h(0x3d, 0xad, 0xff), text: DARK },
  lightGreen: { fill: h(0xcd, 0xf4, 0xd3), stroke: h(0x66, 0xd5, 0x75), text: DARK },
  lightYellow: { fill: h(0xff, 0xec, 0xbd), stroke: h(0xff, 0xc9, 0x43), text: DARK },
  lightOrange: { fill: h(0xff, 0xe0, 0xc2), stroke: h(0xff, 0x9e, 0x42), text: DARK },
  lightRed: { fill: h(0xff, 0xcd, 0xc2), stroke: h(0xff, 0x75, 0x56), text: DARK },
  lightViolet: { fill: h(0xdc, 0xcc, 0xff), stroke: h(0x87, 0x4f, 0xff), text: DARK },
  lightPink: { fill: h(0xff, 0xc2, 0xec), stroke: h(0xf8, 0x49, 0xc1), text: DARK },
  lightTeal: { fill: h(0xc6, 0xfa, 0xf6), stroke: h(0x5a, 0xd8, 0xcc), text: DARK },
  lightGray: { fill: FAINT, stroke: h(0xb3, 0xb3, 0xb3), text: DARK },
};
const TINT = {
  gray: h(0xf9, 0xf9, 0xf9), green: h(0xeb, 0xff, 0xee), teal: h(0xf1, 0xfe, 0xfd),
  blue: h(0xf5, 0xfb, 0xff), violet: h(0xf8, 0xf5, 0xff), pink: h(0xff, 0xf0, 0xfa),
  red: h(0xff, 0xf5, 0xf5), orange: h(0xff, 0xf7, 0xf0), yellow: h(0xff, 0xfb, 0xf0),
};
// Cool and warm tints alternate, so two neighbouring zones never read as one.
const TINT_CYCLE = ['blue', 'orange', 'teal', 'yellow', 'violet', 'pink'];

// A kind fixes shape and colour together, so a colour means the same thing on every board.
const KINDS = {
  start: { shape: 'ROUNDED_RECTANGLE', color: 'lightBlue', key: 'Where it starts' },
  screen: { shape: 'ROUNDED_RECTANGLE', color: 'white', key: 'Screen or step' },
  step: { shape: 'ROUNDED_RECTANGLE', color: 'white', key: 'Step' },
  decision: { shape: 'DIAMOND', color: 'lightYellow', key: 'Decision' },
  success: { shape: 'ROUNDED_RECTANGLE', color: 'lightGreen', key: 'Goal reached' },
  exit: { shape: 'ROUNDED_RECTANGLE', color: 'lightOrange', key: 'Leaves the flow' },
  error: { shape: 'ROUNDED_RECTANGLE', color: 'lightRed', key: 'Error or blocked' },
  focus: { shape: 'ROUNDED_RECTANGLE', color: 'lightPink', key: 'In focus' },
  merge: { shape: 'ELLIPSE', color: 'darkGray', key: 'Paths join', fixed: [24, 24] },
  datastore: { shape: 'ENG_DATABASE', color: 'lightViolet', key: 'Data store' },
  subprocess: { shape: 'PREDEFINED_PROCESS', color: 'white', key: 'Sub-process' },
  io: { shape: 'PARALLELOGRAM_RIGHT', color: 'lightTeal', key: 'Input or output' },
  client: { shape: 'ROUNDED_RECTANGLE', color: 'lightTeal', key: 'App or client' },
  gateway: { shape: 'ROUNDED_RECTANGLE', color: 'lightBlue', key: 'Edge or gateway' },
  service: { shape: 'ROUNDED_RECTANGLE', color: 'white', key: 'Service' },
  queue: { shape: 'ENG_QUEUE', color: 'lightOrange', key: 'Queue or stream' },
  external: { shape: 'ROUNDED_RECTANGLE', color: 'lightGray', key: 'Outside system' },
  state: { shape: 'ROUNDED_RECTANGLE', color: 'white', key: 'State' },
  firstState: { shape: 'ROUNDED_RECTANGLE', color: 'lightBlue', key: 'First state' },
  finalState: { shape: 'ROUNDED_RECTANGLE', color: 'lightGray', key: 'Final state' },
  initial: { shape: 'ELLIPSE', color: 'black', key: 'Start', fixed: [32, 32] },
  final: { shape: 'ELLIPSE', color: 'black', key: 'End', fixed: [32, 32], ring: true },
  choice: { shape: 'DIAMOND', color: 'lightYellow', key: 'Choice', fixed: [56, 56] },
  fork: { shape: 'SQUARE', color: 'black', key: 'Fork or join', fixed: [16, 96] },
  entity: { shape: 'SQUARE', color: 'white', key: 'Entity' },
  participant: { shape: 'ROUNDED_RECTANGLE', color: 'lightBlue', key: 'Participant' },
  planned: { shape: 'ROUNDED_RECTANGLE', color: 'white', key: 'Planned' },
  active: { shape: 'ROUNDED_RECTANGLE', color: 'lightBlue', key: 'In progress' },
  done: { shape: 'ROUNDED_RECTANGLE', color: 'lightGray', key: 'Done' },
  crit: { shape: 'ROUNDED_RECTANGLE', color: 'lightRed', key: 'Critical, heavy outline', heavy: true },
  milestone: { shape: 'DIAMOND', color: 'lightYellow', key: 'Milestone', fixed: [32, 32] },
};
const OFF_PATH = new Set(['exit', 'error']);
const ROUND = new Set(['DIAMOND', 'ELLIPSE', 'HEXAGON', 'OCTAGON']);

const GRID = 8;
const snap = (v) => Math.round(v / GRID) * GRID;
const up8 = (v) => Math.ceil(v / GRID) * GRID;
const TYPE = { node: 20, label: 16, title: 64, subtitle: 28, zone: 24, field: 16 };
const PARA = 4;
const RANK_GAP = 136;
const CROSS_GAP = 80;
const ZONE_GAP = 48;
const ZONE_HEAD = 96;
const ZONE_PAD = 48;
const BOARD_PAD = 80;

const MEDIUM = { family: 'Inter', style: 'Medium' };
const REGULAR = { family: 'Inter', style: 'Regular' };
const SEMI = { family: 'Inter', style: 'Semi Bold' };
const BOLD = { family: 'Inter', style: 'Bold' };
await Promise.all([MEDIUM, REGULAR, SEMI, BOLD].map((f) => figma.loadFontAsync(f)));

const warnings = [];
const created = [];
const elements = [];
const links = [];

// ── Measuring ──
const measurer = figma.createText();
measurer.fontName = MEDIUM;
function natural(chars, font, size) {
  measurer.fontName = font;
  measurer.fontSize = size;
  measurer.textAutoResize = 'WIDTH_AND_HEIGHT';
  measurer.characters = chars || ' ';
  return { w: measurer.width, h: measurer.height };
}
// FigJam clips a round shape's text to its inscribed half box, so round shapes get Figma's 32 px inset.
function fit(label, type) {
  const round = ROUND.has(type);
  const tall = type === 'ENG_DATABASE' || type === 'ENG_QUEUE';
  const w0 = round ? 256 : 224;
  const h0 = round ? 160 : (tall ? 128 : 96);
  measurer.fontName = MEDIUM;
  measurer.fontSize = TYPE.node;
  measurer.textAutoResize = 'HEIGHT';
  let w = w0, hh = h0;
  for (let s = 1; s < 3; s += 0.1) {
    w = w0 * s; hh = h0 * s;
    const aw = round ? w / 2 - 32 : w - (type === 'PARALLELOGRAM_RIGHT' ? 96 : 48);
    const ah = round ? hh / 2 - 32 : hh - (tall ? 64 : 40);
    measurer.resize(Math.max(aw, 1), measurer.height);
    measurer.characters = label || ' ';
    if (measurer.height <= ah) break;
  }
  return { w: up8(w), h: up8(hh) };
}

// ── Drawing primitives ──
function text(parent, chars, font, size, x, y, width) {
  const t = figma.createText();
  t.fontName = font;
  t.fontSize = size;
  t.characters = chars;
  t.fills = solid(DARK);
  parent.appendChild(t);
  if (width) { t.textAutoResize = 'HEIGHT'; t.resize(width, t.height); }
  t.x = x;
  t.y = y;
  created.push(t.id);
  return t;
}
// The one accent is the only pink on any board and the only 8 px outline, so it outweighs every kind's
// fill and still reads first in greyscale, where only a line's weight and darkness are left.
function paint(s, kind, accent) {
  const k = KINDS[kind];
  const pair = SHAPE[k.color];
  const hot = accent || kind === 'focus';
  s.fills = solid(pair.fill);
  s.strokes = solid(hot ? SHAPE.lightPink.stroke : (k.ring ? h(0xb3, 0xb3, 0xb3) : pair.stroke));
  try { s.strokeWeight = hot ? 8 : (k.ring ? 6 : (k.heavy ? 4 : 2)); } catch (err) { /* a shape that refuses a weight keeps FigJam's */ }
  return pair;
}
function shape(parent, kind, label, x, y, w, hh, name, size, accent) {
  const s = figma.createShapeWithText();
  s.shapeType = KINDS[kind].shape;
  s.name = name;
  const pair = paint(s, kind, accent);
  if (label) {
    s.text.fontName = MEDIUM;
    s.text.fontSize = size || TYPE.node;
    s.text.characters = label;
    s.text.fills = solid(pair.text);
  }
  s.resize(w, hh);
  parent.appendChild(s);
  s.x = x;
  s.y = y;
  created.push(s.id);
  return s;
}
// An invisible 16 px dot that a connector can hold on to, so the line moves with the board.
function anchor(parent, cx, cy, name) {
  const a = figma.createShapeWithText();
  a.shapeType = 'ELLIPSE';
  a.name = name;
  a.fills = [];
  a.strokes = [];
  a.resize(16, 16);
  parent.appendChild(a);
  a.x = cx - 8;
  a.y = cy - 8;
  created.push(a.id);
  return a;
}
// POINT pins the end to the node's exact centre. A magnet stops short of an anchor's edge, which
// leaves a visible break wherever two legs meet, while a pinned point joins them into one line.
function end(node, magnet) {
  if (magnet === 'POINT') return { endpointNodeId: node.id, position: { x: node.width / 2, y: node.height / 2 } };
  return { endpointNodeId: node.id, magnet: magnet || 'AUTO' };
}
function connect(parent, from, to, o) {
  const c = figma.createConnector();
  parent.appendChild(c);
  c.name = o.name;
  c.connectorLineType = o.line || 'ELBOWED';
  c.connectorStart = end(from, o.m0);
  c.connectorEnd = end(to, o.m1);
  c.connectorStartStrokeCap = o.startCap || 'NONE';
  c.connectorEndStrokeCap = o.endCap === undefined ? 'ARROW_LINES' : o.endCap;
  c.strokes = solid(o.color || LINE);
  c.strokeWeight = o.weight || 2;
  c.dashPattern = o.dashed ? [10, 6] : [];
  if (o.label) {
    c.text.fontName = MEDIUM;
    c.text.fontSize = TYPE.label;
    c.text.characters = o.label;
  }
  created.push(c.id);
  return c;
}
function zoneSection(parent, label, tint, x, y, w, hh) {
  const sec = figma.createSection();
  parent.appendChild(sec);
  sec.name = label;
  sec.x = x;
  sec.y = y;
  sec.resize(w, hh);
  sec.fills = solid(TINT[tint] || TINT.gray);
  created.push(sec.id);
  text(sec, label, SEMI, TYPE.zone, 32, 32);
  return sec;
}

// ── Layered layout ──
// Cut cycles, rank by longest path (or by zone order in stage mode), add a dummy
// in each rank a long edge crosses so no box sits on its line, order ranks by
// barycenter, then place each rank exactly by weighted isotonic regression. The
// spine, the longest on-path route, weighs most and stays on one straight line.
function layered(items, edges, opt) {
  const LR = opt.LR;
  const ids = items.map((n) => n.id);
  const item = new Map(items.map((n) => [n.id, n]));
  const out = new Map(ids.map((id) => [id, []]));
  const inn = new Map(ids.map((id) => [id, []]));
  edges.forEach((e, i) => { e.i = i; out.get(e.from).push(e); inn.get(e.to).push(e); });
  const seen = new Map();
  const cut = new Set();
  const dfs = (u) => {
    seen.set(u, 1);
    for (const e of out.get(u)) {
      const st = seen.get(e.to);
      if (st === 1) cut.add(e.i);
      else if (!st) dfs(e.to);
    }
    seen.set(u, 2);
  };
  ids.filter((id) => !inn.get(id).length).forEach((id) => { if (!seen.get(id)) dfs(id); });
  ids.forEach((id) => { if (!seen.get(id)) dfs(id); });
  const zones = opt.zones || [];
  const zoneIndex = new Map(zones.map((z, i) => [z.id, i]));
  const stage = opt.zoneMode === 'stage' && zones.length && items.every((n) => zoneIndex.has(n.zone));
  const rank = new Map();
  const longest = (sameZoneOnly) => {
    const indeg = new Map(ids.map((id) => [id, 0]));
    const usable = edges.filter((e) => !cut.has(e.i) && (!sameZoneOnly || item.get(e.from).zone === item.get(e.to).zone));
    usable.forEach((e) => indeg.set(e.to, indeg.get(e.to) + 1));
    const queue = ids.filter((id) => !indeg.get(id));
    const local = new Map(ids.map((id) => [id, 0]));
    while (queue.length) {
      const u = queue.shift();
      for (const e of usable.filter((x) => x.from === u)) {
        local.set(e.to, Math.max(local.get(e.to), local.get(u) + 1));
        indeg.set(e.to, indeg.get(e.to) - 1);
        if (!indeg.get(e.to)) queue.push(e.to);
      }
    }
    return local;
  };
  if (stage) {
    const local = longest(true);
    let base = 0;
    for (const z of zones) {
      const members = ids.filter((id) => item.get(id).zone === z.id);
      members.forEach((id) => rank.set(id, base + local.get(id)));
      base += members.length ? Math.max(...members.map((id) => local.get(id))) + 1 : 0;
    }
  } else {
    longest(false).forEach((v, id) => rank.set(id, v));
  }
  const back = new Set(edges.filter((e) => rank.get(e.to) <= rank.get(e.from)).map((e) => e.i));
  const forward = edges.filter((e) => !back.has(e.i));

  const best = new Map();
  const prev = new Map();
  const tied = new Map();
  const byRank = [...ids].sort((a, b) => rank.get(a) - rank.get(b));
  for (const u of byRank) {
    if (item.get(u).offPath) continue;
    if (!best.has(u)) best.set(u, 1);
    for (const e of forward.filter((x) => x.from === u)) {
      if (item.get(e.to).offPath) continue;
      if ((best.get(e.to) || 0) < best.get(u) + 1) { best.set(e.to, best.get(u) + 1); tied.set(e.to, [u]); }
      else if (best.get(e.to) === best.get(u) + 1) tied.get(e.to).push(u);
    }
  }
  // Where several steps lead equally far into one, the spine runs through the middle one, so the steps that
  // feed a node sit on both sides of it and none has to loop round the others to reach it.
  tied.forEach((list, id) => prev.set(id, list[(list.length - 1) >> 1]));
  let tail = null;
  for (const u of byRank) {
    if (!best.has(u)) continue;
    if (!tail || best.get(u) > best.get(tail) || (best.get(u) === best.get(tail) && item.get(u).goal)) tail = u;
  }
  const spine = new Set();
  for (let u = tail; u; u = prev.get(u)) spine.add(u);

  const maxRank = Math.max(0, ...rank.values());
  const ranks = Array.from({ length: maxRank + 1 }, () => []);
  ids.forEach((id) => ranks[rank.get(id)].push(id));
  const crossSize = new Map(items.map((n) => [n.id, LR ? n.h : n.w]));
  const rankSize = new Map(items.map((n) => [n.id, LR ? n.w : n.h]));
  const lane = new Map(items.map((n) => [n.id, zoneIndex.has(n.zone) ? zoneIndex.get(n.zone) : zones.length]));
  const nb = new Map([...ids].map((id) => [id, { p: [], s: [] }]));
  const dummies = [];
  const chain = new Map();
  for (const e of forward) {
    let last = e.from;
    for (let r = rank.get(e.from) + 1; r < rank.get(e.to); r++) {
      const d = `~${e.i}~${r}`;
      dummies.push(d);
      if (!chain.has(e.i)) chain.set(e.i, []);
      chain.get(e.i).push(d);
      rank.set(d, r);
      ranks[r].push(d);
      crossSize.set(d, 16);
      lane.set(d, lane.get(e.from));
      nb.set(d, { p: [], s: [] });
      nb.get(last).s.push(d);
      nb.get(d).p.push(last);
      last = d;
    }
    nb.get(last).s.push(e.to);
    nb.get(e.to).p.push(last);
  }
  const order = new Map();
  const reindex = () => ranks.forEach((list) => list.forEach((id, i) => order.set(id, i)));
  reindex();
  const laneMode = opt.zoneMode === 'lane';
  // Stacked zones are bands on the cross axis, each laid out on its own and then set one after the
  // other, so no two can overlap. Group zones start loose and are stacked only when loose ones clash.
  const stacked = laneMode || !!opt.stack;
  const zoned = opt.zoneMode === 'group' && !stacked;
  const sortRank = (list, side) => {
    const key = new Map(list.map((id) => {
      const ns = nb.get(id)[side];
      return [id, ns.length ? ns.reduce((a, v) => a + order.get(v), 0) / ns.length : order.get(id)];
    }));
    list.sort((a, b) => {
      if (stacked && lane.get(a) !== lane.get(b)) return lane.get(a) - lane.get(b);
      if (key.get(a) !== key.get(b)) return key.get(a) - key.get(b);
      if (spine.has(a) !== spine.has(b)) return spine.has(a) ? -1 : 1;
      const oa = item.has(a) && item.get(a).offPath, ob = item.has(b) && item.get(b).offPath;
      if (oa !== ob) return oa ? 1 : -1;
      return 0;
    });
    // Equal ties stand with the spine in the middle, so the steps beside it spread to both sides.
    const off = (id) => item.has(id) && item.get(id).offPath;
    for (let i = 0, j; i < list.length; i = j) {
      for (j = i + 1; j < list.length && key.get(list[j]) === key.get(list[i]) && lane.get(list[j]) === lane.get(list[i]) && off(list[j]) === off(list[i]); j++);
      if (j - i > 2 && spine.has(list[i]) && !off(list[i])) list.splice(i + ((j - i - 1) >> 1), 0, list.splice(i, 1)[0]);
    }
  };
  for (let pass = 0; pass < 2; pass++) {
    for (let r = 1; r <= maxRank; r++) { sortRank(ranks[r], 'p'); reindex(); }
    for (let r = maxRank - 1; r >= 0; r--) { sortRank(ranks[r], 's'); reindex(); }
  }
  const cross = new Map();
  const pav = (rows) => {
    const blocks = [];
    for (const it of rows) {
      blocks.push({ sum: it.w * (it.d - it.off), w: it.w, n: 1 });
      while (blocks.length > 1) {
        const b2 = blocks[blocks.length - 1], b1 = blocks[blocks.length - 2];
        if (b1.sum / b1.w <= b2.sum / b2.w) break;
        blocks.splice(blocks.length - 2, 2, { sum: b1.sum + b2.sum, w: b1.w + b2.w, n: b1.n + b2.n });
      }
    }
    const q = [];
    for (const b of blocks) for (let k = 0; k < b.n; k++) q.push(b.sum / b.w);
    return rows.map((it, i) => q[i] + it.off);
  };
  const gapBetween = (a, b) => (zoned && lane.get(a) !== lane.get(b) ? CROSS_GAP + ZONE_HEAD + ZONE_PAD + ZONE_GAP : CROSS_GAP);
  const place = (whole, desired) => {
    const parts = stacked ? [...new Set(whole.map((id) => lane.get(id)))].map((k) => whole.filter((id) => lane.get(id) === k)) : [whole];
    for (const list of parts) {
      let off = 0;
      const rows = list.map((id, i) => {
        if (i > 0) off += (crossSize.get(list[i - 1]) + crossSize.get(id)) / 2 + gapBetween(list[i - 1], id);
        return spine.has(id) ? { d: 0, w: 1000, off } : { d: desired(id), w: 1, off };
      });
      pav(rows).forEach((p, i) => cross.set(list[i], p));
    }
  };
  // A stacked band is set against its own members only, because the bands move apart afterwards.
  const meanOf = (all, id) => {
    const ns = stacked ? all.filter((v) => lane.get(v) === lane.get(id)) : all;
    return ns.length ? ns.reduce((a, v) => a + cross.get(v), 0) / ns.length : cross.get(id);
  };
  ranks.forEach((list) => place(list, () => 0));
  for (let pass = 0; pass < 3; pass++) {
    for (let r = 1; r <= maxRank; r++) place(ranks[r], (id) => meanOf(nb.get(id).p, id));
    if (pass < 2) for (let r = maxRank - 1; r >= 0; r--) place(ranks[r], (id) => meanOf(nb.get(id).s, id));
  }
  const zoneOfRank = ranks.map((list) => {
    const real = list.filter((id) => item.has(id));
    return real.length ? item.get(real[0]).zone : null;
  });
  const extent = ranks.map((list) => Math.max(16, ...list.map((id) => rankSize.get(id) || 16)));
  const zonesAt = ranks.map((list) => [...new Set(list.filter((id) => item.has(id)).map((id) => item.get(id).zone || ''))].sort().join('|'));
  // A gap is as wide as the widest label that sits in it, so a label never touches a box. A gap at a
  // zone boundary also loses a zone pad on each side to the zone's own edge.
  const labelGap = (r) => Math.max(0, ...forward.filter((e) => rank.get(e.to) === r && rank.get(e.from) === r - 1)
    .map((e) => (LR ? (e.lw || 0) + 64 : 0)));
  const centre = [];
  const gapMid = [];
  let pos = 0;
  for (let r = 0; r <= maxRank; r++) {
    if (r > 0) {
      const boundary = (stage && zoneOfRank[r] !== zoneOfRank[r - 1])
        || (opt.zoneMode === 'group' && zonesAt[r] !== zonesAt[r - 1]);
      const floor = boundary ? Math.max(RANK_GAP, ZONE_PAD + ZONE_GAP + (LR ? ZONE_PAD : ZONE_HEAD)) : RANK_GAP;
      const gap = up8(Math.max(labelGap(r) + (boundary && LR ? 2 * ZONE_PAD : 0), floor));
      gapMid[r] = pos + gap / 2;
      pos += gap;
    }
    centre[r] = pos + extent[r] / 2;
    pos += extent[r];
  }
  const box = new Map();
  for (const n of items) {
    const c = snap(cross.get(n.id)), rc = snap(centre[rank.get(n.id)]);
    const cx = LR ? rc : c, cy = LR ? c : rc;
    box.set(n.id, { x: cx - n.w / 2, y: cy - n.h / 2, w: n.w, h: n.h });
  }
  // A long edge passes the ranks between its ends through the slot its dummies reserved. Its two
  // waypoints sit in the gaps before and after that slot, so every bend falls between ranks.
  const point = (along, across) => (LR ? { x: along, y: across } : { x: across, y: along });
  const waypoints = new Map();
  for (const [i, ds] of chain) {
    const first = ds[0], last = ds[ds.length - 1];
    waypoints.set(i, {
      lane: lane.get(first),
      a: point(snap(gapMid[rank.get(first)]), snap(cross.get(first))),
      b: point(snap(gapMid[rank.get(last) + 1]), snap(cross.get(last))),
    });
  }
  // A band is as tall as its boxes and the slots its long edges pass through, and no taller.
  const laneSpan = new Map();
  if (stacked && zones.length) {
    let prevEnd = null;
    for (let k = 0; k <= zones.length; k++) {
      const members = items.filter((n) => lane.get(n.id) === k).map((n) => n.id);
      if (!members.length) continue;
      const spans = members.map((id) => { const b = box.get(id); return LR ? [b.y, b.y + b.h] : [b.x, b.x + b.w]; })
        .concat(dummies.filter((d) => lane.get(d) === k).map((d) => [snap(cross.get(d)) - 8, snap(cross.get(d)) + 8]));
      const lo = Math.min(...spans.map((v) => v[0]));
      const hi = Math.max(...spans.map((v) => v[1]));
      const start = lo - (LR ? ZONE_HEAD : ZONE_PAD);
      const delta = prevEnd === null ? 0 : prevEnd + ZONE_GAP - start;
      members.forEach((id) => { const b = box.get(id); if (LR) b.y += delta; else b.x += delta; });
      for (const w of waypoints.values()) {
        if (w.lane !== k) continue;
        for (const p of [w.a, w.b]) { if (LR) p.y += delta; else p.x += delta; }
      }
      laneSpan.set(k, [lo + delta, hi + delta]);
      prevEnd = hi + delta + ZONE_PAD;
    }
  }
  const all = [...box.values()];
  const ext = {
    x0: Math.min(...all.map((b) => b.x)), y0: Math.min(...all.map((b) => b.y)),
    x1: Math.max(...all.map((b) => b.x + b.w)), y1: Math.max(...all.map((b) => b.y + b.h)),
  };
  const zoneBox = zones.map((z, i) => {
    const members = items.filter((n) => n.zone === z.id).map((n) => box.get(n.id));
    if (!members.length) return null;
    let x0 = Math.min(...members.map((b) => b.x)), y0 = Math.min(...members.map((b) => b.y));
    let x1 = Math.max(...members.map((b) => b.x + b.w)), y1 = Math.max(...members.map((b) => b.y + b.h));
    if (stacked) { const [lo, hi] = laneSpan.get(i); if (LR) { y0 = lo; y1 = hi; } else { x0 = lo; x1 = hi; } }
    if (opt.zoneMode === 'lane') { if (LR) { x0 = ext.x0; x1 = ext.x1; } else { y0 = ext.y0; y1 = ext.y1; } }
    // A back edge inside the zone detours one pad past its boxes, which would lay it on the zone's
    // edge, so that side gets a second pad.
    const loops = edges.some((e) => back.has(e.i) && item.get(e.from).zone === z.id && item.get(e.to).zone === z.id);
    const extra = loops ? ZONE_PAD : 0;
    return { x: x0 - ZONE_PAD, y: y0 - ZONE_HEAD, w: x1 - x0 + 2 * ZONE_PAD + (LR ? 0 : extra),
      h: y1 - y0 + ZONE_HEAD + ZONE_PAD + (LR ? extra : 0) };
  });
  const clash = [];
  if (opt.zoneMode === 'group') {
    zoneBox.forEach((a, i) => {
      if (!a) return;
      zoneBox.forEach((b, j) => {
        if (b && j > i && a.x < b.x + b.w && b.x < a.x + a.w && a.y < b.y + b.h && b.y < a.y + a.h) {
          clash.push(`zones ${zones[i].id} and ${zones[j].id} overlap`);
        }
      });
      items.forEach((n) => {
        const b = box.get(n.id);
        if (n.zone !== zones[i].id && b.x < a.x + a.w && a.x < b.x + b.w && b.y < a.y + a.h && a.y < b.y + b.h) {
          clash.push(`node ${n.id} sits inside zone ${zones[i].id} without belonging to it`);
        }
      });
    });
  }
  const frames = [...all, ...zoneBox.filter(Boolean)];
  const dx = Math.min(...frames.map((b) => b.x)), dy = Math.min(...frames.map((b) => b.y));
  for (const b of [...all, ...zoneBox.filter(Boolean)]) { b.x -= dx; b.y -= dy; }
  for (const w of waypoints.values()) for (const p of [w.a, w.b]) { p.x -= dx; p.y -= dy; }
  return {
    box, zoneBox, back, rank, spine, LR, clash,
    waypoints,
    width: Math.max(...frames.map((b) => b.x + b.w)),
    height: Math.max(...frames.map((b) => b.y + b.h)),
    hasForward: (id) => forward.some((e) => e.from === id),
    outCount: (id) => forward.filter((e) => e.from === id).length,
    inCount: (id) => forward.filter((e) => e.to === id).length,
  };
}

// ── Graph: user flow, process, architecture, state and ER ──
function entityCard(n) {
  const lines = (n.fields || []).map((f) => [f.keys, f.name, f.type].filter(Boolean).join('  '));
  const titleSize = natural(n.label, SEMI, TYPE.node);
  const widest = Math.max(titleSize.w, ...lines.map((l) => natural(l, REGULAR, TYPE.field).w));
  // Every paragraph adds its spacing on top of its line, and a field line is budgeted at 24 px at least,
  // so the last field keeps clear of the card's bottom edge.
  const fieldLine = Math.max(24, natural('Ag', REGULAR, TYPE.field).h);
  return { lines, w: Math.max(224, up8(widest + 64)), h: up8(48 + titleSize.h + PARA + lines.length * (fieldLine + PARA)) };
}
function buildGraph(M) {
  const LR = (M.direction || 'LR') === 'LR';
  const cards = new Map();
  const items = M.nodes.map((n) => {
    if (!KINDS[n.kind]) { warnings.push(`kind ${n.kind} on ${n.id} is unknown, drawn as a step`); n.kind = 'step'; }
    const k = KINDS[n.kind];
    let s;
    if (k.fixed) s = { w: k.fixed[0], h: k.fixed[1] };
    else if (n.kind === 'entity') { const card = entityCard(n); cards.set(n.id, card); s = { w: card.w, h: card.h }; }
    else s = fit(n.label, k.shape);
    return { id: n.id, w: s.w, h: s.h, zone: n.zone, offPath: OFF_PATH.has(n.kind), goal: n.kind === 'success', kind: n.kind };
  });
  // One size per shape class keeps a rhythm across the board.
  const classMax = new Map();
  for (const it of items) {
    if (KINDS[it.kind].fixed || it.kind === 'entity') continue;
    const cls = KINDS[it.kind].shape;
    const m = classMax.get(cls) || { w: 0, h: 0 };
    classMax.set(cls, { w: Math.max(m.w, it.w), h: Math.max(m.h, it.h) });
  }
  for (const it of items) {
    if (KINDS[it.kind].fixed || it.kind === 'entity') continue;
    Object.assign(it, classMax.get(KINDS[it.kind].shape));
  }
  const nodeIds = new Set(M.nodes.map((n) => n.id));
  const zoneIds = new Set((M.zones || []).map((z) => z.id));
  const edges = M.edges.filter((e) => {
    const ok = (nodeIds.has(e.from) || zoneIds.has(e.from)) && (nodeIds.has(e.to) || zoneIds.has(e.to));
    if (!ok) warnings.push(`edge ${e.from} -> ${e.to} names a missing node`);
    return ok;
  });
  edges.forEach((e) => { e.lw = e.label ? natural(e.label, MEDIUM, TYPE.label).w : 0; });
  // An edge to a composite state is laid out against its first member and drawn to the zone itself.
  const firstOf = (zid) => (M.nodes.find((n) => n.zone === zid) || {}).id;
  const layoutEdges = edges
    .map((e) => ({ from: zoneIds.has(e.from) ? firstOf(e.from) : e.from, to: zoneIds.has(e.to) ? firstOf(e.to) : e.to, lw: e.lw }))
    .filter((e) => e.from && e.to && e.from !== e.to);
  const zones = (M.zones || []).map((z, i) => ({ ...z, tint: z.tint || TINT_CYCLE[i % TINT_CYCLE.length] }));
  let L = layered(items, layoutEdges, { LR, zones, zoneMode: M.zoneMode });
  if (L.clash.length) L = layered(items, layoutEdges, { LR, zones, zoneMode: M.zoneMode, stack: true });
  // A board whose zones lie on each other is worse than no board, so it is refused before anything is drawn.
  if (L.clash.length) throw new Error(`nothing was drawn: ${L.clash.join(', ')}`);
  zones.forEach((z, i) => { if (!L.zoneBox[i]) warnings.push(`zone ${z.id} holds no node`); });
  const boxOf = (id) => L.box.get(id) || L.zoneBox[zones.findIndex((z) => z.id === id)];
  // Ports. Every route an edge could take, from any side of its source to any side of its target, is
  // priced. FigJam bends a plain connector itself, so that is judged by every bend it might choose. A
  // pinned route runs through anchors and keeps the bends picked here, so it can take a longer stub, which
  // keeps edges that leave one side off one line. A route that meets a box or a title or rides a zone's
  // border is out, and one that crosses another edge, lies along it, shares its magnet or sits under its
  // label costs more. A node has four magnets, so every edge takes its own while one is free.
  // A pinned route costs PINNED besides, so a plain connector wins wherever it reads as well.
  const DIR = { LEFT: [-1, 0], RIGHT: [1, 0], TOP: [0, -1], BOTTOM: [0, 1] };
  const MAGS = Object.keys(DIR);
  const STUB = 48, CLEAR = 8, BLOCKED = 100000, SHARED = 10000, NEAR = 1500;
  const CLASH = 6000, PINNED = 200, LAP = 56, TITLE_GAP = 8, CORNER = 40, BENT = 3000, RESTARTS = 6, RIM = 16, INSIDE = 40, LANE = 16, AIR = 8, SIDE = 56, SIDEBY = 3000, ARRIVE = 600, MERGE = 3, MERGE_MAX = 200, DETOUR = 2;
  const GAPS = [24, STUB, 72];
  const dock = (id, m) => {
    const b = boxOf(id), v = DIR[m];
    return { x: b.x + (b.w / 2) * (1 + v[0]), y: b.y + (b.h / 2) * (1 + v[1]) };
  };
  // A zone's title, and the levels just above and below it where a run can pass without touching it.
  const heads = zones.map((z, i) => {
    const b = L.zoneBox[i], t = b && natural(z.label, SEMI, TYPE.zone);
    return b && { x: b.x + 32, y: b.y + 32, w: t.w, h: t.h };
  }).filter(Boolean);
  // A zone's border, and the levels in the gap beside it where a run clears both zones. A stub that ends
  // on a border is the usual way a run comes to lie along it, so the gap's middle is a stub length too.
  const rims = L.zoneBox.filter(Boolean).flatMap((z) => [
    { h: true, k: z.y, a: z.x, b: z.x + z.w, o: -1 }, { h: true, k: z.y + z.h, a: z.x, b: z.x + z.w, o: 1 },
    { h: false, k: z.x, a: z.y, b: z.y + z.h, o: -1 }, { h: false, k: z.x + z.w, a: z.y, b: z.y + z.h, o: 1 }]);
  const side = (h) => rims.filter((r) => r.h === h).map((r) => r.k + 24 * r.o);
  const levels = heads.flatMap((t) => [t.y - 16, t.y + t.h + 16]).concat(side(true));
  const cols = side(false);
  const tidy = (pts) => pts.reduce((o, v) => {
    const u = o[o.length - 1], t = o[o.length - 2];
    if (u && u.x === v.x && u.y === v.y) return o;
    if (t && (u.x - t.x) * (v.y - u.y) === (u.y - t.y) * (v.x - u.x)) o.pop();
    o.push(v);
    return o;
  }, []);
  const forward = (pts) => pts.every((v, i) => i < 2 || (v.x - pts[i - 1].x) * (pts[i - 1].x - pts[i - 2].x) + (v.y - pts[i - 1].y) * (pts[i - 1].y - pts[i - 2].y) >= 0);
  // Every right-angle path that leaves p straight out of m, turns at right angles, never doubles back and
  // arrives straight in, with stubs of s0 and s1: the two single bends, then a middle run at the halfway
  // level and, when `extra` is set, at a level that clears a title. Two ports closer than a stub cannot
  // both leave and arrive straight, so the stubs are dropped then.
  const walk = (p, m, q, n, s0, s1, extra) => {
    const a = m ? { x: p.x + DIR[m][0] * s0, y: p.y + DIR[m][1] * s0 } : p;
    const z = n ? { x: q.x + DIR[n][0] * s1, y: q.y + DIR[n][1] * s1 } : q;
    const near = (v, lo, hi) => v > Math.min(lo, hi) - 96 && v < Math.max(lo, hi) + 96;
    const xs = [(a.x + z.x) / 2, ...(extra ? cols.filter((v) => near(v, a.x, z.x)) : [])];
    const ys = [(a.y + z.y) / 2, ...(extra ? levels.filter((v) => near(v, a.y, z.y)) : [])];
    const found = [[{ x: z.x, y: a.y }], [{ x: a.x, y: z.y }], ...xs.map((x) => [{ x, y: a.y }, { x, y: z.y }]), ...ys.map((y) => [{ x: a.x, y }, { x: z.x, y }])]
      .map((mid) => [p, a, ...mid, z, q].filter((v, i, all) => !i || v.x !== all[i - 1].x || v.y !== all[i - 1].y))
      .filter(forward).map(tidy);
    return found.length || !(s0 || s1) ? found : walk(p, m, q, n, 0, 0, extra);
  };
  const plen = (pts) => pts.reduce((t, v, i) => t + (i ? Math.abs(v.x - pts[i - 1].x) + Math.abs(v.y - pts[i - 1].y) : 0), 0);
  const line = (pts) => ({ pts, n: plen(pts), s: pts.slice(1).map((v, i) => {
    const u = pts[i], h = u.y === v.y;
    return { h, k: h ? u.y : u.x, a: h ? Math.min(u.x, v.x) : Math.min(u.y, v.y), b: h ? Math.max(u.x, v.x) : Math.max(u.y, v.y) };
  }) });
  const uniq = (list) => {
    const seen = new Set();
    return list.filter((l) => { const k = l.pts.map((v) => `${v.x},${v.y}`).join(' '); return !seen.has(k) && seen.add(k); });
  };
  // The cheapest such paths, which is where FigJam's own route is likely to fall.
  const bends = (p, m, q, n) => {
    const all = walk(p, m, q, n, STUB, STUB).map(line);
    const best = Math.min(...all.map((l) => l.n));
    return uniq(all.filter((l) => l.n <= best + 1));
  };
  // A bend that lands on another line reads as a crossing too, so a touch counts unless both lines end
  // there, or it joins two edges on the last stretch they merge along into one magnet.
  const tips = (l) => [l.pts[0], l.pts[l.pts.length - 1]];
  const on = (s, x, y) => (s.h ? y === s.k && x >= s.a && x <= s.b : x === s.k && y >= s.a && y <= s.b);
  const crossing = (l, o) => l.s.some((s) => o.s.some((t) => {
    if (s.h === t.h || t.k < s.a || t.k > s.b || s.k < t.a || s.k > t.b) return false;
    const x = s.h ? t.k : s.k, y = s.h ? s.k : t.k, at = (v) => v.x === x && v.y === y;
    const [lz, oz] = [tips(l)[1], tips(o)[1]];
    const joined = lz.x === oz.x && lz.y === oz.y && on(l.s[l.s.length - 1], x, y) && on(o.s[o.s.length - 1], x, y);
    return !joined && !(tips(l).some(at) && tips(o).some(at));
  }));
  const lap = (l, o, gap = LANE) => Math.max(0, ...l.s.flatMap((s) => o.s.filter((t) => s.h === t.h && Math.abs(s.k - t.k) < gap).map((t) => Math.min(s.b, t.b) - Math.max(s.a, t.a))));
  const lapped = (l, o, gap) => lap(l, o, gap) > LAP;
  // An edge keeps out of every zone it neither starts nor ends in. A lane spans the board, so lanes are the exception.
  const strays = (l, homes) => M.zoneMode !== 'lane' && zones.some((z, i) => L.zoneBox[i] && !homes.includes(z.id) && cuts(l.pts, L.zoneBox[i], 0));
  const rides = (l) => l.s.some((s) => rims.some((r) => r.h === s.h && (s.k - r.k) * r.o > -INSIDE && (s.k - r.k) * r.o < RIM && Math.min(r.b, s.b) - Math.max(r.a, s.a) > 0));
  // Whether the path reaches into a box, or comes within `gap` of it.
  const cuts = (pts, b, gap) => pts.slice(1).some((v, i) => {
    const u = pts[i];
    return Math.min(u.x, v.x) < b.x + b.w + gap - 1 && Math.max(u.x, v.x) > b.x - gap + 1
      && Math.min(u.y, v.y) < b.y + b.h + gap - 1 && Math.max(u.y, v.y) > b.y - gap + 1;
  });
  const touch = (r, b) => cuts([{ x: r.x, y: r.y }, { x: r.x + r.w, y: r.y + r.h }], b, 0);
  const crossed = (pts, gap) => items.filter((n) => cuts(pts, L.box.get(n.id), gap)).map((n) => n.id);
  const jobs = [];
  const portsOf = new Map();
  const taken = new Set();
  edges.forEach((e) => {
    const le = !zoneIds.has(e.from) && !zoneIds.has(e.to)
      ? layoutEdges.find((x) => x.from === e.from && x.to === e.to && !taken.has(x.i)) : null;
    if (le) taken.add(le.i);
    const job = { e, route: le && L.waypoints.get(le.i), plain: !!boxOf(e.from) && !!boxOf(e.to) };
    portsOf.set(e, job);
    if (job.plain) jobs.push(job);
  });
  // A label sits on the middle of its connector: of the whole path when FigJam bends it, and of the
  // longest run when the route is pinned, where the label rides that run's own leg.
  const labelAt = (job, ln, pinned) => {
    let leg = 0, d = ln.n / 2;
    if (pinned) {
      ln.s.forEach((s, i) => { if (s.b - s.a > ln.s[leg].b - ln.s[leg].a) leg = i; });
      d = ln.s.slice(0, leg).reduce((t, s) => t + s.b - s.a, 0) + (ln.s[leg].b - ln.s[leg].a) / 2;
    }
    let at = ln.pts[ln.pts.length - 1];
    for (let i = 1; i < ln.pts.length; i++) {
      const u = ln.pts[i - 1], v = ln.pts[i], run = Math.abs(v.x - u.x) + Math.abs(v.y - u.y);
      if (run && d <= run) { at = { x: u.x + (v.x - u.x) * d / run, y: u.y + (v.y - u.y) * d / run }; break; }
      d -= run;
    }
    const w = job.e.lw + 16;
    return { x: at.x - w / 2, y: at.y - 12, w, h: 24, leg };
  };
  // Every route a job can take, each priced for what it meets on its own: boxes, titles and its label.
  let serial = 0;
  const options = (job) => {
    const e = job.e, mine = [e.from, e.to], list = [];
    const [fb, tb] = [boxOf(e.from), boxOf(e.to)];
    // The least any route between the two could run, which a route is held against so a loop round the others costs.
    const reach = Math.max(0, Math.abs(fb.x + fb.w / 2 - tb.x - tb.w / 2) - (fb.w + tb.w) / 2) + Math.max(0, Math.abs(fb.y + fb.h / 2 - tb.y - tb.h / 2) - (fb.h + tb.h) / 2);
    const homes = mine.map((id) => (zoneIds.has(id) ? id : (M.nodes.find((n) => n.id === id) || {}).zone));
    // A transition from a state to itself is left to FigJam, which loops it over the top.
    if (e.from === e.to) return [{ id: ++serial, m0: 'TOP', m1: 'TOP', lines: [line([dock(e.from, 'TOP')])], labs: [], fixed: 0 }];
    const judge = (lines, m0, m1, pinned) => {
      const ok = lines.filter((l) => !crossed(l.pts, 0).some((id) => mine.includes(id))
        && !mine.some((id) => zoneIds.has(id) && cuts(l.pts, boxOf(id), 0)));
      if (!ok.length) return;
      const hits = (gap) => ok.some((l) => crossed(l.pts, gap).some((id) => !mine.includes(id)));
      const labs = e.label ? ok.map((l) => labelAt(job, l, pinned)) : [];
      const bad = hits(0) || ok.some((l) => rides(l) || strays(l, homes) || heads.some((t) => cuts(l.pts, t, TITLE_GAP))) || labs.some((r) => heads.some((t) => touch(r, t)));
      const onNode = labs.some((r) => items.some((n) => !mine.includes(n.id) && touch(r, L.box.get(n.id))));
      list.push({ id: ++serial, m0, m1, lines: ok, labs, pinned, bad, leg: labs.length ? labs[0].leg : 0,
        fixed: ok[0].n + DETOUR * Math.max(0, ok[0].n - reach - 240) + CORNER * (ok[0].pts.length - 2) + (bad ? BLOCKED : 0) + (hits(CLEAR) ? NEAR : 0) + (onNode ? CLASH : 0)
          + (L.spine.has(e.from) && L.spine.has(e.to) && ok.some((l) => l.pts.length > 2) ? BENT : 0) });
    };
    for (const m0 of MAGS) {
      for (const m1 of MAGS) {
        const p = dock(e.from, m0), q = dock(e.to, m1);
        const sets = [];
        // A long edge keeps the track its dummies reserved, and may also leave it, so a track that falls
        // along a zone's border is not the only way across.
        if (job.route) {
          sets.push(GAPS.flatMap((s0) => GAPS.flatMap((s1) => {
            const legs = [walk(p, m0, job.route.a, null, s0, 0), walk(job.route.a, null, job.route.b, null, 0, 0), walk(job.route.b, null, q, m1, 0, s1)];
            return legs[0].length && legs[1].length && legs[2].length
              ? legs.slice(1).reduce((all, leg) => all.flatMap((a) => leg.map((l) => [...a, ...l.slice(1)])), legs[0]).filter(forward).map(tidy) : [];
          })));
        // FigJam draws a plain connector as a straight run, a Z or an L only when each end faces the other.
        } else if (DIR[m0][0] * (q.x - p.x) + DIR[m0][1] * (q.y - p.y) > 0 && DIR[m1][0] * (p.x - q.x) + DIR[m1][1] * (p.y - q.y) > 0) {
          judge(bends(p, m0, q, m1), m0, m1, false);
        }
        sets.push([...GAPS, 2 * STUB, 3 * STUB].flatMap((s0) => GAPS.flatMap((s1) => walk(p, m0, q, m1, s0, s1, true))).filter((pts) => pts.length > 2));
        for (const found of sets) {
          const all = uniq(found.map(line)), shortest = Math.min(...all.map((l) => l.n));
          all.filter((l) => l.n <= shortest + 480).forEach((l) => judge([l], m0, m1, true));
        }
      }
    }
    if (!list.length) list.push({ id: ++serial, m0: 'RIGHT', m1: 'LEFT', lines: [line([dock(e.from, 'RIGHT'), dock(e.to, 'LEFT')])], labs: [], bad: true, fixed: BLOCKED });
    const open = list.filter((o) => !o.bad);
    return open.length ? open : list;
  };
  // What two routes cost one another: a magnet one of them arrives at and the other leaves or arrives at,
  // a crossing, a stretch they share, and a label that sits on the other's line or on its label.
  const ends = (job, o) => [[job.e.from, o.m0, 0], [job.e.to, o.m1, 1]];
  const known = new Map();
  const pair = (a, p, b, q) => {
    const at = p.id * 1e6 + q.id;
    if (known.has(at)) return known.get(at);
    let c = 0;
    let merged = false;
    for (const u of ends(a, p)) for (const v of ends(b, q)) {
      if (u[0] !== v[0] || u[1] !== v[1]) continue;
      merged = merged || !!(u[2] && v[2]);
      c += u[2] && v[2] ? ARRIVE : SHARED;
    }
    if (p.lines.some((l) => q.lines.some((m) => crossing(l, m)))) c += CLASH;
    const run = Math.max(...p.lines.flatMap((l) => q.lines.map((m) => lap(l, m))));
    // Two edges that arrive at one magnet may share their last stretch, which is dearer the longer it runs.
    if (run > LAP) c += merged && run <= MERGE_MAX ? MERGE * run : CLASH;
    else if (p.lines.some((l) => q.lines.some((m) => lapped(l, m, SIDE)))) c += SIDEBY;
    if (p.labs.some((r) => q.lines.some((m) => cuts(m.pts, r, AIR)) || q.labs.some((t) => touch(r, t)))
      || q.labs.some((r) => p.lines.some((l) => cuts(l.pts, r, AIR)))) c += CLASH;
    known.set(at, c);
    return c;
  };
  const own = (o) => o.fixed + (o.pinned ? PINNED : 0);
  const cost = (job, o, skip) => own(o) + jobs.reduce((t, x) => t + (x === job || x === skip ? 0 : pair(job, o, x, x.cur)), 0);
  jobs.forEach((job) => {
    job.opts = options(job);
    job.start = job.opts.reduce((m, o) => (own(o) < own(m) ? o : m));
  });
  // Edges are settled one at a time against the rest, then two that clash are settled together, because
  // each can wait on the other to move first. The sweep runs from several starts and the cheapest board is kept.
  const sweep = (order, begin) => {
    jobs.forEach((job, i) => { job.cur = begin(job, i); });
    for (let round = 0, moved = true; moved && round < 4; round++) {
      moved = false;
      for (const job of order) {
        const best = job.opts.map((o) => ({ o, c: cost(job, o) })).reduce((m, v) => (v.c < m.c ? v : m));
        if (best.o !== job.cur) { moved = true; job.cur = best.o; }
      }
      jobs.forEach((a, i) => jobs.slice(i + 1).forEach((b) => {
        if (!pair(a, a.cur, b, b.cur) && !pair(a, a.start, b, b.cur) && !pair(b, b.start, a, a.cur)) return;
        const top = (job, other) => {
          const seen = {};
          return job.opts.map((o) => ({ o, c: cost(job, o, other) })).sort((x, y) => x.c - y.c)
            .filter((x) => (seen[x.o.m0 + x.o.m1] = (seen[x.o.m0 + x.o.m1] || 0) + 1) <= 2);
        };
        let best = { c: cost(a, a.cur, b) + cost(b, b.cur, a) + pair(a, a.cur, b, b.cur) };
        for (const x of top(a, b)) for (const y of top(b, a)) if (x.c + y.c + pair(a, x.o, b, y.o) < best.c) best = { c: x.c + y.c + pair(a, x.o, b, y.o), x: x.o, y: y.o };
        if (best.x) { moved = true; a.cur = best.x; b.cur = best.y; }
      }));
    }
    return jobs.reduce((t, job) => t + cost(job, job.cur), 0);
  };
  let cheapest = Infinity, chosen = [], seed = 7;
  const draw = (n) => { seed = (seed * 1103515245 + 12345) % 2147483648; return seed % n; };
  for (let k = 0; k < RESTARTS; k++) {
    // After two plain sweeps, each start keeps the best board so far and lets a third of its edges try a new route.
    const total = sweep(k % 2 ? [...jobs].reverse() : jobs,
      (job, i) => (k < 2 || draw(3) === 0 ? (k < 2 ? job.start : job.opts[draw(job.opts.length)]) : chosen[i]));
    if (total < cheapest) { cheapest = total; chosen = jobs.map((job) => job.cur); }
  }
  jobs.forEach((job, i) => {
    job.cur = chosen[i];
    job.m0 = job.cur.m0;
    job.m1 = job.cur.m1;
    job.pts = job.cur.pinned ? job.cur.lines[0].pts : null;
    job.leg = job.cur.leg;
  });
  for (const job of jobs) {
    if (job.cur.bad) warnings.push(`edge ${job.e.from} -> ${job.e.to} runs through a box or a zone title, along a zone border or through a zone it does not join`);
  }
  // Edges that only arrive may merge on one magnet. A magnet an edge leaves from is shared only when no other is free.
  const held = new Map();
  jobs.forEach((j) => new Set(ends(j, j.cur).map((v) => `${v[0]} ${v[1]} ${v[2] ? 1 : 0}`)).forEach((v) => {
    const id = v.split(' ')[0];
    held.set(id, [...(held.get(id) || []), v]);
  }));
  held.forEach((list, id) => {
    const used = new Set(list.map((v) => v.split(' ')[1]));
    const taken = [...used].some((m) => list.filter((v) => v.split(' ')[1] === m).length > 1 && list.some((v) => v.split(' ')[1] === m && v.endsWith(' 0')));
    if (used.size < Math.min(4, list.length) && taken) warnings.push(`two edges share a magnet on ${id} while another is free`);
  });
  const kinds = [...new Set([...M.nodes.map((n) => n.kind), ...M.nodes.filter((n) => n.accent).map(() => 'focus')])];
  const marked = M.nodes.find((n) => n.accent);
  const key = kinds.map((kind) => (kind === 'focus' && marked ? { kind, like: marked.kind } : { kind }));
  for (const style of M.edgeStyles || []) key.push({ line: style });
  return {
    width: L.width, height: L.height, key,
    draw(board, ox, oy) {
      const zoneNodes = zones.map((z, i) => {
        const b = L.zoneBox[i];
        return b ? zoneSection(board, z.label, z.tint, ox + b.x, oy + b.y, b.w, b.h) : null;
      });
      const zoneOf = new Map(zones.map((z, i) => [z.id, zoneNodes[i]]));
      const shapes = new Map();
      for (const n of M.nodes) {
        const b = L.box.get(n.id);
        const parent = zoneOf.get(n.zone) || board;
        const px = parent === board ? 0 : parent.x, py = parent === board ? 0 : parent.y;
        const card = cards.get(n.id);
        const label = card ? [n.label, ...card.lines].join('\n') : (KINDS[n.kind].fixed ? '' : n.label);
        const s = shape(parent, n.kind, label, ox + b.x - px, oy + b.y - py, b.w, b.h, `node:${n.id}`, 0, n.accent);
        if (card) {
          s.text.fontName = REGULAR;
          s.text.fontSize = TYPE.field;
          s.text.setRangeFontName(0, n.label.length, SEMI);
          s.text.setRangeFontSize(0, n.label.length, TYPE.node);
          s.text.textAlignHorizontal = 'LEFT';
          s.text.paragraphSpacing = PARA;
        }
        shapes.set(n.id, s);
        elements.push({ id: s.id, model: n.id, kind: n.kind, text: label });
      }
      edges.forEach((e) => {
        const from = shapes.get(e.from) || zoneOf.get(e.from);
        const to = shapes.get(e.to) || zoneOf.get(e.to);
        const { m0, m1, pts, leg } = portsOf.get(e);
        const style = { dashed: e.style === 'dashed', startCap: e.twoWay ? 'ARROW_LINES' : 'NONE',
          endCap: e.undirected ? 'NONE' : 'ARROW_LINES' };
        let c;
        try {
          if (pts) {
            // A pinned route is one straight leg between each pair of corners, with the label on the
            // longest and the arrow on the last.
            const chain = [from, ...pts.slice(1, -1).map((v, i) => anchor(board, ox + v.x, oy + v.y, `via:${e.from}->${e.to}:${i + 1}`)), to];
            chain.slice(1).forEach((node, i) => {
              const last = i === chain.length - 2;
              const part = connect(board, chain[i], node, { name: last ? `edge:${e.from}->${e.to}` : `leg:${e.from}->${e.to}:${i + 1}`,
                line: 'STRAIGHT', m0: i ? 'POINT' : m0, m1: last ? m1 : 'POINT', label: i === leg ? e.label : '',
                dashed: style.dashed, startCap: i ? 'NONE' : style.startCap, endCap: last ? style.endCap : 'NONE' });
              if (last) c = part;
            });
          } else {
            c = connect(board, from, to, { name: `edge:${e.from}->${e.to}`, m0, m1, label: e.label, ...style });
          }
        } catch (err) {
          warnings.push(`edge ${e.from} -> ${e.to}: ${err.message}`);
          return;
        }
        links.push({ id: c.id, from: from.id, to: to.id, model: `${e.from}->${e.to}`, label: e.label || '',
          via: pts ? 'waypoints' : undefined });
      });
    },
  };
}

// ── Sequence ──
// A request and a reply end in a closed head and an async message in an open one, so the two read apart
// by their head as well as their colour.
const ARROWS = {
  request: { dashed: false, cap: 'ARROW_EQUILATERAL', color: DARK, key: 'Request' },
  reply: { dashed: true, cap: 'ARROW_EQUILATERAL', color: LINE, key: 'Reply' },
  async: { dashed: false, cap: 'ARROW_LINES', color: ASYNC, key: 'Async message' },
  asyncReply: { dashed: true, cap: 'ARROW_LINES', color: ASYNC, key: 'Async reply' },
  focus: { dashed: false, cap: 'ARROW_EQUILATERAL', color: SHAPE.lightPink.stroke, key: 'In focus', weight: 4 },
};
function buildSequence(M) {
  const sizes = M.participants.map((p) => fit(p.label, 'ROUNDED_RECTANGLE'));
  const pw = Math.max(...sizes.map((s) => s.w));
  const ph = Math.max(...sizes.map((s) => s.h));
  const index = new Map(M.participants.map((p, i) => [p.id, i]));
  const PIN = 72;
  const centres = M.participants.map((_, i) => PIN + pw / 2 + i * (pw + 96));
  // A message's label sits in the gap next to its sender, because the middle of a message that
  // crosses a participant is that participant's lifeline. So that gap is the one widened to fit it.
  const near = (a, b) => (b > a ? a + 1 : a - 1);
  // A self message loops out to the right far enough to carry its label, and the gap after it widens to match.
  const SELF_DROP = 40;
  const selfReach = (m) => up8(natural(m.label, MEDIUM, TYPE.label).w + 64);
  let reach = 0;
  for (const m of M.messages) {
    const a = index.get(m.from), b = index.get(m.to);
    if (a === b) {
      reach = Math.max(reach, centres[a] + selfReach(m) + 32 - centres[centres.length - 1]);
      if (a + 1 < centres.length) {
        const short = selfReach(m) + 48 - (centres[a + 1] - centres[a]);
        if (short > 0) for (let i = a + 1; i < centres.length; i++) centres[i] += up8(short);
      }
      continue;
    }
    const need = natural(m.label, MEDIUM, TYPE.label).w + 96;
    const lo = Math.min(a, near(a, b)), hi = Math.max(a, near(a, b));
    const short = need - (centres[hi] - centres[lo]);
    if (short > 0) for (let i = hi; i < centres.length; i++) centres[i] += up8(short);
  }
  const ROW = 72;
  const top = ph + 48;
  const rows = [];
  let y = top;
  for (const m of M.messages) { rows.push(y); y += m.from === m.to ? ROW + SELF_DROP : ROW; }
  const bottom = y + 16;
  const width = centres[centres.length - 1] + Math.max(pw / 2, reach);
  const height = bottom + ph;
  const used = [...new Set([...M.messages.map((m) => m.arrow), ...M.messages.filter((m) => m.accent).map(() => 'focus')])];
  const key = [{ kind: 'participant' }, ...used.map((a) => ({ arrow: a })), { pin: true }];
  return {
    width, height, key,
    draw(board, ox, oy) {
      const heads = M.participants.map((p, i) => {
        const x = ox + centres[i] - pw / 2;
        const head = shape(board, 'participant', p.label, x, oy, pw, ph, `node:${p.id}`);
        const foot = shape(board, 'participant', p.label, x, oy + bottom, pw, ph, `foot:${p.id}`);
        elements.push({ id: head.id, model: p.id, kind: 'participant', text: p.label });
        const life = connect(board, head, foot, { name: `life:${p.id}`, line: 'STRAIGHT', m0: 'BOTTOM', m1: 'TOP',
          endCap: 'NONE', color: LIFELINE });
        life.dashPattern = [6, 6];
        return head;
      });
      M.messages.forEach((m, k) => {
        const yy = oy + rows[k];
        const a = index.get(m.from), b = index.get(m.to);
        const style = { ...(ARROWS[m.arrow] || ARROWS.request), ...(m.accent ? { color: ARROWS.focus.color, weight: 4 } : {}) };
        const self = a === b;
        const x = ox + centres[a];
        const start = anchor(board, x, yy, `at:${k}:from`);
        const stop = anchor(board, ox + centres[b], self ? yy + SELF_DROP : yy, `at:${k}:to`);
        const leg = (p, q, n, label) => connect(board, p, q, { name: `leg:${m.from}->${m.to}:${k + 1}:${n}`,
          line: 'STRAIGHT', m0: 'POINT', m1: 'POINT', label, dashed: style.dashed, endCap: 'NONE', color: style.color, weight: style.weight });
        let from = start;
        if (self) {
          // A self message is a loop of three straight legs, labelled along its top like any other message.
          const p1 = anchor(board, x + selfReach(m), yy, `at:${k}:out`);
          const p2 = anchor(board, x + selfReach(m), yy + SELF_DROP, `at:${k}:back`);
          leg(start, p1, 1, m.label);
          leg(p1, p2, 2, '');
          from = p2;
        } else if (Math.abs(b - a) > 1) {
          // The labelled leg ends on the next lifeline, and the arrow carries on from there unlabelled.
          from = anchor(board, ox + centres[near(a, b)], yy, `at:${k}:via`);
          leg(start, from, 1, m.label);
        }
        const c = connect(board, from, stop, {
          name: `edge:${m.from}->${m.to}:${k + 1}`, line: 'STRAIGHT', m0: 'POINT', m1: 'POINT',
          label: from === start ? m.label : '', dashed: style.dashed, endCap: style.cap, color: style.color, weight: style.weight,
        });
        links.push({ id: c.id, from: heads[a].id, to: heads[b].id, model: `${m.from}->${m.to}`, label: m.label });
        const pin = shape(board, 'initial', String(k + 1), ox + 8, yy - 16, 32, 32, `step:${k + 1}`, 14);
        const v = SHAPE.violet;
        pin.fills = solid(v.fill);
        pin.strokes = solid(v.stroke);
        pin.text.fills = solid(WHITE);
      });
    },
  };
}

// ── Gantt ──
const MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
function buildGantt(M) {
  const day = M.unit === 'day';
  const span = Math.max(1, M.span);
  const scale = day ? Math.min(96, Math.max(8, snap(1680 / span))) : Math.min(8, Math.max(1, 1680 / span));
  const tick = day ? (span <= 14 ? 1 : span <= 70 ? 7 : span <= 200 ? 14 : 28) : (span <= 180 ? 30 : 60);
  const tasks = M.sections.flatMap((s) => s.tasks);
  const nameCol = up8(Math.max(240, ...tasks.map((t) => natural(t.name, MEDIUM, TYPE.label).w + 48),
    ...M.sections.map((s) => natural(s.label, SEMI, TYPE.node).w + 64)));
  const AXIS = 56, ROW = 56, BAR = 32, HEAD = 72;
  const timeW = up8(span * scale);
  const width = nameCol + timeW + 48;
  let y = AXIS;
  const bands = M.sections.map((s) => {
    const band = { y, h: HEAD + s.tasks.length * ROW + 16 };
    y += band.h + 16;
    return band;
  });
  const height = y - 16;
  const label = (offset) => {
    if (day) {
      const d = new Date(`${M.origin}T00:00:00Z`);
      d.setUTCDate(d.getUTCDate() + offset);
      return `${d.getUTCDate()} ${MONTHS[d.getUTCMonth()]}`;
    }
    const [hh, mm] = M.origin.split(':').map(Number);
    const total = hh * 60 + mm + offset;
    return `${String(Math.floor(total / 60) % 24).padStart(2, '0')}:${String(total % 60).padStart(2, '0')}`;
  };
  const length = (t) => {
    const d = t.end - t.start;
    if (day) return d % 7 === 0 ? `${d / 7} week${d === 7 ? '' : 's'}` : `${d} day${d === 1 ? '' : 's'}`;
    return d >= 60 && d % 60 === 0 ? `${d / 60} h` : `${d} min`;
  };
  const statusOf = (t) => (t.tags.includes('milestone') ? 'milestone' : t.tags.includes('crit') ? 'crit'
    : t.tags.includes('active') ? 'active' : t.tags.includes('done') ? 'done' : 'planned');
  const used = [...new Set(tasks.map(statusOf))];
  const order = ['done', 'active', 'planned', 'crit', 'milestone'];
  const marked = tasks.find((t) => t.accent);
  const key = order.filter((s) => used.includes(s)).map((kind) => ({ kind })).concat(marked ? [{ kind: 'focus', like: statusOf(marked) }] : []);
  return {
    width, height, key,
    draw(board, ox, oy) {
      // Grid lines are 1px rectangles, not connectors, so the read-back never counts them as edges.
      // Sections are opaque, so each one draws its own stretch of every line under its bars.
      const ticks = [];
      for (let t = 0; t <= span; t += tick) ticks.push(t);
      const rule = (parent, x, top, hh, name) => {
        const r = figma.createRectangle();
        parent.appendChild(r);
        r.name = name;
        r.fills = solid(FAINT);
        r.resize(1, Math.max(1, hh));
        r.x = x;
        r.y = top;
        created.push(r.id);
      };
      ticks.forEach((t) => {
        const x = ox + nameCol + t * scale;
        const tl = text(board, label(t), REGULAR, TYPE.label, x, oy + 8);
        tl.x = x - tl.width / 2;
        rule(board, x, oy + AXIS - 8, height - AXIS + 8, `grid:${t}`);
      });
      M.sections.forEach((s, i) => {
        const band = bands[i];
        const sec = zoneSection(board, s.label, TINT_CYCLE[i % TINT_CYCLE.length], ox, oy + band.y, width, band.h);
        ticks.forEach((t) => rule(sec, nameCol + t * scale, 0, band.h, `grid:${t}`));
        s.tasks.forEach((t, k) => {
          const ry = HEAD + k * ROW;
          text(sec, t.name, MEDIUM, TYPE.label, 32, ry + (ROW - 20) / 2 - 4);
          const status = statusOf(t);
          const bx = nameCol + t.start * scale;
          let bar;
          if (status === 'milestone') {
            bar = shape(sec, 'milestone', '', bx - 16, ry + (ROW - 32) / 2 - 4, 32, 32, `node:${t.id || t.name}`, 0, t.accent);
          } else {
            const w = Math.max(16, (t.end - t.start) * scale);
            // A critical bar also names itself in words and keeps a heavier outline, so it still reads in greyscale.
            const words = status === 'crit' ? `${length(t)}, critical` : length(t);
            const fits = natural(words, MEDIUM, 14).w + 24 <= w;
            bar = shape(sec, status, fits ? words : '', bx, ry + (ROW - BAR) / 2 - 4, w, BAR, `node:${t.id || t.name}`, 14, t.accent);
          }
          elements.push({ id: bar.id, model: t.id || t.name, kind: status, text: t.name });
        });
      });
    },
  };
}

// ── The board ──
const builders = { graph: buildGraph, sequence: buildSequence, gantt: buildGantt };
let body;
try {
  body = (builders[MODEL.type] || buildGraph)(MODEL);
} catch (err) {
  measurer.remove();
  throw err;
}
const page = figma.currentPage;
const others = page.children.filter((n) => n.id !== measurer.id);
const board = figma.createSection();
board.name = MODEL.title;
board.fills = solid(WHITE);
board.x = others.length ? snap(Math.max(...others.map((n) => n.x + n.width)) + 400) : 0;
board.y = others.length ? snap(Math.min(...others.map((n) => n.y))) : 0;
created.push(board.id);
const wrap = Math.min(Math.max(body.width, 960), 1440);
const title = text(board, MODEL.title, BOLD, TYPE.title, BOARD_PAD, BOARD_PAD);
let cursor = title.y + title.height + 16;
if (MODEL.subtitle) {
  const sub = text(board, MODEL.subtitle, REGULAR, TYPE.subtitle, BOARD_PAD, cursor, wrap);
  cursor = sub.y + sub.height;
}
const ox = BOARD_PAD;
const oy = up8(cursor + 64);
body.draw(board, ox, oy);

// Key: one sample per kind and line the board uses, in the order a reader meets them.
const key = figma.createSection();
board.appendChild(key);
key.name = 'Key';
key.fills = solid(TINT.gray);
key.x = BOARD_PAD;
key.y = oy + body.height + 64;
created.push(key.id);
text(key, 'Key', SEMI, TYPE.zone, 32, 32);
const LINES = {
  dashedOptional: { dashed: true, label: 'Optional or proposed' },
  dashedAsync: { dashed: true, label: 'Async or outside call' },
  identifying: { dashed: false, label: 'Identifying', cap: 'NONE' },
  nonIdentifying: { dashed: true, label: 'Non-identifying', cap: 'NONE' },
  twoWay: { dashed: false, label: 'Both ways', start: 'ARROW_LINES' },
};
let kx = 32;
const rowY = 88;
for (const item of body.key) {
  let label;
  if (item.kind) {
    // The focus sample is drawn as the marked node is, its own kind under the pink outline.
    const as = item.like || item.kind, k = KINDS[as];
    const tall = k.shape === 'ENG_DATABASE' || k.shape === 'ENG_QUEUE';
    const sw = k.fixed ? Math.min(k.fixed[0], 56) : (ROUND.has(k.shape) ? 72 : (tall ? 48 : 88));
    const sh = k.fixed ? Math.min(k.fixed[1], 56) : (ROUND.has(k.shape) || tall ? 56 : 48);
    // FigJam keeps some shapes above a minimum size, so spacing follows the size it actually drew.
    const sample = shape(key, as, '', kx, rowY, sw, sh, `key:${item.kind}`, 0, !!item.like);
    sample.y = rowY + (56 - sample.height) / 2;
    kx += sample.width + 16;
    label = KINDS[item.kind].key;
  } else if (item.pin) {
    const pin = shape(key, 'initial', '1', kx, rowY + 12, 32, 32, 'key:pin', 14);
    pin.fills = solid(SHAPE.violet.fill);
    pin.strokes = solid(SHAPE.violet.stroke);
    pin.text.fills = solid(WHITE);
    kx += 48;
    label = 'Step number';
  } else {
    const spec = item.arrow ? { ...ARROWS[item.arrow], label: ARROWS[item.arrow].key } : LINES[item.line];
    if (!spec) continue;
    const a = anchor(key, kx + 8, rowY + 28, `key:${item.arrow || item.line}:a`);
    const b = anchor(key, kx + 88, rowY + 28, `key:${item.arrow || item.line}:b`);
    connect(key, a, b, { name: `key:${item.arrow || item.line}`, line: 'STRAIGHT', m0: 'POINT', m1: 'POINT',
      dashed: spec.dashed, endCap: spec.cap === undefined ? 'ARROW_LINES' : spec.cap, startCap: spec.start || 'NONE',
      color: spec.color || LINE, weight: spec.weight });
    kx += 112;
    label = spec.label;
  }
  const t = text(key, label, REGULAR, TYPE.label, kx, rowY + 18);
  kx = up8(t.x + t.width + 48);
}
key.resize(Math.max(kx - 16, 240), rowY + 56 + 32);
let bottom = key.y + key.height;
if (MODEL.source) {
  const src = text(board, MODEL.source, REGULAR, TYPE.label, BOARD_PAD, bottom + 32, wrap);
  bottom = src.y + src.height;
}
measurer.remove();
const right = Math.max(...board.children.map((n) => n.x + n.width));
board.resize(up8(right + BOARD_PAD), up8(bottom + BOARD_PAD));

const counts = { nodes: elements.length, connectors: links.length };
const expect = MODEL.expect || {};
for (const [k, v] of Object.entries(expect)) {
  if (counts[k] !== undefined && counts[k] !== v) warnings.push(`${k}: drew ${counts[k]}, the model has ${v}`);
}
// The board is the only record a later session can find, so the tag lets a revision replace this board
// rather than draw a second one. Any plugin can read shared data, so it holds the title and counts only.
const TAG = 'productowner';
let tagged = true;
try {
  board.setSharedPluginData(TAG, MODEL.title, JSON.stringify({ written: new Date().toISOString(), counts }));
} catch (err) {
  tagged = false;
  warnings.push(`the board was not tagged: ${err.message}`);
}
await board.screenshot({ scale: Math.min(1, 1600 / board.width) });
return {
  boardId: board.id,
  tag: tagged ? { namespace: TAG, key: MODEL.title } : null,
  bounds: { x: board.x, y: board.y, w: board.width, h: board.height },
  counts,
  expect,
  elements,
  links,
  warnings,
  createdCount: created.length,
};
