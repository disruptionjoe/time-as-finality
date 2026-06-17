"""Run the T16 spacetime aggregation toy model."""

from __future__ import annotations

import json

from models.spacetime_aggregation import run_t16_analysis


def main() -> None:
    print(json.dumps(run_t16_analysis(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
