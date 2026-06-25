"""Run G10 hostile absorber stress fixture."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from models.s6_g10_hostile_absorber_stress import (
    run_g10_hostile_absorber_stress,
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, help="Optional JSON output path.")
    args = parser.parse_args()

    result = run_g10_hostile_absorber_stress()
    payload = json.dumps(result, indent=2, sort_keys=True)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload + "\n", encoding="utf-8")
    print(payload)


if __name__ == "__main__":
    main()
