# product-lens-audit — notes for Claude and contributors

A public Claude skill (Claude Code plugin + Claude app skill ZIP) that audits a digital product through 13 strategy lenses and outputs two files from one `audit.json`: a visual HTML report for people and a Markdown hands-off brief for AI agents.

Start every session by reading this file and `STATUS.md`, then continue from "Next" in `STATUS.md`. End every session by updating `STATUS.md` and committing.

## Layout

```
.claude-plugin/marketplace.json        this repo is a plugin marketplace
plugins/product-lens-audit/            the only folder that ships to users
  .claude-plugin/plugin.json
  skills/product-lens-audit/
    SKILL.md                           the process Claude follows
    references/                        lenses, data sources, report spec, audit.schema.json
    assets/                            report-template.html, example audits, example hands-off
    scripts/                           validate_audit, build_report, build_handoff, check_report
evals/                                 scenarios, trigger prompts, results log (anonymised)
docs/                                  README screenshots
product-lens-audit-skill.zip           Claude app upload, rebuilt on every skill change
CLAUDE.md, STATUS.md, CHANGELOG.md     repo docs; never move them into plugins/
```

## Rules

- Respond to the maintainer in Ukrainian; code, docs and commits in English.
- Never invent numbers. Missing data shows as "no data" and lowers confidence.
- Audit only the production domain the user names; ignore other subdomains found via search unless the user confirms they are live.
- Real audits stay private (artifacts or local files). Nothing in this repo may name a real audited site, client data or private links; log runs in `evals/results.md` anonymised.
- Public demos use fictional products only.
- Claude writes only `audit.json`; the template and scripts render everything. Change the template, not the data, when layout breaks.
- Keep `SKILL.md` short; details go to `references/`.
- Use connected data sources read-only. Never submit real forms, payments or messages.

## Build and check

```
S=plugins/product-lens-audit/skills/product-lens-audit
python $S/scripts/validate_audit.py audit.json
python $S/scripts/build_report.py audit.json report.html
python $S/scripts/build_handoff.py audit.json handoff.md --json tasks.json
python $S/scripts/check_report.py report.html --out ./report-check   # needs playwright + Chromium
```

Before committing a template or script change, run all four on both `assets/example-audit.json` and `assets/example-audit.en.json`, and check that a deliberately broken input fails.

## Release

1. Bump the version in `.claude-plugin/marketplace.json` and `plugins/product-lens-audit/.claude-plugin/plugin.json`.
2. Add a section to `CHANGELOG.md` (user-facing changes only).
3. Rebuild the ZIP: `cd plugins/product-lens-audit/skills && zip -qr ../../../product-lens-audit-skill.zip product-lens-audit -x '*/__pycache__/*'`
4. `claude plugin validate .`
5. Commit, push; tags and GitHub releases are created by the maintainer.

## Related repos

Same report core and design: `seo-audit`, `qa-audit`, `ui-review`, `ux-review`, `competitor-teardown` (all under github.com/artemhorbenko). Shared core changes are made here first, then copied.
