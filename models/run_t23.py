"""Run the T23 invariant-preserving transformations lab."""

from __future__ import annotations

import json

from models.invariant_preserving_transformations import run_t23_analysis


def main() -> None:
    print(json.dumps(run_t23_analysis(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
