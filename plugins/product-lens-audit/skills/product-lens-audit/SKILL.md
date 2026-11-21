---
name: product-lens-audit
description: Audit a digital product (website, web app, SaaS flow, mobile app screenshots, landing page or funnel) through 13 strategy lenses - CRO, Theory of Constraints, Kaizen, JTBD, continuous discovery, service design, growth loops, PLG, platform, business model, Blue Ocean, reliability and privacy - and deliver a visual report with prioritized, evidence-based improvements. Use when someone asks to audit or review a product, find growth opportunities, explain why a product is not growing or converting, or suggest what to improve next.
---

# Product Lens Audit

Look at a digital product through several strategic lenses and return a short, prioritized list of opportunities in a visual report. Each lens is a different question; the value is in seeing what one lens misses.

Respond in the user's language, and write the report in it too.

Files next to this SKILL.md:
- `references/report-spec.md` - the report's sections, look, tooltips and mobile rules. Read it before step 4.
- `assets/report-template.html` - a finished report (fictional product "Loopwell", content in Ukrainian) to copy and fill. Its fixed interface labels come from a built-in dictionary chosen by `<html lang>`: `uk` and `en` exist; for another language, add an entry to `UI` with the same keys.
- `scripts/check_report.py` - automated render check for step 5.

## 0. Check which data sources are connected

Before gathering, look at the tools this session actually has (search the tool list / ToolSearch; never assume). Build a source list with a status for each: `ok` (connected and used), `demo` (user-supplied sample or partial), `no` (not connected). Typical sources and what they feed:

| Source | Look for tools like | Feeds lenses |
|---|---|---|
| Browser (walk flows, screenshots) | Claude in Chrome, built-in or remote browser | CRO, service design, privacy, PLG |
| Product analytics | GA4, Amplitude, Mixpanel, PostHog, Pendo | CRO, TOC, growth loops, AARRR |
| SEO / search demand | Ahrefs, Semrush, Google Search Console | JTBD, Blue Ocean, acquisition |
| Market traffic | Similarweb | Blue Ocean, PLG, competitors |
| Support / feedback | Intercom, Zendesk, Front, app reviews | discovery, service design, Kaizen |
| Sales / CRM | HubSpot, Salesforce, notes on lost deals | JTBD, discovery, business model |
| Experiments / flags | GrowthBook, LaunchDarkly, Optimizely | CRO, reliability |
| Monitoring | Sentry, Datadog, status page | reliability |

Use a connected source only read-only. If an important source is missing, say which one in one line and continue; never fill the gap with invented numbers. The list goes into the report's data-sources block, and each `no` lowers confidence.

## 0.5 Ask the requester (every question skippable)

First look for saved context: a `product-lens-context.md` or a previous `audit.json` in the project or attached by the user. Read it and ask only about what it does not cover. When the audit ends, offer to save the answers and the audit data there, so the next run can compare (re-audit).

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

For each lens, write 1-3 concrete findings tied to something you actually saw (a screen, a step, a number). Skip a lens if it truly has nothing; say so in one line.

**Improve the existing system**
- **CRO** - Where do people drop out of the journey, and why? Friction, unclear value, too many fields, weak CTA, missing trust signals, mobile issues. For key pages check, in order of impact: value proposition, relevance to the traffic source, clarity, anxiety (risk, missing trust signals), distraction, urgency (only real urgency) - the LIFT factors.
- **Theory of Constraints** - Which single step limits the whole system right now? Improving anything else first is low value. The constraint may be operational (onboarding queue, approvals), not UI.
- **Kaizen** - What internal work is slow, error-prone or manual (setup time, support load, repeated fixes)? Small steady improvements, with a metric.

**Are we solving the right problem?**
- **JTBD** - What progress is the customer really hiring the product for? Format: "When [situation], I want [motivation], so I can [outcome]." Note push/pull/anxiety/habit forces. Does the product talk about the job or about features? Map the customer's main pains and gains against what the product actually relieves or creates (Value Proposition Canvas); unmatched pains are opportunities.
- **Continuous discovery** - What evidence loops exist (interviews, churn reasons, lost deals, tickets)? What should be asked next?
- **Service design** - Does the whole experience hold together: sales promise -> onboarding -> first value -> support -> billing? Look for handoff gaps between teams.

**Grow differently**
- **Growth loops** - Does one successful action create the next (invites, content, shared output)? Measure loop coefficient, cycle time, retention. For return visits use the Hook model: is there an external trigger that brings people back (channel, email, notification), a simple action, a reward worth returning for, and something users invest (subscription, saved items, profile)? A missing trigger is the most common gap.
- **PLG** - Can the product itself acquire, activate or expand (trial, sandbox, self-serve, in-product upsell)? What is time-to-value and the aha moment?
- **Platform/ecosystem** - Could partners, integrations, APIs or agencies add value the team cannot build alone? Are there network effects (each new user or partner makes the product better for others), or could there be?

**Change the game**
- **Business-model innovation** - What if delivery, pricing or ownership changed (managed service, pay-for-outcome, automation instead of tooling)?
- **Blue Ocean (ERRC)** - What could be Eliminated, Reduced, Raised, Created vs. competitors? Which non-customers are ignored? Different must also be valuable - flag what needs validation.

**Protect long-term value**
- **Reliability** - Are critical paths monitored (tracking, payments, emails, rewards)? Safe rollouts, rollback, status communication?
- **Privacy / ethical design** - Unnecessary data collection, unclear terms, dark patterns, fake urgency, consent issues.

Useful supporting tools: AARRR funnel to locate stages, North Star metric to align, Kano (basic / linear / delighter) to classify features, LTV/CAC and incrementality for money questions, HEART (happiness, engagement, adoption, retention, task success) to choose the success metric of each recommendation, Cynefin to decide Optimize vs Explore (clear or complicated problems -> optimize; complex, cause unknown -> explore with small probes).

If specialized skills are installed (page CRO, JTBD, opportunity solution tree, experiment design), mention them as the next step for a deep dive instead of duplicating their work.

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

Read `references/report-spec.md`, then copy `assets/report-template.html`, set `<html lang>` to the report language, and replace only the data at the top of its script (`funnel`, `stage`, `lenses`, `route`, `ops`, `plans`, `detail`, `answers`, `sources`, `kp`, glossary `GL`) and the report's own text (headline, lead, section headings and intros, "how this report was made", footer note). Interface labels translate themselves through `UI`. When the problem steps are not a sequential funnel, use the "leaks vs target" variant described in the spec.

Deliver it as one self-contained HTML page: publish it as an artifact when an artifact tool exists, otherwise save the .html file and send or open it. In chat, reply only with 3-5 summary bullets, the link or file, and one line on what was checked.

## 5. Check the report renders well (before delivering)

Never deliver a report you have not checked.

1. **Script check.** Run `node --check` (or an equivalent parser) on the page's last `<script>`. One syntax error blanks every chart.
2. **Automated render check** when Python and a Chromium-based browser are available (install with `pip install playwright` and `playwright install chromium` if needed):
   `python scripts/check_report.py path/to/report.html --out ./report-check`
   It opens the page as desktop (1280px), tablet (820px, touch) and phone (390px, touch) and fails on: page or console errors, sideways scroll, empty radar/matrix/funnel/KPIs, tooltips that do not open on hover (desktop) or tap (touch) or do not close on a second tap, table cells not wrapped in one `.cv`, filters that break the table or drop tooltips. It also saves screenshots, including dark mode.
3. **Look at the screenshots**: overlapping labels on the radar or matrix, text split into columns, cut-off badges, empty areas, poor dark-theme contrast.
4. **Fix and re-check**, at most twice. If something still fails, say what in one line.
5. **No headless browser** (for example in the Claude app without a shell): open the published page with whatever browser tool exists at desktop and narrow width and check the same list by looking. If no browser tool exists either, run the script check, say plainly which visual checks were not done, and ask the person to open the page on their phone.

## Rules
- Every finding must point to evidence or be clearly marked as an assumption.
- Prefer fewer, sharper recommendations over long lists.
- Do not recommend manipulative tactics even if they would raise conversion.
- Separate optimization ideas from exploration bets; a healthy plan has mostly the first and a few of the second.
- Never invent evidence: no made-up numbers, logos, testimonials, reviews, urgency, discounts or guarantees, either in findings or in suggested copy.
- When a recommendation changes copy (titles, CTAs, offers), give 2 alternative wordings with a one-line reason each.
- Never invent metrics to fill the charts. If funnel numbers are unknown, show the funnel with step names and "no data" instead of bars, and lower confidence.
- Lens scores are judgments: base each on findings, and be consistent (below 40 = big untapped potential, 40-60 = partial, above 60 = solid).
