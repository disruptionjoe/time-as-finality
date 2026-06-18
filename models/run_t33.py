"""Runner for T33: PO1 foundational derivation analysis."""

from __future__ import annotations

import json
import pathlib

from models.po1_foundational_derivation import run_t33_analysis, t33_result_to_dict


def run_t33() -> None:
    result = run_t33_analysis()
    output = t33_result_to_dict(result)

    out_path = pathlib.Path("results") / "po1-foundational-derivation-v0.1.json"
    out_path.parent.mkdir(exist_ok=True)
    out_path.write_text(json.dumps(output, indent=2), encoding="utf-8")

    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    run_t33()
