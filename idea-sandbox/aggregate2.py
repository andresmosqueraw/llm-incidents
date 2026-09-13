#!/usr/bin/env python3
"""Agrega los veredictos del panel de diseño. Lee, cuenta y tabula; no reinterpreta."""
from __future__ import annotations
import json, re, statistics, sys
from pathlib import Path

DIR = Path(sys.argv[1] if len(sys.argv) > 1 else "/home/daw/Sprint/idea-sandbox")
VDIR = DIR / "veredictos"


def extract_json(text: str):
    m = re.search(r"##\s*VEREDICTO_JSON(.*)", text, flags=re.S)
    blob = m.group(1) if m else text
    cand = [f.group(1) for f in re.finditer(r"```(?:json)?\s*(.*?)```", blob, flags=re.S)]
    depth = 0; start = None
    for i, ch in enumerate(blob):
        if ch == "{":
            if depth == 0: start = i
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0 and start is not None:
                cand.append(blob[start:i + 1])
    for c in cand:
        for attempt in (c, re.sub(r",\s*([}\]])", r"\1", re.sub(r"^\s*//.*$", "", c, flags=re.M))):
            try:
                return json.loads(attempt)
            except Exception:
                continue
    return None


def num(v):
    try: return float(v)
    except Exception: return None


def main() -> int:
    rows, mejoras, pre, refut, mvi, gng = [], [], [], [], [], []
    parseados = 0
    for path in sorted(VDIR.glob("*.md")):
        d = extract_json(path.read_text(encoding="utf-8", errors="replace"))
        if not d:
            print(f"!! no parseable: {path.name}")
            continue
        parseados += 1
        rows.append({
            "juez": str(d.get("juez") or path.stem), "rol": str(d.get("rol") or ""),
            "veredicto": str(d.get("veredicto_global") or ""),
            "razon": str(d.get("razon_en_una_frase") or "")[:300],
            "D1": num(d.get("D1")), "D2": num(d.get("D2")), "D3": num(d.get("D3")),
            "fatal": str(d.get("objecion_fatal") or "")[:500],
            "una_medicion": str(d.get("que_mediria_yo_en_su_lugar") or "")[:300],
            "dual": str(d.get("riesgo_uso_dual") or "")[:300],
        })
        for m in d.get("mejoras_concretas") or []:
            mejoras.append((str(d.get("juez")), str(m)[:400]))
        for p in d.get("preregistro_imprescindible") or []:
            pre.append((str(d.get("juez")), str(p)[:300]))
        for h in d.get("hechos_refutados") or []:
            if isinstance(h, dict) and (h.get("hecho") or h.get("problema")):
                refut.append({"juez": str(d.get("juez")), **{k: str(v)[:300] for k, v in h.items()}})
        v = d.get("diseno_minimo_viable") or {}
        if v:
            mvi.append({"juez": str(d.get("juez")), **{k: (str(x)[:120]) for k, x in v.items()}})
        g = str(d.get("criterio_go_no_go") or "")
        if g: gng.append((str(d.get("juez")), g[:300]))

    d1 = [r["D1"] for r in rows if r["D1"] is not None]
    d2 = [r["D2"] for r in rows if r["D2"] is not None]
    d3 = [r["D3"] for r in rows if r["D3"] is not None]
    vc: dict[str, int] = {}
    for r in rows:
        vc[r["veredicto"]] = vc.get(r["veredicto"], 0) + 1

    o = ["# AGREGADO DEL PANEL DE DISEÑO\n",
         f"Jueces con veredicto: {parseados}/{len(list(VDIR.glob('*.md')))}\n",
         f"Veredictos: {vc}",
         "Medias -> D1 %.2f | D2 %.2f | D3 %.2f\n" % (
             statistics.mean(d1) if d1 else -1, statistics.mean(d2) if d2 else -1,
             statistics.mean(d3) if d3 else -1)]
    o.append("\n## 1. Juez por juez\n")
    o.append("| juez | rol | veredicto | D1 | D2 | D3 |")
    o.append("|---|---|---|---|---|---|")
    for r in rows:
        o.append(f"| {r['juez']} | {r['rol']} | {r['veredicto']} | {r['D1']} | {r['D2']} | {r['D3']} |")
    o.append("\n### Razón en una frase\n")
    for r in rows:
        o.append(f"- **{r['juez']}**: {r['razon']}")
    o.append("\n## 2. Objeción fatal de cada juez\n")
    for r in rows:
        o.append(f"### {r['juez']} ({r['rol']})\n{r['fatal']}\n")
    o.append("## 3. Mejoras concretas al diseño\n")
    for j, m in mejoras:
        o.append(f"- [{j}] {m}")
    o.append("\n## 4. Preregistro imprescindible\n")
    for j, p in pre:
        o.append(f"- [{j}] {p}")
    o.append("\n## 5. Diseño mínimo viable propuesto\n")
    for v in mvi:
        o.append(f"- **{v['juez']}**: agentes/corrida {v.get('agentes_por_corrida','')}, corridas {v.get('corridas','')}, "
                 f"tokens {v.get('tokens_estimados','')}, horas {v.get('horas','')}. Recorta primero: {v.get('se_recorta_primero','')}")
    o.append("\n## 6. Criterio go/no-go del piloto\n")
    for j, g in gng:
        o.append(f"- **{j}**: {g}")
    o.append("\n## 7. Uso dual, según los jueces\n")
    for r in rows:
        o.append(f"- **{r['juez']}**: {r['dual']}")
    o.append("\n## 8. La medición que cada juez elegiría\n")
    for r in rows:
        o.append(f"- **{r['juez']}**: {r['una_medicion']}")
    o.append("\n## 9. Hechos del expediente refutados\n")
    if not refut:
        o.append("Ninguno reportado.")
    for h in refut:
        o.append(f"- [{h.get('juez')}] {h.get('hecho','')} :: {h.get('problema','')} :: {h.get('fuente','')}")

    texto = "\n".join(o)
    (DIR / "AGREGADO.md").write_text(texto, encoding="utf-8")
    print(texto)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
