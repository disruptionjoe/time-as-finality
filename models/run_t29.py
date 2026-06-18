"""Run the T29 Projection-Obstruction Schema formalization."""

from __future__ import annotations

import json

from models.projection_obstruction_schema import run_t29_analysis


def main() -> None:
    print(json.dumps(run_t29_analysis(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
