"""Run the T11 compositional-finality laboratory."""

from __future__ import annotations

from dataclasses import asdict
import json

from models.compositional_finality import run_compositional_analysis


def serialize(value: object) -> object:
    if hasattr(value, "__dataclass_fields__"):
        return {key: serialize(item) for key, item in asdict(value).items()}
    if isinstance(value, dict):
        return {str(key): serialize(item) for key, item in value.items()}
    if isinstance(value, (tuple, list, frozenset, set)):
        return [serialize(item) for item in value]
    return value


def main() -> None:
    print(json.dumps(serialize(run_compositional_analysis()), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
