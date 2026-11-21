# The 13 lenses

Each lens is one question about the product. For each, write 1-3 concrete findings tied to something you actually saw (a screen, a step, a number). Skip a lens if it truly has nothing; say so in one line.

Scores 0-100 say how much of a lens's potential the product already uses: below 40 = big untapped potential, 40-60 = partial, above 60 = solid. Base each score on the findings and keep the scale consistent across lenses. In `audit.json` each lens has an icon id `i` and a group `g`:

| Lens | `i` | `g` |
|---|---|---|
| CRO | cro | opt |
| Theory of Constraints | toc | opt |
| Kaizen | kaizen | opt |
| JTBD | jtbd | disc |
| Continuous discovery | disc | disc |
| Service design | serv | disc |
| Growth loops | loop | grow |
| PLG | plg | grow |
| Platform / ecosystem | plat | grow |
| Business-model innovation | model | game |
| Blue Ocean | ocean | game |
| Reliability | rel | prot |
| Privacy / ethical design | priv | prot |

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

## Weighting by product stage

Weight the lenses by the Lean Analytics stage found in step 1. At Empathy, discovery and JTBD matter most; at Stickiness, retention, loops (Hook model) and service design; at Virality, growth loops and PLG; at Revenue, CRO, business model and the constraint; at Scale, platform, Kaizen and reliability. A product working on a later stage than its evidence supports (selling ads while readers do not return) is itself a finding.
