"""Runner for T36: Compression-Finality Crosswalk."""

import json
import pathlib

from models.compression_finality_lab import (
    compression_finality_result_to_dict,
    run_compression_finality_analysis,
)


def run_t36() -> None:
    result = run_compression_finality_analysis()
    output = compression_finality_result_to_dict(result)
    out_path = pathlib.Path("results") / "compression-finality-crosswalk-v0.1.json"
    out_path.parent.mkdir(exist_ok=True)
    out_path.write_text(json.dumps(output, indent=2), encoding="utf-8")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    run_t36()
