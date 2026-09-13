"""Task de Inspect para la familia 1 (triage de artefactos) y para los
ítems de control. Uso:

    inspect eval tasks/triage.py --model anthropic/claude-sonnet-5 \
        -T jsonl_path=data/items/control.jsonl
"""

from pathlib import Path

from inspect_ai import Task, task
from inspect_ai.solver import generate

from common import agent_forensics_scorer
from loader import load_jsonl_as_samples

PROJ = Path(__file__).resolve().parents[1]


@task
def triage(jsonl_path: str = "data/items/control.jsonl", judge_model: str | None = None) -> Task:
    path = Path(jsonl_path)
    if not path.is_absolute():
        path = PROJ / path
    return Task(
        dataset=load_jsonl_as_samples(path),
        solver=generate(),
        scorer=agent_forensics_scorer(judge_model=judge_model),
    )
