"""Runner for T146."""

from __future__ import annotations

import json

from models.weak_measurement_escape_architecture_gate import (
    run_t146_analysis,
    t146_result_to_dict,
)


if __name__ == "__main__":
    print(json.dumps(t146_result_to_dict(run_t146_analysis()), indent=2))
