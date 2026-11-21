# Changelog

## 1.2.0 - 2026-11-21

- English demo: `assets/example-audit.en.json`; README lists every lens and supporting concept, with links to both demos.

- The report template renders everything from one `<script type="application/json" id="audit">` block. Claude writes only data, so a report takes far fewer tokens and the layout cannot drift.
- `references/audit.schema.json` and `assets/example-audit.json`.
- `scripts/validate_audit.py`: evidence for every opportunity, ICE in 1-10, sources for KPI numbers, alternatives and pre-mortem for the top 3.
- `scripts/build_report.py`: validates, fills the template, sets language and title, escapes text.
- `leaks` variant is built into the template; opportunities on the same matrix point are spread apart.
- SKILL.md split: lenses in `references/lenses.md`, data sources in `references/data-sources.md`.
- Step 5 adds a fact check (in Claude Code, by a separate subagent).
- `evals/`: scenarios, trigger prompts, results log.

## 1.1.0 - 2026-11-21

- Report labels in Ukrainian and English: the template picks its `UI` dictionary from `<html lang>`.
- Funnel "no data" state: steps with `n: null` show a hatched bar instead of invented numbers.
- `check_report.py` now flags overlapping text labels in the funnel, KPIs and journey.
- Data shapes documented in `references/report-spec.md`.
- GitHub issue templates: report bug, wrong conclusion, data source request.
- Tested on a real site with every start question skipped and no analytics access.

## 1.0.0 - 2026-11-21

First public release.

- 13 lenses in 5 groups, plus Lean Analytics stage, LIFT, Value Proposition Canvas, Hook model, HEART, Cynefin and pre-mortem.
- Data-source check (step 0) and up to 4 skippable start questions.
- Findings labelled observed or hypothesis, ICE prioritization, optimize vs explore.
- Visual HTML report template: constraint headline, funnel, product stage, lens radar, service-blueprint journey, impact-effort matrix, ranked table, full plan, data and confidence.
- Tooltips for every term: hover on desktop, tap on phone and tablet.
- `scripts/check_report.py`: headless render check on desktop, tablet and phone.
- `product-lens-audit-skill.zip` in the repo root for uploading to the Claude app (rebuild it whenever the skill folder changes).
