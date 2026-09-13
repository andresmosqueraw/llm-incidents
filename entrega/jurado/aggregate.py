#!/usr/bin/env python3
"""Agrega los veredictos del panel. No reinterpreta: lee, cuenta y tabula.

Uso: python3 aggregate.py [dir_veredictos]
Salida: informe en stdout + jurado/AGREGADO.md
"""
from __future__ import annotations
import json, re, sys, statistics
from pathlib import Path

DIR = Path(sys.argv[1] if len(sys.argv) > 1 else "/home/daw/Sprint/jurado")
VDIR = DIR / "veredictos"


def extract_json(text: str):
    """Saca el bloque JSON del veredicto, tolerante a vallas, comentarios y comas finales."""
    cand = []
    m = re.search(r"##\s*VEREDICTO_JSON(.*)", text, flags=re.S)
    blob = m.group(1) if m else text
    for f in re.finditer(r"```(?:json)?\s*(.*?)```", blob, flags=re.S):
        cand.append(f.group(1))
    # último recurso: el bloque balanceado más grande que empiece en {
    depth = 0; start = None
    for i, ch in enumerate(blob):
        if ch == "{":
            if depth == 0:
                start = i
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0 and start is not None:
                cand.append(blob[start : i + 1])
    for c in cand:
        for attempt in (c, re.sub(r",\s*([}\]])", r"\1", re.sub(r"^\s*//.*$", "", c, flags=re.M))):
            try:
                return json.loads(attempt)
            except Exception:
                continue
    return None


def num(v):
    try:
        return float(v)
    except Exception:
        return None


def main() -> int:
    rows, missing, calib, props, refuted, finals = [], [], [], [], [], []
    for path in sorted(VDIR.glob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        data = extract_json(text)
        if not data:
            missing.append((path.name, "JSON no parseable"))
            continue
        juez = str(data.get("juez") or path.stem)
        rol = str(data.get("rol") or "")
        cal = data.get("calibracion_C1") or {}
        calib.append(
            {
                "juez": juez, "rol": rol,
                "D1": num(cal.get("D1")), "D2": num(cal.get("D2")), "D3": num(cal.get("D3")),
                "veredicto": str(cal.get("veredicto") or ""),
                "coincide": cal.get("coincide_con_el_rechazo_previo"),
                "objecion": str(cal.get("objecion_fatal") or "")[:300],
            }
        )
        for c in data.get("candidatas") or []:
            rows.append(
                {
                    "juez": juez, "rol": rol, "id": str(c.get("id") or ""),
                    "D1": num(c.get("D1")), "D2": num(c.get("D2")), "D3": num(c.get("D3")),
                    "veredicto": str(c.get("veredicto") or ""),
                    "objecion": str(c.get("objecion_fatal") or "")[:400],
                    "cambiaria": str(c.get("evidencia_que_cambiaria_mi_veredicto") or "")[:300],
                }
            )
        for p in data.get("propias") or []:
            props.append(
                {
                    "juez": juez, "rol": rol, "titulo": str(p.get("titulo") or ""),
                    "que": str(p.get("que_se_construye") or "")[:400],
                    "datos": str(p.get("datos_y_de_donde") or "")[:300],
                    "numero": str(p.get("numero_que_produce") or "")[:200],
                    "no_prueba": str(p.get("no_prueba") or "")[:200],
                    "como_falla": str(p.get("como_falla") or "")[:200],
                    "D1": num(p.get("D1")), "D2": num(p.get("D2")), "D3": num(p.get("D3")),
                }
            )
        for h in data.get("hechos_refutados") or []:
            if isinstance(h, dict) and (h.get("hecho") or h.get("problema")):
                refuted.append({"juez": juez, **{k: str(v)[:300] for k, v in h.items()}})
        rf = data.get("recomendacion_final") or {}
        finals.append({
            "juez": juez, "rol": rol,
            "construir": str(rf.get("construir_esto") or "")[:400],
            "por_que": str(rf.get("por_que") or "")[:400],
            "alcance": str(rf.get("alcance_para_48_horas") or "")[:300],
            "primer_paso": str(rf.get("primer_paso_concreto") or "")[:200],
        })

    # --- agregación por candidata
    by_cand: dict[str, list[dict]] = {}
    for r in rows:
        by_cand.setdefault(r["id"], []).append(r)

    agg = []
    for cid, rs in by_cand.items():
        d1 = [r["D1"] for r in rs if r["D1"] is not None]
        d2 = [r["D2"] for r in rs if r["D2"] is not None]
        d3 = [r["D3"] for r in rs if r["D3"] is not None]
        tot = [sum(x) for x in zip(d1, d2, d3)] if d1 and d2 and d3 and len(d1) == len(d2) == len(d3) else []
        vc: dict[str, int] = {}
        for r in rs:
            vc[r["veredicto"]] = vc.get(r["veredicto"], 0) + 1
        agg.append({
            "id": cid, "n": len(rs),
            "D1": round(statistics.mean(d1), 2) if d1 else None,
            "D2": round(statistics.mean(d2), 2) if d2 else None,
            "D3": round(statistics.mean(d3), 2) if d3 else None,
            "total_medio": round(statistics.mean(tot), 2) if tot else None,
            "veredictos": vc,
            "objeciones": [r["objecion"] for r in rs if r["objecion"]],
        })
    agg.sort(key=lambda a: (a["total_medio"] is None, -(a["total_medio"] or 0)))

    out = []
    out.append("# AGREGADO DEL PANEL\n")
    out.append(f"Veredictos leídos: {len(list(VDIR.glob('*.md')))} | parseados: {len({r['juez'] for r in rows}) if rows else 0} jueces | fallos de parseo: {len(missing)}\n")

    out.append("## 1. Calibración (C1, la propuesta ya rechazada)\n")
    out.append("| juez | rol | D1 | D2 | D3 | veredicto | coincide con el rechazo |")
    out.append("|---|---|---|---|---|---|---|")
    for c in calib:
        out.append(f"| {c['juez']} | {c['rol']} | {c['D1']} | {c['D2']} | {c['D3']} | {c['veredicto']} | {c['coincide']} |")
    rej = sum(1 for c in calib if c["veredicto"] == "rechazar")
    out.append(f"\nRechazan C1: {rej}/{len(calib)}. Si el panel no puede reproducir un rechazo bien argumentado, sus elogios valen poco.\n")

    out.append("## 2. Puntaje por candidata (media del panel)\n")
    out.append("| id | n jueces | D1 | D2 | D3 | total medio | veredictos |")
    out.append("|---|---|---|---|---|---|---|")
    for a in agg:
        out.append(f"| {a['id']} | {a['n']} | {a['D1']} | {a['D2']} | {a['D3']} | {a['total_medio']} | {a['veredictos']} |")

    out.append("\n## 3. Objeciones fatales por candidata\n")
    for a in agg:
        out.append(f"### {a['id']}")
        for o in a["objeciones"]:
            out.append(f"- {o}")
        out.append("")

    out.append("## 4. Propuestas propias de los jueces\n")
    for p in props:
        out.append(f"### {p['titulo']}  ({p['juez']}, D1={p['D1']} D2={p['D2']} D3={p['D3']})")
        out.append(f"- qué: {p['que']}")
        out.append(f"- datos: {p['datos']}")
        out.append(f"- número que produce: {p['numero']}")
        out.append(f"- no prueba: {p['no_prueba']}")
        out.append(f"- cómo falla: {p['como_falla']}\n")

    out.append("## 5. Recomendaciones finales, textuales\n")
    for f in finals:
        out.append(f"### {f['juez']} ({f['rol']})")
        out.append(f"- construir: {f['construir']}")
        out.append(f"- por qué: {f['por_que']}")
        out.append(f"- alcance 48h: {f['alcance']}")
        out.append(f"- primer paso: {f['primer_paso']}\n")

    out.append("## 6. Hechos del expediente refutados por los jueces\n")
    if not refuted:
        out.append("Ninguno reportado.")
    for h in refuted:
        out.append(f"- [{h.get('juez')}] {h.get('hecho','')} :: {h.get('problema','')} :: {h.get('fuente','')}")

    if missing:
        out.append("\n## 7. Veredictos no parseables\n")
        for n, why in missing:
            out.append(f"- {n}: {why}")

    inform = "\n".join(out)
    (DIR / "AGREGADO.md").write_text(inform, encoding="utf-8")
    print(inform)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
