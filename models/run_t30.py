"""Runner for T30 hostile cross-domain PO1 validation.

Outputs JSON to stdout. Run from the repo root:

    python -m models.run_t30
"""

from __future__ import annotations

import json

from models.cross_domain_projection_obstruction_validation import run_t30_analysis


def main() -> None:
    print(json.dumps(run_t30_analysis(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
