---
name: product-lens-audit
description: Audit a digital product (website, web app, SaaS flow, mobile app screenshots, landing page or funnel) through 13 strategy lenses - CRO, Theory of Constraints, Kaizen, JTBD, continuous discovery, service design, growth loops, PLG, platform, business model, Blue Ocean, reliability and privacy - and deliver a visual report with prioritized, evidence-based improvements. Use when someone asks to audit or review a product, find growth opportunities, explain why a product is not growing or converting, or suggest what to improve next.
---

# Product Lens Audit

Look at a digital product through several strategic lenses and return a short, prioritized list of opportunities in a visual report. Each lens is a different question; the value is in seeing what one lens misses.

Respond in the user's language, and write the report in it too.

Files next to this SKILL.md (read each when its step comes, not up front):
- `references/data-sources.md` - which tools to look for, what to query, fallbacks, polluted-data signs (step 0-1).
- `references/lenses.md` - the 13 lenses, their questions, icon and group ids, weighting by stage (step 2).
- `references/report-spec.md` and `references/audit.schema.json` - the report's sections and the shape of its data (step 4).
- `assets/report-template.html` - the report page; it renders everything from one JSON block. `assets/example-audit.json` is a full example (fictional product "Loopwell", in Ukrainian).
- `scripts/validate_audit.py`, `scripts/build_report.py`, `scripts/check_report.py` - data check, page build, render check (steps 4-5).

## 0. Check which data sources are connected

Before gathering, look at the tools this session actually has (search the tool list / ToolSearch; never assume). `references/data-sources.md` lists what to look for, which queries to run, the fallbacks (browser, screenshots) and the signs of polluted data. Build a source list with a status for each: `ok` (connected and used), `demo` (user-supplied sample or partial), `no` (not connected, or connected but returning an error, "no plan" or no access).

Use a connected source only read-only. If an important source is missing, say which one in one line and continue; never fill the gap with invented numbers. The list goes into the report's data-sources block, and each `no` lowers confidence.

## 0.5 Ask the requester (every question skippable)

First look for saved context: a `product-lens-context.md` or a previous `audit.json` in the project or attached by the user. Read it and ask only about what it does not cover. With a previous `audit.json`, say in the report what changed since then: which steps were done, how the metrics moved, whether the constraint moved.

Then ask one short round of up to 4 questions. Use a multiple-choice question tool when available (AskUserQuestion or similar), and give every question a "Skip" option; otherwise ask in plain text and say they can skip any. Never block: if the person skips or does not answer, state the assumption you take and continue.

Pick the questions that change the analysis most for this product:
- **Who is the main customer** the product must win now (for a media site: advertisers or readers; for SaaS: buyer or user)?
- **The one goal for this quarter** (traffic, first sales, activation, retention, less manual work).
- **Data they can share**: analytics, Search Console, funnel numbers, CRM, support tickets. Screenshots are fine.
- **What already happened**: past experiments, sales conversations, why deals or users were lost.

The last question often gives the strongest evidence of all (for example, "six advertisers asked for our stats and declined" turns a page-copy problem into a traffic problem). When the person shares data mid-run, revise the constraint and priorities instead of appending it.

Record each answer in the sources list as `ok` ("from the owner"), and list all questions with their answers in the report's data section; a skipped one shows "Skipped" plus the assumption taken.

## 1. Gather the material (before judging anything)

Use whatever is available, in this order of preference:
- **Live product**: open it in a browser and walk the key flows yourself (landing -> signup/onboarding -> core action -> payment/share). Take screenshots of each step. Do not submit real forms, payments or messages without asking.
- **Screenshots, Figma, recordings** the user attached.
- **Data**: analytics (funnel steps, conversion per step), support tickets, sales loss reasons, reviews, NPS comments. Ask for it if missing, but do not block on it.
- **Screenshots of dashboards** count as data: read the numbers off them, note the date range, and flag signs of polluted data (very high Direct share, data-center cities, own visits).
- **Context**: use the answers from step 0.5; for anything still unknown, state the assumption.

Write down the main journey as numbered steps. Mark where you have numbers and where you are guessing.

**Find the product stage (Lean Analytics).** Empathy (is the problem real?) -> Stickiness (do people come back?) -> Virality (do they bring others?) -> Revenue -> Scale. Name the current stage from evidence and weight the lenses by it: at Stickiness, retention and loops matter more than monetization. Flag a stage mismatch explicitly (for example, a site trying to sell ads while only 5% of readers ever return).

## 2. Apply the lenses

Read `references/lenses.md` and go through all 13 lenses in 5 groups: improve the system (CRO, Theory of Constraints, Kaizen), right problem (JTBD, continuous discovery, service design), grow differently (growth loops, PLG, platform), change the game (business model, Blue Ocean), protect value (reliability, privacy). For each lens write 1-3 findings tied to something you actually saw, and score it 0-100. If specialized skills are installed (page CRO, JTBD, opportunity solution tree, experiment design), name them as the next step for a deep dive instead of duplicating their work.

## 3. Prioritize

Collect all findings into one table:

| # | Opportunity | Lens | Evidence (what you saw) | Impact | Confidence | Effort | ICE | Type |

- Impact, Confidence, Ease each 1-10; ICE = product. Be honest: low confidence when based on guesses.
- Type = **Optimize** (make the current thing better) or **Explore** (different solution, market or model).
- Put the current constraint (TOC) first unless something else clearly dominates.
- Add guardrails for each growth idea (trust, privacy, reliability risks).
- Label each finding **observed** (seen in data or on the product) or **hypothesis**. Record for numbers: metric definition, period, source, known gaps.
- For the top 3, compare at least 2 alternative solutions before choosing (opportunity solution tree), write the experiment with its risk type (value, usability, viability, feasibility) and a success threshold, and run a short pre-mortem: "it is 3 months later and this failed - why?"; put the answer into the plan.
- List **instrumentation gaps** (missing events, polluted channels, no conversion tracking) as their own opportunity when they block decisions.

## 4. Output: a visual report page

Read `references/report-spec.md`. Write the audit as one `audit.json` that follows `references/audit.schema.json` (start from `assets/example-audit.json`): language, the report's own text (headlines that state their point), KPIs, funnel or leaks, stage, 13 lens scores, journey, opportunities with a `detail` entry each, `plans` for the top 3, start answers, sources and the glossary. You write data only; the template draws every chart, table and label and computes ICE, the health index, quick wins and confidence.

- **With a shell:** `python scripts/build_report.py audit.json report.html`. It runs `validate_audit.py` first and refuses to build on errors (an opportunity without evidence, ICE outside 1-10, a KPI number with no source, a top-3 bet without alternatives or pre-mortem). Fix the data, not the template.
- **Without a shell** (Claude app without code execution): copy `assets/report-template.html`, set `<html lang>` and `<title>`, and replace the content of its `<script type="application/json" id="audit">` block with your JSON. Write `<\/` instead of `</` inside strings. Check the rules from `validate_audit.py` yourself.

Interface labels come from the template's `UI` dictionary chosen by `<html lang>` (`uk`, `en`; add an entry with the same keys for another language). Save `audit.json` next to the report: the next run compares against it.

Deliver one self-contained HTML page: publish it as an artifact when an artifact tool exists, otherwise send the .html file. In chat, reply with 3-5 summary bullets, the link or file, and one line on what was checked.

## 5. Check before delivering

Never deliver a report you have not checked.

1. **Facts.** Every number in the text, KPIs and `why` fields must trace to a source in `sources` or to the owner's answers, and the arithmetic must hold (shares, ratios, counts). In Claude Code, give this check to a separate subagent that has not seen your reasoning: pass it `audit.json` and the raw material (data exports, page text, screenshots) and ask it to list every number it cannot trace. Elsewhere, do the pass yourself, number by number. Fix or remove what does not trace.
2. **Script.** `node --check` on the template's main script if you edited anything beyond the JSON.
3. **Render**, when Python and a Chromium-based browser are available (`pip install playwright`, `playwright install chromium`): `python scripts/check_report.py report.html --out ./report-check`. It opens the page as desktop (1280px), tablet (820px, touch) and phone (390px, touch) and fails on page or console errors, sideways scroll, empty charts or KPIs, overlapping labels, tooltips that do not open on hover or tap or do not close on a second tap, table cells not wrapped in one `.cv`, filters that break the table or drop tooltips. It saves screenshots, including dark mode.
4. **Look at the screenshots**: overlapping labels on the radar or matrix, text split into columns, cut-off badges, empty areas, poor dark-theme contrast.
5. **Fix and re-check**, at most twice. If something still fails, say what in one line.
6. **No headless browser:** open the published page with any browser tool at desktop and narrow width and check the same list by looking. If no browser tool exists, say plainly which visual checks were not done and ask the person to open the page on their phone.

## Rules
- Every finding must point to evidence or be clearly marked as an assumption.
- Prefer fewer, sharper recommendations over long lists.
- Do not recommend manipulative tactics even if they would raise conversion.
- Separate optimization ideas from exploration bets; a healthy plan has mostly the first and a few of the second.
- Never invent evidence: no made-up numbers, logos, testimonials, reviews, urgency, discounts or guarantees, either in findings or in suggested copy.
- When a recommendation changes copy (titles, CTAs, offers), give 2 alternative wordings with a one-line reason each.
- Never invent metrics to fill the charts. If funnel numbers are unknown, show the funnel with step names and "no data" instead of bars, and lower confidence.
- Lens scores are judgments: base each on findings, and be consistent (below 40 = big untapped potential, 40-60 = partial, above 60 = solid).
