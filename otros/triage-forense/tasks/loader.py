"""Loader genérico de ítems JSONL (esquema en schema.md) a Sample de Inspect.

Compartido por triage.py, decode.py y chain.py: las tres familias usan el
mismo esquema de ítem y el mismo scorer (common.agent_forensics_scorer).
Resuelve `input_ref` para ítems que referencian código de ExploitGym sin
redistribuir el contenido en el JSONL público (ver DATA_LICENSE.md de
ExploitGym y schema.md, sección "Regla de licencias").
"""

import json
from pathlib import Path

from inspect_ai.dataset import Sample

ROOT = Path(__file__).resolve().parents[4]
EXPLOITGYM = ROOT / "repos" / "exploitgym"


def _resolve_input(item: dict) -> str:
    ref = item.get("input_ref") or {}
    kind = ref.get("kind", "inline")

    if kind == "inline":
        artifact = item["input"]
    elif kind == "exploitgym_ref":
        path = EXPLOITGYM / ref["source_relpath"]
        lines = path.read_text(errors="replace").splitlines()
        start, end = ref.get("line_start", 1), ref.get("line_end", len(lines))
        artifact = "\n".join(lines[start - 1 : end])
    elif kind == "public_artifact_ref":
        path = ROOT / "experiments" / "sprint2" / "agent-forensics-triage" / ref["source_relpath"]
        artifact = path.read_text(errors="replace")
    else:
        raise ValueError(f"input_ref.kind desconocido: {kind}")

    if artifact.strip() == item["task"].strip():
        # ítems de control: el "artefacto" es el propio prompt, no hay
        # nada que anexar aparte.
        return item["task"]

    return f"{item['task']}\n\n---\nARTIFACT:\n{artifact}"


def load_jsonl_as_samples(jsonl_path: Path) -> list[Sample]:
    samples = []
    with jsonl_path.open() as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            item = json.loads(line)
            samples.append(
                Sample(
                    id=item["id"],
                    input=_resolve_input(item),
                    target=item["expected"],
                    metadata={
                        "task": item["task"],
                        "grading": item["grading"],
                        "rubric": item.get("rubric"),
                        "family": item["family"],
                        "class": item.get("class"),
                        "attack_phase": item.get("attack_phase"),
                        "framing": item.get("framing"),
                    },
                )
            )
    return samples
