#!/usr/bin/env python3
"""Build rules/requirements.json and the rules/aafdid-rules.json bundle.

Inputs
  sources/aafdid-capture/*.json          AAFDID tables captured Aug 2026 (print-to-PDF, via aafdid-open)
  sources/corrections-2026-09-30.json    fixes found by the live AAFDID check on 2026-09-30
  sources/aos-dodi-5000-74.json          Acquisition of Services entries drawn from DoDI 5000.74
  rules/pathways.json, rules/questions.json, rules/currency.json   hand-authored

Every requirement keeps AAFDID's own words for its name, type, source, approval
authority and notes. Applicability comes from AAFDID's marks (program type,
system size, events). Where this tool adds a condition that is not a mark in
the table, the record says why in `rule_basis`.
"""
import json, re, sys, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAP = ROOT / "sources" / "aafdid-capture"
RULES = ROOT / "rules"
VERSION = "1.0.0"
CAPTURED = "2026-08-22"
CHECKED = "2026-09-30"

def load(p):
    return json.loads(Path(p).read_text())

pathways = load(RULES / "pathways.json")
questions = load(RULES / "questions.json")
currency = load(RULES / "currency.json")
corr = load(ROOT / "sources" / "corrections-2026-09-30.json")
aos = load(ROOT / "sources" / "aos-dodi-5000-74.json")

PW = {p["id"]: p for p in pathways["pathways"]}
TABLES = {(p["id"], t["id"]): t for p in pathways["pathways"] for t in p.get("tables", [])}
TABLES[("any", "evm")] = {"id": "evm", "name": "EVMS Application and Reporting Requirements (AAFDID: not specific to any one pathway)",
                          "url": "https://www.waru.edu/aafdid/EVMS-Application-Requirements"}

def corrections_for(fname):
    return [c for c in corr["corrections"] if c["file"] == fname]

def slug(s, n=56):
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return s[:n].rstrip("-")

def norm_type(t):
    t = (t or "").strip()
    tl = t.lower()
    if not t or tl == "none":
        return "unspecified"
    has_s, has_r = "statutory" in tl, "regulatory" in tl
    if has_s and has_r:
        return "both"
    if has_s:
        return "statutory"
    if has_r:
        return "regulatory"
    return "unspecified"

def clean_notes(s):
    if not s:
        return ""
    s = s.strip()
    if len(s) >= 2 and s[0] == '"' and s[-1] == '"':
        s = s[1:-1]
    return re.sub(r"\s+", " ", s).strip()

COND_RX = re.compile(r"\b(only (required|applies|applicable|for)|if (the|a|an|applicable|required)|as applicable|when (the|a|an)|for programs (on|that|with|using)|unless|may be required)\b", re.I)

out = []
used_ids = set()

def add(rec):
    base = rec["id"]
    i = 2
    while rec["id"] in used_ids:
        rec["id"] = f"{base}-{i}"; i += 1
    used_ids.add(rec["id"])
    notes = rec.get("notes") or ""
    rec["note_has_conditions"] = bool(COND_RX.search(notes))
    out.append(rec)

def prov(fname, idx, check="matched live", extra=None):
    p = {"source": f"sources/aafdid-capture/{fname}", "row": idx, "captured": CAPTURED, "checked": CHECKED, "check": check}
    if extra:
        p.update(extra)
    return p

def cond_in(field, vals):
    return {"field": field, "in": list(vals)}

MCA_TYPES = {"mdap": "mdap", "acat_ii": "acat_ii", "acat_iii_or_below": "acat_iii", "mais": "mais"}
MCA_EVENTS = [e["id"] for e in PW["mca"]["events"]]

# ---------------------------------------------------------------- MCA milestone and phase
d = load(CAP / "mca_milestone_phase.json")
fixes = {c["match_name"]: c for c in corrections_for("mca_milestone_phase.json") if "match_name" in c}
for i, r in enumerate(d["rows"], 1):
    types = [MCA_TYPES[t] for t in r["program_types"]]
    check = "matched live"
    if r["name"] in fixes:
        for t in fixes[r["name"]]["set"].get("add_program_types", []):
            if t not in types:
                types.append(t)
        check = "corrected: added ACAT IAM/IAC (MAIS), shown on the live page"
    order = ["mdap", "mais", "acat_ii", "acat_iii"]
    types = [t for t in order if t in types]
    when = [{"event": e, "submission": r["events"][e]} for e in MCA_EVENTS if e in r["events"]]
    cond = cond_in("mca_program_type", types)
    basis = "AAFDID program type and lifecycle event marks"
    name = r["name"]
    if re.search(r"CLINGER", name, re.I):
        cond = {"all": [cond, cond_in("it_type", ["it_system", "embedded_it"])]}
        basis = "AAFDID marks, plus the CCA table notes: CCA applies to programs that acquire IT, including national security systems"
    add({
        "id": f"mca.ms.{slug(name)}", "code": f"MCA-M{i:02d}", "pathways": ["mca"], "table": "ms",
        "name": name, "kind": "event", "type": norm_type(r["type_raw"]), "type_text": r["type_raw"],
        "source": r["source_raw"], "approval": r.get("approval_authority") or "", "when": when,
        "applies_if": cond, "rule_basis": basis, "notes": clean_notes(r.get("notes")),
        "provenance": prov("mca_milestone_phase.json", i, check),
    })

# ---------------------------------------------------------------- MCA recurring and exceptions
for fname, table, prefix, kind in [("mca_recurring.json", "rec", "MCA-R", "recurring"), ("mca_exceptions.json", "exc", "MCA-X", "triggered")]:
    d = load(CAP / fname)
    for i, r in enumerate(d["rows"], 1):
        c = r["columns"]
        types = [MCA_TYPES[k] for k in ("mdap", "acat_ii", "acat_iii_or_below") if k in r.get("marks", {})]
        add({
            "id": f"mca.{table}.{slug(r['name'])}", "code": f"{prefix}{i:02d}", "pathways": ["mca"], "table": table,
            "name": r["name"], "kind": kind, "type": norm_type(c.get("type")), "type_text": c.get("type") or "",
            "source": c.get("source") or "", "approval": "", "procedure": c.get("procedure") or "",
            "when": [], "due_text": re.sub(r"\s+", " ", c.get("due") or "").strip(),
            "applies_if": cond_in("mca_program_type", types), "rule_basis": "AAFDID ACAT marks",
            "notes": clean_notes(r.get("notes")), "provenance": prov(fname, i),
        })

# ---------------------------------------------------------------- MCA CCA compliance
cfix = corrections_for("mca_cca.json")[0]
fn_text = cfix["footnote_text"]
d = load(CAP / "mca_cca.json")
for i, r in enumerate(d["rows"], 1):
    fx = next(x for x in cfix["rows"] if x["index"] == i)
    fns = fx["footnotes"]
    doc = fx.get("documentation") or re.sub(r"\s+", " ", r["columns"].get("documentation") or "").strip()
    if 3 in fns:
        cond = {"field": "it_type", "eq": "it_system"}
        when_txt = "IT systems, including national security systems. Presumed satisfied for weapon systems with embedded IT and for command and control systems that are not themselves IT (AAFDID footnote 3)."
    else:
        cond = cond_in("it_type", ["it_system", "embedded_it"])
        when_txt = "Programs that acquire IT, including national security systems and IT embedded in weapon systems."
    add({
        "id": f"mca.cca.action-{i:02d}", "code": f"MCA-C{i:02d}", "pathways": ["mca"], "table": "cca",
        "name": f"CCA action {i}: {fx['action']}", "kind": "compliance", "type": "statutory", "type_text": "Clinger-Cohen Act (40 U.S.C. Subtitle III)",
        "source": "Clinger-Cohen Act, 40 U.S.C. Subtitle III; DoDI 5000.82", "approval": "",
        "when": [], "due_text": "Report compliance at the events in the CLINGER-COHEN ACT (CCA) COMPLIANCE row of the milestone table.",
        "applies_if": cond, "applies_when": when_txt, "rule_basis": "AAFDID CCA table and its footnotes",
        "notes": f"Evidenced by: {doc}.", "footnotes": [fn_text[str(n)] for n in fns],
        "provenance": prov("mca_cca.json", i, "corrected: footnotes and full action text taken from the live page"),
    })

# ---------------------------------------------------------------- MCA cost data reporting (CSDR)
d = load(CAP / "mca_csdr.json")
ACAT_I_II = cond_in("mca_program_type", ["mdap", "acat_ii"])
csdr_rules = {
    "mca.csdr.contractor-business-data-report": ("conditional", ACAT_I_II, None, "ACAT I and II programs whose contractor business unit holds CSDR contracts expected to exceed $250M (then-year)."),
    "mca.csdr.contractor-cost-data-report": ("contract", {"all": [ACAT_I_II, {"field": "contract_value", "gt": 50000000}]},
                                              {"all": [ACAT_I_II, {"field": "contract_value", "gt": 20000000}, {"field": "contract_value", "lte": 50000000}]},
                                              "ACAT I and II programs: contracts over $50M (then-year). Between $20M and $50M, at the CSDR plan authority's discretion for high-risk, high-interest or software contracts."),
    "mca.csdr.maintenance-and-repair-parts-data-report": ("conditional", {"all": [ACAT_I_II, {"field": "contract_value", "gt": 50000000}]}, None, "Sustainment contracts over $50M for ACAT I and II programs, when the PM cannot provide equivalent data, at the CSDR plan authority's discretion."),
    "mca.csdr.program-resource-distribution-table": ("contract", {"all": [ACAT_I_II, {"field": "contract_value", "gt": 50000000}]},
                                                      {"all": [ACAT_I_II, {"field": "contract_value", "gt": 20000000}, {"field": "contract_value", "lte": 50000000}]},
                                                      "ACAT I and II programs: contracts over $50M (then-year). Between $20M and $50M, at the CSDR plan authority's discretion."),
    "mca.csdr.software-resources-data-report": ("conditional", {"all": [ACAT_I_II, {"field": "contract_value", "gt": 20000000}]}, None, "Software development or production efforts over $20M (then-year) for ACAT I and II programs."),
    "mca.csdr.technical-data-report": ("conditional", {"all": [ACAT_I_II, {"field": "contract_value", "gt": 50000000}]}, None, "Contracts over $50M for ACAT I and II programs, when the PM cannot provide equivalent data, at the CSDR plan authority's discretion."),
}
for i, r in enumerate(d["rows"], 1):
    kind, cond, cond2, when_txt = csdr_rules[r["id"]]
    wr = r["when_required"]
    notes = wr if isinstance(wr, str) else " ".join(f"{k.replace('_', ' ').capitalize()}: {v}" for k, v in wr.items())
    rec = {
        "id": r["id"], "code": f"MCA-D{i:02d}", "pathways": ["mca"], "table": "csdr", "name": r["name"],
        "kind": kind, "type": "regulatory", "type_text": "DoDI 5000.73", "source": "DoDI 5000.73", "approval": "CSDR plan approval authority",
        "when": [], "due_text": "Per the approved CSDR plan.", "applies_if": cond, "applies_when": when_txt,
        "rule_basis": "AAFDID CSDR thresholds (then-year dollars)", "notes": clean_notes(notes), "provenance": prov("mca_csdr.json", i),
    }
    if cond2:
        rec["conditional_if"] = cond2
    add(rec)

# ---------------------------------------------------------------- APB rules (reference) and breach definitions (triggered)
d = load(CAP / "mca_apb.json")
for i, r in enumerate(d["rows"], 1):
    cond = cond_in("mca_program_type", ["mdap"]) if "subprogram" in r["id"] else cond_in("mca_program_type", ["mdap", "acat_ii", "acat_iii"])
    add({
        "id": r["id"], "code": f"MCA-B{i:02d}", "pathways": ["mca"], "table": "apb", "name": f"APB rule: {r['name']}",
        "kind": "reference", "type": "unspecified", "type_text": "", "source": r.get("source") or "DoDI 5000.85", "approval": "MDA",
        "when": [], "applies_if": cond, "rule_basis": "AAFDID Acquisition Program Baselines page", "notes": clean_notes(r["definition"]),
        "provenance": prov("mca_apb.json", i),
    })
d = load(CAP / "mca_breach.json")
for i, r in enumerate(d["rows"], 1):
    add({
        "id": r["id"], "code": f"MCA-N{i:02d}", "pathways": ["mca"], "table": "brch", "name": r["name"],
        "kind": "triggered", "type": "statutory", "type_text": "Statutory", "source": r["source"], "approval": "",
        "when": [], "due_text": "When the breach occurs.", "applies_if": cond_in("mca_program_type", ["mdap"]),
        "rule_basis": "AAFDID Statutory Program Breach Definitions (MDAPs)", "notes": clean_notes(r["definition"]),
        "provenance": prov("mca_breach.json", i),
    })

# ---------------------------------------------------------------- EVMS (all hardware and software pathways)
EVM_PW = ["mca", "mta", "uca", "swa", "dbs"]
COST = {"field": "contract_cost_type", "eq": True}
d = load(CAP / "mca_evms_application.json")
evm_app = [
    ("conditional", {"all": [COST, {"field": "contract_value", "lt": 20000000}]}),
    ("contract", {"all": [COST, {"field": "contract_value", "gte": 20000000}, {"field": "contract_value", "lt": 100000000}]}),
    ("contract", {"all": [COST, {"field": "contract_value", "gte": 100000000}]}),
]
for i, r in enumerate(d["rows"], 1):
    c = r["columns"]
    kind, cond = evm_app[i - 1]
    add({
        "id": f"evm.application.{slug(c['contract_value'])}", "code": f"EVM-0{i}", "pathways": EVM_PW, "table": "evm",
        "name": f"EVMS on contract, {c['contract_value']}: {c['applicability']}", "kind": kind, "type": "regulatory",
        "type_text": "FAR/DFARS and DoDI 5000.85", "source": re.sub(r"\s+", " ", c["source"]).strip(), "approval": "",
        "when": [], "applies_if": cond,
        "applies_when": f"Cost-reimbursable or incentive contract of 18 months or more, valued {c['contract_value']} (then-year dollars, including options).",
        "rule_basis": "AAFDID EVMS Application table; AAFDID notes that EVM is not specific to any one pathway",
        "notes": clean_notes(c.get("notes")), "provenance": prov("mca_evms_application.json", i),
    })
d = load(CAP / "mca_evms_reporting.json")
evm_rep = [
    ("conditional", {"field": "contract_value", "lt": 20000000}, "Contracts under $20M: not required. The PMO may request IPMDAR cost or schedule reporting."),
    ("contract", {"all": [COST, {"field": "contract_value", "gte": 20000000}, {"field": "contract_value", "lt": 100000000}]}, "Monthly when an EVMS requirement is on contract ($20M to under $100M)."),
    ("contract", {"all": [COST, {"field": "contract_value", "gte": 100000000}]}, "Monthly when an EVMS requirement is on contract ($100M or more)."),
]
for i, r in enumerate(d["rows"], 1):
    kind, cond, when_txt = evm_rep[i - 1]
    add({
        "id": f"evm.reporting.{slug(r['contract_value'])}", "code": f"EVM-0{i + 3}", "pathways": EVM_PW, "table": "evm",
        "name": f"IPMDAR (DI-MGMT-81861), {r['contract_value']}: {r['applicability']}", "kind": kind, "type": "regulatory",
        "type_text": "DoDI 5000.85; DI-MGMT-81861", "source": r["source"], "approval": "", "when": [],
        "due_text": "Monthly" if i > 1 else "", "applies_if": cond, "applies_when": when_txt,
        "rule_basis": "AAFDID EVMS Reporting table", "notes": clean_notes(r.get("notes")), "provenance": prov("mca_evms_reporting.json", i),
    })

# ---------------------------------------------------------------- MTA: Table 1 submissions to OSD
pfix = corrections_for("mta_program_info.json")[0]
d = load(CAP / "mta_program_info.json")
DUE = {"At MTA Program Entrance": "entrance", "Throughout MTA Program Execution": "execution", "At MTA Program Exit": "exit"}
n = 0
for i, r in enumerate(d["rows"], 1):
    c = r["columns"]
    if c["name"] == pfix["drop_name"]:
        continue
    n += 1
    sizes = [s for s in ("non_major", "major", "exceeds_mdap") if (c.get(s) or "").strip().lower() == "x"]
    name = re.sub(r"\s+", " ", c["name"]).strip()
    foot = []
    for rf in pfix["rows"]:
        if name.startswith(rf["match_prefix"]):
            name = rf.get("name", name)
            foot = [pfix["footnote_text"][str(k)] for k in rf["footnotes"]]
    cond = cond_in("mta_size", sizes)
    kind, basis, extra = "event", "AAFDID Table 1 marks (non-major, major, exceeds MDAP threshold)", {}
    if name.startswith("Lifecycle Sustainment Plan"):
        cond = {"all": [cond, {"field": "mta_path", "eq": "rf"}]}
        extra["conditional_if"] = {"all": [cond_in("mta_size", sizes), {"field": "mta_path", "eq": "rp"}]}
        basis = "AAFDID marks major systems and above without splitting paths; DoDI 5000.80 Table 1 lists the lifecycle sustainment plan for Rapid Fielding"
    rec = {
        "id": f"mta.osd.{slug(name)}", "code": f"MTA-O{n:02d}", "pathways": ["mta"], "table": "osd", "name": name,
        "kind": kind, "type": "regulatory", "type_text": "Regulatory", "source": c.get("source") or "", "approval": "",
        "when": [{"event": DUE[c["due"]], "submission": "initial"}], "applies_if": cond, "rule_basis": basis,
        "notes": "", "footnotes": foot,
        "provenance": prov("mta_program_info.json", i, "corrected: TYPE column (Regulatory) and footnotes taken from the live page"),
    }
    rec.update(extra)
    add(rec)

# ---------------------------------------------------------------- MTA: statutory and regulatory requirements that may be applicable
mfix = {c["match_name"]: c for c in corrections_for("mta.json")}
d = load(CAP / "mta.json")
for i, r in enumerate(d["rows"], 1):
    c = r["columns"]
    marks = r.get("marks", {})
    sizes = []
    if "non_major" in marks:
        sizes.append("non_major")
    if "major" in marks:
        sizes += ["major", "exceeds_mdap"]
    notes = clean_notes(r.get("notes"))
    check = "matched live"
    if r["name"] in mfix:
        notes = (notes + " " + mfix[r["name"]]["set"]["note_addendum"]).strip()
        check = "matched live; note addendum from the live page"
    if sizes:
        cond, basis = cond_in("mta_size", sizes), "AAFDID major and non-major system marks"
    else:
        cond, basis = {"field": "international", "eq": True}, "AAFDID marks neither column; this tool applies it when international partners are involved"
    add({
        "id": f"mta.sr.{slug(r['name'])}", "code": f"MTA-S{i:02d}", "pathways": ["mta"], "table": "sr", "name": r["name"],
        "kind": "conditional", "type": norm_type(c.get("type")), "type_text": c.get("type") or "", "source": c.get("source") or "",
        "approval": c.get("approval") or "", "when": [], "applies_if": cond, "rule_basis": basis,
        "applies_when_suffix": "AAFDID lists this among requirements that may be applicable; check the note, and the decision authority decides regulatory items.",
        "notes": notes, "provenance": prov("mta.json", i, check),
    })

# ---------------------------------------------------------------- UCA unique requirements
d = load(CAP / "uca.json")
for i, r in enumerate(d["rows"], 1):
    c = r["columns"]; marks = r.get("marks", {})
    acats = [a for a, k in (("acat_ii", "acat_ii"), ("acat_iii", "acat_iii_or_below")) if k in marks]
    when = [{"event": e, "submission": "initial"} for e in ("development", "production", "other") if e in marks]
    add({
        "id": f"uca.ir.{slug(r['name'])}", "code": f"UCA-{i:02d}", "pathways": ["uca"], "table": "ir", "name": r["name"],
        "kind": "event", "type": norm_type(c.get("type")), "type_text": c.get("type") or "", "source": c.get("source") or "",
        "approval": "", "when": when, "applies_if": cond_in("uca_acat", acats), "rule_basis": "AAFDID ACAT and event marks",
        "notes": clean_notes(r.get("notes")), "provenance": prov("uca.json", i),
    })

# ---------------------------------------------------------------- SWA requirements
SWA_EV = {"Entering the Planning Phase": "planning", "Entering the Execution Phase": "execution_entry",
          "During the Execution Phase": "execution", "Each Decision Point": "each_decision"}
d = load(CAP / "swa.json")
rows = [dict(r) for r in d["rows"]]
sfix = corrections_for("swa.json")
for fx in sfix:
    if "insert_after_name" in fx:
        k = next(j for j, r in enumerate(rows) if r["columns"]["name"] == fx["insert_after_name"])
        rows.insert(k + 1, {"name": fx["insert"]["name"], "columns": dict(fx["insert"]), "notes": "", "_inserted": True})
for fx in sfix:
    if "match_name" in fx:
        for r in rows:
            if r["columns"]["name"] == fx["match_name"]:
                r["columns"] = {**r["columns"], **fx["set"]}; r["_corrected"] = True
ABOVE = {"field": "swa_above_acat_ii", "eq": True}
for i, r in enumerate(rows, 1):
    c = r["columns"]; name = c["name"]; t = c.get("type") or ""
    rec = {
        "id": f"swa.ir.{slug(name)}", "code": f"SWA-{i:02d}", "pathways": ["swa"], "table": "ir", "name": name,
        "kind": "event", "type": norm_type(t), "type_text": t, "source": c.get("source") or "", "approval": "",
        "when": [{"event": SWA_EV[c["execution_phase"]], "submission": "initial"}], "applies_if": {"const": True},
        "rule_basis": "AAFDID lists it for software pathway programs", "notes": clean_notes(r.get("notes")),
        "provenance": ({"source": "sources/corrections-2026-09-30.json", "captured": "live page", "checked": CHECKED, "check": "added: row missing from the capture"}
                       if r.get("_inserted") else prov("swa.json", i, "corrected from the live page" if r.get("_corrected") else "matched live")),
    }
    tl = t.lower()
    if "major programs (> acat ii)" in tl or "programs (> acat ii)" in tl:
        rec["type_rule"] = {"if": ABOVE, "then": "statutory", "else": "regulatory"}
    elif "mission critical and mission essential" in tl:
        rec["type_rule"] = {"if": {"field": "mission_critical_it", "eq": True}, "then": "statutory", "else": "regulatory"}
    elif "cape ice" in tl:
        rec["type"] = "regulatory"
        rec["approval"] = "CAPE prepares the ICE above ACAT II unless it delegates"
    elif "software maintenance" in tl:
        rec["type"] = "statutory"; rec["applies_if"] = {"field": "software_maintenance", "eq": True}
        rec["rule_basis"] = "AAFDID TYPE: statutory for programs with software maintenance"
    elif "dot&e oversight list" in tl and "statutory" in tl:
        rec["type"] = "statutory"; rec["applies_if"] = {"field": "dote_oversight", "eq": True}
        rec["rule_basis"] = "AAFDID TYPE: statutory for programs on the DOT&E oversight list"
    elif "may require a tem" in tl:
        rec["type"] = "regulatory"
    m = re.search(r"\((CTRs with \$250M|\$100M\+ contracts|\$100M\+ Programs)\)", name)
    if m:
        rec["kind"] = "contract"
        if m.group(1) == "$100M+ contracts":
            rec["applies_if"] = {"field": "contract_value", "gte": 100000000}
            rec["applies_when"] = "Contracts of $100M or more."
            rec["rule_basis"] = "Threshold in AAFDID's row name"
        else:
            rec["kind"] = "conditional"
            rec["applies_when"] = ("Contractors with $250M or more in CSDR contracts (threshold in AAFDID's row name)."
                                   if m.group(1).startswith("CTRs") else
                                   "Programs of $100M or more (threshold in AAFDID's row name).")
            rec["rule_basis"] = "Threshold in AAFDID's row name; this tool does not ask for program value"
    add(rec)

d = load(CAP / "swa_cca.json")
scfix = corrections_for("swa_cca.json")
for i, r in enumerate(d["rows"], 1):
    act = re.sub(r"\s+", " ", r["columns"]["action"]).strip()
    for fx in scfix:
        if act.startswith(fx["match_prefix"]):
            act = fx["set"]["action"]
    add({
        "id": f"swa.cca.{slug(act, 40)}", "code": f"SWA-C{i:02d}", "pathways": ["swa"], "table": "cca", "name": f"CCA: {act}",
        "kind": "compliance", "type": "statutory", "type_text": "Clinger-Cohen Act (40 U.S.C. Subtitle III)",
        "source": "Clinger-Cohen Act, 40 U.S.C. Subtitle III; DoDI 5000.82", "approval": "", "when": [],
        "due_text": "Report with the CCA compliance entries in the SWA table.",
        "applies_if": {"const": True}, "rule_basis": "AAFDID SWA CCA table",
        "notes": "Evidenced by: " + re.sub(r"\s+", " ", r["columns"].get("documentation") or "").strip() + ".",
        "provenance": prov("swa_cca.json", i),
    })

# ---------------------------------------------------------------- DBS statutory requirements
DBS_EV = {e["name"].split(" (")[0].lower(): e["id"] for e in PW["dbs"]["events"]}
DBS_EV.update({"limited deployment atp(s)": "limited_deployment_atp", "contract award": "contract_award"})
dfix = corrections_for("dbs.json")
d = load(CAP / "dbs.json")
n = 0
for i, r in enumerate(d["rows"], 1):
    c = dict(r["columns"])
    if any(fx.get("drop_name") == c["name"] for fx in dfix):
        continue
    n += 1
    check = "matched live"
    for fx in dfix:
        if fx.get("match_name") == c["name"]:
            c.update(fx["set"]); check = "corrected from the live page"
    name = re.sub(r"\s+", " ", c["name"]).strip()
    name = re.sub(r"Limited Deployment 3 ATP", "Limited Deployment ATP", name)
    ev = DBS_EV[c["decision_point"].strip().lower()]
    cond, basis = {"const": True}, "AAFDID lists it for defense business systems"
    special_when = None
    if name.startswith("Confirmation of CCA compliance Initial Operational"):
        name = name.replace("Confirmation of CCA compliance Initial", "Confirmation of CCA compliance; Initial")
        special_when = "For every defense business system. The IOT&E report part applies to business systems on the DOT&E oversight list."
        basis = "AAFDID puts two items in one cell: CCA confirmation for all DBS, and the IOT&E report for oversight programs"
    elif "mission essential and mission critical" in name.lower():
        cond, basis = {"field": "mission_critical_it", "eq": True}, "AAFDID row name: for mission-essential and mission-critical IT"
    elif "dot&e oversight" in name.lower():
        cond, basis = {"field": "dote_oversight", "eq": True}, "AAFDID row name: for programs on the DOT&E oversight list"
    foot = []
    if name.startswith("CMO Certification"):
        foot = d["table_notes"][:2]
    if "CCA" in name or "Clinger" in name:
        foot = [d["table_notes"][2]]
    add({
        "id": f"dbs.sr.{slug(name)}", "code": f"DBS-{n:02d}", "pathways": ["dbs"], "table": "sr", "name": name,
        "kind": "event", "type": norm_type(c.get("type")), "type_text": c.get("type") or "", "source": re.sub(r"\s+", " ", c.get("source") or "").strip(),
        "approval": "", "when": [{"event": ev, "submission": "initial"}], "phase": c.get("execution_phase"),
        "applies_if": cond, "rule_basis": basis, "notes": "", "footnotes": foot, "provenance": prov("dbs.json", i, check),
        **({"applies_when": special_when} if special_when else {}),
    })

# ---------------------------------------------------------------- AoS from DoDI 5000.74
for i, r in enumerate(aos["requirements"], 1):
    ap = r["applies"]
    cond = {"const": True} if ap == "all" else ap
    rec = {
        "id": f"aos.dodi.{slug(r['name'])}", "code": f"AOS-{i:02d}", "pathways": ["aos"], "table": "dodi", "name": r["name"],
        "kind": r.get("kind", "event"), "type": norm_type(r["type"]), "type_text": r["type"], "source": r["source"],
        "approval": r.get("approval") or "", "when": [{"event": r["event"], "submission": "initial"}] if r.get("kind") != "triggered" else [],
        "applies_if": cond, "rule_basis": "DoDI 5000.74 (AAFDID has no AoS table)", "notes": r.get("note") or "",
        "provenance": {"source": "sources/aos-dodi-5000-74.json", "row": i, "captured": "DoDI 5000.74 Change 1 (2021-06-24)", "checked": CHECKED, "check": "drawn from the DoDI; not an AAFDID row"},
    }
    if r.get("applies_when"):
        rec["applies_when"] = r["applies_when"]
    if r.get("kind") == "triggered":
        rec["due_text"] = r.get("applies_when", "")
    add(rec)

# ---------------------------------------------------------------- plain-English applicability
NOUNS = {
    "mca_program_type": {"mdap": "MDAPs", "mais": "MAIS (legacy)", "acat_ii": "ACAT II", "acat_iii": "ACAT III and below"},
    "uca_acat": {"acat_ii": "ACAT II", "acat_iii": "ACAT III and below"},
    "mta_size": {"non_major": "non-major systems", "major": "major systems", "exceeds_mdap": "programs above MDAP thresholds"},
    "mta_path": {"rp": "Rapid Prototyping", "rf": "Rapid Fielding"},
    "it_type": {"it_system": "IT systems (including national security systems)", "embedded_it": "weapon or C2 systems with embedded IT", "none": "systems with no IT"},
    "svc_vehicle": {"standalone": "a standalone contract", "idiq_base": "a multiple-award IDIQ base award", "task_order": "a task order"},
}
ALL_WORD = {"mca_program_type": "all MCA program types", "uca_acat": "all UCA programs", "mta_size": "all MTA programs",
            "mta_path": "both MTA paths", "it_type": "all systems"}
BOOL_PHRASE = {
    "international": ("international partners are involved", "no international partners are involved"),
    "swa_above_acat_ii": ("cost exceeds the ACAT II thresholds", "cost is at or below the ACAT II thresholds"),
    "mission_critical_it": ("it is mission-critical or mission-essential IT", "it is not mission-critical or mission-essential IT"),
    "dote_oversight": ("it is on the DOT&E oversight list", "it is not on the DOT&E oversight list"),
    "software_maintenance": ("it needs government software maintenance", "it needs no government software maintenance"),
    "contract_cost_type": ("the contract is cost-reimbursable or incentive-type, 18 months or more", "the contract is fixed-price or shorter than 18 months"),
    "svc_special_interest": ("it is designated Special Interest", "it is not designated Special Interest"),
    "svc_overlap": ("it may overlap an existing vehicle", "it does not overlap an existing vehicle"),
    "svc_sensitive_functions": ("contractors perform critical or closely associated functions", "contractors perform no critical or closely associated functions"),
}
NAME = {"contract_value": "the largest contract value", "svc_total_value": "the total estimated value", "svc_annual_value": "the highest single-year value"}
def money(v):
    if v >= 1e9: return f"${v/1e9:g}B"
    if v >= 1e6: return f"${v/1e6:g}M"
    return f"${v:,.0f}"
def join_and(xs):
    xs = list(xs)
    return xs[0] if len(xs) == 1 else ", ".join(xs[:-1]) + " and " + xs[-1]
def join_or(xs):
    xs = list(xs)
    return xs[0] if len(xs) == 1 else ", ".join(xs[:-1]) + " or " + xs[-1]
def phrase(c):
    if "const" in c:
        return "for every program on this pathway"
    if "all" in c:
        return "; ".join(phrase(x) for x in c["all"])
    if "any" in c:
        return "either " + " or ".join(phrase(x) for x in c["any"])
    if "not" in c:
        return "unless " + phrase(c["not"])
    f = c["field"]
    if "eq" in c and isinstance(c["eq"], bool):
        return "when " + BOOL_PHRASE[f][0 if c["eq"] else 1]
    if "eq" in c or "in" in c:
        vals = [c["eq"]] if "eq" in c else c["in"]
        nouns = NOUNS.get(f, {})
        if f in ALL_WORD and len(vals) == len(nouns) and nouns:
            return "for " + ALL_WORD[f]
        if f == "mta_path":
            return join_or(nouns[v] for v in vals) + " only"
        if f == "svc_vehicle":
            return "when bought as " + join_or(nouns[v] for v in vals)
        return "for " + join_and(nouns.get(v, str(v)) for v in vals)
    for op, w in (("gte", "is at least"), ("gt", "is over"), ("lt", "is under"), ("lte", "is at most")):
        if op in c:
            return f"when {NAME.get(f, f)} {w} {money(c[op])}"
    raise ValueError(c)
for r in out:
    if not r.get("applies_when"):
        s = phrase(r["applies_if"])
        r["applies_when"] = s[0].upper() + s[1:] + "."
    r.pop("applies_when_suffix", None)

# ---------------------------------------------------------------- currency notes
def fields_in(c, acc):
    if not isinstance(c, dict): return acc
    for k in ("all", "any"):
        for x in c.get(k, []): fields_in(x, acc)
    if "not" in c: fields_in(c["not"], acc)
    if "field" in c: acc.add(c["field"])
    return acc
for note in currency["notes"]:
    at = note.get("attach", {})
    for r in out:
        hit = r["code"] in at.get("codes", []) or r["table"] in at.get("tables", [])
        if at.get("match") and set(r["pathways"]) & set(at.get("pathways", [])):
            if re.search(at["match"], r["name"] + " " + (r.get("notes") or "")):
                hit = True
        if hit:
            r.setdefault("currency", []).append(note["id"])

# ---------------------------------------------------------------- questions: which requirements each one gates
for q in questions["questions"]:
    q["gates"] = sorted({r["code"] for r in out if q["id"] in fields_in(r["applies_if"], set()) | fields_in(r.get("conditional_if", {}), set()) | fields_in((r.get("type_rule") or {}).get("if", {}), set())})

for r in out:
    t = TABLES.get((r["pathways"][0], r["table"])) or TABLES.get(("any", r["table"]))
    r["table_name"] = t["name"]
    r["url"] = t["url"]

# ---------------------------------------------------------------- write
counts = {}
for r in out:
    for p in r["pathways"]:
        counts.setdefault(p, {}); counts[p][r["kind"]] = counts[p].get(r["kind"], 0) + 1
meta = {
    "name": "AAFDID Navigator rules", "version": VERSION, "built": datetime.date.today().isoformat(),
    "aafdid_capture": f"{CAPTURED} (browser print-to-PDF of every AAFDID table page, parsed in the aafdid-open project)",
    "live_check": f"{CHECKED}: every captured row located on the live AAFDID pages; differences corrected (sources/corrections-2026-09-30.json)",
    "aos_source": "DoDI 5000.74, Change 1 (2021-06-24); AAFDID has no AoS table",
    "requirements": len(out), "by_pathway_and_kind": counts,
    "disclaimer": "Unofficial. AAFDID is itself an overview: comply with its tabular notes and the full text of each cited source. Not affiliated with or endorsed by WARU, DAU or the Department of War.",
}
(RULES / "requirements.json").write_text(json.dumps({"schema": "aafdid-navigator/requirements@1", "requirements": out}, indent=1, ensure_ascii=False) + "\n")
(RULES / "questions.json").write_text(json.dumps(questions, indent=2, ensure_ascii=False) + "\n")
(RULES / "meta.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False) + "\n")
bundle = {"schema": "aafdid-navigator/bundle@1", "meta": meta, "pathways": pathways["pathways"], "finder": pathways["finder"],
          "questions": questions, "currency": currency, "scat": aos["scat"], "scat_cite": aos["scat_cite"], "requirements": out}
(RULES / "aafdid-rules.json").write_text(json.dumps(bundle, ensure_ascii=False, separators=(",", ":")) + "\n")
print(f"{len(out)} requirements")
for p, c in counts.items():
    print(f"  {p}: {sum(c.values())}  {c}")
