// ───────────────────────────────────────────────────────────────
// COMPONENT: COMPOSER TRACE
// ───────────────────────────────────────────────────────────────
// Runs a filled composer script against a recording stand-in for the Figma Plugin API and prints
// what it drew as JSON: every node with its absolute box, every connector with its two endpoints,
// the script's return value, and the error it threw, if any. A connector also reports its end caps,
// dash pattern, stroke and weight, so the arrow a message draws can be measured, and a shape reports its
// stroke, weight and fill, so the accent can be measured against every other mark. Text is measured with fixed
// Inter proportions, so the geometry is a model of the board and never a screenshot of it.
// Usage: node compose-trace.mjs <filled-code.js>
// Exit: 0 the trace was printed, including when the script under test threw, since that error rides in the
// JSON. 1 the file could not be read, with Node's error on stderr.
import { readFileSync } from 'node:fs';

const CHAR = 0.56;
const LINE = 1.21;
let serial = 1;

class Text {
  constructor(page) {
    this.id = `t${serial++}`;
    this.type = 'TEXT';
    this.parent = page;
    this.children = [];
    this.x = 0;
    this.y = 0;
    this.fontSize = 12;
    this.textAutoResize = 'WIDTH_AND_HEIGHT';
    this.chars = '';
    this.w = 0;
    this.h = 0;
    this.fixed = null;
  }
  get characters() { return this.chars; }
  set characters(v) { this.chars = v; this.measure(); }
  measure() {
    const cw = this.fontSize * CHAR, lh = this.fontSize * LINE, lines = this.chars.split('\n');
    if (this.textAutoResize === 'WIDTH_AND_HEIGHT') {
      this.w = Math.max(...lines.map((l) => l.length)) * cw;
      this.h = lines.length * lh;
    } else {
      const w = this.fixed === null ? this.w : this.fixed, per = Math.max(1, Math.floor(w / cw));
      this.w = w;
      this.h = lines.reduce((n, l) => n + Math.max(1, Math.ceil(l.length / per)), 0) * lh;
    }
  }
  get width() { return this.w; }
  get height() { return this.h; }
  resize(w, h) {
    this.fixed = w;
    this.w = w;
    if (this.textAutoResize === 'HEIGHT') this.measure(); else this.h = h;
  }
  setRangeFontName() {}
  setRangeFontSize() {}
  remove() { this.parent.children = this.parent.children.filter((c) => c !== this); }
}

class Node {
  constructor(page, type) {
    this.id = `${type[0]}${serial++}`;
    this.type = type;
    this.children = [];
    this.x = 0;
    this.y = 0;
    this.width = 100;
    this.height = 100;
    this.name = '';
    this.parent = page;
    if (type === 'SHAPE_WITH_TEXT' || type === 'CONNECTOR') this.text = new Text(this);
  }
  resize(w, h) { this.width = w; this.height = h; }
  appendChild(c) {
    c.parent.children = c.parent.children.filter((k) => k !== c);
    c.parent = this;
    this.children.push(c);
  }
  setSharedPluginData() {}
  async screenshot() { return {}; }
  remove() { this.parent.children = this.parent.children.filter((c) => c !== this); }
}

const absolute = (n) => {
  let x = 0, y = 0;
  for (let p = n; p.type !== 'PAGE'; p = p.parent) { x += p.x; y += p.y; }
  return { x, y };
};

export async function trace(code) {
  const page = { type: 'PAGE', children: [] };
  const make = (Kind, type) => () => { const n = new Kind(page, type); page.children.push(n); return n; };
  const figma = {
    currentPage: page,
    loadFontAsync: async () => {},
    createText: make(Text),
    createShapeWithText: make(Node, 'SHAPE_WITH_TEXT'),
    createConnector: make(Node, 'CONNECTOR'),
    createSection: make(Node, 'SECTION'),
    createRectangle: make(Node, 'RECTANGLE'),
  };
  const AsyncFunction = Object.getPrototypeOf(async function () {}).constructor;
  let result = null, error = null;
  try { result = await new AsyncFunction('figma', code)(figma); } catch (err) { error = String(err.message || err); }
  const nodes = [], connectors = [];
  const walk = (n) => {
    for (const c of n.children) {
      const a = absolute(c);
      if (c.type === 'CONNECTOR') {
        connectors.push({ name: c.name, start: c.connectorStart, end: c.connectorEnd, label: c.text.characters,
          line: c.connectorLineType, startCap: c.connectorStartStrokeCap, endCap: c.connectorEndStrokeCap,
          dash: c.dashPattern, stroke: c.strokes, weight: c.strokeWeight });
      } else {
        nodes.push({ id: c.id, name: c.name || '', type: c.type, shape: c.shapeType, x: a.x, y: a.y, w: c.width, h: c.height,
          text: c.type === 'TEXT' ? c.characters : (c.text ? c.text.characters : ''), parent: n.name || '',
          weight: c.strokeWeight, stroke: c.strokes, fill: c.fills });
      }
      walk(c);
    }
  };
  walk(page);
  return { result, error, nodes, connectors };
}

if (process.argv[2]) {
  process.stdout.write(JSON.stringify(await trace(readFileSync(process.argv[2], 'utf8'))));
}
