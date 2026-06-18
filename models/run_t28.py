"""Runner for T28: CAP theorem bridge audit.

Outputs JSON to stdout.  Run from the repo root:

    python -m models.run_t28
"""

from __future__ import annotations

import json
import sys

from models.cap_theorem_bridge import run_cap_analysis


def main() -> None:
    print(json.dumps(run_cap_analysis(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
