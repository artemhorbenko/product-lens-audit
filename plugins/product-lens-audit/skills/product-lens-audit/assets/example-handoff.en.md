# Hands-off: Lens audit: demo report

Implementation brief generated from the audit. Work top to bottom: tasks are ordered by ICE, and a task always comes after the ones it depends on. Treat "hypothesis" tasks as experiments: test before building fully.

## Context

- **Main finding:** The bottleneck: only 9% of buyers ever see the invite
- While almost nobody sees the invite, polishing the share page will change very little. Fix visibility first, then the speed of the loop. In parallel, new clients need a faster launch: without it the product will not move from Revenue to Scale.
- **Product stage:** Revenue. Paying clients exist, so the product is at Revenue. Moving to Scale is blocked by manual launches: 31 days and 3 handoffs between teams for every new client.
- **Confidence:** 60%

### Owner answers and assumptions

- Who is the main customer?: Client brands (B2B)
- Goal for the quarter: More referral purchases at existing clients
- What data exists: Funnel analytics, support tickets, lost-deal reasons
- What has been tried (skipped): Skipped. Assumption: no invite-visibility tests yet

### Data sources

- [ok] Product walk-through — done
- [ok] Flow screenshots — done
- [ok] Start answers (3 of 4) — done
- [demo] Funnel analytics — demo
- [demo] Support tickets — demo
- [demo] Lost-deal reasons — demo
- [no] Ahrefs: search demand — not connected
- [no] Similarweb: competitor traffic — not connected

Missing, so lower confidence: Ahrefs: search demand, Similarweb: competitor traffic.

## Rules for the implementer

- Do not invent numbers. If a metric cannot be measured yet, add the tracking first.
- Do not submit real forms, payments or messages while testing.
- Do not change URLs that already rank without a 301 redirect.
- Keep each change small and measurable; record before/after values.
- When a task is a hypothesis, run the cheapest test first and stop if the threshold is not met.

## Suggested order

| # | ID | Task | ICE | Type | Evidence |
|---|---|---|---|---|---|
| 1 | T01 | Show the invite on the thank-you page and in the order confirmation email (top 3) | 512 | optimize | observed |
| 2 | T02 | Email with a personal link 7 days after delivery (top 3) | 392 | optimize | hypothesis |
| 3 | T08 | 2 interviews a week with lost deals (top 3) | 378 | optimize | observed |
| 4 | T05 | LTV/CAC report on referred customers for the brand's CFO | 288 | optimize | hypothesis |
| 5 | T09 | Remove the fake "offer expires" timer | 288 | optimize | observed |
| 6 | T04 | "Invite shown" event on every integration + automatic tracking check after each client deploy | 280 | optimize | observed |
| 7 | T03 | "Launch in 1 day" campaign template | 252 | optimize | observed |
| 8 | T12 | One owner for the whole launch journey | 252 | optimize | observed |
| 9 | T06 | Sandbox with demo data for prospects | 140 | explore | hypothesis |
| 10 | T10 | Agency workspace for several brands | 120 | explore | hypothesis |
| 11 | T11 | DTC subscription segment: reward = a free month | 120 | explore | hypothesis |
| 12 | T07 | Managed program: the brand sets the goal, we optimize | 72 | explore | hypothesis |

## Tasks

### 1. T01 — Show the invite on the thank-you page and in the order confirmation email

- Lens: TOC · CRO · ICE 512 = 8×8×8 · Type: optimize · observed
- Effort: 2–3 days

**Evidence.** Funnel: of 120,000 purchases only 10,800 (9%) saw the invite. After that conversion is healthy: 36% open the share screen and 40% of them share. So the constraint is right here.

**Hypothesis.** If we show the invite right after purchase, visibility will grow from 9% to 25% or more, because this is the moment of highest satisfaction.

**Steps:**

1. Add the invite block to the thank-you page for every client whose integration allows it.
2. Add the personal link to the order confirmation email.
3. Turn on an A/B test: half of buyers see the new placements, half see the current flow.
4. After 2 weeks compare the share who saw the invite and shares per 1,000 purchases.

**Acceptance criteria:**

- [ ] Visibility ≥ 20% and shares per 1,000 purchases not below control
- [ ] Metric: Share of buyers who saw the invite (now 9%)

**How to verify:** A/B test on 50% of traffic of two clients, 2 weeks

**Risk / guardrail:** Pushiness: show it once per purchase and never cover the order confirmation.

**Alternatives rejected:**

- Pop-up on the product page: rejected, it interrupts the purchase and risks the client's CRO.
- Banner in the account area: kept as the next test, fewer people go there.

**Pre-mortem:** It failed because half of the clients have a custom thank-you page and the block did not render. So check integration compatibility first (step 4).

**Copy variants:**

- "Give a friend 15% off and get $15 after their purchase": the benefit for both in one line.
- "Enjoyed it? Share with a friend and get a bonus": softer, leans on the satisfaction just felt.


### 2. T02 — Email with a personal link 7 days after delivery

- Lens: Growth loops · ICE 392 = 7×7×8 · Type: optimize · hypothesis
- Effort: ≈1 day

**Evidence.** New advocates are rare: 85 of 610 friends who bought (14%). There is no second invite after delivery, yet that is when satisfaction peaks. The effect is untested, so this is a hypothesis.

**Hypothesis.** If we remind buyers of their link after delivery, the share rate will grow, because by then they have tried the product.

**Steps:**

1. Pick one client with enough order volume.
2. Set up an email 7 days after delivery with the personal link.
3. Split buyers into test and control groups.
4. Compare shares per 1,000 purchases over 30 days.

**Acceptance criteria:**

- [ ] +20% shares per 1,000 purchases vs control with complaints < 0.1%
- [ ] Metric: Shares per 1,000 purchases within 30 days

**How to verify:** Manual send for one client with a control group

**Risk / guardrail:** Spam complaints: one email, easy unsubscribe, no follow-up reminders.

**Alternatives rejected:**

- Push notification: rejected, few clients have an app.
- SMS: rejected, expensive and needs separate consent.

**Pre-mortem:** It failed because the email landed in Promotions. Test the subject and sender on a seed inbox before launch.


### 3. T08 — 2 interviews a week with lost deals

- Lens: Discovery · ICE 378 = 6×7×9 · Type: optimize · observed
- Effort: ≈2 hours a week

**Evidence.** Reasons for lost deals are recorded as one phrase in the CRM. Without regular conversations it is unclear what blocks the sale: price, integration or trust.

**Hypothesis.** If we regularly hear why deals are lost, we will find 1–2 recurring barriers before building anything.

**Steps:**

1. Each week take 2 lost or stalled deals from the CRM.
2. A 20-minute call with a 5-question script about past decisions, not hypothetical ones.
3. Record quotes and tags in one table.
4. Once a month summarize patterns and move them to the backlog.

**Acceptance criteria:**

- [ ] At least 8 interviews a month and 1 backlog decision based on them
- [ ] Metric: 2 interviews a week and at least 1 new pattern a month

**How to verify:** 8 calls in a month, a 5-question script

**Risk / guardrail:** Selling instead of researching: ask about past actions, offer nothing.

**Alternatives rejected:**

- A survey for lost deals: as a supplement, answers are few and shallow.
- Analysing sales call recordings: kept, cheap but no substitute for conversations.

**Pre-mortem:** It failed because nobody accepted the invitation. Invite from the founder's name and offer a gift for their time.


### 4. T05 — LTV/CAC report on referred customers for the brand's CFO

- Lens: JTBD · ICE 288 = 8×6×6 · Type: optimize · hypothesis
- Effort: ≈1 week

**Evidence.** The brand hires the referral program for profitable customers without extra work (JTBD), yet the report shows only shares and clicks. That the CFO needs exactly this number is still a hypothesis.

**Steps:**

1. Compare LTV and CAC of referred and other customers on data from 2–3 brands.
2. Build a one-page report for the CFO.
3. Show it in 3 contract renewals and collect the reaction.

**Acceptance criteria:**

- [ ] Metric: Share of renewals where the report was used in the conversation

**Risk / guardrail:** Incrementality: some friends would have bought anyway, so the report needs an honest estimate.


### 5. T09 — Remove the fake "offer expires" timer

- Lens: Privacy · ICE 288 = 4×8×9 · Type: optimize · observed
- Effort: ≈1 hour

**Evidence.** In one client's widget the "offer expires" timer resets on every page reload. This is fake urgency.

**Steps:**

1. Remove the timer or tie it to the real end date of the promotion.
2. Add a rule to the guidelines: real deadlines only.

**Acceptance criteria:**

- [ ] Metric: Complaints and unsubscribes; conversion not below control

**Risk / guardrail:** A small conversion drop is possible, and worth the trust it keeps.


### 6. T04 — "Invite shown" event on every integration + automatic tracking check after each client deploy

- Lens: Reliability · ICE 280 = 7×8×5 · Type: optimize · observed
- Effort: 3–4 days

**Evidence.** Only some integrations send the invite-shown event, so 9% may be an underestimate. This is a measurement gap: without it step 1 cannot be judged fairly.

**Steps:**

1. List the integrations where the event is missing.
2. Add the event to the SDK and the docs.
3. After every client deploy, check automatically that events arrive.
4. Alert the CSM if no events arrive for more than 24 hours.

**Acceptance criteria:**

- [ ] Metric: Share of integrations sending the show event (target 100%)

**Risk / guardrail:** False alarms: alert only after 24 hours of silence.


### 7. T03 — "Launch in 1 day" campaign template

- Lens: Kaizen · ICE 252 = 6×7×6 · Type: optimize · observed
- Effort: ≈1 week

**Evidence.** Launch takes 31 days on average, though sales promise 2 weeks. Most campaigns are assembled by hand from the same blocks.

**Steps:**

1. Take the 3 most common campaign setups.
2. Turn them into templates with default settings.
3. Measure days from signed contract to launch for every new client.

**Acceptance criteria:**

- [ ] Metric: Days from signed contract to launch (now 31)

**Risk / guardrail:** Templates that do not fit: let every block be changed.


### 8. T12 — One owner for the whole launch journey

- Lens: Service design · ICE 252 = 6×6×7 · Type: optimize · observed
- Effort: ≈2 days to set up

**Evidence.** There are 3 handoffs between sales, integration and launch, and nobody owns the whole journey. Hence 31 days instead of the promised 14.

**Steps:**

1. Assign a launch owner for every new client.
2. Draw a service blueprint of the current journey and mark the waits.
3. Each week review clients stuck for more than 7 days.

**Acceptance criteria:**

- [ ] Metric: Days to launch and number of handoffs

**Risk / guardrail:** An owner without authority: give them the right to speed up other teams' work.


### 9. T06 — Sandbox with demo data for prospects

- Lens: PLG · ICE 140 = 7×5×4 · Type: explore · hypothesis
- Effort: 1 day for the test, 3–4 weeks for a version

**Evidence.** Today a brand sees value only after the sale and launch. A sandbox with demo data could shorten the sales cycle, but demand for it is untested.

**Steps:**

1. Run a fake door: a "Try the sandbox" button on the website.
2. Count clicks for 2 weeks.
3. If there are enough clicks, build a minimal version on demo data.

**Acceptance criteria:**

- [ ] Metric: Fake-door clicks and requests from it

**Risk / guardrail:** A fake door disappoints: show an honest message and offer a demo with a person.


### 10. T10 — Agency workspace for several brands

- Lens: Platform · ICE 120 = 6×5×4 · Type: explore · hypothesis
- Effort: 2 weeks of research

**Evidence.** Agencies run several brands, but each brand is set up separately. How many agencies would pay for a shared workspace is unknown.

**Steps:**

1. Talk to 5 partner agencies.
2. Describe a minimal workspace: brand list, shared templates, reports.
3. Decide after the interviews.

**Acceptance criteria:**

- [ ] Metric: Number of agencies ready for a pilot

**Risk / guardrail:** Losing focus before the constraint is solved.


### 11. T11 — DTC subscription segment: reward = a free month

- Lens: Blue Ocean · ICE 120 = 6×4×5 · Type: explore · hypothesis
- Effort: ≈1 month

**Evidence.** DTC subscription brands are underserved by competitors, and a free month is a natural reward for a subscription. Demand is a hypothesis.

**Steps:**

1. Find 10 DTC brands with subscriptions.
2. Offer a pilot with a free-month reward.
3. Compare virality with current clients.

**Acceptance criteria:**

- [ ] Metric: Pilots and the share rate in pilot brands

**Risk / guardrail:** Being different does not mean being wanted. Build nothing before it is confirmed.


### 12. T07 — Managed program: the brand sets the goal, we optimize

- Lens: Business model · ICE 72 = 9×4×2 · Type: explore · hypothesis
- Effort: 3-month pilot

**Evidence.** Some brands want an outcome, not a tool. A managed program paid for results changes the model, but needs different economics.

**Steps:**

1. Offer 2 clients a pilot: they set the goal and limits, we set up and optimize.
2. Track team hours on each pilot.
3. After 3 months compare the margin with the subscription.

**Acceptance criteria:**

- [ ] Metric: Pilot margin and the client's result

**Risk / guardrail:** Manual work eats the margin. Cap the hours.

## Glossary

- **Lean Analytics** (product stages): A model where a product moves through stages: empathy, stickiness, virality, revenue, scale. Each stage has its own metrics and lenses.
- **Service design** (designing the whole journey): Whether the client's whole experience works together, from the sale to launch, support and billing, not just the interface.
- **service blueprint** (service map): A diagram of the journey: what the client does, what the team does visibly and behind the scenes, and which systems support it.
- **Growth loops** (self-feeding growth): One successful action starts the next: a buyer shares, a friend buys, the friend becomes an advocate.
- **Blue Ocean** (uncontested space): Blue Ocean strategy: compete with a different kind of value where competition is still weak.
- **pre-mortem** (imagining failure first): Imagine that 3 months later the idea failed and explain why. The reasons become risks you can close in advance.
- **Discovery** (continuous customer research): Regular customer conversations and testing assumptions before building anything.
- **fake door** (demand test without a product): A button or page for a feature that does not exist yet. Clicks show demand; people are told honestly that it is coming.
- **thank-you** (page after purchase): The page a buyer sees right after placing an order. The moment of highest satisfaction.
- **Sandbox** (playground with demo data): A safe copy of the product where everything can be tried without integration or risk.
- **Kaizen** (continuous small improvements): Improving a process a little at a time: faster, fewer errors, less manual work.
- **JTBD** (the job the customer hires for): Jobs to Be Done: a product is hired to make progress on a job. The brand wants profitable customers without extra work, not a platform.
- **TOC** (Theory of Constraints): A system runs at the speed of its narrowest step. Here it is invite visibility: 9%.
- **CRO** (conversion rate optimization): Getting more people to the valuable action.
- **PLG** (product-led growth): The product itself acquires customers (trial, sandbox), not only sales.
- **ICE** (priority score): Impact × Confidence × Ease, each from 1 to 10. The higher the product, the sooner to start.
- **LTV** (lifetime value): How much money a customer brings over the whole relationship.
- **CAC** (customer acquisition cost): How much it costs to win one new customer.
- **CFO** (chief financial officer): The person who decides whether the program pays off.
- **CSM** (customer success manager): Looks after a client after the sale, from launch to renewal.
- **DTC** (direct-to-consumer): Brands that sell directly to buyers, without marketplaces or distributors.
- **CRM** (customer and deal database): The system where sales track deals, contacts and the reasons they win or lose.
- **SDK** (integration library): Code the client installs on their site so the widget and events work.
- **A/B** (split test): Half of people see the new version, half the old one; the difference shows the effect.
