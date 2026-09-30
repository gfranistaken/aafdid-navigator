# Rules reference

`rules/aafdid-rules.json` is the single file that the web page, both engines and the agent pack read. `tools/build_rules.py` builds it from the hand-written files in `rules/` and the sources in `sources/`.

## Bundle

| Key | What it holds |
| --- | --- |
| `meta` | Version, rules date, capture and live-check dates, record count, disclaimer |
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
| `swa_above_acat_ii` | boolean | SWA | |
| `mission_critical_it` | boolean | SWA, DBS | |
| `dote_oversight` | boolean | MCA, UCA, SWA, DBS | |
| `software_maintenance` | boolean | SWA | |
| `it_type` | choice | MCA, UCA | `it_system` `embedded_it` `none` |
| `contract_value` | money | MCA, MTA, UCA, SWA, DBS | range of the largest contract, then-year dollars, including options: `under_20m` `20m_to_50m` `50m_to_100m` `100m_plus` |
| `contract_cost_type` | boolean | MCA, MTA, UCA, SWA, DBS | cost-reimbursable or incentive, 18 months or more |
| `svc_total_value` | money | AoS | range of the total estimated value, all years, current-year dollars: `under_10m` `10m_to_50m` `50m_to_100m` `100m_to_250m` `250m_to_500m` `500m_to_1b` `1b_plus` |
| `svc_annual_value` | money | AoS | range of the highest single year: `under_25m` `25m_to_250m` `250m_to_300m` `300m_plus` |
| `svc_special_interest` | boolean | AoS | |
| `svc_vehicle` | choice | AoS | `standalone` `idiq_base` `task_order` |
| `svc_overlap` | boolean | AoS | |
| `svc_sensitive_functions` | boolean | AoS | |

A missing field is unknown, and so is a value such as `unknown`, `tbd` or `not sure`. The engines accept these input forms:

- `yes`/`no`, `y`/`n` and `true`/`false`
- dollar answers as a range id, label or synonym (`20m_to_50m`, `$20M to $50M`, `$100M+`), or as an amount such as `45M`, `about $45 million` or `45000000`, which is stored as the range it falls in
- option values, option labels or the synonyms in each option's `aliases` (for example `ACAT IC` for `mdap`)
- event ids, short names such as `MS B`, full names, or the event's `aliases` (for example `Milestone B`, `MSB`)

Matching ignores case, spaces and punctuation. Anything else is not guessed: the result's `unrecognized` list names each ignored field or value with the reason, and the field stays unknown. An event marked `every` (SWA "Each decision point") cannot be the next event, because its items are due at every decision point.

## Dollar ranges

Dollar questions are answered with ranges, so nobody has to enter an estimate. `tools/build_rules.py` writes each dollar question's `options` (id, label, `lo`, `hi`, and whether each end is included). It cuts the ranges at every threshold the rules test for that field, plus the services-category thresholds in `scat` (`total_gte`, `annual_gt`).

- **A value exactly on a cut** goes where the rules put it. "At least" and "under" tests (`gte`, `lt`) put it in the upper range; "over" and "at most" tests (`gt`, `lte`) put it in the lower one.
- **Where the rules disagree**, the upper range wins. At exactly $20M, EVMS applies at "$20M or more" but CSDR reports start "over $20M", so a $20M contract counts as `20m_to_50m` and may show a CSDR report that strictly starts above it. This can only add a report, never drop one.
- **Conditions are evaluated on ranges.** For a condition, a range stands for the amounts strictly inside it. A threshold at an end of the range settles the comparison; a threshold inside the range would leave it unknown, which the cuts prevent.

## Requirement record

| Field | Meaning |
| --- | --- |
| `id` | Stable identifier, `<pathway>.<table>.<slug>` |
| `code` | Short code for people and agents, tied to the release: `MCA-M` milestone, `MCA-R` recurring, `MCA-X` exceptions, `MCA-C` CCA, `MCA-B` APB rules, `MCA-N` breach, `MTA-T` Table 1, `MTA-S` may be applicable, `UCA-`, `SWA-`, `SWA-C` CCA, `DBS-`, `AOS-`, `CSDR-0n`, `EVM-0n` |
| `pathways` | Pathways the record belongs to (the EVMS rows list five, the CSDR rows up to three) |
| `table`, `table_name`, `url` | The AAFDID table (or DoDI) it came from |
| `name`, `type_text`, `source`, `approval`, `procedure`, `notes`, `footnotes` | AAFDID's own words |
| `kind` | `event`, `recurring`, `contract`, `compliance`, `conditional`, `triggered`, `reference` |
| `type` | `statutory`, `regulatory`, `both`, `unspecified` |
| `type_rule` | Optional: `{"if": condition, "then": type, "else": type, "unknown": type, "events": [...]}` where AAFDID's TYPE cell or note makes the type depend on the program. `unknown` is the type to show while the answer is missing; without it the type is `depends`. With `events` (APB and AoA), `then` applies only at those events: each entry in the result's `when` gets its own `type`, and the item's type is the one at the next event when it is due there, otherwise `both` if its events differ |
| `tool_note` | Optional: a note from this tool, kept apart from AAFDID's words, for example why a row without a TYPE column is classed statutory |
| `when` | `[{event, submission: initial or update}]` |
| `due_text` | Due wording for rows without event marks |
| `applies_if` | Condition (below) |
| `conditional_if` | Optional second condition that makes the row "may apply" when `applies_if` is false |
| `applies_when` | Plain-English form of the condition |
| `rule_basis` | Why the condition is what it is: AAFDID marks, or the note or row name it comes from |
| `currency` | Ids of `currency` notes attached to the record |
| `note_has_conditions` | True when the AAFDID note contains conditional wording |
| `phase` | DBS only: the phase column |
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

A mark that covers every option of a question (an MCA row marked for all four program types, say) is stored as `{"const": true}`, so an unanswered question does not hold it up. When a condition is unknown, the engine names only the fields that keep it unknown: parts already settled, such as a false branch of an `any`, are skipped.

## Status and grouping

| Result of `applies_if` | Status |
| --- | --- |
| true | from `kind`: event, recurring, contract and compliance become **required**; conditional becomes **conditional**; triggered becomes **triggered**; reference becomes **reference** |
| unknown | **undetermined**, with the missing fields and their questions |
| false, with `conditional_if` true | **conditional** |
| false, with `conditional_if` unknown | **undetermined** |
| false | **not_applicable**, with `applies_when` as the reason |

Required items are grouped against the profile's `event`:

- `at_focus`: due at the next event.
- `later`: due at an event after it.
- `earlier`: all of its events come before the next one.
- `ongoing`: no event.
- `as_required`: only the unordered "Other" event.
- `by_event`: no next event was given.

Items due at an `every` event (SWA "Each decision point") are always `at_focus` when a next event is given.

UCA programs also get **review** items (status `review`, group `review`). These are the MCA milestone and exceptions rows (`also_review` in `pathways.json`), tested with `mca_program_type` set to the program's `uca_acat`: false drops the row, unknown makes it `undetermined`, and true makes it `review`. Until `uca_acat` is answered none are listed, and the ACAT question's `affects` count includes them.

## Result

`parseInput(text)` reads a profile from text: JSON if the text parses as JSON (a leading byte-order mark is ignored), otherwise a profile block with any line endings. `evaluate(bundle, profile)` returns `profile` (normalized), `pathway`, `focus_event`, `derived` (the AoS services category), `counts` by status, `items` (sorted by group, first event and code), `questions_needed` (the visible questions that would settle unknown items or types, with how many items each affects), `currency_notes`, `unrecognized` and the disclaimer. `toMarkdown`, `toChecklist` and `toProfileBlock` format it; both engines produce identical output.

## Changing the rules

- A row changed on AAFDID: add an entry to a corrections file in `sources/`, and teach `tools/build_rules.py` to apply it. Keep the capture files unchanged.
- A new change since AAFDID: add a note to `rules/currency.json` with its sources and `attach` targets.
- A new question: add it to `rules/questions.json` with `show_if` and `why`, and use its `id` as a field in conditions.
- Then run `tools/build_all.sh`, review `tests/run_tests.py --update` output, and commit rules, snapshots, web page and agent pack together.
