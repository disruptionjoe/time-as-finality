"""Run the T27 GU class-relative no-go bridge audit."""

from __future__ import annotations

import json

from models.gu_class_relative_bridge import run_t27_analysis


def main() -> None:
    print(json.dumps(run_t27_analysis(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
