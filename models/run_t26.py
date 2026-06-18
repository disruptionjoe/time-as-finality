"""Run the T26 D1 restriction-system formalization."""

from __future__ import annotations

import json

from models.d1_restriction_system import run_t26_analysis


def main() -> None:
    print(json.dumps(run_t26_analysis(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
