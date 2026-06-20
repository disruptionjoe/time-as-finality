"""Write T106 bounded-sink reversible-compression results to disk."""

from __future__ import annotations

import json
from pathlib import Path

from models.bounded_sink_reversible_compression import (
    run_t106_analysis,
    t106_result_to_dict,
)


RESULTS_JSON = Path("results/bounded-sink-reversible-compression-v0.1.json")
RESULTS_MD = Path("results/bounded-sink-reversible-compression-v0.1-results.md")


def main() -> None:
    payload = t106_result_to_dict(run_t106_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    bounded = payload["bounded_rle_capacity_audit"]
    exact = payload["exact_rle_capacity_audit"]
    maps = payload["compression_map_audit"]
    cycle = payload["closed_cycle_audit"]
    ordered = maps["ordered_stack_map"]
    orderless = maps["orderless_counter_map"]

    lines = [
        "# T106 Results: Bounded-Sink Reversible Compression",
        "",
        "## Strongest claim",
        "",
        payload["strongest_claim"],
        "",
        "## T80/T84 sequence",
        "",
        f"- Observed masks: `{payload['observations']}`",
        f"- Exported overwritten slots: `{payload['exported_slots']}`",
        f"- Local ring support: `{payload['local_ring_support']}`",
        f"- Exported support: `{payload['exported_support']}`",
        f"- Accounted support: `{payload['accounted_support']}`",
        "",
        "## Compression and sink audits",
        "",
        "| Audit | Verdict | Key data |",
        "| --- | --- | --- |",
        (
            "| Undersized RLE sink | "
            f"{bounded['verdict']} | "
            f"capacity `{bounded['capacity_blocks']}`, required "
            f"`{bounded['required_blocks']}`, exhausted index "
            f"`{bounded['first_exhausted_export_index']}` |"
        ),
        (
            "| Exact RLE sink | "
            f"{exact['verdict']} | "
            f"capacity `{exact['capacity_blocks']}`, block counts "
            f"`{exact['block_count_sequence']}` |"
        ),
        (
            "| Ordered stack export | reversible only with blank sink slots | "
            f"injective `{ordered['injective']}`, lost bits "
            f"`{ordered['lost_bits']}` |"
        ),
        (
            "| Orderless counter compression | merges histories | "
            f"injective `{orderless['injective']}`, max preimages "
            f"`{orderless['maximum_preimages']}`, lost bits "
            f"`{orderless['lost_bits']}` |"
        ),
        "",
        "## Closed bounded cycle",
        "",
        f"- Forward accounted support: `{cycle['forward_accounted_support']}`",
        f"- Full-cycle accounted support: `{cycle['full_cycle_accounted_support']}`",
        f"- Forward accounted monotone: `{cycle['forward_accounted_monotone']}`",
        f"- Full-cycle accounted monotone: `{cycle['full_cycle_accounted_monotone']}`",
        f"- Strict cycle monotone possible: `{cycle['strict_cycle_monotone_possible']}`",
        "",
        cycle["verdict"],
        "",
        "## What this improved",
        "",
        payload["improved"],
        "",
        "## What this weakened",
        "",
        payload["weakened"],
        "",
        "## Falsification condition",
        "",
        payload["falsification_condition"],
        "",
        "## H7 update",
        "",
        payload["h7_update"],
        "",
        "## Claim ledger update",
        "",
        payload["claim_ledger_update"],
        "",
        "## Open blocker",
        "",
        payload["open_blocker"],
        "",
        "## Recommended next",
        "",
        payload["recommended_next"],
        "",
    ]
    return "\n".join(str(line) for line in lines)


if __name__ == "__main__":
    main()
