"""Run the T20 consensus-record theorem transfer lab."""

from __future__ import annotations

import json

from models.consensus_record_theorem_transfer import run_t20_analysis


def main() -> None:
    print(json.dumps(run_t20_analysis(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
