"""Runner for T158 preserved-target gate."""

from __future__ import annotations

import json

from models.weak_measurement_preserved_target_gate import (
    run_t158_analysis,
    t158_result_to_dict,
)


if __name__ == "__main__":
    print(json.dumps(t158_result_to_dict(run_t158_analysis()), indent=2))
