# Results

Scores 1-5: **E** evidence (every finding traces to a source), **H** honesty about missing data, **P** plan specific to the product, **R** report renders on desktop, tablet and phone.

| Date | Version | Scenario | Product | E | H | P | R | Time | What broke |
|---|---|---|---|---|---|---|---|---|---|
| 2026-11-21 | 1.0.0 | data-mid-run | private media site A | 4 | 4 | 4 | 3 | ~40 min | Constraint flipped when the owner's data arrived (copy -> traffic); led to the "revise, don't append" rule. Mobile table cells split into columns; fixed with `.cv`. |
| 2026-11-21 | 1.1.0 | skip-all, connector-error | private media site B | 4 | 5 | 4 | 4 | ~30 min | "No data" label overlapped the constraint note in the funnel; fixed, and check_report now catches overlapping labels. |
| 2026-11-21 | 1.2.0 | install (CLI) | - | - | - | - | - | 1 min | `claude plugin marketplace add artemhorbenko/product-lens-audit` + install works in a clean home. Claude Code desktop and the Claude app: not yet run. |
| 2026-11-21 | 1.2.1 | real data via browser (GA4 + GSC), owner answers, redesign day | private B2B logistics site | 5 | 4 | 4 | 4 | ~35 min | Found the GA4 tag missing after the redesign deploy (told the owner mid-run). Report bugs: a tiny rate showed as "0%"; long labels ran into the bar column; the journey was too tight on tablets. All fixed; check_report now fails on overflowing labels. |
| 2026-11-21 | 1.2.1 | public-only, skip-all, English | B2B SaaS (referral platform) + its main competitor | 4 | 5 | 4 | 5 | ~30 min | No analytics, so constraints are hypotheses from the public site and review data. Competitor audit worked as a benchmark for the first. The browser stopped responding mid-run; review sites via web search filled the gap. |
