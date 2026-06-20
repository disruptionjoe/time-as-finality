"""Write T67 results to disk."""

from __future__ import annotations

import json
from pathlib import Path

from models.povm_correlation_provenance_obstruction import (
    run_t67_analysis,
    t67_result_to_dict,
)


RESULTS_JSON = Path("results/povm-correlation-provenance-obstruction-v0.1.json")
RESULTS_MD = Path("results/povm-correlation-provenance-obstruction-v0.1-results.md")


def main() -> None:
    result = run_t67_analysis()
    payload = t67_result_to_dict(result)
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    overlap = payload["overlap_witness"]
    agreement_audit = payload["best_agreement_threshold_audit"]
    phi_audit = payload["best_phi_threshold_audit"]
    return "\n".join(
        [
            "# T67 Results: Correlation Provenance Obstruction",
            "",
            f"Strongest claim: {payload['strongest_claim']}",
            "",
            f"Weakened claim: {payload['weakened_claim']}",
            "",
            "## Exact-overlap witness",
            "",
            (
                f"- dependent scenario: {overlap['dependent_scenario']}; "
                f"independent scenario: {overlap['independent_scenario']}; "
                f"agreement gap: {overlap['agreement_gap']}; "
                f"phi gap: {overlap['phi_gap']}"
            ),
            f"- interpretation: {overlap['interpretation']}",
            "",
            "## Best scalar-threshold audits",
            "",
            (
                f"- agreement: threshold={agreement_audit['threshold']}, "
                f"orientation={agreement_audit['orientation']}, "
                f"errors={agreement_audit['error_count']}, "
                f"misclassified={agreement_audit['misclassified']}"
            ),
            (
                f"- phi: threshold={phi_audit['threshold']}, "
                f"orientation={phi_audit['orientation']}, "
                f"errors={phi_audit['error_count']}, "
                f"misclassified={phi_audit['misclassified']}"
            ),
            "",
            "## Next move",
            "",
            payload["recommended_next"],
            "",
        ]
    )


if __name__ == "__main__":
    main()
