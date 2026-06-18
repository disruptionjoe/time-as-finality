"""Runner for T34: Chained projection analysis."""

import json
import pathlib

from models.po1_chained_projection import run_t34_analysis, t34_result_to_dict


def run_t34() -> None:
    result = run_t34_analysis()
    output = t34_result_to_dict(result)
    out_path = pathlib.Path("results") / "po1-chained-projection-v0.1.json"
    out_path.parent.mkdir(exist_ok=True)
    out_path.write_text(json.dumps(output, indent=2), encoding="utf-8")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    run_t34()
