"""Runner for T32 PO1 admissibility derivation audit.

Outputs JSON to stdout. Run from the repo root:

    python -m models.run_t32
"""

from __future__ import annotations

import json

from models.po1_admissibility_derivation import run_t32_analysis


def main() -> None:
    print(json.dumps(run_t32_analysis(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
