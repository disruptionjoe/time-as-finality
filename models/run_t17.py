"""Run the T17 consensus finality crosswalk."""

from __future__ import annotations

import json

from models.consensus_finality_crosswalk import run_t17_analysis


def main() -> None:
    print(json.dumps(run_t17_analysis(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
