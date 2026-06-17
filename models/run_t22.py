"""Run the T22 D1 physical reduction map audit."""

from __future__ import annotations

import json

from models.d1_physical_reduction_map import run_t22_analysis


def main() -> None:
    print(json.dumps(run_t22_analysis(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
