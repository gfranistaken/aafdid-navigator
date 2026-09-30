/*!
 * AAFDID Navigator engine 1.0.0
 * Evaluates a program profile against the AAFDID rules bundle (rules/aafdid-rules.json).
 * Runs in browsers (window.AAFDID) and in Node (require('./aafdid.js')). No dependencies.
 * Logic is three-valued: a condition is true, false, or unknown when an answer is missing.
 * Unknown never becomes "not applicable"; it becomes "undetermined" with the question to ask.
 * License: MIT.
 */
(function (root, factory) {
  if (typeof module === 'object' && module.exports) module.exports = factory();
  else root.AAFDID = factory();
}(typeof globalThis !== 'undefined' ? globalThis : this, function () {
  'use strict';

  var ENGINE_VERSION = '1.0.0';
  var STATUS_BY_KIND = {
    event: 'required', recurring: 'required', contract: 'required', compliance: 'required',
    conditional: 'conditional', triggered: 'triggered', reference: 'reference'
  };
  var STATUS_ORDER = ['required', 'conditional', 'triggered', 'undetermined', 'reference', 'not_applicable'];
  var UNORDERED_EVENTS = { other: true };

  function isUnknown(v) { return v === undefined || v === null || v === ''; }

  // ---------------------------------------------------------------- conditions
  function test(c, p) {
    if (!c || c['const'] === true) return true;
    if (c['const'] === false) return false;
    var i, r, unk;
    if (c.all) {
      unk = false;
      for (i = 0; i < c.all.length; i++) { r = test(c.all[i], p); if (r === false) return false; if (r === null) unk = true; }
      return unk ? null : true;
    }
    if (c.any) {
      unk = false;
      for (i = 0; i < c.any.length; i++) { r = test(c.any[i], p); if (r === true) return true; if (r === null) unk = true; }
      return unk ? null : false;
    }
    if (c.not) { r = test(c.not, p); return r === null ? null : !r; }
    var v = p[c.field];
    if (isUnknown(v)) return null;
    if ('eq' in c) return v === c.eq;
    if ('ne' in c) return v !== c.ne;
    if ('in' in c) return c['in'].indexOf(v) !== -1;
    var n = Number(v);
    if ('gte' in c) return n >= c.gte;
    if ('gt' in c) return n > c.gt;
    if ('lte' in c) return n <= c.lte;
    if ('lt' in c) return n < c.lt;
    throw new Error('Unknown condition: ' + JSON.stringify(c));
  }

  function fieldsOf(c, acc) {
    acc = acc || [];
    if (!c || typeof c !== 'object') return acc;
    ['all', 'any'].forEach(function (k) { (c[k] || []).forEach(function (x) { fieldsOf(x, acc); }); });
    if (c.not) fieldsOf(c.not, acc);
    if (c.field && acc.indexOf(c.field) === -1) acc.push(c.field);
    return acc;
  }

  // ---------------------------------------------------------------- answers
  var UNKNOWN_WORDS = ['unknown', '?', 'n/a', 'na', 'tbd', 'not sure', 'none given', 'unsure', "don't know", 'dont know'];

  function parseMoney(v) {
    if (typeof v === 'number') return isFinite(v) ? v : null;
    var s = String(v).trim().toLowerCase().replace(/[, $]/g, '');
    if (!s) return null;
    var m = s.match(/^(\d+(?:\.\d+)?)(k|thousand|m|mm|mil|million|b|bn|billion)?$/);
    if (!m) return null;
    var n = parseFloat(m[1]);
    var u = m[2] || '';
    if (u === 'k' || u === 'thousand') n *= 1e3;
    else if (u === 'm' || u === 'mm' || u === 'mil' || u === 'million') n *= 1e6;
    else if (u === 'b' || u === 'bn' || u === 'billion') n *= 1e9;
    return Math.round(n);
  }

  function parseBool(v) {
    if (typeof v === 'boolean') return v;
    var s = String(v).trim().toLowerCase();
    if (['yes', 'y', 'true', 't', '1'].indexOf(s) !== -1) return true;
    if (['no', 'n', 'false', 'f', '0'].indexOf(s) !== -1) return false;
    return null;
  }

  function normalize(bundle, input) {
    var qs = bundle.questions.questions;
    var out = {};
    input = input || {};
    if (input.program) out.program = String(input.program).trim();
    qs.forEach(function (q) {
      var v = input[q.id];
      if (isUnknown(v)) return;
      if (typeof v === 'string' && UNKNOWN_WORDS.indexOf(v.trim().toLowerCase()) !== -1) return;
      if (q.type === 'boolean') { v = parseBool(v); }
      else if (q.type === 'money') { v = parseMoney(v); }
      else if (q.type === 'choice') {
        var s = String(v).trim().toLowerCase();
        var hit = null;
        q.options.forEach(function (o) {
          if (o.value.toLowerCase() === s || o.label.toLowerCase() === s) hit = o.value;
        });
        v = hit;
      } else if (q.type === 'event') {
        v = String(v).trim();
      }
      if (!isUnknown(v)) out[q.id] = v;
    });
    if (out.event) {
      var pw = pathwayById(bundle, out.pathway);
      var evId = null;
      if (pw) pw.events.forEach(function (e) {
        var s = out.event.toLowerCase();
        if (e.id === out.event || e.short.toLowerCase() === s || e.name.toLowerCase() === s) evId = e.id;
      });
      if (evId) out.event = evId; else delete out.event;
    }
    return out;
  }

  function pathwayById(bundle, id) {
    for (var i = 0; i < bundle.pathways.length; i++) if (bundle.pathways[i].id === id) return bundle.pathways[i];
    return null;
  }

  function questionById(bundle, id) {
    var qs = bundle.questions.questions;
    for (var i = 0; i < qs.length; i++) if (qs[i].id === id) return qs[i];
    return null;
  }

  function visibleQuestions(bundle, profile) {
    return bundle.questions.questions.filter(function (q) {
      if (!q.show_if) return true;
      return test(q.show_if, profile) === true;
    });
  }

  // ---------------------------------------------------------------- services category
  function servicesCategory(bundle, p) {
    if (p.pathway !== 'aos') return null;
    var rows = {};
    (bundle.scat || []).forEach(function (s) { rows[s.id] = s; });
    var id = null, note = '';
    var t = p.svc_total_value, a = p.svc_annual_value;
    if (p.svc_special_interest === true) id = 'special_interest';
    else if (!isUnknown(t)) {
      if (t >= 1e9 || (!isUnknown(a) && a > 3e8)) id = 'I';
      else if (t >= 2.5e8) { id = 'II'; if (isUnknown(a) && t > 3e8) note = 'S-CAT I instead if more than $300M falls in any one year.'; }
      else if (t >= 1e8) id = 'III';
      else if (t >= 1e7) id = 'IV';
      else id = 'V';
      if (isUnknown(p.svc_special_interest)) note = (note ? note + ' ' : '') + 'Unless ASD(A) designates it Special Interest.';
    }
    if (!id) return { id: null, label: 'Undetermined', decision_authority: null, note: 'Enter the total estimated value.', cite: bundle.scat_cite };
    var r = rows[id] || {};
    return { id: id, label: r.label || id, rule: r.rule || '', decision_authority: r.decision_authority || '', note: note, cite: bundle.scat_cite };
  }

  // ---------------------------------------------------------------- evaluation
  function eventInfo(pw) {
    var idx = {}, order = 0;
    pw.events.forEach(function (e) { idx[e.id] = UNORDERED_EVENTS[e.id] ? null : order++; });
    return idx;
  }

  function groupFor(req, status, focus, idx) {
    if (status === 'not_applicable') return 'not_applicable';
    if (status === 'undetermined') return 'undetermined';
    if (status === 'reference') return 'reference';
    if (status === 'triggered') return 'triggered';
    if (status === 'conditional') return 'conditional';
    var evs = (req.when || []).map(function (w) { return w.event; });
    var ordered = evs.filter(function (e) { return idx[e] !== null && idx[e] !== undefined; });
    if (!evs.length) return 'ongoing';
    if (!focus) return 'by_event';
    if (evs.indexOf(focus) !== -1) return 'at_focus';
    if (idx[focus] === null) return ordered.length ? 'by_event' : 'as_required';
    var later = ordered.some(function (e) { return idx[e] > idx[focus]; });
    if (later) return 'later';
    if (ordered.length) return 'earlier';
    return 'as_required';
  }

  function assess(bundle, req, profile, pw, focus, idx, override) {
    var r = test(req.applies_if, profile);
    var status, missing = [], reason = '';
    if (r === true) {
      status = STATUS_BY_KIND[req.kind] || 'required';
    } else if (r === null) {
      status = 'undetermined';
      missing = fieldsOf(req.applies_if).filter(function (f) { return isUnknown(profile[f]); });
    } else {
      var c2 = req.conditional_if ? test(req.conditional_if, profile) : false;
      if (c2 === true) status = 'conditional';
      else if (c2 === null) { status = 'undetermined'; missing = fieldsOf(req.conditional_if).filter(function (f) { return isUnknown(profile[f]); }); }
      else { status = 'not_applicable'; reason = 'Applies when: ' + req.applies_when; }
    }
    if (override && status !== 'not_applicable' && status !== 'undetermined') status = override.status;
    var type = req.type, typeDepends = [];
    if (req.type_rule) {
      var tr = test(req.type_rule['if'], profile);
      if (tr === true) type = req.type_rule.then;
      else if (tr === false) type = req.type_rule['else'];
      else { type = 'depends'; typeDepends = fieldsOf(req.type_rule['if']).filter(function (f) { return isUnknown(profile[f]); }); }
    }
    var evMap = {};
    var srcPw = override ? pathwayById(bundle, req.pathways[0]) : pw;
    srcPw.events.forEach(function (e) { evMap[e.id] = e; });
    var when = (req.when || []).map(function (w) {
      var e = evMap[w.event] || { short: w.event, name: w.event };
      return { event: w.event, short: e.short, name: e.name, submission: w.submission };
    });
    var group = override ? (status === 'undetermined' ? 'undetermined' : 'review') : groupFor(req, status, focus, idx);
    var item = {
      code: req.code, id: req.id, name: req.name, status: status, group: group,
      type: type, type_text: req.type_text || '', source: req.source || '', approval: req.approval || '',
      when: when, due_text: req.due_text || '', applies_when: req.applies_when, notes: req.notes || '',
      table: req.table_name, url: req.url, rule_basis: req.rule_basis || '', kind: req.kind
    };
    if (req.procedure) item.procedure = req.procedure;
    if (req.footnotes && req.footnotes.length) item.footnotes = req.footnotes;
    if (req.note_has_conditions) item.note_has_conditions = true;
    if (req.currency && req.currency.length) item.currency = req.currency.slice();
    if (typeDepends.length) item.type_depends_on = typeDepends;
    if (missing.length) item.missing = missing;
    if (reason) item.reason = reason;
    if (override) item.review_reason = override.reason;
    if (req.phase) item.phase = req.phase;
    return item;
  }

  function evaluate(bundle, input) {
    var profile = normalize(bundle, input);
    var result = {
      engine: 'aafdid-navigator', engine_version: ENGINE_VERSION, rules_version: bundle.meta.version,
      aafdid_capture: bundle.meta.aafdid_capture, live_check: bundle.meta.live_check,
      profile: profile, pathway: null, focus_event: null, derived: {}, counts: {}, items: [],
      questions_needed: [], currency_notes: [], disclaimer: bundle.meta.disclaimer
    };
    var pw = pathwayById(bundle, profile.pathway);
    if (!pw) {
      result.questions_needed.push({ id: 'pathway', text: questionById(bundle, 'pathway').text, affects: bundle.requirements.length });
      return result;
    }
    result.pathway = { id: pw.id, code: pw.code, name: pw.name, instruction: pw.instruction, decision_authority: pw.decision_authority, aafdid_url: pw.aafdid_url, notes: pw.notes || [] };
    var idx = eventInfo(pw);
    var focus = profile.event && idx.hasOwnProperty(profile.event) ? profile.event : null;
    if (focus) pw.events.forEach(function (e) { if (e.id === focus) result.focus_event = { id: e.id, short: e.short, name: e.name }; });

    var items = [];
    bundle.requirements.forEach(function (req) {
      if (req.pathways.indexOf(pw.id) === -1) return;
      items.push(assess(bundle, req, profile, pw, focus, idx, null));
    });
    if (pw.also_review) {
      var ar = pw.also_review;
      var mapped = {};
      Object.keys(profile).forEach(function (k) { mapped[k] = profile[k]; });
      mapped[ar.map_field.to] = profile[ar.map_field.from];
      bundle.requirements.forEach(function (req) {
        if (req.pathways.indexOf(ar.pathway) === -1 || ar.tables.indexOf(req.table) === -1) return;
        if (isUnknown(mapped[ar.map_field.to])) return;
        if (test(req.applies_if, mapped) === false) return;
        var srcPw = pathwayById(bundle, ar.pathway);
        items.push(assess(bundle, req, mapped, srcPw, null, eventInfo(srcPw), { status: ar.status, reason: ar.reason }));
      });
    }

    if (pw.id === 'aos') {
      result.derived.services_category = servicesCategory(bundle, profile);
    }

    var gOrder = ['at_focus', 'by_event', 'later', 'ongoing', 'as_required', 'earlier', 'conditional', 'review', 'triggered', 'undetermined', 'reference', 'not_applicable'];
    function firstEvent(it) {
      var best = 99;
      it.when.forEach(function (w) { var k = idx[w.event]; if (k !== null && k !== undefined && k < best) best = k; });
      return best;
    }
    items.sort(function (a, b) {
      var ga = gOrder.indexOf(a.group), gb = gOrder.indexOf(b.group);
      if (ga !== gb) return ga - gb;
      var ea = firstEvent(a), eb = firstEvent(b);
      if (ea !== eb) return ea - eb;
      return a.code < b.code ? -1 : a.code > b.code ? 1 : 0;
    });
    result.items = items;

    STATUS_ORDER.forEach(function (s) { result.counts[s] = 0; });
    items.forEach(function (it) { result.counts[it.status] = (result.counts[it.status] || 0) + 1; });

    var need = {};
    items.forEach(function (it) {
      (it.missing || []).concat(it.type_depends_on || []).forEach(function (f) { need[f] = (need[f] || 0) + 1; });
    });
    visibleQuestions(bundle, profile).forEach(function (q) {
      if (need[q.id]) result.questions_needed.push({ id: q.id, text: q.text, affects: need[q.id] });
    });

    var used = {};
    items.forEach(function (it) { if (it.status !== 'not_applicable') (it.currency || []).forEach(function (c) { used[c] = true; }); });
    bundle.currency.notes.forEach(function (n) {
      var at = n.attach || {};
      var eventHit = focus && (at.events || []).indexOf(focus) !== -1 && (at.pathways || [pw.id]).indexOf(pw.id) !== -1;
      var qHit = (at.questions || []).some(function (q) { return visibleQuestions(bundle, profile).some(function (v) { return v.id === q; }); });
      if (n.banner || used[n.id] || eventHit || qHit) {
        result.currency_notes.push({ id: n.id, date: n.date, title: n.title, text: n.text, sources: n.sources, applies_here: !!(used[n.id] || eventHit || qHit) });
      }
    });
    return result;
  }

  // ---------------------------------------------------------------- profile block
  var BLOCK_HEADER = 'AAFDID PROFILE v1';

  function formatValue(q, v) {
    if (q.type === 'boolean') return v ? 'yes' : 'no';
    return String(v);
  }

  function toProfileBlock(bundle, input) {
    var p = normalize(bundle, input);
    var lines = [BLOCK_HEADER];
    if (p.program) lines.push('program: ' + p.program);
    var unknown = [];
    visibleQuestions(bundle, p).forEach(function (q) {
      if (isUnknown(p[q.id])) { if (q.id !== 'event') unknown.push(q.id); return; }
      lines.push(q.id + ': ' + formatValue(q, p[q.id]));
    });
    if (unknown.length) lines.push('unknown: ' + unknown.join(', '));
    return lines.join('\n');
  }

  function parseProfileBlock(text) {
    var out = {};
    String(text || '').split(/\r?\n/).forEach(function (line) {
      var m = line.match(/^\s*[-*]?\s*([A-Za-z_]+)\s*:\s*(.*?)\s*$/);
      if (!m) return;
      var k = m[1].toLowerCase(), v = m[2];
      if (k === 'unknown') return;
      out[k] = v;
    });
    return out;
  }

  // ---------------------------------------------------------------- markdown report
  var TYPE_LABEL = { statutory: 'Statutory', regulatory: 'Regulatory', both: 'Statutory and regulatory', unspecified: 'Not stated', depends: 'Depends on an answer' };
  var GROUP_TITLE = {
    at_focus: 'Due at the next event', by_event: 'Due by event', later: 'Due at later events', ongoing: 'Ongoing, contract-level and compliance items',
    as_required: 'As required', earlier: 'From earlier events (should already exist; check for updates)',
    conditional: 'May apply: check the condition', review: 'Also review: MCA entries AAFDID points UCA programs to',
    triggered: 'Only if triggered', undetermined: 'Needs an answer', reference: 'Reference rules', not_applicable: 'Not applicable'
  };

  function esc(s) { return String(s || '').replace(/\|/g, '\\|').replace(/\s+/g, ' ').trim(); }

  function whenText(it) {
    if (it.when && it.when.length) {
      return it.when.map(function (w) { return w.short + (w.submission === 'update' ? ' (update)' : ''); }).join(', ');
    }
    return it.due_text || '';
  }

  function toMarkdown(result, opts) {
    opts = opts || {};
    var L = [];
    if (!result.pathway) {
      L.push('# AAFDID requirements');
      L.push('');
      L.push('Pick a pathway first. Ask: ' + result.questions_needed[0].text);
      return L.join('\n');
    }
    var p = result.pathway;
    L.push('# AAFDID requirements: ' + (result.profile.program || p.name));
    L.push('');
    L.push('- Pathway: ' + p.name + ' (' + p.code + '), ' + p.instruction);
    L.push('- Next event: ' + (result.focus_event ? result.focus_event.name : 'not given; all events listed'));
    if (result.derived.services_category) {
      var sc = result.derived.services_category;
      L.push('- Services category: ' + sc.label + (sc.decision_authority ? '; decision authority: ' + sc.decision_authority : '') + (sc.note ? ' (' + sc.note + ')' : ''));
    }
    L.push('- Counts: ' + ['required', 'conditional', 'triggered', 'undetermined', 'not_applicable'].map(function (s) { return result.counts[s] + ' ' + s.replace('_', ' '); }).join(', '));
    L.push('- Rules ' + result.rules_version + ': AAFDID capture ' + result.aafdid_capture.split(' ')[0] + ', checked live ' + result.live_check.split(':')[0]);
    L.push('');
    var groups = {};
    result.items.forEach(function (it) { (groups[it.group] = groups[it.group] || []).push(it); });
    var order = ['at_focus', 'by_event', 'later', 'ongoing', 'as_required', 'earlier', 'conditional', 'review', 'triggered', 'undetermined', 'reference'];
    order.forEach(function (g) {
      var list = groups[g];
      if (!list || !list.length) return;
      var title = GROUP_TITLE[g];
      if (g === 'at_focus' && result.focus_event) title = 'Due at ' + result.focus_event.name;
      L.push('## ' + title + ' (' + list.length + ')');
      L.push('');
      if (g === 'undetermined') {
        L.push('| Code | Requirement | Missing answer |');
        L.push('| --- | --- | --- |');
        list.forEach(function (it) { L.push('| ' + it.code + ' | ' + esc(it.name) + ' | ' + esc((it.missing || []).join(', ')) + ' |'); });
      } else if (g === 'conditional' || g === 'triggered' || g === 'review') {
        L.push('| Code | Requirement | Type | Condition or trigger | Source |');
        L.push('| --- | --- | --- | --- | --- |');
        list.forEach(function (it) {
          var cond = g === 'triggered' ? (it.due_text || it.applies_when) : (g === 'review' ? whenText(it) : it.applies_when);
          L.push('| ' + it.code + ' | ' + esc(it.name) + ' | ' + TYPE_LABEL[it.type] + ' | ' + esc(cond) + ' | ' + esc(it.source) + ' |');
        });
      } else {
        L.push('| Code | Requirement | Type | When | Approval | Source |');
        L.push('| --- | --- | --- | --- | --- | --- |');
        list.forEach(function (it) {
          L.push('| ' + it.code + ' | ' + esc(it.name) + ' | ' + TYPE_LABEL[it.type] + ' | ' + esc(whenText(it)) + ' | ' + esc(it.approval || it.procedure || '') + ' | ' + esc(it.source) + ' |');
        });
      }
      L.push('');
    });
    if (result.questions_needed.length) {
      L.push('## Questions that would settle the undetermined items');
      L.push('');
      result.questions_needed.forEach(function (q) { L.push('- ' + q.text + ' (' + q.id + '; affects ' + q.affects + ')'); });
      L.push('');
    }
    var cn = result.currency_notes.filter(function (n) { return n.applies_here; });
    if (cn.length) {
      L.push('## Changes since AAFDID that affect this list');
      L.push('');
      cn.forEach(function (n) { L.push('- **' + n.title + '** (' + n.date + '). ' + n.text.replace(/\n+/g, ' ') + ' Source: ' + n.sources.map(function (s) { return '[' + s.title + '](' + s.url + ')'; }).join('; ')); });
      L.push('');
    }
    if (opts.includeNotApplicable !== false && groups.not_applicable) {
      L.push('## Not applicable (' + groups.not_applicable.length + ')');
      L.push('');
      groups.not_applicable.forEach(function (it) { L.push('- ' + it.code + ' ' + esc(it.name) + '. ' + esc(it.reason)); });
      L.push('');
    }
    L.push('_' + result.disclaimer + '_');
    return L.join('\n');
  }

  function toChecklist(result) {
    var L = [];
    if (!result.pathway) return '';
    L.push('AAFDID checklist: ' + (result.profile.program || result.pathway.name));
    result.items.forEach(function (it) {
      if (['required', 'conditional', 'triggered'].indexOf(it.status) === -1) return;
      var tag = it.status === 'required' ? '' : ' [' + (it.status === 'conditional' ? 'may apply' : 'if triggered') + ']';
      L.push('- [ ] ' + it.code + ' ' + it.name + tag + (whenText(it) ? ' (' + whenText(it) + ')' : ''));
    });
    return L.join('\n');
  }

  return {
    version: ENGINE_VERSION, test: test, fieldsOf: fieldsOf, normalize: normalize, evaluate: evaluate,
    visibleQuestions: visibleQuestions, servicesCategory: servicesCategory, toProfileBlock: toProfileBlock,
    parseProfileBlock: parseProfileBlock, toMarkdown: toMarkdown, toChecklist: toChecklist,
    parseMoney: parseMoney, TYPE_LABEL: TYPE_LABEL, GROUP_TITLE: GROUP_TITLE
  };
}));
