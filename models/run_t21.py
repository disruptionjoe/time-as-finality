"""Run the T21 Bell/CHSH finality contextuality check."""

from __future__ import annotations

import json

from models.bell_contextuality_finality import run_t21_analysis


def main() -> None:
    print(json.dumps(run_t21_analysis(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
