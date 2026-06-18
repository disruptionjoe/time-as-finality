"""Run the T2 quantum measurement finality lab."""

from __future__ import annotations

import json

from models.quantum_measurement_finality import run_t2_analysis


def main() -> None:
    print(json.dumps(run_t2_analysis(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
