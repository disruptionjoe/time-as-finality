"""Run the second S6 ambitious-goals suite."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from models.s6_ambitious_goal_suite import run_all_ambitious_goals


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, help="Optional JSON output path.")
    args = parser.parse_args()

    result = run_all_ambitious_goals()
    payload = json.dumps(result, indent=2, sort_keys=True)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload + "\n", encoding="utf-8")
    print(payload)


if __name__ == "__main__":
    main()
