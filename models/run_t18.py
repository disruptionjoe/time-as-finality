"""Run the T18 finality direction theorem check."""

from __future__ import annotations

import json

from models.finality_direction_theorem import run_t18_analysis


def main() -> None:
    print(json.dumps(run_t18_analysis(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
