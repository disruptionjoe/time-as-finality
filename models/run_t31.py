"""Runner for T31: PO1 admissibility conditions audit.

Outputs JSON to stdout.  Run from the repo root:

    python -m models.run_t31
"""

from __future__ import annotations

import json

from models.po1_admissibility_conditions import run_t31_analysis


def main() -> None:
    print(json.dumps(run_t31_analysis(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
