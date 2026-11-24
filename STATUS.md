# Status

Living state of the work. Update at the end of every session. Public repo: no real site names, client data or private links here.

**Version:** 1.3.0 (2026-11-24)

## Done recently

- Hands-off output for AI agents: `build_handoff.py` → `handoff.md` + `tasks.json`, tasks ordered by ICE with dependencies first.
- Rule: audit only the production domain, not subdomains found via search.
- Report data-driven from one JSON block; schema, validate/build scripts; uk/en labels; "no data" states; overlap and overflow checks in `check_report.py`.
- Test runs: media sites (2), B2B logistics site with full GA4/GSC access, B2B SaaS + its main competitor (public data only). See `evals/results.md`.

## In progress

- Nothing open in this repo.

## Next

1. Maintainer: create git tags v1.0.0–v1.3.0 and a GitHub Release (the session cannot push tags).
2. Test in Claude Code desktop and in the Claude app (upload the ZIP).
3. Run trigger evals from `evals/trigger-evals.json` with the skill-creator skill.
4. Test on e-commerce, a mobile app (screenshots only) and a marketplace.
5. Product + competitor mode: audit both and use the competitor as a benchmark.
6. Add reviews (G2, Trustpilot, app stores) and Tranco to `references/data-sources.md`.

## Open questions

- Which real site becomes the public case study (owner consent needed)?
- Move the shared report core into its own repo once 2–3 sibling skills exist?

## Links

- Public demos: EN https://claude.ai/artifact/FyKs3ePt4fFF1xNWq3QDah · UA https://claude.ai/artifact/NF3ziLaGy95NQbqDwN6AAJ
- Roadmap and ideas: kept in the maintainer's private plan doc.
