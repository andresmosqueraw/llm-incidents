"""Extrae fragmentos candidatos de ExploitGym para la clase `benchmark_code`
(familia 1 del dataset agent-forensics-triage).

No redistribuye el contenido en el dataset público: escribe un manifiesto
local (gitignored, bajo data/raw/exploitgym/) con task_id, ruta relativa,
rango de líneas, commit y el propio texto extraído para uso interno del
pipeline de construcción. build_family1.py debe copiar al JSONL público
solo task_id + ruta + líneas + commit, nunca el contenido (ver DATA_LICENSE.md
de ExploitGym: kernel GPL-2.0, V8 BSD-3-Clause, CyberGym por proyecto).

Desviación registrada frente al plan: los `poc` de data/tasks/user/cybergym/
son entradas binarias de fuzzing (crash inputs), no código fuente legible
(confirmado con `file` sobre 15 tareas: ar archive, TIFF, PDF, DWG, "data").
Se sustituye esa fuente por data/tasks/v8/human/*/pov/pov.js, que sí son
PoCs de JavaScript legibles y cumplen el mismo rol (código de benchmark que
se podría confundir con una explotación real).
"""

import hashlib
import json
import random
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
EXPLOITGYM = ROOT / "repos" / "exploitgym"
PROJ = Path(__file__).resolve().parents[1]
OUT_DIR = PROJ / "data" / "raw" / "exploitgym"
OUT_DIR.mkdir(parents=True, exist_ok=True)

N_PER_CATEGORY = 5
MIN_LINES = 20
MAX_LINES = 60
SEED = 42


def git_commit() -> str:
    return subprocess.check_output(
        ["git", "-C", str(EXPLOITGYM), "rev-parse", "HEAD"], text=True
    ).strip()


def read_window(path: Path) -> tuple[str, int, int]:
    lines = path.read_text(errors="replace").splitlines()
    end = min(len(lines), MAX_LINES)
    snippet = "\n".join(lines[:end])
    return snippet, 1, end


def collect(glob_pattern: str, category: str, task_id_fn) -> list[dict]:
    candidates = []
    for path in sorted(EXPLOITGYM.glob(glob_pattern)):
        if not path.is_file():
            continue
        try:
            text = path.read_text(errors="replace")
        except Exception:
            continue
        n_lines = len(text.splitlines())
        if n_lines < MIN_LINES:
            continue
        candidates.append(path)
    return candidates


def build_items(commit: str) -> list[dict]:
    rng = random.Random(SEED)
    items = []

    sources = [
        ("kernel/kernelctf/*/docs/exploit.md", "kernelctf_exploit_md"),
        ("kernel/kernelctf/*/pov/pov.c", "kernelctf_pov_c"),
        ("v8/human/*/pov/pov.js", "v8_human_pov_js"),  # sustituye a cybergym/*/poc (binario, no legible)
    ]

    idx = 0
    for glob_pattern, category in sources:
        candidates = collect(f"data/tasks/{glob_pattern}", category, None)
        rng.shuffle(candidates)
        chosen = candidates[:N_PER_CATEGORY]
        for path in chosen:
            snippet, start, end = read_window(path)
            rel = path.relative_to(EXPLOITGYM)
            # el archivo vive en <task_dir>/<docs|pov>/<archivo>
            task_id = rel.parent.parent.name
            idx += 1
            items.append(
                {
                    "candidate_id": f"BC-{idx:03d}",
                    "family": "triage",
                    "class": "benchmark_code",
                    "category": category,
                    "task_id": task_id,
                    "source_relpath": str(rel),
                    "exploitgym_commit": commit,
                    "line_start": start,
                    "line_end": end,
                    "sha256": hashlib.sha256(snippet.encode()).hexdigest(),
                    "content": snippet,
                }
            )
        print(f"{category}: {len(candidates)} candidatos disponibles, {len(chosen)} elegidos")

    return items


def main():
    commit = git_commit()
    items = build_items(commit)
    out_path = OUT_DIR / "benchmark_code_candidates.json"
    out_path.write_text(json.dumps(items, indent=2, ensure_ascii=False))
    print(f"\n{len(items)} fragmentos escritos en {out_path}")
    print("Recordatorio: este archivo es local (gitignored). El JSONL publico")
    print("(data/items/triage.jsonl) debe referenciar solo task_id/ruta/lineas/commit,")
    print("nunca el campo 'content' (licencias upstream GPL-2.0 / BSD-3-Clause / CyberGym).")


if __name__ == "__main__":
    main()
