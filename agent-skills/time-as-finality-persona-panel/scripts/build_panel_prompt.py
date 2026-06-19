"""Build a reusable Time as Finality persona-panel prompt.

The script reads the repo-local persona reference and emits a prompt that can
be pasted into Codex or another agent runner. It does not call any model.
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
REPO_ROOT = SKILL_DIR.parents[1]
PERSONA_REF = SKILL_DIR / "references" / "personas.md"

FOCUSED_DEFAULT = (1, 2, 4, 7, 9, 10, 22, 23, 25, 50, 51, 52, 54)
HOSTILE_DEFAULT = (25, 27, 42, 50, 52, 54)
GEOMETRY_GU_DEFAULT = (1, 3, 4, 5, 6, 45, 46, 47, 48, 49, 50, 52)
DISTRIBUTED_DEFAULT = (9, 10, 12, 13, 22, 23, 24, 34, 35, 38, 39, 50, 54)


@dataclass(frozen=True)
class Persona:
    number: int
    name: str
    description: str


def parse_personas(reference_path: Path = PERSONA_REF) -> dict[int, Persona]:
    """Parse persona headings from references/personas.md."""

    text = reference_path.read_text(encoding="utf-8")
    pattern = re.compile(
        r"^### (?P<number>\d+)\. (?P<name>.+?)\n\n(?P<description>.*?)(?=\n### |\n## |\Z)",
        re.MULTILINE | re.DOTALL,
    )
    personas: dict[int, Persona] = {}
    for match in pattern.finditer(text):
        number = int(match.group("number"))
        description = " ".join(match.group("description").strip().split())
        personas[number] = Persona(
            number=number,
            name=match.group("name").strip(),
            description=description,
        )
    if len(personas) != 54:
        raise ValueError(f"expected 54 personas, found {len(personas)}")
    return personas


def parse_persona_numbers(raw: str, known: dict[int, Persona]) -> tuple[int, ...]:
    """Parse comma-separated persona numbers."""

    if not raw.strip():
        raise ValueError("--personas cannot be blank")
    numbers: list[int] = []
    for item in raw.split(","):
        item = item.strip()
        if not item:
            continue
        number = int(item)
        if number not in known:
            raise ValueError(f"unknown persona number: {number}")
        numbers.append(number)
    if not numbers:
        raise ValueError("no persona numbers selected")
    return tuple(dict.fromkeys(numbers))


def selected_numbers(args: argparse.Namespace, known: dict[int, Persona]) -> tuple[int, ...]:
    """Resolve CLI selection options to persona numbers."""

    selection_count = sum(
        bool(value)
        for value in (
            args.all,
            args.focused,
            args.hostile,
            args.geometry_gu,
            args.distributed,
            args.personas,
        )
    )
    if selection_count > 1:
        raise ValueError("choose only one persona selection mode")
    if args.all:
        return tuple(sorted(known))
    if args.hostile:
        return HOSTILE_DEFAULT
    if args.geometry_gu:
        return GEOMETRY_GU_DEFAULT
    if args.distributed:
        return DISTRIBUTED_DEFAULT
    if args.personas:
        return parse_persona_numbers(args.personas, known)
    return FOCUSED_DEFAULT


def render_persona_block(numbers: tuple[int, ...], known: dict[int, Persona]) -> str:
    """Render selected personas into prompt text."""

    lines: list[str] = []
    for number in numbers:
        persona = known[number]
        lines.append(f"{persona.number}. {persona.name}: {persona.description}")
    return "\n".join(lines)


def build_prompt(args: argparse.Namespace) -> str:
    """Build the full panel prompt."""

    known = parse_personas()
    numbers = selected_numbers(args, known)
    persona_block = render_persona_block(numbers, known)
    focus = args.focus.strip() if args.focus else "Evaluate the supplied Time as Finality question."
    mode = args.mode

    return f"""Use the Time as Finality Persona Panel.

Repo root:
{REPO_ROOT}

Skill reference:
{SKILL_DIR}

Mode:
{mode}

Task / focus:
{focus}

Selected personas:
{persona_block}

Instructions:
1. Each selected persona must work independently before synthesis.
2. Each persona should assume the idea may be wrong or overclaimed.
3. Each persona must answer in this structure:
   - Summary of understanding
   - Strongest insight
   - Strongest criticism
   - Hidden assumptions
   - Rose
   - Bud
   - Thorn
   - Confidence (1-10)
   - Suggested experiment
   - Suggested theorem or mathematical direction
   - Suggested falsification test
4. After independent responses, synthesize:
   - convergences
   - disagreements
   - strongest warning
   - strongest next executable goal
   - claim-status recommendation
5. If voting is useful, use quadratic voting:
   - each persona has 100 points
   - vote cost is intensity squared
   - intensity is 1-10
6. Do not promote claims beyond repo evidence.
7. Classify cross-domain relationships as analogy, homology, reduction, or equivalence.
"""


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--focus", help="Question, claim, or goal for the panel to evaluate.")
    parser.add_argument(
        "--mode",
        default="audit",
        choices=("audit", "goal", "steelman", "hostile", "synthesis"),
        help="Panel mode to state in the generated prompt.",
    )
    parser.add_argument("--all", action="store_true", help="Use all 54 personas.")
    parser.add_argument("--focused", action="store_true", help="Use the default focused subset.")
    parser.add_argument("--hostile", action="store_true", help="Use the hostile overclaim subset.")
    parser.add_argument("--geometry-gu", action="store_true", help="Use the geometry/GU subset.")
    parser.add_argument("--distributed", action="store_true", help="Use the distributed/record-access subset.")
    parser.add_argument("--personas", help="Comma-separated persona numbers, for example 1,4,9,50.")
    parser.add_argument("--output", help="Optional path to write the prompt.")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    prompt = build_prompt(args)
    if args.output:
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(prompt, encoding="utf-8")
        print(f"Wrote persona-panel prompt to {output}")
    else:
        print(prompt)


if __name__ == "__main__":
    main()
