# Rules reference

`rules/aafdid-rules.json` is the single file that the web page, both engines and the agent pack read. `tools/build_rules.py` builds it from the hand-written files in `rules/` and the sources in `sources/`.

## Bundle

| Key | What it holds |
| --- | --- |
| `meta` | Version, build date, capture and live-check dates, record count, disclaimer |
| `pathways` | Six pathways with events (in order), tables, decision authority, notes, links; UCA's `also_review` |
| `finder` | The pathway-finder questions (`steps`) with yes/no branches and cites |
| `questions` | The intake questions, with `show_if` and the requirement codes each one `gates` |
| `currency` | Changes since AAFDID's tables, each with sources and what it attaches to |
| `scat`, `scat_cite` | Services categories for AoS |
| `requirements` | 268 requirement records |

## Profile fields

| Field | Type | Asked for | Values |
| --- | --- | --- | --- |
| `pathway` | choice | all | `mca` `mta` `uca` `swa` `dbs` `aos` |
| `event` | event | all | an event `id` from the pathway, or blank for all events |
| `mca_program_type` | choice | MCA | `mdap` `mais` `acat_ii` `acat_iii` |
| `uca_acat` | choice | UCA | `acat_ii` `acat_iii` |
| `mta_path` | choice | MTA | `rp` `rf` |
| `mta_size` | choice | MTA | `non_major` `major` `exceeds_mdap` |
| `international` | boolean | MTA | |
| `swa_above_acat_ii` | boolean | SWA | |
| `mission_critical_it` | boolean | SWA, DBS | |
| `dote_oversight` | boolean | SWA, DBS | |
| `software_maintenance` | boolean | SWA | |
| `it_type` | choice | MCA, UCA | `it_system` `embedded_it` `none` |
| `contract_value` | money | MCA, MTA, UCA, SWA, DBS | then-year dollars, including options |
| `contract_cost_type` | boolean | MCA, MTA, UCA, SWA, DBS | cost-reimbursable or incentive, 18 months or more |
| `svc_total_value` | money | AoS | IGCE, current-year dollars |
| `svc_annual_value` | money | AoS | highest single year |
| `svc_special_interest` | boolean | AoS | |
| `svc_vehicle` | choice | AoS | `standalone` `idiq_base` `task_order` |
| `svc_overlap` | boolean | AoS | |
| `svc_sensitive_functions` | boolean | AoS | |

A missing field is unknown. The engines accept these input forms:

- `yes`/`no`, `y`/`n` and `true`/`false`
- money such as `45M`, `$1.2B` or `45000000`
- option values or option labels
- event ids, short names such as `MS B`, or full names

## Requirement record

| Field | Meaning |
| --- | --- |
| `id` | Stable identifier, `<pathway>.<table>.<slug>` |
| `code` | Short code for people and agents, such as `MCA-M06`; tied to the release |
| `pathways` | Pathways the record belongs to (the EVMS rows list five) |
| `table`, `table_name`, `url` | The AAFDID table (or DoDI) it came from |
| `name`, `type_text`, `source`, `approval`, `procedure`, `notes`, `footnotes` | AAFDID's own words |
| `kind` | `event`, `recurring`, `contract`, `compliance`, `conditional`, `triggered`, `reference` |
| `type` | `statutory`, `regulatory`, `both`, `unspecified` |
| `type_rule` | Optional: `{"if": condition, "then": type, "else": type}` for SWA rows whose type depends on the program |
| `when` | `[{event, submission: initial or update}]` |
| `due_text` | Due wording for rows without event marks |
| `applies_if` | Condition (below) |
| `conditional_if` | Optional second condition that makes the row "may apply" when `applies_if` is false |
| `applies_when` | Plain-English form of the condition |
| `rule_basis` | Why the condition is what it is: AAFDID marks, or the note or row name it comes from |
| `currency` | Ids of `currency` notes attached to the record |
| `note_has_conditions` | True when the AAFDID note contains conditional wording |
| `provenance` | Capture file and row, capture date, live-check date and result |

## Conditions

```
{"const": true}
{"field": "mta_size", "in": ["major", "exceeds_mdap"]}
{"field": "dote_oversight", "eq": true}
{"field": "contract_value", "gte": 20000000}          also gt, lt, lte, ne
{"all": [ ... ]}   {"any": [ ... ]}   {"not": { ... }}
```

Evaluation is three-valued (Kleene logic). A test on a missing field is unknown:

- `all` is false if any part is false, otherwise unknown if any part is unknown, otherwise true.
- `any` is true if any part is true, otherwise unknown if any part is unknown, otherwise false.

## Status and grouping

| Result of `applies_if` | Status |
| --- | --- |
| true | from `kind`: event, recurring, contract and compliance become **required**; conditional becomes **conditional**; triggered becomes **triggered**; reference becomes **reference** |
| unknown | **undetermined**, with the missing fields and their questions |
| false, with `conditional_if` true | **conditional** |
| false | **not_applicable**, with `applies_when` as the reason |

Required items are grouped against the profile's `event`:

- `at_focus`: due at the next event.
- `later`: due at an event after it.
- `earlier`: all of its events come before the next one.
- `ongoing`: no event.
- `as_required`: only the unordered "Other" event.
- `by_event`: no next event was given.

UCA programs also get **review** items. These are the MCA milestone and exceptions rows for the program's ACAT level, because AAFDID's UCA page says to use them.

## Changing the rules

- A row changed on AAFDID: add an entry to a corrections file in `sources/`, and teach `tools/build_rules.py` to apply it. Keep the capture files unchanged.
- A new change since AAFDID: add a note to `rules/currency.json` with its sources and `attach` targets.
- A new question: add it to `rules/questions.json` with `show_if` and `why`, and use its `id` as a field in conditions.
- Then run `tools/build_all.sh`, review `tests/run_tests.py --update` output, and commit rules, snapshots, web page and agent pack together.
