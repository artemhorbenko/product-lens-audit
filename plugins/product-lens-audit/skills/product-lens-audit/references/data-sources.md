# Data sources

Check what this session can actually reach before gathering: search the tool list (ToolSearch or similar) for each source below. Never assume a connector exists, and never fill a gap with invented numbers. Use every source read-only.

## Status

| Status | When |
|---|---|
| `ok` | Connected and used, or the owner's own answer or screenshot. |
| `demo` | A sample, a partial export, data you could only read off a screenshot with a cut-off range, or a free tier with partial data. |
| `no` | Not connected; connected but returning an error, "no plan" or "no access"; a plugin that is installed but inactive. Try a failing call once more; if it fails again, mark `no` and move on. |

Confidence in the report is the average of ok = 1, demo = 0.6, no = 0, so list only sources that matter for this product.

## What to look for and what to ask it

### Browser (walk the product)
- **Tools:** Claude in Chrome, the built-in browser, a cloud browser, or WebFetch for public pages.
- **Do:** walk landing -> signup or contact -> core action -> payment or share on desktop and at phone width. Take screenshots of each step and note load problems, broken links and console errors.
- **Don't:** submit real forms, payments or messages.
- **Fallback:** the owner's screenshots or a screen recording. If the shell cannot reach the site, read pages through a CMS connector.
- **Feeds:** CRO, service design, privacy, PLG.

### Product and web analytics
- **Tools:** GA4 (Google's official read-only MCP or a community one), Amplitude, Mixpanel, PostHog, Pendo, Matomo, Plausible, or Ahrefs Web Analytics.
- **Queries, last 90 days:**
  - sessions and users by channel;
  - landing pages with engagement;
  - the funnel steps as events with step-to-step conversion;
  - new vs returning users and a retention cohort;
  - countries and devices;
  - key events (contact clicks, signups, purchases).
- **Fallback:** screenshots of the Acquisition, Engagement and Retention reports, with the date range visible.
- **Polluted data:**
  - Direct above ~40% on a content site;
  - traffic from data-center cities (Ashburn, Boardman, Council Bluffs);
  - 0-second sessions;
  - the owner's own visits;
  - spikes from one referrer;
  - key events counted twice.
- **Feeds:** CRO, TOC, growth loops, AARRR, stage.

### Search demand and SEO
- **Tools:** Google Search Console (MCP or screenshots), Ahrefs, Semrush.
- **Free with Ahrefs:** Domain Rating works for any domain without a plan. Other Ahrefs tools need a plan and fail on other domains; mark them `no` when they do.
- **Search Console, 90 days:**
  - queries and pages with clicks, impressions and position;
  - CTR by position band (1-3, 4-10, 11-20);
  - pages with many impressions and few clicks;
  - countries;
  - indexed vs not indexed pages.
- **Ahrefs:**
  - organic keywords and top pages;
  - organic competitors;
  - referring domains;
  - keyword volume for the job the product serves.
- **Fallback:** Search Console Performance screenshots with the date range visible.
- **Polluted data:**
  - brand queries mixed with non-brand;
  - one viral page hiding a flat rest;
  - impressions from image search counted as web.
- **Feeds:** JTBD, Blue Ocean, acquisition.

### Market and competitors
- **Tools:** Similarweb, Ahrefs organic competitors, web search.
- **Queries:**
  - competitors' traffic by channel;
  - their pricing and formats;
  - what non-customers use instead.
- **Fallback:** web search plus reading competitors' public pages; mark the result `demo`.
- **Feeds:** Blue Ocean, business model, PLG.

### Content and CMS
- **Tools:** a WordPress or other CMS connector, a sitemap.
- **Queries:**
  - post and page counts by type and language;
  - categories and their sizes;
  - empty or test pages;
  - active and inactive plugins (analytics, forms, newsletter, search, SEO);
  - the pages that sell (pricing, advertising, contact).
- **Watch for:**
  - an inactive analytics or search plugin means its data is `no`, not zero;
  - large off-topic pages bring traffic the buyer does not value.
- **Feeds:** service design, reliability, JTBD, Kaizen.

### Support and feedback
- **Tools:** Intercom, Zendesk, Front, Help Scout, app store reviews, NPS tools, comments.
- **Queries:**
  - top ticket reasons for the last 90 days;
  - time to first reply;
  - repeated bugs;
  - review themes, with 2-3 short quotes.
- **Fallback:** the owner's summary.
- **Feeds:** discovery, service design, Kaizen.

### Sales and CRM
- **Tools:** HubSpot, Salesforce, Pipedrive, a deals spreadsheet, notes on lost deals.
- **Queries:**
  - stages and conversion between them;
  - loss reasons;
  - time from first contact to deal;
  - share of revenue from the largest client.
- **Fallback:** ask "what already happened" in step 0.5; one sentence about lost deals is often the strongest evidence.
- **Feeds:** JTBD, discovery, business model.

### Experiments and flags
- **Tools:** GrowthBook, LaunchDarkly, Optimizely, VWO.
- **Queries:** past tests with their results and what was learned.
- **Feeds:** CRO, reliability.

### Monitoring and reliability
- **Tools:** Sentry, Datadog, a status page, uptime checks, PageSpeed Insights.
- **Queries:**
  - error rate on critical paths;
  - incidents in the last 90 days;
  - Core Web Vitals.
- **Feeds:** reliability.

### Social channels
- **Tools:** platform analytics (Telegram, YouTube, Instagram) or the owner's screenshots.
- **Queries:**
  - subscribers;
  - reach per post;
  - clicks to the site.
- **Feeds:** growth loops (external trigger), JTBD for advertisers.

## Recording numbers

For every number you use, keep the metric definition, the period, the source and known gaps. A number in a KPI must name its source (`src` in `audit.json`), and that source must not be marked `no`.
