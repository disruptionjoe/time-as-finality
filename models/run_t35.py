"""Runner for T35: Projection-Obstruction Discovery Engine."""

from __future__ import annotations

import json

from models.projection_obstruction_discovery import run_t35_analysis


def main() -> None:
    print(json.dumps(run_t35_analysis(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
