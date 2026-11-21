# Changelog

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
