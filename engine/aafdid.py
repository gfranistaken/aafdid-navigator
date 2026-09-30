#!/usr/bin/env python3
"""AAFDID Navigator engine 1.1.0, Python port of engine/aafdid.js.

Evaluates a program profile against rules/aafdid-rules.json. Standard library only.
Logic is three-valued: a condition is True, False, or None (unknown) when an answer is missing.
Unknown never becomes "not applicable"; it becomes "undetermined" with the question to ask.
The output matches the JavaScript engine exactly; tests/run_tests.py checks this.

  python3 engine/aafdid.py profile.txt             Markdown report
  python3 engine/aafdid.py profile.json --json     JSON result
  python3 engine/aafdid.py profile.txt --checklist Checklist
  python3 engine/aafdid.py profile.txt --block     Normalized profile block
  python3 engine/aafdid.py - < profile.txt         Read the profile from stdin

License: MIT.
"""
import json, math, re, sys
from pathlib import Path

ENGINE_VERSION = "1.1.0"
STATUS_BY_KIND = {"event": "required", "recurring": "required", "contract": "required", "compliance": "required",
                  "conditional": "conditional", "triggered": "triggered", "reference": "reference"}
STATUS_ORDER = ["required", "conditional", "review", "triggered", "undetermined", "reference", "not_applicable"]
UNORDERED_EVENTS = {"other"}
UNKNOWN_WORDS = ["unknown", "?", "n/a", "na", "tbd", "not sure", "none given", "unsure", "don't know", "dont know"]
GROUP_ORDER = ["at_focus", "by_event", "later", "ongoing", "as_required", "earlier", "conditional", "review",
               "triggered", "undetermined", "reference", "not_applicable"]


def load_bundle(path=None):
    path = Path(path) if path else Path(__file__).resolve().parent.parent / "rules" / "aafdid-rules.json"
    return json.loads(path.read_text(encoding="utf-8"))


# ------------------------------------------------------------------ JavaScript semantics helpers
# The two engines must print byte-identical output, so the Python side reproduces the few
# JavaScript behaviors the engine relies on: String(), whitespace (\s and trim), Math.round,
# Number(), object key order and JSON.stringify.

JS_WS = "\t\n\x0b\x0c\r \xa0                　﻿"
WS = "[\\t\\n\\x0b\\x0c\\r \\xa0\\u1680\\u2000-\\u200a\\u2028\\u2029\\u202f\\u205f\\u3000\\ufeff]"   # JavaScript \s
NOT_LT = "[^\\n\\r\\u2028\\u2029]"                                                                       # JavaScript .
_WS_RUN = re.compile(WS + "+")
_SURROGATE = re.compile("[\ud800-\udfff]")
_INDEX_KEY = re.compile(r"(?:0|[1-9][0-9]*)\Z")


def js_trim(s):
    return s.strip(JS_WS)


def js_num(x):
    """Number.prototype.toString() for a float."""
    if x != x:
        return "NaN"
    if math.isinf(x):
        return "Infinity" if x > 0 else "-Infinity"
    if x == 0:
        return "0"
    if x < 0:
        return "-" + js_num(-x)
    r = repr(x)
    mant, _, e = r.partition("e")
    ip, _, fp = mant.partition(".")
    digits = ip + fp
    point = len(ip) + (int(e) if e else 0)
    stripped = digits.lstrip("0")
    point -= len(digits) - len(stripped)
    digits = stripped.rstrip("0") or "0"
    k, n = len(digits), point
    if k <= n <= 21:
        return digits + "0" * (n - k)
    if 0 < n <= 21:
        return digits[:n] + "." + digits[n:]
    if -6 < n <= 0:
        return "0." + "0" * (-n) + digits
    exp = n - 1
    return (digits[0] + ("." + digits[1:] if k > 1 else "")) + "e" + ("+" if exp >= 0 else "-") + str(abs(exp))


def js_str(v):
    """String(v) as JavaScript prints it, so both engines echo input the same way."""
    if v is None:
        return "null"
    if v is True:
        return "true"
    if v is False:
        return "false"
    if isinstance(v, int):
        return str(v) if abs(v) <= 2 ** 53 else js_num(float(v))
    if isinstance(v, float):
        return js_num(v)
    if isinstance(v, list):
        return ",".join("" if x is None else js_str(x) for x in v)
    if isinstance(v, dict):
        return "[object Object]"
    return str(v)


def js_truthy(v):
    if v is None or v is False or v == "":
        return False
    if isinstance(v, (int, float)) and not isinstance(v, bool):
        return v == v and v != 0
    return True


def _is_num(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool)


def js_eq(a, b):
    """JavaScript strict equality for the JSON value types a profile can hold."""
    if _is_num(a) and _is_num(b):
        return a == b
    if isinstance(a, bool) and isinstance(b, bool):
        return a == b
    if isinstance(a, str) and isinstance(b, str):
        return a == b
    return False


_JS_DEC = re.compile(r"[+-]?(?:Infinity|(?:[0-9]+\.?[0-9]*|\.[0-9]+)(?:[eE][+-]?[0-9]+)?)\Z")


def js_number(v):
    """Number(v) for the value types a profile can hold."""
    if isinstance(v, bool):
        return 1.0 if v else 0.0
    if isinstance(v, (int, float)):
        return float(v)
    if isinstance(v, str):
        t = js_trim(v)
        if t == "":
            return 0.0
        for pre, base in (("0x", 16), ("0o", 8), ("0b", 2)):
            if t[:2].lower() == pre:
                try:
                    return float(int(t[2:], base)) if re.fullmatch(r"[0-9a-fA-F]+", t[2:]) else float("nan")
                except ValueError:
                    return float("nan")
        if _JS_DEC.match(t):
            return float(t.replace("Infinity", "inf"))
    return float("nan")


def js_round(x):
    """Math.round: nearest integer, halves toward +infinity, exact at large magnitudes."""
    f = math.floor(x)
    return f + 1 if x - f >= 0.5 else f


def js_value(x):
    """A number as a JSON value both engines print the same way: int when whole and safe."""
    if isinstance(x, float) and x.is_integer() and abs(x) <= 2 ** 53:
        return int(x)
    return x


def js_keys(d):
    """Object.keys order: integer-like keys ascending, then the rest in insertion order."""
    idx = [k for k in d if isinstance(k, str) and _INDEX_KEY.match(k) and int(k) < 4294967295]
    rest = [k for k in d if k not in idx]
    return sorted(idx, key=int) + rest


def js_quote(s):
    """JSON.stringify for a string."""
    out = ['"']
    for ch in s:
        o = ord(ch)
        if ch == '"':
            out.append('\\"')
        elif ch == "\\":
            out.append("\\\\")
        elif ch == "\b":
            out.append("\\b")
        elif ch == "\f":
            out.append("\\f")
        elif ch == "\n":
            out.append("\\n")
        elif ch == "\r":
            out.append("\\r")
        elif ch == "\t":
            out.append("\\t")
        elif o < 0x20 or 0xD800 <= o <= 0xDFFF:
            out.append("\\u%04x" % o)
        else:
            out.append(ch)
    out.append('"')
    return "".join(out)


def js_json(o, level=0, indent="  "):
    """JSON.stringify(o, null, 2)."""
    if o is None:
        return "null"
    if o is True:
        return "true"
    if o is False:
        return "false"
    if isinstance(o, (int, float)):
        return js_str(o) if (isinstance(o, int) or math.isfinite(o)) else "null"
    if isinstance(o, str):
        return js_quote(o)
    pad, pad2 = indent * level, indent * (level + 1)
    if isinstance(o, (list, tuple)):
        if not o:
            return "[]"
        return "[\n" + ",\n".join(pad2 + js_json(x, level + 1, indent) for x in o) + "\n" + pad + "]"
    if isinstance(o, dict):
        if not o:
            return "{}"
        return "{\n" + ",\n".join(pad2 + js_quote(str(k)) + ": " + js_json(o[k], level + 1, indent) for k in js_keys(o)) + "\n" + pad + "}"
    return js_quote(str(o))


def is_unknown(v):
    return v is None or (isinstance(v, str) and v == "")


# ------------------------------------------------------------------ conditions

def test(c, p):
    if not js_truthy(c) or (isinstance(c, dict) and c.get("const") is True):
        return True
    if c.get("const") is False:
        return False
    if isinstance(c.get("all"), list):
        unk = False
        for x in c["all"]:
            r = test(x, p)
            if r is False:
                return False
            if r is None:
                unk = True
        return None if unk else True
    if isinstance(c.get("any"), list):
        unk = False
        for x in c["any"]:
            r = test(x, p)
            if r is True:
                return True
            if r is None:
                unk = True
        return None if unk else False
    if js_truthy(c.get("not")):
        r = test(c["not"], p)
        return None if r is None else (not r)
    v = p.get(c.get("field")) if isinstance(c.get("field"), str) else None
    if is_unknown(v):
        return None
    if "eq" in c:
        return js_eq(v, c["eq"])
    if "ne" in c:
        return not js_eq(v, c["ne"])
    if "in" in c:
        return any(js_eq(v, x) for x in c["in"])
    if isinstance(v, dict) and "lo" in v:
        return range_test(c, v)
    n = js_number(v)
    if "gte" in c:
        return n >= c["gte"]
    if "gt" in c:
        return n > c["gt"]
    if "lte" in c:
        return n <= c["lte"]
    if "lt" in c:
        return n < c["lt"]
    raise ValueError("Unknown condition: " + json.dumps(c))


def at_least(r, t):
    """A dollar range {lo, hi} stands for the amounts strictly between its ends (hi None: no upper
    end). Ranges are cut at the rules' thresholds, so a comparison is settled unless a threshold
    falls inside the range, which makes it unknown."""
    if r.get("lo") is not None and r["lo"] >= t:
        return True
    if r.get("hi") is not None and r["hi"] <= t:
        return False
    return None


def range_test(c, r):
    if "gte" in c:
        return at_least(r, c["gte"])
    if "gt" in c:
        return at_least(r, c["gt"])
    if "lte" in c:
        k = at_least(r, c["lte"])
        return None if k is None else (not k)
    if "lt" in c:
        k = at_least(r, c["lt"])
        return None if k is None else (not k)
    raise ValueError("Unknown condition: " + json.dumps(c))


def fields_of(c, acc=None):
    acc = [] if acc is None else acc
    if not isinstance(c, dict):
        return acc
    for k in ("all", "any"):
        for x in c.get(k) or []:
            fields_of(x, acc)
    if js_truthy(c.get("not")):
        fields_of(c["not"], acc)
    if js_truthy(c.get("field")) and c["field"] not in acc:
        acc.append(c["field"])
    return acc


def unknown_fields(c, p, acc=None):
    """Fields whose missing answers keep a condition unknown. Branches already settled
    (a false part of an "any", say) are skipped, so only the questions that matter are named."""
    acc = [] if acc is None else acc
    if not isinstance(c, dict) or test(c, p) is not None:
        return acc
    for k in ("all", "any"):
        if isinstance(c.get(k), list):
            for x in c[k]:
                unknown_fields(x, p, acc)
    if js_truthy(c.get("not")):
        unknown_fields(c["not"], p, acc)
    f = c.get("field")
    if js_truthy(f) and is_unknown(p.get(f)) and f not in acc:
        acc.append(f)
    return acc


# ------------------------------------------------------------------ answers

_MONEY_WORDS = re.compile(r"\b(usd|dollars?|then-?year|current-?year|ty|cy|about|approx(imately)?)\b", re.ASCII)
_MONEY_NUM = re.compile(r"(\d*\.?\d+(?:e[+-]?\d+)?)(k|thousand|m|mm|mil|million|b|bn|billion)?", re.ASCII)


def round_money(n):
    """Whole dollars when the value is whole (float noise removed), otherwise cents."""
    r = js_round(n)
    return js_value(float(r) if abs(n - r) < 1e-6 else js_round(n * 100) / 100)


def parse_money(v):
    if isinstance(v, bool):
        return None
    if isinstance(v, (int, float)):
        return round_money(float(v)) if math.isfinite(v) else None
    s = _MONEY_WORDS.sub("", js_trim(js_str(v)).lower())
    s = re.sub("[," + WS[1:-1] + "$~]", "", s)
    if not s:
        return None
    m = _MONEY_NUM.fullmatch(s)
    if not m:
        return None
    n = float(m.group(1))
    u = m.group(2) or ""
    if u in ("k", "thousand"):
        n *= 1e3
    elif u in ("m", "mm", "mil", "million"):
        n *= 1e6
    elif u in ("b", "bn", "billion"):
        n *= 1e9
    return round_money(n) if math.isfinite(n) else None


def parse_bool(v):
    if isinstance(v, bool):
        return v
    s = js_trim(js_str(v)).lower()
    if s in ("yes", "y", "true", "t", "1"):
        return True
    if s in ("no", "n", "false", "f", "0"):
        return False
    return None


def canon(s):
    return re.sub(r"[^a-z0-9]", "", js_str(s).lower())


def match_choice(q, v):
    c = canon(v)
    for o in q["options"]:
        if canon(o["value"]) == c:
            return o["value"]
    for o in q["options"]:
        if canon(o["label"]) == c or any(canon(a) == c for a in o.get("aliases") or []):
            return o["value"]
    return None


def range_for(q, n):
    """The range an amount falls in. A value exactly on a cut goes where the range bounds say."""
    for o in q.get("options") or []:
        lo_ok = n > o["lo"] or (o["lo_incl"] and n == o["lo"])
        hi_ok = o.get("hi") is None or n < o["hi"] or (o["hi_incl"] and n == o["hi"])
        if lo_ok and hi_ok:
            return o["value"]
    return None


def normalize_money(q, v):
    """A dollar answer: a range id, label or synonym, or an amount, which is stored as its range."""
    if isinstance(v, str):
        hit = match_choice(q, v)
        if hit:
            return hit
    n = parse_money(v)
    if n is None:
        return None
    return range_for(q, n) if q.get("options") else n


def match_event(pw, v):
    if not pw:
        return None
    c = canon(v)
    usable = [e for e in pw["events"] if not e.get("every")]
    for e in usable:
        if canon(e["id"]) == c:
            return e["id"]
    for e in usable:
        if canon(e["short"]) == c or canon(e["name"]) == c or any(canon(a) == c for a in e.get("aliases") or []):
            return e["id"]
    return None


def _unknown_word(v):
    return isinstance(v, str) and js_trim(v).lower() in UNKNOWN_WORDS


def normalize_detailed(bundle, inp):
    """Returns {"profile": ..., "unrecognized": [{"field", "value", "reason"}]}."""
    qs = bundle["questions"]["questions"]
    out, bad = {}, []
    if not isinstance(inp, dict):
        inp = {}
    known = {"program"} | {q["id"] for q in qs}
    for k in js_keys(inp):
        if k not in known and not is_unknown(inp[k]):
            bad.append({"field": k, "value": js_str(inp[k]), "reason": "not a profile field"})
    if js_truthy(inp.get("program")):
        pg = js_trim(_WS_RUN.sub(" ", js_str(inp["program"])))
        if pg:
            out["program"] = pg
    for q in qs:
        raw = inp.get(q["id"])
        v = raw
        if is_unknown(v) or q.get("type") == "event":
            continue
        if _unknown_word(v):
            continue
        t = q.get("type")
        if t == "boolean":
            v = parse_bool(v)
        elif t == "money":
            v = normalize_money(q, v)
        elif t == "choice":
            v = match_choice(q, v)
        if is_unknown(v):
            bad.append({"field": q["id"], "value": js_str(raw), "reason": "value not recognized"})
        else:
            out[q["id"]] = v
    ev = inp.get("event")
    if not is_unknown(ev) and not _unknown_word(ev):
        eid = match_event(pathway_by_id(bundle, out.get("pathway")), ev)
        if eid:
            out["event"] = eid
        else:
            bad.append({"field": "event", "value": js_str(ev),
                        "reason": "not an event of this pathway" if js_truthy(out.get("pathway")) else "pathway missing"})
    return {"profile": out, "unrecognized": bad}


def normalize(bundle, inp):
    return normalize_detailed(bundle, inp)["profile"]


def eval_profile(bundle, profile):
    """The profile with each dollar range replaced by its bounds, for evaluating conditions."""
    ep = dict(profile)
    for q in bundle["questions"]["questions"]:
        if q.get("type") != "money" or not isinstance(ep.get(q["id"]), str):
            continue
        for o in q.get("options") or []:
            if o["value"] == ep[q["id"]]:
                ep[q["id"]] = {"lo": o["lo"], "hi": o.get("hi")}
    return ep


def pathway_by_id(bundle, pid):
    for p in bundle["pathways"]:
        if p["id"] == pid:
            return p
    return None


def question_by_id(bundle, qid):
    for q in bundle["questions"]["questions"]:
        if q["id"] == qid:
            return q
    return None


def visible_questions(bundle, profile):
    return [q for q in bundle["questions"]["questions"] if not q.get("show_if") or test(q["show_if"], profile) is True]


# ------------------------------------------------------------------ services category

def services_category(bundle, p):
    """p is the evaluation profile: dollar answers are ranges (or amounts). Thresholds come from bundle["scat"]."""
    if p.get("pathway") != "aos":
        return None
    rows = {r["id"]: r for r in bundle.get("scat") or []}

    def cmp(v, op, n):
        if n is None:
            return None
        return test({"field": "v", op: n}, {"v": v})
    si_note = "Unless ASD(A) designates it Special Interest."
    sid, note = None, ""
    t, a = p.get("svc_total_value"), p.get("svc_annual_value")
    si_unknown = is_unknown(p.get("svc_special_interest"))
    one = rows.get("I") or {}
    a_over = cmp(a, "gt", one.get("annual_gt"))
    if p.get("svc_special_interest") is True:
        sid = "special_interest"
    elif a_over is True:
        sid = "I"
        if si_unknown:
            note = si_note
    elif not is_unknown(t):
        at = [cmp(t, "gte", (rows.get(k) or {}).get("total_gte")) for k in ("I", "II", "III", "IV")]
        if at[0] is True:
            sid = "I"
        elif at[0] is False and at[1] is True:
            sid = "II"
            if a_over is None and cmp(t, "gt", one.get("annual_gt")) is not False:
                note = "S-CAT I instead if more than $300M falls in any one year."
        elif at[1] is False and at[2] is True:
            sid = "III"
        elif at[2] is False and at[3] is True:
            sid = "IV"
        elif at[3] is False:
            sid = "V"
            note = "Only if above the simplified acquisition threshold; below it, DoDI 5000.74 does not apply."
        if sid and si_unknown:
            note = (note + " " if note else "") + si_note
    if not sid:
        return {"id": None, "label": "Undetermined", "decision_authority": None, "note": "Answer the total estimated value.",
                "cite": bundle.get("scat_cite")}
    r = rows.get(sid, {})
    return {"id": sid, "label": r.get("label") or sid, "rule": r.get("rule") or "",
            "decision_authority": r.get("decision_authority") or "", "note": note, "cite": bundle.get("scat_cite")}


# ------------------------------------------------------------------ evaluation

def event_info(pw):
    idx, order, every = {}, 0, {}
    for e in pw["events"]:
        if e["id"] in UNORDERED_EVENTS or e.get("every"):
            idx[e["id"]] = None
        else:
            idx[e["id"]] = order
            order += 1
        if e.get("every"):
            every[e["id"]] = True
    idx["__every"] = every
    return idx


def group_for(req, status, focus, idx):
    if status in ("not_applicable", "undetermined", "reference", "triggered", "conditional"):
        return status
    evs = [w["event"] for w in req.get("when") or []]
    ordered = [e for e in evs if isinstance(idx.get(e), int)]
    if not evs:
        return "ongoing"
    if not focus:
        return "by_event"
    if any(e in idx["__every"] for e in evs):
        return "at_focus"
    if focus in evs:
        return "at_focus"
    if idx.get(focus) is None:
        return "by_event" if ordered else "as_required"
    if any(idx[e] > idx[focus] for e in ordered):
        return "later"
    if ordered:
        return "earlier"
    return "as_required"


def assess(bundle, req, profile, pw, focus, idx, override):
    r = test(req["applies_if"], profile)
    missing, reason = [], ""
    if r is True:
        status = STATUS_BY_KIND.get(req["kind"], "required")
    elif r is None:
        status = "undetermined"
        missing = unknown_fields(req["applies_if"], profile)
    else:
        c2 = test(req["conditional_if"], profile) if req.get("conditional_if") else False
        if c2 is True:
            status = "conditional"
        elif c2 is None:
            status = "undetermined"
            missing = unknown_fields(req["conditional_if"], profile)
        else:
            status = "not_applicable"
            reason = "Applies when: " + req["applies_when"]
    if override and status not in ("not_applicable", "undetermined"):
        status = override["status"]
    typ, type_depends, ev_type = req["type"], [], None
    rule = req.get("type_rule")
    if rule:
        tr = test(rule["if"], profile)
        if tr is True and isinstance(rule.get("events"), list):
            # The type differs by event: rule["then"] at the listed events, rule["else"] at the others.
            # The item's type is the one at the next event when it is due there, otherwise the mix.
            ev_type, kinds = {}, []
            for w in req.get("when") or []:
                k = rule["then"] if w["event"] in rule["events"] else rule["else"]
                ev_type[w["event"]] = k
                if k not in kinds:
                    kinds.append(k)
            if focus and ev_type.get(focus):
                typ = ev_type[focus]
            else:
                typ = kinds[0] if len(kinds) == 1 else ("both" if kinds else rule["then"])
        elif tr is True:
            typ = rule["then"]
        elif tr is False:
            typ = rule["else"]
        else:
            typ = rule["unknown"] if rule.get("unknown") and rule["unknown"] != "depends" else "depends"
            type_depends = unknown_fields(rule["if"], profile)
    src_pw = pathway_by_id(bundle, req["pathways"][0]) if override else pw
    ev_map = {e["id"]: e for e in src_pw["events"]}
    when = []
    for w in req.get("when") or []:
        e = ev_map.get(w["event"], {"short": w["event"], "name": w["event"]})
        o = {"event": w["event"], "short": e["short"], "name": e["name"], "submission": w["submission"]}
        if ev_type is not None:
            o["type"] = ev_type[w["event"]]
        when.append(o)
    if override:
        group = "undetermined" if status == "undetermined" else "review"
    else:
        group = group_for(req, status, focus, idx)
    item = {"code": req["code"], "id": req["id"], "name": req["name"], "status": status, "group": group,
            "type": typ, "type_text": req.get("type_text") or "", "source": req.get("source") or "",
            "approval": req.get("approval") or "", "when": when, "due_text": req.get("due_text") or "",
            "applies_when": req["applies_when"], "notes": req.get("notes") or "", "table": req["table_name"],
            "url": req["url"], "rule_basis": req.get("rule_basis") or "", "kind": req["kind"]}
    if req.get("procedure"):
        item["procedure"] = req["procedure"]
    if req.get("tool_note"):
        item["tool_note"] = req["tool_note"]
    if req.get("footnotes"):
        item["footnotes"] = req["footnotes"]
    if req.get("note_has_conditions"):
        item["note_has_conditions"] = True
    if req.get("currency"):
        item["currency"] = list(req["currency"])
    if type_depends:
        item["type_depends_on"] = type_depends
    if missing:
        item["missing"] = missing
    if reason:
        item["reason"] = reason
    if override:
        item["review_reason"] = override["reason"]
    if req.get("phase"):
        item["phase"] = req["phase"]
    return item


def evaluate(bundle, inp):
    nd = normalize_detailed(bundle, inp)
    profile = nd["profile"]
    ep = eval_profile(bundle, profile)
    meta = bundle["meta"]
    result = {"engine": "aafdid-navigator", "engine_version": ENGINE_VERSION, "rules_version": meta["version"],
              "aafdid_capture": meta["aafdid_capture"], "live_check": meta["live_check"], "profile": profile,
              "pathway": None, "focus_event": None, "derived": {}, "counts": {}, "items": [],
              "questions_needed": [], "currency_notes": [], "unrecognized": nd["unrecognized"],
              "disclaimer": meta["disclaimer"]}
    pw = pathway_by_id(bundle, profile.get("pathway"))
    if not pw:
        result["questions_needed"].append({"id": "pathway", "text": question_by_id(bundle, "pathway")["text"],
                                           "affects": len(bundle["requirements"])})
        return result
    result["pathway"] = {"id": pw["id"], "code": pw["code"], "name": pw["name"], "instruction": pw["instruction"],
                         "decision_authority": pw["decision_authority"], "aafdid_url": pw["aafdid_url"],
                         "notes": pw.get("notes") or []}
    idx = event_info(pw)
    ev = profile.get("event")
    focus = ev if js_truthy(ev) and ev in idx else None
    if focus:
        for e in pw["events"]:
            if e["id"] == focus:
                result["focus_event"] = {"id": e["id"], "short": e["short"], "name": e["name"]}
    items = [assess(bundle, req, ep, pw, focus, idx, None) for req in bundle["requirements"] if pw["id"] in req["pathways"]]
    # Entries of another pathway's tables that AAFDID says to review too (UCA -> MCA ACAT II/III).
    # Until the mapped answer is given they are not listed; the question counts them instead.
    review_pending = 0
    ar = pw.get("also_review")
    if ar:
        mapped = dict(ep)
        mapped[ar["map_field"]["to"]] = ep.get(ar["map_field"]["from"])
        for req in bundle["requirements"]:
            if ar["pathway"] not in req["pathways"] or req["table"] not in ar["tables"]:
                continue
            if test(req["applies_if"], mapped) is False:
                continue
            if is_unknown(mapped.get(ar["map_field"]["to"])):
                # Count the entry if some answer to the question could bring it in.
                q = question_by_id(bundle, ar["map_field"]["from"])
                could = any(test(req["applies_if"], dict(mapped, **{ar["map_field"]["to"]: o["value"]})) is not False
                            for o in ((q or {}).get("options") or []))
                if could:
                    review_pending += 1
                continue
            src_pw = pathway_by_id(bundle, ar["pathway"])
            items.append(assess(bundle, req, mapped, src_pw, None, event_info(src_pw), {"status": ar["status"], "reason": ar["reason"]}))
    if pw["id"] == "aos":
        result["derived"]["services_category"] = services_category(bundle, ep)

    def first_event(it):
        best = 99
        for w in it["when"]:
            k = idx.get(w["event"])
            if isinstance(k, int) and k < best:
                best = k
        return best
    items.sort(key=lambda it: (GROUP_ORDER.index(it["group"]), first_event(it), it["code"]))
    result["items"] = items
    for s in STATUS_ORDER:
        result["counts"][s] = 0
    for it in items:
        result["counts"][it["status"]] = result["counts"].get(it["status"], 0) + 1
    need = {}
    for it in items:
        for f in (it.get("missing") or []) + (it.get("type_depends_on") or []):
            need[f] = need.get(f, 0) + 1
    if review_pending:
        k = ar["map_field"]["from"]
        need[k] = need.get(k, 0) + review_pending
    vis = visible_questions(bundle, profile)
    for q in vis:
        if need.get(q["id"]):
            result["questions_needed"].append({"id": q["id"], "text": q["text"], "affects": need[q["id"]]})
    used = set()
    for it in items:
        if it["status"] != "not_applicable":
            used.update(it.get("currency") or [])
    vis_ids = {v["id"] for v in vis}
    for n in bundle["currency"]["notes"]:
        at = n.get("attach") or {}
        event_hit = bool(focus) and focus in (at.get("events") or []) and pw["id"] in (at.get("pathways") or [pw["id"]])
        q_hit = any(q in vis_ids for q in (at.get("questions") or []))
        if n.get("banner") or n["id"] in used or event_hit or q_hit:
            result["currency_notes"].append({"id": n["id"], "date": n["date"], "title": n["title"], "text": n["text"],
                                             "sources": n["sources"], "applies_here": bool(n["id"] in used or event_hit or q_hit)})
    return result


# ------------------------------------------------------------------ profile block

BLOCK_HEADER = "AAFDID PROFILE v1"


def format_value(q, v):
    if q.get("type") == "boolean":
        return "yes" if v else "no"
    return js_str(v)


def to_profile_block(bundle, inp):
    p = normalize(bundle, inp)
    lines = [BLOCK_HEADER]
    if p.get("program"):
        lines.append("program: " + p["program"])
    unknown = []
    for q in visible_questions(bundle, p):
        if is_unknown(p.get(q["id"])):
            if q["id"] != "event":
                unknown.append(q["id"])
            continue
        lines.append(q["id"] + ": " + format_value(q, p[q["id"]]))
    if unknown:
        lines.append("unknown: " + ", ".join(unknown))
    return "\n".join(lines)


_BLOCK_LINE = re.compile("^" + WS + "*[-*]?" + WS + "*([A-Za-z_]+)" + WS + "*:" + WS + "*(" + NOT_LT + "*?)" + WS + "*\\Z")


def parse_profile_block(text):
    out = {}
    text = js_str(text) if js_truthy(text) else ""
    if text.startswith("\ufeff"):
        text = text[1:]
    for line in re.split(r"\r\n|\r|\n", text):
        clean = re.sub(r"\*\*|__|`", "", line)
        m = _BLOCK_LINE.match(clean)
        if not m:
            continue
        k, v = m.group(1).lower(), m.group(2)
        if k == "unknown":
            continue
        out[k] = v
    return out


# ------------------------------------------------------------------ markdown report

TYPE_LABEL = {"statutory": "Statutory", "regulatory": "Regulatory", "both": "Statutory and regulatory",
              "unspecified": "Not stated", "depends": "Depends on an answer"}
GROUP_TITLE = {
    "at_focus": "Due at the next event", "by_event": "Due by event", "later": "Due at later events",
    "ongoing": "Ongoing, contract-level and compliance items", "as_required": "As required",
    "earlier": "From earlier events (should already exist; check for updates)",
    "conditional": "May apply: check the condition", "review": "Also review: MCA entries AAFDID points UCA programs to",
    "triggered": "Only if triggered", "undetermined": "Needs an answer", "reference": "Reference rules",
    "not_applicable": "Not applicable"}
COUNT_WORDS = [("required", "required"), ("conditional", "may apply"), ("review", "also review"), ("triggered", "triggered"),
               ("undetermined", "need an answer"), ("not_applicable", "not applicable")]


def esc(s):
    return js_trim(_WS_RUN.sub(" ", str(s or "").replace("|", "\\|")))


def when_bits(w):
    b = []
    if w["submission"] == "update":
        b.append("update")
    if w.get("type"):
        b.append(w["type"])
    return " (" + ", ".join(b) + ")" if b else ""


def when_text(it):
    if it.get("when"):
        return ", ".join(w["short"] + when_bits(w) for w in it["when"])
    return it.get("due_text") or ""


def ignored_text(result):
    return "; ".join(u["field"] + " = " + u["value"] + " (" + u["reason"] + ")" for u in result.get("unrecognized") or [])


def to_markdown(result, include_not_applicable=True):
    L = []
    if not result["pathway"]:
        L += ["# AAFDID requirements", "", "Pick a pathway first. Ask: " + result["questions_needed"][0]["text"]]
        if result.get("unrecognized"):
            L += ["", "Ignored input: " + ignored_text(result)]
        return "\n".join(L)
    p = result["pathway"]
    L.append("# AAFDID requirements: " + (result["profile"].get("program") or p["name"]))
    L.append("")
    L.append("- Pathway: " + p["name"] + " (" + p["code"] + "), " + p["instruction"])
    L.append("- Next event: " + (result["focus_event"]["name"] if result["focus_event"] else "not given; all events listed"))
    sc = result["derived"].get("services_category")
    if sc:
        L.append("- Services category: " + sc["label"] + ("; decision authority: " + sc["decision_authority"] if sc.get("decision_authority") else "")
                 + (" (" + sc["note"] + ")" if sc.get("note") else ""))
    L.append("- Counts: " + ", ".join(str(result["counts"][k]) + " " + w for k, w in COUNT_WORDS if k != "review" or result["counts"].get("review")))
    if result.get("unrecognized"):
        L.append("- Ignored input: " + ignored_text(result))
    L.append("- Rules " + result["rules_version"] + ": AAFDID capture " + result["aafdid_capture"].split(" ")[0]
             + ", checked live " + result["live_check"].split(":")[0])
    L.append("")
    groups = {}
    for it in result["items"]:
        groups.setdefault(it["group"], []).append(it)
    for g in ["at_focus", "by_event", "later", "ongoing", "as_required", "earlier", "conditional", "review", "triggered", "undetermined", "reference"]:
        lst = groups.get(g)
        if not lst:
            continue
        title = GROUP_TITLE[g]
        if g == "at_focus" and result["focus_event"]:
            title = "Due at " + result["focus_event"]["name"]
        L.append("## " + title + " (" + str(len(lst)) + ")")
        L.append("")
        if g == "undetermined":
            L.append("| Code | Requirement | Missing answer |")
            L.append("| --- | --- | --- |")
            for it in lst:
                L.append("| " + it["code"] + " | " + esc(it["name"]) + " | " + esc(", ".join(it.get("missing") or [])) + " |")
        elif g in ("conditional", "triggered", "review"):
            L.append("| Code | Requirement | Type | Condition or trigger | Source |")
            L.append("| --- | --- | --- | --- | --- |")
            for it in lst:
                cond = (it.get("due_text") or it["applies_when"]) if g == "triggered" else (when_text(it) if g == "review" else it["applies_when"])
                L.append("| " + it["code"] + " | " + esc(it["name"]) + " | " + TYPE_LABEL[it["type"]] + " | " + esc(cond) + " | " + esc(it["source"]) + " |")
        else:
            L.append("| Code | Requirement | Type | When | Approval | Source |")
            L.append("| --- | --- | --- | --- | --- | --- |")
            for it in lst:
                L.append("| " + it["code"] + " | " + esc(it["name"]) + " | " + TYPE_LABEL[it["type"]] + " | " + esc(when_text(it)) + " | "
                         + esc(it.get("approval") or it.get("procedure") or "") + " | " + esc(it["source"]) + " |")
        L.append("")
    if result["questions_needed"]:
        L.append("## Questions that would settle more of the list")
        L.append("")
        for q in result["questions_needed"]:
            L.append("- " + q["text"] + " (" + q["id"] + "; affects " + str(q["affects"]) + ")")
        L.append("")
    cn = [n for n in result["currency_notes"] if n["applies_here"]]
    if cn:
        L.append("## Changes since AAFDID that affect this list")
        L.append("")
        for n in cn:
            L.append("- **" + n["title"] + "** (" + n["date"] + "). " + re.sub(r"\n+", " ", n["text"]) + " Source: "
                     + "; ".join("[" + s["title"] + "](" + s["url"] + ")" for s in n["sources"]))
        L.append("")
    if include_not_applicable and groups.get("not_applicable"):
        L.append("## Not applicable (" + str(len(groups["not_applicable"])) + ")")
        L.append("")
        for it in groups["not_applicable"]:
            L.append("- " + it["code"] + " " + esc(it["name"]) + ". " + esc(it.get("reason")))
        L.append("")
    L.append("_" + result["disclaimer"] + "_")
    return "\n".join(L)


CHECK_TAG = {"conditional": "may apply", "review": "also review", "triggered": "if triggered"}


def to_checklist(result):
    if not result["pathway"]:
        return ""
    L = ["AAFDID checklist: " + (result["profile"].get("program") or result["pathway"]["name"])]
    for it in result["items"]:
        if it["status"] not in ("required", "conditional", "review", "triggered"):
            continue
        tag = "" if it["status"] == "required" else " [" + CHECK_TAG[it["status"]] + "]"
        wt = when_text(it)
        L.append("- [ ] " + it["code"] + " " + it["name"] + tag + (" (" + wt + ")" if wt else ""))
    return "\n".join(L)


def _no_constant(name):
    raise ValueError("JSON does not allow " + name)


def _js_int(s):
    n = int(s)
    return n if abs(n) <= 2 ** 53 else float(s)


def parse_input(text):
    """A profile from text: JSON if it parses as JSON (as JSON.parse would), otherwise a profile block."""
    text = "" if text is None else str(text)
    if text.startswith("\ufeff"):
        text = text[1:]
    try:
        return json.loads(text, parse_constant=_no_constant, parse_int=_js_int)
    except (ValueError, RecursionError):
        return parse_profile_block(text)


def write_out(text):
    """Write UTF-8 like Node does, whatever the console encoding; lone surrogates become U+FFFD."""
    sys.stdout.buffer.write((_SURROGATE.sub("\ufffd", text) + "\n").encode("utf-8"))
    sys.stdout.flush()


def main(argv):
    files = [a for a in argv if not a.startswith("--")]
    if not files:
        print(__doc__)
        return 2
    bundle = load_bundle()
    raw = sys.stdin.buffer.read() if files[0] == "-" else Path(files[0]).read_bytes()
    inp = parse_input(raw.decode("utf-8", errors="replace"))
    result = evaluate(bundle, inp)
    if "--json" in argv:
        write_out(js_json(result))
    elif "--block" in argv:
        write_out(to_profile_block(bundle, inp))
    elif "--checklist" in argv:
        write_out(to_checklist(result))
    else:
        write_out(to_markdown(result))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
