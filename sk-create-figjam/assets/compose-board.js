// ───────────────────────────────────────────────────────────────
// COMPONENT: FIGJAM BOARD COMPOSER
// ───────────────────────────────────────────────────────────────
// Draws one checked diagram as a framed FigJam board through use_figma: a title
// block, tinted zones, shapes sized to their text, routed connectors, a key and
// a source line, all on an 8 px grid. scripts/compose_board.py fills MODEL from
// a model that passed flow_check.py and THEME from assets/figjam-design.md, so
// the board holds exactly what was checked, drawn in the style the design sets.
// Paste the whole file as the use_figma code. Nothing persists between calls, so
// the return value carries every id the read-back needs.

// ───────────────────────────────────────────────────────────────
// 1. MODEL, DESIGN AND CONSTANTS
// ───────────────────────────────────────────────────────────────

const MODEL = __MODEL__;
// The tokens assets/figjam-design.md sets apart from the built-in design below. An empty object draws the
// built-in design.
const THEME = __THEME__;

// FigJam's own pairs, as fill, stroke and text, and its section tints. A design names them and never changes
// them, so anyone on the board can still recolour a node from FigJam's palette.
const SWATCH = {
  white: ['#FFFFFF', '#B3B3B3', '#1E1E1E'], black: ['#1E1E1E', '#B3B3B3', '#FFFFFF'],
  darkGray: ['#757575', '#5E5E5E', '#FFFFFF'], violet: ['#874FFF', '#5427B4', '#FFFFFF'],
  lightBlue: ['#C2E5FF', '#3DADFF', '#1E1E1E'], lightGreen: ['#CDF4D3', '#66D575', '#1E1E1E'],
  lightYellow: ['#FFECBD', '#FFC943', '#1E1E1E'], lightOrange: ['#FFE0C2', '#FF9E42', '#1E1E1E'],
  lightRed: ['#FFCDC2', '#FF7556', '#1E1E1E'], lightViolet: ['#DCCCFF', '#874FFF', '#1E1E1E'],
  lightPink: ['#FFC2EC', '#F849C1', '#1E1E1E'], lightTeal: ['#C6FAF6', '#5AD8CC', '#1E1E1E'],
  lightGray: ['#D9D9D9', '#B3B3B3', '#1E1E1E'],
};
const TINT = {
  gray: '#F9F9F9', green: '#EBFFEE', teal: '#F1FEFD', blue: '#F5FBFF', violet: '#F8F5FF',
  pink: '#FFF0FA', red: '#FFF5F5', orange: '#FFF7F0', yellow: '#FFFBF0',
};
// The built-in design, which assets/figjam-design.md repeats token for token. A kind names a role and a role
// names a pair, so a colour means the same thing on every board. Kinds stand in the order a reader meets
// them, which is the order of the key.
const D = {
  role: {
    entry: 'lightBlue', neutral: 'white', goal: 'lightGreen', exit: 'lightOrange', error: 'lightRed',
    decision: 'lightYellow', store: 'lightViolet', io: 'lightTeal', client: 'lightTeal', gateway: 'lightBlue',
    queue: 'lightOrange', external: 'lightGray', inProgress: 'lightBlue', done: 'lightGray', pseudo: 'black',
    junction: 'darkGray', marker: 'violet',
  },
  accent: { pair: 'lightPink', node: 8, message: 4 },
  kind: {
    initial: { role: 'pseudo', key: 'Start' },
    start: { role: 'entry', key: 'Where it starts' },
    firstState: { role: 'entry', key: 'First state' },
    client: { role: 'client', key: 'App or client' },
    gateway: { role: 'gateway', key: 'Edge or gateway' },
    participant: { role: 'neutral', key: 'Participant' },
    screen: { role: 'neutral', key: 'Screen or step' },
    step: { role: 'neutral', key: 'Step' },
    state: { role: 'neutral', key: 'State' },
    service: { role: 'neutral', key: 'Service' },
    subprocess: { role: 'neutral', key: 'Sub-process' },
    io: { role: 'io', key: 'Input or output' },
    entity: { role: 'neutral', key: 'Entity' },
    queue: { role: 'queue', key: 'Queue or stream' },
    decision: { role: 'decision', key: 'Decision' },
    choice: { role: 'decision', key: 'Choice' },
    fork: { role: 'pseudo', key: 'Fork or join' },
    merge: { role: 'junction', key: 'Paths join' },
    success: { role: 'goal', key: 'Goal reached' },
    exit: { role: 'exit', key: 'Leaves the flow' },
    error: { role: 'error', key: 'Error or blocked' },
    finalState: { role: 'done', key: 'Final state' },
    final: { role: 'pseudo', key: 'End' },
    datastore: { role: 'store', key: 'Data store' },
    external: { role: 'external', key: 'Outside system' },
    done: { role: 'done', key: 'Done' },
    active: { role: 'inProgress', key: 'In progress' },
    planned: { role: 'neutral', key: 'Planned' },
    crit: { role: 'error', key: 'Critical, heavy outline' },
    milestone: { role: 'decision', key: 'Milestone' },
    focus: { key: 'In focus' },
  },
  type: { family: 'Inter', title: 64, subtitle: 28, zone: 24, node: 20, label: 18, field: 16, small: 14 },
  line: { color: '#757575', async: '#3DADFF', lifeline: '#B3B3B3', weight: 2 },
  zone: { cycle: ['blue', 'orange', 'teal', 'yellow', 'violet'] },
  key: {
    title: 'Key', tint: 'gray', pin: 'Step number', solid: 'Leads to', dashedOptional: 'Optional or proposed',
    dashedAsync: 'Async or outside call', identifying: 'Identifying', nonIdentifying: 'Non-identifying',
    twoWay: 'Both ways', request: 'Request', reply: 'Reply', async: 'Async message', asyncReply: 'Async reply',
  },
};
const T = (function merge(a, b) {
  for (const k in b) a[k] = b[k] && typeof b[k] === 'object' && !Array.isArray(b[k]) && a[k] ? merge(a[k], b[k]) : b[k];
  return a;
})(D, THEME);

// What no design changes: a kind's shape, a fixed size and an outline of its own, the ring of an end state,
// the heavier line of a critical bar and the line gray around a planned bar. Kinds that share a shape and
// whose fills sit close in greyscale also differ by outline, heavy, dashed or both, so colour never carries
// a kind's meaning alone.
const SHAPES = {
  decision: 'DIAMOND', choice: 'DIAMOND', milestone: 'DIAMOND', merge: 'ELLIPSE', initial: 'ELLIPSE',
  final: 'ELLIPSE', datastore: 'ENG_DATABASE', queue: 'ENG_QUEUE', subprocess: 'PREDEFINED_PROCESS',
  io: 'PARALLELOGRAM_RIGHT', fork: 'SQUARE', entity: 'SQUARE',
};
const FIXED = { merge: [24, 24], initial: [32, 32], final: [32, 32], choice: [56, 56], fork: [16, 96], milestone: [32, 32] };
const OUTLINE = {
  final: 'ring', crit: 'heavy', planned: 'line', client: 'line', gateway: 'heavy', success: 'heavy', finalState: 'heavy',
  exit: 'dash', external: 'dash', active: 'dash', error: 'heavy dash',
};
const shapeOf = (kind) => SHAPES[kind] || 'ROUNDED_RECTANGLE';
// A kind's fill, stroke and text. The focus kind draws the accent's own pair.
const pairOf = (kind) => SWATCH[kind === 'focus' ? T.accent.pair : T.role[T.kind[kind].role]] || SWATCH.white;
const ACCENT = SWATCH[T.accent.pair][1];
const INK = '#1E1E1E';
const OFF_PATH = new Set(['exit', 'error']);
// An ER end's mark, keyed by the code the model gives each end: exactly one, zero or one, zero or more, one or more.
const ERD = { 1: 'ERD_EXACTLY_ONE', '?': 'ERD_ZERO_OR_ONE', '*': 'ERD_ZERO_OR_MORE', '+': 'ERD_ONE_OR_MORE' };
const ROUND = new Set(['DIAMOND', 'ELLIPSE', 'HEXAGON', 'OCTAGON']);

const GRID = 8;
const snap = (v) => Math.round(v / GRID) * GRID;
const up8 = (v) => Math.ceil(v / GRID) * GRID;
const TYPE = T.type;
const PARA = 4;
const RANK_GAP = 136;
const CROSS_GAP = 80;
const ZONE_GAP = 48;
const ZONE_HEAD = 96;
const ZONE_PAD = 48;
const BOARD_PAD = 80;
// Each channel is written as hex/255, which is how FigJam knows a colour for one of its palette swatches.
const solid = (x) => [{ type: 'SOLID', color: { r: parseInt(x.slice(1, 3), 16) / 255, g: parseInt(x.slice(3, 5), 16) / 255, b: parseInt(x.slice(5, 7), 16) / 255 } }];

const warnings = [];
const created = [];
const elements = [];
const links = [];

// A family that will not load sets the board in Inter, so a design never stops a board being drawn. Inter
// names its third weight Semi Bold and most families SemiBold, so the second name is tried when the first fails.
const STYLES = ['Medium', 'Regular', 'Semi Bold', 'Bold'];
const load = (family) => Promise.all(STYLES.map((style) => figma.loadFontAsync({ family, style }).then(() => style, (err) => {
  if (style !== 'Semi Bold') throw err;
  return figma.loadFontAsync({ family, style: 'SemiBold' }).then(() => 'SemiBold');
})));
let FAMILY = TYPE.family, NAMES;
try { NAMES = await load(FAMILY); } catch (err) { warnings.push(`the font ${FAMILY} did not load, so the board is set in Inter`); FAMILY = 'Inter'; NAMES = await load(FAMILY); }
const [MEDIUM, REGULAR, SEMI, BOLD] = NAMES.map((style) => ({ family: FAMILY, style }));

// ───────────────────────────────────────────────────────────────
// 2. MEASURING
// ───────────────────────────────────────────────────────────────

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

// ───────────────────────────────────────────────────────────────
// 3. DRAWING PRIMITIVES
// ───────────────────────────────────────────────────────────────

function text(parent, chars, font, size, x, y, width) {
  const t = figma.createText();
  t.fontName = font;
  t.fontSize = size;
  t.characters = chars;
  t.fills = solid(INK);
  parent.appendChild(t);
  if (width) { t.textAutoResize = 'HEIGHT'; t.resize(width, t.height); }
  t.x = x;
  t.y = y;
  created.push(t.id);
  return t;
}
// The accent is the one pair no kind draws and the heaviest outline on any board, so it outweighs every
// kind's fill and still reads first in greyscale, where only a line's weight and darkness are left.
function paint(s, kind, accent) {
  const pair = pairOf(kind), o = OUTLINE[kind] || '';
  const hot = accent || kind === 'focus';
  s.fills = solid(pair[0]);
  s.strokes = solid(hot ? ACCENT : o === 'line' ? T.line.color : pair[1]);
  try {
    s.strokeWeight = hot ? T.accent.node : o === 'ring' ? 6 : o.startsWith('heavy') ? 4 : 2;
    s.dashPattern = !hot && o.endsWith('dash') ? [12, 8] : [];
  } catch (err) { /* a shape that refuses a weight or a dash keeps FigJam's */ }
  return pair;
}
function shape(parent, kind, label, x, y, w, hh, name, size, accent) {
  const s = figma.createShapeWithText();
  s.shapeType = shapeOf(kind);
  s.name = name;
  const pair = paint(s, kind, accent);
  if (label) {
    s.text.fontName = MEDIUM;
    s.text.fontSize = size || TYPE.node;
    s.text.characters = label;
    s.text.fills = solid(pair[2]);
  }
  s.resize(w, hh);
  parent.appendChild(s);
  s.x = x;
  s.y = y;
  created.push(s.id);
  return s;
}
// A step pin: a 32 px dot in the marker role's pair, its number in the pair's own text colour.
function marker(parent, digit, x, y, name) {
  const p = shape(parent, 'initial', digit, x, y, 32, 32, name, TYPE.small);
  const m = SWATCH[T.role.marker];
  p.fills = solid(m[0]);
  p.strokes = solid(m[1]);
  p.text.fills = solid(m[2]);
  return p;
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
// leaves a visible break wherever two legs meet, while a pinned point joins them into one line. A point
// given as x and y pins the end there, measured from the node's corner.
function end(node, magnet = 'AUTO') {
  if (magnet === 'POINT') magnet = { x: node.width / 2, y: node.height / 2 };
  return { endpointNodeId: node.id, [magnet.y === undefined ? 'magnet' : 'position']: magnet };
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
  c.strokes = solid(o.color || T.line.color);
  c.strokeWeight = o.weight || T.line.weight;
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
// A zone takes the first tint along the cycle that no kind inside it draws and that no zone already drawn
// facing it took, in its row or its column however wide the gap a label opened, so a tint never repeats a
// member's hue and two neighbouring zones never read as one. When no tint keeps both, a zone only keeps
// clear of the zones within two zone gaps on any side, and when none keeps that, the neighbour rule wins
// and the warnings say so. The key's own tint is never a zone's.
const tinted = [];
function tintFor(i, kinds, label, x, y, w, h) {
  const c = T.zone.cycle, g = 2 * ZONE_GAP, order = [...c.slice(i % c.length), ...c.slice(0, i % c.length)];
  const hues = new Set(kinds.map((k) => (T.role[(T.kind[k] || {}).role] || T.accent.pair).replace('light', '').toLowerCase()));
  const by = (n) => tinted.filter((z) => (z.x < x + w + g && x < z.x + z.w + g) + (z.y < y + h + g && y < z.y + z.h + g) > n).map((z) => z.t);
  const near = by(1), free = (n) => order.find((t) => !hues.has(t) && !by(n).includes(t));
  let t = free(0) || free(1);
  if (!t) {
    t = order.find((t) => !near.includes(t)) || order[0];
    warnings.push(`zone ${label} repeats the ${t} tint of ${near.includes(t) ? 'a zone beside it' : 'a step inside it'}, because the tint cycle has none left for it`);
  }
  tinted.push({ x, y, w, h, t });
  return t;
}

// A request and a reply end in a closed head and an async message in an open one, so the two read apart
// by their head as well as their colour. A request draws the board's own line, as every other type does.
// The key draws these too, so they sit with the primitives rather than with the sequence builder.
const ARROWS = {
  request: { cap: 'ARROW_EQUILATERAL' },
  reply: { dashed: true, cap: 'ARROW_EQUILATERAL' },
  async: { cap: 'ARROW_LINES', color: T.line.async },
  asyncReply: { dashed: true, cap: 'ARROW_LINES', color: T.line.async },
  focus: { cap: 'ARROW_EQUILATERAL', color: ACCENT, weight: T.accent.message },
};

// ───────────────────────────────────────────────────────────────
// 4. LAYERED LAYOUT
// ───────────────────────────────────────────────────────────────

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
  // An ER card on a left to right board is placed by its top edge, so the cards along a row share their top
  // and read as one row. Every other box is placed by its centre.
  const half = (id) => (opt.top && LR ? 0 : crossSize.get(id) / 2);
  const mid = (id) => snap(cross.get(id)) - half(id) + crossSize.get(id) / 2;
  const gapBetween = (a, b) => (zoned && lane.get(a) !== lane.get(b) ? CROSS_GAP + ZONE_HEAD + ZONE_PAD + ZONE_GAP : CROSS_GAP);
  const place = (whole, desired) => {
    const parts = stacked ? [...new Set(whole.map((id) => lane.get(id)))].map((k) => whole.filter((id) => lane.get(id) === k)) : [whole];
    for (const list of parts) {
      let off = 0;
      const rows = list.map((id, i) => {
        if (i > 0) off += crossSize.get(list[i - 1]) - half(list[i - 1]) + half(id) + gapBetween(list[i - 1], id);
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
  // A top to bottom ER board lines its cards up along the top of their rank instead.
  const box = new Map();
  for (const n of items) {
    const c = snap(cross.get(n.id)), r = rank.get(n.id);
    box.set(n.id, LR ? { x: snap(centre[r]) - n.w / 2, y: c - half(n.id), w: n.w, h: n.h }
      : { x: c - n.w / 2, y: opt.top ? snap(centre[r] - extent[r] / 2) : snap(centre[r]) - n.h / 2, w: n.w, h: n.h });
  }
  // A long edge passes the ranks between its ends through the slot its dummies reserved. Its two
  // waypoints sit in the gaps before and after that slot, so every bend falls between ranks.
  const point = (along, across) => (LR ? { x: along, y: across } : { x: across, y: along });
  const waypoints = new Map();
  for (const [i, ds] of chain) {
    const first = ds[0], last = ds[ds.length - 1];
    waypoints.set(i, {
      lane: lane.get(first),
      a: point(snap(gapMid[rank.get(first)]), snap(mid(first))),
      b: point(snap(gapMid[rank.get(last) + 1]), snap(mid(last))),
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
        .concat(dummies.filter((d) => lane.get(d) === k).map((d) => [mid(d) - 8, mid(d) + 8]));
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
  const clashes = () => {
    const found = [];
    zoneBox.forEach((a, i) => {
      if (!a) return;
      zoneBox.forEach((b, j) => {
        if (b && j > i && a.x < b.x + b.w && b.x < a.x + a.w && a.y < b.y + b.h && b.y < a.y + a.h) {
          found.push(`zones ${zones[i].id} and ${zones[j].id} overlap`);
        }
      });
      items.forEach((n) => {
        const b = box.get(n.id);
        if (n.zone !== zones[i].id && b.x < a.x + a.w && a.x < b.x + b.w && b.y < a.y + a.h && a.y < b.y + b.h) {
          found.push(`node ${n.id} sits inside zone ${zones[i].id} without belonging to it`);
        }
      });
    });
    return found;
  };
  // Zones that share a row, as stages along the flow or as groups side by side, share their top edge, or their
  // left edge on a top to bottom board, so they read as one row of columns. An edge that skips a zone in the
  // row runs over or under it, so that row keeps its zones' own fit and the way past stays open. Where a zone
  // grown to the shared edge would meet another zone or a node it does not hold, every zone keeps its own fit.
  if (!stacked && zones.length > 1) {
    const [p, s, q] = LR ? ['y', 'h', 'x'] : ['x', 'w', 'y'];
    const fitted = zoneBox.map((b) => b && { ...b });
    const before = clashes().length;
    const ids = zones.map((_, i) => i).filter((i) => zoneBox[i]).sort((a, b) => zoneBox[a][p] - zoneBox[b][p]);
    for (let i = 0, j; i < ids.length; i = j) {
      let reach = zoneBox[ids[i]][p] + zoneBox[ids[i]][s];
      for (j = i + 1; j < ids.length && zoneBox[ids[j]][p] < reach; j++) reach = Math.max(reach, zoneBox[ids[j]][p] + zoneBox[ids[j]][s]);
      const at = new Map(ids.slice(i, j).sort((a, b) => zoneBox[a][q] - zoneBox[b][q]).map((z, k) => [z, k]));
      if (edges.some((e) => at.has(lane.get(e.from)) && at.has(lane.get(e.to)) && Math.abs(at.get(lane.get(e.from)) - at.get(lane.get(e.to))) > 1)) continue;
      const lo = zoneBox[ids[i]][p];
      ids.slice(i, j).forEach((z) => { zoneBox[z][s] += zoneBox[z][p] - lo; zoneBox[z][p] = lo; });
    }
    if (clashes().length > before) zoneBox.forEach((b, i) => b && Object.assign(b, fitted[i]));
  }
  const clash = opt.zoneMode === 'group' ? clashes() : [];
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

// ───────────────────────────────────────────────────────────────
// 5. GRAPH BOARDS
// ───────────────────────────────────────────────────────────────

// A user flow, a process, an architecture, a state machine or an ER model.
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
    if (!T.kind[n.kind]) { warnings.push(`kind ${n.kind} on ${n.id} is unknown, drawn as a step`); n.kind = 'step'; }
    const f = FIXED[n.kind];
    let s;
    if (f) s = { w: f[0], h: f[1] };
    else if (n.kind === 'entity') { const card = entityCard(n); cards.set(n.id, card); s = { w: card.w, h: card.h }; }
    else s = fit(n.label, shapeOf(n.kind));
    return { id: n.id, w: s.w, h: s.h, zone: n.zone, offPath: OFF_PATH.has(n.kind), goal: n.kind === 'success', kind: n.kind };
  });
  // One size per shape class keeps a rhythm across the board.
  const classMax = new Map();
  for (const it of items) {
    if (FIXED[it.kind] || it.kind === 'entity') continue;
    const cls = shapeOf(it.kind);
    const m = classMax.get(cls) || { w: 0, h: 0 };
    classMax.set(cls, { w: Math.max(m.w, it.w), h: Math.max(m.h, it.h) });
  }
  for (const it of items) {
    if (FIXED[it.kind] || it.kind === 'entity') continue;
    Object.assign(it, classMax.get(shapeOf(it.kind)));
  }
  const nodeIds = new Set(M.nodes.map((n) => n.id));
  const zoneIds = new Set((M.zones || []).map((z) => z.id));
  const edges = M.edges.filter((e) => {
    const ok = (nodeIds.has(e.from) || zoneIds.has(e.from)) && (nodeIds.has(e.to) || zoneIds.has(e.to));
    if (!ok) warnings.push(`edge ${e.from} -> ${e.to} names a missing node`);
    return ok;
  });
  edges.forEach((e) => { e.lw = e.label ? natural(e.label, MEDIUM, TYPE.label).w : 0; });
  // An edge to or from a composite state is laid out against its inner start, or its first member when it has
  // none, and drawn to the zone itself, so a label line declared early cannot pull a composite ahead of the
  // state that enters it.
  const firstOf = (zid) => (M.nodes.find((n) => n.zone === zid && n.kind === 'initial') || M.nodes.find((n) => n.zone === zid) || {}).id;
  const layoutEdges = edges
    .map((e) => ({ from: zoneIds.has(e.from) ? firstOf(e.from) : e.from, to: zoneIds.has(e.to) ? firstOf(e.to) : e.to, lw: e.lw }))
    .filter((e) => e.from && e.to && e.from !== e.to);
  const zones = (M.zones || []).map((z) => ({ ...z, kinds: M.nodes.filter((n) => n.zone === z.id).map((n) => n.kind) }));
  let L = layered(items, layoutEdges, { LR, zones, top: M.profile === 'er', zoneMode: M.zoneMode });
  if (L.clash.length) L = layered(items, layoutEdges, { LR, zones, top: M.profile === 'er', zoneMode: M.zoneMode, stack: true });
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
  const touch = (r, b, gap = 0) => cuts([{ x: r.x, y: r.y }, { x: r.x + r.w, y: r.y + r.h }], b, gap);
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
  // longest run when the route is pinned, where the label rides that run's own leg. A label is as wide as its
  // words along a level leg and as tall as a line along an upright one, and a leg without AIR past each end
  // of it reads as a broken line, because the label hides it, so that leg is marked short.
  const labelAt = (job, ln, pinned) => {
    let leg = 0, d = ln.n / 2;
    const w = job.e.lw + 16, room = (s) => s.b - s.a - (s.h ? w : 24);
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
    return { x: at.x - w / 2, y: at.y - 12, w, h: 24, leg, short: pinned && room(ln.s[leg]) < 2 * AIR };
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
      // A label keeps AIR clear of every box it does not name, so it never reads as that box's own.
      const onNode = labs.some((r) => r.short || items.some((n) => !mine.includes(n.id) && touch(r, L.box.get(n.id), AIR)));
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
  // The diagram's box holds its routes as well as its boxes, so a line that runs round the outside keeps the
  // board's margin and leaves the gap under the title block clear.
  const pts = jobs.flatMap((job) => job.cur.lines.flatMap((l) => l.pts));
  const grow = (vs, m) => [Math.min(0, ...vs.map((v) => (v < 0 ? -up8(24 - v) : 0))), Math.max(m, ...vs.map((v) => (v > m ? up8(v + 24) : m)))];
  const [x0, x1] = grow(pts.map((v) => v.x), L.width), [y0, y1] = grow(pts.map((v) => v.y), L.height);
  const kinds = [...new Set([...M.nodes.map((n) => n.kind), ...M.nodes.filter((n) => n.accent).map(() => 'focus')])];
  const marked = M.nodes.find((n) => n.accent);
  const key = kinds.map((kind) => (kind === 'focus' && marked ? { kind, like: marked.kind } : { kind }));
  return {
    width: x1 - x0, height: y1 - y0, key,
    draw(board, ox, oy) {
      ox -= x0;
      oy -= y0;
      const zoneNodes = zones.map((z, i) => {
        const b = L.zoneBox[i];
        return b ? zoneSection(board, z.label, tintFor(i, z.kinds, z.label, ox + b.x, oy + b.y, b.w, b.h), ox + b.x, oy + b.y, b.w, b.h) : null;
      });
      const zoneOf = new Map(zones.map((z, i) => [z.id, zoneNodes[i]]));
      const shapes = new Map();
      for (const n of M.nodes) {
        const b = L.box.get(n.id);
        const parent = zoneOf.get(n.zone) || board;
        const px = parent === board ? 0 : parent.x, py = parent === board ? 0 : parent.y;
        const card = cards.get(n.id);
        const label = card ? [n.label, ...card.lines].join('\n') : (FIXED[n.kind] ? '' : n.label);
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
      // Edges that arrive at one magnet each take their own point 24 px along that side, in the order their
      // sources stand across it, so no two run into one arrowhead. FigJam bends a plain connector itself, so the
      // first one keeps the magnet, and a pinned route's last corner moves with its point. A dot is where paths
      // join, so it keeps one point.
      const fan = {};
      jobs.forEach((j) => (fan[j.e.to + j.m1] = fan[j.e.to + j.m1] || []).push(j));
      Object.values(fan).forEach((list) => {
        const to = list[0].e.to, kind = (M.nodes.find((n) => n.id === to) || {}).kind, v = DIR[list[0].m1], b = boxOf(to);
        const [h, g, s] = v[0] ? ['y', 'x', 'h'] : ['x', 'y', 'w'];
        if (!list[1] || FIXED[kind]) return;
        // Two routes that turn in on one level take the side they come from, the one turning nearer outermost,
        // so neither crosses the other.
        const across = (j) => {
          const n = j.pts ? j.pts.length : 0, a = n ? j.pts[n - 2] : dock(j.e.from, j.m0), p = n > 2 ? j.pts[n - 3] : a;
          return a[h] + Math.sign(p[h] - a[h]) * (1e4 - Math.abs(a[g] - b[g])) / 1e6;
        };
        const c = Math.max(0, list.sort((a, o) => across(a) - across(o)).findIndex((j) => !j.pts));
        list.forEach((j, i) => {
          // A round shape's side slopes away from its magnet, so the point steps in to meet it.
          const d = (i - c) * 24, q = dock(to, j.m1), k = ROUND.has(shapeOf(kind)) ? Math.abs(d) / b[s] : 0;
          if (!d) return;
          j.m1 = { x: q.x - b.x + (v[0] ? -v[0] * k * b.w : d), y: q.y - b.y + (v[0] ? d : -v[1] * k * b.h) };
          if (j.pts) j.pts[j.pts.length - 2][h] += d;
        });
      });
      edges.forEach((e) => {
        const from = shapes.get(e.from) || zoneOf.get(e.from);
        const to = shapes.get(e.to) || zoneOf.get(e.to);
        const { m0, m1, pts, leg } = portsOf.get(e);
        // An ER relationship marks each end with its cardinality, so a reader sees which side is the many.
        const style = { dashed: e.style === 'dashed', startCap: e.ends ? ERD[e.ends[0]] : e.twoWay ? 'ARROW_LINES' : 'NONE',
          endCap: e.ends ? ERD[e.ends[1]] : e.undirected ? 'NONE' : 'ARROW_LINES' };
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

// ───────────────────────────────────────────────────────────────
// 6. SEQUENCE BOARDS
// ───────────────────────────────────────────────────────────────

function buildSequence(M) {
  const sizes = M.participants.map((p) => fit(p.label, 'ROUNDED_RECTANGLE'));
  const pw = Math.max(...sizes.map((s) => s.w));
  const ph = Math.max(...sizes.map((s) => s.h));
  // A foot repeats its participant's name at the label size, an echo of the head that adds no weight. A row is
  // as tall as a label and its air, so the board grows no taller than its messages need.
  const tall = natural('Ag', MEDIUM, TYPE.label).h;
  const fh = up8(tall + 24);
  const ROW = up8(tall + 40);
  const index = new Map(M.participants.map((p, i) => [p.id, i]));
  const centres = M.participants.map((_, i) => pw / 2 + i * (pw + 96));
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
  const top = ph + 48;
  const rows = [];
  let y = top;
  for (const m of M.messages) { rows.push(y); y += m.from === m.to ? ROW + SELF_DROP : ROW; }
  const bottom = y + 16;
  const width = centres[centres.length - 1] + Math.max(pw / 2, reach);
  const height = bottom + fh;
  const used = [...new Set([...M.messages.map((m) => m.arrow), ...M.messages.filter((m) => m.accent).map(() => 'focus')])];
  const key = [{ kind: 'participant' }, ...used.map((a) => ({ arrow: a })), { pin: true }];
  return {
    width, height, key,
    draw(board, ox, oy) {
      const heads = M.participants.map((p, i) => {
        const x = ox + centres[i] - pw / 2;
        const head = shape(board, 'participant', p.label, x, oy, pw, ph, `node:${p.id}`);
        const foot = shape(board, 'participant', p.label, x, oy + bottom, pw, fh, `foot:${p.id}`, TYPE.label);
        elements.push({ id: head.id, model: p.id, kind: 'participant', text: p.label });
        const life = connect(board, head, foot, { name: `life:${p.id}`, line: 'STRAIGHT', m0: 'BOTTOM', m1: 'TOP',
          endCap: 'NONE', color: T.line.lifeline });
        life.dashPattern = [6, 6];
        return head;
      });
      M.messages.forEach((m, k) => {
        const yy = oy + rows[k];
        const a = index.get(m.from), b = index.get(m.to);
        const style = { ...(ARROWS[m.arrow] || ARROWS.request), ...(m.accent ? { color: ACCENT, weight: T.accent.message } : {}) };
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
        // A step's number sits beside the lifeline its message leaves, on the side the message does not take.
        marker(board, String(k + 1), x + (b < a ? 16 : -48), yy - 16, `step:${k + 1}`);
      });
    },
  };
}

// ───────────────────────────────────────────────────────────────
// 7. GANTT BOARDS
// ───────────────────────────────────────────────────────────────

const MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
function buildGantt(M) {
  const day = M.unit === 'day';
  const span = Math.max(1, M.span);
  const scale = day ? Math.min(96, Math.max(8, snap(1680 / span))) : Math.min(8, Math.max(1, 1680 / span));
  const tick = day ? (span <= 14 ? 1 : span <= 70 ? 7 : span <= 200 ? 14 : 28) : (span <= 180 ? 30 : 60);
  const tasks = M.sections.flatMap((s) => s.tasks);
  // A section's name is measured in the face and size its section draws it in, so it never runs into a bar.
  const nameCol = up8(Math.max(240, ...tasks.map((t) => natural(t.name, MEDIUM, TYPE.label).w + 48),
    ...M.sections.map((s) => natural(s.label, SEMI, TYPE.zone).w + 64)));
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
  const marked = tasks.find((t) => t.accent);
  const key = [...new Set(tasks.map(statusOf))].map((kind) => ({ kind })).concat(marked ? [{ kind: 'focus', like: statusOf(marked) }] : []);
  return {
    width, height, key,
    draw(board, ox, oy) {
      // Grid lines are 1px rectangles, not connectors, so the read-back never counts them as edges.
      // Sections are opaque, so each one draws its own stretch of every line under its bars.
      const ticks = [], bars = new Map();
      for (let t = 0; t <= span; t += tick) ticks.push(t);
      const rule = (parent, x, top, hh, name) => {
        const r = figma.createRectangle();
        parent.appendChild(r);
        r.name = name;
        r.fills = solid('#D9D9D9');
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
        const sec = zoneSection(board, s.label, tintFor(i, s.tasks.map(statusOf), s.label, ox, oy + band.y, width, band.h), ox, oy + band.y, width, band.h);
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
            const fits = natural(words, MEDIUM, TYPE.small).w + 24 <= w;
            bar = shape(sec, status, fits ? words : '', bx, ry + (ROW - BAR) / 2 - 4, w, BAR, `node:${t.id || t.name}`, TYPE.small, t.accent);
          }
          elements.push({ id: bar.id, model: t.id || t.name, kind: status, text: t.name });
          bars.set(t.id || t.name, bar);
        });
      });
      // A dependency runs from the right end of the bar it waits on onto the top of the left end of the bar it
      // starts, so the arrow turns once and lands where that work begins. The check puts every bar an `after`
      // names above it. A milestone sits on that end, so its arrow drops from the bar's corner onto the diamond's
      // top, and one leaves a milestone from its foot. Arrows that leave one bar share its magnet, so a fork reads
      // as one, and each arrow into one bar lands 24 px along from the one before, the nearest bar's first, so none crosses.
      // A bar too short for that spacing takes its arrows closer together, so each lands on the bar and within 72 px of
      // its left end. Arrows into a milestone meet on its top, because a moment is a join with no room to spread them.
      const at = (id) => tasks.findIndex((x) => (x.id || x.name) === id);
      tasks.forEach((t) => (t.after || []).sort((a, b) => at(b) - at(a)).forEach((id, k) => {
        const me = t.id || t.name, from = bars.get(id), to = bars.get(me);
        if (!from) return warnings.push(`no task ${id} for ${me} to follow`);
        const ms = statusOf(t) === 'milestone';
        const c = connect(board, from, to, { name: `edge:${id}->${me}`, m0: from.shapeType === 'DIAMOND' ? 'BOTTOM'
          : ms ? { x: from.width, y: from.height } : 'RIGHT',
          m1: ms ? 'TOP' : { x: 8 + k * Math.min(24, (Math.min(to.width, 72) - 12) / Math.max(1, t.after.length - 1)), y: 0 } });
        links.push({ id: c.id, from: from.id, to: to.id, model: `${id}->${me}`, label: '' });
      }));
    },
  };
}

// ───────────────────────────────────────────────────────────────
// 8. THE BOARD
// ───────────────────────────────────────────────────────────────

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
board.fills = solid('#FFFFFF');
board.x = others.length ? snap(Math.max(...others.map((n) => n.x + n.width)) + 400) : 0;
board.y = others.length ? snap(Math.min(...others.map((n) => n.y))) : 0;
created.push(board.id);
const wrap = Math.min(Math.max(body.width, 960), 1440);
const title = text(board, MODEL.title, BOLD, TYPE.title, BOARD_PAD, BOARD_PAD);
let cursor = title.y + title.height + 16;
if (MODEL.subtitle) {
  const sub = text(board, MODEL.subtitle, REGULAR, TYPE.subtitle, BOARD_PAD, cursor, wrap);
  // A subtitle that wraps is narrowed for as long as it keeps its number of lines, so its lines come out even
  // and the last one never holds a single word.
  const lines = sub.height;
  if (lines > TYPE.subtitle * 1.6) {
    let lo = wrap / 2, hi = wrap;
    while (hi - lo > 8) { const w = (lo + hi) / 2; sub.resize(w, sub.height); if (sub.height > lines) lo = w; else hi = w; }
    sub.resize(hi, sub.height);
  }
  cursor = sub.y + sub.height;
}
const ox = BOARD_PAD;
const oy = up8(cursor + 64);
body.draw(board, ox, oy);
for (const line of MODEL.edgeStyles || []) body.key.push({ line });

// Key: one sample per kind and line the board uses, in the order a reader meets them, the focus last. It is
// as wide as the diagram, and an entry that would run past that edge starts a new row.
const key = figma.createSection();
board.appendChild(key);
key.name = 'Key';
key.fills = solid(TINT[T.key.tint] || TINT.gray);
key.x = BOARD_PAD;
key.y = oy + body.height + 64;
created.push(key.id);
text(key, T.key.title, SEMI, TYPE.zone, 32, 32);
const LINES = {
  solid: {}, dashedOptional: { dashed: true }, dashedAsync: { dashed: true }, identifying: { cap: 'NONE' },
  nonIdentifying: { dashed: true, cap: 'NONE' }, twoWay: { start: 'ARROW_LINES' },
};
// The focus entry carries the reason the model gives for it, so a reader sees why the accent falls there.
const FOCUS = T.kind.focus.key + (MODEL.why ? `: ${MODEL.why}` : '');
const KINDS = Object.keys(T.kind), LINE_ORDER = Object.keys(LINES), ARROW_ORDER = Object.keys(ARROWS);
const placeOf = (it) => (it.kind === 'focus' || it.arrow === 'focus' ? 999 : it.kind ? KINDS.indexOf(it.kind)
  : it.line ? 100 + LINE_ORDER.indexOf(it.line) : it.arrow ? 200 + ARROW_ORDER.indexOf(it.arrow) : 300);
const keyWidth = Math.max(body.width, 480);
let kx = 32, ky = 88, kr = 0;
for (const item of body.key.sort((a, b) => placeOf(a) - placeOf(b))) {
  const x0 = kx, made = [];
  let label;
  if (item.kind) {
    // The focus sample is drawn as the marked node is, its own kind under the accent's outline.
    const as = item.like || item.kind, f = FIXED[as], sh = shapeOf(as);
    const tall = sh === 'ENG_DATABASE' || sh === 'ENG_QUEUE';
    const sw = f ? Math.min(f[0], 56) : (ROUND.has(sh) ? 72 : (tall ? 48 : 88));
    const sht = f ? Math.min(f[1], 56) : (ROUND.has(sh) || tall ? 56 : 48);
    // FigJam keeps some shapes above a minimum size, so spacing follows the size it actually drew.
    const sample = shape(key, as, '', kx, ky, sw, sht, `key:${item.kind}`, 0, !!item.like);
    sample.y = ky + (56 - sample.height) / 2;
    made.push(sample);
    kx += sample.width + 16;
    label = item.kind === 'focus' ? FOCUS : T.kind[item.kind].key;
  } else if (item.pin) {
    made.push(marker(key, '1', kx, ky + 12, 'key:pin'));
    kx += 48;
    label = T.key.pin;
  } else {
    const spec = item.arrow ? ARROWS[item.arrow] : LINES[item.line];
    if (!spec) continue;
    const name = item.arrow || item.line;
    const a = anchor(key, kx + 8, ky + 28, `key:${name}:a`);
    const b = anchor(key, kx + 88, ky + 28, `key:${name}:b`);
    connect(key, a, b, { name: `key:${name}`, line: 'STRAIGHT', m0: 'POINT', m1: 'POINT',
      dashed: spec.dashed, endCap: spec.cap === undefined ? 'ARROW_LINES' : spec.cap, startCap: spec.start || 'NONE',
      color: spec.color, weight: spec.weight });
    made.push(a, b);
    kx += 112;
    label = name === 'focus' ? FOCUS : T.key[name];
  }
  const t = text(key, label, REGULAR, TYPE.label, kx, ky + 18);
  made.push(t);
  if (t.x + t.width > keyWidth - 32 && x0 > 32) {
    made.forEach((n) => { n.x += 32 - x0; n.y += 72; });
    ky += 72;
  }
  kr = Math.max(kr, t.x + t.width);
  kx = up8(t.x + t.width + 48);
}
key.resize(Math.max(keyWidth, up8(kr + 32)), ky + 88);
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
// rather than draw a second one, and names the design that drew it. Any plugin can read shared data, so it
// holds the title, the counts and the design's name only.
const TAG = 'productowner';
let tagged = true;
try {
  board.setSharedPluginData(TAG, MODEL.title, JSON.stringify({ written: new Date().toISOString(), counts, design: THEME.id || 'built-in' }));
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
