"""Run the T24 multiscale observer-field audit."""

from __future__ import annotations

import json

from models.multiscale_observer_field import run_t24_analysis


def main() -> None:
    print(json.dumps(run_t24_analysis(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
