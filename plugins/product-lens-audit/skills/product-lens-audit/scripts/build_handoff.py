#!/usr/bin/env python3
"""Turn an audit.json into a hands-off file for an AI agent or a developer.

Usage: python build_handoff.py audit.json handoff.md [--json tasks.json]

The report page is for people; this file is for whoever implements the plan.
Plain Markdown, no design: context, sources, constraints, then one task per
opportunity in priority order with evidence, steps, acceptance criteria and a
way to verify. Optional tasks.json carries the same tasks for a tracker.
Standard library only.
"""
import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from validate_audit import validate  # noqa: E402

TOKENS = re.compile(r"\{(health|qw|n|conf)\}")
L = {
    "en": dict(title="Hands-off", intro="Implementation brief generated from the audit. Work top to bottom: tasks are ordered by ICE, and a task always comes after the ones it depends on. Treat \"hypothesis\" tasks as experiments: test before building fully.",
               context="Context", finding="Main finding", stage="Product stage", answers="Owner answers and assumptions", skipped="skipped",
               sources="Data sources", missing="Missing, so lower confidence", rules="Rules for the implementer", tasks="Tasks",
               order="Suggested order", type_o="optimize", type_x="explore", ev_o="observed", ev_h="hypothesis",
               lens="Lens", ice="ICE", type="Type", evidence="Evidence", why="Evidence", steps="Steps", accept="Acceptance criteria",
               verify="How to verify", metric="Metric", effort="Effort", risk="Risk / guardrail", alt="Alternatives rejected",
               pm="Pre-mortem", hypo="Hypothesis", copy="Copy variants", top="top 3", dep="Depends on", task="Task", conf="Confidence", glossary="Glossary",
               stages=["Empathy", "Stickiness", "Virality", "Revenue", "Scale"],
               default_rules=["Do not invent numbers. If a metric cannot be measured yet, add the tracking first.",
                              "Do not submit real forms, payments or messages while testing.",
                              "Do not change URLs that already rank without a 301 redirect.",
                              "Keep each change small and measurable; record before/after values.",
                              "When a task is a hypothesis, run the cheapest test first and stop if the threshold is not met."]),
    "uk": dict(title="Hands-off", intro="Бриф на впровадження, згенерований з аудиту. Ідіть згори донизу: задачі впорядковано за ICE, і кожна стоїть після тих, від яких залежить. Задачі з позначкою «гіпотеза» — це експерименти: спершу перевірка, потім повна реалізація.",
               context="Контекст", finding="Головна знахідка", stage="Етап продукту", answers="Відповіді власника й припущення", skipped="пропущено",
               sources="Джерела даних", missing="Бракує, тому впевненість нижча", rules="Правила для виконавця", tasks="Задачі",
               order="Рекомендований порядок", type_o="оптимізація", type_x="дослідження", ev_o="спостережено", ev_h="гіпотеза",
               lens="Лінза", ice="ICE", type="Тип", evidence="Доказ", why="Доказ", steps="Кроки", accept="Критерії приймання",
               verify="Як перевірити", metric="Метрика", effort="Зусилля", risk="Ризик / запобіжник", alt="Відкинуті альтернативи",
               pm="Pre-mortem", hypo="Гіпотеза", copy="Варіанти тексту", top="топ-3", dep="Залежить від", task="Задача", conf="Впевненість", glossary="Глосарій",
               stages=["Емпатія", "Утримання", "Вірусність", "Дохід", "Масштаб"],
               default_rules=["Не вигадувати цифр. Якщо метрику ще не можна виміряти, спершу додати вимірювання.",
                              "Не відправляти справжні форми, платежі чи повідомлення під час тестів.",
                              "Не змінювати URL, що вже мають позиції, без 301-редиректу.",
                              "Робити зміни малими й вимірюваними; записувати значення до й після.",
                              "Якщо задача — гіпотеза, спершу найдешевший тест; зупинитися, якщо поріг не досягнуто."]),
}


def clean(s, ctx):
    s = TOKENS.sub(lambda m: str(ctx.get(m.group(1), m.group(0))), str(s))
    return s.replace("[[", "**").replace("]]", "**")


def build(a):
    lang = (a.get("lang") or "en")[:2]
    t = L.get(lang, L["en"])
    ops = a.get("ops") or []
    detail, plans = a.get("detail") or {}, a.get("plans") or {}
    lenses = a.get("lenses") or []
    sources = a.get("sources") or []
    health = round(sum(l.get("s", 0) for l in lenses) / len(lenses)) if lenses else 0
    conf = round(sum({"ok": 1, "demo": .6}.get(s.get("status"), 0) for s in sources) / len(sources) * 100) if sources else 0
    qw = sum(1 for o in ops if o.get("I", 0) >= 6 and 11 - o.get("E", 0) <= 5)
    ctx = dict(health=health, qw=qw, n=len(ops), conf=conf)
    text = a.get("text") or {}

    tasks = []
    for i, o in enumerate(ops, 1):
        d = detail.get(str(i), {})
        p = plans.get(str(i), {})
        accept = list(d.get("accept") or [])
        if not accept:
            if d.get("thr"):
                accept.append(d["thr"])
            if d.get("metric"):
                accept.append(f"{t['metric']}: {d['metric']}")
        tasks.append(dict(
            id=f"T{i:02d}", n=i, title=o.get("t"), lens=o.get("ln"), lens_id=o.get("l"),
            type="explore" if o.get("x") == "ex" else "optimize",
            evidence_type="hypothesis" if o.get("ev") == "hyp" else "observed",
            impact=o.get("I"), confidence=o.get("C"), ease=o.get("E"),
            ice=o.get("I", 0) * o.get("C", 0) * o.get("E", 0),
            evidence=d.get("why", ""), steps=d.get("steps") or [], acceptance=accept,
            verify=p.get("t") or (d.get("verify") or ""), hypothesis=p.get("h", ""),
            metric=d.get("metric", ""), effort=d.get("effort", ""), risk=d.get("risk", ""),
            alternatives=d.get("alt") or [], risk_type=d.get("rtype", ""), pre_mortem=d.get("pm", ""),
            copy=d.get("copy") or [], depends_on=d.get("depends") or [],
        ))
    tasks.sort(key=lambda x: (-x["ice"], x["n"]))
    # dependencies first: a task never comes before what it depends on
    by_id, done, ordered = {tk["id"]: tk for tk in tasks}, set(), []
    def place(tk, seen=()):
        if tk["id"] in done or tk["id"] in seen:
            return
        for dep in tk["depends_on"]:
            if dep in by_id:
                place(by_id[dep], seen + (tk["id"],))
        done.add(tk["id"])
        ordered.append(tk)
    for tk in tasks:
        place(tk)
    tasks = ordered
    for rank, tk in enumerate(tasks, 1):
        tk["rank"] = rank

    out = []
    w = out.append
    w(f"# {t['title']}: {a.get('title', '')}".rstrip(": "))
    w("")
    w(t["intro"])
    w("")
    w(f"## {t['context']}")
    w("")
    if text.get("headline"):
        w(f"- **{t['finding']}:** {clean(text['headline'], ctx).replace('**', '')}")
    if text.get("lead"):
        w(f"- {clean(text['lead'], ctx)}")
    st = a.get("stage")
    if st:
        w(f"- **{t['stage']}:** {t['stages'][st.get('cur', 0)]}. {st.get('note', '')}")
    w(f"- **{t['conf']}:** {conf}%")
    w("")
    if a.get("answers"):
        w(f"### {t['answers']}")
        w("")
        for q in a["answers"]:
            mark = f" ({t['skipped']})" if q.get("skipped") else ""
            w(f"- {q.get('q')}{mark}: {q.get('a')}")
        w("")
    if sources:
        w(f"### {t['sources']}")
        w("")
        for s in sources:
            w(f"- [{s.get('status')}] {s.get('name')}" + (f" — {s['note']}" if s.get("note") else ""))
        miss = [s.get("name") for s in sources if s.get("status") == "no"]
        if miss:
            w("")
            w(f"{t['missing']}: {', '.join(miss)}.")
        w("")
    w(f"## {t['rules']}")
    w("")
    for r in (a.get("rules") or t["default_rules"]):
        w(f"- {r}")
    w("")
    w(f"## {t['order']}")
    w("")
    w(f"| # | ID | {t['task']} | {t['ice']} | {t['type']} | {t['evidence']} |")
    w("|---|---|---|---|---|---|")
    for tk in tasks:
        top = f" ({t['top']})" if tk["rank"] <= 3 else ""
        w(f"| {tk['rank']} | {tk['id']} | {tk['title']}{top} | {tk['ice']} | {t['type_x'] if tk['type'] == 'explore' else t['type_o']} | {t['ev_h'] if tk['evidence_type'] == 'hypothesis' else t['ev_o']} |")
    w("")
    w(f"## {t['tasks']}")
    for tk in tasks:
        w("")
        w(f"### {tk['rank']}. {tk['id']} — {tk['title']}")
        w("")
        w(f"- {t['lens']}: {tk['lens']} · {t['ice']} {tk['ice']} = {tk['impact']}×{tk['confidence']}×{tk['ease']} · {t['type']}: {t['type_x'] if tk['type'] == 'explore' else t['type_o']} · {t['ev_h'] if tk['evidence_type'] == 'hypothesis' else t['ev_o']}")
        if tk["effort"]:
            w(f"- {t['effort']}: {tk['effort']}")
        if tk["depends_on"]:
            w(f"- {t['dep']}: {', '.join(tk['depends_on'])}")
        w("")
        if tk["evidence"]:
            w(f"**{t['why']}.** {tk['evidence']}")
            w("")
        if tk["hypothesis"]:
            w(f"**{t['hypo']}.** {tk['hypothesis']}")
            w("")
        if tk["steps"]:
            w(f"**{t['steps']}:**")
            w("")
            for j, s in enumerate(tk["steps"], 1):
                w(f"{j}. {s}")
            w("")
        if tk["acceptance"]:
            w(f"**{t['accept']}:**")
            w("")
            for c in tk["acceptance"]:
                w(f"- [ ] {c}")
            w("")
        if tk["verify"]:
            w(f"**{t['verify']}:** {tk['verify']}")
            w("")
        if tk["risk"]:
            w(f"**{t['risk']}:** {tk['risk']}")
            w("")
        if tk["alternatives"]:
            w(f"**{t['alt']}:**")
            w("")
            for x in tk["alternatives"]:
                w(f"- {x}")
            w("")
        if tk["pre_mortem"]:
            w(f"**{t['pm']}:** {tk['pre_mortem']}")
            w("")
        if tk["copy"]:
            w(f"**{t['copy']}:**")
            w("")
            for x in tk["copy"]:
                w(f"- {x}")
            w("")
    gl = a.get("glossary") or {}
    if gl:
        w(f"## {t['glossary']}")
        w("")
        for k, v in gl.items():
            w(f"- **{k}** ({v.get('g')}): {v.get('d')}")
        w("")
    return "\n".join(out).rstrip() + "\n", tasks


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("audit")
    ap.add_argument("out")
    ap.add_argument("--json", help="also write tasks as JSON for a tracker")
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()
    with open(a.audit, encoding="utf-8") as f:
        audit = json.load(f)
    err, _ = validate(audit)
    if err and not a.force:
        for e in err:
            print("[ERROR]", e)
        print("Not built. Fix audit.json or pass --force.")
        return 1
    md, tasks = build(audit)
    with open(a.out, "w", encoding="utf-8") as f:
        f.write(md)
    if a.json:
        with open(a.json, "w", encoding="utf-8") as f:
            json.dump({"title": audit.get("title"), "lang": audit.get("lang"), "tasks": tasks}, f, ensure_ascii=False, indent=1)
    print(f"Written {a.out} ({len(tasks)} tasks)" + (f" and {a.json}" if a.json else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
