"""Run the T25 minimal D1 generalization audit."""

from __future__ import annotations

import json

from models.minimal_d1_generalization import run_t25_analysis


def main() -> None:
    print(json.dumps(run_t25_analysis(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
