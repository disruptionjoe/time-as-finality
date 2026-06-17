"""Run the T16 dynamical phase-bearing record laboratory."""

from __future__ import annotations

from dataclasses import asdict, is_dataclass
import json

from models.t16_dynamical_phase_records import run_t16_analysis


def _json_default(value):
    if is_dataclass(value):
        return asdict(value)
    if isinstance(value, complex):
        return {"real": value.real, "imag": value.imag}
    if isinstance(value, frozenset | set | tuple):
        return list(value)
    raise TypeError(f"object of type {type(value).__name__} is not JSON serializable")


def main() -> None:
    print(json.dumps(run_t16_analysis(), indent=2, default=_json_default))


if __name__ == "__main__":
    main()
